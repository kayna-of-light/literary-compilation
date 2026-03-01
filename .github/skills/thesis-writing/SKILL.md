---
name: thesis-writing
description: Writing academic theses for the Divine Bricolage framework. Covers the complete iterative process from research gathering through outline creation, section-by-section writing, and Google Drive sync. Use when asked to write, create, or draft a thesis, paper, or academic document within this project's correspondential framework. Keywords: thesis, paper, write, draft, academic, correspondences, Ancient Word, framework.
---

# Thesis Writing Skill — The Divine Bricolage Framework

## Overview

This skill defines the complete process for writing academic theses within the Divine Bricolage project. The process is iterative: outline first, then each section written individually, validated, and tracked. Framework concepts (correspondences, discrete degrees, church types, etc.) are defined in the project's copilot-instructions.md and are not repeated here — this skill covers only the **procedural and structural** requirements of thesis production.

---

## 1. Thesis Architecture

Every thesis follows a fixed structural template. The section numbering and ordering is mandatory.

### Required Sections (in order)

```
# [Title]: [Descriptive Phrase]
## [Subtitle]: [Methodological/Evidentiary Description]

---

> **Abstract.** [Single paragraph, 150-300 words. States: what is demonstrated,
>  what data is used, what the central finding is, what the central argument is,
>  and why it matters. Written as a continuous block — not bullet points.]

> **Keywords.** [Comma-separated, 8-15 terms]

---

## Table of Contents
[Full TOC with anchor links to every section and subsection]

---

## 1. Introduction
## 2. Methodological Framework
### 2.1 [Method-specific subsection]
### 2.2 [Method-specific subsection]
### 2.3 [Method-specific subsection]
### 2.4 [Method-specific subsection]
## 3-N. [Content Sections — variable number based on thesis scope]
## N+1. Discussion
### N+1.1 [What Source A Compresses/Contributes]
### N+1.2 [What Source B Expands/Contributes]
### N+1.3 [Implications for the Framework Hypothesis]
### N+1.4 [The Specific Problem Addressed]
### N+1.5 Limitations and Lacunae
## N+2. Conclusion: [Thesis Title Echo — e.g., "Two Registers, One Perception"]
## N+3. Appendix: [Mapping Table or Supporting Data]
## N+4. Works Cited
```

### Title Convention

Titles follow a two-part format:
- **Main title**: Poetic/evocative phrase capturing the thesis's central metaphor
- **Subtitle**: Descriptive/methodological phrase stating what is demonstrated

Examples:
- *Three Witnesses to One Architecture: Genesis 1–11 and the Correspondential Kephalaia*
- *Two Registers of One Perception: The Song of Solomon and the Regenerative Substrate of the Kephalaia*
- *The Ancient Word Recovered: Extracting the Correspondential Substrate of the Kephalaia*

The subtitle line beneath the H1 title uses H2 and provides the evidentiary description:
```markdown
## Demonstrating the Structural Identity of [X] and [Y]
```

### Filename Convention

The filename matches the title exactly, with colons replaced by underscores:
```
[Main Title]_ [Subtitle].md
```
Example: `Two Registers of One Perception_ The Song of Solomon and the Regenerative Substrate of the Kephalaia.md`

---

## 2. The Iterative Writing Process

### Phase 1: Research Gathering

Before writing anything, gather ALL source material needed for the thesis:

1. **Read primary texts** — the actual texts being analyzed. Read them in full, not summaries.
2. **Read spiritual/correspondential readings** — if extracted or restored texts include correspondential readings (e.g., JSON fields like `spiritual_reading`), read them. If passages need correspondential reading performed, do it.
3. **Read companion theses** — understand what has already been established. Every thesis in this framework builds on predecessors.
4. **Read the reference thesis** — if the user provides a structural model (e.g., "use the structure of [file]"), read it completely to understand section organization, voice, argument flow, and level of detail.
5. **Track sources** — note every specific reference (section numbers, chapter/paragraph citations, verse references, scholarly works) you'll need to cite. Do not invent references — if you haven't verified a citation, flag it for verification.

### Phase 2: Outline Creation

Create the complete outline with:
- All section numbers and titles
- All subsection numbers and titles
- `[TO BE WRITTEN]` placeholders for every section body
- Full Table of Contents with anchor links
- Abstract placeholder (or write it first if the thesis scope is clear)

