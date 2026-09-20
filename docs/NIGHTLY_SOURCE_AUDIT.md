# Nightly Source & Claim Audit — Operating Procedure

**Created**: 2026-09-20
**Runs**: Automated, nightly at 02:00 Europe/Amsterdam
**State**: [`audit_ledger.md`](audit_ledger.md)
**Related**: [`EDITORIAL_ANNOTATION_MANUAL.md`](EDITORIAL_ANNOTATION_MANUAL.md) · [`EVOLVING_CONCEPTUAL_STRAINS.md`](EVOLVING_CONCEPTUAL_STRAINS.md) · [`research_questions.md`](research_questions.md)

---

## Purpose

Work through the `data/` library a few documents at a time, reading each one completely, verifying that every source is real, correctly cited, traced as far back as it goes, and of high quality — and that every claim the document makes is correct. Apply corrections through the editorial tracking system, propagate them across the corpus, and open a PR for review.

This is an **unattended** run. Nobody is watching it. That shapes every rule below: when the correct action is not established, the run does not guess — it logs a research question and leaves the text alone.

---

## Section 0 — Methodological Baseline (read first, every run)

**Before touching any document, read `CLAUDE.md` in full.** Not a skim. The stance it sets is the whole point of this project, and the most damaging thing this job could do is quietly erode it.

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

In scope (correct these):

- A citation that does not exist, or does not say what the document claims it says
- A wrong section number, date, page, name, manuscript siglum, or statistic
- A quotation attributed to the wrong author or work
- A statistic that disagrees with the dataset it came from
- A claim that overstates the reach of the source under it
- A source chain that stops short of an available primary source
- A dead, redirected, paywalled-with-no-alternative, or low-quality source where a better one exists

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

**Batch size: 3 documents.** Drop to 1–2 if they are long or corrections run deep. Never exceed 4. Depth per document matters more than count; this pass takes as many nights as it takes.

Selection must be resumable across fresh sessions and must not collide with a previous night's unmerged PR.

```bash
cd literary-compilation
git fetch origin --prune
git checkout -B claude/nightly-audit-$(date +%F) origin/main
```

Build the exclusion set from **three** places:

1. `docs/audit_ledger.md` on `main` — every document already audited.
2. Every unmerged `origin/claude/nightly-audit-*` branch — read each one's ledger, since those documents are audited but not yet merged:
   ```bash
   for b in $(git branch -r --list 'origin/claude/nightly-audit-*' --no-merged origin/main); do
     git show "$b:docs/audit_ledger.md" 2>/dev/null
   done
   ```
3. Any open PR titled `Nightly source audit — …`.

Then pick from what remains, in this priority order:

1. Documents carrying an existing `[TRACE NEEDED]` marker
2. Documents listed as unfinished in the `EVOLVING_CONCEPTUAL_STRAINS.md` review task list
3. Documents still containing `drive.google.com` links
4. Documents with a bibliography but no editorial header block
5. Everything else, oldest-modified first

**Never prioritize by folder, domain, or subject matter.** Every criterion above is a property of a document's *state* — a marker present, a link unconverted, an annotation missing — and applies identically across all of `data/`. The pass is not steered toward any thematic area.

This matters for what the audit produces. A pass weighted toward some folders would verify parts of the corpus more heavily than others, and the resulting picture of the library's source quality would reflect the selection rule rather than the library. Within a priority tier, take documents in whatever order the filesystem returns them.

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
| **Typed** | Marked `[P]` / `[S]` / `[T]` / `[E]` / `[W]` per the Source Tracing Protocol |
| **Quality** | Primary over secondary; academic for historical claims; first-person for experiential claims |

Use `WebSearch` / `WebFetch` for external verification. **Never fetch a URL ending in `.pdf`** — it crashes the session. Use the abstract, the publisher landing page, or an HTML version, and note the substitution.

Cross-repo statistics (NDE figures, DOPS counts, χ² values) are verified against **`structured-data-analysis`**, which is the source of truth for them. It is checked out alongside this repo. If a figure in a `data/` document disagrees with the dataset, the dataset wins and the document is corrected.

Apply the Gemini rule from `CLAUDE.md`: where a citation points at an internal document, check whether the claim actually originates externally. Internal synthesis is a legitimate source, but it must not stand in front of the original evidence.

### 3.4 Clean the source list

