# Nightly Source & Claim Audit — Operating Procedure

**Created**: 2026-09-20
**Runs**: Automated, nightly at 02:00 Europe/Amsterdam
**Base branch**: `dev` — every nightly branch is cut from `origin/dev` and every PR opens against `dev`, never `main`.
**State**: [`audit_ledger.md`](audit_ledger.md)
**Related**: [`BIBLIOGRAPHY_STANDARDS.md`](BIBLIOGRAPHY_STANDARDS.md) · [`EDITORIAL_ANNOTATION_MANUAL.md`](EDITORIAL_ANNOTATION_MANUAL.md) · [`EVOLVING_CONCEPTUAL_STRAINS.md`](EVOLVING_CONCEPTUAL_STRAINS.md) · [`research_questions.md`](research_questions.md)

---

## Purpose

Work through the `data/` library a few documents at a time, reading each one completely, verifying that every source is real, correctly cited, traced as far back as it goes, and of high quality — and that every claim the document makes is correct. Correct what is wrong in the documents themselves — citations, sources, facts — propagate each correction across the corpus, record the work in the ledger, and open a PR for review.

This is an **unattended** run. Nobody is watching it. That shapes every rule below: when the correct action is not established, the run does not guess — it logs a research question and leaves the text alone.

---

## Section 0 — Methodological Baseline (read first, every run)

**Before touching any document, read `CLAUDE.md` in full and `docs/BIBLIOGRAPHY_STANDARDS.md`.** Not a skim. `CLAUDE.md` sets the stance that is the whole point of this project, and the most damaging thing this job could do is quietly erode it. `BIBLIOGRAPHY_STANDARDS.md` is what §§ 3.3–3.4 below assume you already know — the category-grouped Works Cited format, the ban on personal file citations, and the retired type-code notation.

### The failure mode this job must not produce

A model auditing "scientific claims" defaults to mainstream materialist framing, because that is what it has seen most of. Applied here, that default would read a correctly-sourced post-materialist finding as an error and "correct" it into the very position this corpus exists to test against the data. **That is the single worst outcome of this job — worse than doing nothing.**

The project's position is not a bias to be filtered out. It is the tested hypothesis. From `CLAUDE.md`:

> We analyze empirical findings without filtering for "acceptable" conclusions. We don't seek mainstream approval. We don't defend orthodoxy. We follow the data.

### Hard prohibitions

Never, in any edit, annotation, PR description, or research question:

- **Never** rewrite a post-materialist reading toward a materialist one, or present the materialist reading as the neutral/default/correct one.
- **Never** add hedges, disclaimers, or "critics would argue" softening to a finding that its sources actually support. Accuracy is the goal, not the appearance of balance.
- **Never** recruit an objection because a claim feels large. Read what a study measured, in what sample, by what method, and report that — including where it *supports* the hypothesis. See `CLAUDE.md` § "Do Not Recruit Objections."
- **Never** treat broad confirmation as evidence of a defect. See `CLAUDE.md` § "Confirmation Is Not a Defect."
- **Never** raise the invalid critiques listed in `CLAUDE.md` § "Scholarly Critique Guidelines" ("a materialist would dismiss this", "this is unverifiable", "Swedenborg shouldn't be trusted").
- **Never** treat consensus as self-validating where the theological bias patterns in `CLAUDE.md` apply. Assess the quality of the evidence being rejected, not the fact of rejection.

### What *is* in scope as an error

The distinction that governs this entire job:

> **An error of record is a fact about a source. An interpretation is a position the corpus holds.**
> Errors of record get corrected. Positions get tested against the library — never against a default.

In scope as a **finding** (all of these):

- A citation that does not exist, or does not say what the document claims it says
- A wrong section number, date, page, name, manuscript siglum, or statistic
- A quotation attributed to the wrong author or work
- A statistic that disagrees with the dataset it came from
- A claim that overstates the reach of the source under it
- A source chain that stops short of an available primary source
- A dead, redirected, paywalled-with-no-alternative, or low-quality source where a better one exists