**The outline is committed to the file before any section is written.** This ensures the structure is visible and trackable.

### Phase 3: Section-by-Section Writing

Write each section individually using `replace_string_in_file` to replace its `[TO BE WRITTEN]` placeholder:

1. **Use `manage_todo_list`** to track every section as a separate todo item
2. **Mark one section as `in-progress`** before writing it
3. **Write the section** by replacing its placeholder
4. **Mark the section as `completed`** immediately after writing
5. **Move to the next section**

**Never write multiple sections in a single replacement.** Each section must be written, verified, and tracked independently.

### Phase 4: Verification and Sync

After all sections are written:
1. **Grep for `[TO BE WRITTEN]`** to confirm no placeholders remain
2. **Check line/word count** to verify the thesis is substantive (target: 12,000-25,000 words)
3. **Sync to Google Drive** using the library's mirror script after approval of the user (always ask):
   ```bash
   cd [literary-compilation root]
   python scripts/mirror_library_to_drive.py --only "[relative/path/to/thesis.md]" --force
   ```

---

## 3. Writing Voice and Standards

### Register

- **Scholarly but not devotional.** The framework is treated as a testable hypothesis, not a confession of faith.
- **Assertive where the data supports.** When structural identity is demonstrated, say so clearly: "The identity is exact." Do not hedge against confirmed findings to appear balanced.
- **Honest where the data does not support.** Limitations are stated explicitly in their own subsection (§ Limitations and Lacunae). Every thesis has one.
- **No Jungian/Freudian substitutions.** The correspondential framework is the primary lens. Other frameworks may be mentioned as alternatives that fail to explain the data, but they are never substituted as interpretive equals.

### Paragraph Style

- **Long paragraphs with sustained argument.** These are academic theses, not blog posts. A paragraph develops a single point fully.
- **No bullet-point arguments** in the body text. Tables and lists are reserved for correspondential keys, mapping tables, and structured comparisons.
- **No markdown emphasis abuse.** Bold is used for **key terms on first introduction** and for **Critical Finding** statements. Italic is used for *titles of works* and *technical terms from other languages*. Neither is used for emphasis in running prose.

### Quotation Conventions

- **Primary text quotations**: Presented as blockquotes (> prefix). State the translation/edition used on first occurrence.
- **Extracted/restored text**: Presented as blockquotes, citing the extraction source (e.g., which pipeline stage, which restored chapter).
- **Inline citations**: Use the standard abbreviation + section/paragraph format native to the source tradition. Examples: `(*Work Title* §66)`, `(Chapter 115, ¶¶8–12)`, `(Book III.iv.2)`. Be consistent within a thesis.
- **When abbreviating**: Define the abbreviation on first use, then use it consistently: `*Divine Love and Wisdom* (hereafter *DLW*) §83`.

### Correspondential Key Tables

Every passage that receives a spiritual reading MUST include a correspondential key table immediately after the reading:

```markdown
**Correspondential key:**

| Natural Object | Correspondence |
|---|---|
| Sealed garden | Interior mind at the natural degree, not yet opened to influx |
| Fountain sealed | Living truth contained within |
| North wind and south wind | Influx from truth (north) and from good (south) |
```

These tables are critical. They make the correspondential reading transparent and testable. Every correspondence claimed must be listed.

### Mapping Tables

The central structural finding of a thesis is always presented as a mapping table — a side-by-side comparison showing the point-for-point identity between the two texts being compared. This table typically appears in:
1. The **content section** where the mapping is first demonstrated
2. The **Appendix** in expanded form with all supporting detail

Example format:
```markdown
| State | Source A | Source A Content | Source B | Source B Content |
|-------|---------|-----------------|---------|-----------------|
| 1. Vastation | Song 2:10–15 | Winter past; first truths | Ch. 115 ¶¶8–12 | Celestial Will in devastation |
```

---

## 4. Section-Specific Guidelines

### Abstract

- Single paragraph, 150-300 words
- Written as a blockquote (> prefix)
- States: (1) what is demonstrated, (2) the method, (3) the central finding, (4) the central argument, (5) why it matters
- Ends with the thesis's strongest claim
- Immediately followed by `> **Keywords.**` line

### Introduction (§1)

