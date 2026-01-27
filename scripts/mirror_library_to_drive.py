#!/usr/bin/env python3
"""Mirror the `data/` library to Google Drive as styled PDFs.

What it does
- Converts every Markdown file under `data/` into a clean, styled PDF.
- Mirrors the folder structure into a dedicated Google Drive folder.
- Uploads PDFs, updating existing ones by name.

Why Playwright?
- It renders HTML/CSS via headless Chromium, giving much better styling fidelity
  than pure-Python PDF builders, and it behaves consistently on Windows.

Prereqs
- `pip install markdown jinja2 playwright google-api-python-client google-auth`
- `python -m playwright install chromium`

Auth
- Recommended: service account JSON + a Drive folder shared to that service account.

Examples
  Dry-run (no uploads; shows planned actions):
    python scripts/mirror_library_to_drive.py \
      --drive-root-id "<FOLDER_ID>" \
      --service-account-json "secrets/service_account.json" \
      --dry-run

  Real sync:
    python scripts/mirror_library_to_drive.py \
      --drive-root-id "<FOLDER_ID>" \
      --service-account-json "secrets/service_account.json"

"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import re
import html as _html
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, Optional


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = REPO_ROOT / "data"
OUTPUT_ROOT_DEFAULT = REPO_ROOT / "output" / "library_pdf_mirror"
CACHE_DIR = REPO_ROOT / ".cache"

SECRETS_DIR = REPO_ROOT / "secrets"

ASSETS_DIR = Path(__file__).resolve().parent / "assets"
DEFAULT_CSS_PATH = ASSETS_DIR / "pdf.css"
DEFAULT_TEMPLATE_PATH = ASSETS_DIR / "template.html"

DEFAULT_ENV_PATH = SECRETS_DIR / "google_drive.env"


def _load_simple_env(path: Path) -> dict[str, str]:
    """Load a minimal KEY=VALUE env file.

    - Ignores blank lines and comments starting with '#'
    - Supports optional surrounding quotes for values
    """

    if not path.exists():
        return {}

    out: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        key = k.strip()
        val = v.strip().strip('"').strip("'")
        if key:
            out[key] = val
    return out


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _safe_mkdir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def _path_to_file_uri(path: Path) -> str:
    return path.resolve().as_uri()


def _extract_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            return m.group(1).strip()
    return fallback


def _rewrite_relative_urls(html: str, base_dir: Path) -> str:
    """Rewrite relative image/src/href to file:// URIs so Chromium can load them."""

    def repl_attr(match: re.Match[str]) -> str:
        attr = match.group(1)
        url = match.group(2)
        if url.startswith(("http://", "https://", "mailto:", "file://", "#")):
            return match.group(0)
        # Handle ./, ../ and plain relative
        abs_path = (base_dir / url).resolve()
        return f'{attr}="{_path_to_file_uri(abs_path)}"'

    # src="..." and href="..."
    html = re.sub(r'(src)="([^"]+)"', repl_attr, html)
    html = re.sub(r'(href)="([^"]+)"', repl_attr, html)
    return html


def _convert_internal_md_links_to_reference_text(body_html: str) -> str:
    """Convert internal .md links to styled reference text (non-clickable).

    Internal library links don't work in PDFs viewed from Drive anyway.
    Instead, show them as styled document title references that readers
    can search for in the library.
    """

    # Match <a href="...something.md">Link Text</a>
    # Capture: full tag, href value, link text
    link_re = re.compile(
        r'<a\s+[^>]*href="(?P<href>[^"]*\.md(?:%20[^"]*)?(?:#[^"]*)?)"[^>]*>(?P<text>.*?)</a>',
        flags=re.IGNORECASE | re.DOTALL,
    )

    def repl(m: re.Match[str]) -> str:
        href = m.group("href")
        text = m.group("text").strip()

        # Skip external links (shouldn't match, but be safe)
        if href.startswith(("http://", "https://", "mailto:")):
            return m.group(0)

        # Use the link text as the reference title
        # Clean up any HTML tags inside the link text
        clean_text = re.sub(r"<[^>]+>", "", text).strip()
        if not clean_text:
            # Fallback: extract filename from href
            clean_text = href.split("/")[-1].replace("%20", " ").replace(".md", "")

        return f'<span class="internal-ref"><em>See:</em> {_html.escape(clean_text)}</span>'

    return link_re.sub(repl, body_html)


