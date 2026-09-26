# Nightly Source & Claim Audit — Operating Procedure

**Runs**: automated, nightly at 02:00 Europe/Amsterdam, unattended.
**Base branch**: `dev`. Every nightly branch is cut from `origin/dev` and every PR opens against `dev` — never `main`.
**State**: [`audit_ledger.md`](audit_ledger.md) — the only memory that carries from one run to the next.
**Standards**: [`BIBLIOGRAPHY_STANDARDS.md`](BIBLIOGRAPHY_STANDARDS.md) (what a source list is and may contain) · [`EDITORIAL_ANNOTATION_MANUAL.md`](EDITORIAL_ANNOTATION_MANUAL.md) (a separate system this job does not operate) · [`research_questions.md`](research_questions.md)
**Rewritten**: 2026-09-26, replacing the version that had grown by amendment since 2026-09-20. Where this document and an older habit recorded in the ledger disagree, this document governs.

---

## What this job is

The `data/` library is a body of curated reports. Much of it was drafted with Gemini Deep Research, and it carries that tool's habits: bibliographies that are raw lists of URLs; citations of blogs, fan sites, Wikipedia, Scribd uploads and pirated PDFs in place of the works they repost; quotations that are paraphrases, conflations of two people, or text that exists nowhere; and confident "facts" that no source supports.

The job is to **make each document correct**: every source real, traced to its origin and cited in full; every quotation verified; every factual claim true; every source list in the house format. It is done so that a reader sees only a correct document. The record of the work lives in the ledger, never in the document.

It is **not** a sampling exercise and **not** a list of doubts handed to the author. A night that finds a problem and leaves it for later has done half the job. The author expects the problem found, traced and fixed — in the document, and everywhere else in the library it occurs.

---

## Section 0 — The stance (binding; read every run)

Read [`CLAUDE.md`](../CLAUDE.md) in full and [`BIBLIOGRAPHY_STANDARDS.md`](BIBLIOGRAPHY_STANDARDS.md) before touching anything.

### What the corpus holds, and how to treat it

The corpus applies Swedenborg's framework to evidence and records where it organizes the data. Its correspondential readings are **conclusions derived from the evidence the documents set out** — the transcripts, the confirmations, the texts, the datasets. They are not optional overlays laid on "neutral" facts, and they are not a bias to be corrected toward a mainstream default.

Two consequences:

1. **Never correct toward materialism or orthodoxy.** Never rewrite a post-materialist reading into a materialist one, never present the materialist reading as the neutral baseline, never add hedges, disclaimers or "critics argue" to a supported claim, never recruit an objection because a claim feels large, never treat broad confirmation as a defect, never accept consensus as self-validating where `CLAUDE.md`'s theological-bias patterns apply. Read what a study measured, in what sample, by what method, and report that — including where it supports the hypothesis.
2. **Never describe a derived conclusion as a "stance", "position" or "interpretation" to be left alone as if it were one view among many.** The audit leaves a supported reading untouched because it is sound. When a reading *depends* on a fact the audit finds false or unestablished, name that dependency precisely — "the reading of Scott rests on a lineage no record supports" — and fix the fact; do not demote the reading.

### Errors of record — yours to fix

- A citation that does not exist, or does not say what the document says it says
- A wrong section number, date, page, name, manuscript siglum, volume, imprint
- A quotation that is not verbatim, is credited to the wrong person or work, or conflates two sources
- A statistic that disagrees with its dataset
- A claim that reaches further than its sources
- A source chain that stops at a repost, a summary or a blog when the original is findable
- A dead, personal, unmoderated or reposted source where a real one exists

### Before you report two documents as disagreeing

Read both **to their conclusions**. A document that tests two models and argues past one of them does not hold the one it argued past. The run of 2026-09-25 reported a sibling pair as divergent after reading one of them only to its § 4.4; its conclusion said the opposite. A conflict that survives a full reading of both documents is a finding; one that does not was a reading error.

---

## Section 1 — Precheck: can the run deliver?

Do this before reading anything. An audit that cannot push its branch is pure cost.

