# Knowledge Graph Node Removal Documentation

**Date:** January 7, 2025  
**Status:** ⚠️ REVISED  
**Reason:** Source reports identified as incomplete/incorrect. New research papers will provide corrected findings.  
**Action:** Removal of nodes derived from invalidated reports, with one RESTORATION.

## Summary of Changes

- **Nodes Removed:** 18 (CONSC-021-030 were REPLACED, not removed; CONSC-031-033, 035-039 were removed)
- **CONSC-034 RESTORED:** This node was based on valid DOPS external sources, NOT invalidated reports
- **CONSC-021-030 REPLACED:** These node IDs were reused for new content from valid documents
- **Connections Removed:** References to deleted nodes cleaned from remaining nodes
- **Graph Validation:** ✅ PASSED after restoration

## CORRECTION NOTICE (2025-01-07)

CONSC-034 was **incorrectly grouped** with invalidated report nodes but its actual sources are:
- `data/01_Consciousness_Studies/DOPS Case Verification and Critiques.md` (VALID)
- Stevenson/Tucker DOPS publications (VALID)
- UVA DOPS database (VALID)

The node has been **RESTORED** to the knowledge graph with updated connections.

## Source Reports Invalidated

1. `conceptual_framework_deep_dive_report-analysis_iands_and_nand_2025.md`
2. `conceptual-framework-theory-validation-analysis_iands_and_nand_2025.md`
3. `threefold-path-validation-design-analysis_iands_and_nand_2025.md`
4. `threefold-path-validation-report-analysis_iands_and_nand_2025.md`
5. `volunteer-soul-profile-report-analysis_iands_and_nand_2025.md`

---

## Nodes Removed (CONSC-021 through CONSC-039)

### CONSC-021: Conceptual Framework Theory (CFT) - Empirical Validation
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.8)
- **Definition:** Theory that Being of Light encounters represent objective phenomenological reality that experiencers describe using available cultural vocabulary. Validated through statistical analysis of 6,739 NDEs.
- **Key Claims:**
  - 61.8% of Being of Light encounters identified as "unknown presence"
  - 84.8% no external condemnation in life reviews
  - 79.4% active two-way communication with Being
  - 56.4% complete fear loss; 60-63% cross-religious consistency
  - ML model 68.2% accuracy
- **Connections TO other nodes:** CONSC-004, CONSC-008, CROSS-003, SWED-002
- **Connected FROM:** CONSC-022, CONSC-023, CONSC-024, CONSC-025, CONSC-026, CONSC-027, CONSC-028, CONSC-029, CONSC-030

### CONSC-022: Unknown Presence Phenomenon (61.8%)
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.763)
- **Definition:** Finding that 61.8% of Being of Light encounters are identified as "unknown presence" rather than cultural labels.
- **Key Claims:**
  - Unknown Presence: 1,970 cases (61.8%)
  - God: 732 cases (23.0%)
  - Jesus: 358 cases (11.2%)
  - Religious Figure: 129 cases (4.0%)
- **Connections TO:** CONSC-021, CONSC-004, CONSC-008, CONSC-024

### CONSC-023: Life Review: No External Condemnation (84.8%)
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.763)
- **Definition:** Finding that 84.8% of life reviews involve NO external condemnation.
- **Key Claims:**
  - No judgment at all: 714 cases (57.0%)
  - Self-judgment only: 329 cases (26.3%)
  - Love-to-Shame ratio: 3.4:1
- **Connections TO:** CONSC-003, CONSC-008, CROSS-003, SWED-003, CONSC-021
- **Connected FROM:** CONSC-030

### CONSC-024: Theological Framework Mismatch Hypothesis
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** preliminary (confidence: 0.723)
- **Definition:** Hypothesis that "unknown presence" classification reflects characteristic mismatch rather than pure inability to categorize.
- **Connections TO:** CONSC-022, CONSC-021, EARLY-001, CROSS-003

### CONSC-025: Cross-Religious Fear Loss Consistency (60-63%)
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.763)
- **Definition:** Finding that complete fear of death loss occurs at virtually identical rates across ALL religious backgrounds.
- **Key Claims:**
  - Christian: 62.2%, Atheist: 62.3%, SBNR: 62.5%, Muslim: 62.9%, Jewish: 60.0%
  - Coefficient of variation: 1.8%
- **Connections TO:** CONSC-021, CONSC-004, CROSS-003

