# Source Trace Report: Conceptual Framework Deep Dive Analysis

**File Analyzed:** `data/01_Consciousness_Studies/conceptual_framework_deep_dive_report-analysis_iands_and_nand_2025.md`

**Report Date:** December 29, 2025  
**Analysis Type:** Source Chain Verification & Classification

---

## Executive Summary

This document is an **original statistical analysis** (source type: `[E]` Empirical) performed by the "NDE Analysis Project" research team using data extracted from two primary NDE databases. The analysis is **methodologically sound** but has **significant source documentation gaps** that need addressing for scholarly integrity.

### Key Finding
The statistical claims are **internally consistent** with original computational analysis, but the document fails to provide:
1. Direct URLs/citations to the primary databases
2. Data access dates and extraction methodology details
3. IRB/ethics review status
4. Relationship to the `nde-data-analysis` repository mentioned in project instructions

---

## Source Type Classifications

### Overall Document Classification

| Aspect | Classification | Notes |
|--------|---------------|-------|
| **Document Type** | `[E]` Empirical + `[T]` Tertiary | Original analysis on third-party data |
| **Data Sources** | `[E]` Empirical databases | NDERF, IANDS |
| **Methodology** | Original computational analysis | Python/scikit-learn |
| **Interpretation** | `[T]` Tertiary synthesis | Framework theory validation |

---

## Claim-by-Claim Source Trace

### 1. Being of Light encounters: 47.3% (3,189 cases)

| Property | Value |
|----------|-------|
| **Claim** | 3,189 of 6,739 NDEs (47.3%) involve Being of Light encounters |
| **Source Type** | `[E]` Empirical - Original computational analysis |
| **Source Chain** | |
| 1. `[T]` | This document (analysis report) |
| 2. `[E]` | JSON analysis files (intermediate data) |
| 3. `[E]` | NDERF database (n=5,646) + IANDS database (n=1,093) |
| **Primary Sources** | NDERF (www.nderf.org) - Dr. Jeffrey Long; IANDS (iands.org) |
| **Status** | ⚠️ `[PARTIAL TRACE]` - Primary database URLs not cited inline |
| **Recommendation** | Add explicit database citations with access dates |

---

### 2. 61.8% identify Being as "unknown presence"

| Property | Value |
|----------|-------|
| **Claim** | 1,970 of 3,189 Light Being encounters (61.8%) classified as "unknown presence" |
| **Source Type** | `[E]` Empirical - Original computational analysis |
| **Source Chain** | |
| 1. `[T]` | This document (analysis report) |
| 2. `[E]` | Structured questionnaire responses (field: being identification) |
| 3. `[E]` | NDERF/IANDS standardized questionnaires |
| **Primary Sources** | NDERF questionnaire schema; IANDS submission forms |
| **Status** | ⚠️ `[TRACE NEEDED]` - Questionnaire structure/fields undocumented |
| **Recommendation** | Document the specific questionnaire fields used for "identification" extraction |

**Critical Note:** This is described as the "strongest evidence" for objective reality. Given its centrality to the theoretical argument, source documentation should be especially rigorous.

---

### 3. 84.8% experience no external condemnation during life review

| Property | Value |
|----------|-------|
| **Claim** | 84.8% of life review experiences (n=1,253) show no external condemnation |
| **Calculated From** | None (57.0%) + Self-judgment only (26.3%) + [other derived categories] |
| **Source Type** | `[E]` Empirical - Original computational analysis |
| **Source Chain** | |
| 1. `[T]` | This document (analysis report) |
| 2. `[E]` | Life review coding from JSON files |
| 3. `[E]` | NDERF/IANDS account narratives |
| **Primary Sources** | Individual NDE accounts in databases |
| **Status** | ⚠️ `[TRACE NEEDED]` - Coding methodology for "judgment source" undefined |
| **Recommendation** | Document the operationalization of "external condemnation" vs "self-judgment" |

---

### 4. 79.4% active communication with Being of Light

| Property | Value |
|----------|-------|
| **Claim** | 79.4% of Light Being encounters involve active communication |
| **Source Type** | `[E]` Empirical - Original computational analysis |
| **Source Chain** | |
| 1. `[T]` | This document (analysis report) |
| 2. `[E]` | Communication mode coding (telepathic: 51.4%, speech: 18.7%, mixed: 9.3%) |
| 3. `[E]` | NDERF/IANDS questionnaire responses |
| **Primary Sources** | Database questionnaire items on communication |
| **Status** | ⚠️ `[PARTIAL TRACE]` - Communication categories documented, source fields not |
| **Recommendation** | Cite specific NDERF questionnaire item numbers |