- Replace `drive.google.com` links with internal repo links — `python scripts/normalize_internal_links.py --only "<relative path>"` to preview, `--apply` to write.
- Replace a weak source with the better one where a better one exists, and say so in the ledger.
- Complete partial references to full scholarly form.
- Remove a citation **only** when it is fabricated or wholly unverifiable — and then say so explicitly in the PR. Never silently drop a reference.
- Add type codes. Preserve the full chain, not just the endpoints.

### 3.5 Validate the claims

Read for correctness within the framework — `CLAUDE.md` § "Valid Critiques":

- Internal inconsistency within the document
- Contradiction with an established position elsewhere in the corpus
- Factual errors: dates, names, numbers, manuscript sigla, attributions
- Source chain gaps
- A claim reaching further than its evidence

Where a document and the corpus disagree, establish which is current before editing. `EVOLVING_CONCEPTUAL_STRAINS.md` is the register of what has been superseded.

### 3.6 Apply corrections

Route each finding by kind. **This table is the operative rule** — it reconciles "fix what is wrong" with the manual's "preserve the original":

| Finding | Action |
|---|---|
| Wrong citation, section, date, name, siglum; dead link; fabricated reference | **Fix in place.** An error of record is not a position — nothing is preserved by keeping it wrong. |
| Statistic disagreeing with its dataset | **Fix in place**, naming the source of truth in the ledger. |
| Position superseded by later corpus understanding | **Annotate**, do not rewrite. Header block + at least one inline note, per the manual. |
| Claim overstating its source's reach | **Annotate** `[CRITICAL ANALYSIS #N]` and narrow the stated reach. Do not delete the claim. |
| Claim untraceable after genuine effort | Mark `[TRACE NEEDED]`, log in `docs/research_questions.md`. Leave the text. |
| Correct treatment not established by the library | **No edit.** Research question + ledger note. |

Annotations follow `EDITORIAL_ANNOTATION_MANUAL.md` exactly: header block after the title, at least one inline note in the body (NotebookLM does not carry context across fragments), `Established correction (library)` pointing at a document inside `data/`, no folder path, no extension.

If a correction represents genuinely new conceptual evolution, add a strain to `EVOLVING_CONCEPTUAL_STRAINS.md` and use its number. Do not invent strain numbers that do not exist there.

### 3.7 Propagate across the corpus

**Every correction must be chased through the whole library.** A fixed citation in one document and the same broken citation in eleven others is not a fix.

For each correction applied:

```bash
grep -rn "<the wrong figure / citation / claim>" data/
```

Search the distinctive phrasing, the number, the author name, the section reference — several angles, since the same error rarely appears in identical words. Then:

- Apply the same fix, or the same inline annotation, at **every** occurrence.
- Check documents that cite the corrected document, and confirm what they carry forward is still true.
- Update the strain's document checklist in `EVOLVING_CONCEPTUAL_STRAINS.md`.

Propagation edits are allowed outside the night's batch. They are the only edits that are. Those documents are **not** marked audited in the ledger — they received one correction, not a full read.

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
5. **Strains** — update `EVOLVING_CONCEPTUAL_STRAINS.md` checkboxes; add a strain if warranted.
6. **Commit** — one commit per audited document plus one for the ledger, so review is readable.
7. **Verify** — `git status`, review the full diff, confirm nothing unintended was touched.

### Out of bounds

Do not, in this job:

- Run `scripts/mirror_library_to_drive.py` — it pushes outside the repo; Drive sync stays manual
- Run `scripts/rename_to_titles.py --apply`, or reorganize/reclassify/move files
- Rewrite documents wholesale, or edit anything outside the batch except correction propagation
- Touch `CLAUDE.md`, or any repo other than `literary-compilation` (the others are read-only reference here)
- Merge the PR, or push to `main`

### Open the PR

Push and open a PR against `main`:

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
<What was corrected in place vs. what was annotated, and why each was routed that way.>

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
https://github.com/kayna-of-light/literary-compilation/compare/main...claude/nightly-audit-YYYY-MM-DD?expand=1
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
| Previous night's PR still open | Expected. Exclude its documents and branch from `main` as normal. |
| Merge conflict with an earlier audit branch | Almost always the ledger. Keep both sets of rows. |
| Correct stance genuinely unclear | No edit. Research question. This is the designed outcome, not a failure. |
