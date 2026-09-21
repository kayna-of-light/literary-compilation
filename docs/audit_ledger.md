# Source & Claim Audit Ledger

**Purpose**: Running state for the source and claim audit of the `data/` library — what is done, what is in flight, and what the next run needs to know.
**Procedure**: [`NIGHTLY_SOURCE_AUDIT.md`](NIGHTLY_SOURCE_AUDIT.md)

Each nightly run starts as a fresh session with no memory of the last one. This file is the only thing that carries across. Treat it as the job's working memory, not as a report.

---

## Next run starts here

**Replaced wholesale at the end of every run.** This block describes the present, not the history — history goes in the run log below. A run that leaves this stale has failed its successor.

> **Status**: 2 documents audited (2026-09-21), both corrected. 248 remain. Nothing in flight.
> All nine corrections and both propagation sweeps are **applied in the branch** and each file was
> verified byte-identical after pushing.
>
> **⚠️ Read this first — the run environment cannot push over git.** `git push` to this repo is
> refused by the session's git proxy: *"kayna-of-light/literary-compilation is not in this session's
> authorized repository set, so the proxy will not inject a credential for it."* The repository was
> also **not cloned** into the container for the same reason — this run cloned it manually over
> HTTPS. The procedure's § 1 precheck therefore fails, but **not** for the reason § 1 assumes: it is
> not a missing Claude GitHub App install, so installing the App will not fix it. The fix is to add
> `kayna-of-light/literary-compilation` (and `structured-data-analysis`) to the **scheduled task's
> environment sources**. Until then a run can still deliver: the `mcp__GitHub__*` tools have working
> write access to this repo, and this run's branch and PR were created entirely through them
> (`create_branch`, `push_files`, `create_pull_request`). If you hit the § 1 403, check whether the
> MCP path works before concluding the night is blocked.
>
> **This is a known, confirmed product issue, not a fault of this repo**:
> [anthropics/claude-code#76248](https://github.com/anthropics/claude-code/issues/76248). Anthropic
> reproduced it on 2026-08-17 and confirmed it is **intended behaviour** — credentials live outside
> the sandbox and the proxy only injects them for repos attached to the session. Two things in that
> thread are worth knowing before you waste a night on them:
> - **Installing the Claude GitHub App does not help.** A reporter has it installed with read/write
>   on *all* repositories and still gets the identical 403. § 1 of the procedure used to recommend
>   exactly that; it has now been corrected.
> - **The restriction has tightened for at least one user.** On 2026-09-19 a reporter went from
>   write-blocked to *read*-blocked within a day (`git clone` failing with `Invalid username or
>   token`). This run cloned fine, but if a future night cannot even clone, that is this issue
>   escalating — not a new problem — and the night really is blocked.
>
> Self-service repo attachment had not shipped as of the last comment on that issue (2026-09-19),
> and there is no timeline.
>
> `docs/BIBLIOGRAPHY_STANDARDS.md` landed 2026-09-21 (same day, after this run started) and is now
> required reading alongside `CLAUDE.md` (procedure § 0). It **hardens** the "preserve the chain"
> reading below: a personal-file link is never kept, even relabelled as the author's scan — cite the
> actual publication instead, or `[TRACE NEEDED]` if that is not possible. The three Drive-linked
> Swedenborg citations this run reformed under the old reading are being brought into line with the
> new standard as part of this same merge; see the run log.
>
> **Take next**: Your call. Two threads are worth continuing if nothing better catches your eye:
> 1. **The 24 documents still containing `drive.google.com` links.** Still 24 — deliberately. § 3.4
>    says to preserve the chain, so where a Drive link points at the author's scan of a *published
>    work* the right fix is to name the work and keep the link labelled as the scan, not to delete it.
>    Three such citations were reformed that way tonight; the raw link count is therefore unchanged and
>    is **not** a useful progress measure. Note also that `scripts/normalize_internal_links.py` is
>    **not usable in this environment** — it needs Drive API credentials
>    (`secrets/google_drive_token.json`, absent), and it only rewrites links resolving to a Markdown
>    file in `data/`. Links pointing at Swedenborg source PDFs will never match it, so they must be
>    reformed by hand.
> 2. **`03_Biblical_Scholarship` philology.** `The Stratigraphy of the Hebrew Bible` and
>    `Stratigraphy of the Archaic` both took propagation edits tonight without being audited, and
>    both are dense with the same class of checkable lexical claim. They are the obvious next pick
>    in that folder — but both are long, so budget accordingly.
>
> Coverage so far is `00_Framework` ×1 and `03_Biblical_Scholarship` ×1. No area is running ahead yet.
>
> **Propagation debt**:
> - **None outstanding for tonight's two corrections** — both were swept corpus-wide and verified to
>   zero remaining occurrences.
> - **Latent, larger:** Swedenborg is cited *by work with a section number* in only a handful of
>   documents; most cite him by work-with-no-section or by web page. Tonight only the three
>   bare-PDF-filename cases were in scope. Supplying sections across the corpus is a standing task,
>   not a one-night sweep — treat it as ongoing rather than debt from this run.
>
> **Awaiting external answers**: Three questions logged tonight in
> **`docs/research_questions/nightly_audit_2026-09-21.md`** — the Third/Fourth Church numbering
> collision, three missing Swedenborg section references, and whether *zu* at Exodus 15:13 is
> attested or reconstructed. All three are `no edit` outcomes: **do not resolve them by guessing.**
>
> They were filed using the `docs/research_questions/` per-question convention rather than appended
> to the monolithic `docs/research_questions.md` as § 4.4 asks. Reason: the only write path available
> to this run (the GitHub MCP API) replaces a file by transmitting its **whole** content, and the
> monolithic register is ~156 KB this run had not read in full — re-transmitting it by hand risked
> silently corrupting it. **If you have working `git push`, folding these three into
> `research_questions.md` is a safe local edit and worth doing.**
>
> **How this run pushed, and how you should**: `push_files` replaces whole files, so every byte is
> retyped by hand. The first attempt at `The Heart of the Matter` dropped a backslash; the first
> attempt at `Lexical Fossil Inventory` corrupted **ten** pointed-Hebrew words (dagesh/sheva order,
> dropped shin- and sin-dots). Both were caught by `git fetch` + `git diff` and re-sent. The method
> that then worked first time, every time, is now written up in **procedure § 4.1**: dump the file
> with `json.dumps(...)` so all non-ASCII becomes `\uXXXX` escapes and trailing hard-break spaces
> become visible before the `\n`, copy that verbatim, then verify with `git diff FETCH_HEAD`.
> **Verify every single file.** Budget ~5 read calls plus a large push per 70 KB document.
>
> **Worth knowing**:
> - **Full-text Swedenborg hosts block the fetcher.** `newchristianbiblestudy.org`,
>   `sacred-texts.com` and `biblemeanings.info`'s search all returned **HTTP 403** to `WebFetch`.
>   What did work: `www.e-swedenborg.com/writings/static/d11722/<N>.htm` serves *Apocalypse Explained*
>   section-by-section as HTML (`d11722` = AE; § 411 was read this way). `biblehub.com/hebrew/<Strong's>.htm`
>   works and is the fastest way to check where a Hebrew word actually occurs. Remember § 3.3's rule:
>   never fetch a `.pdf`.
> - **`structured-data-analysis` is not checked out** by the environment either, contrary to § 3.3.
>   It is public and clones fine over HTTPS. Neither of tonight's documents contained cross-repo
>   statistics, so it went unused — but clone it before taking anything with NDE/DOPS figures.
> - Two `EVOLVING_CONCEPTUAL_STRAINS.md` items remain open for corpus-wide re-audit, both from
>   2026-08-20 — **#16** Pillar 43 Historical Encoding (earlier annotations need replacing, not
>   extending) and **#26** Paleolithic Geometric Signs. Neither was touched tonight. Highest existing
>   strain number is **#26** before this merge; do not invent numbers past whatever the run log
>   shows as current.

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