**Finding and fixing are the job.** Every finding above is yours to correct in the document: fix the wrong citation, replace the weak source with the high-quality one, add the source a claim is missing, correct the false fact. What is never allowed is writing *about* the audit into the document — no notes, markers, or asides of any kind (§ 3.6a). The documents in `data/` are curated, official reports: they get corrected, never annotated. Read § 3.6 before touching a file.

Out of scope (leave these alone):

- The correspondential reading of evidence
- The two-tiered hermeneutic
- Post-materialist premises
- Treating Swedenborg as a hypothesis under test
- Any interpretive stance established in the library

### When in doubt

**Do not assume a default. Read the library.** If a claim's correct treatment is not obvious, search `data/` for where the corpus establishes its position on that subject and follow it.

If the library does not settle it: **make no edit.** Log a research question in `docs/research_questions.md`, note it in the ledger and the PR, and move on. An unresolved question surfaced for review is a good outcome. A confident wrong edit made at 3 a.m. is not.

---

## Section 1 — Precheck: confirm the run can deliver

**Do this before reading a single document.** The audit is expensive; a run that cannot push its branch or open a PR has produced nothing but cost. The check is cheap, so it goes first.

```bash
cd literary-compilation
git fetch origin --prune
git push --dry-run origin HEAD:refs/heads/precheck-$(date +%s) 2>&1 | tail -3
```

A `403` means the Claude GitHub App does not have write access to `kayna-of-light/literary-compilation`.

If it fails: **stop. Do not audit.** Send the notification saying the run is blocked on GitHub write access and that an org owner grants it by installing the Claude GitHub App at `https://github.com/apps/claude/installations/select_target`, or by reconnecting GitHub from claude.ai settings. Then end the run. The next night's run re-checks automatically and proceeds the moment access exists — nothing needs to be rescheduled.

If it succeeds, delete nothing (the dry run wrote nothing) and continue.

---

## Section 2 — Select the batch

**You choose what tonight's batch is and how large it is.** There is no fixed list and no fixed number. Read the state of things and decide.

What that means in practice: you might take one long, heavily-cited document and do it properly; or four short ones; or follow a thread — a defect you found last night that probably repeats, a cluster of documents that cite each other, a class of broken citation worth clearing in one sweep. Some nights the useful work is obvious from the handoff block. Some nights you will open the library and something will catch your attention. That is a legitimate reason to pick it.

The judgment you are making is *what is worth a night here*, and you are better placed to make it at the time than a rule written in advance.

### Constraints on that judgment

Four, and only four:

**A reasonable night's work.** Enough that the night counts for something; not so much that the reading goes shallow. Better two documents genuinely understood than five skimmed. If you are past five you are almost certainly skimming — but the ceiling is your own honesty about depth, not a number.

**Finish what you start.** Never leave a document half-audited and marked done. If you misjudge the size, complete the ones you have opened, ledger only those, and PR the partial batch. A shorter honest batch is a good night.

**No standing thematic preference.** Any one night's choice is yours. What must not happen is a *pattern* — always reaching for the same folders or subjects, so that parts of the library get verified heavily and others never at all. That would make the audit's picture of source quality a description of your habits rather than of the corpus. The ledger is the check: if one area is running ahead of the rest, correct toward what has been neglected. Free choice each night, even coverage over time.

**Say why.** Record your reasoning in the ledger and the PR — a sentence is enough. *"Took these three because they all cite the same Greyson figure and I wanted to see whether it travelled wrong."* Discretion nobody can see is discretion nobody can correct; the rationale is what lets the author redirect you.

### What is not discretionary

Correctness of selection. Do not re-audit a document already done, and do not collide with a night still in flight.

```bash
cd literary-compilation
git fetch origin --prune
git checkout -B claude/nightly-audit-$(date +%F) origin/dev
```

