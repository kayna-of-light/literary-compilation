# Research Questions

This document tracks open research questions, gaps in analysis, and hypotheses requiring further investigation. Questions are formatted for use with external research tools (NotebookLM, Gemini Deep Research, NDE Statistical Repository).

> **Usage**: Copy the relevant question block (context + question) to the appropriate research tool. Questions are separated by horizontal rules for easy identification.

---

## How to Add Questions

When identifying a gap or question during framework development:

1. **Classify the domain** — Which thematic area does this question address?
2. **Provide context** — Brief background sufficient for the research tool
3. **State the question clearly** — Specific, answerable research question or hypothesis
4. **Tag the target system** — Which tool is best suited to answer this?

### Target System Tags

| Tag | System | Context Length | Best For |
|-----|--------|----------------|----------|
| `[NLM]` | NotebookLM | Short (~500 chars) | Scholarly sources, theological texts |
| `[GDR]` | Gemini Deep Research | Extended | Web analysis, cross-referencing, synthesis |
| `[NDE]` | NDE Statistical Repository | Variable | Statistical queries on NDE dataset |

---

## Open Questions

### Critical Analysis Follow-Up Questions (2025-12-29)

The following questions emerged from knowledge graph validation and @critic report analysis. These target specific empirical gaps and source verification needs.

---

### [NDE] CONSC-034: Restorative Path Violent Death Correlation

**Target**: `[NDE]`  
**Status**: ✅ RESOLVED  
**Date Added**: 2025-12-29  
**Date Resolved**: 2025-12-30  
**Priority**: HIGH  
**Related Nodes**: CONSC-034, CONSC-002, CONSC-031

**Context**:
The Threefold Path cosmology claims >70% of DOPS past-life cases involve violent or premature death, validating the "Restorative Incarnation" pathway.

**RESOLUTION:**
The claim is **VALIDATED** by the DOPS Case Verification and Critiques report (`data/01_Consciousness_Studies/DOPS Case Verification and Critiques.md`).

**Key Statistical Findings:**

| Metric | Value | Source |
|--------|-------|--------|
| Violent/Unnatural Death Rate | **>70%** | DOPS global database (n=2,500+) |
| Birthmark Prevalence | **30-35%** | Cases with physical correlates |
| Birthmark Verification Rate | **88%** | Medical document confirmation (n=49) |
| Global Solution Rate | **67-73%** | Solved vs. unsolved cases |

**Definition of "Violent Death" in DOPS Coding:**
- Accident
- Murder  
- Suicide
- Combat/War

**Critical Finding from Report:**
> "In over **70%** of verified cases worldwide, the previous personality died by violent or unnatural means (accident, murder, suicide, combat). This 70% figure is a massive deviation from the general mortality statistics of the relevant populations, where natural causes (disease, old age) account for the vast majority of deaths."

**Solved vs. Unsolved Pattern:**
> "Interestingly, the incidence of violent death claims is often *higher* in unsolved cases than in solved ones. This suggests that the trauma of a violent death is the primary driver for the retention of past-life memories (the 'Restorative Incarnation' hypothesis), but the chaos often associated with such deaths (e.g., soldiers dying in foreign wars, anonymous murders) makes verification more difficult."

**Source Chain:**
1. `[T]` DOPS Case Verification and Critiques.md (framework synthesis)
2. `[S]` WHRO Educational News (2024-12-30) - global statistics
3. `[P]` DOPS publications: Stevenson (STE15, STE16), Tucker (2000)
4. `[E]` UVA DOPS database (~2,500 cases)

**Framework Implication:**
The >70% violent death correlation **strongly validates** the "Restorative Incarnation" pathway in the Threefold Path cosmology. The pattern is consistent across cultures despite varying solution rates. The combination of violent death + birthmark correspondence creates a predictable profile supporting the hypothesis that incomplete/traumatic life termination triggers the Restorative path mechanism.

**CONSC-034 Status:** Upgrade from "contested" to **"validated"** with robust DOPS empirical support.

---

### [NDE] CONSC-033: Stage Transition Rates and Truncation Analysis

**Target**: `[NDE]`  
**Status**: RESOLVED  
**Date Added**: 2025-12-29  
**Date Resolved**: 2025-12-29  
**Priority**: HIGH  
**Related Nodes**: CONSC-033, CONSC-028, SWED-003

**Context**:
Four-stage sequential analysis found only 40% canonical rate vs. 70%+ predicted. The 0% unusual ordering (no cases showing Stage 3 before Stage 2) suggests truncation, not disorder. Need granular stage transition data to validate truncation hypothesis.

**Research Question**:
1. What percentage of NDEs terminate at each stage? (Stage 1 only: __%; Stage 1+2: __%; etc.)
2. Are truncated NDEs concentrated at specific stages? (Which stages are "return points"?)
3. Is truncation correlated with NDE cause? (Cardiac arrest vs. trauma vs. other)
4. Can we calculate stage-to-stage transition rates? (P(Stage 2 | Stage 1 complete) = ?)
5. What factors predict NDE depth/duration? (Greyson Scale correlation with stages reached)
6. Is there a "point of no return" after which canonical completion becomes likely?

**RESOLUTION** (from `nde-analysis/docs/reports/threefold-path-validation-report.md`):

**Key Findings:**
- **40.0% (2,698 cases)** follow canonical 4-stage sequence
- **0.0% unusual ordering** - NO cases showed stages out of sequence
- This validates the **truncation hypothesis** - the 30% gap is explained by early termination, not disorder

**Stage-by-Stage Rates (n=6,739):**
| Stage | Element | Rate |
|-------|---------|------|
| Stage 1 (Passage) | OBE | 55.0% (3,706) |
| Stage 1 (Passage) | Tunnel | 23.2% (1,561) |
| Stage 1 (Passage) | Peaceful | 47.4% (3,195) |
| Stage 2 (Arrival) | Being Encounter | **92.9%** (6,262) |
| Stage 2 (Arrival) | Deceased Relatives | 21.1% (1,423) |
| Stage 2 (Arrival) | Sense of Belonging | 46.0% (3,100) |
| Stage 3 (Life Review) | Occurred | **18.6%** (1,253) |
| Stage 3 (Life Review) | No External Condemnation | 84.8% |
| Stage 4 (Integration) | Value Shifts | 35.0% |
| Stage 4 (Integration) | Lost Fear of Death | 41.1% |

**Interpretation:**
- Stage 2 (Being Encounter) nearly universal at 92.9%
- Stage 3 (Life Review) is the major truncation point at only 18.6%
- 60% of NDEs terminate before life review stage
- Absence of disorder (0% unusual ordering) CONFIRMS sequential structure
- CONSC-033 can be upgraded from "contested" to "validated with truncation caveat"

**Source**: `nde-analysis/docs/reports/threefold-path-validation-report.md` (December 13, 2025)

---

### [GDR] CROSS-006: Jesus Identification Percentage Verification

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-29  
**Priority**: MEDIUM  
**Related Nodes**: CROSS-006, CONSC-016

**Context**:
The Jesus Profile Thesis (CROSS-006) claims "~60% Western experiencers identify Being of Light as Jesus." This statistic is used as validation that editorial bricolage "succeeded"—the curated Jesus Profile matches actual spiritual entity encountered. Source chain shows only `[E] NDE phenomenology research (various)`. No specific study cited.

**Research Question**:
1. What is the EXACT percentage and what study/studies is it derived from?
2. Which researcher(s) published this statistic? (Long, Ring, van Lommel, Greyson?)
3. Does the percentage vary by decade? (1970s studies vs. 2020s?)
4. Does the percentage vary by region within "Western" category? (US vs. UK vs. Germany?)
5. How is "identification as Jesus" operationalized? (Name stated, visual match, innate knowing?)
6. What percentage identify other religious figures? (Angels, deceased relatives, generic light?)

**Expected Output**:
Specific citation with study name, sample size, and methodology. If no primary source exists, flag as unsupported claim requiring revision or removal.

**Notes**:
~60% appears in multiple framework documents without primary citation. May be folk knowledge in NDE community that needs verification.

---

### [NLM] SWED-042: Damdat Nask Reconstruction Sources

**Target**: `[NLM]`  
**Status**: ✅ RESOLVED  
**Date Added**: 2025-12-29  
**Date Resolved**: 2025-12-29
**Priority**: MEDIUM  
**Related Nodes**: SWED-042, SWED-004, SWED-041
**Resolution Document**: `data/unclassified/Bundahišn's Damdat Nask Reconstruction.md`

**RESOLUTION:**

**Key Validated Findings:**

| Element | Source | Verification |
|---------|--------|--------------|
| Dāmdād Nask was 4th Nask of Hada Mānsrīg division | Dēnkard 8.5 | MacKenzie, EIr |
| 32 kardag (sections) covering cosmogony, taxonomy, eschatology | Dēnkard 8.5 | West, Widengren |
| Zādspram explicitly cites "the Dāmdād Nask" (3.43, 3.57) | Wizīdagīhā ī Zādspram | MacKenzie |
| Bundahišn structure aligns chapter-for-chapter with Dēnkard summary | Structural analysis | Henning, Götze |
| Chapter 28: Microcosm-Macrocosm correspondence map | Greater Bundahišn | Lincoln, Herrenschmidt |

**Critical Scholarly Assessment:**
- The Bundahišn is "essentially an epitome" (MacKenzie) / "a major source" of the Zand of the Dāmdād Nask
- The "systematic correspondence" claim is VALIDATED by Chapter 28's anatomical-cosmic mapping
- However: "Persepolis archives" destruction is HAGIOGRAPHIC LEGEND, not verified history
- Damdat Nask content survived via ORAL Zand tradition, not burned books

**Knowledge Graph Update:** SWED-042 updated with nuanced scholarly caveats distinguishing hagiographic claims from validated reconstruction evidence.

---

### [GDR] SWED-042: Alexander Archive Destruction Historiography

**Target**: `[GDR]`  
**Status**: ✅ RESOLVED  
**Date Added**: 2025-12-29  
**Date Resolved**: 2025-12-29
**Priority**: MEDIUM  
**Related Nodes**: SWED-042, SWED-004
**Resolution Document**: `data/unclassified/Alexander, Persepolis, and Avestan Texts.md`

**RESOLUTION:**

**Key Findings from Historiographical Analysis:**

| Question | Answer |
|----------|--------|
| Did Alexander burn Persepolis? | **YES** - Undisputed historical fact (330 BCE) |
| Do classical sources mention religious archives? | **NO** - Arrian, Diodorus, Plutarch, Curtius are SILENT on religious texts |
| Was there archaeological evidence of document destruction? | **YES** - Bullae (clay sealings) prove parchment documents existed and were destroyed |
| Was there a written Avesta to destroy? | **NO** - Scholarly consensus: Avesta was ORAL in Achaemenid period |
| Is "12,000 ox-hides" historical? | **NO** - Zoroastrian HAGIOGRAPHY serving Sasanian ideological purposes |

**The Scholarly Consensus (Kellens, Hoffmann, Skjærvø, de Jong):**
1. The Avesta was an **oral corpus** until Sasanian codification (4th-6th c. CE)
2. Alexander destroyed **administrative archives** (Aramaic parchment), not religious texts
3. The "Burned Book" narrative was constructed by Sasanians to:
   - Explain gaps in their tradition
   - Legitimize creating a written canon
   - Compete with "Peoples of the Book" (Christianity, Manichaeism)
4. Mary Boyce's "living books" argument: The real loss was the **slaughter of Magi** who carried oral tradition

**Framework Implication:**
SWED-042 must be updated to clearly distinguish:
- **Validated**: Alexander destroyed Persepolis (fact) + administrative archives burned (archaeological)
- **Hagiographic**: "12,000 ox-hides with gold ink" = legendary expansion
- **Actual mechanism of loss**: Oral transmission disruption + later Islamic conquest

**Knowledge Graph Update:** SWED-042 definition and caveats substantially revised.

---

### [NLM] SWED-043: Daniel Historicity Scholarly Consensus

**Target**: `[NLM]`  
**Status**: ✅ RESOLVED  
**Date Added**: 2025-12-29  
**Date Resolved**: 2025-12-29
**Priority**: MEDIUM  
**Related Nodes**: SWED-043, EARLY-008
**Resolution Document**: `data/unclassified/Daniel_ Historicity and Cultural Synthesis.md`

**RESOLUTION:**

**CRITICAL ERROR CORRECTED:**
Daniel is **NEVER** called "Rab-mag" in the biblical text! That title belongs exclusively to **Nergal-sharezer** in Jeremiah 39:3, 39:13.

**Daniel's Actual Biblical Titles:**
| Title | Reference | Meaning |
|-------|-----------|---------|
| Rab-signīn | Dan 2:48 | Chief Prefect |
| Rab-hartummin | Dan 4:9 (MT 4:6) | Chief of Magicians/Scribes |

**Scholarly Consensus on Historicity:**
- **Final redaction**: 167-164 BCE (Maccabean period) - near-universal consensus
- **Court Tales (Dan 1-6)**: Older traditions, likely 4th-3rd c. BCE
- **Belshazzar**: CONFIRMED historical (Nabonidus Chronicle) - validates genuine tradition
- **"Darius the Mede"**: NO external attestation - likely literary construct
- **Persian loanwords**: ~20 terms confirm deep Persian acculturation

**Validated Historical Details:**
- Belshazzar as regent (historically accurate)
- "Third ruler" offer (Dan 5:16) - reflects actual Neo-Babylonian hierarchy
- Persian administrative terminology
- Fire punishment (Babylonian) vs. lion punishment (Persian) distinction

**Knowledge Graph Update:**
- SWED-043 title changed from "Rab-mag" to "Rab-hartummin"
- Confidence downgraded from "high" to "medium"
- Definition rewritten to reflect compositional dating
- EARLY-008 references corrected

---

### [GDR] Zoroastrian mēnōg/gētīg Ontology Academic Sources

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-29  
**Priority**: MEDIUM  
**Related Nodes**: SWED-041, SWED-042, SWED-004

**Context**:
Framework claims Zoroastrian mēnōg (spiritual)/gētīg (physical) ontology parallels Swedenborg's doctrine of correspondences. This is a significant claim requiring independent verification from academic Iranology, not just Swedenborgian sources.

**Research Question**:
1. How do academic Iranologists (Mary Boyce, Shaul Shaked, Jenny Rose) describe the mēnōg/gētīg distinction?
2. Is there textual evidence for systematic "correspondence" thinking in Zoroastrian sources?
3. How does the Bundahišn taxonomy of beneficent/noxious creatures work?
4. Are there academic studies comparing Zoroastrian natural classification to medieval European correspondence systems?
5. What do scholars say about the antiquity vs. late development of mēnōg/gētīg concepts?
6. Is there any scholarly precedent for connecting Swedenborg's correspondences to Iranian sources?

**Expected Output**:
Independent academic verification of parallel ontology. If scholars confirm systematic correspondence thinking in Zoroastrianism, strengthens Ancient Word hypothesis. If scholars describe it differently, framework interpretation may need revision.

**Notes**:
Key for external triangulation (SWED-037 principle). Framework cannot validate itself—needs independent scholarly confirmation.

---

### Source Tracing Follow-Up Questions (2025-12-29)

The following questions emerged from source tracing analysis of the NDE empirical documents. See `docs/SOURCE_TRACE_REPORT_conceptual_framework_deep_dive.md` for full report.

---

### [NDE] Operationalization: "Unknown Presence" Classification Criteria

**Target**: `[NDE]`  
**Status**: Open  
**Date Added**: 2025-12-29  
**Priority**: HIGH  
**Related Files**: `conceptual_framework_deep_dive_report-analysis_iands_and_nand_2025.md`

**Context**:
Framework analysis claims 61.8% of Being of Light encounters are classified as "unknown presence" (1,970 of 3,189 cases). This is described as the "strongest evidence" for objective reality since it shows experiencers encounter something that transcends their available conceptual categories.

**Research Question**:
1. What questionnaire fields in NDERF/IANDS are used to extract "being identification"?
2. What are the exact response options that map to "unknown presence" classification?
3. Is "unknown presence" a distinct response option, or a researcher-assigned category for ambiguous responses?
4. How do we distinguish "unknown presence" from "not reported" or "declined to answer"?
5. What is the inter-rater reliability for this classification if researcher-assigned?

**Expected Output**:
Documentation of the operationalization criteria for "unknown presence" sufficient for replication.

**Notes**:
This is a CRITICAL claim requiring rigorous methodology documentation. If "unknown" simply means "didn't specify," the interpretation changes dramatically.

