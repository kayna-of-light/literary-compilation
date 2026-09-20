---
name: steward
description: Repository guidance for any agent watching or auto-fixing a pull request in literary-compilation. Read before acting on CI events, review comments, or PR feedback. Covers what these PRs contain, which changes may be pushed unattended, and the methodological constraint that governs every edit. Keywords: PR, pull request, review comment, auto-fix, CI, steward, babysit, watch.
---

# PR Steward — literary-compilation

Guidance for any agent acting on a pull request in this repository: watching CI, responding to review comments, or pushing fixes unattended.

**Read this before your first push in response to any PR event.**

## What these PRs contain

This repository is not code. It is a research corpus — 250 markdown documents synthesizing consciousness studies, Swedenborgian theology, biblical scholarship, and mythological analysis.

Most PRs here come from the nightly source and claim audit ([`docs/NIGHTLY_SOURCE_AUDIT.md`](../../../docs/NIGHTLY_SOURCE_AUDIT.md)). Their diffs are citations, corrections, editorial annotations, and ledger updates. A "fix" is an editorial judgment about scholarship, not a code change.

That changes what unattended pushing means. A bad code fix fails a test. A bad editorial fix quietly misrepresents the corpus and may not be caught for months.

## The binding constraint

**Before pushing any change in response to a review comment, read Section 0 of [`docs/NIGHTLY_SOURCE_AUDIT.md`](../../../docs/NIGHTLY_SOURCE_AUDIT.md).** It is short and it governs every edit in this repository.

The one-line version, which does not substitute for reading it:

> This corpus holds a post-materialist position as a hypothesis under test against data. It is not a bias to be corrected away. An **error of record** — a citation that does not exist, a wrong section number, a statistic disagreeing with its dataset — is yours to fix. An **interpretive position** is not, and must never be "corrected" toward a mainstream reading.

The specific failure to avoid: a reviewer leaves an open-ended note like *"this claim seems strong"* or *"is this well supported?"*, and the response is a hedge, a disclaimer, or a recruited counter-argument. `CLAUDE.md` forbids all three. Reading a comment that way inverts the project's stance while appearing responsive.

When a comment's intent is ambiguous, **ask rather than push**. A reply costs a round trip. A wrong edit costs the corpus.

## What you may push unattended

| Feedback | Action |
|---|---|
| A specific factual correction ("this is §84, not §83") | Push it |
| A citation the reviewer says is wrong or fabricated | Verify, then push |
| Typo, formatting, broken link, malformed annotation | Push it |
| Annotation placement ("this needs an inline note too") | Push it, following `EDITORIAL_ANNOTATION_MANUAL.md` |
| "This reading is wrong" / "this overstates" | **Reply, do not push.** Editorial judgment is the author's. |
| Anything whose correct resolution is not settled by the library | **Reply, do not push.** Log a research question instead. |

When you do push, keep the audit's own rules: corrections propagate corpus-wide (`grep` the library from several angles), and annotations follow the manual — header block plus at least one inline note, since NotebookLM fragments documents and does not carry context across sections.

## CI

This repository has no `.github` directory and no workflows. There is no test suite, linter, or build.

If a check does appear on a PR, it is from a GitHub App rather than repo configuration. Read what it actually reports. **Do not invent a fix for a check you do not understand**, and never edit documents to satisfy a check whose purpose is unclear — in a prose corpus there is no failing test to make green, so a speculative "fix" is just an unreviewed content change.

## Ledger consistency

The audit's state lives in [`docs/audit_ledger.md`](../../../docs/audit_ledger.md). It is how each nightly run knows where the pass has reached.

If a push changes what a PR actually did — a correction withdrawn, a document turning out clean — update the matching ledger row in the same push. A ledger that disagrees with its own PR misleads every later run, and those runs have no memory to catch it.

Do not edit the *"Next run starts here"* block from a PR response. It belongs to the run that wrote it.

## Scope

Never, in response to a PR event:

- Merge the PR, or push to `main`
- Edit `CLAUDE.md`
- Run `scripts/mirror_library_to_drive.py` — it publishes outside the repo
- Run `scripts/rename_to_titles.py --apply`, or move, rename, or reclassify files
- Expand the PR beyond what the review asked for
- Rewrite a document wholesale

The author reviews every PR in this repository. Nothing here needs to be resolved without her.