Build the exclusion set from **three** places:

1. `docs/audit_ledger.md` on `dev` — every document already audited.
2. Every unmerged `origin/claude/nightly-audit-*` branch — read each one's ledger, since those documents are audited but not yet merged:
   ```bash
   for b in $(git branch -r --list 'origin/claude/nightly-audit-*' --no-merged origin/dev); do
     git show "$b:docs/audit_ledger.md" 2>/dev/null
   done
   ```
3. Any open PR titled `Nightly source audit — …`.

### Signals you may find useful

Not a ranking, and nothing here obliges you to pick anything. These are just properties that tend to mark a document as having work in it, and they are cheap to check:

- An existing `[TRACE NEEDED]` marker
- Listed unfinished in the `EVOLVING_CONCEPTUAL_STRAINS.md` review task list
- Still contains `drive.google.com` links, or `[P]`/`[S]`/`[T]`/`[E]`/`[W]` tags
- A source list that is still a raw numbered list of bare URLs rather than the categorized Works Cited format (`docs/BIBLIOGRAPHY_STANDARDS.md`)
- A bibliography but no editorial header block
- Untouched for a long time, or never audited while its neighbours have been

Weigh them however the night warrants. A document showing none of these may still be the right pick — a clean-looking file whose sources have never actually been checked is exactly the kind of thing that hides a bad citation.

Note that all of these are properties of a document's **state**, not of its subject. That is the distinction that keeps free selection from drifting into thematic bias: choose by what a document looks like, not by what it is about.

### 2.1 Claim the batch before auditing

Write the chosen documents into the ledger as `in-progress` rows, then **commit and push the branch immediately** — before reading anything:

```bash
git add docs/audit_ledger.md
git commit -m "Claim audit batch $(date +%F)"
git push -u origin claude/nightly-audit-$(date +%F)
```

This is what makes a crashed run visible. Sessions run in ephemeral containers: an unpushed claim dies with the container, and the night's documents would look untouched while the work is gone. A pushed claim means the next run can always tell the difference between *audited, PR open* and *started, never finished*.

### 2.2 Handle a stale claim

A branch with `in-progress` rows, no open PR, and older than 48 hours is a dead run. Do not resume it — you do not know how far it got, and a half-audited document is worse than an unaudited one. Instead:

- Release those documents back into the queue
- Note the release in the ledger run log with the dead branch name
- Delete nothing; leave the branch for inspection

A branch younger than 48 hours with `in-progress` rows may be a run still going. Exclude its documents and pick others.

---

## Section 3 — Per document

### 3.1 Read it completely

Beginning to end, yourself. No subagent summaries, no skimming to the bibliography. `CLAUDE.md` is explicit: *"For documents in `data/`, read them yourself from beginning to end. No agents. No summaries. You need understanding, not information."*

You cannot judge whether a source supports a claim without knowing what the document is arguing.

### 3.2 Inventory every source

Build a working list of every citation, attribution, statistic, quotation, and named reference — inline and in the bibliography. Include claims phrased as attributions without a formal citation ("Greyson found…", "the DOPS data shows…"). Those are the ones that rot unnoticed.

### 3.3 Verify each source

For each entry:

| Check | Pass condition |
|---|---|
| **Exists** | The work is real; author, title, year, publisher resolve |
| **Says it** | The cited passage actually supports the claim made from it |
| **Located** | Section/page/§ given precisely enough to check (Swedenborg: `DLW §§ 83–85`, not "Swedenborg says") |
| **Traced** | Chain followed to the furthest available primary source |
| **Reachable** | Not a `drive.google.com` link or other personally-hosted file — see `docs/BIBLIOGRAPHY_STANDARDS.md` |
| **Quality** | Primary over secondary; academic for historical claims; first-person for experiential claims |

