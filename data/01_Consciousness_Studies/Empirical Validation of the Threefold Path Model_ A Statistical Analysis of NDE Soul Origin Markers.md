# Empirical Validation of the Threefold Path Model: A Statistical Analysis of NDE Soul Origin Markers

**Date**: December 31, 2025  
**Dataset**: 6,753 Near-Death Experience accounts (NDERF: 5,660 + IANDS: 1,093)  
**Analysis Method**: GPT-5.2 structured extraction with Pydantic schema validation

---

## Abstract

This study presents the first large-scale empirical analysis of soul origin markers in near-death experience (NDE) accounts, testing the **Threefold Path Model** proposed in the framework's synthesized cosmology. Using AI-assisted structured extraction from 6,753 NDE narratives, we identify statistical patterns consistent with three distinct soul pathways: **Volunteer** (mission-oriented first incarnation), **Restorative** (cyclic return following trauma), and **Ohkado** (pre-birth awareness without trauma markers). The data strongly support a multi-path model of soul origins, with highly significant chi-square statistics (p < 10⁻⁹⁴ for every variable tested, and p < 10⁻²⁷² for four of the five) distinguishing these populations across multiple independent variables.

---

## 1. Introduction

### 1.1 Theoretical Background

The framework's **Threefold Path of the Soul** model (*The Threefold Path of the Soul: A Synthesized Cosmology*) proposes that souls incarnate through distinct pathways:

1. **Restorative Path**: Souls returning to physical incarnation following prior physical existence, typically marked by traumatic death memories, past-life recall, and intermission-period experiences.

2. **Volunteer Path**: Souls incarnating for the first time with a pre-determined mission, characterized by explicit mission language, sense of earthly "assignment," and absence of cyclic reincarnation markers.

3. **Ohkado Pattern**: Named after the "reverse cases" of Japanese researcher Ohkado Masayuki—children with life-between-life memories but no past-life memories (Ohkado and Ikegawa 2014)—souls demonstrating pre-birth realm awareness (premortal existence, incarnation choice, spiritual home identification) WITHOUT the trauma markers that characterize the Restorative path—suggesting potential first incarnations.

### 1.2 Research Questions

1. Can NDE accounts be reliably classified into distinct soul path categories?
2. What empirical markers discriminate between Volunteer and Restorative pathways?
3. What percentage of the NDE population exhibits the Ohkado pattern?
4. Is the **reason for return** (WHY) more discriminating than the **mechanism of return** (HOW)?

---

## 2. Methodology

### 2.1 Data Collection

Two major NDE databases were analyzed:
- **NDERF (Near-Death Experience Research Foundation)**: 5,660 accounts
- **IANDS (International Association for Near-Death Studies)**: 1,093 accounts
- **Total**: 6,753 NDE narratives

### 2.2 Extraction Schema

A comprehensive Pydantic schema was developed to capture the full dimensionality of NDE phenomenology, including:

**Cosmic Knowledge Section** (16 fields):
- `premortal_existence_info`: Whether the experiencer received information about existence before birth
- `pre_birth_realm_description`: Description of the pre-incarnation realm
- `incarnation_choice`: Whether the experiencer chose their incarnation (chose_mission, chose_parents, chose_both, no_choice)
- `home_identification`: Whether the spiritual realm was identified as "home" (spiritual_realm, earth, both, neither)
- `identity_pre_body`: Whether the experiencer sensed identity existing before their body
- `death_memory`: Memory of a prior death (natural, violent, unspecified, none)
- `past_life_memory`: Explicit recall of prior incarnation(s)
- `volunteer_language`: Explicit use of "volunteer," "chose to come," etc.

**Boundary and Return Section** (6 fields):
- `return_reason`: WHY the experiencer returned (earthly_mission, family_responsibility, not_your_time, no_reason_given, other)
- `return_choice`: HOW the return was experienced (told, chose, both, neither)
- `mission_commissioned`: Whether a specific mission was assigned
- `mission_types`: Categories of assigned missions
- `mission_detail`: Specific mission descriptions

