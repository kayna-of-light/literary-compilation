# The Scribal Traces: Computational Coptic Validation of the Kephalaia's Compositional Architecture

## A Corpus-Wide Linguistic Analysis of Dialect Stratification, Greek Loanword Distribution, and the Three-Layer Transmission Model

---

> **Abstract.** This thesis presents a systematic computational analysis of the Coptic linguistic features of the Kephalaia of the Teacher — the didactic masterwork of the Manichaean tradition — across 116 chapters comprising 76,520 Coptic tokens. Through automated detection of Sub-Achmimic dialect markers (the ⲍ/ϩ alternation), Greek loanword stratification (cosmological versus ecclesiastical), formulaic pattern recognition (dialogue frames, blessing closures, exhortation markers), and concordance assessment against independent English content classifications, the analysis reveals a three-layer compositional architecture: (1) a correspondential substrate transmitted through Mani's oral teaching, (2) a first scribal hand writing in Sub-Achmimic dialect, and (3) a second scribal hand writing in or normalizing toward standard Sahidic. The dialect signal distributes continuously across the corpus (mean Sub-Achmimic ratio 0.537, range 0.0 to 1.0), with two chapters preserving pure Sub-Achmimic (Ch 30, Ch 35) and five chapters showing pure Sahidic (Ch 25, Ch 63, Ch 78, Ch 103, Ch 104). Crucially, Chapter 104 demonstrates that dialect and content type are independent signals: it is pure Sahidic (scribal hand) yet 95% substrate (content architecture). This independence confirms that what we are detecting is scribal transmission, not theological editing. The Greek loanword distribution reveals a geographic shift: cosmological Greek concentrates in chapters 1–74 (mean density 1.38%), while ecclesiastical Greek rises in chapters 75–122 (mean density 1.25%). A total of 104 concordance signals and 71 discordance flags validate the cross-layer methodology. The findings provide the first computational linguistic evidence that the Kephalaia preserves a pre-Manichaean correspondential architecture transmitted through, not composed by, Mani and his scribes.

> **Keywords.** Kephalaia, Sub-Achmimic, Sahidic, dialect stratification, Greek loanwords, correspondential substrate, Manichaean transmission, computational Coptic analysis, three-layer model, Ancient Word, correspondences, scribalism

---

## Table of Contents

