# Editorial Annotation Manual

**Created**: 2026-01-26  
**Purpose**: Standardized approach for annotating documents with evolved understanding  
**Related**: [EVOLVING_CONCEPTUAL_STRAINS.md](EVOLVING_CONCEPTUAL_STRAINS.md)

---

## Overview

The literary-compilation corpus contains documents generated iteratively over time. As understanding evolves, later documents often correct, reframe, or extend earlier positions. Rather than rewriting documents (which would destroy the historical record), we **annotate** them to guide readers to current understanding.

### Core Principles

1. **Preserve the original** — Never delete or substantially rewrite original content
2. **Link to single source of truth** — All corrections reference `EVOLVING_CONCEPTUAL_STRAINS.md`
3. **Use strain numbers** — Cross-reference using `#N` format for consistency
4. **Minimal invasion** — Annotate only what's necessary; don't clutter
5. **Reader-first** — Annotations should help readers, not demonstrate our cleverness

---

## Annotation Types

| Type | Tag | Use When | Example |
|------|-----|----------|---------|
| General evolution | `[EVOLVED]` | Understanding has developed over time | Framework extensions |
| Error correction | `[CORRECTION]` | Specific factual or conceptual error | Magi attribution error |
| Reinterpretation | `[REFRAMING]` | Same data, new interpretation | Most Ancient Church as allegory |
| Extension | `[EXTENSION]` | Original correct but now extended | Somatic Influx |
| Critical analysis | `[CRITICAL ANALYSIS]` | Scholarly analysis reveals problems | Virgin Birth translation |

---

## Document Structure

### 1. Header Editorial Block

Add immediately after the document title (before any content):

```markdown
# **Document Title Here**

> ---
> **📋 Editorial Notes** | Last reviewed: 2026-01-26
> 
> This document reflects **earlier understanding** on the following strains:
> - **#18** [Bene Qedem as True Carriers](EVOLVING_CONCEPTUAL_STRAINS.md#18-bene-qedem-as-true-carriers-not-magi) — **CRITICAL**: Attributes correspondence to Magi rather than Bene Qedem
> - **#6** [Magi and Daniel Historicity](EVOLVING_CONCEPTUAL_STRAINS.md#6-magi-and-daniel-historicity) — Treats Daniel's role uncritically
> 
> **Summary**: This document correctly describes Magian *institutionalization* of correspondence but incorrectly implies Magi *originated* the wisdom. The true carriers were the Bene Qedem (nomadic "Children of the East"). See "The Bifurcated Gnosis" for corrected transmission chain.
> ---

## **First Section of Original Document...**
```

### Header Block Components

| Component | Required | Description |
|-----------|----------|-------------|
| `📋 Editorial Notes` | Yes | Visual marker for quick identification |
| `Last reviewed` | Yes | Date of annotation (YYYY-MM-DD) |
| Strain list | Yes | Numbered list with links to EVOLVING_CONCEPTUAL_STRAINS.md |
| Priority markers | If CRITICAL | Bold **CRITICAL** for highest priority strains |
| Summary | Yes | 1-3 sentences explaining what readers need to know |

### 2. Inline Annotations

For specific passages that require correction, add annotation immediately after the passage:

```markdown
The Magi developed the Science of Correspondences based on their astronomical observations...

> **[CORRECTION #18]**: The Magi did NOT develop correspondence—they **appropriated** it 
> from the Bene Qedem. See "The Bifurcated Gnosis" for corrected transmission chain.
```

### Inline Annotation Format

```markdown
> **[TYPE #N]**: Brief explanation. See "Document Name" for details.
```

- **TYPE**: One of EVOLVED, CORRECTION, REFRAMING, EXTENSION, CRITICAL ANALYSIS
- **#N**: Strain number from EVOLVING_CONCEPTUAL_STRAINS.md
- **Explanation**: 1-2 sentences maximum
- **Reference**: Point to the document with corrected position