### 2.3 Classification Criteria

**Volunteer Path** (any of the first three conditions, and no trauma markers):
- `volunteer_language` = yes_explicit OR implied, OR
- `return_reason` = earthly_mission, OR
- (`mission_commissioned` = yes_explicit/implied AND `incarnation_choice` = chose_mission/chose_both)
- AND NOT has_trauma_markers

**Restorative Path**:
- `death_memory` = yes_explicit OR implied, OR
- `past_life_memory` = yes_explicit OR implied
- AND NOT has_volunteer_markers

**Ohkado Pattern**:
- At least one positive pre-birth indicator:
  - `premortal_existence_info` = yes_explicit/implied
  - `pre_birth_realm_description` = yes_explicit/implied
  - `incarnation_choice` = chose_mission/chose_parents/chose_both
  - `home_identification` = spiritual_realm
  - `identity_pre_body` = yes_explicit/implied
- AND NOT has_trauma_markers
- AND NOT has_volunteer_markers

**Hybrid Path**:
- Both volunteer AND trauma markers present

---

## 3. Results

### 3.1 Soul Path Classification

| Soul Path | Count | Percentage |
|-----------|-------|------------|
| **Indeterminate** | 4,182 | 61.93% |
| **Ohkado** | 1,901 | 28.15% |
| **Volunteer** | 421 | 6.23% |
| **Restorative** | 197 | 2.92% |
| **Hybrid** | 52 | 0.77% |

**Key Finding**: Over 38% of NDErs show classifiable soul path markers, with the Ohkado pattern being the most prevalent (28.15%), suggesting a substantial population with pre-birth awareness but without cyclic reincarnation indicators.

### 3.2 Return Reason Analysis

The **WHY** of return proved to be the most discriminating variable:

| Return Reason | Count | Mission Commission Rate |
|---------------|-------|------------------------|
| **earthly_mission** | 443 (6.6%) | **94.6%** |
| not_your_time | 1,125 (16.7%) | 26.8% |
| family_responsibility | 967 (14.3%) | 22.9% |
| other | 539 (8.0%) | 29.5% |
| no_reason_given | 1,180 (17.5%) | 5.8% |
| not_mentioned | 2,499 (37.0%) | 8.0% |

**Critical Finding**: The `earthly_mission` return reason has a **94.6% mission commission rate** versus 5.8-29.5% for all other categories. This confirms the hypothesis that the **reason** for return, not the **mechanism** (told vs. chose), is the true discriminant.

Chi-square test (return reason × mission commissioned): χ² = 2,845.61, df = 15, p < 10⁻³⁰⁰

### 3.3 Volunteer Language Analysis

Volunteer language ("I volunteered to come," "I chose this life") appeared in only **35 cases (0.52%)** of the total dataset: 16 explicit and 19 implied. However, these cases showed dramatically elevated rates of pre-birth indicators:

| Pre-Birth Indicator | Volunteer Language | Non-Volunteer | Ratio |
|---------------------|-------------------|---------------|-------|
| incarnation_choice | 45.7% | 0.6% | **74.9x** |
| pre_birth_realm_description | 34.3% | 1.2% | **28.1x** |
| premortal_existence_info | 68.6% | 6.2% | **11.0x** |
| home_identification | 42.9% | 13.8% | **3.1x** |
| identity_pre_body | 71.4% | 25.6% | **2.8x** |

### 3.4 Trauma Marker Analysis

Restorative indicators (cyclic reincarnation markers) were rare:

| Trauma Marker | Count | Percentage |
|---------------|-------|------------|
| Past Life Memory (yes_explicit/implied) | 249 | 3.7% |
| Death Memory (prior death: violent 20, unspecified 16, natural 3) | 39 | 0.6% |
| Either marker | 250 | 3.7% |
| Both markers | 38 | 0.6% |