```bash
cd literary-compilation
git fetch origin --prune
git push --dry-run origin HEAD:refs/heads/precheck-$(date +%s) 2>&1 | tail -3
```

If the dry run fails (typically a 403 — the Claude GitHub App lacks write access to `kayna-of-light/literary-compilation`): **stop**. Notify that the run is blocked on GitHub write access, fixable by installing the Claude GitHub App at `https://github.com/apps/claude/installations/select_target` or reconnecting GitHub in claude.ai settings. End the run; the next night re-checks automatically.

---

## Section 2 — Choose the night's work

### 2.1 Scope is yours, and it is not "one document"

Choose what is worth a night. That can be a single long document, a cluster of siblings that share text and sources, or a defect class followed across the library. **The unit of work is a problem, not a file**: when a document's defect recurs in its siblings, the night that found it fixes it there too (§ 4.5). A narrow batch is fine only if it is finished properly; a wide one is fine only if the reading stays complete.

Constraints:

- **Finish what you open.** A document marked `corrected` has every source traced and every entry in the house format. If the night runs out, the honest outcome is `partial`, with exactly what remains stated in the ledger.
- **No standing thematic preference.** Any one night's choice is free; a *pattern* of always reaching for the same folders or subjects is not. The ledger's coverage line is the check — correct toward folders at zero.
- **Choose by a document's state, not its subject**: raw URL lists, `drive.google.com` links, Reddit/Scribd/fan-site/Wikipedia citations, retired `[P]`/`[S]`/`[T]` codes, no `Works Cited` heading, siblings of a document just audited, never audited while neighbours have been.
- **Say why** — one sentence in the ledger and the PR. Discretion nobody can see is discretion nobody can correct.

### 2.2 Don't collide, don't redo

```bash
git checkout -B claude/nightly-audit-$(date +%F) origin/dev
```

Exclude: every document already audited in `docs/audit_ledger.md` on `dev`; every document in the ledger of an unmerged `origin/claude/nightly-audit-*` branch; every document in an open PR titled `Nightly source audit — …`.

A branch with `in-progress` rows, no open PR, and older than 48 hours is a dead run: release its documents with a `released` row and note the branch in the run log. Do not resume it. A younger one may still be running — exclude its documents.

### 2.3 Claim before you read

Write the chosen documents into the ledger as `in-progress` rows, commit, and push immediately:

```bash
git add docs/audit_ledger.md
git commit -m "Claim audit batch $(date +%F)"
git push -u origin claude/nightly-audit-$(date +%F)
```

A pushed claim is what makes a crashed run visible to the next one.

---

## Section 3 — Auditing a document

### 3.1 Read it, all of it

Beginning to end, before changing anything. You cannot judge whether a source supports a claim without the argument it sits in, and you cannot report a conflict without reading to the conclusion (§ 0).

### 3.2 Inventory every source

The raw source list (often a numbered list of bare URLs, sometimes all on one line), any second annotated bibliography, every inline marker (bare numbers after punctuation — `mind.12`, `" 3`, `)7` — or superscripts ¹²³), every "X says / as Y writes / according to Z", every statistic and every quotation.

### 3.3 Trace every entry — reformatting is not tracing

For each entry answer three questions and record the answers in the ledger: **who wrote it, with what standing, and what is it resting on?** Then cite what it rests on.

| Entry is… | Do this |
|---|---|
| A published work (book, article, thesis, catalogue) | Verify author, title, imprint, year, pages (Crossref, publisher, catalogue, colophon). Cite it in full. Never guess an element — omit what you cannot verify. |
| A primary document (letter, memo, transcript, archival scan, confirmation record) | Cite the document itself, with where its scan or publication can be seen. |
| A blog, news post or aggregator | Identify the author and their standing. Follow what the post quotes or links — the transcript, the book, the interview — and cite that. Keep the post only if it is itself the authority (an identifiable historian's research post, an institution's page) and name its author. |
| A fan site, anonymous blog, forum, Reddit, Quora | Never a source. Find the real evidence for the claim. If none exists after a genuine search, the claim is corrected or narrowed in the body (§ 3.5). |
| Wikipedia | Cite the source its footnote gives, after checking that source exists. |
| Scribd, dokumen.pub, pdfcoffee, archive.org user uploads, pirated PDFs on unrelated sites | Identify the work reposted and cite the original publication. A repost whose original cannot be identified supports nothing; if it is the sole support for a quotation, that quotation is checked against every primary source available and corrected. |
| A personal `drive.google.com` link | The library document it is (relative link — confirm the file exists) or the publication it is a scan of. A Drive file that no longer exists and supports nothing in the body is removed. |
| An internal library document | Relative link. Then apply `CLAUDE.md`'s Gemini rule: if the internal document stands in front of an external original, cite the original too. An internal document that asserts a fact with no source ("research snippets", "genealogical research reveals") does not make that fact sourced. |