---

## Workflow

### Step 1: Identify Documents Needing Annotation

Check `EVOLVING_CONCEPTUAL_STRAINS.md` for:
- **CRITICAL** priority strains (annotate immediately)
- **High** priority strains (annotate in next pass)
- Documents listed under "Documents reflecting earlier position"

### Step 2: Read the Document

Before annotating:
1. Read the full document (or relevant sections)
2. Identify specific passages affected by the strain
3. Assess severity: Does the entire thesis need qualification, or just specific claims?

### Step 3: Determine Annotation Level

| Situation | Annotation Level |
|-----------|------------------|
| Document's core thesis is superseded | Header block only (with strong summary) |
| Specific claims are incorrect | Header block + inline annotations |
| Minor refinements needed | Inline annotations only |
| Document is mixed (some sections correct) | Header block explaining which sections are affected |

### Step 4: Write the Header Block

1. Copy the template from this manual
2. List affected strains with proper links
3. Write a clear, helpful summary
4. Set the review date

### Step 5: Add Inline Annotations (If Needed)

1. Locate specific passages requiring annotation
2. Add annotation immediately after the passage
3. Keep annotations brief—point to EVOLVING_CONCEPTUAL_STRAINS.md for details

### Step 6: Update Tracking

In `EVOLVING_CONCEPTUAL_STRAINS.md`, update the document checklist:
- Change `[ ]` to `[x]` for documents you've annotated
- Add the document if it wasn't already listed

---

## Examples

### Example 1: Critical Correction (Strain #18)

**Document**: `data/02_Swedenborgian_Theology/The Science of Correspondences...from Daniel to Nativity.md`

**Header Block**:
```markdown
# **The Science of Correspondences: A Scholarly Analysis of the Magi from the Era of Daniel to the Nativity**

> ---
> **📋 Editorial Notes** | Last reviewed: 2026-01-26
> 
> This document reflects **earlier understanding** on:
> - **#18** [Bene Qedem as True Carriers](../docs/EVOLVING_CONCEPTUAL_STRAINS.md#18-bene-qedem-as-true-carriers-not-magi) — **CRITICAL**: Attributes correspondence to Magi rather than Bene Qedem
> 
> **Summary**: This document correctly describes Magian political power and their institutionalization of correspondence wisdom, but **incorrectly implies the Magi originated the Science of Correspondences**. Forensic analysis shows the **Bene Qedem** (nomadic "Children of the East"—Ishmaelites, Midianites) were the true carriers. The Magi appropriated and institutionalized this pre-existing wisdom for imperial power. See "The Bifurcated Gnosis" for the corrected transmission chain.
> ---
```

**Inline Annotation** (at specific passage):
```markdown
### **The Legacy of Daniel: A Conduit for Prophetic Transmission**

The historical intersection of the Jewish exile in Babylon with the rise of Medo-Persian power created a unique and profoundly significant channel for the cross-pollination of religious ideas.

> **[CORRECTION #18]**: While Daniel's role as conduit is valid, the "cross-pollination" 
> framing implies the Magi contributed correspondence wisdom. In fact, Daniel transmitted 
> Jewish prophecy TO a priesthood that had already appropriated correspondence from the 
> Bene Qedem. The influence was primarily one-directional.
```

### Example 2: Reframing (Strain #5)

**Document**: `data/02_Swedenborgian_Theology/Communication among the most ancient people...md`

**Header Block**:
```markdown
# **Communication Among the Most Ancient People**

> ---
> **📋 Editorial Notes** | Last reviewed: 2026-01-26
> 
> This document reflects **earlier understanding** on:
> - **#5** [The Most Ancient Church](../docs/EVOLVING_CONCEPTUAL_STRAINS.md#5-the-most-ancient-church) — Treats Golden Age as historical period
> 
> **Summary**: This document interprets "Internal Respiration" as a literal breathing technique in a historical period. Later analysis reframes the Golden Age as **allegorical narrative for hominin cognitive evolution**. "Internal Respiration" corresponds to the decoupling of breathing from locomotion (bipedalism). See "A Validation Analysis of Claims Concerning the Most Ancient Church" for the evolutionary mapping.
> ---
```

