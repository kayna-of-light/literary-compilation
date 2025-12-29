# Research Questions

This document tracks **OPEN** research questions, gaps in analysis, and hypotheses requiring further investigation. Questions are formatted for use with external research tools (NotebookLM, Gemini Deep Research, NDE Statistical Repository).

> **Usage**: Copy the relevant question block (context + question) to the appropriate research tool. Questions are separated by horizontal rules for easy identification.

> **📁 Resolved Questions**: Completed investigations are archived in [resolved_research_questions.md](resolved_research_questions.md). Check there for past research findings and source chains.

---

## ⚠️ ANTI-BIAS INSTRUCTIONS FOR RESEARCH QUESTIONS

**The following principles MUST guide all research question formulation:**

### 1. "Mainstream" ≠ Neutral

Do NOT assume that "mainstream scholarship" or "scholarly consensus" represents objective truth. Much biblical and theological scholarship reflects:
- **Institutional bias**: Scholars trained in confessional seminaries
- **Apologetic motivation**: Protecting doctrinal commitments
- **Selection effects**: Career pressures favoring orthodox conclusions
- **Historical capture**: 2000 years of church-controlled scholarship

**Example of bias**: The claim "Paul taught bodily resurrection (1 Cor 15)" is demonstrably false per the text itself (1 Cor 15:44-50 explicitly argues for *soma pneumatikon*, spiritual body; "flesh and blood cannot inherit the kingdom"). Yet this false claim appears throughout "mainstream" scholarship because it protects orthodox Christology.

### 2. Verify Premises Before Asking External Research

Before assuming framework claims need "external validation":
1. **Check internal sources first** — Our data/ folder contains extensive research
2. **Verify the premise** — Is the challenge itself based on biased assumptions?
3. **Question the questioner** — Who benefits from framing the issue this way?

### 3. The Truth Shows Itself

> "We do not condone theological bias. The truth has to show itself because it is the truth, not because we want it to."

This applies to ALL positions—framework claims AND their challengers. Neither should be accepted because "scholars say so." Both require textual, historical, and logical validation.

### 4. Warning Signs of Biased Research Questions

Questions may embed bias if they:
- ❌ Assume orthodox readings as neutral baseline to be challenged
- ❌ Treat "mainstream" as authority rather than one perspective among many
- ❌ Frame framework positions as "claims" while treating alternatives as "facts"
- ❌ Request validation for positions already well-documented in internal sources
- ❌ Ignore or dismiss evidence that challenges conventional narratives

### 5. Proper Research Question Framing

Questions should:
- ✅ Present all positions as hypotheses requiring evidence
- ✅ Acknowledge potential bias in ALL scholarly traditions
- ✅ Check internal sources before requesting external research
- ✅ Specify what evidence would validate OR refute any position
- ✅ Distinguish between theological interpretation and historical claim

---

## Document Organization

| Document | Purpose |
|----------|---------|
| **research_questions.md** (this file) | **OPEN** questions requiring investigation |
| [resolved_research_questions.md](resolved_research_questions.md) | **RESOLVED** questions with findings archived |

When a question is resolved:
1. Move the entire question block to `resolved_research_questions.md`
2. Update the Status to `✅ RESOLVED`
3. Add the resolution date and findings
4. Update the statistics at the bottom of the resolved document

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

### [NDE] Systematic Verification of NDE Statistical Claims in Framework

**Target**: `[NDE]`  
**Status**: Open  
**Date Added**: 2025-12-30  
**Priority**: HIGH  
**Related Nodes**: CROSS-006, CONSC-*

**Context**:
During source tracing on 2025-12-29/30, we discovered that a statistical claim about Jesus identification rates in NDEs ("~60% of Western experiencers identify the Being of Light as Jesus") was erroneous. The claim originated in a Gemini Deep Research document that cited a source which does NOT contain that statistic. This hallucinated claim propagated into the knowledge graph (CROSS-006) before correction.

This reveals a systematic vulnerability: framework documents generated by AI research tools may contain unverified quantitative claims that appear authoritative but lack actual data foundation.

**Hallucination Propagation Chain Discovered**:
```
Gemini Deep Research → Source Document (unverified claim) → Knowledge Graph → Research Question
```

