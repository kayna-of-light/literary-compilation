# Bibliography Standards

**Created**: 2026-09-21
**Purpose**: One standard for source listings in `data/` documents — what a "Works Cited" section contains, how each entry is formatted, and what does not belong in it.
**Supersedes**: The `[P]`/`[S]`/`[T]`/`[E]`/`[W]` inline type-code system formerly described in `CLAUDE.md`. That system saw almost no use in the corpus and is retired — see § Retired below.
**Related**: `docs/EDITORIAL_ANNOTATION_MANUAL.md` (a separate system, for tracking conceptual evolution — see § Not This below) · `docs/NIGHTLY_SOURCE_AUDIT.md`

---

## The model

The standard already exists in practice. The `data/00_Master_Theses/` documents show it consistently — for example the Works Cited section of *"The River and the Vessel"*:

```markdown
## 14. Works Cited

**Primary Sources:**

1. Swedenborg, Emanuel. *Arcana Coelestia* (Heavenly Secrets). 12 vols. London: 1749-1756. Cited by section number (§).
2. Swedenborg, Emanuel. *Heaven and Hell* (*De Coelo et Ejus Mirabilibus et de Inferno*). London: 1758. Cited by section number (§).
5. Gardner, Iain. *The Kephalaia of the Teacher: The Edited Coptic Manichaean Texts in Translation with Commentary.* Nag Hammadi and Manichaean Studies 37. Leiden: Brill, 1995.

**Scholarly Works:**

8. Von Petzinger, Genevieve. *The First Signs: Unlocking the Mysteries of the World's Oldest Symbols.* New York: Atria, 2016.
16. Klinghardt, Matthias. *The Oldest Gospel and the Formation of the Canonical Gospels.* Leuven: Peeters, 2021.

**Internal Library Documents:**

17. [The Mountain and the Pillar: Externalization as Compensation in Paleolithic and Early Neolithic Symbolic Systems](../06_Mythological_Studies/The%20Mountain%20and%20the%20Pillar_%20Externalization%20as%20Compensation%20in%20Paleolithic%20and%20Early%20Neolithic%20Symbolic%20Systems.md). The sign corpus at the resolution its primary sources support, and the doctrinal sequence of *AC* §920 compared against the archaeological one.

**Data Sources:**

34. NDERF (Near Death Experience Research Foundation). Approximately 3,500 structured NDE accounts. Analyzed in the structured-data-analysis project (projects/nde/).
```

This is the target for every `data/` document with a source list. What follows makes it explicit and gives it authority to override the weaker practices found elsewhere in the corpus — long numbered lists of bare URLs, and the abandoned `[P]`/`[S]`/`[T]` bracket notation.

---

## Structure

A document's source list is one section, headed **`## Works Cited`** (numbered as part of the document's own section sequence where the document numbers its sections — `## 14. Works Cited`, matching the surrounding convention). Do not use `References`, `Bibliography`, or `Sources` for new or rewritten sections; `Works Cited` is the corpus's dominant convention and the one this standard fixes on.

Entries are numbered continuously across the whole section, and grouped under whichever of these four category headers actually have entries — omit a category with nothing in it, and do not invent others:

| Category | What goes here |
|---|---|
| **Primary Sources** | The original texts under analysis — Swedenborg's works, Scripture, ancient texts, primary manuscripts |
| **Scholarly Works** | Secondary academic literature — monographs, peer-reviewed papers, dissertations |
| **Internal Library Documents** | Other `data/` documents in this repository, cited by relative link |
| **Data Sources** | Named datasets analyzed elsewhere in the ecosystem — NDERF, DOPS, MallWorld, etc. |

A fifth category, **Web Sources**, is permitted for a durable, attributable web resource that is not an academic work — an organization's published page, a news article, a public-domain excerpt — when no better-categorized citation applies. It still gets a full citation (§ Format below), never a bare link.

---

## Format

### Primary and Scholarly Works

Chicago-style, full citation, as the Master Theses example shows:

```
N. Author, First. *Title of Work.* Additional detail (translator, series, volume) where relevant. City: Publisher, Year.
```