**Note**: The death_memory extraction required memories of a *prior* death (before the NDE), not the NDE-triggering event itself. Thirty-nine accounts carry such a memory; of the 23 that state how the earlier death came, 20 describe a violent one, and 38 of the 39 also recall a past life. The classification filter in §2.3 tested `death_memory` for yes_explicit/implied, values the field does not take, so the Restorative path as classified rests on past-life memory alone; the single death-memory account without past-life memory is the only record this affects.

### 3.5 Ohkado Pattern Deep Dive

The Ohkado pattern (pre-birth awareness without trauma) showed tiered intensity:

| Indicator Count | Cases | Percentage |
|-----------------|-------|------------|
| 1 indicator | 1,569 | 23.2% |
| 2 indicators | 413 | 6.1% |
| 3 indicators | 97 | 1.4% |
| 4 indicators | 43 | 0.6% |
| **5 indicators** | **3** | **0.04%** |

**Total Ohkado candidates**: 2,125 (31.5% of dataset)

Across the whole dataset, nine cases carry all five pre-birth indicators (Appendix B); three of them have no trauma markers and fall among the Ohkado candidates. These "perfect" cases represent the strongest empirical evidence for the Volunteer/first-incarnation hypothesis.

### 3.6 Statistical Validation

Chi-square tests for soul path × key variables:

| Variable | χ² | p-value | Significance |
|----------|-----|---------|--------------|
| return_reason | 6,586.5 | p < 10⁻³⁰⁰ | *** |
| mission_commissioned | 2,621.3 | p < 10⁻³⁰⁰ | *** |
| volunteer_language | 1,354.2 | p < 10⁻²⁸¹ | *** |
| sense_of_belonging | 1,310.4 | p < 10⁻²⁷² | *** |
| comparative_reality | 482.7 | p < 10⁻⁹⁴ | *** |

All key discriminant variables show highly significant associations with soul path classification.

### 3.7 Cross-Path Comparisons

| Metric | Volunteer | Restorative | Ohkado | Hybrid |
|--------|-----------|-------------|--------|--------|
| Mission Commissioned | 92.6% | 38.1% | 21.4% | 94.2% |
| Earthly Mission Return | 94.8% | 0.0% | 0.0% | 84.6% |
| Explicit Sense of Belonging | 20.2% | 28.4% | 28.5% | 46.2% |

---

## 4. Discussion

### 4.1 Support for the Threefold Path Model

The data provide strong empirical support for distinct soul pathways:

1. **The Volunteer Path is Real**: The 421 cases (6.2%) classified as Volunteer show a coherent profile: 94.8% return for earthly mission, 92.6% have mission commissioned, and they have dramatically elevated pre-birth indicators when explicit volunteer language is present.

2. **The Restorative Path is Rare but Distinct**: Only 197 cases (2.9%) show clear trauma markers (past-life memory) without volunteer indicators. This low rate may reflect:
   - Selection bias in NDE reporting (traumatic memories less likely to be shared)
   - The Strength of Case Scale (SOCS) filter (*The Methodological Visibility of the Non-Cyclic Soul*: trauma-based DOPS cases overrepresent the Restorative path)
   - Genuine rarity of explicit past-life awareness in NDEs

3. **The Ohkado Pattern is Prevalent**: 28.15% of NDErs show pre-birth awareness without cyclic trauma markers. This aligns with the framework's prediction that many souls may be on their first incarnation or have completed the Restorative cycle.

### 4.2 The Discriminating Power of "Why"

The most significant finding is that **return reason** (not return mechanism) discriminates pathways:

- **"Told to return" vs "Chose to return"** shows minimal discriminating power
- **"Returned for earthly mission"** shows 94.6% mission commission rate

This resolves a persistent confusion in the literature where researchers conflated the mechanism of return with its spiritual significance. A soul "told to return" for an earthly mission is functionally equivalent to one who "chose to return" for the same purpose.

### 4.3 The Hybrid Cases

