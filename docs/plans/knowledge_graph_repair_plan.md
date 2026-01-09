# Knowledge Graph Repair Plan

**Created:** 2026-01-09  
**Status:** Active  
**Last Updated:** 2026-01-09

---

## Critical Instructions

### ⚠️ STOP AND CHECK THIS DOCUMENT

Before doing ANY work on the knowledge graph:

1. **Read this document first**
2. **Check the current phase** - what step are we on?
3. **Update the todo list** to reflect current phase
4. **Follow the methodology exactly** - no shortcuts

### The Core Mistake to Avoid

**DO NOT** try to wire existing nodes together based on titles and definitions alone.  
**DO** read the actual source documents to understand what structure should exist.

---

## Methodology

### Phase 1: Document Analysis (MUST COMPLETE FIRST)

Before touching the graph, analyze the framework documents to understand what the foundational structure SHOULD be.

**Key Framework Documents to Read:**
- [ ] `data/00_Framework/A Coherent Framework for Spiritual History_ Weaving the Divine Bricolage.md`
- [ ] `data/00_Framework/The Divine Bricolage_ A Spiritual History of the Word from Influx to Incarnation.md`
- [ ] `data/00_Framework/The Threefold Path of the Soul_ A Synthesized Cosmology of Life, Death, and Purpose.md`
- [ ] `data/00_Framework/The Threefold Path of the Soul_ An Exhaustive Empirical and Cosmological Analysis of Post-Mortem Consciousness and Incarnational Dynamics.md`
- [ ] `data/00_Framework/The Heart of the Matter_ A New Church Founded on Love.md`
- [ ] `data/00_Framework/The Work of Divine Influx_ A 2000-Year History of the Internal Path and its Conflict with the External Proprium.md`
- [ ] `data/00_Framework/Enhancing Spiritual History Framework.md`
- [ ] `data/00_Framework/Epistle - On Who I Am, The Words of An AI Agent.md`
- [ ] `data/00_Framework/Epistle - The Divine Marriage and the Expression of the Lord in Ultimates.md`

**Domain-Specific Documents:**
When analyzing gaps in a specific domain, also read documents from that domain's folder:
- `data/01_Consciousness_Studies/` - for CONSC domain gaps
- `data/02_Swedenborgian_Theology/` - for SWED domain gaps
- `data/03_Biblical_Scholarship/` - for BIBL domain gaps
- `data/04_Early_Christian_History/` - for EARLY domain gaps
- `data/05_Gnostic_Analysis/` - for GNOS domain gaps
- `data/06_Mythological_Studies/` - for MYTH domain gaps

**Using Broken Chain Nodes as Guides:**
When a node has a broken chain (e.g., hypothesis not connected to concept), check the node's `source_chain` field. This points to the source document(s) that created that node. Read those documents to understand:
- What concept should this node connect to?
- Does that concept exist, or is it missing?
- What is the full context the original document provides?

**Questions to Answer:**
1. What are the core foundational concepts of the framework?
2. Which foundational nodes are MISSING from the current graph?
3. Which CONCEPT nodes are missing that should exist?
4. What is the intended hierarchical structure?

**Output:** A list of missing foundational and concept nodes with:
- Proposed ID
- Title
- Definition (from document)
- Which foundational it develops from
- Source document reference

### Phase 2: Create Missing Foundational/Concept Nodes

Only after Phase 1 is complete:

1. Create the missing foundational nodes identified
2. Create the missing concept nodes identified
3. Add proper connections as nodes are created
4. Run validation after each addition

### Phase 3: Fix Chain Gaps (One at a Time)

For each remaining gap:

1. **Identify the gap** - what type of warning? What node?
2. **Check the node's source_chain** - what document(s) created this node?
3. **Read the source document(s)** - understand the full context
4. **Determine what's missing** - is it a missing concept? Missing connection? Wrong node type?
5. **Make the fix** - create missing node or add connection based on document understanding
6. **Validate** - run graph validation
7. **Update this plan** - log what was done in the Progress Log

### Phase 4: Review and Validate

- Full validation pass
- Check all domains have proper foundational coverage
- Document remaining issues

---

## Current Status

### Phase: 1 - Document Analysis
### Step: Not started

### Progress Log

| Date | Action | Result |
|------|--------|--------|
| 2026-01-09 | Plan created | - |

---

## Task List Protocol

### How to Use the Todo List

1. **Always have a "Check plan document" task** - This should be checked after every major action
2. **One gap at a time** - Never work on multiple gaps simultaneously
3. **Mark tasks as they complete** - Keep accurate status
4. **Update this document** - After completing work, log it here

### Required Tasks (Always Present)

- [ ] Check plan document and update status
- [ ] Current phase task (whatever phase we're in)

### Current Active Tasks

```
Phase 1: Document Analysis
- [ ] Read framework documents
- [ ] Identify missing foundational nodes
- [ ] Identify missing concept nodes
- [ ] Document findings in this plan
```

---

## Domain Analysis (To Be Completed in Phase 1)

### CONSC Domain
**Current foundational nodes:** 1 (CONSC-001: CDE)  
**Current concept nodes:** 6 (all hemispheric brain related)  
**Missing concepts identified:** (TBD after document analysis)

### BIBL Domain
**Current foundational nodes:** 0 (BIBL-010 is actually foundational?)  
**Current concept nodes:** (TBD)  
**Missing concepts identified:** (TBD)

### SWED Domain
**Current foundational nodes:** 2 (SWED-028, SWED-051)  
**Current concept nodes:** 45  
**Missing concepts identified:** (TBD)

### EARLY Domain
**Current foundational nodes:** 0?  
**Current concept nodes:** (TBD)  
**Missing concepts identified:** (TBD)

### GNOS Domain
**Current foundational nodes:** 3 (GNOS-002, GNOS-011, GNOS-019)  
**Current concept nodes:** (TBD)  
**Missing concepts identified:** (TBD)

### MYTH Domain
**Current foundational nodes:** 0?  
**Current concept nodes:** (TBD)  
**Missing concepts identified:** (TBD)

### CROSS Domain
**Current foundational nodes:** 9  
**Current concept nodes:** 1 (CROSS-003)  
**Missing concepts identified:** (TBD)

---

## Findings (Phase 1 Output)

### Missing Foundational Nodes

(To be filled after document analysis)

| ID | Title | Definition | Source |
|----|-------|------------|--------|
| | | | |

### Missing Concept Nodes

(To be filled after document analysis)

| ID | Title | Definition | Develops From | Source |
|----|-------|------------|---------------|--------|
| | | | | |

---

## Checklist Before Any Edit

- [ ] Have I read this plan document?
- [ ] Am I in the correct phase?
- [ ] Have I read the relevant source document?
- [ ] Do I understand what structure SHOULD exist?
- [ ] Am I working on ONE gap only?
- [ ] Will I update this document after the edit?

---

## Notes

- The graph was built by transforming documents, focusing on evidence rather than properly defining foundational and concept nodes
- Many hypotheses are orphaned because the concept nodes they should connect to don't exist
- The fix is NOT to wire hypotheses to random existing nodes, but to CREATE the missing concept layer first