Use `WebSearch` / `WebFetch` for external verification. **Never fetch a URL ending in `.pdf`** — it crashes the session. Use the abstract, the publisher landing page, or an HTML version, and note the substitution.

Cross-repo statistics (NDE figures, DOPS counts, χ² values) are verified against **`structured-data-analysis`**, which is the source of truth for them. It is checked out alongside this repo. If a figure in a `data/` document disagrees with the dataset, the dataset wins and the document is corrected.

Apply the Gemini rule from `CLAUDE.md`: where a citation points at an internal document, check whether the claim actually originates externally. Internal synthesis is a legitimate source, but it must not stand in front of the original evidence.

### 3.4 Clean the source list

Full standard: `docs/BIBLIOGRAPHY_STANDARDS.md`. A document's source list is one `## Works Cited` section, entries grouped under **Primary Sources** / **Scholarly Works** / **Internal Library Documents** / **Data Sources** (only the categories that have entries), each in full Chicago-style citation. If a document's list is still a raw numbered list of bare URLs — the common shape for documents that came straight out of Gemini Deep Research — restructure it into that form as part of the audit. This is a structural correction like any other; it does not require the claim underneath to be in question.

**Every `drive.google.com` link gets resolved, and the two cases are different:**

- If the link actually points to another document that lives in this library (a Deep Research citation that resolved to an internal file via Drive instead of a relative path), rewrite it to a relative link — `python scripts/normalize_internal_links.py --only "<relative path>"` to preview, `--apply` to write.
- If the link points to a personal file — a scan, an export, anything only reachable from the author's own Drive — it is not a valid citation regardless of what the file contains. Replace it with the actual publication under **Primary Sources** or **Scholarly Works** (publisher, edition, translator — verify these, don't guess them), or with the corpus document it belongs to as an **Internal Library Document**. Only if no real source can be found after a genuine search, leave the entry as it stands and log a research question — do not mark it `[TRACE NEEDED]` in the document (§ 3.6a), and do not delete a citation you cannot replace.

Other cleanup:

- Replace a weak source with the better one where a better one exists, and say so in the ledger. This is the heart of the job: a claim resting on a Reddit post, a repost, a summary or a secondary gloss gets the high-quality source that actually supports it.
- Complete partial references to full scholarly form (publisher, place, year, translator — verified, not guessed).
- Add the missing entry when the body cites or quotes a work the Works Cited does not list, and correct an entry's description when it credits a quotation or claim to the wrong work.
- Remove a citation **only** when it is fabricated or wholly unverifiable — and then say so explicitly in the PR. Never silently drop a reference.
- Do not add `[P]`/`[S]`/`[T]`/`[E]`/`[W]` tags — that notation is retired. The category the entry sits under already says what kind of source it is.
- Preserve the full chain, not just the endpoints.

**Never write audit provenance into the document.** No "(verified 2026-09-21)", no mention of the ledger, no PR reference, inside the Works Cited section or anywhere else in the body. The document describes what was consulted; the history of checking it belongs only in `docs/audit_ledger.md`.

### 3.4b Completeness — the whole list, not just the claims you checked

**This is the point of the job, not a secondary tidy-up.** Cleaning the source list and finding the actual primary sources behind weak citations is what "auditing a document" means here — checking a handful of claims and leaving the rest of the bibliography untouched is not a partial version of the job, it is a different, smaller job that happens to look similar.

A document does not count as `corrected` in the ledger, and does not get closed out, until **every entry in its Works Cited has been brought into line with `docs/BIBLIOGRAPHY_STANDARDS.md`** — not only the entries behind the specific claims that got investigated in § 3.5. Concretely: if a document has 15 bibliography entries and the night's work verified 5 underlying claims, all 15 entries still get checked against § 3.3's table and reformed under § 3.4, including the ones that don't happen to support a claim you chose to fact-check. A raw numbered list of bare URLs, Scribd reposts, and forum links sitting untouched next to five newly-verified inline facts is not a corrected document — `docs/BIBLIOGRAPHY_STANDARDS.md` § "No unmoderated or reposted sources" exists because of exactly this failure mode, caught once already in this corpus (see the pattern register).