### 3.4 Verify the claims that rest on the sources

- **Quotations**: against full text wherever it can be had — the scan, the Gutenberg/archive text, the Foundation PDF, the publisher page. Search every quoted phrase, not a sample. Watch for the recurring defects: paraphrase in quotation marks, a phrase from a critic or a blogger credited to the subject, two people's words merged into one quotation, a passage credited to the work where the *topic* is treated rather than where the *words* are.
- **Facts**: dates, names, affiliations, "first" claims, genealogies, confirmations. A claim that appears confidently in several documents is not thereby sourced — they are usually copies of one another.
- **Statistics**: against the source of truth. Cross-repo NDE/DOPS figures are checked against `structured-data-analysis`; if the figure disagrees and the same measurement can be restated from the dataset, restate it. If the schema has changed so the measurement cannot be restated without new analysis, that is the one case where a research question is the right outcome (§ 5).

### 3.5 Correct the document

Correct, in the fewest words that make the text true, **in the author's voice and register** — the reader must not be able to tell where the correction was made.

| Finding | Action |
|---|---|
| Wrong citation, section, date, name, work, page, URL | Replace with what is right. |
| Quotation not verbatim | Restore the verbatim wording. |
| Quotation credited to the wrong person or work, or non-existent | Credit it correctly; if the words exist nowhere, replace them with what the source verifiably says on the same point. |
| Weak, reposted, unmoderated or personal source | Replace with the original; update the Works Cited. |
| Claim with no source | Find the source and cite it (body and Works Cited). |
| Claim false, or reaching past its sources | Correct or narrow it to what the sources support — never by adding a hedge. |
| A section built on a false fact | Rewrite the section to what the sources support, keeping the author's argument wherever it survives the correction. (The Retta Scott "Worcester dynasty" sections, corrected 2026-09-26, are the model: the lineage went, the correspondential reading of her work stayed.) |
| Superseded conceptual position (another library document has moved past it) | Not this job's edit — see § 3.7. |

### 3.6 Rebuild the source list

One section, in the format the Master Theses use (`data/00_Master_Theses/`; a finished example from this job: `data/07_Cultural_Pneumatology/The Mechanics of the Soul…` § VIII):

- Heading `## Works Cited`, numbered if the document numbers its sections (`## VIII. Works Cited`, `## 14. Works Cited`). Delete the raw list **and** any duplicate annotated bibliography once every real source is carried into the new one. Prose that sat inside the old bibliography moves, unchanged, to the end of the preceding section.
- Bold category headers, in this order, only those with entries: `**Primary Sources:**`, `**Scholarly Works:**`, `**Internal Library Documents:**`, `**Data Sources:**`, `**Web Sources:**`.
- Entries numbered continuously across categories, alphabetical by author within each, full Chicago style. Internal documents as `[Full H1 title](Encoded%20File%20Name.md)` plus one sentence on what they contribute here. Web sources name author or organization, title, site, date, URL.
- No "accessed on", no type-code brackets, nothing about checking.
- **Renumber every inline marker** to the new list and then check programmatically that every marker resolves to an entry and no entry number is duplicated.

### 3.7 Never write about the audit in a document

No note of any kind goes into a `data/` document: no editorial header block, no `[CORRECTION]`/`[EVOLVED]`/`[CRITICAL ANALYSIS]` note, no `[TRACE NEEDED]` marker (this job overrides the marker mentioned in `CLAUDE.md` and `BIBLIOGRAPHY_STANDARDS.md` — untraced claims are resolved or go to the ledger), no parenthetical recording what was checked, no "at the time of this analysis" gloss, no sentence explaining that a link is dead. A reader of a curated report cannot tell an author's qualification from an audit's marginalia.

