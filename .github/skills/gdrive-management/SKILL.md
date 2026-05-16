---
name: gdrive-management
description: "Manage Google Drive sync for literary-compilation. Use when asked to mirror the library to Drive, build styled PDFs, sync data markdown, force rebuild PDFs, dry-run Drive sync, authenticate Google Drive, inspect gdrive settings, or use scripts/mirror_library_to_drive.py."
---

# Google Drive Library Mirror Management

## When To Use

Use this skill for `literary-compilation` tasks involving the Google Drive PDF mirror, especially:

- Building styled PDFs from Markdown files under `data/`.
- Syncing one document, a folder subset, or the whole library to Drive.
- Running a dry-run before an upload.
- Refreshing OAuth credentials or validating Drive authentication.
- Troubleshooting `scripts/mirror_library_to_drive.py`.
- Deciding whether to use `--only`, `--force`, `--dry-run`, or `--delete-remote-extras`.

This skill is for the library PDF mirror. It is not for large generated artifact archives from other repositories.

## Script

Use the repository script:

```powershell
python scripts/mirror_library_to_drive.py
```

The script converts Markdown files under `data/` into styled PDFs under:

```text
output/library_pdf_mirror/
```

Then it mirrors the PDF folder structure to the configured Google Drive folder.

Default auth files:

```text
secrets/google_drive_oauth_client.json
secrets/google_drive_token.json
secrets/google_drive.env
```

The Drive folder ID can be supplied with `--drive-root-id` or by setting `GOOGLE_DRIVE_ROOT_ID` in `secrets/google_drive.env`.

## Standard Workflow

1. Check Git status first, and do not touch unrelated user files:

   ```powershell
   git status --short --branch
   ```

2. For a single updated document, prefer `--only` with the path relative to `data/`:

   ```powershell
   python scripts/mirror_library_to_drive.py --only "03_Biblical_Scholarship/filename.md"
   ```

3. Force rebuild a single PDF when styling, template, links, or cached output may be stale:

   ```powershell
   python scripts/mirror_library_to_drive.py --only "path/to/file.md" --force
   ```

4. Dry-run before unfamiliar or broad changes:

   ```powershell
   python scripts/mirror_library_to_drive.py --only "path/to/file.md" --dry-run
   ```

5. Sync the whole library only when intended, because it can be slow:

   ```powershell
   python scripts/mirror_library_to_drive.py
   ```

6. Authenticate without building or uploading:

   ```powershell
   python scripts/mirror_library_to_drive.py --auth-only
   ```

## Path Rules

- `--only` paths are relative to `data/`, not the repository root.
- `--only` must point to a Markdown file.
- Use forward slashes in paths for portability.
- The script validates that `--only` stays inside `data/`.

Examples:

```powershell
python scripts/mirror_library_to_drive.py --only "00_Master_Theses/Some Thesis.md" --force
python scripts/mirror_library_to_drive.py --only "08_Correspondential_Texts/Some Document.md" --dry-run
```

## Safety Rules

- Ask for explicit confirmation before using `--delete-remote-extras`.
- Do not use a broad full-library sync when a single `--only` sync will satisfy the request.
- Do not commit or inspect files under `secrets/` beyond checking whether required paths exist.
- Do not treat generated PDFs under `output/library_pdf_mirror/` as source material.
- If Drive API reports `accessNotConfigured`, tell the user the Google Drive API must be enabled for the OAuth project.

## Troubleshooting

If Chromium is missing:

```powershell
python -m playwright install chromium
```

If the script reports missing Drive folder ID, provide `--drive-root-id` or update:

```text
secrets/google_drive.env
```

If OAuth is expired or missing, run:

```powershell
python scripts/mirror_library_to_drive.py --auth-only
```

If a file is not found with `--only`, confirm the path is relative to `data/` and ends in `.md`.