If the full list genuinely cannot be finished in one night — some documents run to 30+ entries — that is a **`partial`** outcome, not `corrected`: ledger the entries actually finished, leave the rest for the next run on this same document, and say so plainly in the PR. `partial` is an honest, acceptable outcome. A document marked `corrected` with its bibliography half-done is not.

### 3.5 Validate the claims

Read for correctness within the framework — `CLAUDE.md` § "Valid Critiques":

- Internal inconsistency within the document
- Contradiction with an established position elsewhere in the corpus
- Factual errors: dates, names, numbers, manuscript sigla, attributions
- Source chain gaps
- A claim reaching further than its evidence

Where a document and the corpus disagree, establish which is current before editing. `EVOLVING_CONCEPTUAL_STRAINS.md` is the register of what has been superseded.

### 3.6 Apply corrections

**Correct the document. Do not write about the correction in it.** Those are the two halves of this section, and the second does not limit the first.

The documents in `data/` are curated, official reports. The audit's job is to make them *right* — every source real, correctly cited, and of high quality; every factual claim true — and to do it so cleanly that a reader sees only a correct document, never the audit. So:

| Finding | Action |
|---|---|
| Wrong citation, section, date, name, siglum, page; wrong work credited for a passage; stale or wrong URL | **Fix in place.** Replace what is wrong with what is right. |
| Weak, reposted, unmoderated or personally-hosted source | **Replace it with the high-quality source** — the primary text, the original publication, the peer-reviewed study — and update the Works Cited to match. |
| Claim with no source, or a source that does not support it | **Find the source that does, and cite it** (inline and in the Works Cited). |
| Works Cited entry incomplete, mis-described, or missing for a work the body uses | **Complete it, correct its description, or add it.** |
| Statistic disagreeing with its dataset, where the same measurement can be restated directly from the source of truth | **Fix the number**, naming the source of truth in the ledger. |
| A factual claim that is false (a date, an event, who did or read what) | **Correct it in the fewest words that make it true**, keeping the author's argument and register. Verify against a primary or high-quality source first. |
| Claim overstating its source's reach | **Find a source that supports the full claim and cite it; if none exists, narrow the wording to what the sources support.** Never add a hedge or disclaimer in place of a correction (§ 0). |
| Source list not in the standard's format | **Reformat per `docs/BIBLIOGRAPHY_STANDARDS.md`.** |
| Statistic whose dataset or schema has since changed, so the measurement cannot be restated without fresh analysis | **No edit.** Research question + ledger note. |
| Interpretive position, or a position superseded by later corpus understanding | **No edit.** Interpretation is the author's; superseded positions belong to the separate annotation system (§ 3.6b). Ledger + research question. |
| Claim untraceable after genuine effort | **No edit** — not even a `[TRACE NEEDED]` marker. Research question + ledger. |
| Correct treatment genuinely not settled by the library or by high-quality sources | **No edit.** Research question + ledger note. |

Edits are **precise**: change what is wrong and what the correction requires, nothing around it. An edit to a Works Cited entry changes what that entry *cites*, never adds a record of how it was checked. Where the body's wording changes, it stays in the author's voice and register — the reader should not be able to tell where the correction was made.

### 3.6a Never inject a note into a `data/` document

**No note of any form goes into a `data/` document. Not in any circumstance this job can produce.** That means none of:

- an editorial header block, or an inline `[CORRECTION #N]` / `[EVOLVED #N]` / `[CRITICAL ANALYSIS #N]` / `[REFRAMING]` / `[EXTENSION]` note;
- a `[TRACE NEEDED]` marker;
- a parenthetical or em-dashed aside recording what the audit checked, confirmed, or doubted — inside a Works Cited entry, a data-provenance table, a "Raw Data Location" list, or anywhere in the body;
- a sentence explaining that a link is dead, that a figure is stale, that a dataset has moved on, or that a citation needs verification;
- an "at the time of this analysis" or similar temporal gloss the document did not already carry.

