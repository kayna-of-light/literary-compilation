# Source & Claim Audit Ledger

**Purpose**: Running state for the source and claim audit of the `data/` library — what is done, what is in flight, and what the next run needs to know.
**Procedure**: [`NIGHTLY_SOURCE_AUDIT.md`](NIGHTLY_SOURCE_AUDIT.md)

Each nightly run starts as a fresh session with no memory of the last one. This file is the only thing that carries across. Treat it as the job's working memory, not as a report.

---

## Next run starts here

**Replaced wholesale at the end of every run.** This block describes the present, not the history — history goes in the run log below. A run that leaves this stale has failed its successor.

> **Status**: 6 documents audited, all `corrected`. 244 remain. Nothing in flight. GitHub write access works;
> tonight's PR was opened normally against `dev`.
>
> **The rule changed on 2026-09-24 — read § 3.6 again before you start.** The author clarified the job:
> **correcting sources and claims in the document is the whole point.** Fix the wrong citation, replace the weak
> source with the high-quality one, add the source a claim is missing, complete or re-describe the Works Cited
> entry, correct the false fact in the fewest words that make it true. What is forbidden is writing *about the
> audit* in the document: no notes, markers, asides, provenance — the reports are curated, official documents, not
> notebooks. Earlier nights read the old rule as "token edits only" and left real fixes as research questions
> because they needed a new bibliography entry; that was wrong. Interpretive positions, and positions superseded
> by a later document (the annotation system), remain the author's.
>
> **Backlog now actionable under the corrected rule** (all verified by earlier nights, all left unedited only
> because of the old reading): the `[GDR]` question on eight inline attributions missing from *The Seed and the
> Sun*'s bibliography; the *eClinicalMedicine* 2022 placebo meta-analysis for the "<1% complete response" claim
> in *The Epistemic Architecture* and *The Seed and the Sun*; Kelly's *The Memory Code* and the unattributed
> "memory palace" claim in *The Epistemic Architecture* § 3.3.2; the AWARE "verified awareness" wording. Worth a
> night of its own before new documents — each is already researched.
>
> **Take next — your call (§ 2), but here is what the evidence says:**
>
> | Candidate | Why |
> |---|---|
> | `06_Mythological_Studies/The River, Not the Chain` | Retired type codes in its actual source list (24 occurrences). Folder never audited. |
> | `03_Biblical_Scholarship/What the Apparatus Cannot See` | 52 type-code prefixes — the largest remaining. Folder never audited. Long; may be a one-document night. |
> | `05_The_Self/The Architecture of Hidden Divinity` + `The Architecture of Autonomy` | Probably another sibling pair (see the new pattern-register entry); both have raw Gemini-style `#### Works cited` lists of bare URLs with "accessed on" dates — i.e. the Reddit/Scribd/bare-URL defect class, which **no run has touched yet** and which is where the mass is. Both are load-bearing: tonight's two documents cite them for their central mechanic. |
>
> Smaller type-code carriers (3–4 occurrences, may be inline rather than a source list — check before picking):
> `01_Consciousness_Studies/The Form That Precedes the Body`, `06_Mythological_Studies/Descent Remembered as
> Ascent`, `The Temple and the Trench`, `The Philosopher`. `The Garment and What Wears It` still carries codes
> in **Appendix A** deliberately — that is argument apparatus, not a source list. Leave it.
>
> Coverage so far: `01_Consciousness_Studies` ×1, `02_Swedenborgian_Theology` ×1, `05_The_Self` ×2,
> `08_Correspondential_Texts` ×1, `00_Master_Theses` ×1. **Still at zero: `00_Framework`, `03_Biblical_Scholarship`,
> `04_Early_Christian_History`, `06_Mythological_Studies`, `07_Cultural_Pneumatology`.** Correct toward those.
>
> **Standing defect classes, re-counted 2026-09-23**: Reddit/Scribd/Quora in **102** documents; `drive.google.com`
> in **24**; both untouched. Neither of tonight's documents carried either.
>
> **Propagation debt**: none. Every fix tonight was grepped corpus-wide; none recurs outside the batch.
>
> **Awaiting external answers**: 10 research questions from the audit are open — 9 from earlier nights and 1
> from 2026-09-23. Three of tonight's four were **resolved on 2026-09-24 by correcting the documents** (the
> *Apocalypse Revealed* §11 attribution, Henning/Milik and the incomplete entries, the Part numbering and quotation
> credits) and moved to `docs/resolved_research_questions.md`. The one left open is interpretive: whether *The
> Protective Garment* should be annotated, revised or retired against its later rewrite *The Empty Room*.
>
> **Worth knowing**:
> - **Gutenberg has Blavatsky in full** (IDs in the pattern register). Every quoted phrase in a document can be
>   checked in one regex pass with context. Tonight all 25+ were verbatim — report that, it is a real result.
> - **Swedenborg primary texts not in the Drive** (*TCR*, *Sacred Scripture*, *DLW*): the Swedenborg Foundation
>   hosts Standard Edition PDFs at `swedenborg.com/wp-content/uploads/2013/03/swedenborg_foundation_<title>.pdf`
>   (`curl` + `pypdfium2`, fine), and `e-swedenborg.com/writings/static/d12851/<n>.htm` is *TCR* by section, readable
>   with `WebFetch`. The Drive folder `1DwYsxv8ZWc695x1Y997Ozka2yizs7k83` has AC, HH, AR, AE, *Last Judgment*,
>   *White Horse*, *Spiritual Diary*. Recipe for Drive PDFs: `download_file_content` → the result lands in a
>   tool-results JSON file → base64-decode `content` → `pypdfium2` in a fresh venv.
> - `nag-hammadi-analysis/output/english/tractates/` has the Robinson English text of every tractate — `grep`
>   works on the English (not on the Coptic). It settled the *Apocalypse of Adam* kingdom details in one call.
> - Two `EVOLVING_CONCEPTUAL_STRAINS.md` items remain open from 2026-08-20 — **#16** and **#26**. This job does not
>   touch that file. Highest strain number is still **#26**.
> - The NDE entity-role block is stale at the **schema** level, not the data level — see the 2026-09-22 question
>   before trying to recompute anything. Most other NDE figures in the corpus reproduce exactly.
---

