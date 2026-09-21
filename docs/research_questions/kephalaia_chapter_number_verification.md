# Kephalaia Chapter-Number Verification: Body-Cosmos Map and "Three Entreaties"

**Target**: `[GDR]`
**Status**: Open
**Date Added**: 2026-09-21
**Priority**: HIGH
**Related Documents**:
- `data/08_Correspondential_Texts/The Garment and What Wears It_ Dating the Correspondential Substrate Beneath the Manichaean Kephalaia.md` (§5, §9, §10, Appendix A, Appendix B, Works Cited — cites "Chapter 38" for the body-cosmos map at least 8 times, "Chapter 115" once for the regenerative micro-architecture)
- `data/00_Framework/The Ancient Word Recovered_ Extracting the Correspondential Substrate of the Kephalaia.md` (§6.4–6.6, and elsewhere — the source document that first establishes "Chapter 38" as the body-cosmos/soul-tissue/regeneration chapter; `Chapter 38, K.89–102` cited as a specific manuscript page range)
- `data/06_Mythological_Studies/Two Registers of One Perception_ The Song of Solomon and the Regenerative Substrate of the Kephalaia.md` (built entirely around "Chapter 115, 'The Three Entreaties'" as its primary Kephalaia text — Sections 5, 6, and the whole comparative argument)

## Context

Both citations were checked during the 2026-09-21 nightly source audit of *The Garment and What Wears It*, which cites Chapter 38 and Chapter 115 as internal-library-established facts (via *The Ancient Word Recovered* and *Two Registers of One Perception* respectively) rather than re-verifying them independently. Neither the audit nor, apparently, the documents that originated the citations had direct access to Iain Gardner's *The Kephalaia of the Teacher* (Brill, 1995) — the primary source — when the citations were written. The audit could not obtain that primary text either (no PDF fetch permitted per this repo's standing rule; the manichaean-analysis companion repo's Kephalaia OCR/translation outputs are gitignored and not checked into that repository; an Internet Archive copy exists but is controlled-digital-lending and did not return full-text search results).

### Finding 1 — Chapter 38 (moderate-to-high confidence of an error)

Three independent web search results, from three separately-phrased queries, converged on:
- **Chapter 38** titled "On the Light-Mind, the Apostles, and the Saints" (or "Concerning the Light Mind and the Apostles and the Saints") — no body-cosmos content in any description found.
- **Chapter 70** titled "On the Body, That It Was Made to Resemble the Cosmos" — explicitly described (in a scholarly-context search snippet) as containing "two separate schema for relating the zodiacal signs to the parts of the body" and offering "a melothesiac reading of ... archontic powers as zodiacal signs fused with the organs, bones, and sinews of the body."

This thematic match (zodiac/organ/bone/sinew correspondences) is close enough to the material *The Garment and What Wears It* and *The Ancient Word Recovered* both quote and describe ("His ribs are all the firmaments"; "His navel is the sphere of the stars and the signs of the zodiac"; mind bound to bone, thought to sinew, teaching to vein) that this is very unlikely to be coincidence. None of the sources found could confirm the exact quoted wording verbatim against Gardner's actual translation, and *The Ancient Word Recovered* cites a specific manuscript page range for "Chapter 38" (`K.89–102`) that was not independently checked — if that page range is itself correct while the chapter *number* is wrong, resolving which one is the error (and what the true chapter/page range is for the body-cosmos material) requires the primary text.

### Finding 2 — Chapter 115 (weaker, inconclusive)

One source (a general-knowledge query, not spot-checked against a scholarly citation) gave Chapter 115's title as "The Catechumen asks the Apostle: Will Rest come about for Someone who has come out of the Body, if the Saints pray over and make an Alms-offering for him?" — a post-mortem intercessory-prayer topic, not the "Three Entreaties" rescue narrative (Mother of Life / Celestial Will / First Man) that *Two Registers of One Perception* and *The Garment and What Wears It* both build on. A second, independent search snippet corroborated similar catechumen/alms/rest phrasing, but for an unspecified chapter number in the 111–115 range, not conclusively 115 itself. No source was found that confirmed or denied "The Three Entreaties" as a real Gardner chapter title at all. This finding is considerably weaker than Finding 1 and should not be treated as more than "worth checking."

## Research Question

Using direct access to Iain Gardner, *The Kephalaia of the Teacher: The Edited Coptic Manichaean Texts in Translation with Commentary* (Brill, Nag Hammadi and Manichaean Studies 37, 1995) — ideally the physical text or a full-text-searchable copy, not secondary summaries:

1. Confirm the chapter number, title, and manuscript page range (`K.` pagination) of the chapter containing the body-cosmos map ("built after the likeness of a man," ribs = firmaments, navel = sphere of the stars and zodiac) and the soul-tissue correspondence (mind/bone, thought/sinew, teaching/vein, counsel/flesh, reflection/skin). Is it Chapter 38 or Chapter 70, or another chapter entirely? Quote the actual text to settle it.
2. Confirm the chapter number and title of the "Three Entreaties" narrative (Mother of Life petitioning the Father of Greatness on behalf of the First Man/Celestial Will, three successive divine powers descending in rescue). Is this Chapter 115, or does it belong elsewhere?
3. If either number is wrong, trace how far the error has propagated: `The Ancient Word Recovered` (source of the Chapter 38 claim and its `K.89–102` page range), `Two Registers of One Perception` (source of the Chapter 115 / "Three Entreaties" claim, and its own supporting-chapter citations to 31, 55, 114, 122 — these should be re-verified too, since if 115 is wrong, the others may share the same error pattern), and `The Garment and What Wears It` (downstream of both). Also check `Three Witnesses to One Architecture` (cited by *The Garment and What Wears It* as the source of the macro-architecture/compression-principle claim) for the same class of chapter-number error, since it was not checked in this pass.
4. If a chapter number is confirmed wrong, the correction should be applied at the *source* document first (`The Ancient Word Recovered` or `Two Registers of One Perception`, whichever actually originates each claim), then propagated to every downstream document per the standard propagation procedure — not patched only in `The Garment and What Wears It`, where the error was noticed.

## Why this matters

This is not a challenge to the correspondential reading itself — nothing here questions whether the Kephalaia contains function-grounded body-cosmos correspondence, only which chapter number the material sits at. But `The Garment and What Wears It` uses "Chapter 38" as its central transmission-fingerprint evidence (§5) and load-bearing comparison against the *Bundahišn* (§9), and a wrong chapter number under a specific, checkable citation is exactly the kind of error-of-record the nightly audit exists to catch — it just could not be finished in one night without primary-source access this session did not have.
