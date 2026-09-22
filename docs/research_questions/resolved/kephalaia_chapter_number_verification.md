# Kephalaia Chapter-Number Verification: Body-Cosmos Map and "Three Entreaties"

**Target**: `[GDR]`
**Status**: ✅ RESOLVED
**Date Added**: 2026-09-21
**Date Resolved**: 2026-09-22
**Priority**: HIGH
**Related Documents**:
- `data/08_Correspondential_Texts/The Garment and What Wears It_ Dating the Correspondential Substrate Beneath the Manichaean Kephalaia.md`
- `data/00_Framework/The Ancient Word Recovered_ Extracting the Correspondential Substrate of the Kephalaia.md`
- `data/06_Mythological_Studies/Two Registers of One Perception_ The Song of Solomon and the Regenerative Substrate of the Kephalaia.md`

## Original Question

The 2026-09-21 nightly audit of *The Garment and What Wears It* flagged, via web search alone (no primary-source access), that "Kephalaia Chapter 38" (cited as the body-cosmos/soul-tissue map) and "Chapter 115" (cited as the "Three Entreaties" regenerative narrative) might be mis-numbered — a different chapter's title seemed to match the described content better for Chapter 38, and an inconclusive secondary source gave a different title for Chapter 115. Both citations trace to *The Ancient Word Recovered* and *Two Registers of One Perception* respectively; neither had been independently checked against Iain Gardner's *The Kephalaia of the Teacher* (Brill, 1995) — the primary source.

## RESOLUTION

**Both citations are correct. The 2026-09-21 finding was a false positive, produced by relying on `WebSearch` result snippets instead of the primary text.**

The user pointed out, the following day, that the primary source was directly available the whole time: a Google Drive folder (`https://drive.google.com/drive/folders/1dCwKutKXBYDY1Z3mRFCwX1EQCB0S14Qk`) contains `Kephalaia_Reading_Edition.pdf` — a reading edition of Gardner's 1995 translation with commentary and apparatus stripped but chapter numbers, titles, and manuscript (`K.`) page-and-line references intact — and this session had Google Drive tools available (`mcp__Google-Drive__*`) that were never used during the original audit. The PDF was downloaded, decoded, and its text extracted directly (`pypdf`, after working around a broken system `cryptography` install by using a fresh virtualenv).

**Chapter 38, verified verbatim from the primary text (p. ~89 of the reading edition):**

> Chapter 38
> Concerning the Light Mind and the Apostles and the Saints.
> ... 90.15 - 92.8 Mani begins his discussion with the macrocosmos. The universe is constructed in the form of a human. Its life and soul are the five sons of the First Man. ...

The chapter *title* names only its catechetical frame (a disciple's five questions to Mani about the Light Mind and the apostolate) — which is why web search summaries describing only the title looked unrelated to body-cosmos content. But the chapter's *body*, spanning manuscript pages K.89–102 (matching *The Ancient Word Recovered*'s citation exactly — "the longest chapter... extends over thirteen manuscript pages"), opens its macrocosm discussion at K.90.15 and contains, verified verbatim:

> All the error, when the enemy of the lights constructed it, he constructed after the likeness of a man. The head of the universe is the beginning of the garments... His ribs are all the firmaments. His navel is the sphere of the stars and the signs of the zodiac...

— an exact match to the passage quoted in *The Garment and What Wears It* §5 and *The Ancient Word Recovered* §6.4 — followed a few pages later by the soul-tissue correspondence ("mind bound in bone... thought in sinew... insight in vein... counsel in flesh... consideration in skin"), also confirmed verbatim. **Chapter 38 is correct. No "Chapter 70" exists with this content** — that title ("On the Body, That It Was Made to Resemble the Cosmos") returned by web search was either describing a different, unrelated secondary passage, a different edition's renumbering, or was simply an unreliable search-summary artifact. It does not appear in the primary text at the location the search implied.

**Chapter 115, verified verbatim (p. ~110 of the reading edition):**

> Chapter 115
> The Catechumen asks the Apostle: will Rest come about for Someone who has come out of the Body, if the Saints pray [over] and make an Alms-offering [for him]?
> 271.13-26 Mani replies that supplications made by the elect in faith will be granted... 271.26 - 273.9 Mani explains the archetypal supplication whereby the Mother of Life besought the Father for a helper, on behalf of the First Man; and was granted the Living Spirit that saved him from the abyss. 273.9-14 Reiteration... 273.15- Mani begins to recount a second archetypal episode... 273.20 - 274.21 The great gods of the first and second emanations beseech the Father for a leader... They are granted the Third Ambassador... 274.30 - 277.3 ... a third supplication regarding the liberation of the living soul...

The 2026-09-21 finding correctly identified the *title* (the catechumen's alms/rest question — this part of the earlier web search was accurate) but wrongly inferred from the title alone that the "Three Entreaties" content must belong to a different chapter. It does not: the title is the chapter's *frame* (a disciple's question about intercessory prayer), and Mani's *answer* to that question is structured as three successive archetypal entreaties — Mother of Life → Living Spirit (for the First Man), the gods → Third Ambassador (for a leader), and a third entreaty for the living soul's liberation — exactly the "three successive entreaties, three successive divine powers descending in answer" pattern *Two Registers of One Perception* describes. **Chapter 115 is correct.**

## What this corrects in the corpus

- `data/08_Correspondential_Texts/The Garment and What Wears It...` — the `[CRITICAL ANALYSIS]` inline note and the Works Cited caveat added 2026-09-21 have been removed (2026-09-22) as unfounded; the Works Cited entry for the Kephalaia now states the verified chapter titles and K.-page ranges directly, with a brief note on why the chapter *titles* alone (which name only each chapter's catechetical frame) undersell what each chapter's *body* contains.
- `EVOLVING_CONCEPTUAL_STRAINS.md` — no strain was ever opened for this (the 2026-09-21 ledger correctly routed it as "flag, don't edit" rather than as a confirmed correction), so nothing to retract there.
- `docs/audit_ledger.md` — pattern register entry "A load-bearing primary-source chapter/section citation doesn't match independently-verifiable secondary descriptions" has been corrected to record the actual lesson: `WebSearch` snippets describing a primary source's *chapter titles* are not a reliable proxy for that chapter's *content*, especially for chapters whose title names only a narrative frame. A new pattern entry records that Google Drive-hosted primary-source PDFs are available for the Kephalaia via the `1dCwKutKXBYDY1Z3mRFCwX1EQCB0S14Qk` folder and should be checked *before* relying on general web search for any future Kephalaia (or other primary-text) citation question.

## Lesson for future audits

This is the mirror image of the failure mode `docs/NIGHTLY_SOURCE_AUDIT.md` § 0 warns about — not defaulting to a materialist reading, but manufacturing doubt about a citation that was correct all along, because the verification method (web search snippets) was weaker than the claim being checked. The 2026-09-21 run did the responsible thing procedurally (flagged rather than silently "fixed" the citation, logged a research question, was explicit about what it hadn't verified) — but the deeper lesson is to check for available primary-source access (Drive folders the user has shared, companion-repo outputs, session tools like `mcp__Google-Drive__*`) *before* concluding that primary-source access is unavailable, not just before making an edit. "I don't have access" should be a conclusion reached after checking the session's actual tool inventory and any Drive folders mentioned in project context, not an assumption.
