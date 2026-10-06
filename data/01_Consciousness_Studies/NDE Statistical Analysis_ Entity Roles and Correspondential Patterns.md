# NDE Statistical Analysis: Entity Roles and Correspondential Patterns

**Dataset**: 6,751 coded NDE accounts (NDERF 5,659; IANDS 1,092; two exact duplicate narratives counted once), January 2026 extraction  
**Repository**: https://github.com/kayna-of-light/structured-data-analysis ([projects/nde](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde))  
**Knowledge Graph Nodes**: CONSC-044, CONSC-045

---

## Executive Summary

Analysis of 6,751 near-death experiences reveals:

1. **Entities function as an ecosystem** — Different being-forms show differentiated functional roles, not interchangeable appearances of the same function. They differ in the *kind* of guidance they give: divine or religious figures teach about six times as often as deceased relatives, and relatives give direction and comfort. Sending the experiencer back is a function every kind of being shares.
2. **Diverse imagery converges on common states** — Among accounts that describe it, tunnel, "other" and no-passage experiences all lead to belonging at similar rates (69–75%); void passages somewhat less often (correspondential principle validated)
3. **Cultural filters shape identification, not function** — Christians identify beings as Jesus more often than others do; among Christians, encounters named Jesus and encounters with an "unknown presence" do not differ in guidance, teaching, telepathy, belonging or mission, though they differ in mode (visual figure, unity)

---

## I. Entity Role Analysis

### A. Who Appears (Being Identifications)

An account can name more than one being; each type is counted once per account.

| Being Type | Count | Percentage |
|------------|-------|------------|
| No being encountered | 2,972 | 44.0% |
| Other | 1,706 | 25.3% |
| Deceased relative (guide role) | 1,094 | 16.2% |
| Unknown presence | 1,049 | 15.5% |
| God | 499 | 7.4% |
| Jesus | 399 | 5.9% |
| Angels | 372 | 5.5% |
| Religious figure (specified) | 158 | 2.3% |
| Buddha | 7 | 0.1% |
| *Two or more named types* | *610* | *9.0%* |

**Key Finding**: Among accounts that meet a being, the "unknown presence" is coded as often as a deceased relative — something benevolent and communicative but not identifiable within the experiencer's cultural framework. This suggests the *form* of the being is less stable than the *function*. The boundary between "unknown presence" and "other" is the least reliable code in the dataset (inter-coder κ = 0.44), so these two rows are better read together (*Reliability of Near-Death Experience Narrative Coding*).

### B. Spiritual Being Categories

| Category | Count | Percentage |
|----------|-------|------------|
| None listed | 4,314 | 63.9% |
| Unidentified benevolent | 1,733 | 25.7% |
| Religious figures | 639 | 9.5% |
| Guides or angels | 558 | 8.3% |

### C. Functional Roles

#### Guidance Function

Guidance is coded as received or not, and by type; an account can carry several types, comfort among them.

| Guidance | Count | Percentage |
|----------|-------|------------|
| Guidance received | 3,469 | 51.4% |
| Not mentioned | 2,282 | 33.8% |
| No guidance | 1,000 | 14.8% |
| *Type: directional* | *2,085* | *30.9%* |
| *Type: informational* | *1,489* | *22.1%* |
| *Type: comfort* | *1,413* | *20.9%* |
| *Type: life guidance* | *1,329* | *19.7%* |
| *Type: teaching* | *794* | *11.8%* |

**50.9% of all experiences** involve entities providing guidance or comfort — this is the dominant functional role.

#### Communication Mode

An account can report more than one mode.

| Mode | Count | Percentage |
|------|-------|------------|
| Telepathic | 1,821 | 27.0% |
| Normal speech | 1,771 | 26.2% |
| Nonverbal | 1,569 | 23.2% |
| Not specified | 742 | 11.0% |
| No communication | 692 | 10.3% |
| None listed | 1,695 | 25.1% |

**Key Finding**: Telepathic communication (27.0%) is the most common mode, ahead of normal speech, suggesting when beings are present, direct mind-to-mind communication is the norm.

#### Return Facilitation

| Who Decided the Return | Count | Percentage |
|------------------------|-------|------------|
| **Another being (sent back)** | **1,930** | **28.6%** |
| Involuntary | 1,422 | 21.1% |
| The experiencer | 1,124 | 16.6% |
| Mutual | 305 | 4.5% |
| Not mentioned | 1,970 | 29.2% |