## How to read the tables

| Column | Meaning |
|---|---|
| **Date** | Run date (YYYY-MM-DD) |
| **Document** | Path relative to `data/` |
| **Why** | Why this document was chosen — a few words is enough |
| **Sources** | Citations verified / total found |
| **Corrections** | Fixed in place (F) — corrected citations, replaced or added sources, completed Works Cited entries, corrected facts, source-list reformats (procedure § 3.6). Nothing is annotated and no note about the audit is ever written into the document (§§ 3.6a, 3.6b). Findings that did not become edits go in this column too, marked as left alone, with why. |
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
| Audited | 6 |
| In flight | 1 (+2 follow-ups) |
| Remaining | 244 |

Refresh the total with `find data -name "*.md" | wc -l`.

---

## Audited documents

| Date | Document | Why | Sources | Corrections | Propagated | Open | Outcome |
|---|---|---|---|---|---|---|---|
| 2026-09-21 | `01_Consciousness_Studies/NDE Statistical Analysis_ Entity Roles and Correspondential Patterns.md` | Retired `[P]`/`[S]`/`[E]` type-code table still in use; cites cross-repo NDE/DOPS statistics checkable against `structured-data-analysis`; folder untouched on `main` so far | 4/4 checked (repo URL, Swedenborg *HH* §§87–115, NDERF/IANDS counts, dead output link) | 3F (repo org name; Swedenborg citation verified correct, no change; dead link flagged, not silently kept) — see 2026-09-22 row below: an original 1A (opened strain #27, annotated the document) was retracted as a misuse of the annotation system | 8 files (marconian→kayna-of-light repo-URL fix only, not audited) | 1 (re-run entity-role/guidance/return analysis against current schema) | corrected |
| 2026-09-22 | `01_Consciousness_Studies/NDE Statistical Analysis_ Entity Roles and Correspondential Patterns.md` | Follow-up, not a new selection — user flagged that the 2026-09-21 pass had injected notes into a curated document | 0 (no new source checking; prior edits were reverted) | All injected prose reverted: the editorial header block, both `[CORRECTION #27]` inline notes, the dead-link narration in Raw Data Location (link restored, org-corrected), the "the correspondence doctrine chapter; §116 opens…" gloss on the Swedenborg entry, and the "at the time of this analysis (December 2025)" glosses on the NDERF/IANDS entries. Strain #27 deleted from `EVOLVING_CONCEPTUAL_STRAINS.md`. **What remains on this document is exactly: the `marconian`→`kayna-of-light` URL fix (4 occurrences) and the mandated Source Chain→Works Cited reformat with entry content carried over unchanged.** | 0 | 0 (the `[NDE]` research question stays open — logging it was right; editing the document over it was not) | corrected |
| 2026-09-21 | `08_Correspondential_Texts/The Garment and What Wears It_ Dating the Correspondential Substrate Beneath the Manichaean Kephalaia.md` | Retired type-code notation both inline (dating table) and in Works Cited; dense multi-tier source chain (Theopompus/Plutarch, Old Avestan, Ebla archive) worth a careful trace; folder untouched on `main` so far | 9/9 primary sources + 12/12 internal-doc links checked | 0F (nothing confidently wrong enough to edit) + 2A ([CRITICAL ANALYSIS] notes, unresolved — Kephalaia Ch.38 and Ch.115 citations) + Works Cited restructured (type-code headers dropped, "Companion Theses" renamed to "Internal Library Documents") | 0 (finding is internal to this document; the two source documents it inherited the citations from — *The Ancient Word Recovered*, *Two Registers of One Perception* — were not read in full tonight, so no edit was propagated to them) | 1 (Kephalaia chapter-number verification — see `docs/research_questions/kephalaia_chapter_number_verification.md`) | corrected |
| 2026-09-22 | `08_Correspondential_Texts/The Garment and What Wears It_ Dating the Correspondential Substrate Beneath the Manichaean Kephalaia.md` | Follow-up, not a new selection — user pointed out a Google Drive folder with the primary Kephalaia text existed and was accessible the whole time, unused in the 2026-09-21 pass | 2/2 (Ch.38, Ch.115) verified verbatim against the primary text (Drive-hosted Gardner reading-edition PDF); **both citations correct as originally written** | All injected prose reverted: the 2026-09-21 `[CRITICAL ANALYSIS]` inline note and Works Cited caveat, and then (after the user's precision instruction) the replacement verification note that had been written into the Kephalaia entry in their place. That entry is now byte-identical to how the author wrote it. **What remains on this document is exactly: the retired `[P]`/`[T]` type-code legend and header suffixes removed, "Companion Theses in the Library"→"Internal Library Documents", and the two matching TOC anchors — all mandated by `BIBLIOGRAPHY_STANDARDS.md`. No content change to any citation.** | 0 | 0 (research question from 2026-09-21 resolved, moved to `docs/research_questions/resolved/`) | corrected |
| 2026-09-22 | `02_Swedenborgian_Theology/The Epistemic Architecture of Post-Materialist Inquiry_ A Methodological Thesis on Hypothesis-Testing with the Swedenborgian Framework.md` | in-progress | **14/14 Works Cited entries checked** + every inline attribution. Verified: AWARE citation (*Resuscitation* 85.12: 1799–1805); van Lommel *Lancet* 358.9298: 2039–2045; Stevenson 43/49 = 88%; **HH §256 read verbatim from the Drive primary text and confirmed exactly on point** (spirits speaking from their own memory; the ancients believing they had returned to a former life); Turner's nine factors listed correctly, 7 psycho-spiritual; Lang/Schmidt, Göbekli Tepe 9500 BCE, Babylon 32°N 2:1 daylight ratio, 364-day calendar, Daniel *Rab-hartummin*, Qumran 1QS, Mercury/Eddington/Pound-Rebka/LIGO all correct. Planck 1949 Williams & Norgate left standing (US Philosophical Library 1949 / London edition date ambiguous — not demonstrably wrong). Kelly (2016) never cited inline. | **3F.** (1) Appendix B dataset counts corrected against the source of truth: NDERF ~3,500→5,660, IANDS ~600→1,093 — the document's own N=6,753 was already right, the appendix breakdown summed to 4,100. (2) Kelly *The Memory Code* 2016→2017 (Pegasus Books is the 2017 North American edition; Allen & Unwin published the 2016 first, per the author's own editions page). (3) `## References` → `## Works Cited`, regrouped Primary/Scholarly in Chicago form per `BIBLIOGRAPHY_STANDARDS.md`, entry content carried across unchanged; the drafting-status checklist line renamed to match. **Left alone, deliberately**: the 2.6×/14.9%/5.7% Jesus-identification sentence (traced to the archived Dec-2025 notebook — 2.6× is the God+Jesus ratio, and no 5.7% non-Christian Jesus rate exists; restating it is an authorial choice, and the field is retired); "2% of cardiac arrest survivors reported **verified** awareness" (study says 2% with explicit recall, one verified case); the entity-role table (non-restatable, see pattern register); the Swedenborg Dole edition dates (carried across unchanged in the reformat); "266-year-old framework" (a property of when the document was written). | 2 files — `00_Master_Theses/The River and the Vessel`, `00_Master_Theses/The Beast That Wears the Lamb` (identical NDERF/IANDS count fix only, not audited). `01_Consciousness_Studies/Correspondential Structure in Collective Dream Space` carries "3,500+" and was **deliberately not touched** — with the "+" the statement is true, and it is a document this run has not read. | 4 logged ([NDE] schema-retirement; [NDE] the 2.6× ratio; [GDR] AWARE wording; [GDR] Dole edition dates) + 1 citation offer (the eClinicalMedicine placebo meta-analysis) | corrected |
| 2026-09-22 | `00_Master_Theses/The Seed and the Sun_ A Statistical and Phenomenological Investigation into the Architecture of Consciousness, the Paths of the Soul, and the Dissolution of the Hard Problem.md` | in-progress | **52/52 Works Cited entries checked** — 26 internal links resolved (1 broken, fixed), 5 primary sources, 14 scholarly works, 7 data sources. Data Sources verified *against the datasets themselves*: NDERF 5,660 / IANDS 1,093 / 6,753 total, DOPS 2,500+, RRP 149, PMC 350, MallWorld 2,678 from 2,038 authors through 19 Jan 2026 — **all exact**. Ohkado & Greyson 2014 verified down to the page range *and* the sample size (N = 22 interviews from Tachibana 2003) by downloading and extracting the article itself. Moody/Mockingbird 1975 and Ring/Coward McCann & Geoghegan 1980 confirmed. A large block of NDE statistics recomputed from the 6,753 records and reproducing **exactly** — see the research question for the full list. | **1F.** Works Cited entry 52 pointed at a bare filename; the target is in `../01_Consciousness_Studies/`. Link corrected. Nothing else. **Left alone, deliberately**: §4.2's "the highest rate of any being category" for the 29.5% relative gatekeeping rate — contradicted by both sibling documents' tables (each puts a being at 30.7%), but the measurement is non-restatable and narrowing the clause is the author's call; the 6,739-vs-6,753 mixed denominators (traced to `The Threefold Path of the Soul`, real chain); Gardner "2nd ed. 2020" (unconfirmable, and appears in ≥2 documents — not retracting a Kephalaia detail on search-absence again); "nearly 3,000 reports" for a raw corpus now at 3,743. **Nearly corrected in error**: §4.3's "3.8 to 1" ratio does not follow from the 40.9% and 11.8% in the same sentence (those give 3.5:1) — but 3.8:1 is **right**, because the East-West report defines impersonal as brilliant light *plus* presence-without-visual (45.1% vs 11.8%). Changing it would have introduced an error. | 0 (the one fix is internal to this document) | 3 logged ([NDE] schema-retirement, shared with the row above; [GDR] Gardner 2nd ed.; [GDR] eight inline attributions missing from the bibliography) | corrected |
| 2026-09-23 | `05_The_Self/The Empty Room and the Self That Filled It_ H.P. Blavatsky, the Ancient Word, and the Inversion from Reception to Self-Deification.md` | Retired `[P]`/`[S]`/`[T]` codes in its actual source list; `05_The_Self` never audited; sibling of the next row, so the two share sources and one pass verifies both | **All 27 Works Cited entries checked** (12 primary, 3 scholarly, 12 internal links — all resolve) + every inline quotation and attribution. **Every Blavatsky quotation verified verbatim** against the Gutenberg texts of *Isis Unveiled* I–II, *The Secret Doctrine* (3rd ed.) and *The Key to Theosophy* — 25+ quotations, none misquoted. *TCR* §279 wording confirmed (Chadwick). *Apocalypse Revealed* §11 and *Doctrine of Holy Scripture* §§101–103 read from the primary texts. Henning 1943 (*BSOAS* 11.1: 52–74), Gardner 1995, Gardner & Lieu 2004, Blavatsky publishers/dates, Turfan 1902–14, Medinet Madi 1929, Uyghur 762/763, Bailey 1880–1949 all confirmed. The 43-classification tally (12/16/11/3/1/0) reproduces exactly in both cited source documents. *Architecture of Autonomy* §1.2/§1.3/Table 1 and the §1.3 quotation confirmed. | **3F.** (1) Alice Bailey's claimed dictation "two decades"→"three decades" (1919–1949, per Lucis Trust and every standard account). (2) *Architecture of Hidden Divinity* "§I"→"§II" — the cited Divine Spark / salvation-as-self-realization / "I am God" material is §§2.1–2.3; Section I is the cosmology of captivity. (3) Works Cited: type-code legend clause and `[P]`/`[S]`/`[T]` prefixes removed, "Secondary Sources"→"Scholarly Works", "Framework Synthesis Documents"→"Internal Library Documents"; entry content unchanged. **Left alone, deliberately**: the "seek for it in China" directive attributed to *Doctrine of the Sacred Scripture* (it is *AR* §11 — fix needs a new bibliography entry); Henning 1943 cited for Qumran (predates Qumran; Milik 1976 is the source); Le Coq and *Studies in Occultism* entries incomplete; Abstract/§19 Part numbers vs TOC; Works Cited glosses crediting several *Secret Doctrine* quotations to *Isis*. | 0 (no occurrence outside the batch — grepped for each fix) | 4 logged, shared with the row below (`[GDR]` × 4, dated block 2026-09-23) | corrected |
| 2026-09-23 | `05_The_Self/The Protective Garment_ H.P. Blavatsky, Swedenborg's Ancient Word, and the Anatomy of a Counterfeit Correspondential Key.md` | Same as above — retired type codes in the source list, and the earlier sibling of *The Empty Room* | **All 30 Works Cited entries checked** (13 primary, 3 scholarly, 14 internal links — all resolve) + every inline quotation; shares the verification above. *Apocalypse of Adam* kingdom accounts (virgin womb / nourished in heaven / great prophet; thirteen then the kingless generation) confirmed against NHC V,5 in `nag-hammadi-analysis`. *Thirteen Kingdoms* and *Beast That Wears the Lamb* claims confirmed. | **3F.** (1) "Irenaeus ranks twelfth"→"tenth" — the document's own frequency table ranks him tenth, and *The Empty Room* already says tenth. (2) "the other fills it with himself"→"herself" (the referent is Blavatsky; *The Empty Room* has "herself"). (3) Works Cited reformatted as above, plus the three matching TOC entries/anchors. **Left alone, deliberately**: §10's "She read the *Apocalypse of Adam*" — an anachronism (NHC V found 1945, published 1963; she died 1891), but not a token fix; §4's "she did not have the dictionary" and §11's "including, in large part, Swedenborg himself", both corrected in *The Empty Room* §§4, 17 — an annotation question for the author, not for this job; drafting remnant "the reason the user judged this thesis worth writing" (§12.4); "eight major works" vs four listed; the setext-heading defect that puts a whole paragraph into the TOC; the same *AR* §11 and Henning findings as above. | 0 | shared with the row above | corrected |
| 2026-09-24 | `05_The_Self/The Empty Room and the Self That Filled It_ H.P. Blavatsky, the Ancient Word, and the Inversion from Reception to Self-Deification.md` | Follow-up, not a new selection — the author clarified that correcting sources and claims in the document is the job, and that only audit notes are forbidden; the 2026-09-23 pass had left verified fixes as research questions | 0 new (applies the 2026-09-23 verification) | **F.** Body: "in his doctrine of the Sacred Scripture" → "in *Apocalypse Revealed* (§11, 1766)"; "reproduces this directive *verbatim*" → "reproduces this directive"; "quotes his own phrasing" → "quotes it as his own words"; "published the Tartary doctrine in 1771" → "in 1766 and again in 1771" (×2); Appendix C "(1771)" → "(1766–1771)"; "(Henning, 1943)" → "(Milik, 1976; Henning, 1943)"; Abstract and §19 "(Part I)" → "(Part II)" to match the TOC. Works Cited: *Apocalypse Revealed* §11 and Milik 1976 added; Le Coq now cites *Buried Treasures of Chinese Turkestan* (1928); *Studies in Occultism* completed (Point Loma, 1910); *Key to Theosophy* imprint corrected; *Sacred Scripture*, Henning and the three Blavatsky entries re-described so each quotation is credited to the work it is in. **Left alone**: "I have not got it" in quotation marks — rhetorical paraphrase in the author's voice, not a factual claim. | 0 — each correction grepped corpus-wide; none recurs | 3 of the 2026-09-23 questions resolved and moved to `resolved_research_questions.md` | corrected |
| 2026-09-24 | `05_The_Self/The Protective Garment_ H.P. Blavatsky, Swedenborg's Ancient Word, and the Anatomy of a Counterfeit Correspondential Key.md` | Same follow-up | 0 new | **F.** The same *Apocalypse Revealed*, 1766, Milik and Works Cited corrections as above. §10: "She read the *Apocalypse of Adam*" corrected — it surfaced at Nag Hammadi in 1945, after her death in 1891 — keeping the argument by pointing to the gnostic deposit she did read (the position *The Empty Room* §15 establishes). §12.4 drafting remnant "the reason the user judged this thesis worth writing" → "the reason this thesis was worth writing". Missing blank line before a `---` restored, which had turned the end of §2.4 into a heading and a TOC entry; the stray TOC entry and a mismatched TOC anchor fixed. **Left alone**: §4 and §11 positions that *The Empty Room* revises (interpretive — annotation is the author's call); "eight major works" (the count's source run is not in the repository). | 0 | 1 open (narrowed) | corrected |
| 2026-09-24 | `06_Mythological_Studies/The River, Not the Chain_ The Great Chain of Being as a Reception Artifact.md` | Folder never audited (coverage correction); retired type codes in its actual source list (24); primary-text-heavy (Plato, Plotinus, Aristotle, Darwin, Lovejoy) so every attribution is checkable | in-progress | | | | in-progress |
| 2026-09-24 | `02_Swedenborgian_Theology/The Epistemic Architecture of Post-Materialist Inquiry_ A Methodological Thesis on Hypothesis-Testing with the Swedenborgian Framework.md` | Follow-up, not a new audit — handoff backlog: already-verified fixes (placebo meta-analysis, Kelly *Memory Code*/memory-palace attribution, AWARE wording) deferred only under the old § 3.6 reading | in-progress | | | | in-progress |
| 2026-09-24 | `00_Master_Theses/The Seed and the Sun_ A Statistical and Phenomenological Investigation into the Architecture of Consciousness, the Paths of the Soul, and the Dissolution of the Hard Problem.md` | Same follow-up — the `[GDR]` question on eight inline attributions missing from the bibliography, and the placebo meta-analysis | in-progress | | | | in-progress |

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
| Primary sources are in Google Drive, and the Swedenborg PDFs have a broken text layer | A citation needs checking against a primary text and the web hosts 403 or only summarise it. Two runs in a row concluded "no primary-source access" while the actual books sat in the author's Drive, reachable by this session's own tools. | **Check Drive first.** `mcp__Google-Drive__search_files` with `parentId = '<folder>'`, or `title contains 'arcana'`. Confirmed present: all **12 Arcana Coelestia** Standard Edition volumes and the 5 **Spiritual Diary** volumes (in `Swedenborg/Books/`, folder `1DwYsxv8ZWc695x1Y997Ozka2yizs7k83`); Gardner's **Kephalaia of the Teacher**, a stripped **Kephalaia Reading Edition**, Polotsky's German Kephalaia, the **Fihrist**, the Cologne Mani Codex, Book of Giants, Mandaean Book of John (folder `1dCwKutKXBYDY1Z3mRFCwX1EQCB0S14Qk` and its `Books/` child). Each AC volume states its own section range on its title page — vol. 2 is §§1114–2134 — so check the range before trusting an inherited volume number. **To extract text: `download_file_content` returns base64; decode it, then use `pypdfium2`, not `pypdf`.** The Swedenborg PDFs carry a custom font encoding that `pypdf` renders as a substitution cipher ("Arcana" → "–rcana", digits scrambled), which silently defeats string search and would make any grep-based conclusion worthless; `pypdfium2` decodes them cleanly. Install either in a **fresh venv** — the system Python's `cryptography` is broken and takes `pypdf`/`pdfminer` down with it. `pdftoppm`/poppler is unavailable and not installable, so `Read`'s PDF page rendering does not work here; `pypdfium2` is the fallback for that too. | Established 2026-09-22 after two runs had wrongly recorded the primary sources as unreachable. |
| A statistic is stale because the **schema** changed, not just the data | A `data/` document's figures were computed from fields that a companion repo's later re-extraction removed or split. The citation is correct, the analysis script is in the repo, and the numbers still look computable — but the variables they were computed from no longer exist. | **Check the field names before concluding anything.** Diff the analysis script's keys against the current records (`python3` over `projects/*/structured/*.json`). If a retired field has been *split* (one mutually-exclusive categorical into a yes/no plus a multi-select), the old percentages are **not recomputable** — they were a partition and the successor is not. That makes a re-run an analysis-design decision, which is procedure § 3.6's "no edit + research question" row, not a figure to fix. Say so explicitly in the question, or the next run will try to recompute it again. Distinguish this sharply from figures that *do* reproduce: check them, and report the exact matches, because the staleness is usually narrower than it first looks. | NDE entity-role block, 2026-09-22. `entity_role_analysis.py` reads `guidance_level`, `return_choice`, `communication_mode`, `religious_affiliation`; **none** exist in the current 6,753 records. Meanwhile a large block of *other* NDE figures in the same documents reproduced to the decimal. |
| A ratio or superlative that does not follow from the two numbers printed beside it | A sentence gives two percentages and a ratio between them, and the arithmetic does not work (40.9% and 11.8% "yielding a ratio of 3.8 to 1" — that is 3.5). It reads as an obvious one-token fix. | **Do not fix it from the sentence.** Go to the source report and find what the ratio actually measures. In the case seen, the source defines "impersonal" as brilliant light **plus** presence-without-visual (45.1% vs 11.8% = 3.8:1) — the ratio is correct and the compression in the citing sentence is what misleads. "Correcting" 3.8 to 3.5 would have written a real error into a Master Thesis. The same caution applies to superlatives: check which table the claim is measured against before narrowing it. | `00_Master_Theses/The Seed and the Sun` § 4.3, 2026-09-22 — caught before editing. The genuinely-wrong superlative in the same document (§ 4.2, "highest rate of any being category") was left alone for the opposite reason: it *is* wrong on both sibling tables, but the underlying measurement is non-restatable. |
| A Swedenborg citation that names the right doctrine but the wrong work | A document attributes a well-known Swedenborg passage to the work where the *topic* is treated, not the one where the *words* are. Seen: the Ancient Word in Great Tartary + "seek for it in China" credited to *Doctrine of the Sacred Scripture* (1763), whose §§101–103 discuss the Ancient Word but never mention Tartary or China; the directive is *Apocalypse Revealed* §11 (1766), and *TCR* §279 has the Tartary sentence without the directive. | Read the cited section itself before accepting the attribution — topic overlap between Swedenborg's works is heavy, and the same doctrine recurs in two or three books with different wording. Primary texts: Drive folder `1DwYsxv8ZWc695x1Y997Ozka2yizs7k83` has AC, HH, AR, AE, *Last Judgment*, *White Horse* and the *Spiritual Diary*; it does **not** have *TCR*, *Sacred Scripture* or *DLW*. For those, the Swedenborg Foundation's own Standard Edition PDFs are on `swedenborg.com/wp-content/uploads/2013/03/swedenborg_foundation_<title>.pdf` and `curl` + `pypdfium2` reads them cleanly; `e-swedenborg.com/writings/static/d12851/<n>.htm` serves *TCR* (Chadwick) section by section and `WebFetch` works on it. Check the rest of the library for the same passage before editing — `02_Swedenborgian_Theology/The Resonant Cosmos` already cites it correctly as *AR* 11. Then correct it: fix the body citation and add or re-describe the Works Cited entry (a new bibliography entry is a normal correction, not a reason to defer). | `05_The_Self/The Empty Room…` and `05_The_Self/The Protective Garment…` §8 — logged 2026-09-23 under the old reading of § 3.6, corrected in both documents 2026-09-24. |
| Sibling documents: an earlier version still standing beside its rewrite | Two `data/` documents share most of their text, one evidently a later rewrite of the other. The later one quietly corrects positions the earlier one still states — and the earlier one has no annotation saying so. | **Diff them before auditing either** (`diff <(sed … a) <(sed … b)` or a paragraph-level compare) — it halves the reading, shows which is later, and every point where they diverge is a candidate finding. A token error present in one and already fixed in the other (Irenaeus "twelfth" vs "tenth"; "himself" vs "herself") is safe to fix — the library itself establishes the correction. A *position* the later document corrected is not a token fix and not this job's to annotate: log it for the author (§ 3.6b), naming the sections on both sides. | *The Protective Garment* (earlier) / *The Empty Room* (later), `05_The_Self`, 2026-09-23. Worth checking whether other folders have similar pairs — `05_The_Self/The Architecture of Hidden Divinity` and `The Architecture of Autonomy` look like another (both Gemini-style, same subject), not yet compared. |
| Verifying Theosophical / nineteenth-century quotations | A document quotes Blavatsky (or another public-domain author) at length without page numbers, and web searches return only paraphrases. | **Project Gutenberg has the full texts** — *Isis Unveiled* I–II (68705, 75871), *The Secret Doctrine* 3rd ed. vols 1–4 (54824, 54488, 56880, 61626 — vol 4 is the index), *The Key to Theosophy* (55618), *Studies in Occultism* no. 1 (17009). `curl https://www.gutenberg.org/cache/epub/<id>/pg<id>.txt`, collapse whitespace, strip `_`, and regex-search every quoted phrase across all of them at once; print ±200 characters of context so you see *which work* and *what the sentence is about*, not only that it exists. The 3rd-ed. *Secret Doctrine* paginates differently from 1888, so it confirms wording and work, not page. 25+ quotations checked this way in under a minute on 2026-09-23 — all verbatim, and it caught that several quotations the Works Cited credits to *Isis* are actually in the *Secret Doctrine*. | `05_The_Self` Blavatsky pair, 2026-09-23. |

Candidates to watch for in early runs, from the corpus's history — confirm before treating any as established:

- Much of this library came out of Gemini Deep Research. Generated bibliographies are the usual place fabricated or subtly wrong citations hide, and a citation pointing at an internal document may be standing in front of an external original (`CLAUDE.md` § Source Tracing, rule 2).
- Statistics travel between documents by copying. A figure wrong in one place is likely wrong in several — always grep the number itself.
- `EVOLVING_CONCEPTUAL_STRAINS.md` records that header-only annotations failed once already: NotebookLM fragments documents and does not carry context across sections. Every occurrence needs an adjacent inline note.
- `WebFetch` summarizes a page through a small, fast model before returning it — for a long Swedenborg *Arcana Coelestia* section (some run for pages), a "this doesn't mention X" summary is weak evidence that X is genuinely absent, not strong evidence of a citation error. Treat a WebFetch "not found" on a long primary-source section as inconclusive, not as a finding, unless cross-checked a second way (a different host, a targeted search for the specific phrase, or — better — the section is short enough that a summary miss is implausible).

---

## Run log

Narrative per run — what the batch surfaced, and anything a later run should know that does not fit the tables. Newest first. Unlike the handoff block, this accumulates.

### 2026-09-24 — The rule corrected: fix the sources, never annotate the report

The author read PR #9 and corrected the premise the last three runs had been working under: *"Of course you are
allowed to edit sources and to correct them. That is the whole point… What I told you you are not allowed to do
is use the reports to write your audit notes and things of similar nature in. The reports are not notebooks, but
high quality, highly curated and official reports."* The 2026-09-22 rewrite of § 3.6 had answered a real problem
(notes injected into documents) with the wrong rule (only token edits allowed), and so every night since had been
logging verified fixes as research questions whenever the fix needed a new bibliography entry or a reworded clause.

Procedure § 3.6 rewritten: the table now routes wrong citations, weak or reposted sources, missing sources,
incomplete or mis-described entries, false facts and overreaching claims to **fix in the document**, and keeps
"no edit" only for interpretive positions, superseded positions (the annotation system), non-restatable
statistics and the genuinely untraceable. § 3.6a (no notes, markers or provenance in a `data/` document) is
unchanged — that was always the actual rule. The steward skill updated to match.

Then applied to the 2026-09-23 batch (rows above): three of its four research questions resolved by correcting
both documents, one narrowed to the interpretive part. Earlier nights' questions that were deferred for the same
reason are listed in the handoff as the next thing to clear.

### 2026-09-23 — The Blavatsky pair in `05_The_Self`: every quotation verbatim, one Swedenborg citation in the wrong book

Precheck passed; batch claimed and pushed before reading. **Batch**: `05_The_Self/The Empty Room and the Self That
Filled It` and `05_The_Self/The Protective Garment`. Chosen because the previous handoff named the retired-type-code
documents as the cheapest real win and asked for coverage to move off consciousness statistics; these two are the
type-code carriers in `05_The_Self`, a folder never audited, and they share most of their sources — so one
verification pass serves both. Both read start to finish (573 and 478 lines).

**The quotations are clean — and that is worth saying plainly.** Both theses rest on Blavatsky's own sentences,
quoted without page numbers. Every one was found verbatim in the Gutenberg texts: the Swedenborg/Tartary passages
and "we prefer decidedly to take the word of Swedenborg" (*Isis* I, II), "one small parent volume" and "the
universally diffused religion" (*SD* I), the three fundamental propositions and "self-induced and self-devised
efforts, checked by its Karma" (*SD* I), "Man tends to become a God and then—God" (*SD* I), "transform the animal of
clay into an immortal God" (*SD* II), "becomes its own Saviour in each world and incarnation" (*Key*), Irenaeus
"takes, as usual, the metaphor for reality" (*SD*), the Ophite serpent-Logos and Sophia-Achamoth passages (*Isis*
II), "a genuine Evangel of the Gnostics" (*SD*, on the *Pistis Sophia*), the horse "which is a Cycle" (*SD*). The
theses quote their subject accurately. The only slippage is in the Works Cited glosses, which credit several *Secret
Doctrine* quotations to *Isis Unveiled* — logged, not edited.

**The one real citation error is on the Swedenborg side.** Both documents credit the "seek for it in China"
directive to *Doctrine of the Sacred Scripture*. Its §§101–103, read in full from the Foundation's Standard Edition,
discuss the Ancient Word as preserved *in heaven* and never mention Tartary or China. The directive is *Apocalypse
Revealed* §11 (1766), read verbatim from the Drive copy; *TCR* §279 carries the Tartary sentence (the documents
quote it correctly) but not the directive. The library already has it right in `The Resonant Cosmos`. Not edited,
because the fix needs a new Works Cited entry; logged with the exact proposed wording.

**The two documents are one text in two drafts**, and reading them side by side was the most productive thing
tonight. *The Empty Room* is the later rewrite, and it corrects three positions *The Protective Garment* still
holds — most sharply §10's "She read the *Apocalypse of Adam*", which is impossible (NHC V, found 1945; she died
1891). Two token errors in the earlier draft were already fixed in the later one (Irenaeus "twelfth"→"tenth", which
the earlier draft's own table contradicts; "himself"→"herself" of Blavatsky), so those were safe to carry across.
The positional differences are the author's to settle — annotation is not this job (§ 3.6b). New pattern-register
entry on sibling documents.

**The four edits.** Bailey's claimed dictation "two decades"→"three" (1919–1949); *Architecture of Hidden
Divinity* "§I"→"§II" (the cited Divine Spark / self-realization / "I am God" material is §§2.1–2.3); the two
earlier-draft tokens above. Plus both Works Cited lists stripped of the retired `[P]`/`[S]`/`[T]` notation with
headers renamed per `BIBLIOGRAPHY_STANDARDS.md` and entry content unchanged. Nothing propagated — each fix was
grepped corpus-wide and occurs nowhere else.

**Not edited, and why each is right to leave**: Henning 1943 cited for Qumran (the underlying fact is true, the
attribution overreaches — Milik 1976 is the Qumran source and is already in the library); the Le Coq and *Studies
in Occultism* entries, which name no publication; "I have not got it" printed in quotation marks as Swedenborg's
words; *The Empty Room*'s Abstract and Conclusion numbering its Parts differently from its own TOC. Also fixed
in passing, in this ledger only: the pattern-register table had two blank lines splitting it into three tables.

### 2026-09-22 (night run) — Two documents audited; the entity-role staleness finally explained, and one near-miss edit

First run since the procedure was rewritten to permit exactly two kinds of edit. The result: **four token
changes across four files, zero lines of prose**, against seven findings routed to "no edit + research
question." Precheck passed, batch claimed and pushed before any reading, both documents read start to
finish.

**Batch**: `02_Swedenborgian_Theology/The Epistemic Architecture of Post-Materialist Inquiry` and
`00_Master_Theses/The Seed and the Sun`. Chosen because the previous handoff named both as the
best-motivated picks — each carries the disputed entity-role figures that 2026-09-22's earlier pass logged
but could not settle "because two of the three documents are unread." They are read now.

**What reading them settled — and what it didn't.** It did not settle which "Told to Return" column is
right, but it produced the reason nobody could: the measurement is gone at the schema level, not the data
level. `entity_role_analysis.py` reads four fields (`guidance_level`, `return_choice`, `communication_mode`,
`religious_affiliation`) and **none of them exist** in the current 6,753 records. `guidance_level` was a
single mutually-exclusive categorical — which is exactly why the published Guidance/Comfort rows sum to
90–95% — and it has been replaced by a yes/no `guidance_received` plus a multi-select `guidance_types` where
`comfort` can co-occur with `teaching`. A partition replaced by a non-partition cannot be recomputed. That
turns the standing question from "someone should re-run this" into "someone must first decide how to
operationalise it, and record that it is a new measurement." Logged as a new `[NDE]` question that gates the
two older ones. New pattern-register entry.

**The other half is the part worth protecting.** Having established the staleness, the obvious next move is
to distrust the numbers generally — and that would be wrong. A large block of `The Seed and the Sun`'s NDE
statistics was recomputed directly from the 6,753 structured records and reproduces **exactly**: light
encounter 11.8%/40.9%, 623 (9.2%) earthly-mission returns, deceased relatives 17.9% (14.9% named / 2.9%
unnamed), life review 17.5% (10.6/6.9), judgment sources 1.4/2.3/3.0, 49.4% reluctant on n=3,563, 70.1% not
returning by own choice, return-reason counts 1,459/1,164/711/623, identity continuity 64.8/1.4/0.6/33.2,
84.7% Christian among those with identified religion, and every cell of Appendix C summing to 6,753.
MallWorld (2,678 from 2,038 authors through 19 Jan 2026), remission (350 + 149 + 50 + 20 = 569) and the
κ = 0.84 inter-rater figure all verified against their sources too. The staleness is narrow. Say so.

**The near-miss, and the reason § 0 exists.** `The Seed and the Sun` § 4.3 reads "Impersonal brilliant light
… accounted for 40.9%, yielding a ratio of 3.8 to 1." 40.9/11.8 is 3.5, not 3.8 — a one-token fix, obvious,
and **wrong**. The East-West report defines impersonal as brilliant light *plus* presence-without-visual:
45.1% vs 11.8% = 3.82. The ratio is correct; only the compression in the citing sentence misleads.
"Correcting" it would have written a genuine error into a Master Thesis over a citation that was right.
Second pattern-register entry. The inverse case sits two sections earlier: § 4.2's "highest rate of any
being category" **is** wrong on both sibling documents' tables — and was still left alone, because the
underlying measurement is non-restatable and narrowing the clause is an authorial judgment.

**Primary sources were used, not deferred to.** `HH §256` read verbatim from the Drive copy of *Heaven and
Hell* and confirmed exactly on point — spirits speaking from their own memory, and the ancients concluding
they had returned to a former life. Ohkado & Greyson (2014) verified down to its sample size (N = 22
interviews from Tachibana 2003) by `curl`-ing the DOPS-hosted PDF and extracting it with `pypdfium2`. That
second technique is new and worth keeping: § 3.3's "never fetch a `.pdf`" is a constraint on `WebFetch`, not
a prohibition on reading PDFs, and a citation that would otherwise sit at one remove got checked against the
article itself.

**The four edits.** NDERF ~3,500 → 5,660 and IANDS ~600 → 1,093 in three documents (the appendix breakdown
summed to 4,100 while all three state N=6,753 in their own bodies); Kelly *The Memory Code* 2016 → 2017
(Pegasus is the 2017 North American edition, per the author's own editions page); `## References` →
`## Works Cited` in Chicago category form; and one broken relative link in `The Seed and the Sun`'s entry 52.
Nothing else. Every citation still reads as the author wrote it.

**For the next run**: the well-motivated single-document threads are now exhausted. What is left is mass —
102 documents citing Reddit/Scribd/Quora, 24 with Drive links, 13 with raw `## References` headings, 3 still
carrying retired type codes. And coverage has quietly become a problem: all four audited documents are
consciousness-statistics documents, and seven folders have never been touched. The handoff block names the
cheapest correction to both.

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

### 2026-09-22 — Two loose ends traced to primary sources, both resolved without an edit

Closing the two things the earlier passes left hanging, now that the Drive primary sources are known
to be reachable.

**1. The statistics propagation nobody had checked — this is the night's real finding.** The pattern
register said "statistics travel between documents by copying — always grep the number itself," and the
2026-09-21 run propagated only the URL fix. Grepping the figures instead turns up the December 2025
entity-role statistics load-bearing in **four more documents**, two of them top-tier:
`02_Swedenborgian_Theology/The Epistemic Architecture of Post-Materialist Inquiry` (reproduces the
guidance/comfort cross-tabulation verbatim, all six rows, and builds its anti-Jungian argument on it),
`00_Master_Theses/The Seed and the Sun` (6,739 records, the 70–73%/60.0%/54.5% spread, 33.3%, 29.5%,
χ² = 41.13 p = 0.008), `00_Framework/A Prophet Mighty in Deed and Word` (29.5%), and
`00_Framework/The Threefold Path of the Soul` (the 6,739 total). That is the propagation surface any
re-run has to cover, and it is recorded in the `[NDE]` research question.

Tracing it surfaced **two genuine discrepancies**, both logged as a new `[NDE]` research question, both
**left unedited** — two of the three documents have not been read by this audit, and the December 2025
run is not reproducible from the repository, so neither can be settled here:

- *The Epistemic Architecture*'s "Told to Return" column matches `NDE Statistical Analysis` on only one
  of six rows (God 30.7 vs 25.1, Jesus 29.0 vs 28.5, Religious figure 28.5 vs 30.7, Angels 25.8 vs
  22.2, Deceased relative 29.5 = 29.5, Unknown presence 18.7 vs 19.2) — while its guidance and comfort
  columns match to the decimal. God/Religious figure look transposed, which suggests a row misalignment
  on carry-over, but the two columns could equally be different cuts of the return variable. Which
  document is right is not determinable from here.
- *The Seed and the Sun* calls the deceased-relative 29.5% rate "the highest rate of any being
  category." On `NDE Statistical Analysis`'s own table religious figures are higher at 30.7%, so the
  superlative fails; on *The Epistemic Architecture*'s column it fails too (God 30.7%). The narrower
  claim the argument actually needs — relatives gatekeep more than higher beings do relative to their
  guidance role — is unaffected, and the other two documents state it correctly. A one-clause fix, but
  in a `00_Master_Theses` document, so the author's call.

**2. `The Garment and What Wears It`'s Swedenborg citation — verified, no error.** The 2026-09-21 pass
left `AC §§66, 1020, 1238, 2896–2897` "inconclusive" because `WebFetch` summaries of those sections
didn't surface the *Bene Qedem* content. Read §1238 verbatim from the Drive copy of the Standard
Edition (vol. 2, §§1114–2134) and the worry dissolves: it is squarely about Genesis 10–11 as
correspondential composition — "Noah, Shem, Ham, Japheth, and Canaan never existed as men… the
above-mentioned names were given in order that all the differences in general might be referred to
them" — which is exactly the first clause of the citation's own gloss. The gloss is *compound* (Genesis
1–11 as correspondential composition; the *Bene Qedem* as retainers), and the earlier pass had
mis-modelled it as claiming every listed section supports both clauses. §2896–2897 carry the
representative-Word theme as previously checked. **Nothing cited is false; no edit.** Worth noting for
the author if they ever want the second clause cited directly: the explicit loci are in the same work
at **§1675** ("Balaam, who was one of the sons of the east, or from Syria, where there was a remnant of
the ancient church") and **§1756** ("Balaam, who was of the sons of the East, from Syria where the
ancient church still existed") — the latter in a passage specifically about who preserved the ancient
representative style of writing. Strengthening a citation is the author's prerogative, not the audit's.

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
