#!/usr/bin/env python3
"""Normalize Google Drive links in library Markdown to internal repo links.

Problem
- Some Deep Research–generated Markdown files cite other library docs using Google Drive URLs.
- We want those references to become stable internal links (relative paths within `data/`).

What this script does
- Scans `data/**/*.md` (or a subset) for Google Drive links.
- Uses the Google Drive API to resolve the Drive file ID to a filename.
- Matches that filename (and/or the anchor text) to a Markdown file in the local library.
- Rewrites the link target to a relative path to that Markdown file.

Notes
- By default this is a dry-run. Use `--apply` to write changes.
- This script does NOT modify the PDF mirroring behavior; it only normalizes Markdown.

Auth
- OAuth (recommended): uses cached token in `secrets/google_drive_token.json`
- Service account: requires sharing the relevant Drive content to the service account.

"""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional


def _href_escape(path: str) -> str:
    # Markdown/GitHub relative links need URL escaping for spaces.
    # We keep '/' intact and only escape spaces (most common failure case).
    return path.replace(" ", "%20")

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT_DEFAULT = REPO_ROOT / "data"
SECRETS_DIR = REPO_ROOT / "secrets"


def _safe_mkdir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def _extract_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            return m.group(1).strip()
    return fallback


def _norm(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[\u2018\u2019]", "'", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


@dataclass(frozen=True)
class LocalDoc:
    rel: str  # posix relative to data/
    title: str
    title_norm: str
    stem_norm: str


def build_local_index(data_root: Path) -> tuple[dict[str, list[LocalDoc]], dict[str, list[LocalDoc]]]:
    by_title: dict[str, list[LocalDoc]] = {}
    by_stem: dict[str, list[LocalDoc]] = {}

    for md_path in sorted(data_root.rglob("*.md")):
        if md_path.name.lower().startswith("readme"):
            continue
        rel = md_path.relative_to(data_root).as_posix()
        text = md_path.read_text(encoding="utf-8")
        title = _extract_title(text, fallback=md_path.stem)
        doc = LocalDoc(rel=rel, title=title, title_norm=_norm(title), stem_norm=_norm(md_path.stem))
        by_title.setdefault(doc.title_norm, []).append(doc)
        by_stem.setdefault(doc.stem_norm, []).append(doc)

    return by_title, by_stem


def _extract_drive_id(url: str) -> Optional[str]:
    # https://drive.google.com/open?id=<ID>
    m = re.search(r"[?&]id=([a-zA-Z0-9_-]{10,})", url)
    if m:
        return m.group(1)
    # https://drive.google.com/file/d/<ID>/view
    m = re.search(r"/file/d/([a-zA-Z0-9_-]{10,})", url)
    if m:
        return m.group(1)
    # https://drive.google.com/drive/folders/<ID>
    m = re.search(r"/drive/folders/([a-zA-Z0-9_-]{10,})", url)
    if m:
        return m.group(1)
    return None


def _drive_service_from_service_account(service_account_json: Path):
    from google.oauth2.service_account import Credentials
    from googleapiclient.discovery import build

    scopes = ["https://www.googleapis.com/auth/drive.readonly"]
    creds = Credentials.from_service_account_file(str(service_account_json), scopes=scopes)
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def _drive_service_from_user_oauth(oauth_client_json: Path, token_json: Path):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow

    scopes = ["https://www.googleapis.com/auth/drive.readonly"]

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


def drive_get_name(service, file_id: str) -> Optional[str]:
    try:
        meta = service.files().get(fileId=file_id, fields="id,name,mimeType").execute()
        if not isinstance(meta, dict):
            return None
        # skip folders
        if meta.get("mimeType") == "application/vnd.google-apps.folder":
            return None
        return meta.get("name")
    except Exception:
        return None


def resolve_target_rel(
    *,
    drive_name: str,
    anchor_text: Optional[str],
    by_title: dict[str, list[LocalDoc]],
    by_stem: dict[str, list[LocalDoc]],
) -> Optional[str]:
    # Prefer matching by anchor text title.
    if anchor_text:
        key = _norm(anchor_text)
        docs = by_title.get(key)
        if docs and len(docs) == 1:
            return docs[0].rel

    base = drive_name
    base = re.sub(r"\.(pdf|docx|doc|txt|md)$", "", base, flags=re.IGNORECASE)
    key = _norm(base)

    docs = by_title.get(key)
    if docs and len(docs) == 1:
        return docs[0].rel

    docs = by_stem.get(key)
    if docs and len(docs) == 1:
        return docs[0].rel

    # If ambiguous, refuse to guess.
    return None


def compute_rel_href(from_md: Path, to_md: Path) -> str:
    # Always produce a stable repo-internal relative link.
    return Path(os.path.relpath(to_md, start=from_md.parent)).as_posix()


def rewrite_markdown(
    *,
    md_path: Path,
    data_root: Path,
    service,
    by_title: dict[str, list[LocalDoc]],
    by_stem: dict[str, list[LocalDoc]],
    stats: dict[str, int],
) -> tuple[str, list[dict[str, Any]]]:
    """Return updated markdown text and per-change records."""

    text = md_path.read_text(encoding="utf-8")
    rel_self = md_path.relative_to(data_root).as_posix()

    changes: list[dict[str, Any]] = []
    drive_cache: dict[str, Optional[str]] = {}

    # 1) Rewrite markdown links [text](url)
    link_re = re.compile(r"\[(?P<txt>[^\]]+)\]\((?P<url>https?://[^)]+)\)")

    def repl_link(m: re.Match[str]) -> str:
        url = m.group("url")
        file_id = _extract_drive_id(url)
        if not file_id:
            return m.group(0)

        if file_id not in drive_cache:
            drive_cache[file_id] = drive_get_name(service, file_id)
        drive_name = drive_cache[file_id]
        if not drive_name:
            stats["drive_unresolved"] += 1
            return m.group(0)

        target_rel = resolve_target_rel(
            drive_name=drive_name,
            anchor_text=m.group("txt"),
            by_title=by_title,
            by_stem=by_stem,
        )
        if not target_rel:
            stats["local_unresolved"] += 1
            return m.group(0)

        target_abs = data_root / target_rel
        href = _href_escape(compute_rel_href(md_path, target_abs))
        changes.append(
            {
                "kind": "md_link",
                "from": rel_self,
                "text": m.group("txt"),
                "old": url,
                "new": href,
                "drive_id": file_id,
                "drive_name": drive_name,
                "target": target_rel,
            }
        )
        stats["rewritten"] += 1
        return f"[{m.group('txt')}]({href})"

    text2 = link_re.sub(repl_link, text)

    # 2) Rewrite GDR-style references lines: "1. Title, https://drive.google.com/open?id=..."
    ref_line_re = re.compile(
        r"^(?P<prefix>\s*\d+(?:\\\.)?)\s*(?P<title>[^\n,]+?),\s*(?P<url>https?://drive\.google\.com/[^\s]+)\s*$",
        flags=re.MULTILINE,
    )

    def repl_ref_line(m: re.Match[str]) -> str:
        url = m.group("url")
        file_id = _extract_drive_id(url)
        if not file_id:
            return m.group(0)

        if file_id not in drive_cache:
            drive_cache[file_id] = drive_get_name(service, file_id)
        drive_name = drive_cache[file_id]
        if not drive_name:
            stats["drive_unresolved"] += 1
            return m.group(0)

        target_rel = resolve_target_rel(
            drive_name=drive_name,
            anchor_text=m.group("title"),
            by_title=by_title,
            by_stem=by_stem,
        )
        if not target_rel:
            stats["local_unresolved"] += 1
            return m.group(0)

        target_abs = data_root / target_rel
        href = _href_escape(compute_rel_href(md_path, target_abs))

        changes.append(
            {
                "kind": "gdr_ref_line",
                "from": rel_self,
                "text": m.group("title"),
                "old": url,
                "new": href,
                "drive_id": file_id,
                "drive_name": drive_name,
                "target": target_rel,
            }
        )
        stats["rewritten"] += 1
        return f"{m.group('prefix')} [{m.group('title')}]({href})"

    text3 = ref_line_re.sub(repl_ref_line, text2)

    # 3) Rewrite inline GDR-style references where multiple items are on one line.
    # Example:
    #   "1. Some Title, https://drive.google.com/open?id=... 2. Other Title, https://drive..."
    inline_ref_re = re.compile(
        r"(?P<prefix>(?:^|\s)\d+(?:\\\.)?)\s*(?P<title>[^\n,]+?),\s*(?P<url>https?://drive\.google\.com/[^\s)]+)",
        flags=re.MULTILINE,
    )

    def repl_inline_ref(m: re.Match[str]) -> str:
        url = m.group("url")
        file_id = _extract_drive_id(url)
        if not file_id:
            return m.group(0)

        if file_id not in drive_cache:
            drive_cache[file_id] = drive_get_name(service, file_id)
        drive_name = drive_cache[file_id]
        if not drive_name:
            stats["drive_unresolved"] += 1
            return m.group(0)

        target_rel = resolve_target_rel(
            drive_name=drive_name,
            anchor_text=m.group("title"),
            by_title=by_title,
            by_stem=by_stem,
        )
        if not target_rel:
            stats["local_unresolved"] += 1
            return m.group(0)

        target_abs = data_root / target_rel
        href = _href_escape(compute_rel_href(md_path, target_abs))

        changes.append(
            {
                "kind": "gdr_inline_ref",
                "from": rel_self,
                "text": m.group("title"),
                "old": url,
                "new": href,
                "drive_id": file_id,
                "drive_name": drive_name,
                "target": target_rel,
            }
        )
        stats["rewritten"] += 1
        # Preserve leading whitespace (if any) by keeping prefix group verbatim.
        return f"{m.group('prefix')} [{m.group('title')}]({href})"

    text4 = inline_ref_re.sub(repl_inline_ref, text3)

    # 4) Ensure any internal .md links have URL-safe spaces.
    internal_md_link_re = re.compile(r"\]\((?!https?://)(?P<href>[^)]+\.md)\)", flags=re.IGNORECASE)

    def repl_internal_space(m: re.Match[str]) -> str:
        href = m.group("href")
        escaped = _href_escape(href)
        if escaped == href:
            return m.group(0)
        changes.append(
            {
                "kind": "escape_spaces",
                "from": rel_self,
                "old": href,
                "new": escaped,
            }
        )
        stats.setdefault("escaped", 0)
        stats["escaped"] += 1
        return f"]({escaped})"

    text5 = internal_md_link_re.sub(repl_internal_space, text4)

    if text5 != text:
        stats["files_changed"] += 1

    return text5, changes


def main() -> None:
    parser = argparse.ArgumentParser(description="Replace Google Drive links with internal library links")
    parser.add_argument("--data-root", default=str(DATA_ROOT_DEFAULT), help="Root of the library markdown (default: data/)")
    parser.add_argument(
        "--auth",
        default="oauth",
        choices=["oauth", "service-account"],
        help="Authentication mode. oauth uses your cached token; service-account uses a service account JSON",
    )
    parser.add_argument(
        "--oauth-client-json",
        default=str(SECRETS_DIR / "google_drive_oauth_client.json"),
        help="Path to OAuth client JSON (default: secrets/google_drive_oauth_client.json)",
    )
    parser.add_argument(
        "--oauth-token-json",
        default=str(SECRETS_DIR / "google_drive_token.json"),
        help="Path to OAuth token cache JSON (default: secrets/google_drive_token.json)",
    )
    parser.add_argument(
        "--service-account-json",
        default=None,
        help="Path to service account JSON (required when --auth service-account)",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        help="Only process one markdown file (relative to data/). Can be repeated.",
    )
    parser.add_argument("--limit", type=int, default=None, help="Process only first N markdown files (for testing)")
    parser.add_argument("--apply", action="store_true", help="Write changes to disk")
    parser.add_argument(
        "--report-json",
        default=None,
        help="Optional path to write a JSON report of replacements",
    )

    args = parser.parse_args()

    data_root = Path(args.data_root)
    if not data_root.exists():
        raise SystemExit(f"data root not found: {data_root}")

    by_title, by_stem = build_local_index(data_root)

    if args.auth == "service-account":
        if not args.service_account_json:
            raise SystemExit("--service-account-json is required for --auth service-account")
        sa = Path(args.service_account_json)
        if not sa.exists():
            raise SystemExit(f"service account json not found: {sa}")
        service = _drive_service_from_service_account(sa)
    else:
        client = Path(args.oauth_client_json)
        token = Path(args.oauth_token_json)
        if not client.exists():
            raise SystemExit(f"OAuth client JSON not found: {client}")
        # token may be created/refreshed
        service = _drive_service_from_user_oauth(client, token)

    md_paths: list[Path]
    if args.only:
        md_paths = []
        for rel in args.only:
            rel_clean = rel.replace("\\", "/").lstrip("/")
            p = (data_root / rel_clean).resolve()
            try:
                p.relative_to(data_root.resolve())
            except Exception as e:
                raise SystemExit(f"--only must be under data/: {rel}") from e
            if not p.exists():
                raise SystemExit(f"--only file not found: {p}")
            md_paths.append(p)
    else:
        md_paths = [p for p in sorted(data_root.rglob("*.md")) if not p.name.lower().startswith("readme")]

    if args.limit is not None:
        md_paths = md_paths[: args.limit]

    stats = {"files": 0, "files_changed": 0, "rewritten": 0, "drive_unresolved": 0, "local_unresolved": 0}
    report: dict[str, Any] = {"stats": stats, "changes": []}

    for md_path in md_paths:
        stats["files"] += 1
        updated, changes = rewrite_markdown(
            md_path=md_path,
            data_root=data_root,
            service=service,
            by_title=by_title,
            by_stem=by_stem,
            stats=stats,
        )

        if changes:
            report["changes"].extend(changes)
            if args.apply:
                md_path.write_text(updated, encoding="utf-8")

    if args.report_json:
        out = Path(args.report_json)
        _safe_mkdir(out.parent)
        out.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")

    print(
        " ".join(
            [
                f"files={stats['files']}",
                f"files_changed={stats['files_changed']}",
                f"rewritten={stats['rewritten']}",
                f"drive_unresolved={stats['drive_unresolved']}",
                f"local_unresolved={stats['local_unresolved']}",
            ]
        )
    )


if __name__ == "__main__":
    main()