### CONSC-026: Being of Light: Personal Conscious Entity Evidence
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.763)
- **Definition:** Demonstration that Being of Light exhibits five markers of personal conscious entity.
- **Key Claims:**
  - Active communication: 79.4%
  - Telepathic mode: 51.4%
  - Significant guidance: 59.6%
- **Connections TO:** CONSC-008, CONSC-004, SWED-002, CONSC-021

### CONSC-027: Being of Light: Unique Authoritative Position
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.763)
- **Definition:** Evidence that Being of Light occupies a DISTINCT, central role compared to other beings.
- **Key Claims:**
  - Light Being guidance: 59.6% vs Other beings: 49.3%
  - Light Being alone: 71.6%
- **Connections TO:** CONSC-008, CONSC-004, CONSC-021

### CONSC-028: Normative Path Hypothesis: Continuation Evidence
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.782)
- **Definition:** Five independent markers support CONTINUATION as normative post-death path, NOT reincarnation.
- **Key Claims:**
  - Deceased relatives present: 18.7%
  - Return as exception: 41.6%
  - Identity/memory preserved: 89.9%
  - Reincarnation indicators: 0%
  - Sequential ordering: 40% follow canonical sequence
- **Connections TO:** CONSC-011, CONSC-013, CONSC-005, SWED-003, CONSC-002, CONSC-033
- **Connected FROM:** CONSC-031, CONSC-033, CONSC-037

### CONSC-029: Pure Projection Model: Substantially Weakened
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.745)
- **Definition:** Statistical falsification of the hypothesis that NDE Being of Light encounters are pure mental projections.
- **Connections TO:** CONSC-021, CONSC-022, CONSC-025, CONSC-004

### CONSC-030: Empathetic Life Review Component (25.7%)
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.705)
- **Definition:** Finding that 25.7% of life reviews involve experiencing others' perspectives.
- **Connections TO:** CONSC-003, CONSC-008, CROSS-003, CONSC-023

### CONSC-031: Threefold Path: Pathway Distribution (88.5% Normative / 11.5% Volunteer)
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.812)
- **Definition:** Statistical validation of the "Both/And" cosmological thesis.
- **Key Claims:**
  - Normative Path: 5,966 cases (88.5%)
  - Volunteer Path: 773 cases (11.5%)
- **Connections TO:** CONSC-028, CONSC-005, SWED-003, CONSC-032, CONSC-034
- **Connected FROM:** CONSC-035, CONSC-036, CONSC-050, CONSC-053

### CONSC-032: Volunteer Soul Path: Commissioning Moment Phenomenon
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.772)
- **Definition:** Distinct NDE pattern (11.5%) where experiencers are "sent back" to fulfill a specific mission.
- **Key Claims:**
  - Sent back involuntarily: 52.6%
  - Higher life review rate: 36.5% vs. 18.6% normative
  - Return Choice: χ² = 768.95, Cramér's V = 0.338
- **Connections TO:** CONSC-031, CONSC-002, CONSC-013, CONSC-028, CONSC-035
- **Connected FROM:** CONSC-035, CONSC-036, CONSC-037, CONSC-038, CONSC-039, CONSC-048

### CONSC-033: Normative Path: Four-Stage Sequential Analysis (40% Canonical, 0% Disorder)
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.745)
- **Definition:** Statistical analysis showing 40% follow canonical sequence, 0% showed unusual ordering.
- **Key Claims:**
  - Canonical sequence: 40.0%
  - Unusual ordering: 0% (validates sequential architecture)
  - Stage breakdowns: OBE 55%, Tunnel 23.2%, Being of Light 92.9%
- **Connections TO:** CONSC-028, SWED-003, CONSC-021, CONSC-034
- **Connected FROM:** CONSC-034

### CONSC-034: Restorative Incarnation Path: Violent Death Correlation Validated (>70%)
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** ✅ **RESTORED** - Valid DOPS external sources
- **Definition:** DOPS statistical analysis validates >70% violent death correlation.
- **Key Claims:**
  - Violent death rate: >70%
  - Birthmark prevalence: 30-35%
  - Birthmark verification: 88%
  - Global solution rate: 67-73%
- **Source Chain:** DOPS Case Verification document, Stevenson/Tucker publications, UVA DOPS database
- **Connections TO:** CONSC-002, CONSC-030, CONSC-005, CONSC-020
- **RESTORATION NOTE:** This node was incorrectly removed because it shared ID range with invalidated report nodes. However, its actual sources are valid external DOPS research, not the invalidated internal analyses.