Swedenborg's works are cited by section number (§) in the body text, and the Works Cited entry names the specific published edition or translation used — never a personal scan. If several editions or translations are consulted across the corpus, this is not a problem to standardize away; cite the one actually used for each document.

### Internal Library Documents

A relative markdown link to the file, followed by one sentence on what it specifically contributes to this document's argument — not a restatement of its title:

```
N. [Full document title as it appears as an H1](../folder/Encoded%20File%20Name.md). What this document specifically contributes to the present argument.
```

### Data Sources

Name, one line on scale (N, what it is), and a pointer to where it lives if analyzed elsewhere:

```
N. NDERF (Near Death Experience Research Foundation). Approximately 3,500 structured NDE accounts. Analyzed in the structured-data-analysis project (projects/nde/).
```

### Web Sources

```
N. Author or Organization. "Title of Page or Article." *Site Name*, Date if known. URL.
```

A URL is present but is not the citation — the author/organization and title carry the reference. A bare `N. Some Title, https://...` line is not an acceptable entry in any category.

---

## What does not belong in a Works Cited section

### No personal file links

**Never cite a `drive.google.com` link, or any other personally-hosted file, as a source.** This includes scans of published works (a PDF of Swedenborg's *Spiritual Diary* sitting in a personal Drive folder), personal notes, and any file a reader other than the corpus's author cannot open.

Every citation in this corpus should be independently verifiable by someone who does not have access to the author's Drive. If a source has a personal-Drive citation today:

- If it is a published work, cite the actual publication — publisher, edition, translator — under **Primary Sources** or **Scholarly Works**, exactly as `00_Master_Theses` already does for Swedenborg, Gardner, Pope, and the rest.
- If it is genuinely part of this corpus's own material (an experience log, a research note that belongs in `data/`), it is an **Internal Library Document**, cited by relative link — not an external Drive link.
- If neither applies — a private file with no public existence and no place in this corpus — it is not a citable source. Either the claim it supports needs a real source, or it should be marked `[TRACE NEEDED]` and logged to `docs/research_questions.md`. A private link that only the author can open is not a source; it is a citation of something the reader is being asked to trust without being able to check.

This is not a special pass over the 35 documents that currently carry `drive.google.com` citations — the nightly source audit (`docs/NIGHTLY_SOURCE_AUDIT.md`) treats this as an ordinary correction of record and cleans them as it reaches them, using the routing above.

### No unmoderated or reposted sources

Reddit, Quora, Scribd, forum threads, comment sections, and similar user-generated platforms are not citable sources in a Works Cited section, regardless of what they're hosting or how confidently they're worded. This is not a style preference — the corpus's much of its material came out of Gemini Deep Research, which cites these routinely, and as of 2026-09-21 they appear in **over 90 documents**. This is corpus-wide, not incidental.

Two distinct problems hide under "not a citable source," and they route differently:

**Repost hosts (Scribd, Academia.edu uploads by someone other than the author, document-sharing sites).** These usually carry a real underlying work — a journal article, a book chapter, a published sampler — uploaded without attribution to the original. The task is not to reformat the Scribd link; it is to **identify what the reposted document actually is** and cite the original publication instead:

- Search the reposted title, distinctive phrases from it, or its apparent author for the original: a journal, a publisher, an institutional repository. Most resolve — a "Genesis 2:5-7" Scribd upload is very likely a specific, findable journal article; a study-Bible "sampler" is very likely that Bible's actual publisher edition.
- Cite the original under **Primary Sources** or **Scholarly Works** once found, exactly as any other published work.
- If no original can be identified after a real attempt — not a single search — treat it as unverifiable (below).

**Claim sources (Reddit posts, forum threads, Quora answers, comment sections).** These are not documents standing in for a real source; they are someone's unverified assertion, typically anonymous, with no editorial or institutional check on it. A citation here is not a formatting problem — it means **the claim itself was never actually verified**, only found stated somewhere. The forum post is never the fix:

- If the claim is true and significant, it is independently checkable — find the real source that supports it (a scholarly work, a primary text, a dataset) and cite that instead. The Reddit thread disappears from the Works Cited entirely; it was never evidence, only a lead.
- If a genuine, real attempt to independently verify the claim turns up nothing — no scholarly treatment, no primary-source support — the claim is **unverified content masquerading as a citation**, and the routing is the same as an uncheckable personal file above: mark `[TRACE NEEDED]` and log a research question, or remove the claim if it is not load-bearing to the document's argument. Never leave the Reddit link standing "because the claim seems plausible." Plausibility is not verification, and an anonymous forum post asserting something is not stronger evidence than no citation at all — it is weaker, because it dresses an unverified claim as if it were checked.

**What is not covered by this section**: an institutional or identifiably-authored web page — a university's own site (`rsc.byu.edu`), a named scholar's own page, an institutional repository (`deepblue.lib.umich.edu`, `epublications.marquette.edu`), a serious subject-specific project with named editorial oversight (`thetorah.com`) — is not an "aggregator" merely because it isn't a print publisher. These are legitimate **Web Sources** (§ Format above) when no better-categorized citation applies. The test is real authorship and some form of accountability for what's published, not the domain's appearance or whether it charges for access.

This is exactly the class of correction `docs/NIGHTLY_SOURCE_AUDIT.md` § 3.3's "Quality" check exists for, and it is **not optional or secondary to claim-level fact-checking** — see that procedure's § 3.4b.

### No type-code brackets

Do not tag entries `[P]`, `[S]`, `[T]`, `[E]`, or `[W]`. The category header already states what kind of source it is — a bracket in front of every line number is redundant markup that only two documents in the entire corpus ever adopted. See § Retired.

### No audit provenance

Nothing about *when* or *how* a source was checked belongs in the document — no "(verified 2026-09-21)", no "(confirmed in nightly audit)", no reference to `docs/audit_ledger.md` or a PR number. That state lives exclusively in the ledger. A Works Cited section describes what was consulted, not the history of someone checking that it was consulted correctly. This is distinct from — and must not be confused with — the editorial annotation system below.

---

## Not this: editorial annotations are a separate system

`docs/EDITORIAL_ANNOTATION_MANUAL.md` governs a different mechanism: `[CORRECTION #N]`, `[EVOLVED #N]`, and the header block that marks where a document's *conceptual position* has been superseded by later understanding. That system is unaffected by this document and continues exactly as specified there. The two are easy to conflate because both are bracketed inline markers, so the distinction is worth stating plainly:

- **Bibliography standards** (this document) govern how a *source* is cited — is it real, is it attributed correctly, is it reachable.
- **Editorial annotations** (`EDITORIAL_ANNOTATION_MANUAL.md`) govern how a *claim* is flagged when the corpus's own understanding has moved past what the document says.

A citation cleanup is never an occasion to add or remove an editorial annotation, and an editorial annotation is never a substitute for fixing a bad citation.

---

## Retired: the `[P]`/`[S]`/`[T]`/`[E]`/`[W]` protocol

`CLAUDE.md` formerly specified inline type codes — `[P]` Primary, `[S]` Secondary, `[T]` Tertiary, `[E]` Empirical, `[W]` Web — to be prefixed to every citation in a source chain. In practice the corpus never adopted this: as of 2026-09-21, two documents out of 250 use it. The category-grouped Works Cited format above carries the same information (what kind of source this is) without the bracket notation, and is what the corpus actually does.

The two documents still carrying the old bracket notation do not need a special pass — clean them up under this standard whenever the nightly audit or any other edit touches them, the same as any other formatting inconsistency.

The concepts underneath the retired protocol remain sound and are restated here without the notation:

- **Pursue the original.** If a document cites Swedenborg via a secondary source, cite Swedenborg directly with book and section.
- **Verify Gemini references.** When Gemini Deep Research cites an internal document, check whether the claim actually originates from an external source — internal synthesis is valid but should not stand in front of the original evidence.
- **Flag untraced claims.** Mark `[TRACE NEEDED]` (this one marker survives — it is a claim-level flag, not a source-type tag) when the original source cannot be found, and log it to `docs/research_questions.md`.