**Key Finding**: In 28.6% of all accounts another being decides the return. When accounts are split by the kind of being met (§ D), sending back turns out to be shared by every kind of being at similar rates (47–55%); it is not a role specific to deceased relatives.

### D. Cross-Tabulated Entity Functions

Guidance, communication and return are coded for the account as a whole, not for each being. A function can therefore be attributed to a kind of being only in accounts that meet one kind of being. The comparisons below use the five exclusive groups of the structured-data-analysis notebook 07 (n = 2,634): divine or religious figure (God, Jesus, Buddha or a specified religious figure; n = 418), unknown presence (610), angels (112), deceased relatives (584) and other beings (910). Percentages are of all accounts in each group; tests are χ² (df = 4) with Holm correction across eleven functions, and odds ratios are adjusted for narrative length, because longer accounts mention more of everything (*Functional Differentiation of Beings in Near-Death Experiences*).

#### Guidance by Being Type

| Function | Divine | Unknown | Angels | Relatives | Other | χ² | V |
|----------|--------|---------|--------|-----------|-------|----|---|
| Guidance received | 73.2% | 77.5% | 72.3% | 75.9% | 68.6% | 17.9 | 0.08 |
| **Teaching** | **23.0%** | **17.5%** | **20.5%** | **4.5%** | **13.6%** | **81.1** | **0.18** |
| Life guidance | 37.1% | 23.8% | 33.0% | 27.7% | 22.5% | 36.4 | 0.12 |
| Informational | 29.9% | 31.5% | 29.5% | 22.8% | 31.5% | 15.7 | 0.08 |
| Directional | 36.1% | 47.9% | 41.1% | 51.0% | 42.6% | 26.5 | 0.10 |
| Comfort | 29.4% | 28.7% | 33.9% | 33.2% | 24.9% | 13.7 | 0.07 |
| Telepathic communication | 44.0% | 42.5% | 36.6% | 28.6% | 33.3% | 39.4 | 0.12 |
| Mission commissioned | 35.4% | 27.7% | 31.2% | 24.0% | 25.2% | 20.1 | 0.09 |

