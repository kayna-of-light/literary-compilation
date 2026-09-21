# Source & Claim Audit Ledger

**Purpose**: Running state for the source and claim audit of the `data/` library — what is done, what is in flight, and what the next run needs to know.
**Procedure**: [`NIGHTLY_SOURCE_AUDIT.md`](NIGHTLY_SOURCE_AUDIT.md)

Each nightly run starts as a fresh session with no memory of the last one. This file is the only thing that carries across. Treat it as the job's working memory, not as a report.

---

## Next run starts here

**Replaced wholesale at the end of every run.** This block describes the present, not the history — history goes in the run log below. A run that leaves this stale has failed its successor.

> **Status**: 2 documents audited 2026-09-21, both `corrected`. 248 remain. Nothing in flight.
>
> **On the stranded PR #3**: `origin/claude/nightly-audit-2026-09-21`, closed unmerged by the repo
> owner, still holds 2 real audited documents (`The Heart of the Matter`, `Lexical Fossil Inventory`)
> and propagation edits to 5 more that are **not** on `main`. Untouched by tonight's run (no force-push,
> no reopen). Still unresolved — a maintainer decision (reopen/merge that PR, or treat those 2 documents
> as needing a fresh audit) would help the next run avoid duplicating or permanently losing that work.
> If nobody has acted on it by the next run, that run should flag it again rather than silently drop it.
>
> **Take next**: Your call, per procedure § 2. Two live threads if nothing else catches your eye:
> 1. `docs/research_questions/kephalaia_chapter_number_verification.md` — resolving this needs primary
>    access to Gardner's *Kephalaia of the Teacher* (1995), which this run did not have (no PDF fetch,
>    Internet Archive copy is lending-restricted, manichaean-analysis's Kephalaia outputs are gitignored).
>    If a future run gets that access — e.g. a session with the manichaean-analysis repo's generated
>    `output/` populated, or a Google Drive-mounted copy — this is worth closing out: it blocks trusting
>    the central evidence chapter of `The Garment and What Wears It` and touches `The Ancient Word
>    Recovered` (a `00_Framework` document, so defects there propagate furthest) and `Two Registers of
>    One Perception`. Reading those two source documents in full (neither was read tonight) is the actual
>    next step, not just re-searching the web.
> 2. Any other `01_Consciousness_Studies` document reporting NDE statistics dated before January 2026 is
>    a candidate for the same "superseded extraction pass" problem found in strain #27 tonight — not yet
>    checked which ones, if any, are affected.
>
> Coverage so far (both nights combined, counting only what's on `main`): `01_Consciousness_Studies` ×1,
> `08_Correspondential_Texts` ×1. Everything else is untouched — no pattern to correct toward yet, but
> worth tracking once more nights land.
>
> **Propagation debt**: None outstanding from tonight — the `marconian`→`kayna-of-light` URL fix was
> swept corpus-wide and a follow-up grep came back clean. The Kephalaia chapter-number question (above)
> is not propagation debt in the technical sense — nothing was fixed yet to propagate — but it is real
> follow-up work.
>
> **Awaiting external answers**: 2 research questions logged tonight, both open — `[NDE]` (re-run
> entity-role analysis against the current `structured-data-analysis` schema) and `[GDR]` (Kephalaia
> chapter-number verification, standalone file above).
>
> **Worth knowing**:
> - Two `EVOLVING_CONCEPTUAL_STRAINS.md` items remain open for corpus-wide re-audit, both from
>   2026-08-20 — **#16** Pillar 43 Historical Encoding and **#26** Paleolithic Geometric Signs. Neither
>   touched tonight. Highest strain number is now **#27** (NDE Entity-Role Statistics, opened tonight) —
>   do not invent numbers past it.
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
| Audited | 2 |
| In flight | 0 |
| Remaining | 248 |

Refresh the total with `find data -name "*.md" | wc -l`.

---

## Audited documents

| Date | Document | Why | Sources | Corrections | Propagated | Open | Outcome |
|---|---|---|---|---|---|---|---|
| 2026-09-21 | `01_Consciousness_Studies/NDE Statistical Analysis_ Entity Roles and Correspondential Patterns.md` | Retired `[P]`/`[S]`/`[E]` type-code table still in use; cites cross-repo NDE/DOPS statistics checkable against `structured-data-analysis`; folder untouched on `main` so far | 4/4 checked (repo URL, Swedenborg *HH* §§87–115, NDERF/IANDS counts, dead output link) | 3F (repo org name; Swedenborg citation verified correct, no change; dead link flagged, not silently kept) + 1A (strain #27: every table's stats are from a superseded Dec-2025 extraction pass) | 8 files (marconian→kayna-of-light repo-URL fix only, not audited) | 1 (re-run entity-role/guidance/return analysis against current schema) | corrected |
| 2026-09-21 | `08_Correspondential_Texts/The Garment and What Wears It_ Dating the Correspondential Substrate Beneath the Manichaean Kephalaia.md` | Retired type-code notation both inline (dating table) and in Works Cited; dense multi-tier source chain (Theopompus/Plutarch, Old Avestan, Ebla archive) worth a careful trace; folder untouched on `main` so far | 9/9 primary sources + 12/12 internal-doc links checked | 0F (nothing confidently wrong enough to edit) + 2A ([CRITICAL ANALYSIS] notes, unresolved — Kephalaia Ch.38 and Ch.115 citations) + Works Cited restructured (type-code headers dropped, "Companion Theses" renamed to "Internal Library Documents") | 0 (finding is internal to this document; the two source documents it inherited the citations from — *The Ancient Word Recovered*, *Two Registers of One Perception* — were not read in full tonight, so no edit was propagated to them) | 1 (Kephalaia chapter-number verification — see `docs/research_questions/kephalaia_chapter_number_verification.md`) | corrected |

---

## Pattern register

Recurring defect classes and how to handle them. **This is what makes the job compound** — without it, night 8 rediscovers from scratch what night 3 already worked out, and handles it differently.

Add an entry when a problem looks like it will recur. Update the existing entry rather than adding a near-duplicate.

| Pattern | What it looks like | Handling | Seen in |
|---|---|---|---|
| Personal Drive PDF cited as a source | A `## Works Cited` (or raw numbered list) entry linking `drive.google.com`, naming a file like `experiences_part-024.pdf` or a personal scan of a published work | Never leave standing. Publication → cite it properly under Primary/Scholarly. Belongs in this repo → Internal Library Document, relative link. Neither → `[TRACE NEEDED]` + research question. Full routing: `docs/BIBLIOGRAPHY_STANDARDS.md`. | 35 documents confirmed by grep at the standard's introduction (2026-09-21); not yet remediated |
| Reddit / Scribd / other unmoderated or reposted sources | A Works Cited entry linking `reddit.com` (a forum post treated as if it were evidence for a claim) or `scribd.com` (a reuploaded document with no attribution to the real original) | Never a citation in itself. Scribd etc.: find and cite the actual underlying publication. Reddit etc.: find independent verification for the claim and cite that, or `[TRACE NEEDED]` if none exists — the forum post is never the fix, even reformatted. Full routing: `docs/BIBLIOGRAPHY_STANDARDS.md` § "No unmoderated or reposted sources." | **Over 90 documents corpus-wide** confirmed by grep (2026-09-21) — this is the largest single defect class found so far, larger than the Drive-link pattern above. Budget for it explicitly; do not assume a document is close to done because its inline claims check out. |
| Stale personal-org GitHub URL (`github.com/marconian/<repo>` instead of `github.com/kayna-of-light/<repo>`) | A citation or "Repository:" line pointing at the maintainer's personal GitHub namespace from before the companion repos (`structured-data-analysis`, `proto-luke-reconstruction`, etc.) moved to the `kayna-of-light` org. The personal URL 403s; the org URL 200s. | Mechanical, low-judgment fix — `sed` the org name wherever it appears. Always grep the whole corpus for `github.com/marconian` when you find one instance; it travels by copy-paste same as any other citation. | 9 documents fixed 2026-09-21 (8 `structured-data-analysis`, 1 `proto-luke-reconstruction`); corpus-wide grep came back clean after the fix — treat as closed unless a new instance surfaces. |
| A `data/` document's statistics were computed from a since-superseded external dataset snapshot | A "Data Sources" citation to `structured-data-analysis` (or another companion repo) is accurate as a *pointer*, but the specific numbers in the document's tables no longer match what a fresh run against that repo's current data produces — because the source repo re-extracted, re-scraped, or otherwise regenerated its dataset after the citing document was written, sometimes with a materially different schema. | Don't hand-recompute and silently overwrite every table — the categorical fields may have changed shape entirely (not just the numbers), which turns "fix the stat" into an analysis-design decision the audit shouldn't make unilaterally. Check the companion repo's git history / extraction timestamps for a bulk-regeneration event; if found, route as a `CORRECTION`-type strain (annotate, don't rewrite) and log a research question for the actual re-run, rather than treating it as a same-day "fix in place" stat error. | `01_Consciousness_Studies/NDE Statistical Analysis...` (strain #27, 2026-09-21) — `structured-data-analysis`'s NDE dataset was fully re-extracted in January 2026 under a revised schema; a December-2025-dated document's tables were all stale as a result. Any other NDE/DOPS-statistics document dated before January 2026 in this corpus is a candidate for the same problem and has not been checked. |
| A load-bearing primary-source chapter/section citation doesn't match independently-verifiable secondary descriptions of that chapter/section | A companion thesis cites e.g. "Kephalaia Chapter 38" repeatedly as its central evidence for a specific textual feature, but independent search results describe that chapter number as being about something else entirely, while a *different* chapter number matches the described content closely. | Do not silently renumber a citation this consequential on secondary-source web evidence alone, especially when the citation originates in a document outside tonight's batch (propagating an unverified fix is worse than flagging it). Flag with an inline `[CRITICAL ANALYSIS]` note stating the evidence and its limits, and log a detailed research question naming exactly what a reader with primary-source access needs to check. Trace the citation to where it *originates* (often an earlier `00_Framework` or `00_Master_Theses` document that several other theses build on) so the eventual fix, once confirmed, gets applied at the source and propagated outward — not patched only where it was noticed. | `08_Correspondential_Texts/The Garment and What Wears It...` (2026-09-21) — Kephalaia "Chapter 38" (claimed: body-cosmos map) vs. likely-correct "Chapter 70"; originates in `00_Framework/The Ancient Word Recovered`. See `docs/research_questions/kephalaia_chapter_number_verification.md`. |

Candidates to watch for in early runs, from the corpus's history — confirm before treating any as established:

- Much of this library came out of Gemini Deep Research. Generated bibliographies are the usual place fabricated or subtly wrong citations hide, and a citation pointing at an internal document may be standing in front of an external original (`CLAUDE.md` § Source Tracing, rule 2).
- Statistics travel between documents by copying. A figure wrong in one place is likely wrong in several — always grep the number itself.
- `EVOLVING_CONCEPTUAL_STRAINS.md` records that header-only annotations failed once already: NotebookLM fragments documents and does not carry context across sections. Every occurrence needs an adjacent inline note.
- `WebFetch` summarizes a page through a small, fast model before returning it — for a long Swedenborg *Arcana Coelestia* section (some run for pages), a "this doesn't mention X" summary is weak evidence that X is genuinely absent, not strong evidence of a citation error. Treat a WebFetch "not found" on a long primary-source section as inconclusive, not as a finding, unless cross-checked a second way (a different host, a targeted search for the specific phrase, or — better — the section is short enough that a summary miss is implausible).

---

## Run log

Narrative per run — what the batch surfaced, and anything a later run should know that does not fit the tables. Newest first. Unlike the handoff block, this accumulates.

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