**Corrected Statistics (from actual NDE data analysis, n=3,189 Being of Light encounters)**:
- Unknown Presence: 61.8%
- God: 23.0%
- Jesus: 11.2%
- Religious Figure: 4.0%

**Research Question**:
1. Systematically audit all NDE percentage claims appearing in `data/01_Consciousness_Studies/` documents
2. Cross-reference each quantitative claim against the actual nde-data-analysis repository data
3. Flag any claims that cannot be traced to actual statistical analysis
4. For each flagged claim: identify the original source cited, verify whether that source contains the claimed statistic, and correct or remove erroneous claims
5. Create an audited statistics reference table that can be used as authoritative data source

**Key Documents Requiring Audit**:
- `Divine Bricolage vs. Swedenborg's Jesus.md` (corrected 2025-12-30)
- `Pure Encounter or Cultural Construct.md`
- `Researching Near-Death Experiences.md`
- `threefold-path-validation-report-analysis_iands_and_nand_2025.md`
- `conceptual_framework_deep_dive_report-analysis_iands_and_nand_2025.md`
- `conceptual-framework-theory-validation-analysis_iands_and_nand_2025.md`

**Expected Output**:
1. Verified statistics reference table with proper citations to nde-data-analysis queries
2. List of corrected or flagged claims
3. Updated knowledge graph nodes as needed
4. Protocol for future statistical claim verification

**Notes**:
This is critical for maintaining scholarly integrity. AI-generated source documents should be treated as hypotheses requiring verification, not as authoritative sources. All quantitative claims must be traceable to actual data.

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

> **✅ RESOLVED** — See [resolved_research_questions.md](resolved_research_questions.md) for findings.  
> **Summary**: `UNKNOWN_PRESENCE` is a distinct enum value in the questionnaire schema (not ambiguous/missing data). AI-assisted classification distinguishes it from `NOT_SPECIFIED` (no mention) and `NONE` (no being). The 61.8% rate represents experiencers who encountered a being but couldn't categorize it despite available vocabulary.

---

### [NDE] Operationalization: "Reincarnation Indicators" Search Criteria

> **✅ RESOLVED** — See [resolved_research_questions.md](resolved_research_questions.md) for findings.  
> **Summary**: "0% reincarnation indicators" is based on structural absence of specific elements (next-life selection, memory wipe prep, karmic cycling language), not keyword search. The claim is valid within scope: NDEs show continuation, not cycling preparation. Caveat: NDEs are return cases, so cannot test complete post-death journey or Restorative Path.

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

## NDE/DOPS Research Questions

> **⚠️ INTERNAL NOTE (not for external research tools)**
> 
> The following questions address potential selection artifacts in existing research:
> - DOPS methodology requires a deceased "Previous Personality" for verification, potentially filtering out non-cyclic cases
> - Intermission phenomenology appears in ~20% of cases — a minority, not a norm
> - The 70%+ violent death correlation indicates exceptional return, not universal reincarnation (VALIDATED—see CONSC-046)
> - Cultural imagery variation may reflect correspondential clothing of constant functional states (VALIDATED—see CONSC-045)
> 
> **NEW (2025-01-03)**: The "Reincarnation Methodology Selection Artifact" document has been processed, adding:
> - **CONSC-047**: SOCS Selection Bias (Trauma Filter Hypothesis) — explains WHY 70% violent death in DOPS
> - **CONSC-048**: Ohkado Reverse Cases — empirical evidence for non-cyclic origin (pre-birth WITHOUT past-life)
> - **CONSC-049**: Veridical Pre-Existence (VPE) — perinatal verification method for first incarnation claims
> - **CONSC-050**: COPET Proposal — Cases of Pre-Existence Type methodology to complement CORT
> 
> See: `data/01_Consciousness_Studies/Reincarnation Methodology Selection Artifact.md`
> 
> Questions are designed to test these specific hypotheses without assuming any framework.

---

### [NDE+GDR] Discriminant Analysis: Using Restorative Markers to Identify Non-Cyclic Origin Cases