def _wrap_reference_section(body_html: str) -> str:
    """Wrap a References/Sources section in a div for bibliography-specific styling.

    Also handles Google Deep Research's Dutch heading "Geciteerd werk".
    Wraps the heading + following content until the next heading of the same or higher level.
    """

    titles = {
        "references",
        "works cited",
        "bibliography",
        "sources",
        "geciteerd werk",
        "geciteerde werken",
    }
    dutch_titles = {"geciteerd werk", "geciteerde werken"}

    # Match any heading level 2-6; title may be wrapped in tags like <strong>.
    heading_re = re.compile(
        r"<h(?P<level>[2-6])(?P<attrs>[^>]*)>(?P<inner>.*?)</h(?P=level)>",
        flags=re.IGNORECASE | re.DOTALL,
    )

    for m in heading_re.finditer(body_html):
        inner_html = m.group("inner")
        inner_text = re.sub(r"<[^>]+>", "", inner_html)
        norm = re.sub(r"\s+", " ", inner_text).strip().lower()
        if norm not in titles:
            continue

        level = int(m.group("level"))
        start = m.start()
        after_heading = m.end()

        # Find the next heading of same or higher level.
        next_heading_re = re.compile(r"<h([2-6])\b", flags=re.IGNORECASE)
        end = len(body_html)
        for m2 in next_heading_re.finditer(body_html, pos=after_heading):
            next_level = int(m2.group(1))
            if next_level <= level:
                end = m2.start()
                break

        section_html = body_html[start:end]

        # Normalize Dutch heading to English in the PDF output.
        if norm in dutch_titles:
            # Replace the *first* heading tag in the section.
            section_html = heading_re.sub(
                lambda mm: f"<h{mm.group('level')}{mm.group('attrs')}>References</h{mm.group('level')}>",
                section_html,
                count=1,
            )

        wrapped = (
            body_html[:start]
            + '<div class="references-section">'
            + section_html
            + "</div>"
            + body_html[end:]
        )
        return wrapped

    return body_html


def _postprocess_references_section(html_doc: str) -> str:
    """Improve readability of long, auto-generated reference lists.

    - Linkify bare URLs inside references-section.
    - Insert a line break before long URLs when preceded by comma/space.
    """

    m = re.search(r'<div class="references-section">', html_doc, flags=re.IGNORECASE)
    if not m:
        return html_doc

    # Find end of div (non-nested in our generation) by last occurrence after start.
    start = m.start()
    end = html_doc.find("</div>", m.end())
    if end == -1:
        return html_doc
    end += len("</div>")

    block = html_doc[start:end]

    # Linkify bare URLs (not already inside an href attribute).
    url_re = re.compile(r"(?<![\"'=])(https?://[^\s<]+)")

    def linkify(match: re.Match[str]) -> str:
        url = match.group(1)
        href = _html.escape(url, quote=True)
        return f'<a href="{href}">{_html.escape(url)}</a>'

    block = url_re.sub(linkify, block)

    # Break before URLs when they follow a comma.
    block = re.sub(
        r",\s*(<a href=\"https?://[^\"]+\">https?://[^<]+</a>)",
        r"<br/><span class=\"ref-url\">\1</span>",
        block,
    )

    # Any remaining links in the references section get URL styling.
    block = re.sub(
        r"(<a href=\"https?://[^\"]+\">https?://[^<]+</a>)",
        r"<span class=\"ref-url\">\1</span>",
        block,
    )

    # GDR-style inline bibliography often comes as a single paragraph: "1. ... url 2. ... url ...".
    # Force the numbered items onto separate lines for readability.
    block = re.sub(
        r"(</span>\s*)(\d{1,3})\.\s+",
        r"\1<br/><span class=\"ref-item-num\">\2.</span> ",
        block,
    )
    block = re.sub(
        r"(</a>\s*)(\d{1,3})\.\s+",
        r"\1<br/><span class=\"ref-item-num\">\2.</span> ",
        block,
    )

    return html_doc[:start] + block + html_doc[end:]