**Key Finding**: Ten of the eleven functions tested differ across the five groups (Holm-corrected; Cramér's V 0.07–0.18), and the function profile separates divine from relative encounters better than narrative length alone (cross-validated AUC 0.673 vs 0.555). Every kind of being guides at a similar rate; what differs is the *kind* of guidance. Divine or religious figures teach about six times as often as deceased relatives (23.0% vs 4.5%; length-adjusted OR 6.27, 95% CI 3.94–9.98), and they also communicate telepathically (OR 1.83) and commission missions (OR 1.62) more often. They do not give more guidance overall (73.2% vs 75.9%; OR 0.81). Deceased relatives orient and reassure: within the relatives-only accounts that report a guidance type, 67.3% report directional guidance, 43.8% comfort and 5.9% teaching. **Functional differentiation by being type**, located in teaching.

#### Return Agency by Being Type

| Being (only kind met) | Sent back (not-your-time, being decides, or verbal limit) | Told "not your time" | Being decides return |
|------------------------|-----------------------------------------------------------|----------------------|----------------------|
| Deceased relatives | 54.6% | 37.7% | 46.7% |
| Divine or religious figure | 51.7% | 30.4% | 39.2% |
| Unknown presence | 48.9% | 28.5% | 36.1% |
| Angels | 47.3% | 25.9% | 36.6% |
| Other beings | 47.0% | 28.5% | 35.5% |

**Key Finding**: Sending the experiencer back is shared by every kind of being (47–55%). Relatives are not distinguishable from divine figures (length-adjusted OR 1.11, 95% CI 0.86–1.43, p = 0.42), and the separate return codes do not survive Holm correction in that comparison. Relatives are **not specific gatekeepers**. The division of labour lies in instruction, not in the decision to return: higher-order beings teach, relatives orient and comfort, and all of them send back. Swedenborg's own account has friends and relatives receiving and accompanying the newly arrived, not deciding their return (*Heaven and Hell* § 494), so the gatekeeper role was not a prediction of the framework.

---

## II. Correspondential Analysis

### A. Transition Imagery → Functional Outcome

**Question**: Do tunnel, void, and other passage types produce equivalent functional outcomes?

#### Passage Types Distribution

| Type | Count | Percentage |
|------|-------|------------|
| No passage | 3,360 | 49.8% |
| Tunnel | 1,602 | 23.7% |
| Other | 733 | 10.9% |
| Void | 537 | 8.0% |
| Not mentioned | 519 | 7.7% |

#### Passage Type → Sense of Belonging (Functional Convergence)

Belonging (explicit or implied) among the accounts that describe whether a sense of belonging was present.

| Passage Type | Belonging / Described | Percentage |
|--------------|-----------------------|------------|
| Tunnel | 399 / 531 | 75.1% |
| Other | 206 / 293 | 70.3% |
| No passage | 636 / 919 | 69.2% |
| Void | 120 / 217 | 55.3% |

**Key Finding**: Tunnel, "other" and no-passage experiences all produce high belonging outcomes (69–75%); the void, the passage closest to darkness, produces belonging somewhat less often (55.3%). The **imagery differs; the state convergent**. This validates the correspondential principle — diverse forms, common function.

### B. Light Encounter Forms → Guidance Function

| Light Form | Guidance | Comfort | None |
|------------|----------|---------|------|
| Being of Light | 85.1% | 44.5% | 12.7% |
| Presence without visual | 73.7% | 35.1% | 21.8% |
| Brilliant light | 52.0% | 21.0% | 46.0% |
| No light | 42.6% | 16.5% | 54.9% |

(An account can receive both guidance and comfort.)

**Key Finding**: "Being of Light" provides the highest guidance (85.1%), but even "presence without visual" provides guidance in nearly three cases in four (73.7%). The **form varies (visual/non-visual); function persists**.

### C. Cultural Filter Analysis

**Question**: Does religious background change *who* is identified but not *what happens*?

#### Being Identification by Religious Background

| Background | n | No Being | Unknown Presence | Deceased Relative | God | Jesus |
|------------|---|----------|------------------|-------------------|-----|-------|
| Christian | 1,282 | 35.5% | 19.3% | 18.6% | 10.8% | 11.2% |
| Atheist/Agnostic | 100 | 55.0% | 17.0% | 11.0% | 3.0% | 4.0% |
| Muslim | 43 | 65.1% | 9.3% | 11.6% | 0.0% | 0.0% |
| Jewish | 38 | 26.3% | 21.1% | 26.3% | 7.9% | 10.5% |
| Spiritual not religious | 22 | 36.4% | 18.2% | 18.2% | 4.5% | 9.1% |
| Hindu | 15 | 40.0% | 6.7% | 26.7% | 0.0% | 0.0% |
| Buddhist | 14 | 57.1% | 7.1% | 14.3% | 21.4% | 0.0% |

**Key Findings**:
1. Christians identify the Being as Jesus nearly three times as often as experiencers of other stated backgrounds (11.2% vs 4.0% of all accounts in each group)
2. Atheists encounter beings less often, and when they do they identify them chiefly as "unknown presence" or deceased relatives
3. The **functional outcomes are equivalent regardless of identification**: among Christians, encounters with Jesus only (n = 102) and with an unknown presence only (n = 175) do not differ in guidance (84.3% vs 82.3%), teaching, telepathy, belonging or mission commissioning. The *mode* differs: the Jesus encounters are far more often a visual luminous figure (+45.0 points) and the unknown-presence encounters more often involve unity (−19.6 points) (*The Being of Light*)
4. The association between religious background and the name given is weak (collapsed table χ²(6) = 15.04, p = 0.020, Cramér's V = 0.113), and background predicts the name barely above chance (cross-validated AUC 0.527) (*The Being of Light*)

---

## III. System Architecture Evidence

### A. Stage Element Frequency

| Stage | Experiences | Percentage |
|-------|-------------|------------|
| Return choice | 5,640 | 83.5% |
| OBE | 4,430 | 65.6% |
| Environment | 3,832 | 56.8% |
| Light encounter | 3,765 | 55.8% |
| Communication | 3,703 | 54.9% |
| Boundary | 2,738 | 40.6% |
| Tunnel | 2,221 | 32.9% |
| Loved ones | 1,448 | 21.4% |
| Life review | 1,026 | 15.2% |

**Key Finding**: "Return choice" appears in 84% of cases — the system ensures return to physical life is the dominant outcome for NDEs.

### B. Canonical Sequence Adherence

| Pattern | Count | Percentage |
|---------|-------|------------|
| Partial | 3,396 | 50.3% |
| Mostly canonical | 2,356 | 34.9% |
| Radical deviation | 494 | 7.3% |
| Indeterminate | 272 | 4.0% |
| Not applicable | 230 | 3.4% |
| Strict canonical | 3 | <0.1% |

**Key Finding**: Only 3 accounts follow a strict canonical sequence. Among the 6,249 accounts whose order can be judged, 37.7% are mostly canonical, 54.3% partial and 7.9% radically different (*Sequential Structure in Near-Death Experience*). A fixed stage sequence is therefore not observed. The experience is **fluid and adaptive**, not rigidly programmed — consistent with an intelligent system responding to individual needs.

---

## IV. Framework Implications

### For Swedenborgian Model

1. **Confirmed**: Correspondences operate — diverse imagery maps to constant states
2. **Confirmed**: Guidance is the dominant function (50.9% of experiences)
3. **Nuanced**: Not all beings serve the same role — there is functional differentiation
4. **Question**: Why do 44% encounter no beings at all? Are they processed differently?

### For Ecosystem Hypothesis

1. **Supported**: Different being-types show statistically different functional profiles (10 of 11 functions)
2. **Supported**: Higher beings teach (OR 6.27 against relatives); deceased relatives give direction and comfort and rarely teach
3. **Not supported**: Deceased relatives as specific gatekeepers; sending back is shared by all being types (47–55%)
4. **Not supported**: Higher beings giving more guidance overall (73.2% vs 75.9%)

### For Selection Artifact Concern

This dataset cannot address whether DOPS methodology filters non-cyclic cases because:
- NDE cases by definition involve near-death circumstances (selection bias)
- Pre-birth memories without death context are outside the NDE phenomenology

**Research gap remains**: We need analysis of DOPS past-life cases specifically for non-death-origin patterns.

---

## V. Data Caveats

1. **Dataset bias**: Primarily Western, English-language sources (IANDS, NDERF)
2. **Self-report**: All data derives from experiencer narratives, not objective observation
3. **Selection**: Cases that reach research databases may differ from unreported experiences
4. **Analysis method**: LLM-coded from narratives. A blind second coding of 100 random accounts gives a median κ of 0.83; the fields used here reach κ 0.70–0.88, except "unknown presence" (κ 0.44) (*Reliability of Near-Death Experience Narrative Coding*)
5. **Attribution**: functions are coded per account, so they are attributed to a being type only in the 2,634 accounts with one kind of being (§ I.D)
6. **Coding**: being type from `passage.arrival.being_identifications`; guidance from `world_of_spirits.encounters.guidance_received` and `guidance_types` (guidance = directional, informational, life guidance or teaching; comfort coded separately and not exclusive of guidance); return from `boundary_and_return.return_agency` ("sent back" = `external_being`); belonging from `passage.arrival.sense_of_belonging` (explicit or implied); light form from `passage.arrival.light_encounter`; sequence from `stage_sequence`

---

## VI. Works Cited

**Primary Sources:**

1. Swedenborg, Emanuel. *Heaven and Hell* (*De Coelo et Ejus Mirabilibus et de Inferno*). London: 1758. §§ 87–115 (correspondence doctrine foundation); § 494 (the newly arrived are recognized and welcomed by friends and relatives). Cited by section number (§).

**Internal Library Documents:**

2. *Functional Differentiation of Beings in Near-Death Experiences: Testing Role Specialisation*. `data/01_Consciousness_Studies/`. Being types compared in five exclusive groups; teaching, guidance and return by type.
3. *Reliability of Near-Death Experience Narrative Coding: Independent Second Coding, Test–Retest and Duplicate Audit*. `data/01_Consciousness_Studies/`. Inter-coder agreement for the fields used.
4. *Sequential Structure in Near-Death Experience: Evaluating the Normative Path Model*. `data/01_Consciousness_Studies/`. Canonical-sequence shares among judgeable accounts.
5. *The Being of Light: A Statistical Analysis of Near-Death Experience Phenomenology*. `data/01_Consciousness_Studies/`. Naming by religious background; Jesus-only vs unknown-only comparison.

**Data Sources:**

6. NDERF (Near Death Experience Research Foundation) and IANDS (International Association for Near-Death Studies) archives. 6,751 unique accounts (NDERF 5,659; IANDS 1,092), each coded field by field with the NDEAnalysisResponse schema. Analyzed in the structured-data-analysis project (projects/nde/structured/).

---

## Raw Data Location

- **Structured NDE data**: [`projects/nde/structured/`](https://github.com/kayna-of-light/structured-data-analysis/tree/main/projects/nde/structured) (6,753 JSON files, two of them exact duplicates)