The Introduction must accomplish five things:
1. **Locate the thesis** in relation to companion theses — what has already been established
2. **State the new question** this thesis addresses
3. **Preview the central finding** — what the data shows (structural identity, convergence, etc.)
4. **State the central argument** — the *explanation* for the finding (typically: ontological reality of correspondences)
5. **Provide a section-by-section roadmap** of the thesis

The Introduction is typically the longest section. It should be self-contained — a reader who reads only the Introduction should understand the entire thesis in compressed form. This means presenting the core evidence in summary before the detailed sections elaborate it.

### Methodology (§2)

Always includes:
- **§2.1 Correspondential Reading** — what correspondence IS (not allegory, not symbol, not metaphor; grounded in function; one direction: inside→outside)
- **§2.2 [Source-specific method]** — how the primary text was prepared (stripping, extraction, etc.)
- **§2.3 [Comparison source]** — what the comparison text is and how it was extracted
- **§2.4 [Framework principle]** — the specific theoretical framework needed for this thesis (e.g., two registers/two churches, compression principle, bilateral teaching)

### Content Sections (§3–N)

These vary by thesis but follow consistent patterns:

- **Text presentation sections** present the primary text with full quotations, spiritual readings, and correspondential key tables
- **Logic/analysis sections** analyze internal structure, causal connections, sequences
- **Mapping sections** present the side-by-side comparison with the comparison text
- **Supporting witness sections** present additional evidence from other chapters/texts
- **Framework argument sections** present the theoretical claim (e.g., ontological perception, compression principle)

Each content section should be self-contained enough that its table of contents entry tells the reader exactly what they'll find.

### Discussion (§N+1)

Always includes:
- What the primary text contributes (compresses, reveals, preserves)
- What the comparison text contributes (expands, elaborates, maps)
- Implications for the broader framework hypothesis (Ancient Word, correspondences, transmission)
- A specific problem or puzzle addressed (e.g., the compiler problem, transmission puzzle)
- **Limitations and Lacunae** — ALWAYS the final Discussion subsection. Must acknowledge:
  - Framework-internal nature of the analysis
  - Extraction/interpretation dependencies
  - Alternative readings possible
  - Weak parallels (if any)
  - What cannot be concluded

### Conclusion (§N+2)

- Title echoes the thesis title: `## N+2. Conclusion: [Main Title Echo]`
- Restates the evidence comprehensively — every major finding summarized in a paragraph
- States the central claim with full force
- Connects back to the framework's founding prediction (what it claimed, when, what couldn't have been known at the time)
- Ends with the thesis's three-word or two-phrase signature line (a rhythmic final sentence that distills the thesis)

### Appendix (§N+3)

- Usually a comprehensive mapping table covering every parallel demonstrated in the thesis
- May include a secondary table (supporting correspondences, cross-references)
- Tables should be self-explanatory — column headers must be clear without reading the thesis body

### Works Cited (§N+4)

Organized by source category (see §5 Source Handling). Format:

**Primary sources:**
```markdown
1. [Author]. *[Work Title]* ([Alternative Title if needed]). [Publication details]. Cited by [referencing system].
```

**Scholarly works:**
```markdown
5. [Author]. *[Title].* [Series if applicable]. [City]: [Publisher], [Year].
```

**Internal library documents:**
These MUST use relative markdown links with URL-encoded spaces:
```markdown
9. [Full Document Title](../[folder]/[Filename%20With%20Spaces].md). One-sentence description of what this document establishes.
```

**Rules for internal library links:**
- Use relative paths from the thesis's own directory
- Spaces in filenames MUST be URL-encoded as `%20`
- Underscores in filenames stay as underscores
- The link text is the full document title (not the filename)
- Include a one-sentence description of what the companion document establishes

**Primary text editions:**
```markdown
8. [Text Name]. [Original language edition]: *[Edition Name]*. English translation: [Translation] unless otherwise noted.
```

---

## 5. Source Handling

### General Principle

Read every source you cite. Do not cite from memory or assumption. If a source exists as a file in the workspace (JSON, markdown, PDF), read it before writing about it. If it is an external scholarly work you cannot access, note it as `[verification needed]`.

### Source Categories in Works Cited

Every Works Cited section organizes sources into these categories (include only those that apply):