**Target**: `[NDE]` + `[GDR]`  
**Status**: Open  
**Date Added**: 2025-01-06  
**Updated**: 2025-01-03 (New supporting evidence from CONSC-047/048/049/050)  
**Priority**: HIGHEST  
**Depends On**: CONSC-046 (Restorative Return validation), CONSC-010 (Volunteer Soul), CONSC-045 (Correspondential Validation), **NEW: CONSC-047 (Trauma Filter), CONSC-048 (Ohkado Reverse Cases), CONSC-049 (VPE), CONSC-050 (COPET Proposal)**

**New Evidence (2025-01-03)**:
- **Ohkado Reverse Cases (CONSC-048)**: Japanese researcher documented children with intermission memories but NO past-life recall — direct empirical support for non-cyclic entry hypothesis
- **SOCS Trauma Filter (CONSC-047)**: DOPS SOCS awards 0 points for first incarnation claims — structural methodological exclusion
- **Veridical Pre-Existence (CONSC-049)**: Rivas/Dirven/Smit documented perinatal verification as alternative to PP verification
- **Key Cases**: Vincent B. (guided tour of future life), Karim ("blue ray" arrival with parent choice)

**Context**:
The DOPS Restorative Return analysis (CONSC-046) has now VALIDATED six independent markers that characterize the trauma-driven reincarnation pathway:

| Marker | Validated Finding |
|--------|------------------|
| **Violent death** | >70% prevalence (massive deviation from baseline) |
| **Birthmarks** | 35% prevalence, 88% medical verification |
| **Temporal urgency** | Shorter intermissions (p<.01), suicide ~3 months |
| **Age distribution** | PP avg age ~28; 25% <15 (inverted mortality curve) |
| **Behavioral** | 35% phobias matching death mode |
| **Resolution** | Symptoms remit after verification |

These markers describe a **specific, anomaly-driven mechanism** — NOT a universal system of reincarnation. The question: can we use these validated markers INVERSELY to identify cases that represent a DIFFERENT pathway?

**Theoretical Framework**:
The Threefold Path model (CONSC-010) predicts three distinct post-mortem pathways:
1. **Normative Linear** — Spiritual progression without earthly return (majority)
2. **Restorative Return** — Trauma-driven return for healing/completion (minority)
3. **Volunteer/Non-Cyclic** — First incarnation or mission-oriented entry (rare)

If pathway 3 is real and distinguishable, cases should show:
- ABSENCE of Restorative trauma markers (no violent death, no birthmarks, no phobias)
- PRESENCE of different positive markers (mission language, choosing, purpose statements)

**Discriminant Filter Design**:

| Restorative Profile (Exclude) | Non-Cyclic Profile (Include) |
|------------------------------|------------------------------|
| Prior-life death narrative | NO death narrative; spiritual realm origin |
| Birthmarks from wounds | NO birthmarks |
| Phobias matching death mode | NO trauma phobias |
| Short intermission (urgency) | "Choosing" language / deliberate selection |
| PTSD-like symptoms | Mission-orientation; purpose statements |
| "Unfinished business" theme | "I came to help" / "I chose you" themes |

**Research Questions**:

**1. NDE Repository Query**:
Cross-tabulate in the NDE statistical repository:
- Pre-existence memories/themes × violent death circumstance (should be NEGATIVELY correlated if pathways are distinct)
- "Sent back with mission" × trauma indicators
- "Choosing to come" vs "forced back" language patterns

**2. DOPS Literature Analysis**:
Search published DOPS/pre-existence literature for cases that:
- Have NONE of the six Restorative markers
- Report spiritual realm origin, choosing parents, mission statements
- Describe first incarnation explicitly ("I was always in the light" vs "I was someone else")

**3. Phenomenological Contrast**:
If cases are identified in both groups:
- What additional phenomenological features distinguish them?
- Do "non-cyclic" cases show different emotional tone (curiosity vs. distress)?
- Do they show different claim patterns (purpose vs. identity)?

**4. Statistical Validation**:
If enough cases exist:
- Chi-square analysis: Are Restorative markers negatively correlated with mission/volition markers?
- Cluster analysis: Do cases naturally cluster into distinct phenomenological groups?

