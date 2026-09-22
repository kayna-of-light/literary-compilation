# Source & Claim Audit Ledger

**Purpose**: Running state for the source and claim audit of the `data/` library — what is done, what is in flight, and what the next run needs to know.
**Procedure**: [`NIGHTLY_SOURCE_AUDIT.md`](NIGHTLY_SOURCE_AUDIT.md)

Each nightly run starts as a fresh session with no memory of the last one. This file is the only thing that carries across. Treat it as the job's working memory, not as a report.

---

## Next run starts here

**Replaced wholesale at the end of every run.** This block describes the present, not the history — history goes in the run log below. A run that leaves this stale has failed its successor.

> **Read this first — the 2026-09-21 run got the editing discipline wrong, and the procedure that
> licensed it has been rewritten.** That run injected prose into both documents it audited: an editorial
> header block and inline `[CORRECTION]` notes, a newly-opened strain, `[CRITICAL ANALYSIS]` caveats,
> verification asides inside Works Cited entries, and a dead-link explanation that replaced a working
> link. All of it is reverted. **Procedure §§ 3.6, 3.6a and 3.6b are now the binding rule: exactly two
> edits are permitted to a `data/` document — a surgical correction of record (the wrong token, nothing
> else) and a source-list reformat to `BIBLIOGRAPHY_STANDARDS.md` carrying entry content across
> unchanged. No note of any form is ever injected. The audit does not annotate and does not open
> strains.** Findings go in this ledger; unresolved questions go in `docs/research_questions.md`. A night
> that finds a lot and edits almost nothing is a night done right. Read § 3.6 before touching a file,
> and § 4 step 7 before pushing.
>
> **Status**: 2 documents audited 2026-09-21, both `corrected`; three follow-up correction passes on
> 2026-09-22, all of them reverting the previous night's edits rather than auditing anything new (run
> log has the detail). 248 remain. Nothing in flight.
>
> **On the stranded PR #3**: `origin/claude/nightly-audit-2026-09-21`, closed unmerged by the repo
> owner, still holds 2 real audited documents (`The Heart of the Matter`, `Lexical Fossil Inventory`)
> and propagation edits to 5 more that are **not** on `main`. Untouched by this run too (no force-push,
> no reopen). Still unresolved — a maintainer decision (reopen/merge that PR, or treat those 2 documents
> as needing a fresh audit) would help the next run avoid duplicating or permanently losing that work.
> If nobody has acted on it by the next run, that run should flag it again rather than silently drop it.
>
> **Important correction from 2026-09-22, read before starting**: the 2026-09-21 run flagged two Kephalaia
> chapter citations in `The Garment and What Wears It` as possibly wrong, based only on `WebSearch`
> snippets. **Both were actually correct** — confirmed the next day against the real primary text (a
> Google Drive-hosted Gardner reading-edition PDF) once someone thought to check for it. The flags have
> been retracted from the document; full story in
> `docs/research_questions/resolved/kephalaia_chapter_number_verification.md`. **The actionable lesson**:
> this project has a Google Drive folder of primary-source PDFs (Kephalaia reading edition, "Ancient
> Word" extraction, and a `Books` subfolder — folder id `1dCwKutKXBYDY1Z3mRFCwX1EQCB0S14Qk`) that this
> session's `mcp__Google-Drive__*` tools can reach directly. **Check it before concluding primary-source
> access is unavailable for any Swedenborg, Kephalaia, or other primary-text verification** — don't rely
> on `WebSearch` summaries of a primary text's structure when the text itself might be one Drive search
> away. If a PDF needs full-text extraction: `mcp__Google-Drive__download_file_content` returns base64;
> decode it, and use `pypdf` in a fresh Python venv (`python3 -m venv` + `pip install pypdf`) rather than
> the system Python, whose `cryptography` install was broken in this environment and breaks every PDF
> library that depends on it.
>
> **Second correction from 2026-09-22, also read before starting**: the 2026-09-21 run also misused the
> editorial annotation system. Finding that `NDE Statistical Analysis` reports statistics from a dataset
> `structured-data-analysis` has since re-extracted under a different schema is real and was correctly
> logged as an open `[NDE]` research question — but the run then also added a header block, two inline
> `[CORRECTION #27]` notes, and opened strain #27 in `EVOLVING_CONCEPTUAL_STRAINS.md`, as if the position
> were already corrected somewhere in the library. It wasn't — nobody has re-run the analysis yet. **The
> editorial annotation system is only for genuine conceptual/interpretive evolution already established
> by another document in the library. It is never a way to flag deferred or future work — that is what
> `docs/research_questions.md` is for, with no edit to the document itself.** All three edits (header
> block, both inline notes, the strain) were reverted 2026-09-22; the research question stays open. See
> the corrected pattern-register entry above and procedure § 3.6's routing table — "correct treatment not
> established by the library" means no edit, not "annotate as if it were."
>
> **Take next**: Your call, per procedure § 2. One live thread if nothing else catches your eye: any other
> `01_Consciousness_Studies` document reporting NDE statistics dated before January 2026 is a candidate
> for the same underlying dataset-staleness problem — not yet checked which ones, if any, are affected.
> If you find one, log a research question only; do not repeat the annotation-system mistake above.
>
> Coverage so far (both nights combined, counting only what's on `main`): `01_Consciousness_Studies` ×1,
> `08_Correspondential_Texts` ×1. Everything else is untouched — no pattern to correct toward yet, but
> worth tracking once more nights land.
>
> **Propagation debt**: None outstanding — the `marconian`→`kayna-of-light` URL fix was swept
> corpus-wide 2026-09-21 and a follow-up grep came back clean.
>
> **Awaiting external answers**: 1 research question open — `[NDE]` (re-run entity-role analysis against
> the current `structured-data-analysis` schema, logged 2026-09-21). The `[GDR]` Kephalaia question is
> resolved (see above).
>
> **Worth knowing**:
> - `The Garment and What Wears It` still uses `[P]`/`[S]`/`[T]`/`[E]` codes in **Appendix A's** dating
>   table, with its own legend sentence, and that was left deliberately. `BIBLIOGRAPHY_STANDARDS.md`
>   retires the codes as a *source-listing* notation; Appendix A is not a source list — it is the
>   thesis's own argument, classifying the kind of evidence securing each dating tier. Reformatting a
>   Works Cited section is in scope; rewriting an argument's apparatus is not. Leave it.
> - Two `EVOLVING_CONCEPTUAL_STRAINS.md` items remain open for corpus-wide re-audit, both from
>   2026-08-20 — **#16** Pillar 43 Historical Encoding and **#26** Paleolithic Geometric Signs. Neither
>   touched. Highest strain number is **#26** — a #27 was briefly opened 2026-09-21 for the NDE dataset
>   staleness finding and deleted the next day as a misuse of the strain system (see above); do not
>   reopen it and do not invent numbers past #26 without an actual established conceptual correction.
> - `docs/BIBLIOGRAPHY_STANDARDS.md` (landed 2026-09-21) is required reading alongside `CLAUDE.md`
>   (procedure § 0). Both documents audited tonight were brought fully into line with it. The corpus-wide
>   `drive.google.com` (24 documents) and unmoderated/reposted-source (90+ documents) defect classes it
>   describes are essentially untouched still — neither of tonight's two documents happened to carry
>   either pattern, so no dent was made in those counts. Still the largest standing defect classes in the
>   corpus; still worth picking up directly on a future night rather than only encountering incidentally.
> - `WebFetch` is unreliable for confirming *absence* of content in a long primary-source section (see
>   pattern register) — don't treat a "this page doesn't mention X" summary as a finding on its own for
>   a multi-page *Arcana Coelestia* section or similar.
> - `structured-data-analysis`'s `entity_role_analysis.py` script is stale (one commit in its history,
>   never updated for schema changes since) and unrunnable as-is against the current dataset. If a
>   future run needs to verify NDE/DOPS statistics in another document, check field names in
>   `projects/nde/models/questionnaire.py` against whatever script or report you're relying on before
>   trusting its output.

---

## How to read the tables

| Column | Meaning |
|---|---|
| **Date** | Run date (YYYY-MM-DD) |
| **Document** | Path relative to `data/` |
| **Why** | Why this document was chosen — a few words is enough |
| **Sources** | Citations verified / total found |
| **Corrections** | Fixed in place (F) — surgical corrections of record, plus source-list reformats. These are the only edits this job makes to a `data/` document; nothing is annotated and no note is ever injected (procedure §§ 3.6, 3.6a, 3.6b). Findings that did not become edits go in this column too, marked as left alone. |
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
| Audited | 2 |
| In flight | 0 |
| Remaining | 248 |

Refresh the total with `find data -name "*.md" | wc -l`.

---

## Audited documents

| Date | Document | Why | Sources | Corrections | Propagated | Open | Outcome |
|---|---|---|---|---|---|---|---|
| 2026-09-21 | `01_Consciousness_Studies/NDE Statistical Analysis_ Entity Roles and Correspondential Patterns.md` | Retired `[P]`/`[S]`/`[E]` type-code table still in use; cites cross-repo NDE/DOPS statistics checkable against `structured-data-analysis`; folder untouched on `main` so far | 4/4 checked (repo URL, Swedenborg *HH* §§87–115, NDERF/IANDS counts, dead output link) | 3F (repo org name; Swedenborg citation verified correct, no change; dead link flagged, not silently kept) — see 2026-09-22 row below: an original 1A (opened strain #27, annotated the document) was retracted as a misuse of the annotation system | 8 files (marconian→kayna-of-light repo-URL fix only, not audited) | 1 (re-run entity-role/guidance/return analysis against current schema) | corrected |
| 2026-09-22 | `01_Consciousness_Studies/NDE Statistical Analysis_ Entity Roles and Correspondential Patterns.md` | Follow-up, not a new selection — user flagged that the 2026-09-21 pass had injected notes into a curated document | 0 (no new source checking; prior edits were reverted) | All injected prose reverted: the editorial header block, both `[CORRECTION #27]` inline notes, the dead-link narration in Raw Data Location (link restored, org-corrected), the "the correspondence doctrine chapter; §116 opens…" gloss on the Swedenborg entry, and the "at the time of this analysis (December 2025)" glosses on the NDERF/IANDS entries. Strain #27 deleted from `EVOLVING_CONCEPTUAL_STRAINS.md`. **What remains on this document is exactly: the `marconian`→`kayna-of-light` URL fix (4 occurrences) and the mandated Source Chain→Works Cited reformat with entry content carried over unchanged.** | 0 | 0 (the `[NDE]` research question stays open — logging it was right; editing the document over it was not) | corrected |
| 2026-09-21 | `08_Correspondential_Texts/The Garment and What Wears It_ Dating the Correspondential Substrate Beneath the Manichaean Kephalaia.md` | Retired type-code notation both inline (dating table) and in Works Cited; dense multi-tier source chain (Theopompus/Plutarch, Old Avestan, Ebla archive) worth a careful trace; folder untouched on `main` so far | 9/9 primary sources + 12/12 internal-doc links checked | 0F (nothing confidently wrong enough to edit) + 2A ([CRITICAL ANALYSIS] notes, unresolved — Kephalaia Ch.38 and Ch.115 citations) + Works Cited restructured (type-code headers dropped, "Companion Theses" renamed to "Internal Library Documents") | 0 (finding is internal to this document; the two source documents it inherited the citations from — *The Ancient Word Recovered*, *Two Registers of One Perception* — were not read in full tonight, so no edit was propagated to them) | 1 (Kephalaia chapter-number verification — see `docs/research_questions/kephalaia_chapter_number_verification.md`) | corrected |
| 2026-09-22 | `08_Correspondential_Texts/The Garment and What Wears It_ Dating the Correspondential Substrate Beneath the Manichaean Kephalaia.md` | Follow-up, not a new selection — user pointed out a Google Drive folder with the primary Kephalaia text existed and was accessible the whole time, unused in the 2026-09-21 pass | 2/2 (Ch.38, Ch.115) verified verbatim against the primary text (Drive-hosted Gardner reading-edition PDF); **both citations correct as originally written** | All injected prose reverted: the 2026-09-21 `[CRITICAL ANALYSIS]` inline note and Works Cited caveat, and then (after the user's precision instruction) the replacement verification note that had been written into the Kephalaia entry in their place. That entry is now byte-identical to how the author wrote it. **What remains on this document is exactly: the retired `[P]`/`[T]` type-code legend and header suffixes removed, "Companion Theses in the Library"→"Internal Library Documents", and the two matching TOC anchors — all mandated by `BIBLIOGRAPHY_STANDARDS.md`. No content change to any citation.** | 0 | 0 (research question from 2026-09-21 resolved, moved to `docs/research_questions/resolved/`) | corrected |

---

## Pattern register

Recurring defect classes and how to handle them. **This is what makes the job compound** — without it, night 8 rediscovers from scratch what night 3 already worked out, and handles it differently.

Add an entry when a problem looks like it will recur. Update the existing entry rather than adding a near-duplicate.

| Pattern | What it looks like | Handling | Seen in |
|---|---|---|---|
| Personal Drive PDF cited as a source | A `## Works Cited` (or raw numbered list) entry linking `drive.google.com`, naming a file like `experiences_part-024.pdf` or a personal scan of a published work | Never leave standing. Publication → cite it properly under Primary/Scholarly. Belongs in this repo → Internal Library Document, relative link. Neither → `[TRACE NEEDED]` + research question. Full routing: `docs/BIBLIOGRAPHY_STANDARDS.md`. | 35 documents confirmed by grep at the standard's introduction (2026-09-21); not yet remediated |
| Reddit / Scribd / other unmoderated or reposted sources | A Works Cited entry linking `reddit.com` (a forum post treated as if it were evidence for a claim) or `scribd.com` (a reuploaded document with no attribution to the real original) | Never a citation in itself. Scribd etc.: find and cite the actual underlying publication. Reddit etc.: find independent verification for the claim and cite that, or `[TRACE NEEDED]` if none exists — the forum post is never the fix, even reformatted. Full routing: `docs/BIBLIOGRAPHY_STANDARDS.md` § "No unmoderated or reposted sources." | **Over 90 documents corpus-wide** confirmed by grep (2026-09-21) — this is the largest single defect class found so far, larger than the Drive-link pattern above. Budget for it explicitly; do not assume a document is close to done because its inline claims check out. |
| Stale personal-org GitHub URL (`github.com/marconian/<repo>` instead of `github.com/kayna-of-light/<repo>`) | A citation or "Repository:" line pointing at the maintainer's personal GitHub namespace from before the companion repos (`structured-data-analysis`, `proto-luke-reconstruction`, etc.) moved to the `kayna-of-light` org. The personal URL 403s; the org URL 200s. | Mechanical, low-judgment fix — `sed` the org name wherever it appears. Always grep the whole corpus for `github.com/marconian` when you find one instance; it travels by copy-paste same as any other citation. | 9 documents fixed 2026-09-21 (8 `structured-data-analysis`, 1 `proto-luke-reconstruction`); corpus-wide grep came back clean after the fix — treat as closed unless a new instance surfaces. |
| A `data/` document's statistics were computed from a since-superseded external dataset snapshot | A "Data Sources" citation to `structured-data-analysis` (or another companion repo) is accurate as a *pointer*, but the specific numbers in the document's tables no longer match what a fresh run against that repo's current data produces — because the source repo re-extracted, re-scraped, or otherwise regenerated its dataset after the citing document was written, sometimes with a materially different schema. | **This is a "no edit" case, not an annotation case — corrected 2026-09-22 after the original routing was wrong.** The editorial annotation system (`[CORRECTION #N]`, `EVOLVING_CONCEPTUAL_STRAINS.md`) is for genuine conceptual/interpretive evolution — a later document reaching a different *understanding*, already established in the library. It is not a mechanism for flagging deferred work, and a strain must never be opened to mark "this needs to be redone" when nothing has actually been redone yet. A stale external dataset is a data-currency fact, not a conceptual correction. Do not hand-recompute and silently overwrite every table (the categorical fields may have changed shape, making that an analysis-design decision the audit shouldn't make unilaterally) — but also do not touch the document at all. Route it exactly per procedure § 3.6's "Correct treatment not established by the library → No edit. Research question + ledger note" row: leave the document untouched, log a research question describing what a fresh run would need to check, and note it here. Only annotate via the strain system if an actual corrected document already exists in the library *and* covers the specific claim being annotated — never to flag work that still needs to happen. | `01_Consciousness_Studies/NDE Statistical Analysis...` — originally (2026-09-21) wrongly given a header block, two inline `[CORRECTION #27]` notes, and a new strain #27, all reverted 2026-09-22. `structured-data-analysis`'s NDE dataset was fully re-extracted in January 2026 under a revised schema; the December-2025-dated document's tables are stale as a result, and this is real, correctly logged as an `[NDE]` research question — the error was editing the document and opening a strain over it, not identifying the problem. Any other NDE/DOPS-statistics document dated before January 2026 in this corpus is a candidate for the same underlying staleness and has not been checked; if found, log a research question only, do not repeat the annotation mistake. |
| `WebSearch` chapter-title snippets are not evidence about a chapter's *content* | A companion thesis cites e.g. "Kephalaia Chapter 38" as its evidence for a specific textual feature; `WebSearch` results describe that chapter's *title* as being about something else (its catechetical frame), and a *different* chapter's title sounds like a closer thematic match — but the title only names the frame, not the ~13-page body, which does contain the cited material starting partway in. | **Do not treat a web-search chapter-title summary as resolving a content question.** A chapter can run many manuscript pages under a title that only labels its opening frame or catechetical hook; the cited material can sit well past where the title's topic ends. Before flagging a primary-source citation as wrong on `WebSearch` evidence alone, check whether the session already has (or the user's project context mentions) real primary-source access — a Drive folder, a companion repo's generated output, a checked-out PDF — and use it. `mcp__Google-Drive__*` tools plus a Python venv (`pip install pypdf` — the base system's `cryptography` install can be broken; a fresh venv sidesteps it) can decode and full-text-search a Drive-hosted PDF directly. | `08_Correspondential_Texts/The Garment and What Wears It...` — flagged 2026-09-21 on `WebSearch` evidence alone (Kephalaia "Chapter 38" vs. a web-suggested "Chapter 70"; also flagged "Chapter 115"), both citations verified **correct** 2026-09-22 against the primary text once a Drive-hosted reading edition was actually checked (folder `1dCwKutKXBYDY1Z3mRFCwX1EQCB0S14Qk`, `Kephalaia_Reading_Edition.pdf`). Full resolution and lesson: `docs/research_questions/resolved/kephalaia_chapter_number_verification.md`. The flag-don't-silently-fix instinct itself was right; what was missing was checking for available primary-source access before concluding it was unavailable. |

Candidates to watch for in early runs, from the corpus's history — confirm before treating any as established:

- Much of this library came out of Gemini Deep Research. Generated bibliographies are the usual place fabricated or subtly wrong citations hide, and a citation pointing at an internal document may be standing in front of an external original (`CLAUDE.md` § Source Tracing, rule 2).
- Statistics travel between documents by copying. A figure wrong in one place is likely wrong in several — always grep the number itself.
- `EVOLVING_CONCEPTUAL_STRAINS.md` records that header-only annotations failed once already: NotebookLM fragments documents and does not carry context across sections. Every occurrence needs an adjacent inline note.
- `WebFetch` summarizes a page through a small, fast model before returning it — for a long Swedenborg *Arcana Coelestia* section (some run for pages), a "this doesn't mention X" summary is weak evidence that X is genuinely absent, not strong evidence of a citation error. Treat a WebFetch "not found" on a long primary-source section as inconclusive, not as a finding, unless cross-checked a second way (a different host, a targeted search for the specific phrase, or — better — the section is short enough that a summary miss is implausible).

---

## Run log

Narrative per run — what the batch surfaced, and anything a later run should know that does not fit the tables. Newest first. Unlike the handoff block, this accumulates.

### 2026-09-22 — Third correction: every injected note reverted, and the procedure rewritten to forbid them

The two corrections below each fixed one instance of a single underlying failure without seeing the
pattern. The user named it: *"Edits are only allowed with fine grained precision, and whatever form of
notes should never be injected, make sure the instructions follow that too."*

Re-read the whole `data/` diff against `origin/main` line by line — which is what should have happened
before the first push — and found the note-injection habit in three more places nobody had flagged yet,
including one written *during* the previous correction:

- `NDE Statistical Analysis`: the Swedenborg Works Cited entry carried a parenthetical recording what
  the audit had verified ("the correspondence doctrine chapter; § 116 opens the next chapter…"); the
  NDERF and IANDS entries carried an invented temporal gloss ("at the time of this analysis (December
  2025)"); and the Raw Data Location list had a working link *deleted* and replaced with three
  sentences explaining that the path 404s. That last one is the worst of the set — it destroyed
  document content to make room for audit commentary.
- `The Garment and What Wears It`: the Kephalaia Works Cited entry, having had its `[CRITICAL ANALYSIS]`
  caveat removed an hour earlier, had a long verification note written into it instead — the same
  mistake in a quieter register.

All reverted. The two audited documents now carry **only**: the `marconian`→`kayna-of-light` URL fix,
the mandated Source Chain→Works Cited reformat with entry content carried across unchanged, and the
retired type-code notation removed per `BIBLIOGRAPHY_STANDARDS.md`. Nothing else. Every citation reads
as the author wrote it.

**The procedure was the root cause, and is now fixed.** § 3.6's routing table had told the run to
*annotate* three separate finding classes and to mark a fourth `[TRACE NEEDED]` in the document; § 3.7
told it to propagate "the same inline annotation"; § 4 step 5 told it to "add a strain if warranted".
Those instructions licensed everything above. § 3.6 now names the only two permitted edits (a surgical
correction of record; a source-list reformat) and routes every other finding to **no edit**. Two new
subsections are explicit: **§ 3.6a — never inject a note into a `data/` document**, enumerating the
forms (header blocks, inline markers, `[TRACE NEEDED]`, parenthetical asides recording what was
checked, dead-link narration, temporal glosses), with the reason stated: a reader of a curated thesis
cannot distinguish an author's considered qualification from an audit's marginalia, and the note reads
as the document's own voice. **§ 3.6b — the audit does not annotate and does not open strains**, with
the precondition that makes the annotation system inapplicable here (the corrected position must
already exist in the library) and the rule that it is never a vehicle for deferred work. § 0 now
separates *finding* from *edit* up front, § 4's verify step requires reading the full `data/` diff and
reverting any line that is prose rather than a corrected token, and "Out of bounds" leads with both
prohibitions. The ledger's Corrections column no longer offers "Annotated (A)" or "`[TRACE NEEDED]` (T)"
as routes, because they are no longer routes.

**For the next run**: the audit's product is this ledger and `docs/research_questions.md`. A night that
finds ten real problems and edits nothing except four wrong URLs has done the job correctly. Resist the
pull to leave a mark in the document proving the work happened — the ledger is where that belongs.

### 2026-09-22 — Second correction: misuse of the editorial annotation system

Also a same-thread follow-up, immediately after the Kephalaia retraction below — the user flagged
directly that editing `NDE Statistical Analysis_ Entity Roles and Correspondential Patterns.md` with a
header block, inline `[CORRECTION #27]` notes, and a new strain in `EVOLVING_CONCEPTUAL_STRAINS.md` was
not a legitimate use of the editorial system, "absolutely not allowed... for deferred work."

The finding underneath was real: `NDE Statistical Analysis` (December 2025) reports statistics from a
dataset `structured-data-analysis` re-extracted in January 2026 under a different schema, and that is
correctly an open research question. The mistake was routing it through the annotation/strain machinery
instead of procedure § 3.6's "correct treatment not established by the library → no edit, research
question + ledger note" row. `EDITORIAL_ANNOTATION_MANUAL.md` and `CLAUDE.md`'s strain system exist to
mark where the corpus's *own conceptual understanding* has already moved on, documented by an actual
corrected position established somewhere else in the library (Limbus as Cartesian artifact, biological
determinism about Jesus, etc.) — never to flag "this dataset is stale, someone should redo the analysis
sometime." Opening a strain for the second case dresses an open, unresolved task up as a settled
correction, which is exactly backwards: a reader hitting the header block would believe the position had
already been corrected, when nothing had been re-run at all.

Reverted in full: removed the header block and both inline `[CORRECTION #27]` notes from the document,
restored the Works Cited and Raw Data Location entries to plain factual citations (no "superseded"
editorializing), and deleted strain #27 from `EVOLVING_CONCEPTUAL_STRAINS.md` entirely — highest strain
number is back to #26. The `[NDE]` research question in `docs/research_questions.md` was correctly
logged and stays open; only its "close strain #27" line was corrected, since there is no strain to
close. Pattern register entry for this defect class rewritten to state the actual rule plainly, so a
future run doesn't reach for the annotation system reflexively the next time a citation points at a
dataset that has moved on.

### 2026-09-22 — Retraction: the 2026-09-21 Kephalaia chapter-number finding was wrong

Not a new nightly run — a same-thread follow-up after the user read the 2026-09-21 PR and pointed out
two things: (1) `The Ancient Word Recovered` already gives a specific manuscript page range for
"Chapter 38" (`K.89–102`) that the previous night noted but didn't chase down, and (2) a Google Drive
folder (`1dCwKutKXBYDY1Z3mRFCwX1EQCB0S14Qk`) holds the actual primary-source PDFs — a Gardner reading
edition and an "Ancient Word" extraction — that this session's `mcp__Google-Drive__*` tools could reach
the whole time. Also pointed out access to `manichaean-analysis` was real, though that repo's own
Kephalaia output turned out to still be gitignored/unavailable — the Drive folder was the actual
missing piece, not the repo.

Downloaded and decoded `Kephalaia_Reading_Edition.pdf` (base64 via `mcp__Google-Drive__download_file_content`,
`pypdf` in a fresh venv after the system `cryptography` install proved broken), extracted full text,
and checked both flagged citations directly:

- **Chapter 38** — confirmed verbatim. The chapter header reads "Chapter 38 / Concerning the Light Mind
  and the Apostles and the Saints." — matching what `WebSearch` found the night before. But the chapter's
  body (K.89–102, exactly matching *The Ancient Word Recovered*'s page-range citation) opens its
  macrocosm discussion at K.90.15 ("Mani begins his discussion with the macrocosmos. The universe is
  constructed in the form of a human") and contains the exact quoted body-cosmos passage ("His ribs are
  all the firmaments...") and the soul-tissue correspondence (mind/bone, thought/sinew, etc.) later in
  the same chapter. The title names only the chapter's catechetical frame — a disciple's five questions
  to Mani — which is why a web search describing only the title looked unrelated to body-cosmos content.
  There is no "Chapter 70" with this material; that title, surfaced by `WebSearch` the previous night,
  does not appear in the primary text where the search implied.
- **Chapter 115** — also confirmed verbatim. Title: "The Catechumen asks the Apostle: will Rest come
  about for Someone who has come out of the Body, if the Saints pray and make an Alms-offering for
  him?" — again matching the previous night's web finding. But Mani's answer to that question is
  structured as three successive archetypal entreaties (Mother of Life → Living Spirit for the First
  Man; the gods → Third Ambassador for a leader; a third entreaty for the living soul's liberation) —
  exactly the "Three Entreaties" pattern `Two Registers of One Perception` describes. The previous
  night's inconclusive flag correctly read the title but wrongly inferred the content from it alone.

**Both `[CRITICAL ANALYSIS]` notes retracted** from `The Garment and What Wears It` (inline note and
Works Cited caveat both removed). A verification note summarising the above was written into the
Kephalaia Works Cited entry in their place — which was the same mistake again in a quieter register,
and was itself reverted in the precision pass logged above; the entry now stands exactly as the author
wrote it. Research question moved to `docs/research_questions/resolved/kephalaia_chapter_number_verification.md`
with the full resolution write-up. Pattern register entry corrected — the actual lesson is not "primary
source chapter citations are risky," it's "a `WebSearch` chapter-title snippet answers a title question,
not a content question, and check for real primary-source access (a Drive folder, a synced companion
repo) before assuming there isn't any." New note added to the handoff block pointing at the Drive folder
directly so this isn't rediscovered by accident again.

**What this means for trust in the rest of last night's work**: nothing else from 2026-09-21 is in
question — the Kephalaia finding was explicitly flagged as unresolved and never asserted as a
correction in the first place (no strain was opened, no citation was silently changed), so retracting
it is exactly the recovery the flag-don't-edit discipline was designed to make cheap. The other
document (`NDE Statistical Analysis`) and the rest of `The Garment and What Wears It`'s findings
(repo-URL fix, Ebla/Theopompus/*ed* verifications, Works Cited restructuring) are unaffected.

### 2026-09-21 — Two documents corrected; one large open finding needing primary-source access

Both documents in tonight's claimed batch (see run log entry below for the claim and the stranded-PR
anomaly found beforehand) are now closed out as `corrected`.

**`01_Consciousness_Studies/NDE Statistical Analysis_ Entity Roles and Correspondential Patterns.md`.**
Fixed a stale `github.com/marconian/structured-data-analysis` repo URL (should be
`github.com/kayna-of-light/...` — the repo moved orgs and this document was never updated), verified
*Heaven and Hell* §§87–115 is precisely the correspondence-doctrine chapter (§116 opens "The Sun in
Heaven" — citation was already correct), flagged a dead link to a generated output file that was never
committed, and restructured the ad hoc source table into a proper Works Cited. The real finding:
every statistic in the document — being-identification percentages, guidance-function cross-tabs,
return-facilitation, passage-type-to-belonging convergence, canonical-sequence adherence — was
computed from a December 2025 dataset snapshot (n=6,739) that `structured-data-analysis` has since
replaced wholesale. A January 2026 re-extraction (n=6,753, GPT-5.2) restructured the categorical
schema itself (`guidance_level` → `guidance_received`+`guidance_types`; `return_choice` →
`return_agency`/`return_willingness`/`return_reasons`; `light_encounter` from a list to a singleton;
etc.), so this wasn't a same-day "fix the number" job — direct reproduction against the current
dataset (script in `structured-data-analysis/projects/nde/scripts/entity_role_analysis.py` is itself
stale and unrunnable against the current schema; had to hand-adapt field names) showed every table
shifted by a large, schema-driven margin (e.g. `unknown_presence`: 31.4% then vs. 15.5% now). Filed
as strain #27, annotated (header block + 3 inline notes) rather than hand-rewriting every table, since
remapping the old categories onto the new schema is an analysis-design decision, not a mechanical
fix — logged a research question for the actual re-run. One overlapping scope is already covered by a
validated current internal document: `The Being of Light_ A Statistical Analysis of Near-Death
Experience Phenomenology.md` (also had the same `marconian` URL bug, fixed same night). The
`marconian`→`kayna-of-light` fix propagated to 8 more files corpus-wide (7 `structured-data-analysis`
citations, 1 `proto-luke-reconstruction`); a corpus-wide grep afterward came back clean.

**`08_Correspondential_Texts/The Garment and What Wears It_ Dating the Correspondential Substrate
Beneath the Manichaean Kephalaia.md`.** A dense, carefully self-critical dating thesis (it already
guards against its own circularity better than most documents in this corpus) — read in full,
including its two key companion theses' relevant sections. Verified accurate: Kephalaia Chapter 72's
title, the Theopompus/Plutarch *De Iside* 46–47 citation on Magian two-principle eschatology, the Ebla
archive's scale and dates (~17,000 tablets, 2500–2250 BCE, Matthiae, excavated from 1974), and the
*ed* (Strong's 108) distribution (exactly Gen 2:6 + Job 36:27, no under-count — the exact defect class
the previous run's pattern register flagged, and it came back clean here). Restructured Works Cited to
drop the retired `[P]`/`[T]` bracket headers and rename "Companion Theses in the Library" to "Internal
Library Documents"; all 12 internal-document links resolve. **The significant open finding**:
independent secondary-source verification (three separate search results, converging) strongly
suggests "Kephalaia Chapter 38" — cited 8+ times in this document as its central transmission-
fingerprint evidence, the body-cosmos/soul-tissue map — is actually titled "On the Light-Mind, the
Apostles, and the Saints" in Gardner's edition, while a different chapter (70), "On the Body, That It
Was Made to Resemble the Cosmos," matches the described zodiac/organ content closely. A weaker,
inconclusive finding raises the same question for "Chapter 115" (cited for the regenerative
micro-architecture in a different companion thesis). **Not corrected in place**: the citation
originates upstream in `00_Framework/The Ancient Word Recovered` (Chapter 38, with a specific
manuscript page range `K.89–102` also unverified) and `06_Mythological_Studies/Two Registers of One
Perception` (Chapter 115), neither of which was read in full tonight, and primary-source access
(Gardner 1995, *The Kephalaia of the Teacher*) was not obtainable this session — no PDF fetch, no
usable Internet Archive full-text search (the item is controlled-digital-lending), nothing in the
manichaean-analysis companion repo's checked-in files. Flagged with inline `[CRITICAL ANALYSIS]` notes
in the audited document only; full write-up and propagation plan at
`docs/research_questions/kephalaia_chapter_number_verification.md`. This is exactly the kind of thing
§0 warns against handling carelessly in the other direction — not "correct a correspondential reading
toward materialism," but the mirror-image risk of confidently "fixing" a load-bearing citation across
multiple documents on secondary-source web evidence alone. Also spot-checked *Arcana Coelestia*
§§1238, 2896–2897 (the Bene Qedem/correspondences-retained claim); `WebFetch`'s page summaries didn't
obviously surface that content, but this is inconclusive rather than a finding — see the new pattern-
register entry on `WebFetch` reliability for long AC sections — logged as a note here, not annotated
in the document.

### 2026-09-21 — Batch claimed; stranded-PR anomaly found during precheck

**§ 1 precheck passed cleanly** — a real `git push --dry-run` succeeded, no 403. This is the "first
real test" the previous (now-closed) branch's handoff block asked this run to report on: the
repo-selection fix the maintainer applied mid-day on 2026-09-21 appears to have resolved the
routine-firing git-access problem. Full `git`/`gh`-style flow used throughout, not the MCP-tools
fallback.

**Before claiming, found `origin/claude/nightly-audit-2026-09-21` still on GitHub, unmerged, backing
a closed-not-merged PR #3** ("Nightly source audit — 2026-09-21 — 2 documents, all follow-up
resolved"). That branch contains real, verified audit work — `00_Framework/The Heart of the Matter`
and `03_Biblical_Scholarship/Lexical Fossil Inventory` fully corrected, plus propagation edits to 5
more files (`Conversation relating the Fourth Church`, `The Biological Error and the Theological
Rescue`, `Stratigraphy of the Archaic`, `The Stratigraphy of the Hebrew Bible`, `The Architecture of
Autonomy`) — none of which is reflected on `main` (confirmed: `main`'s ledger still reads 0 audited,
highest strain is #26, not #27). PR #3 was closed by the repo owner (`marconian`) directly, no
comment, `mergeable_state: clean` — so this was almost certainly a deliberate decision, not a
technical failure, and not this run's call to reverse. **This run did not touch that branch**: no
force-push, no reopen, no cherry-pick — picked a distinct branch name
(`claude/nightly-audit-2026-09-21-2`) to avoid colliding with it. Flagged in tonight's PR/notification
for the maintainer's attention; if the two documents there should count as already-audited, a human
decision (reopen/merge, or explicitly mark done in this ledger) is needed first. Tonight's batch was
chosen fresh against `main`'s actual state and does not overlap those two files, so no work here
depends on that question being resolved either way.

Claimed batch of 2 (see rows above), on `main`'s state (0 audited, 250 remaining, highest strain #26).

### 2026-09-20 — Ledger opened

Nightly audit configured. Queue is the full library: 250 documents, none audited.

Starting conditions:

- **83** documents carry a bibliography section; the rest cite inline or not at all
- **46** already carry an editorial header block
- **24** still contain `drive.google.com` links (`scripts/normalize_internal_links.py`)
- **2** use the `[P]`/`[S]`/`[T]`/`[E]`/`[W]` type codes from the Source Tracing Protocol — so type-coding will be a large share of early work
- `EVOLVING_CONCEPTUAL_STRAINS.md` has two open items: **#16** Pillar 43 Historical Encoding and **#26** Paleolithic Geometric Signs, both opened 2026-08-20

Batch size is the run's own judgment, so the length of the pass is not fixed. As a rough sense of scale, a few documents a night puts a full pass somewhere near three months. Depth matters more than pace — a short honest batch beats a long shallow one.