### Example 3: Extension (Strain #14)

**Document**: `data/02_Swedenborgian_Theology/Swedenborg's Natural World Correspondences.md`

**Header Block**:
```markdown
# **Swedenborg's Natural World Correspondences**

> ---
> **📋 Editorial Notes** | Last reviewed: 2026-01-26
> 
> This document reflects **earlier understanding** on:
> - **#14** [Somatic Influx](../docs/EVOLVING_CONCEPTUAL_STRAINS.md#14-somatic-influx-and-radical-remission) — Treats correspondence as primarily symbolic
> 
> **Summary**: This document correctly presents correspondences as symbolic/hermeneutic relationships. Later research **extends** this to bidirectional operation: the body is "the soul in ultimates," meaning spiritual transformation can produce physical reorganization (radical remission). See "The Architecture of Anomaly" for empirical evidence.
> ---
```

---

## Link Format

### Relative Paths

From `data/` subdirectories, use:
```markdown
[Strain Name](../docs/EVOLVING_CONCEPTUAL_STRAINS.md#anchor)
```

From other locations, adjust path accordingly:
```markdown
[Strain Name](../../docs/EVOLVING_CONCEPTUAL_STRAINS.md#anchor)
```

### Anchor Format

Anchors are auto-generated from headings:
- `### 18. Bene Qedem as True Carriers (Not Magi)` → `#18-bene-qedem-as-true-carriers-not-magi`
- `### 5. The Most Ancient Church` → `#5-the-most-ancient-church`

---

## Do's and Don'ts

### ✅ DO

- Keep annotations brief and helpful
- Always link to EVOLVING_CONCEPTUAL_STRAINS.md
- Use strain numbers consistently
- Update tracking when you annotate a document
- Preserve all original content
- Date your annotations

### ❌ DON'T

- Don't rewrite original document content
- Don't add lengthy explanations inline—link to the strains document
- Don't annotate documents that already reflect current understanding
- Don't annotate minor refinements that don't affect reader comprehension
- Don't use annotation to editorialize or add opinion

---

## Maintenance

### When Understanding Evolves Further

1. Add new strain to `EVOLVING_CONCEPTUAL_STRAINS.md`
2. Identify affected documents
3. Add/update annotations in those documents
4. Update this manual if new annotation types are needed

### Periodic Review

- Review annotated documents when strains are updated
- Remove annotations if documents are rewritten to reflect current understanding
- Update review dates in header blocks

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│  HEADER BLOCK (after title, before content)                 │
│                                                             │
│  > ---                                                      │
│  > **📋 Editorial Notes** | Last reviewed: YYYY-MM-DD       │
│  >                                                          │
│  > This document reflects **earlier understanding** on:     │
│  > - **#N** [Strain](link) — Impact                         │
│  >                                                          │
│  > **Summary**: Brief explanation.                          │
│  > ---                                                      │
├─────────────────────────────────────────────────────────────┤
│  INLINE ANNOTATION (after specific passage)                 │
│                                                             │
│  > **[TYPE #N]**: Brief correction. See "Doc" for details.  │
├─────────────────────────────────────────────────────────────┤
│  TYPES: EVOLVED | CORRECTION | REFRAMING | EXTENSION |      │
│         CRITICAL ANALYSIS                                   │
├─────────────────────────────────────────────────────────────┤
│  WORKFLOW: 1. Check strains → 2. Read doc → 3. Determine    │
│            level → 4. Write header → 5. Add inline →        │
│            6. Update tracking                               │
└─────────────────────────────────────────────────────────────┘
```