---

### [NDE] Operationalization: "Reincarnation Indicators" Search Criteria

**Target**: `[NDE]`  
**Status**: Open  
**Date Added**: 2025-12-29  
**Priority**: HIGH  
**Related Files**: `conceptual_framework_deep_dive_report-analysis_iands_and_nand_2025.md`

**Context**:
Framework claims "0% reincarnation indicators" in NDE accounts as evidence for "Normative Path" (continuation without reincarnation). A 0% finding is an extraordinary claim requiring extraordinary documentation.

**Research Question**:
1. What search terms/keywords were used to identify "reincarnation indicators"?
2. What narrative patterns were coded as potential reincarnation evidence?
3. Were Eastern religion NDEs (Hindu, Buddhist) included in this search?
4. How were accounts mentioning "returning" or "choosing a new life" handled?
5. Were ambiguous phrases like "going back" coded as reincarnation indicators?

**Expected Output**:
Complete operationalization of "reincarnation indicator" category including search terms, coding criteria, and examples of included/excluded narratives.

**Notes**:
0% is almost certainly an artifact of coding choices or sample bias. Need to understand methodology to assess validity.

---

### [GDR] NDERF Database Access and Research Protocols

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-29  
**Priority**: MEDIUM  
**Related Files**: Source tracing documentation

**Context**:
Framework analysis uses NDERF database (n=5,646) as primary data source. Need to verify the data access and usage protocols for scholarly citation.

**Research Question**:
1. What is the official research access protocol for NDERF data?
2. Are there published datasets or APIs, or is web scraping required?
3. What are NDERF's data use and citation requirements?
4. Has Dr. Jeffrey Long published methodology for the NDERF questionnaire?
5. Are there IRB-approved protocols for secondary analysis of NDERF data?

**Expected Output**:
Documentation of data access protocols and citation requirements for NDERF database use.

**Notes**:
This affects all NDE empirical documents in the framework.

---

### Critical Analysis Follow-Up Questions

The following questions emerged from rigorous critical review of framework claims (2025-12-27). These require external research to strengthen or revise framework positions.

---

### [NDE] Cross-Cultural Being Identification

**Target**: `[NDE]`  
**Status**: RESOLVED  
**Date Added**: 2025-12-27  
**Date Resolved**: 2025-12-29

**Context**:
Framework claims NDErs identify "Being of Light" as Jesus based on personality match, even atheists/non-Christians. Critical analysis challenges this: selection bias (most studies in Christian-majority cultures) and expectation effects. Need cross-cultural statistical data.

**Research Question**:
In NDEs from Hindu-majority, Buddhist-majority, and Islamic-majority populations, what percentage of experiencers identify the "Being of Light" encountered as:
1. Jesus Christ
2. Deities from their cultural tradition (Krishna, Yamaraj, Buddha, etc.)
3. Generic "deceased relatives" or unnamed beings
4. No being encountered

Does personality-based identification transcend cultural conditioning, or do experiencers interpret the encounter through pre-existing religious frameworks?

**RESOLUTION** (from `nde-analysis/docs/reports/conceptual_framework_deep_dive_report.md`):

**Being of Light Identification (n=3,189 Light Being encounters):**
| Identification | Count | Percentage |
|----------------|-------|------------|
| **Unknown Presence** | **1,970** | **61.8%** |
| God | 732 | 23.0% |
| Jesus | 358 | 11.2% |
| Religious Figure | 129 | 4.0% |

**Critical Finding: 61.8% identify as "Unknown Presence"** - transcends ALL cultural categories.

**By Religious Background:**
| Religion | % "Unknown Presence" | % Using Cultural Labels |
|----------|---------------------|------------------------|
| Atheist/Agnostic | **70.3%** | 29.7% |
| Christian | ~62% | ~38% (God/Jesus) |
| Spiritual not Religious | ~60% | ~40% |
| Muslim | ~29% | ~71% |
| Hindu/Buddhist | ~30-38% | ~62-70% |

**Statistical Test:**
- Chi-Square: χ² = 461.23, p < 0.0001 (highly significant)
- Cramér's V = 0.240 (medium effect size)
- **Result:** Religious background significantly affects HOW the Light Being is named

**Key Interpretation:**
1. **Universal Singular Entity:** ONE Light Being across ALL religions (even polytheists report singular presence)
2. **Transcends Categories:** 61.8% cannot label the being - strongest evidence for objective reality
3. **Cultural Vocabulary, Not Cultural Entity:** Christians use "God/Jesus," Muslims use "Allah," Atheists use "Unknown" - but ALL describe the SAME BEING with consistent properties
4. **Atheists most likely to report "Unknown"** - no pre-existing vocabulary, yet encounter same entity
5. The Being exhibits consistent characteristics: singular, loving, conscious, authoritative

**Framework Implications:**
- Framework's "Jesus identification" claim requires nuance: only 11.2% identify as Jesus
- The 61.8% "Unknown Presence" rate STRENGTHENS the objective reality model
- Cultural naming ≠ cultural projection; the entity transcends conceptual categories

**Source**: `nde-analysis/docs/reports/conceptual_framework_deep_dive_report.md` (December 13, 2025)

**Notes**:
If Hindu NDErs predominantly report Hindu deities rather than Jesus, framework's "pure identification" claim requires revision. See `critical_analysis_report.md` Section 7B.

---

### [GDR] Dying Brain Hypothesis - Current State

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27

**Context**:
Framework interprets NDEs as evidence for post-mortem consciousness. Critical analysis notes framework doesn't adequately engage strongest neuroscientific alternatives. Need comprehensive review of current dying brain research to address fairly.

**Research Question**:
What is the current state of neuroscientific explanations for NDE phenomenology? Specifically:
1. Borjigin et al. (2013) findings on surge of brain activity at death
2. DMT hypothesis (Strassman; endogenous release at death)
3. Temporal lobe seizure models for life review
4. Visual cortex explanations for tunnel/light
5. Recent AWARE study results and methodological critiques

How do neuroscientists explain veridical perception cases? What are the strongest counterarguments to materialist explanations that framework should address?

**Notes**:
Framework should engage this literature seriously, not dismissively. Veridical perception is framework's strongest evidence; need to know neuroscience's best responses. See `critical_analysis_report.md` Section 7A.

---

### [GDR] CDE Core Validation: Methodological Frameworks for Detecting Conscious Influence

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: CRITICAL  
**Related Nodes**: CONSC-001, CROSS-003, CROSS-004

**Context**:
The Consciousness-Driven Evolution (CDE) hypothesis is THE CORE MECHANISM of the entire framework. It proposes that NDE research demonstrates contact with a single, all-encompassing, loving consciousness (consistent across cultures). If this unified loving consciousness exists and is real, its influence should be visible in historical patterns, measurable in narrative evolution, consistent across cultures, and directional toward coherence/love/unity. This is not a competing theory—it's testing whether we can detect the fingerprints of unified loving consciousness throughout human history.

**Research Question**:
What methodologies exist for detecting non-material causal influences on historical and cultural patterns? Specifically:
1. How do we distinguish conscious influence from standard memetic/cultural evolution?
2. What statistical signatures would differentiate conscious influence from random cultural drift?
3. Can we identify "influx events" where consciousness-related breakthroughs cluster historically?
4. What would constitute falsifiable predictions of conscious influence on myth/narrative evolution?
5. Do Boyd & Richerson's Dual Inheritance Theory or Wilson's Cultural Group Selection provide sufficient explanations for "ruling love polarity" patterns (cooperation vs. defection dynamics at cultural scale)?
6. If consciousness is fundamental (not epiphenomenal), what observable differences should exist compared to materialist cultural evolution models?

**Expected Output**:
Methodological framework for testing CDE as core mechanism. Criteria for distinguishing conscious influence from emergent cultural patterns. Falsifiable predictions that would validate or challenge the hypothesis.

**Notes**:
This is the foundational question for the entire framework. CDE is not competing with memetics—it's proposing consciousness as the causal driver BEHIND memetic selective pressures. See CONSC-001, framework synthesis documents.

---

### [NDE] NDE Consistency Across Cultures: Loving Consciousness Foundation

**Target**: `[NDE]`  
**Status**: RESOLVED  
**Date Added**: 2025-12-27  
**Date Resolved**: 2025-12-29  
**Priority**: CRITICAL  
**Related Nodes**: CONSC-004, CONSC-008, CONSC-016

**Context**:
CDE's foundational premise: NDE research demonstrates contact with a single, all-encompassing, loving consciousness consistent across cultures, backgrounds, and beliefs. If this is accurate, it provides the empirical foundation for claiming conscious influence on history. Need statistical validation.

**Research Question**:
What percentage of NDEs across all cultures report encounter with a loving, unified consciousness (vs. neutral or negative)?
1. How consistent is the "loving presence" phenomenology across: religious believers, atheists, different faith traditions?
2. Statistical analysis: Does religious/cultural background predict NDE affective valence (loving vs. neutral vs. negative)?
3. Temporal stability: Has this pattern remained consistent from 1970s NDE research to present?
4. Cross-cultural comparison: Japanese, Hindu, Muslim, Indigenous NDEs—same loving consciousness or culturally-specific beings?
5. Correlation between depth of NDE (Greyson Scale score) and sense of unified loving consciousness?
6. What percentage of atheist/materialist NDErs report the same loving presence as religious believers?

**RESOLUTION** (from `nde-analysis/docs/reports/conceptual_framework_deep_dive_report.md`):

**Key Finding: CONSISTENT LOVING CONSCIOUSNESS VALIDATED**

**Being of Light Encounter (n=6,739):**
- **Being of Light encounters: 47.3%** (3,189 cases)
- Among encounters, **79.4% report active communication** (intentional two-way dialogue)
- **59.6% receive significant guidance** from the Being
- The Being exhibits **consistent personal characteristics** across all backgrounds

**Fear Loss by Religion (virtually identical rates):**
| Religion | Total | Lost Fear | Percentage |
|----------|-------|-----------|------------|
| Spiritual not Religious | 464 | 290 | 62.5% |
| Christian | 1,669 | 1,038 | 62.2% |
| Atheist/Agnostic | 348 | 217 | **62.3%** |
| Muslim | 35 | 22 | 62.9% |
| Jewish | 30 | 18 | 60.0% |

**Cross-Religious Consistency:**
- Range: 60.0% - 62.9%
- Mean: 62.0%
- **Standard deviation: 1.1%**
- **Coefficient of variation: 1.8%** (extremely low)

**Belief Correction Evidence:**
| Pattern | Finding |
|---------|---------|
| **Christians expecting judgment** | Found love → 86.8% no condemnation |
| **Atheists expecting nothingness** | Found consciousness → 20.4% became spiritual |
| **Universal pattern** | 56.4% complete fear loss across ALL backgrounds |

**Five Markers of Personal Conscious Entity (Being of Light):**
1. **Intentional Communication:** 79.4% engage in dialogue
2. **Purposeful Guidance:** 59.6% receive specific teaching
3. **Emotional Expression:** Conveys love, understanding, acceptance
4. **Individual Recognition:** Knows experiencer's life story
5. **Responsive Interaction:** Answers questions, responds to thoughts

**Interpretation:**
- The 1.8% variation coefficient across religions provides **strong statistical evidence** for consistent conscious entity
- **This is NOT cultural projection** - if it were, Christian and Muslim rates would differ significantly
- Atheists show SAME transformation rates as believers (62.3% vs 62.2%)
- The "expect judgment, find love" pattern demonstrates experience CORRECTS theological expectations

**Conclusion:** CDE's foundational premise is **VALIDATED** - a consistent loving consciousness appears across all cultural/religious boundaries with statistically negligible variation.

**Source**: `nde-analysis/docs/reports/conceptual_framework_deep_dive_report.md` (December 13, 2025)

**Notes**:
This is CRITICAL. If loving consciousness is NOT consistent across cultures, CDE's premise collapses. If IT IS consistent, provides extraordinary evidence for unified conscious influence. See CONSC-004, CONSC-008 caveats on selection bias.

---

### [NDE] Distressing NDEs and the Ruling Love Hypothesis

**Target**: `[NDE]`  
**Status**: RESOLVED  
**Date Added**: 2025-12-27  
**Date Resolved**: 2025-12-29  
**Priority**: HIGH  
**Related Nodes**: CONSC-004, SWED-003, CROSS-003

**Context**:
Swedenborgian cosmology predicts post-mortem experiences reflect "ruling love"—self-centered souls should experience initial distress matching their internal state. Framework emphasizes blissful NDEs. Need statistical data on distressing experiences to test ruling love hypothesis.

**Research Question**:
What percentage of documented NDEs are classified as distressing, frightening, or hellish?
1. Breakdown by type: Inverse Experience (opposite of blissful), Void/Emptiness, Hellish Realm encounters?
2. Demographic/psychological profiles: Do distressing NDEs correlate with specific personality traits, life circumstances, or moral frameworks?
3. Transition patterns: What percentage of distressing NDEs later shift to positive (as in Howard Storm case)?
4. Aftereffects: Do distressing NDErs show same life transformation as positive NDErs, or different trajectories?
5. Cross-cultural variation: Are distressing NDEs more common in certain cultural/religious contexts?
6. Ruling love test: Can we identify correlation between self-reported life orientation (service vs. self-interest) and NDE valence?

**RESOLUTION** (from `nde-analysis/docs/reports/conceptual_framework_deep_dive_report.md`):

**Key Findings - Life Review Judgment Data (n=1,253 with life reviews):**
| Judgment Source | Count | Percentage |
|-----------------|-------|------------|
| None | 714 | 57.0% |
| Self-judgment only | 329 | 26.3% |
| Guide/Light judgment | 116 | 9.3% |
| Not mentioned | 74 | 5.9% |
| **Harsh/punishing** | **20** | **1.6%** |

**No External Condemnation: 84.8%** (none + self-judgment only)

**Emotional Tone During Life Review:**
| Emotion | Count | Percentage |
|---------|-------|------------|
| Mixed emotions | 564 | 45.0% |
| Love | 336 | 26.8% |
| Neutral | 97 | 7.7% |
| Shame/Regret | 98 | 7.8% |
| Not specified | 138 | 11.0% |

**Love-to-Shame Ratio: 3.4:1**

**No External Condemnation by Religion:**
| Religion | Total | No External | Rate |
|----------|-------|-------------|------|
| Spiritual not Religious | 132 | 87 | 65.9% |
| Atheist/Agnostic | 147 | 90 | 61.2% |
| Christian | 775 | 673 | 86.8% |
| Muslim | 15 | 9 | 60.0% |

**Interpretation:**
- Distressing/punishing experiences are RARE at only **1.6%**
- This is BELOW the expected 5-15% threshold
- 84.8% no external condemnation rate is remarkably consistent across religions (60-87%)
- The data suggests life reviews are predominantly non-judgmental
- Framework implications: Ruling love may manifest differently than expected—the Being of Light appears to demonstrate unconditional acceptance rather than reflecting back self-orientation

**Source**: `nde-analysis/docs/reports/conceptual_framework_deep_dive_report.md` (December 13, 2025)

**Notes**:
Critical test of ruling love polarity. Cherry-picking blissful NDEs while ignoring distressing ones undermines framework integrity. Must address full phenomenological range. See CONSC-004, Swedenborg H&H §§ 477-480.

---

### [NDE] Life Review: Empathetic Component Statistical Frequency

**Target**: `[NDE]`  
**Status**: RESOLVED  
**Date Added**: 2025-12-27  
**Date Resolved**: 2025-12-29  
**Priority**: HIGH  
**Related Nodes**: CONSC-003, CONSC-017, CROSS-003

