# Source & Claim Audit Ledger

**Purpose**: Running record of which `data/` documents have been fully audited, by the nightly job or by hand.
**Procedure**: [`NIGHTLY_SOURCE_AUDIT.md`](NIGHTLY_SOURCE_AUDIT.md)

This file is the job's memory. Each nightly run starts from nothing and reads this to know where the pass has reached. Rows are append-only — corrections to a row go in a new row, never by editing history.

---

## How to read this

| Column | Meaning |
|---|---|
| **Date** | Run date (YYYY-MM-DD) |
| **Document** | Path relative to `data/` |
| **Sources** | Citations checked / total citations found |
| **Corrections** | Fixed in place (F) · Annotated (A) · Flagged `[TRACE NEEDED]` (T) |
| **Propagated** | Files outside the batch that received the same correction |
| **Open** | Research questions logged |
| **Outcome** | `clean` · `corrected` · `partial` · `blocked` |

A document appears here only after a **complete** read and source pass. Files touched solely by correction propagation are listed in the **Propagated** column of the row that caused them — they are not themselves audited and remain in the queue.

---

## Progress

| Metric | Count |
|---|---|
| Documents in `data/` | 250 |
| Audited | 0 |
| Remaining | 250 |

Refresh the total with `find data -name "*.md" | wc -l`.

---

## Audited documents

| Date | Document | Sources | Corrections | Propagated | Open | Outcome |
|---|---|---|---|---|---|---|
| — | _No documents audited yet. First scheduled run: 2026-09-21._ | — | — | — | — | — |

---

## Run log

Narrative notes per run — what the batch surfaced, patterns worth knowing, anything a later run should be aware of. Newest first.

### 2026-09-20 — Ledger opened

Nightly audit configured. Queue is the full library: 250 documents, none audited.

Starting conditions worth noting for early runs:

- **83** documents carry a bibliography section; the rest cite inline or not at all
- **46** already carry an editorial header block
- **24** still contain `drive.google.com` links (`scripts/normalize_internal_links.py`)
- **2** use the `[P]`/`[S]`/`[T]`/`[E]`/`[W]` type codes from the Source Tracing Protocol — so type-coding will be a large share of early work
- `EVOLVING_CONCEPTUAL_STRAINS.md` has two open items: **#16** Pillar 43 Historical Encoding and **#26** Paleolithic Geometric Signs, both opened 2026-08-20 for corpus-wide re-audit

Priority order for selection is in the procedure, § 1.