The editorial annotation system (`EDITORIAL_ANNOTATION_MANUAL.md`, `EVOLVING_CONCEPTUAL_STRAINS.md`) records where the corpus's *own conceptual position* has moved, as established by another library document. This job does not add annotations, does not open strains and does not edit that file. If a document looks as if it needs one, say so in the ledger for the author.

---

## Section 4 — Tracing tools and the corpus

### 4.1 Full text beats summaries

`WebFetch` summarizes through a small model — a "not found" from it proves nothing about a long text. Get the text itself:

- **Never `WebFetch` a URL ending in `.pdf`** (it crashes the session). `curl -sSL -o f.pdf URL`, then extract with `pypdfium2` in a fresh venv (`python3 -m venv v && v/bin/pip install pypdfium2 beautifulsoup4`). Not `pypdf` — it mangles the Swedenborg Foundation fonts into a substitution cipher.
- **Scanned typescripts and images**: the `Read` tool shows an image; for many pages, OCR with `rapidocr-onnxruntime` in the venv and search the text (OCR is lossy — search stems and variants, then read the hit on the image).
- **Books**: Project Gutenberg and archive.org `_djvu.txt` for public-domain texts; archive.org lending items are not readable from the session. dokumen.pub pages carry a book's full text *and* its copyright page — use them to verify wording and edition, then cite the book, never the dokumen page.
- **Metadata**: Crossref (`api.crossref.org/works/<doi>`), PubMed E-utilities, publisher pages, the WikiTree API (`api.wikitree.com/api.php?action=getProfile&key=…`), archive.org `advancedsearch` and `metadata` endpoints.
- **The author's Drive** (Google Drive MCP tools): primary texts (Swedenborg, Kephalaia, Lovejoy…) and the PDF mirror of the library. `search_files` with `title contains` or `fullText contains` settles whether a cited Drive file still exists.
- Specific holdings and URL patterns that have already been found (Swedenborg Foundation PDFs for all twelve *Arcana* volumes, Hans Perk's Graham transcripts, Gutenberg IDs, …) are kept in the ledger's pattern register. Check it before searching from scratch.

### 4.2 Agents

`CLAUDE.md`'s rule for deep research — read the library yourself — applies to the documents in the batch: the orchestrating run reads each of them itself, in full. Agents are for breadth: tracing many external entries in parallel, or taking whole sibling documents in parallel under a written brief. If you use them:

- Give each a written brief carrying Section 0, § 3 and everything already verified that night.
- Give each agent its own files; never two agents on one file.
- **Review every agent's diff line by line and its report before committing.** An agent's work is yours once it lands.

### 4.3 Know the corpus's copy-paste families

Gemini reports on one subject were generated in batches and share whole paragraphs. A defect in one is usually in five. The pattern register lists known families (the `07_Cultural_Pneumatology` Disney reports are one). Diff siblings before auditing them.

### 4.4 Verified facts are corrected, never handed back as questions

If you have established a fact from a primary source, it is not a question. Correct it — everywhere. Do not log it as a "finding for the author", do not restate it in a notification or a question as if it were pending.

### 4.5 Propagate every correction across the whole library

A citation fixed in one document and left broken in eleven others is not fixed.

- `grep` the library from several angles for each correction: the wrong words, the number, the name, the URL, the section reference.
- Apply the correction at every occurrence, outside the batch too. Where the corrected fact carries a section elsewhere (§ 3.5, last row), rewrite that section to what the sources support.
- Propagated documents are **not** marked audited — they received corrections, not a full read. List them in the ledger row that caused them.
- A propagated bibliography entry (a repost swapped for its original) goes into the other document's list as it stands; that document's full rebuild waits for its own audit — unless the night takes it on.

---

## Section 5 — Research questions: only for what cannot be settled

A research question is a failure to resolve, recorded honestly — not a place to put work.

Log one (in `docs/research_questions.md`, target tag `[NLM]`/`[GDR]`/`[NDE]`) only when:

- the evidence needed is genuinely out of reach from the session (a book available only in print or on loan, an archive, a paywalled record with no alternative), **and** you have exhausted what is reachable — say what you searched; or
- the fix requires new analysis rather than correction (a statistic whose dataset schema has changed); or
- the correction would change a conclusion the author holds and the evidence does not settle which way — a decision, not a fact.

Before logging, ask: *could I settle this tonight with full text, OCR, an API, the author's Drive, or a further search?* If yes, settle it.

When a question is resolved, move it to `docs/resolved_research_questions.md` with the resolution and date.

---

## Section 6 — Close out

1. **Ledger rows** — flip each `in-progress` row to its outcome (`corrected`, `partial`, `clean`, `blocked`, `released`). A row records: why chosen; every entry traced with who/standing/what-it-rests-on for anything that was not a straightforward publication; every correction; every file touched by propagation; any research question. Rows are append-only; a later follow-up is a new row.
2. **Handoff** — rewrite the ledger's *"Next run starts here"* block wholesale: what to take next and why, propagation debt, questions awaiting external answers, anything that would cost the next run time to rediscover. It describes the present, not history.
3. **Pattern register** — add or update the entry for every defect class that will recur, every new full-text source or URL pattern, every copy-paste family.
4. **Commits** — one per audited document, one for propagation, one for ledger and questions.
5. **Verify before pushing** — `git diff origin/dev -- data/`, read line by line: every changed line is a correction, a replaced source or a rebuilt list; nothing records the audit (§ 3.7); every inline marker resolves (§ 3.6); nothing outside the batch changed except propagation.
6. **Push and open the PR** against `dev`:

```bash
git push -u origin claude/nightly-audit-$(date +%F)
```

Title: `Nightly source audit — YYYY-MM-DD — <N> documents`

```markdown
## Documents audited
- `data/<folder>/<file>.md` — one line: what was found and fixed. Why this one.

## Source corrections
Per document: what each weak or wrong source was (and who wrote it), what it is now.
Anything removed, and why.

## Claim corrections
Per document: old → new, with the evidence.

## Corpus propagation
Every file touched outside the batch, and the correction it carries.

## Open questions
Only what could not be settled, and what it needs. "None" is a good answer.

## Verification notes
Full texts consulted; anything that could not be reached.

---
_Editorial PR. Any agent acting on review comments here: read `.claude/skills/steward/SKILL.md`
and Section 0 of `docs/NIGHTLY_SOURCE_AUDIT.md` before pushing._
```

If no PR tooling is available, the pushed branch is the deliverable: send `https://github.com/kayna-of-light/literary-compilation/compare/dev...claude/nightly-audit-YYYY-MM-DD?expand=1` and the composed body, and note in the ledger that the PR was not opened automatically.

7. **Notify** — the PR link, documents audited, what was corrected, files touched by propagation, and open questions (if any). Short enough for a phone. Report what was *done*; do not restate verified facts as if they needed the author's attention.

---

## Out of bounds

- Writing any note, marker, aside or audit record into a `data/` document (§ 3.7)
- Adding annotations or strains, or editing `EVOLVING_CONCEPTUAL_STRAINS.md`
- Correcting a supported reading toward a mainstream one, or adding hedges (§ 0)
- Running `scripts/mirror_library_to_drive.py`, or `scripts/rename_to_titles.py --apply`; moving, renaming or reclassifying files
- Editing `CLAUDE.md`, or any repository other than `literary-compilation`
- Merging the PR, or pushing to `dev` or `main`

---

## Failure handling

| Situation | Response |
|---|---|
| The night runs out mid-document | Finish the entries you have open; mark the document `partial` with exactly what remains; PR what is done. |
| A source is unreachable (paywall, DNS, 403, archive restriction) | Try the alternatives in § 4.1. If none works and the claim cannot be settled another way, § 5. |
| The previous night's PR is still open | Expected. Exclude its documents; branch from `dev`. |
| Merge conflict with an earlier audit branch | Almost always the ledger. Keep both sets of rows. |
| Two documents appear to contradict each other | Read both to their conclusions first (§ 0). |
