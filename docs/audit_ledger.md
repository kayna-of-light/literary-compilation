# Source & Claim Audit Ledger

**Purpose**: Running state for the source and claim audit of the `data/` library — what is done, what is in flight, and what the next run needs to know.
**Procedure**: [`NIGHTLY_SOURCE_AUDIT.md`](NIGHTLY_SOURCE_AUDIT.md)

Each nightly run starts as a fresh session with no memory of the last one. This file is the only thing that carries across. Treat it as the job's working memory, not as a report.

---

## Next run starts here

**Replaced wholesale at the end of every run.** This block describes the present, not the history — history goes in the run log below. A run that leaves this stale has failed its successor.

> **Status**: Not yet started. Queue is the full library.
>
> **Take next**: Your call — nothing is claimed yet, so the whole library is open. Procedure § 2 has signals worth checking and the constraints on the choice. Pick by what a document's state looks like, not by what it is about, and say in your row why you picked it.
>
> **Propagation debt**: None.
>
> **Awaiting external answers**: None.
>
> **Worth knowing**: Two `EVOLVING_CONCEPTUAL_STRAINS.md` items are open for corpus-wide re-audit, both from 2026-08-20 — **#16** Pillar 43 Historical Encoding (earlier annotations need replacing, not extending) and **#26** Paleolithic Geometric Signs. Worth knowing about when you meet a document that touches either; not an instruction to seek them out.
>
> `docs/BIBLIOGRAPHY_STANDARDS.md` was added 2026-09-21 and is now required reading alongside `CLAUDE.md` (procedure § 0). It replaces the old `[P]`/`[S]`/`[T]`/`[E]`/`[W]` type-code system with a categorized Works Cited format, and bans citing personally-hosted files (`drive.google.com`) or unmoderated/reposted sources (`reddit.com`, `scribd.com`, forum threads) as sources — the latter now confirmed at **over 90 documents corpus-wide**, the largest defect class found so far. No document has been brought into line with either rule yet.
>
> **This is the actual point of the job, not a secondary cleanup pass — read procedure § 3.4b before starting.** A document does not count as `corrected` until its *entire* Works Cited list meets the standard, not just the entries behind whichever claims got fact-checked. Given the scale just found, batch size may need to shrink from "a few documents" toward one document done thoroughly — a 20-entry bibliography with several Scribd reposts to track down is real research time. `partial` is an honest, expected outcome some nights; a document marked `corrected` with half its bibliography untouched is not.

---

## How to read the tables

| Column | Meaning |
|---|---|
| **Date** | Run date (YYYY-MM-DD) |
| **Document** | Path relative to `data/` |
| **Why** | Why this document was chosen — a few words is enough |
| **Sources** | Citations verified / total found |
| **Corrections** | Fixed in place (F) · Annotated (A) · Flagged `[TRACE NEEDED]` (T) |
| **Propagated** | Files outside the batch that received the same correction |
| **Open** | Research questions logged |
| **Outcome** | `in-progress` · `clean` · `corrected` · `partial` · `blocked` · `released` |

Batch selection is the run's own judgment (procedure § 2), so **Why** is not optional bookkeeping — it is what makes that judgment reviewable and correctable. A run that records what it chose but not why leaves the author nothing to steer by.

Rows are append-only — a later correction to a row goes in a new row, never by editing history. The one exception is flipping `in-progress` to a final outcome at the end of the run that claimed it.

A document counts as audited only after a **complete** read and source pass — and "complete" means the *entire* Works Cited list is brought into line with `docs/BIBLIOGRAPHY_STANDARDS.md`, not just the entries behind whichever claims got fact-checked that night (procedure § 3.4b). A document with five verified claims and ten untouched Scribd/Reddit citations is `partial`, never `corrected`. Files touched solely by correction propagation appear in the **Propagated** column of the row that caused them; they are not audited and stay in the queue.