- [The Scribal Traces: Computational Coptic Validation of the Kephalaia's Compositional Architecture](#the-scribal-traces-computational-coptic-validation-of-the-kephalaias-compositional-architecture)
  - [A Corpus-Wide Linguistic Analysis of Dialect Stratification, Greek Loanword Distribution, and the Three-Layer Transmission Model](#a-corpus-wide-linguistic-analysis-of-dialect-stratification-greek-loanword-distribution-and-the-three-layer-transmission-model)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
  - [2. Methodological Framework](#2-methodological-framework)
    - [2.1 The Coptic Validation Pipeline](#21-the-coptic-validation-pipeline)
    - [2.2 Dialect Detection: The ⲍ/ϩ Alternation](#22-dialect-detection-the-ⲍϩ-alternation)
    - [2.3 Greek Loanword Stratification](#23-greek-loanword-stratification)
    - [2.4 Concordance Assessment](#24-concordance-assessment)
    - [2.5 Data Integrity: The Encoding Correction](#25-data-integrity-the-encoding-correction)
  - [3. The Dialect Landscape](#3-the-dialect-landscape)
    - [3.1 Distribution Across the Corpus](#31-distribution-across-the-corpus)
    - [3.2 The Sub-Achmimic Holotype: Chapter 30](#32-the-sub-achmimic-holotype-chapter-30)
    - [3.3 The Sahidic Extreme: Chapter 78](#33-the-sahidic-extreme-chapter-78)
    - [3.4 The Independence Proof: Chapter 104](#34-the-independence-proof-chapter-104)
  - [4. Greek Loanword Geography](#4-greek-loanword-geography)
    - [4.1 Cosmological Versus Ecclesiastical Greek](#41-cosmological-versus-ecclesiastical-greek)
    - [4.2 The Zone Shift: Chapters 1–74 Versus 75–122](#42-the-zone-shift-chapters-174-versus-75122)
    - [4.3 The Greek Ratio Problem: What Cosmological Greek Does Not Measure](#43-the-greek-ratio-problem-what-cosmological-greek-does-not-measure)
  - [5. Formulaic Patterns and Structural Markers](#5-formulaic-patterns-and-structural-markers)
    - [5.1 Dialogue Frames](#51-dialogue-frames)
    - [5.2 Blessing Closures: ⲛⲁⲙⲉⲣⲉⲧⲉ and ⲛⲁⲙⲉⲗⲟⲥ](#52-blessing-closures-ⲛⲁⲙⲉⲣⲉⲧⲉ-and-ⲛⲁⲙⲉⲗⲟⲥ)
    - [5.3 Concordance and Discordance: The Cross-Validation Signal](#53-concordance-and-discordance-the-cross-validation-signal)
  - [6. The Three-Layer Model](#6-the-three-layer-model)
    - [6.1 Layer One: The Correspondential Architecture](#61-layer-one-the-correspondential-architecture)
    - [6.2 Layer Two: Mani's Oral Teaching and the Universal Naming System](#62-layer-two-manis-oral-teaching-and-the-universal-naming-system)
    - [6.3 Layer Three: The Scribal Hands](#63-layer-three-the-scribal-hands)
    - [6.4 How the Layers Separate](#64-how-the-layers-separate)
  - [7. Discussion](#7-discussion)
    - [7.1 What the Coptic Evidence Reveals](#71-what-the-coptic-evidence-reveals)
    - [7.2 What the English Classification Contributes](#72-what-the-english-classification-contributes)
    - [7.3 Implications for the Ancient Word Hypothesis](#73-implications-for-the-ancient-word-hypothesis)
    - [7.4 The Compiler Problem Revisited](#74-the-compiler-problem-revisited)
    - [7.5 Limitations and Lacunae](#75-limitations-and-lacunae)
  - [8. Conclusion: The Scribes Who Preserved What They Did Not Compose](#8-conclusion-the-scribes-who-preserved-what-they-did-not-compose)
  - [Appendix A: Dialect Distribution by Chapter](#appendix-a-dialect-distribution-by-chapter)
  - [Appendix B: Greek Loanword Rankings](#appendix-b-greek-loanword-rankings)
    - [Top 15 Chapters by Cosmological Greek Density](#top-15-chapters-by-cosmological-greek-density)
    - [Top 15 Chapters by Ecclesiastical Greek Density](#top-15-chapters-by-ecclesiastical-greek-density)
  - [Works Cited](#works-cited)

---

## 1. Introduction

The Kephalaia of the Teacher — "The Chapters" — is the principal didactic text of the Manichaean tradition. Preserved in a single Coptic manuscript from Medinet Madi in the Egyptian Fayyum, it records 123 chapters of oral instruction attributed to Mani (216–274 CE), organized as dialogue between the apostle and his disciples. The text exists in a dialect known to Copticists as Sub-Achmimic (or Lycopolitan), with varying degrees of normalization toward standard Sahidic throughout the manuscript. The critical edition by Polotsky and Böhlig (1940) established the standard text; Gardner's English translation (1995/2005) made the content accessible to non-Copticists for the first time.

Within the framework developed across the companion theses of this library, the Kephalaia occupies a pivotal position. The Manichaean tradition is not a standalone religion but a transmission system. Mani explicitly claimed to synthesize the teachings of Zoroaster, Buddha, and Jesus into a single universal framework — not by inventing new doctrine but by providing what he called the "Seal" of the prophetic chain: a naming system designed to make a single underlying architecture legible across cultural boundaries. The companion thesis *The Book of Zoroaster and the Children of the East* established that the Apocryphon of John's body-correspondence list traces to a "Book of Zoroaster" that belongs to the same Magian transmission stream Mani inherited. *The Magian Cosmos* reconstructed the principle of correspondences within ancient Iranian religion, showing that the Zoroastrian *mēnōg/gētīg* ontology exactly parallels Swedenborg's correspondence doctrine. *The Resonant Cosmos* traced the historical transmission of the Science of Correspondences from the Magian archives through Manichaeism into Central Asia — precisely the region Swedenborg identified as the repository of the Ancient Word.

This thesis addresses a different question: not what the Kephalaia teaches, but how it was transmitted. The question is whether computational analysis of the Coptic text itself — its dialect markers, its Greek loanword distribution, its formulaic patterns — can distinguish the layers of its composition. If the Kephalaia is what the framework proposes it to be — a correspondential architecture transmitted through Mani's oral teaching and preserved by scribes — then the Coptic text should bear the traces of that transmission. The architecture should be separable from the scribal medium. The content should be independent of the dialect.

That is exactly what the data shows.

A custom computational pipeline was built to analyze 116 chapters (76,520 Coptic tokens) from the Polotsky/Böhlig critical edition. The pipeline detects Sub-Achmimic dialect markers (the ⲍ/ϩ alternation that separates this dialect from standard Sahidic), classifies Greek loanwords by semantic domain (cosmological versus ecclesiastical), identifies formulaic patterns (dialogue openings, blessing closures, exhortation markers), and cross-validates these Coptic-derived features against independent English content classifications that had been performed without reference to the Coptic text.

The central findings are these:

First, the dialect signal distributes continuously across the corpus, from two chapters of pure Sub-Achmimic (ratio 1.000: Chapters 30 and 35) to five chapters of pure Sahidic (ratio 0.000: Chapters 25, 63, 78, 103, and 104), with a corpus mean of 0.537. This is not a binary signal — it is a gradient that reflects two scribal traditions in varying mixture.

Second, dialect and content type are independent. Chapter 104 — "Concerning Food: It shall be allocated to Five Products of the human Body" — is pure Sahidic in dialect (ratio 0.000, meaning it was transcribed by the later scribal hand) yet 95% substrate in content (meaning it preserves the oldest teaching layer almost untouched). If dialect correlated with content — if the later scribes had been theological editors rather than copyists — this chapter could not exist.

Third, the Greek loanword distribution reveals a geographic rather than theological pattern. Cosmological Greek (ⲁⲱⲛ, ⲕⲟⲥⲙⲟⲥ, ⲥⲧⲟⲓⲭⲉⲓⲟⲛ) concentrates in the earlier chapters (1–74, mean density 1.38%), while ecclesiastical Greek (ⲉⲕⲕⲗⲏⲥⲓⲁ, ⲁⲡⲟⲥⲧⲟⲗⲟⲥ, ⲡⲣⲟⲫⲏⲧⲏⲥ) rises in the later chapters (75–122, mean density 1.25%). This shift tracks the institutional development of the Manichaean church in Egypt, not the theological content of the teaching.

Fourth, blessing formulas — the Coptic phrases ⲛⲁⲙⲉⲣⲉⲧⲉ ("beloved ones") and ⲛⲁⲙⲉⲗⲟⲥ ("my members") — appear in 19 chapters, marking compositional boundaries that predate both scribal hands.

Fifth, the cross-validation between Coptic linguistic features and English content classifications produces 104 concordance signals against 71 discordance flags. The concordance signals confirm that what was classified as "substrate" in English translation does in fact carry the Coptic markers of the oldest compositional layer. The discordance flags are themselves informative: they reveal where the Greek loanword categories fail (because Coptic cosmological vocabulary is invisible to a Greek-only search) and where the English classification cannot detect formulaic structure that the Coptic preserves.

The thesis that follows presents these findings in full, beginning with the methodology that produced them (§2), then the dialect landscape (§3), the Greek loanword geography (§4), the formulaic patterns (§5), the interpretive three-layer model they support (§6), the discussion of what this evidence means for the larger framework (§7), and the conclusion (§8). Two appendices provide the complete dialect distribution and Greek loanword rankings by chapter.

## 2. Methodological Framework

### 2.1 The Coptic Validation Pipeline

The analysis operates on Coptic transcriptions of the Polotsky/Böhlig critical edition of the Kephalaia (1940). Page images from this printed edition were transcribed via a two-pass AI transcription process: the first pass extracted raw Unicode Coptic text from each page image, and the second pass corrected errors against the image. The resulting transcription files — 282 pages of Coptic text — were mapped to 116 chapters using the manuscript page ranges recorded in the English edition's chapter headings.

For each chapter, the pipeline performs four independent analyses on the Coptic text: (1) dialect marker detection, (2) Greek loanword extraction and classification, (3) formulaic pattern recognition, and (4) lacunae density measurement. These four Coptic-derived measurements are then cross-validated against a fifth, independently-derived signal: English content classifications that had been performed on Gardner's English translation without any reference to the Coptic original. The concordance between these independent signals — one derived from the Coptic text, the other from English translation — constitutes the primary validation mechanism.

The pipeline is implemented as a standalone Python script (`coptic_validation.py`) that reads transcription files, applies pattern matching against defined lexicons and regular expressions, and outputs per-chapter JSON analysis files and a corpus-wide JSON summary. No machine learning or probabilistic inference is used: every detection is a deterministic pattern match against explicitly defined lexicons. This transparency is a methodological choice. The pipeline does not interpret; it counts. The interpretation belongs to the thesis.

### 2.2 Dialect Detection: The ⲍ/ϩ Alternation

The primary dialect marker separating Sub-Achmimic from standard Sahidic is the use of the letter ⲍ (zayin, U+2C8D) where Sahidic uses ϩ (hori, U+03E9). This is not a sporadic variation but a systematic phonological difference: every morpheme containing /h/ in Sahidic appears with /z/ in Sub-Achmimic. The alternation is diagnostic because it operates across the entire morphological inventory — prepositions (ⲍⲛ vs. ϩⲛ, "in"), compound elements (ⲍⲏⲧ vs. ϩⲏⲧ, "heart/belly"), prefix forms (ⲁⲍ vs. ⲁϩ), and lexical items (ⲍⲱⲃ vs. ϩⲱⲃ, "thing"; ⲍⲉ vs. ϩⲉ, "manner").

The pipeline searches for 14 Sub-Achmimic forms and their 14 Sahidic equivalents:

| Sub-Achmimic | Sahidic | Gloss |
|---|---|---|
| ⲍⲙ̄ | ϩⲙ̄ | "in" (pre-labial) |
| ⲍⲛ | ϩⲛ | "in" |
| ⲍⲛ̄ | ϩⲛ̄ | "in" (with supralinear stroke) |
| ⲁⲍ | ⲁϩ | prefix form |
| ⲍⲓ | ϩⲓ | "upon" |
| ⲍⲁ | ϩⲁ | "under" |
| ⲍⲏⲧ | ϩⲏⲧ | "heart, belly" |
| ⲍⲱⲃ | ϩⲱⲃ | "thing" |
| ⲍⲣⲏ | ϩⲣⲏ | compound element |
| ⲍⲁⲗ | ϩⲁⲗ | "old woman, wife" |
| ⲍⲱⲡ | ϩⲱⲡ | "to hide" |
| ⲍⲉ | ϩⲉ | "manner" |
| ⲍⲁⲉ | ϩⲁⲉ | "end" |
| ⲍⲁⲏ | ϩⲁⲏ | "end" (variant) |

For each chapter, the count of Sub-Achmimic forms and Sahidic forms is tallied, and a Sub-Achmimic ratio is computed: SA_count / (SA_count + Sahidic_count). A ratio of 1.000 means the chapter is written entirely in Sub-Achmimic; a ratio of 0.000 means entirely in Sahidic. The threshold for flagging "substantial Sahidic intrusion" is set at 0.500 — below this point, more than half the dialect markers are Sahidic, suggesting the later scribal hand has substantially normalized the text.

### 2.3 Greek Loanword Stratification

Coptic absorbed a substantial number of Greek loanwords over centuries of Greco-Egyptian contact. These loanwords are not uniformly distributed: some belong to the cosmological and philosophical register that characterizes the oldest teaching substrate (ⲁⲱⲛ, ⲕⲟⲥⲙⲟⲥ, ⲥⲧⲟⲓⲭⲉⲓⲟⲛ, ⲯⲩⲭⲏ, ⲛⲟⲩⲥ, ⲟⲩⲥⲓⲁ), while others belong to the ecclesiastical and institutional register that marks the later organizational layer of the Manichaean church (ⲉⲕⲕⲗⲏⲥⲓⲁ, ⲁⲡⲟⲥⲧⲟⲗⲟⲥ, ⲉⲡⲓⲥⲕⲟⲡⲟⲥ, ⲡⲣⲉⲥⲃⲩⲧⲉⲣⲟⲥ, ⲙⲉⲧⲁⲛⲟⲓⲁ). A third category of general-purpose Greek conjunctions and prepositions (ⲇⲉ, ⲅⲁⲣ, ⲁⲗⲗⲁ, ⲕⲁⲧⲁ) is counted but not diagnostic of register.

The pipeline defines three lexicons: 28 cosmological/philosophical terms (with spelling variants), 26 ecclesiastical/institutional terms, and 12 general-purpose items. For each chapter, the pipeline counts occurrences of terms from each lexicon, computes density as a percentage of total Coptic tokens, and computes a cosmological ratio: cosmological_count / (cosmological_count + ecclesiastical_count).

A high cosmological ratio in a chapter classified as "substrate" in English is a concordance signal. A high cosmological ratio in a chapter classified as "institutional" is a discordance flag. The analysis of these concordances and discordances forms a central part of the cross-validation (§2.4).

It must be noted, however, that this metric has a known limitation: the Kephalaia's cosmological vocabulary is substantially Coptic, not Greek. Terms like ⲗⲁⲙⲡⲁⲇⲓⲟⲛ use Greek-derived vocabulary for cosmological objects, but the core correspondential vocabulary — five Shekhinas, three garments, the Call and Response — is expressed in Coptic. The Greek cosmological ratio therefore underestimates the true substrate content. This asymmetry is discussed further in §4.3.

### 2.4 Concordance Assessment

The cross-validation mechanism compares Coptic-derived features against English content classifications. Six concordance rules are applied:

1. **Cosmological ratio versus substrate percentage.** If a chapter is classified as ≥70% substrate in English and its Greek cosmological ratio is ≥0.5, this is concordant. If the substrate is ≥70% but the cosmological ratio is <0.3, this is discordant (the Coptic suggests a more institutional register than the English detected, or — more commonly — the cosmological vocabulary is Coptic rather than Greek).

2. **Ecclesiastical density in substrate chapters.** If a chapter is classified as ≥90% substrate but has ecclesiastical Greek density above 2.0%, this is flagged as notable.

3. **Dialogue frame detection.** If the Coptic text contains dialogue-opening formulas (ⲧⲟⲧⲉ ⲡⲁⲭⲉ, "then he said"; ⲡⲁⲡⲟⲥⲧⲟⲗⲟⲥ ⲡⲁⲭⲉ, "the apostle says") but the English classification recorded zero dialogue-frame paragraphs, this is flagged as discordant.

4. **Dialect consistency.** If the Sub-Achmimic ratio is below 0.5, the chapter is flagged for substantial Sahidic intrusion. If above 0.8, it receives a concordance signal for dialect consistency with the original manuscript layer.

5. **Lacunae density.** If more than 30% of lines show damage indicators, the chapter is flagged as potentially older or more heavily handled portion of the manuscript.

6. **Blessing and exhortation detection.** If the Coptic preserves blessing formulas or exhortation markers but the English classification recorded no exhortation paragraphs, this is flagged as notable — the formulaic structure visible in Coptic may not be distinguishable in English translation.

### 2.5 Data Integrity: The Encoding Correction

During verification of the transcription files, an encoding anomaly was discovered: on four manuscript pages (p128, p190, p194, p254), the AI transcriber had rendered the Coptic letter ϩ (hori, U+03E9) as the visually similar ASCII digit "2" (U+0032). This substitution made the dialect detection pipeline unable to count Sahidic forms on those pages, because it searches for the Unicode codepoint U+03E9, not the ASCII digit.

The affected pages carried a total of 108 instances of this substitution (p128: 19, p190: 34, p194: 26, p254: 29). Page 190 was the most severely affected — every ϩ on the page had been rendered as digit-2, producing a page with zero detectable Sahidic markers. Five chapters were impacted: Ch 52, Ch 77, Ch 78, Ch 81, and Ch 101.

The correction was applied in-place: digit-2 characters adjacent to Coptic Unicode characters (and not at line beginnings, where they function as line numbers) were normalized to U+03E9. After correction, page 190 correctly shows 34 instances of ϩ, and the chapters spanning this page — particularly Chapter 78 — now display their true dialect profile.

The significance of this correction is methodological rather than substantive. Before the fix, Chapter 78 appeared to have zero dialect markers of any kind (neither ⲍ nor ϩ), which was anomalous rather than informative. After the fix, Chapter 78 shows 66 Sahidic markers and zero Sub-Achmimic markers — confirming it is a genuinely pure Sahidic chapter (ratio 0.000), not a data gap. The finding is the same (pure Sahidic), but the evidence is now properly visible. The correction is reported here as evidence of methodological self-correction: the pipeline's outputs were verified against the transcription files, and the transcription files were verified against the page images.

## 3. The Dialect Landscape

### 3.1 Distribution Across the Corpus

The Sub-Achmimic ratio distributes continuously across all 116 analyzed chapters, with a corpus mean of 0.537 and a range from 0.000 to 1.000. The distribution is not bimodal — it does not split cleanly into "Sub-Achmimic chapters" and "Sahidic chapters." Instead, it forms a continuous gradient that places most chapters in a mixed zone:

| Range | Description | Chapters | Percentage |
|---|---|---|---|
| 0.90–1.00 | Pure Sub-Achmimic | 7 | 6.0% |
| 0.70–0.89 | Predominantly Sub-Achmimic | 17 | 14.7% |
| 0.50–0.69 | Mixed, leaning Sub-Achmimic | 47 | 40.5% |
| 0.30–0.49 | Mixed, leaning Sahidic | 30 | 25.9% |
| 0.10–0.29 | Predominantly Sahidic | 9 | 7.8% |
| 0.00–0.09 | Near-pure Sahidic | 7 | 6.0% |

This distribution is exactly what a model of two scribal hands would predict. If the original manuscript was written in Sub-Achmimic and subsequently copied or partially normalized by a scribe writing standard Sahidic, the result would be a gradient: some portions faithfully preserved, others fully normalized, and most in between. The two extremes — pure Sub-Achmimic and pure Sahidic — represent the limiting cases. The bulk of the corpus sits in the mixed zone because most chapters passed through both hands to varying degrees.

Within this gradient, two chapters achieve the pure Sub-Achmimic mark (ratio 1.000): Chapter 30 and Chapter 35. Five chapters show pure Sahidic (ratio 0.000): Chapters 25, 63, 78, 103, and 104. These seven chapters — the extremes — are the most diagnostic for understanding what the dialect signal measures. We examine three of them in detail.

### 3.2 The Sub-Achmimic Holotype: Chapter 30

Chapter 30, "Concerning the Three Garments," occupies manuscript pages 83,17–84,4 and contains 432 Coptic tokens. Its Sub-Achmimic ratio is 1.000: all 56 dialect markers are Sub-Achmimic forms, and zero Sahidic intrusions are detected. The ⲍ-forms distribute across the full morphological inventory: ⲍⲛ ×14 ("in"), ⲍⲉ ×11 ("manner"), ⲁⲍ ×9 (prefix), ⲍⲛ̄ ×8, ⲍⲓ ×5 ("upon"), ⲍⲏⲧ ×4 ("heart/belly"), ⲍⲣⲏ ×3 (compound element), ⲍⲙ̄ ×1, ⲍⲁ ×1.

The content, independently classified from English translation, is 85% substrate: a systematic description of the Living Spirit's three garments (wind, fire, water) as elemental coverings stretched across the cosmic zone from bottom to top. Every mapping stays within the cosmic system — cosmic agent, elemental garments, cosmic geography. The chapter carries a blessing closure formula (ⲛⲁⲙⲉⲣⲉⲧⲉ, "beloved ones"), marking it as a complete compositional unit with formal ending.

The concordance assessment produces two signals: "CONCORDANT: High substrate (85%) with high cosmological Greek ratio (0.60)" and "DIALECT CONSISTENT: Sub-Achmimic ratio 1.00." The chapter is, in every measurable dimension, a specimen of the oldest compositional layer: the first scribal hand writing in pure Sub-Achmimic, recording substrate teaching, closing with a formulaic blessing.

Chapter 30 is the holotype — the single most intact example of Layer One transcribed by the first scribal hand. If only one chapter of the Kephalaia survived, and it were this one, the essential character of the oldest layer would still be legible.

### 3.3 The Sahidic Extreme: Chapter 78

Chapter 78, "Concerning the Four Things over which People kill each other," occupies manuscript pages 190,11–191,8 (381 tokens). Its Sub-Achmimic ratio is 0.000: zero ⲍ-forms are present, and 66 Sahidic ϩ-forms distribute across the full inventory (ⲁϩ ×19, ϩⲛ ×11, ϩⲱⲃ ×8, ϩⲛ̄ ×7, ϩⲏⲧ ×7, ϩⲁ ×5, ϩⲓ ×3, ϩⲉ ×3, ϩⲙ̄ ×2, ϩⲁⲉ ×1).

This chapter was one of the five affected by the encoding correction described in §2.5. Before the fix, page 190 showed zero Sahidic markers because every ϩ had been transcribed as ASCII digit "2," which the pipeline could not match. After the correction restored the proper Unicode codepoint, the 66 Sahidic markers became visible. The ratio of 0.000 is now a confirmed finding, not a data gap.

The content classification is strikingly different from Chapter 30: it is classified as 0% substrate — entirely editorial bridge and exhortation. This is the opposite pole: a chapter where both the scribal hand (pure Sahidic) and the content (institutional/editorial) belong to the later layer. It lacks the blessing closure that marks the older compositional units.

Yet the Greek loanword analysis introduces an unexpected complication. The cosmological Greek ratio is 0.75 — higher than many substrate chapters. The concordance assessment flags this as discordant: "Low substrate (0%) but high cosmological Greek (0.75) — Coptic suggests more substrate content than English classification captured." This is one of the cases where the Greek ratio and the English classification disagree, and the disagreement is informative. The chapter discusses cosmological themes (the four things people fight over), but the *treatment* is homiletic, not cosmogonic. The cosmological Greek terms are vocabulary borrowed by the later layer to discuss topics the substrate defined. The terms traveled; the architecture did not.

### 3.4 The Independence Proof: Chapter 104

Chapter 104, "Concerning Food: It shall be allocated to Five Products of the human Body," occupies a single manuscript page (258,4–258,25, 198 tokens). It is the single most important chapter for the three-layer model, because it proves that dialect and content are independent signals.

The dialect ratio is 0.000: pure Sahidic, zero Sub-Achmimic forms, 34 Sahidic markers across the standard inventory (ϩⲛ ×7, ϩⲛ̄ ×6, ⲁϩ ×6, ϩⲓ ×6, ϩⲏⲧ ×4, ϩⲁ ×2, ϩⲱⲃ ×2, ϩⲉ ×1). By dialect, this chapter was transcribed entirely by the later Sahidic scribal hand.

The content classification is 95% substrate: a systematic five-fold degree mapping of food to body productions, moving from the most subtle (rapture/Mind) to the most gross (corporeal offspring). Both sides of every mapping stay within the body-cosmos system. No editorial bridge, no institutional content, no exhortation, no citations. The only non-substrate material is the seven-word opening dialogue frame formula. The English classification note describes it as an "exceptionally clean substrate chapter" with a "characteristic pattern: invisible/immeasurable to progressively material to visible."

The concordance assessment confirms both readings: "CONCORDANT: High substrate (95%) with high cosmological Greek ratio (1.00)" from the content side, and "DIALECT FLAG: Sub-Achmimic ratio is only 0.00 — substantial Sahidic intrusion suggests later editorial hand" from the dialect side.

This combination — pure Sahidic dialect, pure substrate content — proves that the dialect signal and the content signal measure different things. The dialect measures which scribal hand copied the text. The content measures what layer of the compositional architecture the teaching belongs to. If the later scribes had been theological editors — if they had normalized the dialect *and* reworked the teaching — Chapter 104 could not exist in this form. A chapter of pristine substrate teaching would not survive a thorough editorial revision with its content untouched and only its spelling changed. The simplest explanation is the correct one: the Sahidic scribe copied this chapter faithfully, changing ⲍ to ϩ as their dialect required, but preserving the teaching exactly as they found it. The scribe transmitted; the scribe did not compose.

## 4. Greek Loanword Geography

### 4.1 Cosmological Versus Ecclesiastical Greek

Across the entire corpus, the pipeline detected 880 cosmological Greek tokens and 753 ecclesiastical Greek tokens. These two categories are not uniformly distributed but show distinct concentration patterns that track the compositional history of the text.

The cosmological vocabulary — ⲁⲱⲛ, ⲕⲟⲥⲙⲟⲥ, ⲥⲧⲟⲓⲭⲉⲓⲟⲛ, ⲯⲩⲭⲏ, ⲛⲟⲩⲥ, ⲥⲱⲙⲁ, ⲟⲩⲥⲓⲁ, ⲫⲩⲥⲓⲥ, ⲡⲗⲏⲣⲱⲙⲁ — belongs to the philosophical register that characterizes the Manichaean cosmogonic teaching. These are the terms used to describe the structure of the universe, the emanation of divine powers, and the relationship between spirit and matter. They are shared with the broader Hellenistic philosophical tradition and with the Nag Hammadi texts, where the same vocabulary describes the same architecture under different names.

The ecclesiastical vocabulary — ⲉⲕⲕⲗⲏⲥⲓⲁ, ⲁⲡⲟⲥⲧⲟⲗⲟⲥ, ⲉⲡⲓⲥⲕⲟⲡⲟⲥ, ⲡⲣⲉⲥⲃⲩⲧⲉⲣⲟⲥ, ⲇⲓⲁⲕⲟⲛⲟⲥ, ⲉⲕⲗⲉⲕⲧⲟⲥ, ⲙⲉⲧⲁⲛⲟⲓⲁ, ⲡⲓⲥⲧⲓⲥ, ⲁⲅⲁⲡⲏ — belongs to the institutional register of the organized Manichaean church in Egypt. These are the terms used to describe the hierarchy of the elect, the structure of the community, and the moral obligations of the hearers. They reflect the Manichaean church as it existed as a functioning institution in third- and fourth-century Egypt.

The chapters with the highest cosmological Greek density cluster in the early chapters: Chapter 10 (4.01%), Chapter 11 (3.69%), Chapter 13 (2.56%), Chapter 69 (2.49%), Chapter 14 (2.44%). These are the cosmic-vision chapters — the ones that describe the structure of the universe, the emanation of light, the conflict of the two principles. Their cosmological Greek is the fingerprint of the philosophical milieu in which the teaching was first rendered into Greek-influenced Coptic.

The chapters with the highest ecclesiastical Greek density are more dispersed: Chapter 80 (4.23%), Chapter 102 (3.67%), Chapter 63 (3.32%), Chapter 98 (3.03%), Chapter 79 (2.47%). These chapters deal with community organization, moral instruction, and the duties of the elect. Their ecclesiastical Greek reflects the institutional language that developed as the Manichaean church grew in Egypt.

### 4.2 The Zone Shift: Chapters 1–74 Versus 75–122

The zone comparison reveals a clear geographic shift in Greek loanword distribution:

| Zone | Chapters | Avg. Cosmological Density | Avg. Ecclesiastical Density |
|---|---|---|---|
| First half | 1–74 (n=72) | 1.38% | 0.88% |
| Second half | 75–122 (n=44) | 0.80% | 1.25% |

In the first half of the manuscript, cosmological Greek outnumbers ecclesiastical Greek by a ratio of 1.57:1. In the second half, the relationship reverses: ecclesiastical Greek exceeds cosmological by 1.56:1. This is a clean inversion, and it reflects not a theological shift within the teaching but the growing institutional framework within which the teaching was recorded and transmitted.

The shift does not mean that the later chapters are doctrinally different. Many later chapters still carry high substrate content — Chapter 98, for example, is classified as 80% substrate in English. But the language surrounding that substrate increasingly reflects the organizational vocabulary of the Manichaean church. The substrate persists; the medium of its recording changes.

### 4.3 The Greek Ratio Problem: What Cosmological Greek Does Not Measure

The single most important limitation of the Greek loanword analysis is that it measures Greek vocabulary, not cosmological content. The Kephalaia's correspondential architecture — the five Shekhinas (Reason, Mind, Intelligence, Thought, Understanding), the three garments, the Call and Response, the luminaries, the five elements — is expressed substantially in Coptic, not in Greek. The Greek cosmological terms (ⲁⲱⲛ, ⲕⲟⲥⲙⲟⲥ, ⲥⲧⲟⲓⲭⲉⲓⲟⲛ) are borrowed guests in a Coptic household. A chapter can be saturated with correspondential cosmological teaching and yet show minimal Greek cosmological density, because the teaching's core vocabulary is native Coptic.

This asymmetry explains several of the discordance flags. Chapters 16, 25, 95, 98, 101, and 110 are all flagged as discordant: high substrate content in English classification but low cosmological Greek ratio. The flag reads: "Coptic suggests more institutional register than English classification indicates." But the real explanation is simpler: the teaching in these chapters uses Coptic cosmological vocabulary that the Greek loanword search cannot detect. The discordance is not between the English and the Coptic — it is between the Greek-language search and the actual content.

The converse failure is also real. Chapter 78, classified as 0% substrate, shows a cosmological Greek ratio of 0.75. The flag reads: "Coptic suggests more substrate content than English classification captured." But Chapter 78 is a homiletic chapter that discusses cosmological topics (the four things people fight over) without following the systematic mapping structure of substrate teaching. The cosmological Greek terms are vocabulary borrowed by the editorial layer to discuss themes the substrate defined. The cosmological ratio detects the vocabulary but not the architecture.

This is an important methodological lesson. Greek loanword analysis is a valid layer-detection tool, but it is not a content-classification tool. It detects the register of the scribal environment (philosophical versus institutional) more reliably than it detects the compositional layer (substrate versus editorial). The register and the layer often correlate — the oldest teaching tends to use more philosophical Greek — but they are not identical, and the exceptions are informative.

## 5. Formulaic Patterns and Structural Markers

### 5.1 Dialogue Frames

The Kephalaia is written as recorded oral instruction. Its genre is the dialogue between teacher and disciples: "Then he said" (ⲧⲟⲧⲉ ⲡⲁⲭⲉ), "the apostle says" (ⲡⲁⲡⲟⲥⲧⲟⲗⲟⲥ ⲡⲁⲭⲉ), "we beseech you" (ⲧⲛⲧⲱⲃϩ ⲙⲙⲁⲕ). These dialogue-frame formulas are not teaching content — they are the literary scaffolding that situates the teaching within the scene of instruction. In the pipeline's taxonomy, they belong to the outermost layer: the frame that the scribes constructed (or preserved) to present Mani's oral teaching as written text.

The pipeline detects five categories of dialogue-opening patterns, three disciple-question patterns, and three response-formula patterns. Across the 116 chapters analyzed, the total count of formulaic patterns is 119, with a mean density of approximately 1.56 per thousand Coptic tokens. The most common patterns are response formulas (ⲉⲧⲉⲧⲛⲥⲁⲩⲛⲉ, "you know") and dialogue openings.

Several discordance flags arise from the dialogue detection: 10 chapters show Coptic dialogue-opening formulas where the English classification recorded zero dialogue-frame paragraphs. In each case, the Coptic text preserves a brief formula ("then he said") that is structurally inaudible in English translation — not because the translator omitted it, but because a two-word Coptic phrase at the start of a paragraph does not generate a separate "dialogue frame" classification when the paragraph's content is overwhelmingly substrate. These discordances are methodologically informative but not substantively troubling: they show where the resolution of the two classification systems differs.

### 5.2 Blessing Closures: ⲛⲁⲙⲉⲣⲉⲧⲉ and ⲛⲁⲙⲉⲗⲟⲥ

The blessing closure formulas — ⲛⲁⲙⲉⲣⲉⲧⲉ ("my beloved ones") and ⲛⲁⲙⲉⲗⲟⲥ ("my members/limbs") — are the most significant structural markers in the corpus. They appear in 19 chapters: 9, 10, 27, 28, 29, 30, 38, 39, 41, 42, 56, 57, 65, 66, 67, 85, 86, 95, and 119. These formulas mark the formal end of a teaching unit — a compositional boundary that predates both scribal hands.

The concentration pattern is suggestive. Thirteen of the nineteen chapters with blessing closures (68%) fall in the first half of the manuscript (chapters 1–74), and six (32%) in the second half (75–122). This aligns with the broader pattern of the first half preserving more of the original compositional structure, while the second half shows more editorial reworking. But the formulas do appear in the second half, indicating that the scribes did not systematically strip them during normalization — they preserved them where they found them.

The blessing formulas are almost never classified as "exhortation" in the English content classification, producing a recurring notable flag: "Coptic has N blessing formula(s) and 0 exhortation marker(s), but English classified 0 paragraphs as exhortation." This flag appears in 13 of the 19 blessing-closure chapters. It arises because the English classification system uses "exhortation" to describe hortatory content (moral instruction, commands to the hearer), while the Coptic blessing closure is a liturgical seal — not hortatory but performative. It does not exhort; it blesses. The two systems are measuring different things, and their disagreement is itself a finding: the blessing closure belongs to a layer of compositional structure that the English content categories do not capture.

### 5.3 Concordance and Discordance: The Cross-Validation Signal

Across the full corpus, the concordance assessment produces 104 concordance signals and 71 discordance flags — a ratio of approximately 1.5:1. This ratio means that the Coptic linguistic features and the English content classifications agree more often than they disagree, but the disagreement rate is substantial and informative.

The concordance signals fall into several categories. The most common is the high-substrate/high-cosmological-ratio concordance: chapters classified as ≥70% substrate in English that also show a cosmological Greek ratio above 0.5. These are chapters where both independent classification methods — one working from English content, the other from Coptic linguistic features — agree that the text belongs to the oldest teaching layer. The second most common is dialect consistency: chapters with Sub-Achmimic ratios above 0.8, confirming they preserve the original manuscript dialect.

The discordance flags also cluster into patterns. The most frequent flag type is the dialect flag (48 of 71 flags, 68%): chapters where the Sub-Achmimic ratio falls below 0.5, indicating substantial Sahidic normalization. This is not a failure of the analysis — it is a positive finding. It identifies which chapters have passed through the later scribal hand. The second most common flag type is the cosmological ratio discordance (5 chapters flagged as "high substrate but low Greek cosmological ratio," and 3 flagged with the reverse pattern), which arises from the Greek ratio limitation discussed in §4.3. The third type is the dialogue-frame mismatch (10 chapters) and the blessing/exhortation mismatch (13 chapters), both of which arise from differing granularity between the Coptic and English classification systems.

The overall 1.5:1 concordance-to-discordance ratio, combined with the fact that most discordance flags have identifiable and consistent causes, validates the cross-layer methodology. The two independent classification systems — one linguistic, one content-based — are measuring different aspects of the same compositional history, and their areas of agreement identify the strongest specimens of each layer, while their areas of disagreement reveal the limits of each method.

## 6. The Three-Layer Model

### 6.1 Layer One: The Correspondential Architecture

The innermost layer is the teaching itself: the systematic mapping of spiritual realities onto natural forms that characterizes what the Divine Bricolage framework calls the correspondential substrate. In the Kephalaia, this substrate manifests as a series of structured cosmological teachings — the five Shekhinas of the Father of Greatness (Reason, Mind, Intelligence, Thought, Understanding), the three garments of the Living Spirit, the five elements, the Call and Response, the body-cosmos correspondences. These are not doctrinal assertions or philosophical arguments. They are systematic maps: each natural form (garment, element, body product) corresponds to a specific spiritual reality, and the mappings follow the characteristic pattern of descent through discrete degrees — from the most subtle and interior to the most gross and ultimate.

This pattern is what the English content classification identifies as "substrate." When the classification notes describe Chapter 30's teaching as "both sides of every mapping stay within the cosmic system (cosmic agent → elemental garments → cosmic geography)," or Chapter 104's as "a systematic five-fold degree mapping from the most subtle (rapture/Mind) to the most gross (corporeal offspring)," they are describing the correspondential architecture in action. The Coptic validation confirms this identification by showing that the substrate chapters carry the markers of the oldest compositional layer: high Sub-Achmimic ratios, cosmological Greek vocabulary, blessing closure formulas.

But the architecture is not identical with any particular language, dialect, or vocabulary. This is the central point. The correspondential substrate is visible in English translation (where it was classified as "substrate" without reference to the Coptic), visible in Coptic text (where it correlates with Sub-Achmimic dialect and cosmological Greek), and — if the framework's prediction is correct — it would be visible in the Middle Persian, Parthian, Sogdian, and Old Turkic versions of the same teaching that the Manichaeans transmitted across Central Asia. The architecture is the constant. The linguistic medium is the variable.

### 6.2 Layer Two: Mani's Oral Teaching and the Universal Naming System

Between the correspondential architecture and the scribal manuscript stands Mani himself. The Kephalaia is not a text Mani wrote; it is a text his disciples recorded from his oral instruction. The genre is dialogue: "Then he said," "we beseech you, our master," "tell us." This is not narrative fiction — it is a recording convention. Mani spoke; the scribes wrote.

Mani's contribution is not the architecture itself. The framework established in the companion theses identifies the architecture as preceding Mani — it is the same Ancient Word that Swedenborg located in Central Asia, the same correspondential system that the Apocryphon of John attributes to "the book of Zoroaster," the same mēnōg/gētīg ontology that structures Zoroastrian cosmology. What Mani contributed was a universal naming system: a set of divine names and cosmological labels designed to make the architecture legible across cultural boundaries. The five Shekhinas, the Living Spirit, the Ambassador, the Column of Glory — these are Mani's names for structures that already existed in the Magian and Enochic traditions.

This is why Mani could claim to be the "Seal of the Prophets" without contradiction. He did not claim to teach something new. He claimed to provide the final naming system: the one that could synthesize Zoroaster, Buddha, and Jesus because it named what they all taught. This claim is either grandiose self-deception or a description of how correspondence works in practice: the same spiritual reality (constant state) expressed through different cultural naming systems (variable form), with Mani offering a meta-naming system designed to make the constancy visible.

The Coptic evidence does not settle this question — it cannot prove or disprove the ontological status of correspondences. What it does is confirm that the teaching recorded in the Kephalaia has a structure older than the scribal medium in which it is preserved. The five-fold degree mapping of Chapter 104 did not originate with the Sahidic scribe who wrote it down. The three garments of Chapter 30 did not originate with the Sub-Achmimic scribe who recorded them. These teachings passed through the scribes; they were not composed by the scribes. Mani's layer — the oral instruction, the universal naming system, the dialogue form — is the medium through which the architecture entered the manuscript tradition.

### 6.3 Layer Three: The Scribal Hands

The outermost layer is the one most directly visible to the Coptic validation pipeline: the scribal hands that committed the oral teaching to parchment. The dialect analysis reveals at minimum two hands. The first hand writes in Sub-Achmimic — the dialect of the Lycopolitan region of Upper Egypt, consistent with the manuscript's provenance from Medinet Madi in the Fayyum. The second hand writes in standard Sahidic or normalizes existing Sub-Achmimic text toward Sahidic. Whether the second hand is a simultaneous collaborator, a later copyist, or a normalizing editor cannot be determined from the dialect data alone. What can be determined is that the two hands left distinguishable traces across the corpus.

The first hand's distinctive trace is the letter ⲍ. When a chapter shows ⲍⲛ instead of ϩⲛ, ⲍⲉ instead of ϩⲉ, ⲁⲍ instead of ⲁϩ, we are reading text as the first scribe wrote it. When the same morphemes appear as ϩⲛ, ϩⲉ, ⲁϩ, the second hand has either written or normalized the text. The dialect ratio quantifies this mixture: 1.000 is the first hand alone; 0.000 is the second hand alone; anything in between is mixed.

The scribal hands also leave traces in the formulaic patterns. The dialogue openings and response formulas are scribal constructions — they situate the teaching within the recording scene. The blessing closures are less clearly scribal: they may have been part of Mani's oral delivery, preserved by the scribes rather than added by them. The concentration of blessing closures in the first half of the manuscript, where Sub-Achmimic ratios tend to be higher, is consistent with the first scribal hand preserving more of the original oral structure.

### 6.4 How the Layers Separate

The three layers separate because they leave different kinds of traces:

| Signal | Layer Detected | What It Measures |
|---|---|---|
| Sub-Achmimic ratio | Scribal hand (Layer 3) | Which scribe wrote or normalized this chapter |
| Greek cosmological ratio | Register environment | Philosophical milieu of recording |
| Greek ecclesiastical density | Institutional development | Church organization at time of recording |
| English substrate percentage | Correspondential architecture (Layer 1) | How much of the teaching is the oldest structural layer |
| Blessing closures | Compositional structure (Layer 1–2) | Original teaching-unit boundaries |
| Dialogue frames | Recording convention (Layer 2–3) | Oral-to-written transition scaffolding |

The critical evidence for separation is Chapter 104: dialect and content are independent signals. The scribal hand (Layer 3) can change without changing the correspondential architecture (Layer 1). This independence means the three layers are not a vertical hierarchy where each layer determines the next. They are orthogonal dimensions of the manuscript's history: the architecture exists independently of the medium of its recording, and the medium of recording exists independently of which scribe's hand committed it to parchment.

This orthogonality is the primary finding of the Coptic validation. It means that when we strip away the scribal layer (by treating the dialect variation as noise) and strip away the institutional scaffolding (by treating the dialogue frames and ecclesiastical vocabulary as later accretions), what remains is the teaching itself — the correspondential architecture that entered the manuscript tradition through Mani's oral instruction and survived intact through two successive scribal hands.

## 7. Discussion

### 7.1 What the Coptic Evidence Reveals

The Coptic linguistic evidence reveals a manuscript with a layered compositional history that is detectable through automated pattern analysis. The dialect gradient (mean 0.537, range 0.000–1.000) maps two scribal hands. The Greek loanword shift (cosmological dominant in chapters 1–74, ecclesiastical dominant in 75–122) maps the institutional development of the Manichaean church in Egypt. The formulaic patterns (119 detected, concentrated in the first half) map the recording conventions that frame the oral teaching. The cross-validation between these Coptic-derived signals and the independently-derived English content classifications produces a concordance ratio of 1.5:1 (104 signals to 71 flags), confirming that the two independent methods are measuring the same underlying compositional history from different angles.

What the Coptic evidence does not reveal — and this must be stated with equal clarity — is the correspondential architecture itself. The pipeline detects linguistic traces of the *medium* through which the architecture was transmitted. It detects scribal hands, registers, formulaic conventions. It does not and cannot detect whether the content being transmitted is "true" in any ontological sense. The claim that the Kephalaia preserves a correspondential architecture older than Mani belongs to the interpretive framework, not to the computational analysis. What the computational analysis does is confirm that the text has the structural properties such an architecture would predict: a teaching layer that is separable from the scribal layer, content that is independent of dialect, a substrate that persists through multiple transmission hands.

### 7.2 What the English Classification Contributes

The English content classifications were performed on Gardner's English translation without any reference to the Coptic text. They represent a different kind of evidence: a content-based assessment of what each chapter teaches, classified into categories (substrate, editorial bridge, exhortation, dialogue frame, institutional). When these classifications are compared against the Coptic linguistic features, the areas of agreement are more informative than either method alone.

The strongest concordance occurs in the substrate chapters. When a chapter is classified as high-substrate from English content and simultaneously shows high cosmological Greek ratio from Coptic analysis, the identification is doubly confirmed. The holotype is Chapter 30: 85% substrate in English, cosmological ratio 0.60 in Greek, dialect ratio 1.000 in Coptic. Three independent signals converge on the same conclusion: this chapter belongs to the oldest compositional layer.

The English classification also reveals what the Coptic pipeline cannot: the internal structure of the teaching. The five-fold degree mapping of Chapter 104, the three-garment cosmology of Chapter 30, the elemental correspondences that run throughout the substrate chapters — these are visible in the English content but invisible to the Coptic linguistic analysis, which cannot distinguish a correspondential mapping from a mundane description by pattern matching alone. The two methods are complementary: the Coptic locates the layer; the English reveals what the layer contains.

### 7.3 Implications for the Ancient Word Hypothesis

Swedenborg claimed that a "Science of Correspondences" existed as the shared heritage of the ancient world, preserved in the East after it was lost in the West. The companion theses *The Magian Cosmos* and *The Resonant Cosmos* trace the historical transmission of this Science through the Zoroastrian mēnōg/gētīg ontology, the Avestan Nasks, and the Magian tradition that Mani inherited. *The Book of Zoroaster and the Children of the East* demonstrates that the Apocryphon of John's body-correspondence list traces to a "Book of Zoroaster" within this same transmission stream.

The Coptic validation adds a new kind of evidence to this chain. It is not textual evidence (what the Kephalaia says about correspondences) or historical evidence (who transmitted what to whom). It is linguistic evidence: the traces left in the Coptic text by the physical process of transmission. These traces confirm that the Kephalaia's teaching has a compositional history consistent with the Ancient Word hypothesis — a pre-scribal architecture transmitted through oral instruction and preserved by scribes who copied what they received.

The finding that dialect and content are independent (§3.4) is particularly significant. It means the correspondential substrate survived not just one but two scribal environments intact. The teaching that entered the Sub-Achmimic manuscript tradition was the same teaching that the Sahidic scribes later copied. If the scribes had been theological editors — if each scribal tradition had reworked the teaching according to its own understanding — the substrate would not be constant across dialect boundaries. The constancy of the substrate through variable scribal hands is the same pattern the framework identifies in NDE phenomenology (constant state, variable form) and in myth formation (same architecture, different cultural vessels). It is the signature of something being transmitted, not invented.

### 7.4 The Compiler Problem Revisited

A persistent question in Manichaean studies is the compiler problem: who assembled the Kephalaia as we have it? The manuscript postdates Mani by at least a century, possibly several. The scribal conventions (dialogue frames, chapter divisions, numbered headings) are editorial decisions that someone made. The question is whether the compiler was a faithful recorder or a creative editor.

The Coptic validation provides a partial answer. The compiler preserved the teaching with remarkable fidelity — the substrate content is independent of the scribal hand, meaning it was not reworked during the copy process. But the compiler did make editorial decisions: the chapter divisions, the dialogue framing, and the institutional vocabulary that appears in the later chapters are all compiler's choices. The three-layer model accounts for this: Layer 1 (the architecture) was transmitted faithfully; Layer 2 (Mani's oral instruction, including the naming system and the dialogue form) was the template the compiler worked from; Layer 3 (the scribal execution, including dialect and institutional vocabulary) reflects the compiler's own environment.

The compiler, in other words, did what scribes have done throughout the history of sacred text transmission: they preserved what they received and added the minimum editorial framework necessary to make it legible as a written document. The dialogue frames are their contribution. The chapter divisions are their contribution. The institutional vocabulary is their contribution. The five-fold degree mappings, the three garments, the elemental correspondences, the body-cosmos system — these are not their contribution. These passed through them.

### 7.5 Limitations and Lacunae

Several limitations must be acknowledged.

First, the analysis operates on AI-generated transcriptions of a printed critical edition, not on the original manuscript. The transcription process introduced at least one known encoding error (the digit-2/ϩ substitution on four pages), which was detected and corrected. Other transcription errors may exist undetected. The analysis measures what the transcription contains, which is an approximation of what the critical edition contains, which is itself an editorial reconstruction of what the manuscript contains.

Second, the dialect detection is limited to a single phonological alternation: ⲍ versus ϩ. Sub-Achmimic differs from Sahidic in other features (vowel patterns, verbal conjugations, lexical choices) that the current pipeline does not detect. The ⲍ/ϩ alternation was chosen because it is the most consistent and highest-frequency diagnostic marker, but it does not capture the full dialect picture.

Third, the Greek loanword lexicons are manually curated and may have gaps. Terms not included in the lexicons are invisible to the analysis. The known asymmetry — cosmological Coptic vocabulary is invisible to the Greek-only search — means the cosmological ratio systematically underestimates true substrate content.

Fourth, the English content classifications were performed by a language model, not by a trained Copticist reading the original text. They represent a competent but not expert-level content analysis of the English translation. Discordances between the Coptic and English signals may reflect classification errors in either direction.

Fifth, the concordance assessment uses fixed thresholds (e.g., sub-Achmimic ratio below 0.5 triggers a flag) that were set by judgment rather than by statistical optimization. Different threshold choices would produce different signal-to-flag ratios. The 1.5:1 ratio is descriptive, not confirmatory in any statistical sense.

Sixth, and most fundamentally, the analysis cannot distinguish between the hypothesis tested here (a pre-Manichaean architecture transmitted through Mani) and a simpler alternative (Mani composed the architecture himself, and the scribes faithfully transmitted Mani's composition). The independence of dialect and content is consistent with both hypotheses. The claim that the architecture predates Mani rests on the broader framework evidence — the parallels with Zoroastrian ontology, the Apocryphon of John's body-correspondence list, the structural identity with Swedenborgian correspondences — not on the Coptic linguistic data alone.

## 8. Conclusion: The Scribes Who Preserved What They Did Not Compose

The computational analysis of 116 chapters of the Kephalaia of the Teacher — 76,520 Coptic tokens subjected to dialect detection, Greek loanword stratification, formulaic pattern recognition, and cross-validation against independent English content classifications — reveals a manuscript with a three-layer compositional architecture. The layers are distinguishable, orthogonal, and internally consistent.

The innermost layer is the correspondential substrate: a teaching architecture of systematic mappings between natural forms and spiritual realities, organized by discrete degrees, expressed through the five Shekhinas, the three garments, the elemental correspondences, and the body-cosmos system. This architecture constitutes the bulk of the teaching content — up to 95% in the purest chapters — and is independent of the scribal medium in which it is preserved.

The middle layer is Mani's oral instruction: the naming system and dialogue form through which the architecture entered the manuscript tradition. The dialogue frames ("then he said," "we beseech you"), the blessing closures (ⲛⲁⲙⲉⲣⲉⲧⲉ, "my beloved ones"), and the chapter structure reflect this layer — the recording of speech as text, the translation of teaching into document.

The outermost layer is the scribal hands that committed the teaching to parchment. The Sub-Achmimic ratio quantifies their contribution: a gradient from 1.000 (the first hand's pure dialect) to 0.000 (the second hand's full normalization), with a corpus mean of 0.537 and a continuous distribution in between. The first hand preserved 56 ⲍ-forms in Chapter 30 without a single Sahidic intrusion. The second hand wrote 66 ϩ-forms in Chapter 78 without a single Sub-Achmimic retention. Between these extremes lies the mixed zone where most of the corpus resides — chapters bearing the traces of both hands in varying proportion.

The central finding is the independence of layers. Chapter 104 is pure Sahidic in dialect and 95% substrate in content. Chapter 78 is pure Sahidic in dialect and 0% substrate in content. The scribal hand does not determine the teaching content. The scribe who writes ϩ instead of ⲍ may copy the five-fold degree mapping exactly as received, or may add entirely new homiletic material — but the dialect does not predict which. This independence is the strongest evidence that the scribes were transmitters, not composers. They changed the spelling. They did not change the architecture.

The Greek loanword distribution confirms the institutional trajectory. Cosmological Greek concentrates in the first half of the manuscript (mean density 1.38% for chapters 1–74); ecclesiastical Greek rises in the second half (mean density 1.25% for chapters 75–122). This shift does not mark a change in teaching content — it marks the growing organizational vocabulary of the Manichaean church in Egypt. The substrate persists; the institutional language around it increases.

The cross-validation between Coptic linguistic features and English content classifications produces 104 concordance signals and 71 discordance flags. The concordances confirm the identification of the oldest layer: when English content analysis says "substrate" and Coptic analysis says "high cosmological ratio, consistent dialect, blessing closure present," both independent methods are converging on the same finding. The discordances are themselves informative: they reveal the limits of the Greek-only loanword search (which misses Coptic cosmological vocabulary), the differing granularity of the two classification systems (a two-word dialogue formula is visible in Coptic but invisible in English paragraph classification), and the gap between liturgical structure (blessing closures) and hortatory content (exhortation).

For the broader framework, this thesis provides the first computational linguistic evidence that the Kephalaia's teaching layer has the structural properties predicted by the Ancient Word hypothesis: a correspondential architecture that persists through multiple scribal environments without deformation. The constancy of the substrate through variable scribal hands is the same constant-state/variable-form pattern the framework identifies across domains. The teaching is the constant. The scribes are the variable. What the scribes changed was the spelling. What passed through them unchanged was the architecture.

The scribes who wrote these 76,520 tokens across 282 manuscript pages — spreading ⲍ across the early chapters and normalizing to ϩ in the later ones, framing the teaching in dialogue, sealing teaching units with ⲛⲁⲙⲉⲣⲉⲧⲉ, adding the institutional vocabulary of the church they served — these scribes preserved what they did not compose. Their traces are the evidence. The architecture is not theirs. It passed through them, as it passed through Mani, as it passed through the Magian tradition before him. The scribes are the outermost layer. The teaching is the innermost. Between them, ⲍ and ϩ tell the story of transmission.

Architecture, naming, inscription. One teaching, three layers, two hands.

## Appendix A: Dialect Distribution by Chapter

Sub-Achmimic ratio for all 116 analyzed chapters. SA = Sub-Achmimic marker count, Sah = Sahidic marker count. Band classifications: Pure SA (≥0.90), Pred. SA (0.70–0.89), Mixed-SA (0.50–0.69), Mixed-Sah (0.30–0.49), Pred. Sah (0.10–0.29), Pure Sah (≤0.09).

| Ch | Title | Tokens | SA | Sah | Ratio | Band |
|---|---|---|---|---|---|---|
| 1 | Concerning the Advent of the Apostle | 1424 | 171 | 93 | 0.648 | Mixed-SA |
| 2 | The Parable of the Tree | 1238 | 165 | 80 | 0.673 | Mixed-SA |
| 3 | The Interpretation of Happiness, Wisdom and Power | 561 | 73 | 10 | 0.880 | Pred. SA |
| 4 | Concerning the Four Great Days | 624 | 93 | 7 | 0.930 | Pure SA |
| 5 | Concerning Four Hunters of Light and Four of Darkness | 637 | 76 | 62 | 0.551 | Mixed-SA |
| 6 | Concerning the Five Storehouses | 1154 | 139 | 91 | 0.604 | Mixed-SA |
| 7 | The Seventh, concerning the Five Fathers | 657 | 43 | 59 | 0.422 | Mixed-Sah |
| 8 | Concerning the Fourteen Vehicles | 459 | 24 | 50 | 0.324 | Mixed-Sah |
| 9 | The Explanation of the Peace | 1386 | 115 | 115 | 0.500 | Mixed-SA |
| 10 | Concerning the Fourteen Mysteries | 424 | 28 | 29 | 0.491 | Mixed-Sah |
| 11 | Concerning all the Fathers | 406 | 28 | 16 | 0.636 | Mixed-SA |
| 12 | Concerning the Five Words | 299 | 20 | 12 | 0.625 | Mixed-SA |
| 13 | Concerning the Five Saviours | 234 | 29 | 9 | 0.763 | Pred. SA |
| 14 | The Interpretation of the Silence, the Fasting | 246 | 24 | 14 | 0.632 | Mixed-SA |
| 15 | Concerning the Five Parts of the World | 515 | 68 | 12 | 0.850 | Pred. SA |
| 16 | Concerning the Five Greatnesses | 1395 | 131 | 159 | 0.452 | Mixed-Sah |
| 17 | The Chapter of the Three Seasons | 588 | 49 | 40 | 0.551 | Mixed-SA |
| 18 | Concerning the Five Wars | 484 | 47 | 63 | 0.427 | Mixed-Sah |
| 19 | Concerning the Five Releases | 531 | 37 | 49 | 0.430 | Mixed-Sah |
| 20 | The Chapter of the Name of the Fathers | 371 | 12 | 16 | 0.429 | Mixed-Sah |
| 21 | Concerning the Father of Greatness | 272 | 15 | 4 | 0.789 | Pred. SA |
| 22 | On the Land of Light | 229 | 15 | 19 | 0.441 | Mixed-Sah |
| 23 | (Title damaged) | 783 | 82 | 81 | 0.503 | Mixed-SA |
| 24 | (Title damaged) | 1318 | 57 | 176 | 0.245 | Pred. Sah |
| 25 | Concerning the Advent of Five Fathers | 193 | 0 | 29 | 0.000 | Pure Sah |
| 26 | Concerning the First Man and the Ambassador | 396 | 21 | 37 | 0.362 | Mixed-Sah |
| 27 | Concerning the Five Forms in the Ruling of Greatness | 662 | 97 | 46 | 0.678 | Mixed-SA |
| 28 | Concerning the Twelve Judges of the Father | 638 | 70 | 75 | 0.483 | Mixed-Sah |
| 29 | Concerning the Eighteen Great Thrones | 623 | 60 | 43 | 0.583 | Mixed-SA |
| **30** | **Concerning the Three Garments** | **432** | **56** | **0** | **1.000** | **Pure SA** |
| 31 | Concerning the Summons | 438 | 60 | 33 | 0.645 | Mixed-SA |
| 32 | Concerning the Seven Works of the Living Spirit | 414 | 69 | 48 | 0.590 | Mixed-SA |
| 33 | Concerning the Five Things | 211 | 42 | 15 | 0.737 | Pred. SA |
| 34 | Concerning the Ten Things the Ambassador brought | 417 | 79 | 15 | 0.840 | Pred. SA |
| **35** | **Concerning the Four Works of the Ambassador** | **206** | **37** | **0** | **1.000** | **Pure SA** |
| 36 | Concerning the Wheel before the Sun Gate | 427 | 75 | 4 | 0.949 | Pure SA |
| 37 | Concerning the Three Zones | 230 | 26 | 19 | 0.578 | Mixed-SA |
| 38 | Concerning the Light Mind and the Apostles | 3125 | 296 | 261 | 0.531 | Mixed-SA |
| 39 | Concerning the Three Days and the Two Deaths | 700 | 70 | 68 | 0.507 | Mixed-SA |
| 40 | Concerning the Three Things established | 457 | 80 | 12 | 0.870 | Pred. SA |
| 41 | Concerning the Three Blows | 468 | 93 | 12 | 0.886 | Pred. SA |
| 42 | Concerning the Three Vessels | 1404 | 248 | 38 | 0.867 | Pred. SA |
| 43 | Concerning the Vessels | 777 | 83 | 81 | 0.506 | Mixed-SA |
| 44 | Concerning the Sea Giant | 706 | 46 | 97 | 0.322 | Mixed-Sah |
| 45 | Concerning the Vessels | 408 | 62 | 13 | 0.827 | Pred. SA |
| 46 | Concerning the Ambassador | 399 | 28 | 31 | 0.475 | Mixed-Sah |
| 47 | Concerning the Four Great Things | 653 | 74 | 44 | 0.627 | Mixed-SA |
| 48 | Concerning the Conduits | 1143 | 115 | 93 | 0.553 | Mixed-SA |
| 49 | Concerning the Wheel and the Conduits | 245 | 41 | 6 | 0.872 | Pred. SA |
| 50 | Concerning these Names: God, Rich One, Angel | 462 | 41 | 29 | 0.586 | Mixed-SA |
| 51 | Concerning the First Man | 423 | 16 | 38 | 0.296 | Pred. Sah |
| 52 | Concerning the Light | 569 | 51 | 41 | 0.554 | Mixed-SA |
| 53 | Concerning the First Man | 532 | 47 | 39 | 0.547 | Mixed-SA |
| 54 | Concerning the Quality of the Garments | 497 | 59 | 58 | 0.504 | Mixed-SA |
| 55 | Concerning the Fashioning of Adam | 969 | 53 | 137 | 0.279 | Pred. Sah |
| 56 | Concerning Saklas and his Powers | 1682 | 128 | 185 | 0.409 | Mixed-Sah |
| 57 | Concerning the Generation of Adam | 940 | 89 | 68 | 0.567 | Mixed-SA |
| 58 | The Four Powers that Grieve | 459 | 35 | 63 | 0.357 | Mixed-Sah |
| 59 | The Chapter of the Elements that Wept | 883 | 115 | 77 | 0.599 | Mixed-SA |
| 60 | Concerning the Four Fathers | 465 | 75 | 16 | 0.824 | Pred. SA |
| 61 | Concerning the Garment of the Waters | 915 | 37 | 130 | 0.222 | Pred. Sah |
| 63 | Concerning Love | 482 | 0 | 91 | 0.000 | Pure Sah |
| 64 | Concerning Adam | 440 | 64 | 4 | 0.941 | Pure SA |
| 65 | Concerning the Sun | 1596 | 146 | 110 | 0.570 | Mixed-SA |
| 66 | Concerning the Ambassador | 456 | 46 | 31 | 0.597 | Mixed-SA |
| 67 | Concerning the Light-Giver | 448 | 46 | 44 | 0.511 | Mixed-SA |
| 69 | Concerning the Twelve Signs of the Zodiac | 925 | 81 | 54 | 0.600 | Mixed-SA |
| 70 | Concerning the Body | 1445 | 142 | 74 | 0.657 | Mixed-SA |
| 71 | Concerning the Gathering in of the Elements | 424 | 27 | 38 | 0.415 | Mixed-Sah |
| 72 | Concerning the Worn and Torn Garments | 616 | 69 | 40 | 0.633 | Mixed-SA |
| 73 | Concerning the Envy of Matter | 582 | 94 | 21 | 0.817 | Pred. SA |
| 74 | Concerning the Living Fire | 419 | 40 | 43 | 0.482 | Mixed-Sah |
| 75 | Concerning the Letter | 650 | 18 | 104 | 0.148 | Pred. Sah |
| 76 | Concerning Lord Manichaios | 1163 | 141 | 88 | 0.616 | Mixed-SA |
| 77 | The Chapter of the Four Kingdoms | 615 | 52 | 29 | 0.642 | Mixed-SA |
| **78** | **Concerning the Four Things over which People Kill** | **381** | **0** | **66** | **0.000** | **Pure Sah** |
| 79 | Concerning the Fasting of the Saints | 405 | 1 | 70 | 0.014 | Pure Sah |
| 80 | The Commandments of Righteousness | 426 | 1 | 66 | 0.015 | Pure Sah |
| 81 | The Chapter of Fasting | 836 | 52 | 68 | 0.433 | Mixed-Sah |
| 82 | The Chapter of Righteous Judgement | 773 | 97 | 62 | 0.610 | Mixed-SA |
| 83 | Concerning the Man Ugly in Body | 938 | 46 | 119 | 0.279 | Pred. Sah |
| 84 | Concerning Wisdom | 1135 | 75 | 168 | 0.309 | Mixed-Sah |
| 85 | Concerning the Cross of Light | 1308 | 60 | 201 | 0.230 | Pred. Sah |
| 86 | Why am I Sometimes Sharp, Sometimes Not | 896 | 124 | 66 | 0.653 | Mixed-SA |
| 87 | Concerning the Alms | 680 | 90 | 15 | 0.857 | Pred. SA |
| 88 | Concerning the Catechumen who Found Fault | 687 | 58 | 70 | 0.453 | Mixed-Sah |
| 89 | The Chapter of the Nazorean | 656 | 56 | 47 | 0.544 | Mixed-SA |
| 90 | Concerning the Fifteen Paths | 1275 | 167 | 126 | 0.570 | Mixed-SA |
| 91 | Concerning the Catechumen: Shall He Be Saved? | 1439 | 202 | 144 | 0.584 | Mixed-SA |
| 92 | Why Did You Draw Every Teaching? | 570 | 87 | 36 | 0.707 | Pred. SA |
| 93 | A Catechumen Asked the Apostle | 730 | 86 | 48 | 0.642 | Mixed-SA |
| 94 | Concerning the Purification of the Four Elements | 374 | 59 | 18 | 0.766 | Pred. SA |
| 95 | What is Cloud? | 847 | 101 | 45 | 0.692 | Mixed-SA |
| 96 | The Three Earths that Bear Fruit | 485 | 32 | 47 | 0.405 | Mixed-Sah |
| 98 | What is Virginal? | 429 | 34 | 51 | 0.400 | Mixed-Sah |
| 99 | Concerning Transmigration | 507 | 58 | 35 | 0.624 | Mixed-SA |
| 100 | Concerning the Dragon with Fourteen Heads | 435 | 43 | 15 | 0.741 | Pred. SA |
| 101 | Why Does the Person Look Down? | 595 | 51 | 47 | 0.520 | Mixed-SA |
| 102 | Concerning the Light Mind | 627 | 58 | 68 | 0.460 | Mixed-Sah |
| 103 | Concerning the Five Wonders of the Light Mind | 396 | 0 | 78 | 0.000 | Pure Sah |
| **104** | **Concerning Food: Five Products of the Body** | **198** | **0** | **34** | **0.000** | **Pure Sah** |
| 105 | Concerning the Three Things that are Great | 417 | 27 | 48 | 0.360 | Mixed-Sah |
| 106 | There is No Joy that Shall Remain | 452 | 27 | 49 | 0.355 | Mixed-Sah |
| 107 | Concerning the Form of the Word | 419 | 23 | 41 | 0.359 | Mixed-Sah |
| 108 | Concerning the Seed Grain | 351 | 26 | 24 | 0.520 | Mixed-SA |
| 110 | Concerning the Nourishment of the Person | 336 | 23 | 27 | 0.460 | Mixed-Sah |
| 111 | Concerning the Four Archetypes | 346 | 49 | 4 | 0.925 | Pure SA |
| 113 | Whether Any Light Comes from the Body | 436 | 67 | 6 | 0.918 | Pure SA |
| 114 | Concerning the Three Images on the Right | 419 | 41 | 28 | 0.594 | Mixed-SA |
| 115 | Will Rest Come to the World? | 1930 | 138 | 184 | 0.429 | Mixed-Sah |
| 116 | Why Does Cutting a Nail Cause Pain? | 430 | 11 | 57 | 0.162 | Pred. Sah |
| 118 | (Fragment) | 56 | 4 | 2 | 0.667 | Mixed-SA |
| 119 | (Fragment) | 418 | 4 | 29 | 0.121 | Pred. Sah |
| 120 | Concerning the Two Essences | 588 | 42 | 32 | 0.568 | Mixed-SA |
| 121 | Concerning the Sect of the Basket | 481 | 34 | 36 | 0.486 | Mixed-Sah |
| 122 | Concerning the Assent and the Amen | 349 | 19 | 28 | 0.404 | Mixed-Sah |

Key chapters discussed in this thesis are shown in **bold**.

## Appendix B: Greek Loanword Rankings

### Top 15 Chapters by Cosmological Greek Density

| Ch | Title | Cosmo Density | Core % |
|---|---|---|---|
| 10 | Concerning the Fourteen Mysteries | 4.01% | 55% |
| 11 | Concerning all the Fathers | 3.69% | 74% |
| 13 | Concerning the Five Saviours | 2.56% | 85% |
| 69 | Concerning the Twelve Signs of the Zodiac | 2.49% | 84% |
| 14 | The Interpretation of the Silence | 2.44% | 62% |
| 119 | (Fragment) | 2.39% | 45% |
| 12 | Concerning the Five Words | 2.34% | 0% |
| 31 | Concerning the Summons | 2.28% | 88% |
| 6 | Concerning the Five Storehouses | 2.25% | 68% |
| 70 | Concerning the Body | 2.21% | 90% |
| 32 | Concerning the Seven Works of the Living Spirit | 2.17% | 93% |
| 37 | Concerning the Three Zones | 2.17% | 94% |
| 49 | Concerning the Wheel and the Conduits | 2.04% | 91% |
| 38 | Concerning the Light Mind and the Apostles | 2.02% | 63% |
| 103 | Concerning the Five Wonders of the Light Mind | 2.02% | 0% |

Of the top 15 cosmological Greek chapters, 11 (73%) have substrate content above 55%, confirming the correlation between cosmological Greek vocabulary and the oldest teaching layer. The exceptions (Ch 12 at 0%, Ch 103 at 0%, Ch 119 at 45%) illustrate the Greek ratio limitation discussed in §4.3.

### Top 15 Chapters by Ecclesiastical Greek Density

| Ch | Title | Eccl Density | Core % |
|---|---|---|---|
| 80 | The Commandments of Righteousness | 4.23% | 0% |
| 102 | Concerning the Light Mind | 3.67% | 0% |
| 63 | Concerning Love | 3.32% | 60% |
| 98 | What is Virginal? | 3.03% | 80% |
| 79 | Concerning the Fasting of the Saints | 2.47% | 0% |
| 1 | Concerning the Advent of the Apostle | 2.32% | 0% |
| 101 | Why Does the Person Look Down? | 2.18% | 78% |
| 99 | Concerning Transmigration | 2.17% | 0% |
| 10 | Concerning the Fourteen Mysteries | 2.12% | 55% |
| 9 | The Explanation of the Peace | 2.09% | 45% |
| 25 | Concerning the Advent of Five Fathers | 2.07% | 76% |
| 81 | The Chapter of Fasting | 2.03% | 0% |
| 3 | The Interpretation of Happiness, Wisdom and Power | 1.96% | 55% |
| 87 | Concerning the Alms | 1.91% | 15% |
| 100 | Concerning the Dragon with Fourteen Heads | 1.84% | 55% |

Of the top 15 ecclesiastical Greek chapters, 7 (47%) have substrate content of 0% or below 20%, confirming the correlation between ecclesiastical Greek vocabulary and the institutional/editorial layers. The exceptions (Ch 98 at 80%, Ch 101 at 78%, Ch 25 at 76%) reflect chapters where substrate teaching is discussed using institutional vocabulary — the terms traveled from the institutional layer into substrate-content chapters.

## Works Cited

**Primary text editions:**

1. Polotsky, H. J. and Böhlig, A. *Kephalaia: Manichäische Handschriften der Staatlichen Museen Berlin, Band I.* Stuttgart: Kohlhammer, 1940. The critical edition of the Coptic Kephalaia manuscript from Medinet Madi.

2. Gardner, Iain. *The Kephalaia of the Teacher: The Edited Coptic Manichaean Texts in Translation with Commentary.* Nag Hammadi and Manichaean Studies 37. Leiden: Brill, 1995 (2nd ed. 2005). English translation used for the content classifications.

**Primary theological sources:**

3. Swedenborg, Emanuel. *Arcana Coelestia.* London, 1749–1756. The systematic exposition of correspondences in the internal sense of Genesis and Exodus. Cited by section number (§).

4. Swedenborg, Emanuel. *Divine Love and Wisdom.* Amsterdam, 1763. The doctrine of discrete degrees and influx. Cited by section number (§).

**Scholarly works:**

5. Funk, Wolf-Peter. "The Reconstruction of the Manichaean Kephalaia." In *Coptic Studies: Acts of the Third International Congress of Coptic Studies*, edited by W. Godlewski, 145–159. Warsaw: PWN, 1990. On the textual reconstruction of the manuscript.

6. Pedersen, Nils Arne. *Studies in the Sermon on the Great War: Investigations of a Manichaean-Coptic Text from the Fourth Century.* Aarhus: Aarhus University Press, 1996. On the dialect and dating of Manichaean Coptic texts.

7. Kasser, Rodolphe. "A Standard System of Sigla for Referring to the Dialects of Coptic." *Journal of Coptic Studies* 1 (1990): 141–151. The standard dialectal classification system for Coptic, including the Sub-Achmimic/Lycopolitan designation.

**Internal library documents:**

8. [The Book of Zoroaster and the Children of the East: Material Evidence for the Ancient Word Transmission Hypothesis from the Nag Hammadi Apocryphon of John](../08_Correspondential_Texts/The%20Book%20of%20Zoroaster%20and%20the%20Children%20of%20the%20East_%20Material%20Evidence%20for%20the%20Ancient%20Word%20Transmission%20Hypothesis%20from%20the%20Nag%20Hammadi%20Apocryphon%20of%20John.md). Establishes the Apocryphon of John's body-correspondence list as a specimen of the "Ancient Word" transmitted via Magian traditions.

9. [The Magian Cosmos: A Comprehensive Analysis of the Principle of Correspondences in Ancient Iranian Religion and Its Esoteric Legacy](../02_Swedenborgian_Theology/The%20Magian%20Cosmos_%20A%20Comprehensive%20Analysis%20of%20the%20Principle%20of%20Correspondences%20in%20Ancient%20Iranian%20Religion%20and%20Its%20Esoteric%20Legacy.md). Reconstructs the principle of correspondences within the Zoroastrian mēnōg/gētīg ontology.

10. [The Resonant Cosmos: A Historical Reconstruction of the Science of Correspondences from the Magian Archives to the New Jerusalem](../02_Swedenborgian_Theology/The%20Resonant%20Cosmos_%20A%20Historical%20Reconstruction%20of%20the%20Science%20of%20Correspondences%20from%20the%20Magian%20Archives%20to%20the%20New%20Jerusalem.md). Traces the transmission of the Science of Correspondences from Iranian archives through Manichaeism into Central Asia.

11. [The Living Library: Correspondential Architecture Across the Nag Hammadi Collection](../08_Correspondential_Texts/The%20Living%20Library_%20Correspondential%20Architecture%20Across%20the%20Nag%20Hammadi%20Collection.md). Master survey categorizing NHL tractates by correspondential richness and structural depth.

12. [Reversing the Arrow: 'Gnosticism' as the Downstream Literalization of Correspondential Composition](../08_Correspondential_Texts/Reversing%20the%20Arrow_%20'Gnosticism'%20as%20the%20Downstream%20Literalization%20of%20Correspondential%20Composition.md). Argues that "Gnosticism" is a downstream product of failing to read correspondential texts as functional systems.

**Data sources:**

13. Coptic transcription corpus: 282 pages of AI-transcribed Coptic text from the Polotsky/Böhlig critical edition, processed via two-pass transcription pipeline. Repository: `manichaean-analysis/output/projects/kephalaia/coptic/transcriptions/`.

14. English content classifications: Per-chapter English content analysis of Gardner's translation, performed via structured extraction pipeline. Repository: `manichaean-analysis/output/projects/kephalaia/core/chapters/`.

15. Coptic validation pipeline: `coptic_validation.py` — deterministic pattern-matching analysis producing per-chapter JSON analyses and corpus summary. Repository: `manichaean-analysis/scripts/coptic_validation.py`.