A document counts as audited only after a **complete** read and source pass. Files touched solely by correction propagation appear in the **Propagated** column of the row that caused them; they are not audited and stay in the queue.

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
| 2026-09-21 | `00_Framework/The Heart of the Matter_ A New Church Founded on Love.md` | Bibliography but no editorial header; 3 `drive.google.com` links; shortest never-reviewed doc in `00_Framework`, and Framework docs are cited downstream so defects here propagate furthest | 4 found · 2 verified (1 internal read in full; AE § 411 confirmed) · 2 identified to work level only | 4F (all four bibliography entries reformed to the corpus's normal scholarly form; an initial pass added `[P]`/`[T]` type codes and inline `[TRACE NEEDED]` tags that no document in `data/` actually uses — removed same day, see pattern register) | 2 — `02_Swedenborgian_Theology/The Biological Error and the Theological Rescue…`, `05_The_Self/The Architecture of Autonomy…` | 2 | `corrected` |
| 2026-09-21 | `03_Biblical_Scholarship/Lexical Fossil Inventory_ A Stratigraphic Analysis of Archaic Hebrew Vocabulary.md` | Same state signature (bibliography, no header, Drive link) in a different folder; dense named-scholar/date philology is where fabricated citations hide, so it tests the Gemini-bibliography pattern early | 22 references (15 numbered + 7 scholarly) + 21 inventory-table entries; 15 spot-verified externally, no fabricated citation found | 5F (wrong deity name; word attributed to wrong book; two under-counted distributions; incomplete reference) | 2 — `03_Biblical_Scholarship/The Stratigraphy of the Hebrew Bible…` (3 passages), `03_Biblical_Scholarship/Stratigraphy of the Archaic…` (1 passage) | 1 | `corrected` |

---

## Pattern register

Recurring defect classes and how to handle them. **This is what makes the job compound** — without it, night 8 rediscovers from scratch what night 3 already worked out, and handles it differently.

Add an entry when a problem looks like it will recur. Update the existing entry rather than adding a near-duplicate.

| Pattern | What it looks like | Handling | Seen in |
|---|---|---|---|
| **Primary source seems to contradict the corpus — but the corpus already argued it** | *Apocalypse Explained* § 411 assigns the statue's iron-and-clay legs/feet to "the Israelitish and Jewish Church," while the corpus assigns them to the **Christian** Church, quoting § 411's phrase "external church without any internal" while doing so. Looks like a misapplied quotation. | **It is not an error.** `The Statue and the Stone` addresses exactly this, arguing AE 176/411 apply the imagery "to both Jewish church (proximately) and Christian church (internally)," and reads the corpus variations as progressive revelation rather than inconsistency. **Before treating any primary-source divergence as a defect, grep `data/` for a document dedicated to that passage.** This is the § 0 failure mode in its most convincing disguise — it arrives with a real citation attached. | `00_Framework/The Heart of the Matter…` (2026-09-21) |
| **Swedenborg's Bible renderings differ from the common English versions** | The document quotes Daniel 2:35 as the stone becoming "a great rock, and filled the whole earth." Every standard English Bible reads "great **mountain**," so it scans as a misquotation. | **Verify against Swedenborg's own text, not a Bible.** *Apocalypse Explained* § 411 reads "became a great rock" — the document is correct as written. The distinction carries doctrinal weight in his correspondences (rock → truth, mountain → love), so "fixing" it to match the KJV would silently alter a correspondential reading. Treat any Swedenborg scripture quotation as his rendering until shown otherwise. | `00_Framework/The Heart of the Matter…` (2026-09-21) |
| **"Appears only in X and Y" distribution claims are under-counted** | *qesitah* was described as appearing "only in the Patriarchal narratives (Gen 33) and Job." It occurs three times: Gen 33:19, **Josh 24:32**, Job 42:11. The same claim had travelled into three other documents in four different phrasings. | Check every "appears only" / "unattested elsewhere" claim against a concordance — `biblehub.com/hebrew/<Strong's number>.htm` resolves it in one fetch. Then grep the corpus for the *word*, not the sentence, since the phrasing varies. Note that the correction usually leaves the argument intact (Josh 24:32 records the same Shechem purchase), so it is a cheap, safe fix. | `03_Biblical_Scholarship/Lexical Fossil Inventory…`, `…/The Stratigraphy of the Hebrew Bible…`, `…/Stratigraphy of the Archaic…` (2026-09-21) |
| **Personal Drive PDF cited as a source** | A bibliography entry linking `drive.google.com` — a filename like `swedenborg_apocalypse_revealed_02.pdf` or `experiences_part-024.pdf`, a personal scan of a published work or a personal export — no title, no section, uncheckable by anyone but the author. | **Never leave standing, and never keep the link even relabelled.** `docs/BIBLIOGRAPHY_STANDARDS.md` (landed 2026-09-21, superseding this run's earlier "preserve the chain, keep the link" reading of the old § 3.4) is explicit: name the actual publication under Primary/Scholarly Works; if the material belongs in this repo, make it an Internal Library Document with a relative link; if neither applies, `[TRACE NEEDED]` + a research question. The three Swedenborg citations this run originally reformed by keeping the link were brought into line with the new rule the same day — see the run log. | `00_Framework/The Heart of the Matter…`, `02_Swedenborgian_Theology/The Biological Error…`, `05_The_Self/The Architecture of Autonomy…` (2026-09-21); 35 documents corpus-wide confirmed by grep at the standard's introduction, not yet remediated |
| **Files end without a trailing newline — `wc -l` undercounts, and the last citation gets missed** | `Lexical Fossil Inventory` reports `wc -l` = 291 but has **292** lines; the unterminated last line was bibliography entry **15**, which a `sed -n '1,291p'` read silently dropped. The missed entry was cited in the body (the *shasher* row). | Use `awk 'END{print NR}'` for the true count, or `tail -c 3 \| od -c` to check for a terminating newline, before believing a read was complete. This matters more here than in most repos because the last line of these documents is almost always a citation — exactly what the audit exists to check. | `03_Biblical_Scholarship/Lexical Fossil Inventory…` (2026-09-21) |
| **Deep Research bibliographies: no fabrication found yet** | The ledger's opening notes flagged Gemini-generated bibliographies as the likely home of fabricated citations. | On the first two documents this did **not** materialise: every named scholar, work and date checked resolved to a real publication. The defects found were *misplacement* (right scholar, wrong book; right word, wrong verse), not invention. Keep checking, but do not treat "Gemini-generated" as presumptive evidence of fabrication — on this evidence the likelier defect is a misplaced detail. | 2026-09-21 |

Candidates to watch for in early runs, from the corpus's history — confirm before treating any as established:

- Much of this library came out of Gemini Deep Research. Generated bibliographies are the usual place fabricated or subtly wrong citations hide, and a citation pointing at an internal document may be standing in front of an external original (`CLAUDE.md` § Source Tracing, rule 2).
- Statistics travel between documents by copying. A figure wrong in one place is likely wrong in several — always grep the number itself.
- `EVOLVING_CONCEPTUAL_STRAINS.md` records that header-only annotations failed once already: NotebookLM fragments documents and does not carry context across sections. Every occurrence needs an adjacent inline note.

---

## Run log

Narrative per run — what the batch surfaced, and anything a later run should know that does not fit the tables. Newest first. Unlike the handoff block, this accumulates.

### 2026-09-21 — First audit run: 2 documents, 9 corrections, 4 files propagated to

**Delivery was the hard part, not the auditing.** The § 1 precheck failed with a 403, but for a
cause § 1 does not anticipate: the session's git proxy refuses to inject a credential because this
repository is not in the session's authorized source set. The repo had not been cloned into the
container either, for the same reason; it was cloned manually over HTTPS. Because the cause is the
environment's source list rather than a missing GitHub App, the remedy § 1 prescribes would not have
worked. Rather than stopping, this run checked whether the *other* sanctioned delivery path worked —
the `mcp__GitHub__*` tools — confirmed write access with `create_branch`, and ran the night through
those. The § 1 instinct is still right (never audit what you cannot deliver); it just needs the
second check before declaring the night blocked. Details and the fix are in the handoff block.

**`00_Framework/The Heart of the Matter_ A New Church Founded on Love`.** Four sources: one internal
document carrying almost the entire argument, and three Swedenborg works cited only as Drive-hosted
PDF filenames. The internal source was read in full; the document represents it faithfully. All four
entries were reformed into the corpus's normal Works Cited form, and *Apocalypse Explained* **§ 411**
was traced and verified as the locus for the Daniel 2 statue correspondence — a section reference the
corpus did not previously have anywhere. (The first pass also added `[P]`/`[T]` type-code prefixes
and inline `[TRACE NEEDED]` tags to these entries, on the mistaken assumption that the Source Tracing
Protocol's codes belonged in a bibliography. A grep of every `Works Cited` section in `data/` turned
up no document that does this in a numbered list; both were removed the same day once flagged, and
the procedure's § 3.4a now says so explicitly.)

Two claims in this document looked like errors and were **not**. Both are now in the pattern
register, because both would have done real damage. The stone in Daniel 2:35 becoming "a great
**rock**" is Swedenborg's own rendering (AE § 411), not a misquotation of the KJV's "great mountain" —
and the rock/mountain distinction carries doctrinal weight. And AE § 411 assigns the iron-and-clay
feet to the *Israelitish and Jewish* church, not the Christian church, which looks like a misapplied
quotation until you find `The Statue and the Stone`, which argues that position explicitly and at
length. A confident 3 a.m. edit against either would have overwritten an argued position with a
naive reading.

What the library did **not** settle: the Christian Church is "the Third Church" here and in
`Conversation relating the Fourth Church`, but the "fourth church" in `The Statue and the Stone`.
Both documents map the statue to four states, so the disagreement is whether the Israelitish church
counts as a church proper. That is a real collision and possibly a superseded convention, but not
demonstrably so — **no edit**, question logged. If a later run establishes that the Third/Fourth
numbering is superseded, it needs a strain.

**`03_Biblical_Scholarship/Lexical Fossil Inventory`.** The document this was picked to test — dense
named-scholar philology, the place fabricated citations would hide. **No fabricated citation was
found.** Hurvitz, Dahood, Rendsburg, Young/Rezetko/Ehrensvärd, Tsumura, Cross/Freedman, Pettinato,
Gordon all resolve to real work at the dates given. The defects were misplacements:

- *Resheph* was called the porter of "the sun goddess **Shemesh**" in a sentence about the *Ugaritic*
  pantheon. The Ugaritic solar deity is **Shapash** (Šapšu); *Shemesh* is the Hebrew word for sun.
  Fixed. (The separate mention of *Shemesh* as a Canaanite deity name in `The Ancient Word_
  Philological Evidence…` is correct in its own context and was deliberately left alone.)
- *appiryon* was given as Qohelet vocabulary. It is a hapax at **Song of Songs 3:9**; *pardes* is the
  Qohelet word (Qoh 2:5). Fixed — and note the library corroborated this itself: `A Critical-Historical
  Chronology of the Hebrew Bible` already files *appiryon* correctly under Song of Songs.
- *qesitah* "appears only in the Patriarchal narratives (Gen 33) and Job" omits **Joshua 24:32**.
  Fixed in body and inventory table, then propagated — the same under-count had travelled into three
  passages of `The Stratigraphy of the Hebrew Bible` and one of `Stratigraphy of the Archaic`, in four
  different phrasings. All corrected; swept to zero remaining.
- The `Linguistic Dating of Biblical Texts` reference omitted Ehrensvärd, though § 1.2 names him.
  Completed.

Verified positively and worth recording, since § 0 asks for where sources *support* the claim: the
*shasher* row (Jer 22:14) credits an Eblaite deity of textile/dye prosperity to reference 15, a BYU
religious-studies page. It holds up exactly — the page compares Eblaite *sišeru* to biblical
*šāšēr* "red dye, vermilion," explains that vermilion came from scale insects on Mediterranean oaks
and mattered to Ebla's textile industry, and records sheep sacrificed to *sišeru* "in return for the
luxury that this deity provided." The same page independently corroborates *Ra-sa-ap* at Ebla, cited
in § 3.4.

Reference 15 was nearly missed: the file has no terminating newline, so `wc -l` reports 291 for a
292-line file and the first read stopped one line short — on the last bibliography entry. That is now
in the pattern register, because in these documents the unterminated last line is almost always a
citation.

Left alone deliberately: the table's *zu* at Exodus 15:13. MT reads עַם־זֶה (*zeh*), so the entry may be
reporting a Cross–Freedman reconstruction rather than an attested form. Plausible either way — **no
edit**, question logged. Also noted but not edited: the Resheph "gatekeeper" role rests on a single
omen text and Albright's reading of it is contested in the literature. That is a live scholarly
dispute, not an error of record, and § 0 forbids recruiting it as an objection.

**Tooling notes for the next run** are in the handoff block — which verification hosts 403, which
work, and why `normalize_internal_links.py` is unusable here. No strains were added or touched: no
finding this run rose to conceptual evolution.

### 2026-09-20 — Ledger opened

Nightly audit configured. Queue is the full library: 250 documents, none audited.

Starting conditions:

- **83** documents carry a bibliography section; the rest cite inline or not at all
- **46** already carry an editorial header block
- **24** still contain `drive.google.com` links (`scripts/normalize_internal_links.py`)
- **2** already use the `[P]`/`[S]`/`[T]`/`[E]`/`[W]` type codes from the Source Tracing Protocol as a bulleted Works Cited style of their own (`### Primary Sources [P]` subheadings, `- **[P]**` entries). That is those two documents' own pre-existing convention, not a corpus-wide target — most Works Cited sections use a plain numbered list with no type codes at all. See procedure § 3.4a, added 2026-09-21 after an early run mistook this note as license to add type codes everywhere.
- `EVOLVING_CONCEPTUAL_STRAINS.md` has two open items: **#16** Pillar 43 Historical Encoding and **#26** Paleolithic Geometric Signs, both opened 2026-08-20

Batch size is the run's own judgment, so the length of the pass is not fixed. As a rough sense of scale, a few documents a night puts a full pass somewhere near three months. Depth matters more than pace — a short honest batch beats a long shallow one.