**`in-progress` rows are claims.** A run writes them and pushes before auditing, so a session that dies leaves a visible trace instead of silently losing its work. A claim older than 48 hours with no open PR is a dead run: release those documents back to the queue with a `released` row and note the dead branch in the run log. Never resume someone else's claim — you cannot know how far it got.

---

## Progress

| Metric | Count |
|---|---|
| Documents in `data/` | 250 |
| Audited | 0 |
| In flight | 0 |
| Remaining | 250 |

Refresh the total with `find data -name "*.md" | wc -l`.

---

## Audited documents

| Date | Document | Why | Sources | Corrections | Propagated | Open | Outcome |
|---|---|---|---|---|---|---|---|
| — | _No documents audited yet. First scheduled run: 2026-09-21._ | — | — | — | — | — | — |

---

## Pattern register

Recurring defect classes and how to handle them. **This is what makes the job compound** — without it, night 8 rediscovers from scratch what night 3 already worked out, and handles it differently.

Add an entry when a problem looks like it will recur. Update the existing entry rather than adding a near-duplicate.

| Pattern | What it looks like | Handling | Seen in |
|---|---|---|---|
| Personal Drive PDF cited as a source | A `## Works Cited` (or raw numbered list) entry linking `drive.google.com`, naming a file like `experiences_part-024.pdf` or a personal scan of a published work | Never leave standing. Publication → cite it properly under Primary/Scholarly. Belongs in this repo → Internal Library Document, relative link. Neither → `[TRACE NEEDED]` + research question. Full routing: `docs/BIBLIOGRAPHY_STANDARDS.md`. | 35 documents confirmed by grep at the standard's introduction (2026-09-21); not yet remediated |
| Reddit / Scribd / other unmoderated or reposted sources | A Works Cited entry linking `reddit.com` (a forum post treated as if it were evidence for a claim) or `scribd.com` (a reuploaded document with no attribution to the real original) | Never a citation in itself. Scribd etc.: find and cite the actual underlying publication. Reddit etc.: find independent verification for the claim and cite that, or `[TRACE NEEDED]` if none exists — the forum post is never the fix, even reformatted. Full routing: `docs/BIBLIOGRAPHY_STANDARDS.md` § "No unmoderated or reposted sources." | **Over 90 documents corpus-wide** confirmed by grep (2026-09-21) — this is the largest single defect class found so far, larger than the Drive-link pattern above. Budget for it explicitly; do not assume a document is close to done because its inline claims check out. |

Candidates to watch for in early runs, from the corpus's history — confirm before treating any as established:

- Much of this library came out of Gemini Deep Research. Generated bibliographies are the usual place fabricated or subtly wrong citations hide, and a citation pointing at an internal document may be standing in front of an external original (`CLAUDE.md` § Source Tracing, rule 2).
- Statistics travel between documents by copying. A figure wrong in one place is likely wrong in several — always grep the number itself.
- `EVOLVING_CONCEPTUAL_STRAINS.md` records that header-only annotations failed once already: NotebookLM fragments documents and does not carry context across sections. Every occurrence needs an adjacent inline note.

---

## Run log

Narrative per run — what the batch surfaced, and anything a later run should know that does not fit the tables. Newest first. Unlike the handoff block, this accumulates.

### 2026-09-20 — Ledger opened

Nightly audit configured. Queue is the full library: 250 documents, none audited.

Starting conditions:

- **83** documents carry a bibliography section; the rest cite inline or not at all
- **46** already carry an editorial header block
- **24** still contain `drive.google.com` links (`scripts/normalize_internal_links.py`)
- **2** use the `[P]`/`[S]`/`[T]`/`[E]`/`[W]` type codes from the Source Tracing Protocol — so type-coding will be a large share of early work
- `EVOLVING_CONCEPTUAL_STRAINS.md` has two open items: **#16** Pillar 43 Historical Encoding and **#26** Paleolithic Geometric Signs, both opened 2026-08-20

Batch size is the run's own judgment, so the length of the pass is not fixed. As a rough sense of scale, a few documents a night puts a full pass somewhere near three months. Depth matters more than pace — a short honest batch beats a long shallow one.