def render_markdown_to_html(md_path: Path, css_text: str, template_text: str) -> str:
    import markdown as md
    from jinja2 import Template

    md_text = md_path.read_text(encoding="utf-8")
    title = _extract_title(md_text, fallback=md_path.stem)

    body_html = md.markdown(
        md_text,
        extensions=[
            "extra",  # tables, fenced_code, etc.
            "toc",
            "footnotes",
            "sane_lists",
        ],
        output_format="html",
    )

    # Convert internal .md links to styled reference text (titles only, not clickable)
    body_html = _convert_internal_md_links_to_reference_text(body_html)

    body_html = _rewrite_relative_urls(body_html, base_dir=md_path.parent)
    body_html = _wrap_reference_section(body_html)
    body_html = _postprocess_references_section(body_html)

    template = Template(template_text)
    return template.render(title=title, css=css_text, body_html=body_html)


async def html_to_pdf(html: str, pdf_path: Path) -> None:
    from playwright.async_api import async_playwright

    _safe_mkdir(pdf_path.parent)

    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch()
        except Exception as e:
            msg = str(e)
            if "playwright install" in msg or "Executable doesn't exist" in msg:
                raise SystemExit(
                    "Playwright Chromium is not installed. Run: `python -m playwright install chromium`"
                ) from e
            raise
        page = await browser.new_page()
        await page.set_content(html, wait_until="networkidle")
        await page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "20mm", "bottom": "20mm", "left": "18mm", "right": "18mm"},
        )
        await browser.close()


@dataclass(frozen=True)
class BuildRecord:
    md_sha256: str
    css_sha256: str
    template_sha256: str


def _load_build_index(path: Path) -> Dict[str, BuildRecord]:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    out: Dict[str, BuildRecord] = {}
    for rel, rec in data.items():
        out[rel] = BuildRecord(
            md_sha256=rec["md_sha256"],
            css_sha256=rec["css_sha256"],
            template_sha256=rec["template_sha256"],
        )
    return out


def _save_build_index(path: Path, index: Dict[str, BuildRecord]) -> None:
    _safe_mkdir(path.parent)
    data = {
        rel: {
            "md_sha256": rec.md_sha256,
            "css_sha256": rec.css_sha256,
            "template_sha256": rec.template_sha256,
        }
        for rel, rec in index.items()
    }
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def iter_markdown_files(data_root: Path) -> Iterable[Path]:
    for path in sorted(data_root.rglob("*.md")):
        # skip obvious non-library artifacts if you add any later
        if path.name.lower().startswith("readme"):
            continue
        yield path


def _resolve_only_paths(data_root: Path, only: list[str]) -> list[Path]:
    resolved: list[Path] = []
    for rel in only:
        rel_clean = rel.replace("\\", "/").lstrip("/")
        p = (data_root / rel_clean).resolve()
        # Ensure it stays inside data_root
        try:
            p.relative_to(data_root.resolve())
        except Exception as e:
            raise SystemExit(f"--only path must be under data/: {rel}") from e
        if not p.exists():
            raise SystemExit(f"--only file not found: {p}")
        if p.suffix.lower() != ".md":
            raise SystemExit(f"--only must point to a .md file: {p}")
        resolved.append(p)
    return resolved


def md_to_pdf_path(md_path: Path, data_root: Path, output_root: Path) -> Path:
    rel = md_path.relative_to(data_root)
    return (output_root / rel).with_suffix(".pdf")


