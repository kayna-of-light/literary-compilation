# Graph Node Templates Overview

Use these templates when adding or refining nodes. They align with the strict minimal chain enforced by `scripts/graph_utils.py`.

## Global Requirements (all node types)
- **Fields (required)**: `title`, `domain`, `node_type`, `status`, `definition`, `source_chain` (>=1 entry), `connections` (list, can start empty)
- **Source chain entry**:
  - Evidence nodes: full chain to primary/secondary/empirical as applicable.
  - Non-evidence nodes: a single `[T]` entry pointing to the internal framework doc that minted the node is sufficient provenance.
- **Status**: `preliminary | validated | contested` (per metadata)
- **Trace**: set `trace_status: untraced | partial | complete`
- **Connections**: only minimal verbs allowed
  - Development: `develops` / `developed_by`
  - Epistemic: `supports` / `contradicts` (evidence → hypothesis only)
  - Integration: `integrates_into` / `integrated_from` (concept ↔ synthesis)
  - Peer: `parallels`, `contrasts`
  - Structural: `requires`, `required_by`
- **No skip links**: evidence→concept, hypothesis→synthesis, etc., are disallowed

## Evidence Node Template
```
ID: DOMAIN-###
node_type: evidence
title: "..."
status: preliminary|validated|contested
domain: <domain id>
definition: >
  Concise claim of what the evidence shows.
source_chain:
  - type: E|P|S|T|W
    ref: "..."
    note: "..."  # optional
confidence_factors:
  source_type: external|internal
  methodology: randomized_controlled|prospective|retrospective|observational|textual_critical|case_study|theoretical|na
  sample_size: population|large_1000+|medium_100-999|small_10-99|minimal_<10|na
  replication: independent_replicated|internal_replicated|single_study|unreplicated|na
  # external track
  peer_review: peer_reviewed_journal|peer_reviewed_book|dissertation|preprint|unpublished|primary_text|na
  source_chain_quality: primary_verified|primary_unverified|mixed|secondary|tertiary|web
  # internal track (if source_type: internal)
  methodological_transparency: full|high|moderate|low|minimal|na
  source_data_quality: peer_reviewed_database|institutional_database|curated_corpus|mixed_sources|web_scraped|na
  critic_reviewed: reviewed_no_issues|reviewed_minor_issues|reviewed_major_issues|reviewed_unresolved|not_reviewed
connections:
  - target: HYPOTHESIS-ID
    type: supports|contradicts
    note: "..."
trace_status: partial|complete|untraced
critic_notes: {}  # optional block
```

> Agents: Only evidence nodes go through source-tracer, confidence-extractor, and critic workflows.

## Hypothesis Node Template
```
node_type: hypothesis
title: "..."
status: ...
domain: ...
definition: >
  Testable claim derived from a concept.
source_chain:
  - type: T|S|P|E|W
    ref: "..."
connections:
  - target: CONCEPT-ID
    type: developed_by
    note: "..."
  - target: CONCEPT-ID (optional peer/structural)
    type: parallels|contrasts|requires|required_by
  # inbound expected from evidence via supports/contradicts (do not add outbound)
trace_status: ...
critic_notes: {}  # optional
```

> Agents: Non-evidence nodes keep a single `[T]` provenance entry; skip source-tracer, confidence-extractor, critic.

## Concept Node Template
```
node_type: concept
title: "..."
status: ...
domain: ...
definition: >
  Core idea situated under a foundational claim.
source_chain:
  - type: T|S|P|E|W
    ref: "..."
connections:
  - target: FOUNDATIONAL-ID
    type: developed_by
    note: "..."
  - target: HYPOTHESIS-ID
    type: develops
    note: "..."
  - target: SYNTHESIS-ID (if applicable)
    type: integrates_into
    note: "..."
  - target: CONCEPT-ID (peer/structural as needed)
    type: parallels|contrasts|requires|required_by
trace_status: ...
critic_notes: {}  # optional
```

> Agents: Non-evidence nodes keep a single `[T]` provenance entry; skip source-tracer, confidence-extractor, critic.

## Foundational Node Template
```
node_type: foundational
title: "..."
status: ...
domain: ...
definition: >
  Axiomatic or tier-1 claim anchoring concepts.
source_chain:
  - type: P|S|T
    ref: "..."
connections:
  - target: CONCEPT-ID
    type: develops
    note: "..."
  - target: FOUNDATIONAL-ID (peer/structural if truly same-tier)
    type: parallels|contrasts|requires|required_by
trace_status: ...
critic_notes: {}  # optional
```

> Agents: Non-evidence nodes keep a single `[T]` provenance entry; skip source-tracer, confidence-extractor, critic.

## Synthesis Node Template
```
node_type: synthesis
title: "..."
status: ...
domain: cross|...
definition: >
  Integration of multiple validated concepts.
source_chain:
  - type: T|S|P|E|W
    ref: "..."
connections:
  - target: CONCEPT-ID
    type: integrated_from
    note: "..."
  - target: SYNTHESIS-ID (peer/structural as needed)
    type: parallels|contrasts|requires|required_by|integrates_into
trace_status: ...
critic_notes: {}  # optional
```

> Agents: Non-evidence nodes keep a single `[T]` provenance entry; skip source-tracer, confidence-extractor, critic.

## Command Workflow (preferred; avoid manual edits)
1) Add connections safely:
   - `python scripts/graph_utils.py add-connection -s SRC -T TGT -c TYPE --note "..." --dry-run`
   - Remove `--dry-run` to apply.
2) Fix inverses: `python scripts/graph_utils.py fix-inverses --dry-run` then without `--dry-run`.
3) Validate: `python scripts/graph_utils.py validate -v`
4) Persist scores (after confidence_factors updates on evidence nodes): `python scripts/graph_utils.py persist-scores`
5) Export view: `python scripts/graph_utils.py export-md`

Keep editing in YAML minimal and rely on the utils for adds/changes wherever possible.