A dead link is **fixed or left alone**, never narrated. A stale figure is **corrected from the source of truth or left alone**, never captioned. `docs/BIBLIOGRAPHY_STANDARDS.md` § "No audit provenance" already forbids this; it is restated here because the failure is easy and the damage is silent — a reader of a curated thesis cannot tell an author's considered qualification from an audit's marginalia, and once injected, the note reads as the document's own voice.

**The audit's output is the corrected document, plus its record in `docs/audit_ledger.md` and open questions in `docs/research_questions.md`. The record of the audit lives only in those two files. The document is not a notepad.**

### 3.6b The audit does not annotate, and does not open strains

`EDITORIAL_ANNOTATION_MANUAL.md` and `EVOLVING_CONCEPTUAL_STRAINS.md` are a **separate editorial system with a different job**: recording where the corpus's own conceptual position has *already* moved, as established by another document in the library. It has two hard preconditions this job cannot satisfy on its own:

- the corrected position must **already exist** in a `data/` document, and
- it must actually cover the specific claim being annotated.

**The annotation system is never a way to flag deferred, pending, or future work.** Opening a strain to mark "this needs to be redone" dresses an unresolved task up as a settled correction: a reader meeting the header block believes the position has been corrected when nothing has been done at all. That inverts the system's entire purpose.

So: **this job does not add annotations, does not add strains, and does not edit `EVOLVING_CONCEPTUAL_STRAINS.md`.** If a document looks like it genuinely warrants an annotation, that is a finding to hand the author — ledger + research question — not an edit to make. The author decides, or authorizes a separate annotation pass that is not this job.

### 3.7 Propagate across the corpus

**Every correction must be chased through the whole library.** A fixed citation in one document and the same broken citation in eleven others is not a fix.

For each correction applied:

```bash
grep -rn "<the wrong figure / citation / claim>" data/
```

Search the distinctive phrasing, the number, the author name, the section reference — several angles, since the same error rarely appears in identical words. Then:

- Apply **the same fix** at **every** occurrence — the same corrected citation, figure or fact, adapted only as far as the surrounding sentence grammatically requires.
- Check documents that cite the corrected document, and confirm what they carry forward is still true. Where it is not, that is a finding for the ledger — not licence to edit a document you have not read.

Propagation edits are allowed outside the night's batch. They are the only edits that are, and only in the form above: § 3.6a's prohibition on notes applies with full force here, where you have not read the document you are touching.

Those documents are **not** marked audited in the ledger — they received one correction, not a full read.

---

## Section 4 — Close out the run

1. **Ledger** — flip this run's `in-progress` rows to their final outcome: date, path, sources checked, corrections applied, propagation reach, open questions. Never leave a row `in-progress` in a run that completed.

2. **Handoff** — rewrite the ledger's *"Next run starts here"* block. This is the single most useful thing you leave behind, because the next run begins with no memory of tonight. Replace it wholesale (it describes the present, not history) with:
   - Which documents the next run should take, and why
   - Propagation debt: corrections that need chasing further than you got
   - Questions logged tonight that are waiting on an external answer
   - Anything surprising that would cost the next run time to rediscover