def build_pdfs(
    *,
    data_root: Path,
    output_root: Path,
    css_path: Path,
    template_path: Path,
    limit: Optional[int],
    force: bool,
    only: Optional[list[Path]] = None,
) -> list[Path]:
    css_text = css_path.read_text(encoding="utf-8")
    template_text = template_path.read_text(encoding="utf-8")

    css_sha = _sha256_file(css_path)
    template_sha = _sha256_file(template_path)

    index_path = CACHE_DIR / "pdf_build_index.json"
    index = _load_build_index(index_path)

    built: list[Path] = []
    md_files = list(only) if only else list(iter_markdown_files(data_root))
    if limit is not None:
        md_files = md_files[:limit]

    for md_path in md_files:
        rel = md_path.relative_to(data_root).as_posix()
        pdf_path = md_to_pdf_path(md_path, data_root, output_root)

        md_sha = _sha256_file(md_path)
        rec = index.get(rel)
        up_to_date = (
            rec is not None
            and rec.md_sha256 == md_sha
            and rec.css_sha256 == css_sha
            and rec.template_sha256 == template_sha
            and pdf_path.exists()
        )

        if up_to_date and not force:
            continue

        html = render_markdown_to_html(md_path, css_text=css_text, template_text=template_text)
        asyncio.run(html_to_pdf(html, pdf_path))

        index[rel] = BuildRecord(md_sha256=md_sha, css_sha256=css_sha, template_sha256=template_sha)
        built.append(pdf_path)

    _save_build_index(index_path, index)
    return built


def stream_build_and_upload(
    *,
    data_root: Path,
    output_root: Path,
    css_path: Path,
    template_path: Path,
    drive_root_id: str,
    auth_mode: str,
    service_account_json: Optional[Path],
    oauth_client_json: Optional[Path],
    oauth_token_json: Optional[Path],
    limit: Optional[int],
    force: bool,
    dry_run: bool,
    delete_remote_extras: bool,
    only: Optional[list[Path]] = None,
) -> tuple[int, int]:
    """Build and upload each file immediately instead of batch processing.
    
    Returns (built_count, uploaded_count).
    """
    css_text = css_path.read_text(encoding="utf-8")
    template_text = template_path.read_text(encoding="utf-8")

    css_sha = _sha256_file(css_path)
    template_sha = _sha256_file(template_path)

    index_path = CACHE_DIR / "pdf_build_index.json"
    index = _load_build_index(index_path)

    # Initialize Drive service once
    if auth_mode == "service-account":
        if service_account_json is None:
            raise SystemExit("--service-account-json is required for --auth service-account")
        service = _drive_service_from_service_account(service_account_json)
    elif auth_mode == "oauth":
        if oauth_client_json is None:
            raise SystemExit("--oauth-client-json is required for --auth oauth")
        token_path = oauth_token_json or (SECRETS_DIR / "google_drive_token.json")
        service = _drive_service_from_user_oauth(oauth_client_json, token_path)
    else:
        raise SystemExit(f"Unknown auth mode: {auth_mode}")

    folder_cache: dict[str, str] = {"": drive_root_id}
    desired_pdf_paths: set[str] = set()

    md_files = list(only) if only else list(iter_markdown_files(data_root))
    if limit is not None:
        md_files = md_files[:limit]

    built_count = 0
    uploaded_count = 0
    total = len(md_files)

    for i, md_path in enumerate(md_files, 1):
        rel = md_path.relative_to(data_root).as_posix()
        pdf_path = md_to_pdf_path(md_path, data_root, output_root)
        pdf_rel = pdf_path.relative_to(output_root)
        desired_pdf_paths.add(pdf_rel.as_posix())

        md_sha = _sha256_file(md_path)
        rec = index.get(rel)
        up_to_date = (
            rec is not None
            and rec.md_sha256 == md_sha
            and rec.css_sha256 == css_sha
            and rec.template_sha256 == template_sha
            and pdf_path.exists()
        )

        file_name = md_path.stem + ".pdf"
        status_prefix = f"[{i}/{total}] {rel}"

        # Build PDF if needed
        if up_to_date and not force:
            print(f"{status_prefix} - cached")
        else:
            print(f"{status_prefix} - building...", end=" ", flush=True)
            html = render_markdown_to_html(md_path, css_text=css_text, template_text=template_text)
            asyncio.run(html_to_pdf(html, pdf_path))
            index[rel] = BuildRecord(md_sha256=md_sha, css_sha256=css_sha, template_sha256=template_sha)
            _save_build_index(index_path, index)  # Save after each build
            built_count += 1
            print("done", end=" ", flush=True)

        # Upload to Drive
        parts = list(pdf_rel.parts)
        file_name = parts.pop(-1)

        # Ensure folder chain
        rel_folder = ""
        parent_id = drive_root_id
        for part in parts:
            rel_folder = f"{rel_folder}/{part}" if rel_folder else part
            if rel_folder in folder_cache:
                parent_id = folder_cache[rel_folder]
                continue
            try:
                parent_id = _drive_ensure_folder(service, parent_id, part, dry_run=dry_run)
            except Exception as e:
                friendly = _describe_http_error(e)
                if friendly:
                    raise SystemExit(friendly) from e
                raise
            folder_cache[rel_folder] = parent_id

        if not (up_to_date and not force):
            print("uploading...", end=" ", flush=True)
        _drive_upload_pdf(
            service,
            parent_id=parent_id,
            local_pdf=pdf_path,
            remote_name=file_name,
            dry_run=dry_run,
        )
        uploaded_count += 1
        if not (up_to_date and not force):
            print("✓")

    if delete_remote_extras:
        _delete_remote_extras(
            service,
            drive_root_id=drive_root_id,
            desired_pdf_paths=desired_pdf_paths,
            dry_run=dry_run,
        )

    return built_count, uploaded_count