**Falsification Criteria**:
- **Supports hypothesis**: Statistically significant negative correlation between trauma markers and mission/volition markers
- **Refutes hypothesis**: No correlation pattern; markers appear randomly distributed
- **Inconclusive**: Too few non-Restorative cases to analyze (suggests selection artifact)

**Expected Value**:
If non-cyclic origin cases are REAL and DISTINGUISHABLE:
- The validated Restorative markers function as a negative filter
- Filtered cases show coherent positive markers of non-cyclic origin
- This validates the Threefold Path model and refines incarnation cosmology

If this shows NOTHING:
- Either non-cyclic cases are extremely rare / methodologically invisible
- Or the phenomenology is indistinguishable (pathways differ only in origin, not in markers)
- Or the Volunteer Soul paradigm is theoretically valid but empirically undetectable

---

### [GDR] DOPS Non-Cyclic Cases: Pre-Birth Memories Without Death Narrative

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-29  
**Priority**: HIGH  

**Context**:
DOPS research methodology is designed to study "Cases of the Reincarnation Type" (CORT) — children who remember previous lives. The verification process requires identifying a deceased "Previous Personality" whose life matches the child's statements. Cases are "solved" when this PP is identified and statements verified.

This methodology creates a potential selection artifact: it can only capture cases where a prior earthly life and death occurred. But what about children who report pre-birth memories of a spiritual realm, choosing their parents, being sent by a guide — but have NO memories of being someone else who died?

Such cases would be:
- Not classifiable as "reincarnation type" (no prior earthly life)
- Unverifiable (no deceased PP to match)
- Potentially excluded from analysis or dismissed as fantasy

If souls can incarnate for purposes OTHER than returning after a prior death (first incarnation, mission-oriented entry, arrival from non-earthly origin), these cases would be invisible in current DOPS methodology.

**Research Question**:
Search published literature for cases with pre-birth/spiritual realm memories but NO previous-life death narrative:

1. **DOPS unsolved cases**: Do any published DOPS summaries describe children with pre-birth memories (realm descriptions, choosing parents, being sent) but NO identifiable PP? What happens to these cases?

2. **Pre-birth memory literature**: Rivas, Dirven, and Smit have published research specifically on pre-existence memories. What do they report about cases WITHOUT a prior-life-death component? What is the phenomenology? How frequent?

3. **"Stranger" cases**: DOPS distinguishes "same-family" cases (child reincarnates into family of PP) from "stranger" cases (unrelated family). Stranger cases are harder to verify. Do these show different phenomenological profiles? Higher rate of "I chose you" vs. "I was sent"?

4. **First-incarnation claims**: Are there ANY published cases where a child explicitly claims this is their first earthly life, but reports memories of a pre-birth spiritual realm? How are these handled methodologically?

5. **Origin descriptions**: In cases with intermission memories (memories of the period between death and rebirth), do any describe coming from somewhere OTHER than a previous earthly life? Descriptions like "I was with God," "I came from far away," "I was in the light" — without any PP death narrative?

6. **Western case patterns**: Western DOPS cases have lower "solved" rates than Asian cases. Could this be because Western subjects more frequently report pre-birth memories without verifiable PP details? (Would suggest the pattern exists but is methodologically invisible)

**Expected Output**:
Evidence for or against the existence of a "non-cyclic origin" cohort in the data — children with genuine pre-birth spiritual memories who did NOT have a prior earthly death. If such cases exist but are filtered out by methodology, this reveals a selection artifact. If they genuinely don't appear in any literature, that's important data too.

**Key Sources**:
- Rivas, T., Dirven, A., & Smit, R. — "Paranormal Aspects of Pre-Existence Memories in Young Children"
- Tucker, J. — Case selection methodology papers
- DOPS published descriptions of unsolved or excluded cases

---

### [NDE/DOPS] Convergent Functional States Between NDEs and Intermission Memories