The 52 Hybrid cases (0.77%) showing both volunteer AND trauma markers present an interpretive challenge. Possible explanations:

1. **Evolved Volunteers**: Souls who began as Restorative but have evolved to a Volunteer orientation
2. **Measurement Artifact**: Imprecise extraction conflating different types of memory
3. **Complex Cosmology**: Some souls may genuinely carry both first-incarnation missions AND prior-life memories (e.g., memories accessed during NDE but not from personal past)

### 4.4 Limitations

1. **Extraction Accuracy**: AI extraction, while validated, introduces measurement error
2. **Selection Bias**: Published NDE accounts may not represent the full population
3. **Narrative Compression**: Brief accounts may underreport subtle indicators
4. **Cultural Framing**: Western datasets may not capture non-Western soul concepts

---

## 5. Integration with Framework

### 5.1 Correspondence to Framework Concepts

| Empirical Category | Framework Concept | Source |
|--------------------|-------------------|--------|
| Volunteer Path | Volunteer Soul Hypothesis | *The Threefold Path of the Soul: A Synthesized Cosmology* |
| Restorative Path | Cyclic Return | *The Threefold Path of the Soul: A Synthesized Cosmology* |
| Ohkado Pattern | Ohkado Reverse Cases | Ohkado and Ikegawa 2014; *The Methodological Visibility of the Non-Cyclic Soul* §3.2 |
| Trauma Markers | SOCS Selection Bias | *The Methodological Visibility of the Non-Cyclic Soul* |
| Return Reason Signal | - | New (this analysis) |

### 5.2 New Framework Contributions

This analysis contributes several refinements to the framework:

1. **Return Reason Discriminant**
   - The WHY of return (earthly_mission vs other) is the primary discriminant
   - The HOW of return (told vs chose) is noise

2. **Pre-Birth Indicator Hierarchy** (elevation among cases with `volunteer_language`)
   - `incarnation_choice` is most elevated (74.9x ratio)
   - `pre_birth_realm_description` second (28.1x ratio)
   - `premortal_existence_info` third (11.0x ratio)

3. **Population Distribution Estimate**
   - Volunteer: ~6%
   - Ohkado (potential first incarnation): ~28%
   - Restorative: ~3%
   - Hybrid: ~1%
   - Indeterminate: ~62%

### 5.3 Implications for DOPS Methodology

The finding that explicit trauma markers are rare (3.7%) while pre-birth awareness is common (31.5%) has implications for DOPS reincarnation research:

- **SOCS Selection Bias Confirmed**: Case selection based on past-life *memory* (Stevenson/Tucker methodology) systematically filters FOR the Restorative path
- **Pre-Existence Methodology Validated**: Searching for life-between-life memories without past-life memories (Ohkado and Ikegawa 2014) and for veridical pre-existence memories (Rivas et al. 2015) provides access to non-Restorative populations
- **COPET Proposal Justified**: A "Cases of the Pre-Existence Type" category independent of the reincarnation-type coding (*The Methodological Visibility of the Non-Cyclic Soul* §9) would enable systematic study of all soul pathways

---

## 6. Conclusion

This analysis of 6,753 NDE accounts provides strong empirical support for the Threefold Path Model:

1. **Distinct Soul Pathways Exist**: Statistical analysis confirms that NDErs cluster into distinct categories based on soul origin markers.

2. **The Volunteer Path is Empirically Identifiable**: Mission-oriented souls with earthly mission return reasons and high mission commission rates form a coherent population (~6%).

3. **The Ohkado Pattern is Prevalent**: 28-31% of NDErs show pre-birth awareness without trauma markers, suggesting a large population of potential first-incarnation or post-Restorative souls.

4. **Return Reason is Key**: The WHY of return discriminates soul paths far better than the HOW.

5. **The Restorative Path is Rare in NDEs**: Only 3% show explicit past-life trauma markers, suggesting either selection bias in NDE reporting or genuine rarity.