3. **Pattern register** — if this run hit a defect class that will recur (a citation style that fabricates, a statistic copied wrong across many files, a source that keeps appearing dead), add or update its entry in the ledger's pattern register: what it looks like, how you handled it, where you have seen it. Knowledge that stays in one night's run log is knowledge the job loses.
4. **Research questions** — append anything unresolved to `docs/research_questions.md` in the documented format with the right `[NLM]` / `[GDR]` / `[NDE]` target tag.
5. **Strains** — nothing to do. This job does not touch `EVOLVING_CONCEPTUAL_STRAINS.md` (§ 3.6b). If something there looks stale or newly warranted, say so in the ledger and leave it to the author.
6. **Commit** — one commit per audited document plus one for the ledger, so review is readable.
7. **Verify** — `git status`, then **read the full `data/` diff line by line** (`git diff origin/dev -- data/`) and confirm every changed line is a correction from § 3.6's table. Any line that records the audit — a note, a marker, an aside about what was checked or doubted — is a violation of § 3.6a; revert it before pushing. Confirm nothing unintended was touched.

### Out of bounds

Do not, in this job:

- **Write a note, marker, aside, or any other audit commentary into a `data/` document** — see § 3.6a. This is the prohibition most easily broken and the one that does the most damage. (Correcting the document's own text is not commentary — that is the job.)
- **Add an annotation, add a strain, or edit `EVOLVING_CONCEPTUAL_STRAINS.md`** — see § 3.6b
- Run `scripts/mirror_library_to_drive.py` — it pushes outside the repo; Drive sync stays manual
- Run `scripts/rename_to_titles.py --apply`, or reorganize/reclassify/move files
- Rewrite documents wholesale, or edit anything outside the batch except correction propagation
- Touch `CLAUDE.md`, or any repo other than `literary-compilation` (the others are read-only reference here)
- Merge the PR, or push directly to `dev` or `main`

### Open the PR

Push and open a PR against `dev`:

```bash
git push -u origin claude/nightly-audit-$(date +%F)
```

Title: `Nightly source audit — YYYY-MM-DD — <N> documents`

Body:

```markdown
## Documents audited
- `data/<folder>/<file>.md` — <one line: what was found>

## Source corrections
<Per document: what was wrong, what it is now, how it was verified.
 Fabricated or removed citations called out explicitly.>

## Claim corrections
<What was corrected in place, and what was found but deliberately left alone — with why
 each was routed that way. Findings left alone are the normal case, not a shortfall.>

## Corpus propagation
<Every file touched outside the batch, and the correction it carries.>

## Open questions
<Logged to research_questions.md — what could not be settled from the library, and what it needs.>

## Verification notes
<How external sources were checked. Any PDF substitutions. Anything left unverified.>

---
_Editorial PR. Any agent acting on review comments here: read `.claude/skills/steward/SKILL.md`
and Section 0 of `docs/NIGHTLY_SOURCE_AUDIT.md` before pushing. Corrections of record are
fixable; interpretive positions are the author's._
```

**If no PR tooling is available in the run** (no `mcp__github__*` tools and no `gh` CLI), the branch push is still the deliverable. Push it, then send this URL instead — it opens GitHub's PR form pre-filled from the branch, so the PR is one click away:

```
https://github.com/kayna-of-light/literary-compilation/compare/dev...claude/nightly-audit-YYYY-MM-DD?expand=1
```

Put the PR body you composed into the notification so it can be pasted straight in. Note in the ledger that the PR was not opened automatically.

Then send the notification: the PR link, documents audited, corrections applied, files propagated to, and open questions. Keep it short enough to read on a phone.

If the run found nothing to correct, say so plainly — a clean batch is a real result. Still open the PR for the ledger update.

---

## Failure handling

| Situation | Response |
|---|---|
| Batch bigger than the session can finish | Finish the documents you started, ledger only those, PR the partial batch. Never half-audit a document and mark it done. |
| External verification unavailable (network, paywall) | Mark the source unverified in the ledger, leave the citation, log a research question. Do not guess. |
| Previous night's PR still open | Expected. Exclude its documents and branch from `dev` as normal. |
| Merge conflict with an earlier audit branch | Almost always the ledger. Keep both sets of rows. |
| Correct stance genuinely unclear | No edit. Research question. This is the designed outcome, not a failure. |