### CONSC-035: Volunteer Soul Path: Machine Learning Predictive Validation (74.5% Accuracy)
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.8)
- **Definition:** ML analysis demonstrates volunteer path can be predicted from NDE phenomenology alone.
- **Key Claims:**
  - ML accuracy: 74.5%
  - Top predictor: significant_guidance (0.437)
- **Connections TO:** CONSC-032, CONSC-031, CONSC-036
- **Connected FROM:** CONSC-036, CONSC-037, CONSC-038

### CONSC-036: Volunteer Soul Path: Demographic Non-Prediction
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.8)
- **Definition:** Volunteer soul pathway is NOT predicted by demographics.
- **Connections TO:** CONSC-035, CONSC-032, SWED-003

### CONSC-037: Volunteer Soul Path: Enhanced Transformation Outcomes (d = 0.59)
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.775)
- **Definition:** Volunteer souls exhibit higher transformation rates.
- **Key Claims:**
  - Transformation score: 4.49 vs 2.90 (Cohen's d = 0.59)
  - No fear of death: +23.2%
  - Major value shifts: +30.4%
- **Connections TO:** CONSC-032, CONSC-035, CONSC-028, CONSC-039

### CONSC-038: Telepathic Communication: Key Volunteer Soul Discriminator (V = 0.261)
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.738)
- **Definition:** Telepathic communication mode is significant predictor of volunteer path.
- **Key Claims:**
  - Telepathic: Volunteer 58.6% vs Normative 37.3%
  - χ² = 458.57, Cramér's V = 0.261
- **Connections TO:** CONSC-032, CONSC-035, CONSC-039, CONSC-026

### CONSC-039: Volunteer Soul Mission Typology: Ten Archetypal Categories
- **Domain:** CONSC
- **Node Type:** evidence
- **Status:** validated (confidence: 0.643)
- **Definition:** Content analysis reveals 10 primary mission categories.
- **Key Claims:**
  - Writing/Creative: 30.1%
  - Work/Profession: 26.5%
  - Teaching/Sharing: 18.1%
  - 89.3% lack explicit mission details
- **Connections TO:** CONSC-032, CONSC-037, CONSC-038, SWED-006

---

## External References to Removed Nodes

These nodes contain references to removed nodes that need updating:

### In Main Nodes Section:
1. **CONSC-002** (line ~567): `target: CONSC-034` - references Restorative Path validation
2. **CONSC-003** (line ~692): `target: CONSC-023` - references life review analysis

### In Extended Nodes Section:
3. **CONSC-046** (line ~17125): `target: CONSC-034` - references Restorative Path
4. **CONSC-047** (line ~17206): `target: CONSC-034` - contextualizes SOCS bias
5. **CONSC-048** (line ~17335): `target: CONSC-032` - parallels Commissioning Moment
6. **CONSC-050** (line ~17518): `target: CONSC-031` - supports 11.5% Volunteer estimate
7. **CONSC-053** (line ~17783): `target: CONSC-031` - "Updates earlier 11.5% Volunteer estimate"

---

## Notes for Future Re-Integration

When the new research papers are processed:

1. **Conceptual Framework Theory nodes** (CONSC-021 through CONSC-030) dealt with:
   - Being of Light encounters and their properties
   - Life review characteristics
   - Cultural/religious variation in NDE phenomenology
   - Belief correction patterns

2. **Threefold Path nodes** (CONSC-031 through CONSC-034) dealt with:
   - Pathway distribution (Normative/Volunteer/Restorative)
   - Four-stage sequential analysis
   - Violent death correlation for Restorative path

3. **Volunteer Soul Profile nodes** (CONSC-035 through CONSC-039) dealt with:
   - ML predictive validation
   - Demographic non-prediction
   - Transformation outcomes
   - Communication patterns
   - Mission typology

4. **Statistics to potentially restore/correct:**
   - 11.5% Volunteer path figure (CONSC-031, referenced by CONSC-053)
   - 88.5% Normative path figure
   - 61.8% Unknown Presence identification
   - 84.8% No external condemnation
   - 74.5% ML accuracy
   - Various effect sizes and chi-square values

---

## Preservation Note

The node IDs CONSC-031-033, 035-039 should be reserved and reused when the corrected findings are integrated. This maintains traceability between the original (incorrect) nodes and their corrected replacements.

Note: CONSC-021-030 were REPLACED (not simply removed) with new content from valid documents during the same session.

**Total Nodes Removed:** 8 (CONSC-031-033, 035-039)  
**Total Nodes REPLACED:** 10 (CONSC-021-030 with new content)  
**Total Nodes RESTORED:** 1 (CONSC-034)