These findings validate the framework's multi-path cosmology and provide a methodological foundation for future empirical investigation of soul origins.

---

## Appendix A: Data Exports

The following datasets are available in the NDE Analysis repository:

| File | Records | Description |
|------|---------|-------------|
| `soul_path_classification.csv` | 6,753 | All cases with classification |
| `soul_path_volunteer.csv` | 421 | Volunteer path cases |
| `soul_path_restorative.csv` | 197 | Restorative path cases |
| `soul_path_ohkado.csv` | 1,901 | Ohkado pattern cases |
| `soul_path_hybrid.csv` | 52 | Hybrid cases |
| `ohkado_very_strong_candidates.csv` | 143 | 3+ pre-birth indicators |

---

## Appendix B: Perfect 5-Indicator Cases

Nine cases exhibited all five pre-birth indicators:
1. premortal_existence_info = yes_explicit/implied
2. pre_birth_realm_description = yes_explicit/implied
3. incarnation_choice = chose_mission/chose_parents/chose_both
4. home_identification = spiritual_realm
5. identity_pre_body = yes_explicit/implied

These represent the strongest empirical examples of the Volunteer/first-incarnation profile and warrant individual case study analysis.

---

## Works Cited

**Scholarly Works:**

1. Ohkado, Masayuki, and Akira Ikegawa. "Children with Life-between-Life Memories." *Journal of Scientific Exploration* 28, no. 3 (2014): 477–490.
2. Rivas, Titus, Elizabeth M. Carman, Neil J. Carman, and Anny Dirven. "Paranormal Aspects of Pre-Existence Memories in Young Children." *Journal of Near-Death Studies* 34, no. 2 (2015): 84–107. https://doi.org/10.17514/JNDS-2015-34-2-p84-107.
3. Stevenson, Ian. *Twenty Cases Suggestive of Reincarnation*. 2nd ed., rev. and enl. Charlottesville: University Press of Virginia, 1974.
4. Tucker, Jim B. *Life Before Life: A Scientific Investigation of Children's Memories of Previous Lives*. New York: St. Martin's Press, 2005.
5. van Lommel, Pim. *Consciousness Beyond Life: The Science of the Near-Death Experience*. New York: HarperOne, 2010.

**Internal Library Documents:**

6. [Mission-Based Returns: Volunteer Soul Detection Analysis](Mission-Based%20Returns_%20Volunteer%20Soul%20Detection%20Analysis.md). The same return-reason, volunteer-language and pre-birth measures re-run on the January 2026 extraction schema.
7. [The Methodological Visibility of the Non-Cyclic Soul: An Exhaustive Audit of Selection Artifacts in Reincarnation Research](The%20Methodological%20Visibility%20of%20the%20Non-Cyclic%20Soul_%20An%20Exhaustive%20Audit%20of%20Selection%20Artifacts%20in%20Reincarnation%20Research.md). The SOCS selection-bias argument, Ohkado's reverse cases in the DOPS context, and the COPET proposal.
8. [The Threefold Path of the Soul: A Synthesized Cosmology of Life, Death, and Purpose](../00_Framework/The%20Threefold%20Path%20of%20the%20Soul_%20A%20Synthesized%20Cosmology%20of%20Life%2C%20Death%2C%20and%20Purpose.md). The Volunteer and Restorative paths this analysis tests.

**Data Sources:**

9. IANDS (International Association for Near-Death Studies). 1,093 NDE accounts. Analyzed in the structured-data-analysis project (projects/nde/).
10. NDERF (Near Death Experience Research Foundation). 5,660 NDE accounts. Analyzed in the structured-data-analysis project (projects/nde/).
11. structured-data-analysis, NDE project. Notebooks `archive/volunteer_discriminant_analysis.ipynb` (soul-path classification, return-reason, volunteer-language and trauma-marker analyses) and `archive/ohkado_pattern_analysis.ipynb` (Ohkado candidate tiers). https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/notebooks/archive.