def _drive_service_from_service_account(service_account_json: Path):
    from google.oauth2.service_account import Credentials
    from googleapiclient.discovery import build

    scopes = ["https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_file(str(service_account_json), scopes=scopes)
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def _drive_service_from_user_oauth(oauth_client_json: Path, token_json: Path):
    """Build a Drive service using OAuth user login.

    This uses an Installed App OAuth client (Desktop) JSON from Google Cloud.
    The first run will open a browser to authenticate and then persist a token.
    """

    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow

    scopes = ["https://www.googleapis.com/auth/drive"]

    creds: Any = None
    if token_json.exists():
        creds = Credentials.from_authorized_user_file(str(token_json), scopes=scopes)

    if creds and getattr(creds, "expired", False) and getattr(creds, "refresh_token", None):
        creds.refresh(Request())
    elif not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(str(oauth_client_json), scopes=scopes)
        creds = flow.run_local_server(port=0)

    if not creds:
        raise SystemExit("OAuth credentials could not be created")

    _safe_mkdir(token_json.parent)
    token_json.write_text(creds.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def _describe_http_error(e: Exception) -> Optional[str]:
    try:
        from googleapiclient.errors import HttpError

        if not isinstance(e, HttpError):
            return None
        # HttpError.content is bytes
        content = getattr(e, "content", b"")
        if isinstance(content, (bytes, bytearray)):
            text = content.decode("utf-8", errors="replace")
        else:
            text = str(content)

        if "accessNotConfigured" in text or "drive.googleapis.com" in text and "disabled" in text:
            return (
                "Google Drive API is not enabled for this OAuth project. "
                "Enable it in Google Cloud Console for the OAuth project, then retry."
            )
        return None
    except Exception:
        return None


def _drive_list_children(service, parent_id: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    page_token: Optional[str] = None
    while True:
        resp = (
            service.files()
            .list(
                q=f"'{parent_id}' in parents and trashed=false",
                fields="nextPageToken, files(id, name, mimeType)",
                pageToken=page_token,
                pageSize=1000,
            )
            .execute()
        )
        items.extend(resp.get("files", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return items


def _drive_find_child(service, parent_id: str, name: str, mime_type: Optional[str] = None) -> Optional[dict[str, Any]]:
    children = _drive_list_children(service, parent_id)
    for item in children:
        if item.get("name") != name:
            continue
        if mime_type and item.get("mimeType") != mime_type:
            continue
        return item
    return None


def _drive_ensure_folder(service, parent_id: str, folder_name: str, dry_run: bool) -> str:
    FOLDER_MIME = "application/vnd.google-apps.folder"
    if dry_run:
        # In dry-run, never touch Drive. Return a deterministic placeholder id.
        # This id must not be used for API calls.
        digest = hashlib.sha256(f"{parent_id}/{folder_name}".encode("utf-8")).hexdigest()[:12]
        return f"DRY_RUN_FOLDER_{digest}"

    found = _drive_find_child(service, parent_id, folder_name, mime_type=FOLDER_MIME)
    if found:
        return found["id"]

    if dry_run:
        return "DRY_RUN_FOLDER_ID"

    metadata = {"name": folder_name, "mimeType": FOLDER_MIME, "parents": [parent_id]}
    created = service.files().create(body=metadata, fields="id").execute()
    return created["id"]


def _drive_upload_pdf(
    service,
    *,
    parent_id: str,
    local_pdf: Path,
    remote_name: str,
    dry_run: bool,
) -> None:
    from googleapiclient.http import MediaFileUpload
    if dry_run:
        return

    existing = _drive_find_child(service, parent_id, remote_name, mime_type="application/pdf")

    media = MediaFileUpload(str(local_pdf), mimetype="application/pdf", resumable=False)
    if existing:
        service.files().update(fileId=existing["id"], media_body=media).execute()
    else:
        body = {"name": remote_name, "parents": [parent_id]}
        service.files().create(body=body, media_body=media, fields="id").execute()


def sync_pdfs_to_drive(
    *,
    drive_root_id: str,
    auth_mode: str,
    service_account_json: Optional[Path],
    oauth_client_json: Optional[Path],
    oauth_token_json: Optional[Path],
    local_pdf_root: Path,
    data_root: Path,
    dry_run: bool,
    delete_remote_extras: bool,
    limit: Optional[int],
    only_rel_paths: Optional[list[str]] = None,
) -> int:
    if auth_mode == "service-account":
        if service_account_json is None:
            raise SystemExit("--service-account-json is required for --auth service-account")
        service = _drive_service_from_service_account(service_account_json)
    elif auth_mode == "oauth":
        if oauth_client_json is None:
            raise SystemExit("--oauth-client-json is required for --auth oauth")
        token_path = oauth_token_json or (SECRETS_DIR / "google_drive_token.json")
        service = _drive_service_from_user_oauth(oauth_client_json, token_path)
    else:
        raise SystemExit(f"Unknown auth mode: {auth_mode}")

    if only_rel_paths:
        pdf_files = [local_pdf_root / Path(p).with_suffix(".pdf") for p in only_rel_paths]
    else:
        pdf_files = sorted(local_pdf_root.rglob("*.pdf"))
    if limit is not None:
        pdf_files = pdf_files[:limit]

    uploaded = 0

    folder_cache: dict[str, str] = {"": drive_root_id}

    desired_pdf_paths: set[str] = set()

    for pdf_path in pdf_files:
        rel = pdf_path.relative_to(local_pdf_root)
        desired_pdf_paths.add(rel.as_posix())
        parts = list(rel.parts)
        file_name = parts.pop(-1)

        # ensure folder chain
        rel_folder = ""
        parent_id = drive_root_id
        for part in parts:
            rel_folder = f"{rel_folder}/{part}" if rel_folder else part
            if rel_folder in folder_cache:
                parent_id = folder_cache[rel_folder]
                continue
            try:
                parent_id = _drive_ensure_folder(service, parent_id, part, dry_run=dry_run)
            except Exception as e:
                friendly = _describe_http_error(e)
                if friendly:
                    raise SystemExit(friendly) from e
                raise
            folder_cache[rel_folder] = parent_id

        _drive_upload_pdf(
            service,
            parent_id=parent_id,
            local_pdf=pdf_path,
            remote_name=file_name,
            dry_run=dry_run,
        )
        uploaded += 1

    if delete_remote_extras:
        _delete_remote_extras(
            service,
            drive_root_id=drive_root_id,
            desired_pdf_paths=desired_pdf_paths,
            dry_run=dry_run,
        )

    return uploaded


def _delete_remote_extras(
    service,
    *,
    drive_root_id: str,
    desired_pdf_paths: set[str],
    dry_run: bool,
) -> None:
    """Delete remote PDFs (and then empty folders) that aren't in the local mirror.

    Safety:
    - Only deletes PDFs under the mirror root.
    - Deletes folders only if they become empty.
    """

    FOLDER_MIME = "application/vnd.google-apps.folder"
    PDF_MIME = "application/pdf"

    # Collect remote tree
    remote_pdfs: dict[str, str] = {}  # rel_path -> fileId
    remote_folders: list[tuple[str, str]] = []  # (rel_folder, folderId)

    def walk_folder(folder_id: str, rel_prefix: str) -> None:
        children = _drive_list_children(service, folder_id)
        for item in children:
            name = item.get("name")
            mime = item.get("mimeType")
            item_id = item.get("id")
            if not name or not mime or not item_id:
                continue

            rel_path = f"{rel_prefix}/{name}" if rel_prefix else name
            if mime == FOLDER_MIME:
                remote_folders.append((rel_path, item_id))
                walk_folder(item_id, rel_path)
            elif mime == PDF_MIME:
                remote_pdfs[rel_path] = item_id

    walk_folder(drive_root_id, "")

    # Delete PDFs not present locally
    extras = sorted(set(remote_pdfs.keys()) - desired_pdf_paths)
    for rel_path in extras:
        if dry_run:
            continue
        service.files().delete(fileId=remote_pdfs[rel_path]).execute()

    # Delete empty folders bottom-up
    # Sort by path depth (deepest first)
    for rel_folder, folder_id in sorted(remote_folders, key=lambda t: t[0].count("/"), reverse=True):
        children = _drive_list_children(service, folder_id)
        if children:
            continue
        if dry_run:
            continue
        service.files().delete(fileId=folder_id).execute()


def main() -> None:
    parser = argparse.ArgumentParser(description="Mirror `data/` markdown files to Google Drive as PDFs")
    parser.add_argument(
        "--config-env",
        default=str(DEFAULT_ENV_PATH),
        help="Optional env file for local settings (default: secrets/google_drive.env)",
    )
    parser.add_argument(
        "--drive-root-id",
        required=False,
        default=None,
        help="Google Drive folder ID to mirror into (or set GOOGLE_DRIVE_ROOT_ID in secrets/google_drive.env)",
    )
    parser.add_argument(
        "--auth",
        default="oauth",
        choices=["oauth", "service-account"],
        help="Authentication mode. oauth = login with your Google account; service-account = service account JSON",
    )
    parser.add_argument(
        "--oauth-client-json",
        default=str(SECRETS_DIR / "google_drive_oauth_client.json"),
        help="Path to Google OAuth client JSON (Installed app / Desktop). Default: secrets/google_drive_oauth_client.json",
    )
    parser.add_argument(
        "--oauth-token-json",
        default=str(SECRETS_DIR / "google_drive_token.json"),
        help="Path to OAuth token cache JSON. Default: secrets/google_drive_token.json",
    )
    parser.add_argument(
        "--service-account-json",
        default=None,
        help="Path to service account JSON (Drive folder must be shared to that service account)",
    )
    parser.add_argument(
        "--output-root",
        default=str(OUTPUT_ROOT_DEFAULT),
        help=f"Local output root for generated PDFs (default: {OUTPUT_ROOT_DEFAULT})",
    )
    parser.add_argument("--css", default=str(DEFAULT_CSS_PATH), help="CSS file for PDF styling")
    parser.add_argument("--template", default=str(DEFAULT_TEMPLATE_PATH), help="HTML template file")
    parser.add_argument("--limit", type=int, default=None, help="Process only the first N files (for testing)")
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        help="Process only a specific markdown file (relative to data/). Can be repeated.",
    )
    parser.add_argument("--force", action="store_true", help="Rebuild PDFs even if unchanged")
    parser.add_argument("--dry-run", action="store_true", help="Do not create folders or upload files")
    parser.add_argument(
        "--auth-only",
        action="store_true",
        help="Only authenticate and cache tokens/credentials; do not build PDFs or touch Drive",
    )
    parser.add_argument(
        "--delete-remote-extras",
        action="store_true",
        help="Delete remote PDFs (and empty folders) that are not present locally under the mirror root",
    )

    args = parser.parse_args()

    config_env_path = Path(args.config_env) if args.config_env else None
    env_cfg: dict[str, str] = _load_simple_env(config_env_path) if config_env_path else {}

    drive_root_id = ((args.drive_root_id or "") or env_cfg.get("GOOGLE_DRIVE_ROOT_ID", "")).strip()
    if not drive_root_id and not args.auth_only:
        raise SystemExit(
            "Missing Drive folder id. Provide --drive-root-id or set GOOGLE_DRIVE_ROOT_ID in secrets/google_drive.env"
        )

    data_root = DATA_ROOT
    if not data_root.exists():
        raise SystemExit(f"data/ folder not found at {data_root}")

    _safe_mkdir(SECRETS_DIR)

    service_account_json: Optional[Path] = None
    if args.service_account_json:
        service_account_json = Path(args.service_account_json)
        if not service_account_json.exists():
            raise SystemExit(f"service account json not found: {service_account_json}")

    oauth_client_json = Path(args.oauth_client_json) if args.oauth_client_json else None
    oauth_token_json = Path(args.oauth_token_json) if args.oauth_token_json else None
    if args.auth == "oauth":
        if oauth_client_json is None or not oauth_client_json.exists():
            raise SystemExit(
                "OAuth client JSON not found. Create a Google Cloud OAuth client (Desktop) and save it to: "
                f"{oauth_client_json}"
            )

    if args.auth_only:
        # Validate credentials and cache token, then exit.
        try:
            if args.auth == "oauth":
                _drive_service_from_user_oauth(oauth_client_json, oauth_token_json)  # type: ignore[arg-type]
            else:
                if service_account_json is None:
                    raise SystemExit("--service-account-json is required for --auth service-account")
                _drive_service_from_service_account(service_account_json)
        except Exception as e:
            friendly = _describe_http_error(e)
            if friendly:
                raise SystemExit(friendly) from e
            raise
        print("Auth OK")
        return

    output_root = Path(args.output_root)
    css_path = Path(args.css)
    template_path = Path(args.template)

    only_files: Optional[list[Path]] = None
    only_rel_paths: Optional[list[str]] = None
    if args.only:
        only_files = _resolve_only_paths(data_root, args.only)
        only_rel_paths = [p.relative_to(data_root).as_posix() for p in only_files]

    # Stream mode: build and upload each file immediately instead of batch
    built, uploaded = stream_build_and_upload(
        data_root=data_root,
        output_root=output_root,
        css_path=css_path,
        template_path=template_path,
        drive_root_id=drive_root_id,
        auth_mode=args.auth,
        service_account_json=service_account_json,
        oauth_client_json=oauth_client_json,
        oauth_token_json=oauth_token_json,
        limit=args.limit,
        force=args.force,
        dry_run=args.dry_run,
        delete_remote_extras=args.delete_remote_extras,
        only=only_files,
    )

    print(f"PDFs built: {built}")
    print(f"PDFs synced: {uploaded}{' (dry-run)' if args.dry_run else ''}")


if __name__ == "__main__":
    main()