**Target**: `[NDE]` + `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-29  
**Priority**: HIGH  

**Context**:
Two separate research traditions study consciousness during the transition between physical lives:

1. **NDE Research**: Adults who clinically die and are resuscitated report experiences during the period of death. These are observations of the "exit" from physical life.

2. **DOPS Intermission Research**: ~20% of children with past-life memories also report memories of the period BETWEEN lives — after the previous personality's death and before their own birth. These are observations of the "entry" into physical life.

If both research streams are observing the same underlying reality, they should show convergence — not necessarily in imagery (which may be correspondentially clothed differently for a dying adult vs. a pre-verbal child's later reconstruction), but in FUNCTIONAL STATES.

Previous analyses compared phenomenological details (do both report "light"? "beings"? "tunnels"?). This may be the wrong level of analysis. We should compare whether both show the same functional transition sequence.

**Research Question**:
Do NDE phenomenology and DOPS intermission memories show convergent FUNCTIONAL STATES?

| Functional State | NDE Manifestation | DOPS Intermission Manifestation | Convergent? |
|------------------|-------------------|--------------------------------|-------------|
| **Separation from body** | Out-of-body experience, viewing resuscitation | Watching own funeral, hovering near corpse | Compare rates |
| **Transition/movement** | Tunnel, void, darkness | Walking, flying, transformation | Compare features |
| **Arrival/orientation** | Entering realm of light, meeting guide | "Stable stage" in discarnate realm | Compare duration |
| **Evaluation** | Life review | (Largely absent in DOPS data?) | Test divergence |
| **Decision point** | Choice to return, being told "not your time" | Choosing parents, being sent/directed | Compare agency |
| **Re-entry to body** | Returning to same body | Entering new body (womb, conception) | Compare mechanism |

Specific questions:

1. **Separation state**: What percentage of NDEs report OBE? What percentage of DOPS intermission cases report post-death observation of earthly events? Are these functionally equivalent?

2. **Evaluation divergence**: Life Review appears in ~19% of NDEs. Is there ANY equivalent in DOPS intermission data? If not, why? (Different population? Different temporal direction — review looks backward, intermission looks forward?)

3. **Decision/agency**: NDE "return decision" and DOPS "choosing parents" — both involve agency regarding physical embodiment. Are they functionally equivalent? What percentage involve choice vs. being directed by authority?

4. **Re-entry mechanisms**: NDEs describe returning TO THE SAME BODY. DOPS children describe entering A NEW BODY (often vivid descriptions of conception/womb entry). Same process, different direction? Or genuinely different mechanism?

5. **Absent states**: Are there states that appear in one dataset but NOT the other? What would this mean?

**Expected Output**:
A functional state comparison map. If NDE and DOPS intermission show the same states in the same sequence (despite imagery differences), this strongly validates a unified model of consciousness transition. If they show different states or sequences, they may be different phenomena requiring different explanations.

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

## DOMAIN 1: CONSCIOUSNESS STUDIES — EMPIRICAL VALIDATION GAPS

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

### [GDR] CDE vs. Dual Inheritance Theory: Critical Predictions

**Target**: `[GDR]`  
**Status**: Open  
**Date Added**: 2025-12-27  
**Date Revised**: 2025-12-30  
**Priority**: CRITICAL  
**Related Nodes**: CONSC-001, CROSS-003, CROSS-004

**⚠️ FRAMING NOTE**: The premise that materialist theories are "simpler" assumes metaphysical naturalism as default. Post-materialist frameworks argue consciousness is fundamental and material explanations are the additions requiring justification. This question should be reframed: Do either DIT/CGS or CDE better explain the observed data, regardless of metaphysical commitments?

**Context**:
Framework proposes Consciousness-Driven Evolution (CDE) as selective pressure on memetic evolution. Critical analysis notes alternatives (Boyd & Richerson's Dual Inheritance Theory, Wilson's Cultural Group Selection) may explain same phenomena without metaphysical "consciousness-as-causal-force" assumption. However, DIT/CGS assume consciousness-as-epiphenomenon, which is also a metaphysical assumption.

**Research Question**:
How do Dual Inheritance Theory and Cultural Group Selection explain cultural evolution patterns framework attributes to CDE?
1. What predictions do DIT and CGS make about when cooperative vs. competitive cultural strategies dominate?
2. How do these theories explain prosocial norm emergence?
3. Do DIT/CGS treat consciousness as epiphenomenal correlate or causal driver? What is their metaphysical assumption?
4. What specific, testable predictions does CDE make that DIT/CGS cannot explain?
5. Can CDE explain any cultural trajectory that DIT/CGS cannot?
6. What anomalies exist in cultural evolution that neither theory fully explains?
7. Are there phenomena (cross-cultural NDE convergence, veridical perception) that DIT/CGS cannot account for but CDE can?

**Expected Impact**:
This is a fair comparison test—both frameworks should be evaluated on explanatory power, not assumed metaphysical priority. Neither materialism nor post-materialism should be treated as "default."

**Notes**:
Already in research question log. Central epistemological issue. Both frameworks have metaphysical commitments—neither is "simpler" in any absolute sense.

---

## DOMAIN 2: SWEDENBORGIAN THEOLOGY — SOURCE VALIDATION GAPS

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

### [CROSS] Dying Brain Hypothesis: Critical Evaluation of Evidence Quality

> **✅ RESOLVED** — See [resolved_research_questions.md](resolved_research_questions.md) for findings.  
> **Summary**: Comprehensive analysis in `data/01_Consciousness_Studies/Evaluating Dying Brain Hypothesis Critically.md`. DBH mechanisms (anoxia, DMT, gamma surge, temporal lobe) fail to explain: veridical perception during flat EEG, hyper-lucidity (inverse relationship), empathetic life review, terminal lucidity, and shared death experiences. AWARE study shows awareness 3+ minutes into arrest. Key veridical cases (Reynolds, Sullivan, Dentures Man) addressed with skeptical rebuttals. 63 scholarly sources.

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
**Date Revised**: 2025-12-30  
**Priority**: High  
**Related Nodes**: EARLY-003, EARLY-001

**⚠️ BIAS NOTICE**: This question's framing should be scrutinized. The premise that "continuity scholars" represent objective baseline while "discontinuity" is framework's theological judgment may itself reflect orthodox apologetic bias. Scholars trained in confessional traditions have institutional incentives to harmonize Jesus and Paul. The question of who transformed whom is not settled by counting scholars on each side.

**Context**:
Framework presents "foundational divergence" between Jesus's teaching and Paul's theology as historical fact. Critical analysis Section 9 notes this reads as polemic—framework selectively emphasizes discontinuity while downplaying continuity. Need balanced scholarly assessment.

**Key Internal Evidence Already Documented**:
- `A Foundational Divergence.md` - Comprehensive comparison of teachings
- Multiple structural differences: Torah observance (Jesus upholds vs. Paul dismisses), Kingdom of God (Jesus's focus) vs. Christ-centered soteriology (Paul's focus), James's critique in Epistle of James 2:14-26

**Research Question**:
What is range of scholarly opinion on Jesus-Paul continuity vs. discontinuity? Investigate: (1) Scholars who emphasize continuity (Paul preserves Jesus's message)—main arguments AND potential confessional bias, (2) Scholars who emphasize discontinuity (Paul invents Christianity)—main arguments, (3) How do scholars handle apparent differences (Kingdom of God vs. Christ-centered theology, Torah observance, justification by faith)?, (4) Are "continuity" readings apologetically motivated to protect canonical unity?, (5) What textual evidence would be required to demonstrate actual incompatibility?, (6) How do scholars assess Epistle of James as potential critique of Pauline theology?, (7) Do scholars see Jamesian vs. Pauline movements as irreconcilable or as spectrum within early diversity?

**Expected Impact**:
This question is complex because BOTH "continuity" and "discontinuity" camps may have theological motivations. Framework should present evidence for discontinuity while acknowledging the debate exists.

**Notes**:
Critical analysis Section 9. Both positions require scrutiny—not just framework's position.

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

## STATISTICS

| Category | Count |
|----------|-------|
| **Total Open** | 56 |
| **NDE Domain** | 9 |
| **GDR Domain** | 12 |
| **CROSS Domain** | 10 |
| **EARLY Domain** | 6 |
| **MYTH Domain** | 6 |
| **BIBL Domain** | 5 |
| **SWED Domain** | 3 |
| **GNOS Domain** | 3 |
| **NLM Domain** | 1 |
| **GDR/NLM Combined** | 1 |

**Last Updated**: 2025-12-30

---

## PRIORITY SUMMARY

### HIGH PRIORITY RESEARCH QUESTIONS

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