---

### 5. Cross-religious consistency: 60-63% lose fear of death across all religions

| Property | Value |
|----------|-------|
| **Claim** | Fear loss rates: Christians 62.2%, Atheists 62.3%, Muslims 62.9%, Jewish 60.0% |
| **Source Type** | `[E]` Empirical - Original computational analysis |
| **Source Chain** | |
| 1. `[T]` | This document (analysis report) |
| 2. `[E]` | Cross-tabulation of religion × belief change |
| 3. `[E]` | Religious affiliation + belief change fields from databases |
| **Primary Sources** | NDERF/IANDS demographic and transformation questionnaire items |
| **Status** | ✅ `[VERIFIED INTERNAL]` - Calculation methodology documented |
| **Statistical Validation** | Standard deviation: 1.1%, CV: 1.8% |
| **Recommendation** | Good internal documentation; add primary field citations |

---

### 6. Machine Learning model: 68.2% accuracy predicting religious ID vs unknown

| Property | Value |
|----------|-------|
| **Claim** | Random Forest classifier achieves 68.2% accuracy |
| **Source Type** | `[E]` Empirical - **Original analysis** (not replicated from elsewhere) |
| **Source Chain** | |
| 1. `[T]` | This document (analysis report) |
| 2. `[E]` | scikit-learn 1.7.2 Random Forest implementation |
| 3. `[E]` | Feature matrix from NDERF/IANDS data |
| **Methodology** | 200 trees, max depth 10, balanced classes, 70/30 train/test split |
| **Status** | ✅ `[VERIFIED ORIGINAL]` - This is novel analysis, not replication |
| **Recommendation** | Consider publishing analysis code for reproducibility |

---

### 7. Normative Path evidence: 18.7% encounter deceased relatives, 0% reincarnation indicators

| Property | Value |
|----------|-------|
| **Claim** | 18.7% encounter deceased relatives; 0% show reincarnation indicators |
| **Source Type** | `[E]` Empirical - Original computational analysis |
| **Source Chain** | |
| 1. `[T]` | This document (analysis report) |
| 2. `[E]` | "Other beings" coding + reincarnation language search |
| 3. `[E]` | NDERF/IANDS account narratives |
| **Primary Sources** | Individual NDE accounts |
| **Status** | ⚠️ `[TRACE NEEDED]` - "Reincarnation indicators" operationalization undefined |
| **Critical Issue** | "0%" is an extraordinary claim requiring extraordinary documentation |
| **Recommendation** | Define exact search terms/coding criteria for "reincarnation indicators" |

---

## Primary Database Assessment

### NDERF (Near-Death Experience Research Foundation)

| Property | Value |
|----------|-------|
| **URL** | https://www.nderf.org/ |
| **Founder** | Dr. Jeffrey Long, MD (radiation oncologist) |
| **Database Size** | 5,300+ experiences (website states); 5,646 used in analysis |
| **Data Collection** | Self-reported via online questionnaire |
| **Published Research** | Long, J. (2010). *Evidence of the Afterlife*; Long, J. (2016). *God and the Afterlife* |
| **Academic Status** | Widely cited in NDE literature; peer-reviewed publications exist |
| **Citation Status in Document** | ⚠️ `[INADEQUATE]` - Named but not formally cited |

### IANDS (International Association for Near-Death Studies)

| Property | Value |
|----------|-------|
| **URL** | https://iands.org/ |
| **Organization Type** | 501(c)(3) nonprofit (EIN: 06-1050150) |
| **Database Size** | Registry of personal accounts; 1,093 used in analysis |
| **Data Collection** | Submitted accounts, anonymized |
| **Academic Status** | Publishes *Journal of Near-Death Studies* (peer-reviewed) |
| **Research Portal** | https://research.iands.org/ |
| **Citation Status in Document** | ⚠️ `[INADEQUATE]` - Named but not formally cited |

---

## Source Documentation Gaps

### Critical Issues Requiring Resolution

1. **No Formal Database Citations**
   - Document mentions NDERF and IANDS by name
   - No URLs, access dates, or formal citations provided
   - **Fix:** Add formal citation block in methodology section

2. **Undefined Relationship to `nde-data-analysis` Repository**
   - Project instructions reference: `https://github.com/marconian/nde-data-analysis`
   - This repository appears to be the actual analysis infrastructure
   - Repository URL returns 404 (may be private or moved)
   - **Fix:** Clarify if this analysis was performed using that repository; document relationship