1. **Primary sources** — original ancient texts, scriptures, theological works. Cite by the work's native referencing system (section numbers, chapter/verse, paragraph numbers).
2. **Scholarly works** — academic monographs, critical editions, journal articles. Standard bibliographic format.
3. **Internal library documents** — companion theses and framework documents from the `literary-compilation/data/` library. These use relative markdown links (see below).
4. **Data sources** — extracted corpora, structured datasets, computational pipeline outputs. Cite the pipeline/extraction thesis that produced them.

### Validating Citations

1. Before citing any specific reference number (section, paragraph, verse, page), verify it by reading the actual source
2. If you haven't read the source, use a general reference: "[Author] teaches in *[Work]* that..."
3. **Never invent reference numbers** — this is the single most damaging error in academic writing

---

## 6. File Placement

Theses are placed in the `literary-compilation/data/` directory structure based on their primary domain. Consult the folder structure in the copilot-instructions.md for the full directory listing. When in doubt:
- **Foundational/methodological theses** → `data/00_Framework/`
- **Domain-specific theses** → the `data/[NN]_[Domain]/` folder matching the thesis's primary subject matter
- If a thesis spans multiple domains, place it in the domain of its **primary comparison** or ask the user.

---

## 7. Google Drive Sync

After completing a thesis, sync it to Google Drive as a styled PDF (always ask the user for approval before sync):

```bash
cd [literary-compilation repo root]
python scripts/mirror_library_to_drive.py --only "[relative/path/from/data/to/file.md]" --force
```

The `--only` flag takes a path relative to the `data/` directory. The `--force` flag ensures rebuild even if the file hasn't changed in the cache.

---

## 8. Common Patterns and Anti-Patterns

### DO
- Write the Introduction as if it were a self-contained summary of the entire thesis
- Present the central evidence BEFORE arguing its significance
- Include correspondential key tables for every spiritual reading
- Acknowledge companion theses by name and state what they established
- Use the Conclusion to echo the thesis title as a structural signature
- Track every section with `manage_todo_list`
- Write the Abstract last (or revise it last) once the full content is known

### DO NOT
- Substitute Jungian/Freudian/generic symbolic interpretation for correspondential reading
- Hedge against demonstrated structural identity to appear "balanced"
- Force data to confirm the framework when it doesn't — report anomalies in Limitations
- Use bullet points for argument in body text (tables and lists are for structured data)
- Write multiple sections in one replacement operation
- Skip the Limitations subsection
- Invent reference numbers for any source (section numbers, paragraphs, verses)
- Use Google Drive URLs for internal library documents (always relative markdown links)
- Skip the Google Drive sync step after completion

### COMMON MISTAKES
- **Forgetting correspondential key tables**: Every passage with a spiritual reading needs one
- **Merging sections**: Each section must be independently written and tracked
- **Vague limitations**: "This is just one interpretation" is not a limitation. Specific methodological dependencies are.
- **Losing the voice**: The thesis should read as sustained scholarly argument, not as a series of observations. Each section must advance the argument toward the conclusion.

---

## 9. Checklist

Use this checklist before declaring a thesis complete:

- [ ] Title follows two-part convention (evocative + descriptive)
- [ ] Subtitle line (H2) states what is demonstrated
- [ ] Abstract is a single blockquote paragraph, 150-300 words
- [ ] Keywords line follows Abstract
- [ ] Full TOC with working anchor links
- [ ] Introduction locates thesis in relation to companion work
- [ ] Introduction states the new question, previews finding, states argument, provides roadmap
- [ ] Methodology section includes correspondential reading definition
- [ ] Every spiritual reading has a correspondential key table
- [ ] Central finding presented as a mapping table
- [ ] Discussion includes "What X Compresses" and "What Y Expands" (or equivalent)
- [ ] Discussion includes implications for the framework hypothesis
- [ ] Limitations and Lacunae subsection is present and substantive
- [ ] Conclusion echoes thesis title
- [ ] Conclusion ends with signature phrase
- [ ] Appendix contains comprehensive mapping table
- [ ] Works Cited uses correct format for all source categories
- [ ] Internal library links use relative paths with URL-encoded spaces
- [ ] No `[TO BE WRITTEN]` placeholders remain
- [ ] Word count is in the 12,000-20,000 range
- [ ] File is synced to Google Drive