**Context**:
Life review is treated as core NDE component and evidence for post-materialist framework. The empathetic component (feeling impact of actions from others' perspectives) would demonstrate moral/consciousness dimension that dying brain models cannot explain. Need frequency data.

**Research Question**:
What percentage of NDEs include a life review component?
1. Of those with life review, what percentage report empathetic component (experiencing events from others' emotional perspectives) vs. purely observational memory replay?
2. How does life review frequency vary by: cultural background, religious affiliation, age at NDE, cause (cardiac arrest vs. trauma vs. other)?
3. Is there correlation between empathetic life reviews and subsequent life transformation (increased empathy, prosocial behavior)?
4. Cross-cultural consistency: Do all cultures report similar empathetic life review, or is this Western Christian phenomenon?
5. Neurological challenge: Can dying brain models explain why experiencers report feeling others' emotions during memory replay?

**RESOLUTION** (from `nde-analysis/docs/reports/conceptual_framework_deep_dive_report.md` and `threefold-path-validation-report.md`):

**Life Review Frequency (n=6,739):**
- **Life Review Occurrence: 18.6%** (1,253 cases: 546 extensive, 707 brief)

**Empathetic Component:**
| Category | Among Life Reviews | Of Total Sample |
|----------|-------------------|-----------------|
| Yes explicit | 241 (19.2%) | — |
| Implied | 81 (6.5%) | — |
| No | 845 (67.4%) | — |
| Not mentioned | 86 (6.9%) | — |
| **Total Empathetic** | **25.7%** | **4.9%** |

**Interpretation:**
- Life review is LESS common than expected (18.6% vs. common assumption of 40%+)
- **Empathetic component: 25.7%** of those with life reviews (~322 cases)
- This is BELOW the 40% threshold that would strongly validate the claim
- However, the absence of empathetic experience in 67.4% may reflect reporting limitations, not absence of phenomenon
- **Critical nuance**: 84.8% experienced no external condemnation, 45% mixed emotions, 26.8% love
- The emotional quality of life review (loving, non-judgmental) is MORE consistent than empathetic component

**Framework Implications:**
- Life review as "core" NDE component requires qualification (only 18.6%)
- Empathetic component exists but is minority experience (25.7%)
- The non-judgmental nature of life review (84.8% no condemnation) is better documented than empathetic perspective-taking

**Source**: `nde-analysis/docs/reports/conceptual_framework_deep_dive_report.md` and `threefold-path-validation-report.md` (December 13, 2025)

---

### [GDR] Historical Pattern Detection: Influx Events and Consciousness Breakthroughs

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: HIGH  
**Related Nodes**: CONSC-001, SWED-002, SWED-004, CROSS-004

**Context**:
If unified loving consciousness influences history through "divine influx," there should be identifiable historical moments when consciousness-related breakthroughs cluster: Ancient Word → Hebrew Prophets → Christ → Swedenborg. Can we detect measurable patterns distinguishing these from random cultural innovation?

**Research Question**:
Can we identify historical "influx events" where consciousness-related breakthroughs cluster? Investigate:
1. Timeline analysis: Do universalist/compassion-oriented religious innovations cluster in specific periods vs. distribute randomly?
2. Geographic patterns: Do societies with stronger correspondence-based cognition (symbolic thinking linking nature to spirit) show different cultural trajectories than purely rational/materialist ones?
3. Correlation studies: Is there measurable relationship between collective spiritual development (compassion ethics, non-violence) and cultural flourishing (stability, innovation, longevity)?
4. Resistance patterns: Can we detect consistent "proprium/self-love" opposition that resists loving consciousness influence (empire-building, slavery, hierarchical oppression)?
5. Cross-cultural convergence: Do independent cultures develop similar ethical breakthroughs (Golden Rule equivalents) suggesting common conscious influence vs. independent evolution?

**Expected Output**:
If breakthroughs cluster non-randomly and show cross-cultural convergence toward compassion ethics, supports conscious influence hypothesis. If random or explainable by diffusion/natural selection, challenges CDE premise.

**Notes**:
This tests whether "fingerprints of unified loving consciousness" are detectable in history. Framework claims influx operates throughout time—must be testable. See Swedenborg Divine Providence, SWED-002.

---

### [GDR] Narrative Evolution: Unity→Fragmentation Pattern Detection

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: HIGH  
**Related Nodes**: MYTH-002, MYTH-015, CONSC-001

**Context**:
Framework claims myths consistently evolve from unity→fragmentation across independent cultures (Ancient Word degradation). This would be measurable signature of conscious influence. Need cross-cultural statistical analysis to test pattern validity.

**Research Question**:
Do myths consistently evolve from unity→fragmentation as framework claims? Analyze:
1. Proto-myth reconstruction: Can we identify common mythic elements (primordial unity, creation patterns) that diverge into opposing trajectories across cultures?
2. Trajectory A (Unity): Do myths emphasizing monotheism, compassion, interconnectedness show measurable "coherence" compared to...
3. Trajectory B (Fragmentation): Myths emphasizing polytheistic conflict, hierarchical oppression, cosmic alienation?
4. Independent evolution test: Do cultures with NO historical contact show same unity→fragmentation pattern, or is this limited to ANE/Mediterranean sphere?
5. Statistical signatures: Can we measure "coherence loss" in religious traditions over time (tracking doctrine splits, schisms, competing interpretations)?
6. Counter-examples: Are there myths that evolve from fragmentation→unity, contradicting framework's directional claim?

**Expected Output**:
If unity→fragmentation pattern exists cross-culturally with statistical significance, supports conscious influence degradation model. If pattern is ANE-specific or bidirectional, challenges framework's universal claim.

**Notes**:
Core CDE prediction—myths should show measurable trajectory based on ruling love orientation. See MYTH-002 (Heart of Division vs. Unity), MYTH-015 (Genesis/Enuma Elish). Must distinguish pattern-finding from confirmation bias.

---

### [GDR] Proto-Myth Signatures: Conscious Source vs. Convergent Evolution

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: MEDIUM  
**Related Nodes**: MYTH-002, SWED-004, MYTH-008

**Context**:
Framework proposes proto-myths sharing "Ancient Word" origins show statistical signatures of common conscious source vs. convergent evolution from universal human cognition. Need methodology to distinguish.

**Research Question**:
Do proto-myths sharing Ancient Word origins show measurable signatures of common source vs. convergent evolution? Investigate:
1. Linguistic methodology: Can comparative mythology use methods similar to proto-Indo-European reconstruction to trace mythic relationships?
2. Signature analysis: What would distinguish myths sharing a conscious source (Ancient Word) vs. arising independently from universal cognitive patterns (Jung's archetypes, CSR findings)?
3. Structural vs. content similarity: Do shared mythic structures (flood, creation, fall) indicate common origin or cognitive universals?
4. Distribution patterns: If Ancient Word existed, should we expect regional clustering vs. global distribution of similar myths?
5. Test case: Flood narratives (Gilgamesh, Atrahasis, Genesis, Hindu Matsya, Aztec)—common memory of event, conscious transmission, or convergent response to local flooding?
6. Falsification: What evidence would prove myths arose independently rather than from common Ancient Word?

**Expected Output**:
Methodology for distinguishing conscious transmission vs. convergent evolution. If no distinguishing criteria exist, Ancient Word claim remains unfalsifiable theological interpretation.

**Notes**:
Ancient Word hypothesis (SWED-004) is central to framework but potentially unfalsifiable. Need honest assessment of whether this can be tested empirically or must remain faith claim. See MYTH-003, MYTH-008.

---

### [NDE] Veridical Perception: AWARE Study Systematic Review

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: CRITICAL  
**Related Nodes**: CONSC-004, CONSC-017

**Context**:
Framework cites veridical perception during cardiac arrest as strongest evidence consciousness operates independently of brain. Must report overall success/failure rates in controlled studies, not just remarkable anecdotes. AWARE/AWARE II provide systematic data.

**Research Question**:
In the AWARE study (Parnia 2014) and AWARE II:
1. Total numbers: (a) cardiac arrests studied, (b) survivors reporting awareness during arrest, (c) survivors who could have seen hidden targets, (d) verified accurate perceptions of targets?
2. What were methodological critiques of these studies, and how did researchers respond?
3. What is the statistical significance of any positive results?
4. What do neuroscientists consider strongest alternative explanations for verified perceptions (information leakage, prior knowledge, lucky guesses, anesthesia awareness)?
5. Have any veridical perception claims been independently replicated in controlled hospital settings?
6. What percentage of NDErs report veridical perception outside controlled studies, and what are verification challenges?

**Expected Output**:
This is framework's empirical linchpin. If verification rates are statistically significant under controlled conditions, dramatically strengthens post-materialist case. If near-zero despite large sample, framework must engage why consciousness independence doesn't manifest when properly controlled.

**Notes**:
Framework MUST present full statistical context—success AND failure rates. Cherry-picked anecdotes insufficient for scientific claim. See CONSC_Domain_Validation_Report Section 3.1, critical analysis Section 7A.

---

### [GDR] Love-Oriented vs. Self-Oriented Traditions: Narrative Stability Measurement

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: MEDIUM  
**Related Nodes**: CONSC-001, CROSS-003, MYTH-002

**Context**:
CDE predicts measurable difference in narrative stability between love-oriented (neighbor-focused) traditions vs. self-oriented (power-focused) traditions. Love should produce coherence; self-orientation should produce fragmentation. Can we measure this?

**Research Question**:
Is there measurable difference in narrative/doctrinal stability between love-oriented vs. self-oriented religious/philosophical traditions? Analyze:
1. Coherence metrics: Can we quantify doctrinal stability (fewer schisms, consistent core ethics) vs. fragmentation (competing interpretations, sectarian divisions)?
2. Longitudinal tracking: Do traditions emphasizing universal compassion (Buddhism, Franciscanism, Quakers) show greater doctrinal continuity than traditions emphasizing hierarchy/power (imperial Christianity, militant Islam)?
3. Corruption resistance: Do love-oriented movements maintain ethical core despite institutional corruption better than power-oriented movements?
4. Innovation patterns: When traditions splinter, do love-oriented splits produce complementary expressions vs. self-oriented splits producing antagonistic factions?
5. Historical longevity: Correlation between love-ethics centrality and tradition survival/influence over time?
6. Falsification test: What would constitute evidence that love/self-orientation does NOT predict narrative stability?

**Expected Output**:
If love-oriented traditions show measurably greater coherence and stability, supports CDE's ruling love polarity mechanism. If no difference or opposite pattern, challenges framework's core prediction.

**Notes**:
This tests CDE's specific prediction: ruling love (love vs. self) acts as selective pressure on memetic evolution. Must be measurable to be meaningful. See CROSS-003, framework synthesis documents on ruling love.

---

### [GDR/NLM] Swedenborgian Predictive Power: Influx and NDE Phenomenology

**Target**: `[GDR]` `[NLM]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: HIGH  
**Related Nodes**: SWED-002, SWED-003, CONSC-004

**Context**:
Framework claims Swedenborg's 18th-century "influx" doctrine and post-mortem cosmology predict NDE phenomenology before NDE research existed (1970s). If true, remarkable validation. Need specific comparison.

**Research Question**:
Does Swedenborg's influx doctrine predict NDE phenomenology discovered 200+ years later? Compare:
1. Swedenborg's "World of Spirits" description (Heaven and Hell §§ 421-535) to NDE "otherworldly realm" phenomenology—specific matches?
2. Swedenborg's "life review" as ruling love revelation vs. NDE empathetic life review—same mechanism?
3. Swedenborg's post-mortem "sorting" by internal state vs. NDE "self-judgment" reports—predictive accuracy?
4. Swedenborgian "Divine Human" encounter descriptions vs. NDE "Being of Light" personality profile?
5. Temporal sequence: Can we verify Swedenborg described these BEFORE any documented NDE reports?
6. Specificity test: Are Swedenborg's descriptions specific enough to constitute genuine prediction vs. vague compatibility?

**Expected Output**:
If Swedenborg's descriptions specifically predict later NDE findings, extraordinary validation for framework. If descriptions are post-hoc compatible but not genuinely predictive, weakens theological foundation.

**Notes**:
This is crucial epistemological test. Genuine prediction (before discovery) vs. ret roactive compatibility (after discovery) is critical distinction. Swedenborg wrote 1740s-1770s; systematic NDE research began 1970s (Moody, Ring). See SWED-003, CONSC-004.

---

### [GDR] Ruling Love Polarity: Moral Psychology Validation

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: MEDIUM  
**Related Nodes**: CROSS-003, SWED-008, CONSC-007

**Context**:
Framework's ruling love binary (self-love vs. neighbor-love) needs validation against contemporary moral psychology. Does human motivation research support this polarity, or is it oversimplified?

**Research Question**:
How does Swedenborgian "ruling love" binary relate to contemporary moral psychology? Investigate:
1. Kohlberg's moral development stages (progression from self-interest to principled ethics)—compatible with ruling love or contradictory?
2. Haidt's Moral Foundations Theory (multiple independent values: care, fairness, loyalty, authority, sanctity, liberty)—can these map to binary polarity or does multiplicity refute reductive model?
3. Developmental psychology: Do people shift moral orientations over lifespan? If yes, what does this mean for "ruling love" as allegedly fixed pole?
4. Regeneration doctrine: If Swedenborg's "regeneration" allows ruling love to change, is binary about current state vs. ultimate trajectory?
5. Mixed motivations: Can framework distinguish temporary self-interest (biological drives, survival) from proprium (spiritual self-glorification)?
6. Cross-cultural validation: Is self/other-orientation binary universal across cultures or Western construct?

**Expected Output**:
Framework must show ruling love model handles real human psychological complexity. If cannot, model is oversimplified theological construct useful for interpretation but not descriptively accurate.

**Notes**:
Critical analysis Section 3 identifies ruling love polarity as potentially reductive. Framework can survive this challenge but needs nuancing. See CROSS-003 caveats, SWED-008 on regeneration allowing change.

---

### [GDR] Proprium Resistance Patterns: Historical Correlation Studies

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: MEDIUM  
**Related Nodes**: SWED-005, GNOS-001, EARLY-003

**Context**:
CDE predicts consistent "proprium/self-love" patterns that resist loving consciousness influence throughout history. Can we identify measurable historical signatures of this resistance?

**Research Question**:
Can we detect "proprium resistance patterns" that consistently oppose loving consciousness influence? Analyze:
1. Empire-building cycles: Do imperial expansions correlate with periods of declining compassion ethics and increasing hierarchical control?
2. Institutional corruption: When religious/spiritual movements gain power, is there measurable shift from love-focused to self-preservation focused messaging?
3. Gnostic emergence: Do gnostic movements (emphasizing elite knowledge, material rejection, self-divinity) consistently arise in response to institutional Christianity's power consolidation?
4. Slavery and oppression: Can we track correlation between self-oriented theology (chosen people, divine right, racial superiority) and oppressive social structures?
5. Counter-movements: Do kenotic movements (Desert Fathers, Franciscans, Quakers, Anabaptists) consistently emerge as responses to proprium-captured institutions?
6. Statistical patterns: Frequency, duration, and outcomes of love-oriented vs. power-oriented movements over 2000-year period?

**Expected Output**:
If proprium resistance shows consistent, measurable patterns correlating with institutional power and opposing compassion movements, validates framework's mechanism. If patterns are random or absent, challenges structural claim.

**Notes**:
Tests whether "proprium" is real historical force or theological projection onto human power dynamics. Must be falsifiable. See SWED-005, GNOS-001, EARLY-003, "Work of Divine Influx" document.

---

### [NDE] Intermission Memories: DOPS vs. NDE Phenomenological Convergence

**Target**: `[NDE]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: MEDIUM  
**Related Nodes**: CONSC-002, CONSC-004, CONSC-014

**Context**:
Framework identifies parallel features between children's "intermission memories" (DOPS research—memories between past life and current incarnation) and NDEs as convergent evidence for post-mortem phenomenology. Need statistical comparison to test convergence claim.

**Research Question**:
Do DOPS intermission memories and NDE phenomenology show genuine convergence? Compare:
1. Structural sequence: Do intermission memories follow same phase pattern as NDEs (separation → transit → realm → return)?
2. Phenomenological features: What percentage of DOPS intermission cases include: (a) light/radiant realm, (b) deceased relatives encountered, (c) life planning/mission selection, (d) choice to return vs. being sent back, (e) reluctance to incarnate?
3. Unique elements: Do intermission memories include features NOT common in NDEs (memory erasure, incarnation reluctance, mission assignment)?
4. Statistical correlation: Do children with intermission memories have higher rate of later NDEs, suggesting same souls?
5. Cross-validation: Can we identify specific children who report BOTH past-life memories AND subsequent NDE, describing same cosmology?
6. Content vs. structure: Is convergence limited to abstract structure, or do specific phenomenological details match?

**Expected Output**:
Strong convergence (>60% feature overlap) validates framework's integrated post-mortem model. Significant divergence suggests separate phenomenology requiring different explanations. Structural match + content divergence supports universal structure with culturally-conditioned content.

**Notes**:
CONSC-002 and CONSC-004 connections claim parallelism. Need quantitative comparison, not impressionistic similarity. See CONSC_Domain_Validation_Report Section 3.1, Volunteer Soul Incarnation Profile Building.md.

---

### [NLM] Swedenborg's Doctrine Evolution: Internal Consistency Analysis

**Target**: `[NLM]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: MEDIUM  
**Related Nodes**: SWED-001, SWED-004, CROSS-001

**Context**:
Framework applies HCM to Bible (identifying sources, redactions, evolution) but not to Swedenborg. For epistemological consistency, need scholarly analysis of development across Swedenborg's theological corpus (1749-1771).

**Research Question**:
How do Swedenborg's core doctrines evolve from Arcana Coelestia (1749-1756) through Heaven and Hell (1758) to Divine Love and Wisdom (1763) and True Christian Religion (1771)? Specifically:
1. Correspondences doctrine: Any shifts in methodology or specific interpretation across works?
2. Ancient Word claim: Does treatment become more or less literal about Genesis 1-11 as "made-up history"?
3. Ruling love doctrine: Development or refinement of amor regnans concept over time?
4. Post-mortem cosmology: Consistent description of World of Spirits, or evolution in detail?
5. Contradictions or revisions: Where does he change or refine earlier positions?
6. Contextual influences: Can we identify 18th-century intellectual currents (pietism, rationalism, Neoplatonism) affecting his development?

**Expected Output**:
Shows intellectual honesty—framework applies critical methods to ALL texts. May reveal development suggesting Swedenborg refined theology over time (normal for any thinker). Demonstrates methodological consistency.

**Notes**:
Sensitive but necessary for epistemological integrity. See critical analysis Action 1.3 and framework improvement plan. NotebookLM limit requires focused, concise query—may need multiple queries for different doctrines.

---

## REFORMULATION SUMMARY (2025-12-27)

### Critical Correction: CDE Properly Positioned as Core Framework Mechanism

**Previous Mischaracterization**: CDE (Consciousness-Driven Evolution) was incorrectly treated as a side theory competing with standard memetics/cultural evolution models (Dual Inheritance Theory, Cultural Group Selection).

**Actual Status**: **CDE IS THE CORE MECHANISM** of the entire framework.

### The CDE Hypothesis Restated

**Premise**: NDE research demonstrates contact with a single, all-encompassing, loving consciousness (consistent across cultures, backgrounds, beliefs).

**Core Claim**: If this unified loving consciousness exists and is real, its influence should be:
- **Visible** in historical patterns (influx events, consciousness breakthroughs clustering)
- **Measurable** in narrative evolution (unity→fragmentation trajectories)
- **Consistent** across cultures and time periods (cross-cultural ethical convergence)
- **Directional** toward coherence, love, unity (distinguishable from random drift)

**What We're Testing**: Not "does CDE compete with other theories?" but "can we detect the fingerprints of a unified loving consciousness throughout human history?"

### Research Questions Added/Reformulated

#### Foundation Questions (Establishing NDE Basis)
1. **NDE Consistency Across Cultures** - Does loving consciousness appear consistently regardless of background?
2. **Distressing NDEs and Ruling Love** - Do negative experiences validate Swedenborgian polarity prediction?
3. **Life Review Empathetic Component** - Statistical frequency of the mechanism framework emphasizes
4. **Veridical Perception Systematic Review** - Controlled study results, not cherry-picked anecdotes

#### Pattern Questions (Detecting Historical Influence)
5. **Historical Influx Events** - Can we identify consciousness breakthrough clustering?
6. **Narrative Unity→Fragmentation** - Do myths show measurable CDE-predicted trajectories?
7. **Proto-Myth Signatures** - Common source vs. convergent evolution methodology
8. **Love vs. Self-Oriented Traditions** - Measurable stability differences validating ruling love polarity?
9. **Proprium Resistance Patterns** - Consistent historical signatures of self-love opposition?

#### Measurement Questions (How to Test This Rigorously)
10. **CDE Core Validation Methodologies** - How do we distinguish conscious influence from emergent patterns?
11. **Swedenborgian Predictive Power** - Did Swedenborg predict NDE findings 200 years early?
12. **Ruling Love and Moral Psychology** - Does binary model align with contemporary research?
13. **Intermission Memory Convergence** - Do DOPS and NDE phenomenology genuinely overlap?

#### Integration Questions (Cross-Domain Validation)
14. **Swedenborg Doctrine Evolution** - Applying HCM consistently to ALL texts

### Priority Classification

**CRITICAL** (Framework Foundation):
- CDE Core Validation Methodologies
- NDE Consistency Across Cultures
- Veridical Perception Systematic Review

**HIGH** (Core Mechanism Validation):
- Historical Influx Events
- Narrative Unity→Fragmentation Detection
- Distressing NDEs and Ruling Love
- Life Review Empathetic Component
- Swedenborgian Predictive Power

**MEDIUM** (Refinement and Nuancing):
- All remaining questions

### Key Distinctions from Previous Formulation

| Previous Framing | Corrected Framing |
|------------------|-------------------|
| "CDE vs. Dual Inheritance Theory" | "CDE as mechanism BEHIND memetic selective pressures" |
| "Does CDE add unique explanatory power?" | "Can we detect unified consciousness influence?" |
| "Competing hypothesis comparison" | "Testing for measurable fingerprints of conscious causation" |
| Side theory | **Core framework mechanism** |

### Methodological Notes

1. **Falsifiability**: Each question includes "what would disprove this?" criteria
2. **Statistical rigor**: Emphasizes quantitative data over anecdotal evidence
3. **Cross-cultural validation**: Tests whether patterns are universal or culturally-specific
4. **Temporal analysis**: Checks for historical clustering vs. random distribution
5. **Convergent validation**: Multiple independent lines of evidence

### Research Pipeline Status

- **Open**: 14 new/reformulated questions
- **In Progress**: 0 (awaiting external research execution)
- **Resolved**: 0 (pending research completion)

These questions are formatted for execution with appropriate external research tools (NDE Statistical Repository, Gemini Deep Research, NotebookLM) as specified in individual question blocks.

---

### [GDR] Oral Tradition Stability Research

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27

**Context**:
Framework cites Aboriginal songlines preserving "14,000-year narratives" as evidence oral traditions could preserve Ancient Word. Critical analysis notes: geographic features dating to post-glacial period ≠ narrative content remaining unchanged. Need linguistic/anthropological research on oral tradition drift.

**Research Question**:
What is the scholarly consensus on stability vs. drift in oral traditions over millennia? Specifically:
1. Jack Goody's work on oral vs. literate cultures
2. Studies of transmission fidelity in non-literate societies
3. Difference between preserving geographic/ecological information vs. narrative content
4. Documented cases of oral tradition modification over generations
5. Australian Aboriginal songline research: what's verified vs. romanticized?

Can oral traditions preserve *specific narrative content* accurately over 10,000+ years, or do they exhibit significant drift and innovation while maintaining thematic continuity?

**Notes**:
Framework needs this to support Ancient Word hypothesis. If oral traditions show substantial drift, claim that Ancient Word could persist accurately through oral transmission weakens. See `critical_analysis_report.md` Section 4B.

---

### [NLM] Swedenborg's Cultural Context

**Target**: `[NLM]`  
**Status**: Open  
**Date Added**: 2025-12-27

**Context**:
Framework applies historical-critical method to Bible but not to Swedenborg's writings. Critical analysis recommends either applying HCM consistently or acknowledging asymmetry. If applying HCM to Swedenborg, need analysis of cultural/intellectual influences.

**Research Question**:
What 18th-century intellectual currents influenced Swedenborg's theological system? How do his doctrines relate to:
1. Swedish Lutheran pietism and mysticism
2. Cartesian dualism (mind-body separation)
3. Neoplatonic emanation theories
4. Kabbalistic traditions (his knowledge of Jewish mysticism)
5. Paracelsus and Jakob Boehme (earlier Christian mystics)
6. Enlightenment rationalism (his scientific background)

To what extent are Swedenborg's "correspondences" original vs. synthesizing existing symbolic interpretation traditions? How did his theology evolve across his corpus (*Arcana Coelestia* → *True Christian Religion*)?

**Notes**:
This is **sensitive** but necessary for intellectual honesty. Can accept Swedenborg as revelatory while acknowledging cultural situatedness (as with biblical authors). See `critical_analysis_report.md` Section 1C and `framework_improvement_action_plan.md` Action 1.3.

---

### [GDR] Proto-Luke Hypothesis Scholarly Status

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27

**Context**:
Framework presents Proto-Luke (Jamesian protograph) as significant source. Critical analysis notes: hypothesis stacked on hypothesis (Markan priority → Q → L → Proto-Luke → Jamesian attribution). Knowledge graph acknowledges "hypothesis stacked on hypothesis" with low confidence. Need current scholarly assessment.

**Research Question**:
What is the current status of B.H. Streeter's Proto-Luke hypothesis (1924) in NT scholarship? Specifically:
1. How many contemporary scholars accept Proto-Luke as distinct pre-Lukan source?
2. Main arguments FOR Proto-Luke (textual evidence, coherence)
3. Main arguments AGAINST (can be explained by Lukan redaction of Mark + Q + L)
4. Relationship to Klinghardt's Marcionite hypothesis (contested minority view)
5. How does "Jamesian protograph" attribution relate to standard Proto-Luke theory?

Is there textual evidence *requiring* Proto-Luke, or can Lukan peculiarities be explained by editorial activity on standard sources?

**Notes**:
Framework relies heavily on this for Jamesian tradition reconstruction. If hypothesis is marginal in scholarship, claims should be marked speculative. See `critical_analysis_report.md` Section 14C and knowledge graph EARLY-002 caveats.

---

### [GDR] DOPS Verification Rate

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27

**Context**:
Framework emphasizes strongest DOPS cases (James Leininger, Ryan Hammons) with verified statements and birthmarks. Critical analysis asks: What's the *overall* verification rate? Cherry-picking strongest cases while ignoring weaker ones inflates evidential strength.

**Research Question**:
Of the 2,500+ cases documented by UVA DOPS:
1. What percentage have *any* verified statements?
2. What percentage have *multiple* verified statements?
3. What percentage have physical correspondences (birthmarks to wounds)?
4. What percentage lack verification (no documentation found)?
5. How do researchers handle cases where verification attempts fail?

What are the methodological critiques of DOPS research (information leakage, cryptomnesia, selective reporting)? How strong are Tucker's responses to these critiques?

**Notes**:
Framework should report both successes and failures. If verification rate is low (even 10-20% would be remarkable), that context matters for assessing evidential strength. See `critical_analysis_report.md` Section 14C.

---

### [NLM] Paul's Self-Abasement Passages

**Target**: `[NLM]`  
**Status**: ✅ RESOLVED  
**Date Added**: 2025-12-27  
**Date Resolved**: 2025-12-29  
**Resolution Document**: `data/05_Gnostic_Analysis/The Paradox of the Pneumatic Ego.md`

**Context**:
Framework characterizes Paul as exhibiting "proprium" (self-love) based on confrontational passages and authority claims. Critical analysis notes: Paul also has extensive self-abasement language (servant, slave, least of apostles, weakness boasting in 2 Corinthians). Need balanced assessment.

**Research Question**:
How do Pauline scholars interpret passages where Paul describes himself with extreme humility? Examples:
1. "Slave of Christ" (δοῦλος Χριστοῦ)
2. "Least of the apostles" (1 Cor 15:9)
3. Weakness boasting (2 Cor 11-12)
4. Suffering catalogues (2 Cor 6:4-10)

Do scholars see these as:
- Authentic humility (Paul's genuine self-perception)
- Rhetorical strategy (establishing authority paradoxically)
- Mixed: Sincere humility alongside prophetic zeal

How does this complicate framework's "proprium" diagnosis?

**RESOLUTION SUMMARY**:
The "Paradox of the Pneumatic Ego" document provides exhaustive forensic analysis concluding that Paul's humility is **BOTH authentic AND rhetorical**—and this synthesis actually **CONFIRMS** rather than refutes the proprium diagnosis:

1. **"Slave of Christ" (*doulos*)**: Scholars (Dale Martin et al.) recognize "derivative authority" mechanism—slave of cosmic Lord = plenipotentiary above human accountability
2. **"Least of the apostles"**: Functions as "Theology of Immunity"—by confessing worst sin, Paul places himself beyond human judgment and establishes "Sole Revelator" status
3. **Weakness boasting**: "Paradox of Power"—embracing weakness makes Paul rhetorically invulnerable and claims he is the clearest divine channel
4. **Suffering catalogues**: "Credentials of authenticity" validating independent mission without Jerusalem authorization

**Key Finding**: The dichotomy "authentic vs. rhetorical" is FALSE. Paul exhibits "**Proprium of the Spirit**"—not worldly vanity but absolute confidence in private revelation superseding external authority. His humility is the hammer that breaks historical "vessels" to release pneumatic "spirit."

**Graph Update**: New node GNOS-013 created to capture this synthesis.

---

<!-- 
TEMPLATE:

---

### [Domain] Question Title

**Target**: `[NLM]` / `[GDR]` / `[NDE]`  
**Status**: Open / In Progress / Resolved  
**Date Added**: YYYY-MM-DD

**Context**:
[Brief background providing necessary context for the research tool. For NotebookLM, keep under 500 characters. For Gemini Deep Research, include fuller detail.]

**Research Question**:
[Clear, specific question or hypothesis to investigate]

**Notes**:
[Any additional context, related sources, or preliminary findings]

-->

---

## DOMAIN 1: CONSCIOUSNESS STUDIES — EMPIRICAL VALIDATION GAPS

---

### [NDE] DOPS 70% Violent Death Statistic Verification

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: CRITICAL  
**Related Nodes**: CONSC-002, CONSC-005

**Context**:
Framework claims "over 70% of cases studied worldwide" in DOPS research involve violent/unnatural deaths (previous personality died by murder, accident, combat). This statistic is used as evidence for "Restorative Incarnation" mechanism—traumatic death requires second chance to complete development. However, the statistic appears in multiple documents without specific citation to Stevenson or Tucker publication.

**Research Question**:
1. What is the actual percentage of violent/unnatural deaths in Stevenson's and Tucker's published DOPS case collections? Is 70% accurate?
2. In which specific publication(s) does this statistic appear?
3. Is this percentage statistically significant compared to:
   - Historical baseline violent death rates in regions/time periods of previous personalities
   - Expected violent death rates for demographic (young adults) overrepresented in cases
4. Could selection bias explain correlation? (Violent deaths more traumatic/memorable → more likely to carry over memories → more likely to be reported and investigated)
5. How do DOPS researchers interpret this correlation—do they endorse "restorative" interpretation or offer alternative explanations?

**Expected Impact**:
This statistic is foundational to framework's hybrid post-mortem model (Tier 2a: Restorative Incarnation). If statistic is unverified, inflated, or attributable to selection bias, entire interpretive structure requires revision.

**Notes**:
Treated as established fact throughout framework (CONSC-002, CONSC-005, synthesis documents). Requires immediate verification. See CONSC_Domain_Validation_Report Section 1.5.

---

### [NDE] Life Review Frequency and Phenomenology

**Target**: `[NDE]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: CONSC-003, CROSS-003

**Context**:
Framework treats life review as core NDE component and critical evidence for post-materialist framework. Life review's empathetic component (feeling impact of actions from others' perspectives) would demonstrate moral/consciousness dimension that dying brain models cannot easily explain. However, no frequency data provided—framework describes phenomenology without statistical support.

**Research Question**:
1. What percentage of NDEs in NDERF/IANDS database include a life review component?
2. Of those with life review, what percentage report empathetic component (experiencing events from others' emotional perspectives) vs. purely observational memory replay?
3. How does life review frequency vary by:
   - Cultural background
   - Religious affiliation
   - Age at NDE
   - Cause (cardiac arrest vs. other)
4. Is there correlation between empathetic life reviews and subsequent life transformation?
5. Are there cultural variations in this feature?

**Expected Impact**:
High empathetic component frequency would strengthen framework's ruling love revelation claim. If life review is rare component, or if empathetic aspect is uncommon, framework interpretation requires significant revision.

**Notes**:
CONSC-003 currently validated with high confidence but lacks statistical support. See CONSC_Domain_Validation_Report Section 1.3.

---

### [NDE] Being of Light Cross-Cultural Identification Patterns

**Target**: `[NDE]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: CONSC-004

**Context**:
Framework claims NDErs identify "Being of Light" as Jesus based on personality match, even atheists/non-Christians. Critical analysis challenges this: selection bias (most NDERF/IANDS studies from Christian-majority cultures) and expectation effects. Need cross-cultural statistical data to test whether identification is culturally conditioned or transcends religious background.

**Research Question**:
In NDEs from Hindu-majority, Buddhist-majority, Islamic-majority, and Indigenous populations, what percentage of experiencers identify the "Being of Light" encountered as:
1. Jesus Christ
2. Deities from their cultural tradition (Krishna, Yamaraj, Vishnu, Buddha, Muhammad, ancestors)
3. Generic "deceased relatives" or unnamed beings
4. No being encountered

Does personality-based identification transcend cultural conditioning, or do experiencers interpret the encounter through pre-existing religious frameworks? What percentage of atheist/agnostic NDErs identify the being as Jesus?

**Expected Impact**:
If Hindu NDErs predominantly report Hindu deities rather than Jesus, framework's "pure identification" claim requires major revision toward cultural conditioning explanation. If Jesus appears cross-culturally, remarkable evidence for framework.

**Notes**:
Already in research question log. Critical for framework's NDE interpretation. See CONSC_Domain_Validation_Report Section 1.4 and 2.2.

---

### [NDE] Tunnel and Light Frequency Statistics

**Target**: `[NDE]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: CONSC-004

**Context**:
Framework describes tunnel/darkness-to-light transition as "one of the most widely reported and iconic elements" of NDEs. Source document (`Researching Near-Death Experiences.md`) provides detailed phenomenological description but no statistical frequency data. Need quantification to support "widely reported" claim.

**Research Question**:
1. What percentage of NDEs include tunnel or void transit experience?
2. What percentage include movement toward/immersion in light?
3. How do these frequencies vary by:
   - Cultural background
   - Religious affiliation
   - Cause of NDE (cardiac arrest, trauma, illness, childbirth)
   - Age of experiencer
4. What percentage of NDEs lack these structural elements entirely?

**Expected Impact**:
Determines whether "iconic element" claim is statistically accurate or based on memorable anecdotes. If frequency is lower than framework implies, descriptive language requires adjustment.

**Notes**:
See CONSC_Domain_Validation_Report Section 3.1. Framework documents use qualitative language ("widely reported," "commonly") without quantification.

---

### [NDE] Distressing NDE Frequency and Typology

**Target**: `[NDE]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: CONSC-004, SWED-003

**Context**:
Framework emphasizes blissful NDEs with beings of light. Distressing/hellish NDEs documented in `Researching Near-Death Experiences.md` (Type 1: Inverse Experience, Type 2: Void, Type 3: Hellish Realm) but no frequency data. Swedenborg's cosmology predicts post-mortem experiences reflect ruling love—self-centered souls should experience initial distress. Need statistical validation.

**Research Question**:
1. What percentage of documented NDEs are classified as distressing, frightening, or hellish?
2. What are relative frequencies of three distressing types (Inverse, Void, Hellish Realm)?
3. What demographic/psychological profiles correlate with distressing vs. pleasant NDEs?
4. Do experiencers report subsequent life changes similar to positive NDEs, or different trajectories?
5. Are there cultural/religious variations in distressing NDE frequency?
6. Do distressing NDEs transition to positive experiences (as in Howard Storm case), and if so, what percentage?

**Expected Impact**:
Could validate Swedenborgian prediction that ruling love determines initial post-mortem experience. If distressing NDEs are very rare (<5%), framework must address why cosmology doesn't match empirical patterns. If common (>20%), framework should integrate more prominently.

**Notes**:
Critical analysis identified cherry-picking concern—framework emphasizes confirming cases. Must address full phenomenological range. See CONSC_Domain_Validation_Report Section 2.2.

---

### [NDE] Veridical Perception: AWARE Study Results and Verification Rates

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: CRITICAL  
**Related Nodes**: CONSC-004

**Context**:
Framework cites veridical perception during cardiac arrest as strongest evidence consciousness operates independently of brain. Critical analysis notes framework must report overall success/failure rates in controlled studies, not just remarkable anecdotes. AWARE study (Parnia 2014) and AWARE II had thousands of cardiac arrests with hidden targets designed to test claims.

**Research Question**:
In the AWARE study and follow-up AWARE II:
1. Total numbers: (a) cardiac arrests studied, (b) survivors reporting awareness during arrest, (c) survivors who could have seen hidden targets, (d) verified accurate perceptions of targets
2. What were methodological critiques of the studies?
3. How did researchers respond to critiques?
4. What do neuroscientists consider strongest alternative explanations for verified perceptions (information leakage, prior knowledge, lucky guesses, anesthesia awareness)?
5. Have any veridical perception claims been independently replicated in controlled hospital settings?
6. What is the statistical significance of positive results?

**Expected Impact**:
This is framework's empirical linchpin. If verification rates are statistically significant under controlled conditions, dramatically strengthens post-materialist case. If near-zero despite large sample, framework must engage why "consciousness independence" doesn't manifest when properly controlled.

**Notes**:
Framework must present full statistical context—success AND failure rates. Cherry-picked anecdotes insufficient for scientific claim. See CONSC_Domain_Validation_Report Section 3.1.

---

### [GDR] DOPS Case Verification: Overall Success Rates

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: CONSC-002

**Context**:
Framework emphasizes strongest DOPS cases (Leininger, Hammons) with multiple verified statements and physical correspondences. Critical analysis asks: What's overall verification rate across 2,500+ cases? Cherry-picking strongest cases while ignoring weaker ones inflates evidential strength. Tucker's methodology requires honest presentation including failures.

**Research Question**:
Of UVA DOPS 2,500+ documented cases:
1. What percentage have ANY verified statements?
2. What percentage have MULTIPLE (3+) verified statements?
3. What percentage have physical correspondences (birthmarks matching wounds)?
4. What percentage lack documentation (previous person not identified)?
5. How does DOPS handle failed verification attempts—are these published or only successful cases?
6. What are main methodological critiques (information leakage, cryptomnesia, leading questions, fraud)?
7. What are Tucker's specific responses to these critiques?
8. Have independent researchers attempted replication with similar success rates?

**Expected Impact**:
Even 10-20% verification rate would be remarkable if properly controlled. But framework must report full picture. If only handful of 2500 cases verify with strong evidence, evidential weight changes dramatically. Statistical context essential for honest assessment.

**Notes**:
Identified in critical analysis as evidence overreach. Research question log has related question; this focuses specifically on verification statistics across entire dataset. See CONSC_Domain_Validation_Report Section 1.5 and 3.2.

---

### [NDE] Intermission Memory Phenomenological Comparison

**Target**: `[NDE]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: CONSC-002, CONSC-004, CONSC-005

**Context**:
Framework identifies parallel features between children's "intermission memories" (DOPS research) and NDEs as convergent evidence for post-mortem phenomenology. `Volunteer Soul Incarnation Profile Building.md` claims these describe "the exact same event from two different temporal perspectives." Need statistical comparison to test whether features genuinely converge or framework is selectively pattern-matching.

**Research Question**:
Comparing DOPS intermission memory reports to NDE phenomenology:
1. What percentage of DOPS intermission cases include: (a) light/radiant realm, (b) deceased relatives encountered, (c) life planning/mission selection, (d) choice to return vs. being sent back, (e) reluctance to incarnate?
2. Do intermission memories include features NOT common in NDEs (memory erasure, incarnation reluctance, mission assignment)?
3. What are key differences suggesting distinct phenomena vs. overlapping cosmology?
4. Statistical correlation: Do children with intermission memories have higher rate of later NDEs?
5. Structural sequence comparison: Does intermission follow same phase pattern as NDEs (separation → transit → realm → return)?

**Expected Impact**:
Strong convergence validates framework's integrated post-mortem model. Significant divergence suggests separate phenomenology requiring different explanations. If structural sequence matches but content differs, supports "universal structure + culturally-conditioned content" interpretation.

**Notes**:
CONSC-002 and CONSC-004 connections claim parallelism. Need quantitative comparison, not impressionistic similarity. See CONSC_Domain_Validation_Report Section 3.1.

---

### [GDR] CDE vs. Dual Inheritance Theory: Critical Predictions

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: CRITICAL  
**Related Nodes**: CONSC-001, CROSS-003, CROSS-004

**Context**:
Framework proposes Consciousness-Driven Evolution (CDE) as selective pressure on memetic evolution. Critical analysis notes simpler alternatives (Boyd & Richerson's Dual Inheritance Theory, Wilson's Cultural Group Selection) may explain same phenomena without metaphysical "consciousness-as-causal-force" assumption. Framework needs to demonstrate unique explanatory/predictive power.

**Research Question**:
How do Dual Inheritance Theory and Cultural Group Selection explain cultural evolution patterns framework attributes to CDE?
1. What predictions do DIT and CGS make about when cooperative vs. competitive cultural strategies dominate?
2. How do these theories explain prosocial norm emergence without "ruling love" or consciousness-as-fundamental?
3. Do DIT/CGS treat consciousness as epiphenomenal correlate or causal driver?
4. What specific, testable predictions does CDE make that DIT/CGS cannot explain?
5. Can CDE explain any cultural trajectory that DIT/CGS cannot?
6. If framework's "ruling love polarity" is reframed as "cooperation/defection strategies," does CDE add anything beyond standard evolutionary game theory?
7. Can ANY cultural trajectory falsify CDE, or does it explain all outcomes post-hoc?

**Expected Impact**:
This is Occam's Razor test. If simpler theories explain same data, burden is on framework to show why metaphysical addition is necessary. If CDE makes unique testable predictions, it's legitimate competing hypothesis. If not, it's theological interpretation of naturalist explanations, not competing scientific theory.

**Notes**:
Already in research question log. Central epistemological issue. See CONSC_Domain_Validation_Report Section 1.1 and 4.1. Requires sophisticated analysis—use GDR extended context.

---

## DOMAIN 2: SWEDENBORGIAN THEOLOGY — SOURCE VALIDATION GAPS

### [SWED] Swedenborg's Doctrine Evolution Across Corpus

**Target**: `[NLM]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: SWED-001, SWED-004, CROSS-001

**Context**:
Framework applies HCM to Bible (identifying sources, redactions, evolution) but not to Swedenborg. Critical analysis recommends consistency. Need scholarly analysis of development across Swedenborg's theological corpus (1749-1771).

**Research Question**:
How do Swedenborg's core doctrines (correspondences, influx, ruling love, regeneration) evolve from *Arcana Coelestia* (1749-1756) through *Heaven and Hell* (1758) to *Divine Love and Wisdom* (1763) and *True Christian Religion* (1771)? Are there contradictions or revisions? How does his treatment of Ancient Word claim change? Does he become more or less literal about Genesis 1-11 as "made-up history"?

**Expected Impact**:
Shows intellectual honesty—framework applies critical methods to ALL texts. May reveal development suggesting Swedenborg refined theology over time (normal for any thinker).

**Notes**:
Sensitive but necessary for epistemological consistency. See critical analysis Action 1.3 and framework improvement plan. NotebookLM limit requires focused, specific query.

---

### [SWED] Swedenborg's 18th-Century Intellectual Context

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: SWED-001, SWED-004

**Context**:
Framework presents Swedenborg's correspondences as revelatory spiritual perception. Critical analysis notes: all thinkers are culturally situated. Understanding 18th-century influences doesn't negate spiritual authority but shows how revelation works THROUGH cultural context, not independent of it (parallel to biblical authors).

**Research Question**:
What intellectual traditions influenced Swedenborg's theological system? Analyze: (1) Swedish Lutheran pietism and mysticism in 1700s, (2) Cartesian mind-body dualism (Swedenborg was scientist), (3) Neoplatonic emanation theories available in his era, (4) What exposure did Swedenborg have to Kabbalistic traditions?, (5) How do his correspondences relate to earlier Christian mystical interpretation (Paracelsus, Boehme, medieval allegory)?, (6) Enlightenment rationalism's influence on his systematic theology approach?, (7) Were "symbolic interpretation of sacred texts" traditions already existing that Swedenborg systematized?

**Expected Impact**:
Places Swedenborg in intellectual history without diminishing revelatory status. Shows how divine influx works through cultural forms. Strengthens framework by demonstrating methodological consistency.

**Notes**:
See framework improvement plan Action 1.3, Option A. This is extended research needing full GDR context.

---

### [SWED] Independent Validation of Correspondence Claims

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: SWED-001, CROSS-001

**Context**:
Critical analysis identifies circular reasoning: "Swedenborg says Exodus = regeneration → We find regeneration in Exodus → Therefore Swedenborg validated." Framework needs independent methodology for distinguishing true correspondences from invented ones. This is unfalsifiability problem at core of framework.

**Research Question**:
Is there ANY methodology for validating correspondential interpretations that doesn't presuppose Swedenborg's authority? Investigate: (1) What criteria distinguish legitimate symbolic reading from arbitrary allegory?, (2) Historical-critical scholars identify "authorial intent" through source analysis—can this validate/challenge correspondences?, (3) Do pre-Swedenborgian Jewish/Christian allegorical traditions identify same correspondences independently?, (4) Comparative mythology: do symbolic patterns Swedenborg identifies appear cross-culturally (suggesting universal archetypes) or only in Hebrew Bible?, (5) Can correspondences make testable predictions? (e.g., "If passage X corresponds to spiritual state Y, redaction criticism should show composition in historical context matching Y")

**Expected Impact**:
If independent validation methods exist, dramatically strengthens framework. If unfalsifiable by design, framework must acknowledge this is theological hermeneutic, not empirically validated epistemology.

**Notes**:
This is THE critical epistemological question. See critical analysis Section 1 and falsifiability analysis action item. Requires sophisticated research.

---

### [SWED] Most Ancient Church: Archaeological Evidence vs. Golden Age Fallacy

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: SWED-006, SWED-004

**Context**:
Knowledge graph SWED-006 caveats note "Risk of Golden Age fallacy—archaeological evidence shows cognitive progress, not decline." Framework reinterprets Swedenborg's "Most Ancient Church" as allegory for cognitive architecture, not literal recent history. Need scholarly assessment of this move.

**Research Question**:
What does archaeological/paleoanthropological evidence show about cognitive evolution from Lower Paleolithic through Neolithic? Specifically: (1) Evidence for symbolic thought (art, burial, ornament) over time—increasing or stable?, (2) Social complexity and cooperation—becoming more sophisticated or degrading?, (3) "Golden Age" claims in history: are they universal myth reflecting nostalgia rather than fact?, (4) Swedenborg's literal claim of recent (4000-5000 BCE) Most Ancient Church in Near East—does this match or contradict archaeological record?, (5) Is framework's reinterpretation (allegorical cognitive architecture vs. literal history) defensible while still claiming Swedenborg's authority?

**Expected Impact**:
If archaeological record contradicts literal Golden Age, framework's allegorical reinterpretation is necessary but raises questions about selective literalism. If evidence ambiguous, framework has more flexibility.

**Notes**:
Knowledge graph already includes caveats. Research determines whether allegorical reading is apologetic retrofit or genuinely supported by Swedenborg's own writings.

---

## DOMAIN 3: BIBLICAL SCHOLARSHIP — METHODOLOGICAL RIGOR GAPS

### [BIBL] Gospel Embarrassment Criterion: Current Scholarly Assessment

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: BIBL-002, EARLY-003

**Context**:
Framework uses embarrassment criterion to identify authentic Jesus material vs. Pauline overlay. "Re-evaluating Gospel Embarrassment.md" exists in data. Need current scholarly status of this criterion—has it been challenged or refined?

**Research Question**:
What is current status of "criterion of embarrassment" in historical Jesus research? Specifically: (1) Do majority of scholars still consider it valid?, (2) What are main critiques (e.g., "embarrassing to whom? Later church or original community?")?, (3) How do scholars handle cases where "embarrassment" might be rhetorical strategy (e.g., humility claims establishing authority)?, (4) Examples where criterion has been challenged on specific passages?, (5) Alternative criteria that have superseded or supplemented embarrassment in contemporary scholarship?

**Expected Impact**:
If criterion remains robust, strengthens framework's Jesus-Paul divergence analysis. If widely challenged, framework must use more sophisticated methods.

**Notes**:
Data file suggests framework is aware of complexities. Research determines whether usage is defensible or needs revision.

---

### [BIBL] Lukan Redaction of Q and Proto-Luke Material

**Target**: `[NLM]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: EARLY-002, BIBL-001

**Context**:
Framework proposes Proto-Luke as Jamesian source. But Luke-Acts heavily redacts sources (removes Davidic emphasis, Hellenizes Jesus). How much original Jamesian material survived? Can we distinguish Jamesian substrate from Lukan theology?

**Research Question**:
What criteria do scholars use to distinguish Lukan redaction from pre-Lukan sources in Q and L material? Can "de-redaction" reliably recover earlier forms? What are limits of source criticism—how much uncertainty exists? Specifically for Jamesian protograph hypothesis: what textual evidence would validate vs. falsify it?

**Expected Impact**:
Determines confidence level for Proto-Luke hypothesis. If source criticism is highly uncertain, hypothesis must be marked speculative. If methods robust, framework justified in using it.

**Notes**:
Knowledge graph EARLY-002 acknowledges "hypothesis stacked on hypothesis" with low confidence. Research determines appropriate uncertainty level.

---

### [BIBL] Western Non-Interpolations: Scholarly Consensus

**Target**: `[NLM]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Low  
**Related Nodes**: BIBL-007

**Context**:
Framework references Westcott-Hort's "Western Non-Interpolations"—passages in Alexandrian manuscripts absent from Western tradition, suggesting Western deletions rather than Alexandrian additions. Need current scholarly status.

**Research Question**:
Do contemporary textual critics accept Westcott-Hort's Western Non-Interpolations category? What's the current explanation for these variants? Have NA28/UBS5 editions retained or revised W-H's judgments? Which specific passages are most debated?

**Expected Impact**:
Minor—ensures framework uses current textual scholarship rather than 19th-century assumptions.

**Notes**:
Low priority but relevant for scholarly credibility. NotebookLM query appropriate for technical detail.

---

## DOMAIN 4: EARLY CHRISTIAN HISTORY — HYPOTHESIS VALIDATION GAPS

### [EARLY] Jamesian Protograph: Textual Evidence vs. Theological Inference

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: EARLY-002, EARLY-010

**Context**:
Framework presents "Jamesian protograph" underlying Proto-Luke as significant source. Knowledge graph acknowledges "hypothesis stacked on hypothesis" (Markan priority → Q → L → Proto-Luke → Jamesian attribution) with low confidence. Critical analysis questions whether this is scholarly hypothesis or framework's theological inference.

**Research Question**:
What is the textual evidence specifically for Jamesian authorship or community of Proto-Luke material? Investigate: (1) Does mainstream NT scholarship attribute any pre-Lukan sources to James or Jerusalem church?, (2) Is "Jamesian protograph" a hypothesis in scholarly literature or framework's designation?, (3) What features (law-observance, Davidic emphasis, poor/rich polarity) actually correlate with James's theology vs. general Jewish Christianity?, (4) Could L material derive from other Jewish-Christian communities besides James's circle?, (5) How does Klinghardt's Marcionite hypothesis (contested minority view) relate to Jamesian protograph theory?, (6) What would constitute textual evidence that would falsify Jamesian attribution?

**Expected Impact**:
If "Jamesian protograph" is framework's inference rather than scholarly hypothesis, must be clearly marked as interpretive. If scholarly support exists, determines appropriate confidence level.

**Notes**:
Critical analysis Section 14C. This is crucial for framework's Jesus-Paul divergence argument. Must distinguish established from speculative.

---

### [EARLY] Desposyni Dynastic Claims: Historical Evidence

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: EARLY-007, EARLY-010

**Context**:
Framework presents Desposyni (Jesus's biological family) as dynastic leaders of early church into 4th century. Relies on Eusebius, Hegesippus, Epiphanius. Need assessment of source reliability and scholarly consensus on these claims.

**Research Question**:
What is scholarly consensus on Desposyni leadership claims? Analyze: (1) How historically reliable are Hegesippus and Epiphanius (writing 2nd-3rd centuries about 1st-century events)?, (2) Are there independent corroborations of dynastic succession beyond these sources?, (3) What evidence exists for biological descendants of Jesus leading churches outside Jerusalem?, (4) How does this interact with Davidic lineage claims—were Desposyni asserting messianic royal authority?, (5) Why would imperial church tolerate rival authority structure until Sylvester I (318 CE)—what changed?, (6) Is the 318 CE delegation story to Sylvester historically credible or legendary?

**Expected Impact**:
If Desposyni claims are contested or based on unreliable late sources, framework must mark as speculative. If scholarly support exists, strengthens Jesus-Paul divergence narrative.

**Notes**:
EARLY-007 has trace_status: partial. Need external scholarly assessment, not just patristic citations.

---

### [EARLY] Magi as Persian Priests: Zoroastrian Connection Evidence

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Low  
**Related Nodes**: EARLY-008, EARLY-009

**Context**:
Framework proposes Magi were authentic Persian Zoroastrian priests who recognized Jesus through astronomical prophecy, bringing Avestan wisdom into Christianity. Data includes "Persian Roots of Early Christianity.md" and "The Cycle of Celestial Knowledge.md". Need scholarly assessment.

**Research Question**:
What evidence supports Matthean Magi as historical Zoroastrian priests vs. Matthean literary creation? Investigate: (1) Dating of Zoroastrian texts—do they predate Christianity or are they later compilations?, (2) Specific Zoroastrian doctrines (Saoshyant savior, resurrection, final judgment) that parallel Christianity—direction of influence?, (3) Matthew's Magi narrative: scholarly consensus on historicity vs. theological symbolism?, (4) If Magi were historical, could they have been Jewish Babylonian exiles rather than Zoroastrians?, (5) What is mainstream scholarship on Persian influence on Second Temple Judaism and early Christianity?

**Expected Impact**:
If Zoroastrian-Christian connection is well-established, fascinating historical insight. If speculative or direction of influence unclear, framework must present more tentatively.

**Notes**:
Interesting but peripheral to core framework. Low priority. Data documents suggest substantial research already done—need external validation.

---

### [EARLY] Paul's Damascus Vision: Scholarly Explanations

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: EARLY-003, GNOS-003

**Context**:
Framework treats Paul's Damascus vision as genuine spiritual experience but interprets it through proprium lens (Paul's subjective construction). "Paul's Damascus Vision: Scholarly Critique.md" exists in data. Need current neurological and psychological scholarship.

**Research Question**:
What explanations do scholars offer for Paul's Damascus vision? Analyze: (1) Neurological hypotheses (temporal lobe epilepsy, photosensitive migraine, heat stroke), (2) Psychological explanations (guilt-induced hallucination, conversion psychology), (3) How do scholars distinguish "genuine religious experience" from pathological explanations?, (4) What's the relationship between Acts accounts (3 versions with contradictions) and Paul's own testimony (Gal 1, 1 Cor 9, 15)?, (5) Does framework's "subjective proprium construction" interpretation have scholarly parallels?

**Expected Impact**:
Framework doesn't need to adopt naturalist explanations, but should engage them. Shows scholarly awareness even while maintaining theological interpretation.

**Notes**:
Data file "Paul's Damascus Vision_ Scholarly Critique.md" suggests engagement already. Research confirms framework uses current scholarship.

---

## DOMAIN 5: GNOSTIC ANALYSIS — CATEGORY DEFINITION GAPS

### [GNOS] "Gnostic Impulse" Category: Historical Heterogeneity

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: GNOS-001, GNOS-004, GNOS-006

**Context**:
Critical analysis Section 8 identifies "Gnostic Impulse" as problematic category encompassing radically heterogeneous phenomena (ancient Valentinianism, SBNR spirituality, simulation hypothesis, UFO religions). Functions as polemical catch-all for positions framework opposes. Risks anachronism and essentialism.

**Research Question**:
How do scholars of Gnosticism define "gnostic" as historical movement vs. typological category? Investigate: (1) Michael Williams's critique in *Rethinking "Gnosticism"*—why he argues category is incoherent, (2) Karen King's *What is Gnosticism?*—problems with applying modern construct to ancient diversity, (3) Is "gnostic impulse" a recognized scholarly category or framework's neologism?, (4) What structural features MUST be present for something to be "gnostic" (material evil? divine spark? Demiurge? secret knowledge?)—do modern SBNR movements meet these criteria?, (5) Could framework's pattern be better described as "anti-institutionalism" or "autonomous spirituality" without gnostic baggage?

**Expected Impact**:
If scholarly consensus is moving away from "gnostic" as transhistorical category, framework needs tighter definition or different terminology. If structural parallels are robust, usage defended.

**Notes**:
Critical analysis Section 8 and Action 2.3 in improvement plan. High priority—affects large swath of framework's polemical architecture.

---

### [GNOS] Paul as Proto-Gnostic: Mainstream vs. Framework Position

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: GNOS-003, GNOS-005, EARLY-003

**Context**:
Framework identifies "gnostic substrate" in Paul (cosmic drama, flesh/spirit dualism, hidden wisdom, mysterion language). Knowledge graph GNOS-003 acknowledges this is minority view—mainstream situates Paul in Jewish apocalypticism. Critical analysis notes cherry-picking: Paul's bodily resurrection theology and creation affirmation contradict gnostic cosmology.

**Research Question**:
What is mainstream NT scholarship's position on Paul's relationship to Gnosticism? Specifically: (1) Do scholars see Paul as proto-gnostic, Jewish apocalyptic, or something else?, (2) How do scholars explain Valentinian use of Paul—influence from Paul or gnostic reading imposed on Paul?, (3) What are strongest arguments AGAINST gnostic Paul (e.g., 1 Cor 15 bodily resurrection, Romans 8 creation groaning)?, (4) How do scholars interpret Paul's "wisdom/foolishness" dichotomy—is this gnostic dualism or prophetic critique?, (5) Does Pastoral Epistles' "falsely called gnosis" (1 Tim 6:20) suggest early orthodox reading saw Paul as ANTI-gnostic?, (6) What is scholarly assessment of framework's selective emphasis on dualist passages while downplaying resurrection/creation passages?

**Expected Impact**:
If mainstream firmly rejects gnostic Paul, framework must present this as theological interpretation, not historical consensus. If debate exists, appropriate to explore but with clear uncertainty markers.

**Notes**:
Critical analysis Sections 5A and 9. Knowledge graph GNOS-003 includes caveats but framework documents may overstate case. Research determines appropriate confidence level.

---

## DOMAIN 6: MYTHOLOGICAL STUDIES — EVIDENTIAL RIGOR GAPS

### [MYTH] Oral Tradition Stability: Songlines vs. Narrative Content

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: MYTH-008, SWED-004

**Context**:
Framework cites Aboriginal songlines preserving "14,000-year narratives" as evidence oral traditions could preserve Ancient Word. Critical analysis Section 4B notes: preserving geographic/ecological information ≠ narrative content remaining unchanged. Need linguistic/anthropological research on oral tradition drift vs. stability.

**Research Question**:
What is scholarly consensus on stability vs. drift in oral traditions over millennia? Investigate: (1) Jack Goody's work on oral vs. literate cultures—how does transmission fidelity differ?, (2) Studies of oral traditions in non-literate societies (Polynesian, African, Native American)—documented drift over generations?, (3) Australian Aboriginal songlines specifically: what's preserved (geographic routes, ecological knowledge, ritual sequences) vs. what varies (narrative elaboration, mythic details)?, (4) Difference between preserving spatial/ecological information (landmark navigation) vs. preserving specific narrative content (plot, characterization, theological meaning)?, (5) Is 10,000+ year narrative stability plausible or is framework romanticizing oral tradition?, (6) How does framework's Ancient Word hypothesis differ from universal cognitive archetypes (Jung) or convergent mythmaking (natural, not influx-driven)?

**Expected Impact**:
Critical for Ancient Word hypothesis. If oral traditions show substantial narrative drift, claim of 10,000-year stable correspondence system weakens dramatically. If spatial memory differs from narrative memory, framework must distinguish claims.

**Notes**:
Already in research question log but worth expanding. This is empirical test of unfalsifiable theological claim (Ancient Word). Research determines plausibility.

---

### [MYTH] Göbekli Tepe Astronomical Interpretation: Archaeological Consensus

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: MYTH-008, SWED-004

**Context**:
Framework cites Göbekli Tepe (11,600 BP) as potential astronomical observatory encoding Younger Dryas cataclysm, supporting Ancient Word hypothesis. This comes from Martin Sweatman's work. Need scholarly assessment—is this mainstream archaeology or fringe theory?

**Research Question**:
What is archaeological consensus on Göbekli Tepe's function and symbolism? Specifically: (1) Is Martin Sweatman's astronomical interpretation (Pillar 43 as star map, Younger Dryas comet) accepted by mainstream archaeologists or considered speculative?, (2) What do excavators (Klaus Schmidt, Lee Clare) say about site's purpose?, (3) Alternative interpretations of the iconography that don't require astronomical knowledge?, (4) If astronomical, does this prove transmission of specific narrative content or just observation of celestial events?, (5) How does this compare to other Neolithic sites—is Göbekli Tepe unique or part of broader pattern?, (6) What is scholarly assessment of "lost advanced civilization" theories that use Göbekli Tepe as evidence?

**Expected Impact**:
If mainstream archaeology skeptical of astronomical interpretation, framework must present more tentatively. If accepted, strengthens Ancient Word plausibility.

**Notes**:
MYTH-008 cites this as evidence. Göbekli Tepe is often used by alternative history proponents (Graham Hancock)—framework must distinguish legitimate scholarship from fringe.

---

### [MYTH] Proto-Myth Divergence: Traceable Evidence vs. Theoretical Construct

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: MYTH-002, MYTH-005, MYTH-006

**Context**:
Framework proposes proto-myths diverged into opposing trajectories ("Heart of Division" vs. "Heart of Unity") driven by consciousness evolution. This is elegant theoretical model—but is there empirical way to trace actual historical divergence, or is this unfalsifiable interpretive framework?

**Research Question**:
How do comparative mythologists trace genetic relationships between myths? Investigate: (1) Linguistic methods for reconstructing proto-myths (parallel to proto-Indo-European language reconstruction), (2) Can we date divergences—when did Genesis creation narrative branch from Enuma Elish traditions?, (3) What is scholarly assessment of "binary divergence" model—do myths split into opposing pairs or show more complex diffusion patterns?, (4) Evidence for borrowing/influence vs. common ancestry—how do scholars distinguish?, (5) Could similar mythic patterns result from universal human cognition (cognitive science of religion) rather than historical divergence from common source?, (6) What would constitute evidence for vs. against framework's CDE-driven divergence?

**Expected Impact**:
Determines whether proto-myth analysis is empirically grounded or theologically imposed pattern. If methods exist for tracing divergence, framework on solid ground. If unfalsifiable, mark as interpretive.

**Notes**:
MYTH-002, MYTH-005 (Enuma Elish), MYTH-006 (Genesis) develop this extensively. Research determines scholarly support.

---

## DOMAIN 7: CROSS-DOMAIN & METHODOLOGICAL — FUNDAMENTAL GAPS

### [CROSS] CDE vs. Dual Inheritance Theory: Comparative Predictions

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: CONSC-001, CROSS-003

**Context**:
Critical analysis Section 2B identifies simpler alternative explanations for cultural evolution patterns: Boyd & Richerson's Dual Inheritance Theory, Wilson's Cultural Group Selection. These explain cooperation/conflict without metaphysical "consciousness as causal force." Framework needs to show CDE adds unique explanatory/predictive power vs. these simpler theories.

**Research Question**:
How do Dual Inheritance Theory and Cultural Group Selection explain cultural evolution? Specifically: (1) What predictions do Boyd & Richerson's DIT make about when cooperative vs. competitive strategies dominate?, (2) How does CGS explain prosocial norm emergence without invoking consciousness-as-fundamental?, (3) Do these theories require consciousness as causal driver or treat it as epiphenomenal correlate?, (4) What testable predictions does CDE make that DIT/CGS cannot explain?, (5) If framework's "ruling love polarity" is reframed as "cooperation/defection strategies," does CDE add anything beyond standard evolutionary game theory?, (6) Can ANY cultural trajectory falsify CDE, or does it explain all outcomes post-hoc?

**Expected Impact**:
This is Occam's Razor test. If simpler theories explain same data, burden is on framework to show why metaphysical addition is necessary. If CDE makes unique testable predictions, it's legitimate competing hypothesis. If not, it's theological interpretation of naturalist explanations.

**Notes**:
Critical analysis Section 2B and already in research question log. Central epistemological issue. Requires sophisticated analysis—use GDR extended context.

---

### [CROSS] Dying Brain Hypothesis: Strongest Current Evidence

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: CONSC-004

**Context**:
Framework interprets NDEs as evidence for post-mortem consciousness. Critical analysis Section 7A: framework doesn't adequately engage strongest neuroscientific alternatives. Must address dying brain explanations seriously, not dismissively, to maintain intellectual credibility.

**Research Question**:
What is current state of neuroscientific explanations for NDE phenomenology? Specifically: (1) Borjigin et al. (2013) findings on surge of gamma brain activity at death in rats—implications for human consciousness?, (2) DMT hypothesis (Strassman)—is endogenous DMT released at death? What's evidence?, (3) Temporal lobe models for life review (memory cascade during oxygen deprivation), (4) Visual cortex anoxia explanations for tunnel/light perception, (5) How do neuroscientists explain veridical perception cases—information leakage? Prior knowledge? Statistical artifacts?, (6) What are strongest counterarguments neuroscientists offer to "consciousness survives death" interpretation?, (7) Has anyone proposed naturalist explanation for empathetic life review component?

**Expected Impact**:
Framework strengthened by engaging best alternatives seriously. If dying brain models are weak, shows why post-materialist interpretation needed. If strong, framework must articulate why insufficient despite plausibility.

**Notes**:
Already in research question log. Critical analysis emphasizes this as intellectual honesty requirement. Framework can maintain post-materialist position while acknowledging strength of alternatives.

---

### [CROSS] Falsification Criteria for Correspondence Doctrine

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: SWED-001, CROSS-001

**Context**:
Critical analysis Section 1B: correspondence doctrine is unfalsifiable by design. Framework acknowledges this in knowledge graph but still claims "epistemological integration." Need clear answer: what would falsify Swedenborgian correspondences? If nothing, this is faith commitment, not validated knowledge.

**Research Question**:
Can correspondence doctrine be falsified? Investigate: (1) What would Swedenborg himself say constitutes false vs. true correspondence?, (2) Historical cases where correspondence interpretations were abandoned as incorrect, (3) Do different Swedenborgian scholars disagree on specific correspondences—if so, how is disagreement resolved?, (4) Could historical-critical findings ever force revision of correspondence (e.g., if source criticism shows text composite, does this affect spiritual sense?)?, (5) If answer is "correspondences cannot be falsified," how does framework defend calling this epistemology rather than hermeneutics?, (6) Is framework willing to acknowledge correspondence doctrine as faith commitment rather than validated claim?

**Expected Impact**:
Central epistemological question. If falsification criteria exist, framework on stronger ground. If admitted as unfalsifiable, requires reframing entire epistemological stance per critical analysis recommendations.

**Notes**:
THE crucial question for framework's intellectual honesty. See critical analysis Section 1, critical issues summary, falsifiability analysis action plan. This research determines whether fundamental reframing necessary.

---

### [CROSS] Historical-Critical Method Applied to Swedenborg: Feasibility

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: CROSS-001, SWED-001

**Context**:
Critical analysis Section 1C identifies methodological asymmetry: HCM applied to Bible but not Swedenborg. Framework improvement plan Action 1.3 offers two options: (A) apply HCM to Swedenborg, or (B) acknowledge asymmetry as theological stance. Need research to determine if Option A is feasible.

**Research Question**:
Has anyone attempted historical-critical analysis of Swedenborg's theological writings? Investigate: (1) Scholarly work on Swedenborg's biography, spiritual crisis (1740s), vision experiences, (2) Analysis of Swedenborg's theological development across works (evolution of doctrines), (3) Identification of Swedenborg's sources (which earlier mystics, philosophers, theologians influenced him?), (4) Psychological explanations for visions (neurological, psychiatric, genuine mystical?), (5) How do New Church scholars handle contradictions or problematic passages in Swedenborg?, (6) Would critical analysis of Swedenborg necessarily undermine framework, or can it show how revelation works THROUGH cultural context (parallel to biblical inspiration)?

**Expected Impact**:
If scholarship exists, framework can engage it honestly. Option A (apply HCM to Swedenborg) becomes feasible and strengthens methodological consistency. If scholarship thin or would require original research beyond framework scope, Option B (acknowledge asymmetry) more practical.

**Notes**:
High priority for epistemological integrity. See critical analysis Section 1C and Action 1.3. Sensitive topic but necessary for intellectual honesty.

---

## DOMAIN 8: EVIDENCE PRESENTATION — CHERRY-PICKING & BALANCE GAPS

### [EARLY] Paul's Humility vs. Authority: Balanced Scholarly Assessment

**Target**: `[NLM]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: EARLY-003, SWED-005, GNOS-003

**Context**:
Already in research question log. Critical analysis Sections 5A and 9 note framework selectively emphasizes confrontational Paul (authority claims, confronting Peter) while downplaying humble Paul ("slave of Christ," "least of apostles," weakness boasting). How do scholars interpret this?

**Research Question**:
How do Pauline scholars interpret passages where Paul describes himself with extreme humility? Examples: (1) "Slave of Christ" (δοῦλος Χριστοῦ), (2) "Least of the apostles" (1 Cor 15:9), (3) Weakness boasting (2 Cor 11-12), (4) Suffering catalogues (2 Cor 6:4-10). Do scholars see these as: (a) Authentic humility (Paul's genuine self-perception), (b) Rhetorical strategy (establishing authority paradoxically through humility), (c) Mixed: Sincere humility alongside prophetic zeal? How does this complicate framework's "proprium" diagnosis?

**Expected Impact**:
Framework must engage full Paul, not just confirming passages. If scholars see authentic humility, "proprium" interpretation requires nuancing or revision.

**Notes**:
Already logged. Including here for completeness. NotebookLM query—needs concise formulation.

---

### [CONSC] NDE Cultural Variation: Being of Light Identification

**Target**: `[NDE]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: CONSC-004

**Context**:
Already in research question log. Critical analysis Section 7B challenges framework's "pure identification" claim (atheists identifying being as Jesus based on personality match). Selection bias: most studies in Christian-majority cultures. Expectation effects.

**Research Question**:
In NDEs from Hindu-majority, Buddhist-majority, and Islamic-majority populations, what percentage of experiencers identify the "Being of Light" encountered as: (1) Jesus Christ, (2) Deities from their cultural tradition (Krishna, Yamaraj, Buddha, etc.), (3) Generic "deceased relatives" or unnamed beings, (4) No being encountered. Does personality-based identification transcend cultural conditioning, or do experiencers interpret the encounter through pre-existing religious frameworks?

**Expected Impact**:
If Hindu NDErs predominantly report Hindu deities rather than Jesus, framework's "pure identification" claim requires revision. If Jesus appears cross-culturally, remarkable evidence for framework.

**Notes**:
Already logged. Critical for framework's NDE interpretation. Statistical repository should have cross-cultural data.

---

## DOMAIN 9: UNDERREPRESENTED DOMAINS — EXPANSION NEEDS

### [BIBL] Synoptic Problem Solutions: Current Scholarly Distribution

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: BIBL-001, BIBL-002

**Context**:
Framework relies on Markan priority and Q hypothesis for source analysis. Knowledge graph shows Biblical Scholarship domain is underrepresented (13 nodes, 12%) compared to Swedenborgian Theology (33 nodes, 29%). Need current scholarly consensus on Synoptic Problem to ensure framework uses mainstream solutions.

**Research Question**:
What percentage of NT scholars accept: (1) Markan priority (Mark written first), (2) Q hypothesis (sayings source used by Matthew/Luke), (3) Farrer hypothesis (Luke used Matthew, no Q needed), (4) Griesbach hypothesis (Matthew first, Mark conflation), (5) Other solutions? Has consensus shifted in recent decades? What are strongest arguments for/against Q? Does framework's source analysis depend critically on Q existing, or can it work with alternative solutions?

**Expected Impact**:
Ensures framework uses current scholarly consensus. If Q is contested, source analysis requiring Q should be marked tentative.

**Notes**:
Biblical Scholarship domain underrepresented per prompt statistics. This question expands BIBL nodes with fundamental source-critical information.

---

### [BIBL] Gospel Genre and Historiographical Standards

**Target**: `[NLM]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: BIBL-002

**Context**:
Framework references Richard Burridge's work identifying Gospels as *bioi* (ancient biography). This affects historical expectations—ancient biography allowed theological shaping, not modern journalistic accuracy. Need clarity on what this means for historicity claims.

**Research Question**:
How do scholars define Gospel genre as ancient biography (*bioi*)? What historiographical standards did ancient *bioi* follow—verbatim accuracy, thematic accuracy, theological shaping? How does this affect assessment of Gospel historical reliability? Specifically: if Gospels are *bioi*, does this validate or challenge framework's use of embarrassment criterion and source criticism to reconstruct "authentic Jesus"?

**Expected Impact**:
Affects confidence in historical reconstructions. If *bioi* genre allowed substantial creative shaping, historical Jesus reconstruction becomes more uncertain.

**Notes**:
Biblical Scholarship expansion. Framework references Burridge but implications for historicity need clarity.

---

### [GNOS] Desert Fathers' Philautia vs. Swedenborg's Proprium

**Target**: `[NLM]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Low  
**Related Nodes**: SWED-005, GNOS-001

**Context**:
Knowledge graph SWED-005 evidence includes "Desert Fathers identified philautia as root of passions." Framework equates this with Swedenborg's proprium. Need verification and analysis of relationship.

**Research Question**:
What did Desert Fathers (Evagrius, Cassian) teach about *philautia* (self-love)? How does it relate to their teaching on passions (*logismoi*)? What's the relationship to pride (*hyperēphania*) vs. self-love specifically? How similar/different is this to Swedenborg's proprium doctrine?

**Expected Impact**:
Minor—validates connection or shows framework is overstating patristic parallel. Strengthens historical grounding of proprium concept.

**Notes**:
Gnostic Analysis domain underrepresented (9 nodes, 8%). This expands with patristic connection validation.

---

### [GNOS] "I AM God" Mechanic in Modern Spirituality: Empirical Survey

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: GNOS-004, GNOS-006

**Context**:
Framework identifies "I AM God" mechanic in modern SBNR movements, New Age, channeled systems. Claims this is proprium self-deification. Need empirical data on prevalence of this belief in contemporary spirituality.

**Research Question**:
What percentage of SBNR-identified individuals hold beliefs matching "gnostic impulse" pattern: (1) "I am divine/God," (2) "Material world is illusion/prison," (3) "Salvation through gnosis/awakening," (4) "Reject external moral authority"? Are these beliefs statistically clustered (one dimensional trait) or independent? How do sociologists of religion classify contemporary spirituality—do they recognize "gnostic" pattern or see more heterogeneity? What are demographic predictors of these beliefs?

**Expected Impact**:
If "gnostic impulse" is empirically identifiable pattern in modern spirituality, validates framework's category. If beliefs show no clustering, framework may be imposing pattern on diverse phenomena.

**Notes**:
Strengthens Gnostic Analysis domain with empirical data. Addresses critical analysis Section 8 concern about category overreach.

---

### [CROSS] Two-Tiered Epistemology: Philosophical Assessment

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: CROSS-001

**Context**:
Critical analysis Section 1A: framework conflates hermeneutic interpretation with epistemological integration. "This is hermeneutics, not epistemology." Framework claims "two-tiered epistemology" but operates as theological overlay on accepted scientific findings. Need philosophical analysis.

**Research Question**:
How do philosophers of science and epistemologists assess "dual epistemology" or "complementary ways of knowing" claims? Investigate: (1) Stephen Jay Gould's "Non-Overlapping Magisteria" (NOMA)—scholarly reception and critiques, (2) Critical realist philosophy (Roy Bhaskar, Alister McGrath)—stratified ontology with multiple levels, (3) What distinguishes epistemology (method of knowledge justification) from hermeneutics (method of interpretation)?, (4) Can theological interpretation of scientific findings constitute epistemology, or is it fundamentally hermeneutic?, (5) What would framework need to demonstrate to claim genuine "epistemological integration" rather than "interpretive overlay"?, (6) Are there successful models of faith-reason integration that avoid unfalsifiability trap?

**Expected Impact**:
Central to framework's self-understanding. If philosophical analysis shows framework is hermeneutic stance (not epistemology), requires fundamental reframing per critical analysis recommendations.

**Notes**:
THE key philosophical question. Cross-domain expansion addressing core framework claim. See critical analysis Section 1, falsifiability analysis.

---

## DOMAIN 10: COMPARATIVE & VALIDATION — EXTERNAL PERSPECTIVE GAPS

### [MYTH] Memory Code Hypothesis: Scholarly Reception

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: MYTH-003, MYTH-008, SWED-006

**Context**:
Framework cites Lynne Kelly's "Memory Code" hypothesis linking monuments to mnemonic technology. MYTH-008 and SWED-006 reference this as parallel to Swedenborg's Most Ancient Church cognitive state. Need scholarly assessment of Kelly's work.

**Research Question**:
What is academic reception of Lynne Kelly's Memory Code hypothesis? Investigate: (1) Has her work been peer-reviewed in archaeological/anthropological journals?, (2) Do mainstream archaeologists accept monuments-as-mnemonic-devices interpretation for Stonehenge, Göbekli Tepe, etc.?, (3) What evidence supports vs. challenges the hypothesis?, (4) How does Memory Code differ from or relate to "oral tradition" stability research?, (5) If mnemonic monuments did encode information, what types (genealogy, ritual sequences, astronomical observations) vs. theological narratives?, (6) Does Memory Code support Ancient Word hypothesis or offer naturalist alternative?

**Expected Impact**:
If Kelly's work is mainstream, strengthens framework's cognitive technology claims. If fringe or contested, framework must present more tentatively.

**Notes**:
Mythological Studies domain at 16 nodes (14%)—good coverage. This validates existing node MYTH-003.

---

### [MYTH] Enuma Elish and Genesis: Direction of Influence

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: MYTH-005, MYTH-006

**Context**:
Framework extensively analyzes Genesis/Enuma Elish parallels, proposing proto-myth divergence into "Heart of Division" vs. "Heart of Unity." Need scholarly consensus on historical relationship—borrowing, common source, or independent development?

**Research Question**:
What is scholarly consensus on relationship between Genesis creation accounts and Enuma Elish? Specifically: (1) Dating: Is Enuma Elish older than Genesis 1-11 (usually dated to exilic/post-exilic period)?, (2) Did Israelite authors know Babylonian myths during exile?, (3) Is relationship borrowing-and-subversion (Genesis deliberately countering Babylonian cosmology) or common ancient Near Eastern worldview?, (4) What about Genesis 1 vs. Genesis 2-3—different relationships to ANE myths?, (5) How do scholars explain parallels (flood, creation by divine word, separation of waters)—genetic relationship or cognitive universals?, (6) Is framework's "proto-myth divergence" model supported or is simpler explanation sufficient?

**Expected Impact**:
Determines whether proto-myth theory is necessary or framework is over-interpreting natural parallels. If scholars see borrowing-and-subversion, framework's "Heart of Unity" interpretation validated. If independent development, CDE-driven divergence unnecessary.

**Notes**:
Mythological Studies validation. MYTH-005 and MYTH-006 develop this extensively—need external scholarly check.

---

### [EARLY] Jesus vs. Paul Incompatibility: Scholarly Consensus

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: EARLY-003, EARLY-001

**Context**:
Framework presents "foundational divergence" between Jesus's teaching and Paul's theology as historical fact. Critical analysis Section 9 notes this reads as polemic—framework selectively emphasizes discontinuity while downplaying continuity. Need balanced scholarly assessment.

**Research Question**:
What is range of scholarly opinion on Jesus-Paul continuity vs. discontinuity? Investigate: (1) Scholars who emphasize continuity (Paul preserves Jesus's message)—main arguments, (2) Scholars who emphasize discontinuity (Paul invents Christianity)—main arguments, (3) How do scholars handle apparent differences (Kingdom of God vs. Christ-centered theology, Torah observance, justification by faith)?, (4) Is "incompatibility" framework's theological judgment or widely recognized historical problem?, (5) Alternative explanations: Paul adapting Jesus for Gentile context (contextual, not ideological difference)?, (6) How do scholars assess Epistle of James as potential critique of Pauline theology?, (7) Do scholars see Jamesian vs. Pauline movements as irreconcilable or as spectrum within early diversity?

**Expected Impact**:
If scholarly consensus sees continuity, framework's "foundational divergence" thesis is theological interpretation, not historical consensus. If debate exists, framework position is legitimate but must acknowledge alternative views.

**Notes**:
Critical analysis Section 9 and Action 2.4. Early Christian History domain adequately represented (17 nodes, 15%) but this validates core framework claim.

---

### [EARLY] Talpiot Tomb Statistical Analysis: Current Assessment

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Low  
**Related Nodes**: EARLY-011, BIBL-008

**Context**:
Framework references Talpiot tomb identification (Jesus, Mariamene, DNA evidence). Knowledge graph EARLY-011 acknowledges "highly contested." Need current scholarly assessment of Feuerverger's statistical methods and tomb identification claims.

**Research Question**:
What is scholarly consensus on Talpiot tomb identification? Investigate: (1) Andrey Feuerverger's statistical analysis claiming 600:1 odds favoring Jesus family tomb—critiques?, (2) How do archaeologists assess name commonality arguments (Yeshua, Mariamene, Yosef were common names)?, (3) What's the status of DNA evidence (non-maternal relationship between "Yeshua" and "Mariamene" ossuaries)?, (4) Why do most scholars reject tomb identification despite statistical/DNA claims?, (5) Is framework treating this as validated evidence or speculative possibility?, (6) If speculative, does framework acknowledge appropriate uncertainty?

**Expected Impact**:
Low impact—peripheral to core framework. But if framework overstates Talpiot evidence, marks need for confidence revision.

**Notes**:
EARLY-011 caveats show awareness of controversy. Research confirms framework presentation is appropriately tentative.

---

### [MYTH] Proto-Indo-European Reconstruction: Methodology as Model

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Low  
**Related Nodes**: MYTH-002, MYTH-008

**Context**:
Framework proposes tracing proto-myths through comparative analysis. Historical linguistics successfully reconstructs proto-languages (PIE) through systematic sound correspondences. Could similar methodology validate proto-myth hypothesis?

**Research Question**:
How do historical linguists reconstruct proto-languages, and can these methods apply to mythology? Investigate: (1) What are rigorous methods for PIE reconstruction (comparative method, regular sound correspondences, exclusion of borrowings)?, (2) Have scholars attempted parallel "comparative mythology" using linguistic methods?, (3) Georges Dumézil's comparative Indo-European mythology—scholarly reception and critiques, (4) Difference between linguistic reconstruction (systematic rules) and mythological comparison (thematic parallels)—can mythology be reconstructed with same rigor?, (5) What would constitute evidence for common proto-myth vs. independent development from cognitive universals?, (6) How could framework's proto-myth claims be tested?

**Expected Impact**:
If rigorous methods exist for mythological reconstruction, framework could adopt them. If mythology resists linguistic-style reconstruction, proto-myth claims remain speculative interpretive framework.

**Notes**:
Methodological strengthening. Mythological Studies domain well-developed but could use more rigorous validation methods.

---

## DOMAIN 11: CRITICAL SELF-EXAMINATION — FRAMEWORK VULNERABILITIES

### [CROSS] Confirmation Bias Safeguards: How Framework Self-Corrects

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: CROSS-001, CONSC-001

**Context**:
Critical analysis throughout identifies confirmation bias risks: framework finds what it looks for (correspondences in texts, ruling love in history, gnostic impulse in opponents). Knowledge graph acknowledges CONSC-001 "unfalsifiable as currently formulated—any outcome can be retroactively explained." How can framework avoid bias trap?

**Research Question**:
What methods exist in theology, philosophy, and history of ideas to avoid confirmation bias in interpretive frameworks? Investigate: (1) Falsificationism in philosophy of science (Popper)—can it apply to hermeneutic frameworks?, (2) How do theologians distinguish legitimate typology from eisegesis (reading meaning into text)?, (3) Biblical scholars' methods for distinguishing authorial intent from interpreter's projection, (4) Social science methods for avoiding selective evidence (systematic sampling, blinding, preregistration)—any applicable to historical/theological research?, (5) Case studies where interpretive frameworks corrected themselves based on contradictory evidence, (6) What institutional practices (peer review, devil's advocacy, adversarial collaboration) could framework adopt?

**Expected Impact**:
Critical for framework's intellectual integrity. If safeguards exist and framework adopts them, demonstrates commitment to truth over confirmation. If none exist for hermeneutic frameworks, must acknowledge inherent limitation.

**Notes**:
Meta-methodological question. Addresses critical analysis concern that framework is confirmation-bias-prone by design.

---

### [CROSS] Parsimony Test: What Does Framework Explain That Simpler Theories Cannot?

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: CROSS-001, CONSC-001, CROSS-002

**Context**:
Critical analysis repeatedly invokes Occam's Razor: simpler explanations should be preferred unless complex theory adds unique explanatory power. Framework adds metaphysical layer (correspondences, influx, ruling love, consciousness-as-causal) to naturalist explanations. What does this addition accomplish?

**Research Question**:
Conduct systematic parsimony analysis: For each major framework claim, identify simplest alternative explanation and articulate what framework's metaphysical addition provides. Examples: (1) NDE phenomenology: dying brain (simpler) vs. afterlife evidence (framework)—what does afterlife interpretation explain that dying brain cannot?, (2) Cultural evolution: dual inheritance theory (simpler) vs. CDE (framework)—unique predictions?, (3) Mythic parallels: cognitive universals + diffusion (simpler) vs. Ancient Word divergence (framework)—testable differences?, (4) Paul's theology: Jewish apocalypticism (simpler) vs. gnostic proprium (framework)—explanatory advantage?, (5) Gospel formation: natural bricolage (simpler) vs. divine influx (framework)—observable distinction? For each: Does framework make novel predictions, explain anomalies, or provide existential meaning (not explanatory power)?

**Expected Impact**:
Honest assessment of what framework provides. If it explains phenomena simpler theories cannot, justifies metaphysical addition. If it provides meaning but not explanation, should be framed as existential/theological framework, not superior epistemology.

**Notes**:
Core philosophical assessment. Addresses Occam's Razor challenges throughout critical analysis. Extended research question requiring systematic comparison.

---

### [CROSS] Framework Success Criteria: What Would Change Framework's Mind?

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: CROSS-001

**Context**:
Critical analysis questions whether framework can be challenged by evidence. If unfalsifiable claims dominate and all outcomes confirm ruling love polarity, framework becomes closed system. Intellectual integrity requires specifying conditions that would force revision.

**Research Question**:
What empirical findings or theoretical developments would require framework revision or abandonment? Systematically identify: (1) NDE research: What patterns would disconfirm post-mortem consciousness interpretation?, (2) DOPS research: What failure rate would undermine reincarnation evidence?, (3) Cross-cultural NDE studies: What distribution of being identification would challenge framework?, (4) Cultural evolution: What historical trajectories cannot be explained by ruling love polarity?, (5) Textual criticism: What source findings would challenge correspondence interpretations?, (6) Neurological: What findings would make consciousness-as-fundamental untenable?, (7) Philosophical: What demonstration would prove framework is unfalsifiable and therefore not genuine knowledge claim?

**Expected Impact**:
Demonstrates intellectual honesty and openness to revision. If framework can specify disconfirming conditions, shows it's empirically engaged. If cannot, confirms critical analysis: this is closed theological system, not open epistemology.

**Notes**:
Most important meta-question. See critical issues summary "Key Questions Framework Must Answer." This addresses all 15 questions systematically.

---

## DOMAIN 12: INTEGRATION & SYNTHESIS — CROSS-DOMAIN CONNECTION GAPS

### [CROSS] Correspondence Principle Applied Across Domains: Consistency Check

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: SWED-001, CROSS-002, MYTH-001, BIBL-003

**Context**:
Framework applies Swedenborgian correspondences to biblical texts, myths, and historical events. Cross-Domain nodes are underrepresented (5 nodes, 4%). Need systematic analysis: are correspondence interpretations consistent across domains, or does framework apply them selectively?

**Research Question**:
Conduct cross-domain correspondence consistency analysis: (1) Does "water" correspond to same spiritual reality in Genesis, Exodus, Gospels, and NDE reports?, (2) Do "mountain," "journey," "battle," "marriage" correspondences remain stable across textual domains?, (3) Where correspondences shift meaning, what's the principle governing variation?, (4) How does framework distinguish legitimate correspondence from allegorical reading that could fit any text?, (5) Are there domains where correspondence doctrine works better (myth, sacred texts) vs. worse (history, scientific findings)?, (6) Does framework apply correspondences to ALL events/texts or only those fitting theology?, (7) Statistical: What percentage of framework's textual analyses use correspondence interpretation vs. other methods?

**Expected Impact**:
If correspondences are systematically applied with internal consistency, strengthens doctrine. If applied selectively or inconsistently, confirms circular reasoning concern.

**Notes**:
Cross-Domain expansion (currently 4%). Addresses critical analysis falsifiability and consistency concerns.

---

### [CROSS] Divine Influx vs. Human Creativity: Observational Distinction

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: High  
**Related Nodes**: SWED-002, CROSS-002, MYTH-001

**Context**:
Framework claims Gospel writers, myth-makers, and scribes were guided by divine influx operating through natural bricolage process. Critical issues summary Key Questions #7: "What's the difference between 'influx' and 'human creativity' observationally?" This is unfalsifiability problem—same outcome (coherent narrative) explained by influx or by human skill.

**Research Question**:
Can divine influx be distinguished from human creativity by any observable criteria? Investigate: (1) What does Swedenborg say about how influx operates—conscious, unconscious, deterministic, probabilistic?, (2) Would authors know they were receiving influx or would it feel like their own thoughts?, (3) Comparison: inspired Scripture vs. uninspired religious texts—what observable differences validate inspiration claims?, (4) Could brilliant natural creativity (Shakespeare, Homer) produce texts indistinguishable from influx-guided ones?, (5) Does framework predict any signatures of influx (internal coherence, prophetic accuracy, cross-generational consistency) testable against non-influx texts?, (6) If influx is indistinguishable from creativity, is this distinction meaningful or theological projection?

**Expected Impact**:
Central unfalsifiability problem. If no observational distinction exists, "influx" is theological interpretation imposed on natural creativity, not empirical claim. Framework must acknowledge this or provide testable criteria.

**Notes**:
Critical issues summary Key Question #7. Addresses whether theological layer adds explanatory power or just religious language to natural phenomena.

---

### [CROSS] Ruling Love Polarity: Mixed Motivations and Developmental Change

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Priority**: Medium  
**Related Nodes**: CROSS-003, SWED-008

**Context**:
Critical analysis Section 3: ruling love polarity is reductive binary model (self-love vs. neighbor-love). Human motivation is multidimensional. Framework needs to address: (1) How does it handle mixed motivations?, (2) Can ruling love change over lifetime (regeneration), and if so, how is binary maintained?, (3) What about stages of moral development (Kohlberg)?

**Research Question**:
How does framework's ruling love binary relate to contemporary moral psychology? Investigate: (1) Kohlberg's stages of moral development (progression from self-interest to principled ethics)—compatible with ruling love or contradictory?, (2) Haidt's Moral Foundations Theory (multiple independent values)—can this be mapped to binary or does it refute reductive model?, (3) Developmental psychology: do people shift orientations over lifespan, and if so, what does this mean for "ruling love" as fixed pole?, (4) How does Swedenborg handle ambiguous cases—people with mixed motivations?, (5) Does regeneration (SWED-008) mean ruling love CAN change, and if yes, is binary about current state vs. ultimate trajectory?, (6) Can framework distinguish temporary self-interest (biological drives, survival) from proprium (spiritual self-glorification)?

**Expected Impact**:
Framework must show ruling love model handles real human complexity. If cannot, model is oversimplified theological construct useful for interpretation but not descriptive of psychology.

**Notes**:
Critical analysis Section 3 and critical issues #11. Moderate priority—framework can survive this challenge but needs nuancing.

---

## PRIORITY SUMMARY & HANDOFF RECOMMENDATIONS

### HIGH PRIORITY RESEARCH QUESTIONS (15 Questions)

These address critical epistemological issues, core framework claims, or major evidentiary gaps that could significantly strengthen or require revision of framework:

**Epistemological Core** (6 questions):
1. [CROSS] Two-Tiered Epistemology: Philosophical Assessment
2. [CROSS] Falsification Criteria for Correspondence Doctrine
3. [CROSS] Historical-Critical Method Applied to Swedenborg: Feasibility
4. [CROSS] Confirmation Bias Safeguards: How Framework Self-Corrects
5. [CROSS] Parsimony Test: What Does Framework Explain That Simpler Theories Cannot?
6. [CROSS] Framework Success Criteria: What Would Change Framework's Mind?

**Empirical Validation** (5 questions):
7. [CONSC] Life Review Empathetic Component Statistical Frequency
8. [CONSC] Distressing NDEs and Hellish Experiences
9. [CONSC] Veridical Perception Verification Rate in AWARE Studies
10. [CONSC] Children's Past-Life Cases: Overall Verification Rates
11. [CONSC] NDE Cultural Variation: Being of Light Identification

**Methodological Integrity** (4 questions):
12. [CROSS] CDE vs. Dual Inheritance Theory: Comparative Predictions
13. [CROSS] Dying Brain Hypothesis: Strongest Current Evidence
14. [SWED] Independent Validation of Correspondence Claims
15. [MYTH] Oral Tradition Stability: Songlines vs. Narrative Content

### MEDIUM PRIORITY RESEARCH QUESTIONS (14 Questions)

Address significant gaps, strengthen specific domains, or nuance existing claims:

**Domain Development**:
16. [SWED] Swedenborg's Doctrine Evolution Across Corpus
17. [SWED] Swedenborg's 18th-Century Intellectual Context
18. [SWED] Most Ancient Church: Archaeological Evidence vs. Golden Age Fallacy
19. [BIBL] Gospel Embarrassment Criterion: Current Scholarly Assessment
20. [BIBL] Lukan Redaction of Q and Proto-Luke Material
21. [BIBL] Synoptic Problem Solutions: Current Scholarly Distribution
22. [BIBL] Gospel Genre and Historiographical Standards
23. [CONSC] Intermission Memory vs. NDE Feature Comparison
24. [EARLY] Jamesian Protograph: Textual Evidence vs. Theological Inference
25. [EARLY] Desposyni Dynastic Claims: Historical Evidence
26. [EARLY] Paul's Damascus Vision: Scholarly Explanations
27. [GNOS] "Gnostic Impulse" Category: Historical Heterogeneity
28. [GNOS] Paul as Proto-Gnostic: Mainstream vs. Framework Position
29. [GNOS] "I AM God" Mechanic in Modern Spirituality: Empirical Survey

### LOW PRIORITY RESEARCH QUESTIONS (7 Questions)

Strengthen details, validate peripheral claims, or explore tangential connections:

30. [BIBL] Western Non-Interpolations: Scholarly Consensus
31. [EARLY] Magi as Persian Priests: Zoroastrian Connection Evidence
32. [EARLY] Talpiot Tomb Statistical Analysis: Current Assessment
33. [GNOS] Desert Fathers' Philautia vs. Swedenborg's Proprium
34. [MYTH] Göbekli Tepe Astronomical Interpretation: Archaeological Consensus
35. [MYTH] Memory Code Hypothesis: Scholarly Reception
36. [MYTH] Proto-Indo-European Reconstruction: Methodology as Model

### INTEGRATION QUESTIONS (4 Questions)

Cross-domain synthesis and consistency checks:

37. [CROSS] Correspondence Principle Applied Across Domains: Consistency Check
38. [CROSS] Divine Influx vs. Human Creativity: Observational Distinction
39. [CROSS] Ruling Love Polarity: Mixed Motivations and Developmental Change
40. [MYTH] Proto-Myth Divergence: Traceable Evidence vs. Theoretical Construct
41. [MYTH] Enuma Elish and Genesis: Direction of Influence
42. [EARLY] Jesus vs. Paul Incompatibility: Scholarly Consensus

---

## AGENT HANDOFF RECOMMENDATIONS

### @source-tracer
**When**: After external research resolves source questions  
**Questions**: All questions resulting in identification of primary sources, original scholarship, or tracing claims to foundations  
**Action**: Integrate findings into knowledge graph source chains, update trace_status

### @knowledge-compiler  
**When**: Research produces new conceptual information requiring node creation  
**Questions**: All questions yielding new concepts, relationships, or evidence  
**Action**: Create new nodes, update existing nodes with evidence/caveats, establish connections

### @consciousness-expert
**When**: Formulating follow-up questions on NDE/DOPS research  
**Questions**: #7, #8, #9, #10, #11, #23  
**Action**: Assist with technical formulation for NDE Statistical Repository

### @graph-reviewer
**When**: Determining which untraced claims are highest priority for research  
**Questions**: Review current research question priority assignments  
**Action**: Validate priority classifications based on graph dependencies

### @critic
**When**: Research reveals challenges to framework assumptions  
**Questions**: All HIGH PRIORITY epistemological questions (#1-6, #12-15)  
**Action**: Assess whether findings require framework revision, reframing, or falsification

---