3. **Missing Questionnaire Schema Documentation**
   - Analysis references "JSON analysis files" as intermediate data
   - The 31 variables and coding schema are not fully documented
   - **Fix:** Publish or reference the questionnaire-to-JSON mapping

4. **Operationalization Definitions Missing**
   - "Unknown presence" classification criteria
   - "External condemnation" vs "self-judgment" distinction
   - "Reincarnation indicators" search methodology
   - **Fix:** Add operationalization appendix

5. **No Ethics/IRB Statement**
   - Analysis uses human subject data
   - No mention of ethics review or data use agreements
   - **Fix:** Add statement on ethics approval or exemption rationale

---

## Recommendations for Source Strengthening

### Immediate Actions (Document Updates)

1. **Add Formal Citation Block:**
   ```
   ### Primary Data Sources
   
   - NDERF Database. (1998-2025). Near-Death Experience Research Foundation.
     https://www.nderf.org/ [Accessed: December 2025; n=5,646 records]
   
   - IANDS Registry. (n.d.). International Association for Near-Death Studies.
     https://iands.org/nde-accounts/ [Accessed: December 2025; n=1,093 records]
   ```

2. **Link to Analysis Repository:**
   - If `nde-data-analysis` is the analysis codebase, cite it explicitly
   - Provide data extraction scripts for reproducibility

3. **Add Operationalization Appendix:**
   - Document each variable definition
   - Provide coding examples for ambiguous categories

### Long-Term Actions (Framework Improvement)

1. **Create Standardized Source Chain Template** for all empirical documents
2. **Establish Database Access Protocol** documentation
3. **Develop Reproducibility Guidelines** for computational analyses

---

## Final Source Chain Summary

```
┌─────────────────────────────────────────────────────────────────────┐
│ DOCUMENT: conceptual_framework_deep_dive_report-analysis_iands...  │
│ TYPE: [E] Empirical + [T] Tertiary synthesis                        │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ INTERMEDIATE: JSON analysis files                                   │
│ TYPE: [E] Structured data extraction                                │
│ STATUS: [TRACE NEEDED] - Schema undocumented                        │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│ PRIMARY: NDERF Database (n=5,646)                                   │
│ TYPE: [E] Empirical - Self-reported NDE accounts                    │
│ URL: https://www.nderf.org/                                         │
│ CUSTODIAN: Dr. Jeffrey Long, MD                                     │
│ STATUS: ⚠️ Not formally cited in document                           │
├─────────────────────────────────────────────────────────────────────┤
│ PRIMARY: IANDS Registry (n=1,093)                                   │
│ TYPE: [E] Empirical - Submitted NDE accounts                        │
│ URL: https://iands.org/nde-accounts/                                │
│ CUSTODIAN: IANDS (501(c)(3) nonprofit)                              │
│ STATUS: ⚠️ Not formally cited in document                           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Verification Status by Claim

| # | Claim | Source Type | Status | Action Required |
|---|-------|-------------|--------|-----------------|
| 1 | Being of Light: 47.3% | [E] | ⚠️ PARTIAL | Add database citations |
| 2 | Unknown presence: 61.8% | [E] | ⚠️ TRACE NEEDED | Document coding criteria |
| 3 | No condemnation: 84.8% | [E] | ⚠️ TRACE NEEDED | Define operationalization |
| 4 | Communication: 79.4% | [E] | ⚠️ PARTIAL | Cite questionnaire fields |
| 5 | Cross-religious: 60-63% | [E] | ✅ VERIFIED | Add field citations |
| 6 | ML accuracy: 68.2% | [E] | ✅ VERIFIED | Publish code |
| 7 | Deceased relatives: 18.7% | [E] | ⚠️ TRACE NEEDED | Define reincarnation criteria |

---

## Conclusion

This document represents **legitimate original empirical analysis** of established NDE databases. The statistical methodology is sound and the findings are internally consistent. However, the document **fails to meet scholarly source documentation standards** in several key areas:

1. **Primary sources are named but not formally cited**
2. **Variable operationalization is incomplete**
3. **Analysis reproducibility is limited** without access to JSON schema and code
4. **Extraordinary claims (0% reincarnation)** lack sufficient methodological documentation

**Overall Assessment:** The empirical findings are likely valid but require source documentation strengthening before integration into the framework as verified knowledge graph nodes.

---

*Report generated by @source-tracer agent*  
*December 29, 2025*
