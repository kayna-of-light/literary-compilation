#!/usr/bin/env python3
"""
Knowledge Graph Utilities for The Divine Bricolage

Provides functions for querying, validating, and visualizing the knowledge graph.

Usage:
    python graph_utils.py stats              # Show graph statistics
    python graph_utils.py validate           # Check graph integrity (errors + warnings)
    python graph_utils.py validate -v        # Verbose validation with info messages
    python graph_utils.py audit              # Full audit report with recommendations
    python graph_utils.py audit -o report.md # Write audit to file
    python graph_utils.py list [domain]      # List nodes (optionally by domain)
    python graph_utils.py connections        # Show connection network
    python graph_utils.py untraced           # List claims needing source tracing
    python graph_utils.py export-md          # Export to markdown for GitHub viewing
    python graph_utils.py confidence         # Show all confidence scores
    python graph_utils.py score NODE_ID      # Calculate score for specific node
    python graph_utils.py low-confidence     # Find nodes with low confidence
    python graph_utils.py needs-extraction   # List evidence nodes without confidence_factors
    python graph_utils.py persist-scores     # Calculate and write confidence scores to graph
    python graph_utils.py chain-check NODE_ID # Analyze a node's chain completeness
    python graph_utils.py warnings           # Show warnings by type (chain, inverse, cardinality)
    python graph_utils.py add-connection -s SRC -T TGT -c TYPE [--note "..."] [--dry-run]
    python graph_utils.py fix-inverses       # Add any missing inverse connections (supports dry-run)

Connection Validation (strict minimal chain):
    - DEVELOPMENT: foundational → concept → hypothesis (develops/developed_by)
    - EPISTEMIC: evidence → hypothesis (supports/contradicts)
    - INTEGRATION: concept → synthesis (integrates_into/integrated_from)
    - PEER: same-level parallels/contrasts; STRUCTURAL: requires/required_by
    No skip links are allowed (e.g., evidence→concept, hypothesis→synthesis).

Options:
    -j, --json       Output as JSON
    -v, --verbose    Include informational messages
    -o, --output     Write output to file
    -d, --domain     Filter by domain ID
    -t, --threshold  Confidence threshold (default: 0.50)
"""

import sys
import yaml
import json
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime, date
from copy import deepcopy


class DateEncoder(json.JSONEncoder):
    """Custom JSON encoder that handles date and datetime objects."""
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)


# Paths
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
GRAPH_PATH = REPO_ROOT / "graph" / "knowledge_graph.yaml"
MARKDOWN_PATH = REPO_ROOT / "graph" / "knowledge_graph.md"


# =============================================================================
# CONFIDENCE SCORING SYSTEM
# =============================================================================
# Evidence nodes have intrinsic confidence from empirical factors.
# All other nodes derive confidence from their evidence base.
# Scores are calculated from enum values written by the Confidence Extractor agent.

# Enum-to-score mappings for intrinsic confidence factors

# ===== SHARED FACTORS (both tracks) =====
METHODOLOGY_SCORES = {
    "randomized_controlled": 1.0,
    "prospective": 0.85,
    "retrospective": 0.70,
    "observational": 0.65,
    "textual_critical": 0.60,
    "case_study": 0.50,
    "theoretical": 0.30,
    "na": 0.50,  # Neutral default
}

SAMPLE_SIZE_SCORES = {
    "population": 1.0,
    "large_1000+": 0.95,
    "medium_100-999": 0.75,
    "small_10-99": 0.50,
    "minimal_<10": 0.25,
    "na": 0.50,
}

REPLICATION_SCORES = {
    "independent_replicated": 1.0,
    "internal_replicated": 0.75,
    "single_study": 0.50,
    "unreplicated": 0.25,
    "na": 0.50,
}

# ===== EXTERNAL TRACK FACTORS =====
# For cited peer-reviewed studies: traditional scientific validation
PEER_REVIEW_SCORES = {
    "peer_reviewed_journal": 1.0,
    "peer_reviewed_book": 0.90,
    "dissertation": 0.75,
    "preprint": 0.50,
    "unpublished": 0.30,
    "primary_text": 0.80,  # Primary texts have inherent authority
    "na": 0.50,  # Use na for internal track
}

# ===== INTERNAL TRACK FACTORS =====
# For our analyses: transparency + critic review as validation
METHODOLOGICAL_TRANSPARENCY_SCORES = {
    "full": 1.0,       # Complete methodology documented, all steps traceable
    "high": 0.85,      # Methodology documented with minor gaps
    "moderate": 0.65,  # Key methods documented but some steps unclear
    "low": 0.40,       # Limited documentation
    "minimal": 0.20,   # Methods not documented
    "na": 0.50,        # Use na for external track
}

SOURCE_DATA_QUALITY_SCORES = {
    "peer_reviewed_database": 1.0,    # NDERF, IANDS, DOPS
    "institutional_database": 0.85,   # Institutional but non-peer-reviewed
    "curated_corpus": 0.75,           # Carefully curated textual corpus
    "mixed_sources": 0.65,            # Multiple source types
    "web_scraped": 0.45,              # Web-scraped data
    "na": 0.50,                       # Use na for external track
}

CRITIC_REVIEWED_SCORES = {
    "reviewed_no_issues": 1.0,        # Critic reviewed, no proof-breaking issues
    "reviewed_minor_issues": 0.80,    # Minor issues noted
    "reviewed_major_issues": 0.60,    # Major issues addressed
    "reviewed_unresolved": 0.30,      # Unresolved proof-breaking issues
    "not_reviewed": 0.50,             # Not yet reviewed
}

# ===== SOURCE CHAIN (both tracks) =====
SOURCE_CHAIN_QUALITY_SCORES = {
    "primary_verified": 1.0,
    "primary_unverified": 0.80,
    "mixed": 0.70,
    "secondary": 0.60,
    "tertiary": 0.40,
    "web": 0.50,
}

# ===== WEIGHTS FOR COMBINING FACTORS =====
# External track: peer_review matters, transparency factors ignored
EXTERNAL_WEIGHTS = {
    "methodology": 0.30,
    "sample_size": 0.20,
    "replication": 0.25,
    "peer_review": 0.15,
    "source_chain_quality": 0.10,
}

# Internal track: transparency matters, peer_review ignored
# Critic review is primary validation mechanism
INTERNAL_WEIGHTS = {
    "methodology": 0.25,
    "sample_size": 0.20,
    "replication": 0.15,
    "methodological_transparency": 0.20,  # Can others trace our work?
    "source_data_quality": 0.10,          # Quality of underlying data
    "critic_reviewed": 0.10,              # Our peer review mechanism
}

# Legacy support - maps to external by default
INTRINSIC_WEIGHTS = EXTERNAL_WEIGHTS

# Node type caps (foundational claims can't be "high" without extensive evidence)
NODE_TYPE_CAPS = {
    "foundational": 0.70,
    "concept": 0.85,
    "hypothesis": 0.90,
    "evidence": 1.00,
    "synthesis": 0.85,
}

# Penalty for open proof-breaking critiques
PROOF_BREAKING_PENALTY = 0.25


# =============================================================================
# CONNECTION TYPE VALIDATION RULES
# =============================================================================
# The knowledge graph enforces a bidirectional chain structure:
#
#   DEVELOPMENT FLOW (top-down, concepts becoming specific):
#     foundational → concept → hypothesis → [evidence validates]
#     "develops", "produces", "operationalizes"
#
#   EPISTEMIC FLOW (bottom-up, confidence flowing upward):
#     evidence → hypothesis → concept → foundational
#     "supports", "validates"
#
# These are the SAME chain viewed from different directions.
# Violations indicate structural problems that need fixing.
#
# SYNTHESIS nodes integrate multiple nodes and can connect more freely.

# =============================================================================
# CARDINALITY RULES
# =============================================================================
# Some connections have implied cardinality:
#
# ONE-TO-MANY (one source, many targets):
#   - develops: one concept develops into many hypotheses
#   - produces: one foundational produces many concepts
#   - contains: one node contains many parts
#
# MANY-TO-ONE (many sources, one target):
#   - supports/validates: many evidence nodes support one hypothesis
#   - instantiates: many examples instantiate one concept
#   - supported_by/validated_by: receiving support from many sources
#
# SYMMETRIC (direction doesn't matter):
#   - parallels, contrasts, intersects

# Minimal connection type sets (strict chain, no skips)
EVIDENCE_SUPPORT = {'supports'}              # evidence → hypothesis
EVIDENCE_SUPPORT_INV = {'supported_by'}      # hypothesis → evidence (inverse)
EVIDENCE_OPPOSITION = {'contradicts'}        # evidence → hypothesis (refutation)
EVIDENCE_OPPOSITION_INV = {'contradicted_by'}# hypothesis → evidence (inverse)
CHAIN_DOWN = {'develops'}                    # foundational → concept → hypothesis
CHAIN_DOWN_INV = {'developed_by'}            # inverse of develops
INTEGRATION = {'integrates_into'}            # concept → synthesis
INTEGRATION_INV = {'integrated_from'}        # inverse of integrates_into
PEER = {'parallels', 'contrasts'}            # same-level observational
STRUCTURAL = {'requires', 'required_by'}     # same-level dependency

# All valid relationship types
ALL_VALID_TYPES = (
    EVIDENCE_SUPPORT | EVIDENCE_SUPPORT_INV |
    EVIDENCE_OPPOSITION | EVIDENCE_OPPOSITION_INV |
    CHAIN_DOWN | CHAIN_DOWN_INV |
    INTEGRATION | INTEGRATION_INV |
    PEER | STRUCTURAL
)

# =============================================================================
# CONNECTION RULES BY NODE TYPE PAIR
# =============================================================================
# Format: (source_type, target_type): {allowed connection types}
#
# =============================================================================
# CORE CHAIN PRINCIPLE:
# =============================================================================
# DEVELOPMENT flows DOWN:  Foundational → Concept → Hypothesis → Evidence
# EPISTEMIC flows UP:      Evidence → Hypothesis → Concept → Foundational
#
# CRITICAL: Epistemic support must flow LEVEL BY LEVEL, not skip levels:
#   - Evidence supports/validates → Hypothesis (one level up)
#   - Hypothesis supports → Concept (one level up)  
#   - Concept supports → Foundational (one level up)
#
# Evidence NEVER receives epistemic support from non-evidence.
# Foundational NEVER receives direct epistemic support from evidence/hypothesis.
#
# =============================================================================
# SYNTHESIS: HORIZONTAL INTEGRATION
# =============================================================================
# Synthesis is PEER to Foundational, not vertically above it.
# - Synthesis = integration of validated concepts from potentially MULTIPLE foundational domains
# - Synthesis RECEIVES from concepts (concept → synthesis via integrates_into)
# - Synthesis does NOT support foundational (axioms cannot be proven by synthesis)
# - Synthesis can bridge ACROSS foundational domains (cross-domain integration)
#
# Think of it as: Foundational (axiomatic starting points) | Synthesis (derived integrations)
# Both are "high level" but different in kind.
# =============================================================================

CONNECTION_TYPE_RULES = {
    # === FOUNDATIONAL ===
    ('foundational', 'foundational'): PEER,
    ('foundational', 'concept'):      CHAIN_DOWN,
    ('foundational', 'hypothesis'):   set(),  # NO SKIP
    ('foundational', 'evidence'):     set(),  # NO SKIP
    ('foundational', 'synthesis'):    PEER,

    # === CONCEPT ===
    ('concept', 'foundational'):      CHAIN_DOWN_INV,
    ('concept', 'concept'):           PEER | STRUCTURAL,
    ('concept', 'hypothesis'):        CHAIN_DOWN,
    ('concept', 'evidence'):          set(),  # NO SKIP
    ('concept', 'synthesis'):         INTEGRATION,

    # === HYPOTHESIS ===
    ('hypothesis', 'foundational'):   set(),  # NO SKIP
    ('hypothesis', 'concept'):        CHAIN_DOWN_INV,
    ('hypothesis', 'hypothesis'):     PEER | STRUCTURAL,
    ('hypothesis', 'evidence'):       EVIDENCE_SUPPORT_INV | EVIDENCE_OPPOSITION_INV,
    ('hypothesis', 'synthesis'):      set(),  # NO SKIP

    # === EVIDENCE ===
    ('evidence', 'foundational'):     set(),  # NO SKIP
    ('evidence', 'concept'):          set(),  # NO SKIP
    ('evidence', 'hypothesis'):       EVIDENCE_SUPPORT | EVIDENCE_OPPOSITION,
    ('evidence', 'evidence'):         PEER,
    ('evidence', 'synthesis'):        set(),  # NO SKIP

    # === SYNTHESIS ===
    ('synthesis', 'foundational'):    PEER,
    ('synthesis', 'concept'):         INTEGRATION_INV,
    ('synthesis', 'hypothesis'):      set(),  # NO SKIP
    ('synthesis', 'evidence'):        set(),  # NO SKIP
    ('synthesis', 'synthesis'):       PEER | INTEGRATION | INTEGRATION_INV,
}

# Semantic inverses - when A→B exists, B→A should use the inverse type
CONNECTION_INVERSES = {
    'develops': 'developed_by',
    'developed_by': 'develops',
    'integrates_into': 'integrated_from',
    'integrated_from': 'integrates_into',
    'requires': 'required_by',
    'required_by': 'requires',
    'supports': 'supported_by',
    'supported_by': 'supports',
    'contradicts': 'contradicted_by',
    'contradicted_by': 'contradicts',
    # Symmetric connections
    'parallels': 'parallels',
    'contrasts': 'contrasts',
    'contradicts': 'contradicts',
}

def calculate_intrinsic_confidence(factors: dict) -> float:
    """
    Calculate intrinsic confidence score from enum factors.
    Used for evidence nodes.
    
    DUAL-TRACK SYSTEM:
    - External sources (source_type: external): Uses peer_review factor
    - Internal sources (source_type: internal): Uses transparency factors + critic_reviewed
    
    If source_type not specified, infers from factors present.
    """
    if not factors:
        return 0.0
    
    # Determine which track to use
    source_type = factors.get('source_type', None)
    
    if source_type is None:
        # Infer from factors present
        has_internal_factors = any(f in factors for f in 
            ['methodological_transparency', 'source_data_quality', 'critic_reviewed'])
        source_type = 'internal' if has_internal_factors else 'external'
    
    # Select appropriate weights
    weights = INTERNAL_WEIGHTS if source_type == 'internal' else EXTERNAL_WEIGHTS
    
    # Build score maps based on track
    if source_type == 'internal':
        score_maps = {
            "methodology": METHODOLOGY_SCORES,
            "sample_size": SAMPLE_SIZE_SCORES,
            "replication": REPLICATION_SCORES,
            "methodological_transparency": METHODOLOGICAL_TRANSPARENCY_SCORES,
            "source_data_quality": SOURCE_DATA_QUALITY_SCORES,
            "critic_reviewed": CRITIC_REVIEWED_SCORES,
        }
    else:
        score_maps = {
            "methodology": METHODOLOGY_SCORES,
            "sample_size": SAMPLE_SIZE_SCORES,
            "replication": REPLICATION_SCORES,
            "peer_review": PEER_REVIEW_SCORES,
            "source_chain_quality": SOURCE_CHAIN_QUALITY_SCORES,
        }
    
    score = 0.0
    total_weight = 0.0
    
    for factor, weight in weights.items():
        value = factors.get(factor)
        # Skip factors that are 'na' - they should not contribute to score
        if value and value != 'na' and factor in score_maps:
            factor_score = score_maps[factor].get(value, 0.5)
            score += factor_score * weight
            total_weight += weight
    
    if total_weight > 0:
        return score / total_weight  # Weighted average
    return 0.0


def calculate_derived_confidence(node_id: str, nodes: dict, flat_connections: list = None, visited: set = None) -> float:
    """
    Calculate derived confidence from direct supporting connections.
    Aligns to the minimal chain: evidence → hypothesis → concept → foundational, concept → synthesis.
    Only considers adjacent-level, allowed connection types.
    """
    if visited is None:
        visited = set()
    if node_id in visited:
        return 0.0
    visited.add(node_id)

    node = nodes.get(node_id, {})
    node_type = node.get('node_type', 'concept')

    if node_type == 'evidence':
        factors = node.get('confidence_factors', {})
        return calculate_intrinsic_confidence(factors)

    # Build inbound map once
    inbound = defaultdict(list)
    for other_id, other_node in nodes.items():
        for conn in other_node.get('connections', []):
            tgt = conn.get('target')
            if tgt and tgt in nodes:
                inbound[tgt].append({
                    'source': other_id,
                    'source_type': other_node.get('node_type', 'concept'),
                    'type': conn.get('type'),
                })

    # Allowed inbound support by node_type
    support_matrix = {
        'hypothesis': {'supports': {'evidence'}},
        'concept': {'developed_by': {'hypothesis'}},
        'foundational': {'developed_by': {'concept'}},
        'synthesis': {'integrated_from': {'concept'}},
    }

    evidence_scores = []
    inbound_list = inbound.get(node_id, [])
    allowed = support_matrix.get(node_type, {})

    for inc in inbound_list:
        conn_type = inc.get('type')
        src_type = inc.get('source_type')
        src_id = inc.get('source')

        if conn_type not in allowed:
            continue
        if src_type not in allowed[conn_type]:
            continue
        if src_id not in nodes:
            continue

        src_node = nodes[src_id]
        if src_type == 'evidence':
            score = calculate_intrinsic_confidence(src_node.get('confidence_factors', {}))
        else:
            score = src_node.get('confidence', 0.30)

        if score > 0.30:
            # Slight attenuation for non-evidence sources
            evidence_scores.append(score if src_type == 'evidence' else score * 0.85)

    if evidence_scores:
        base_score = max(evidence_scores)
        strong_streams = [s for s in evidence_scores if s >= 0.60]
        stream_bonus = min(0.1, max(0, (len(strong_streams) - 1) * 0.03))
        return min(1.0, base_score + stream_bonus)

    return 0.30


def get_node_cycles(node_id: str, nodes: dict) -> list:
    """
    Check if a specific node is involved in any circular proof chains.
    Returns list of cycles the node participates in (empty if none).
    """
    all_cycles = detect_proof_cycles(nodes)
    node_cycles = []
    for cycle in all_cycles:
        if node_id in cycle:
            node_cycles.append(cycle)
    return node_cycles


def calculate_node_confidence(node_id: str, nodes: dict, flat_connections: list = None) -> dict:
    """
    Calculate full confidence assessment for a node.
    Returns dict with score, label, and breakdown.
    
    IMPORTANT: If node is part of a circular proof chain, returns
    score=0 and label='circular' as cycles are epistemologically invalid.
    
    Args:
        node_id: The node to calculate confidence for
        nodes: Dictionary of all nodes
        flat_connections: Optional flat list of [source, type, target] connections
    """
    node = nodes.get(node_id, {})
    node_type = node.get('node_type', 'concept')
    
    # Check for circular proof chains FIRST
    cycles = get_node_cycles(node_id, nodes)
    if cycles:
        return {
            "node_id": node_id,
            "node_type": node_type,
            "base_score": 0.0,
            "cap_applied": None,
            "capped_score": 0.0,
            "proof_breaking_penalty": None,
            "final_score": 0.0,
            "label": "circular",
            "score_source": "blocked",
            "circular_chains": [' -> '.join(c) for c in cycles],
            "error": "Node is part of circular proof chain - confidence cannot be calculated",
        }
    
    # Base score calculation
    if node_type == 'evidence':
        factors = node.get('confidence_factors', {})
        base_score = calculate_intrinsic_confidence(factors)
        score_source = "intrinsic"
    else:
        base_score = calculate_derived_confidence(node_id, nodes, flat_connections)
        score_source = "derived"
    
    # Apply node type cap
    cap = NODE_TYPE_CAPS.get(node_type, 0.85)
    capped_score = min(base_score, cap)
    
    # Apply proof-breaking penalty
    critic_notes = node.get('critic_notes', {})
    proof_breaking_count = critic_notes.get('proof_breaking_open', 0)
    penalty = proof_breaking_count * PROOF_BREAKING_PENALTY
    final_score = max(0.0, capped_score - penalty)
    
    # Determine label
    # Note: 'circular' label is handled above in cycle check
    if proof_breaking_count > 0:
        label = "contested"
    elif final_score >= 0.75:
        label = "high"
    elif final_score >= 0.50:
        label = "medium"
    elif final_score >= 0.25:
        label = "low"
    else:
        label = "preliminary"
    
    return {
        "node_id": node_id,
        "node_type": node_type,
        "base_score": round(base_score, 3),
        "cap_applied": cap if base_score > cap else None,
        "capped_score": round(capped_score, 3),
        "proof_breaking_penalty": round(penalty, 3) if penalty > 0 else None,
        "final_score": round(final_score, 3),
        "label": label,
        "score_source": score_source,
    }


def get_all_confidence_scores(graph: dict) -> list:
    """Get confidence scores for all nodes."""
    nodes = get_all_nodes(graph)
    flat_connections = graph.get('connections', []) or []
    results = []
    
    for node_id in nodes:
        result = calculate_node_confidence(node_id, nodes, flat_connections)
        result['title'] = nodes[node_id].get('title', 'Untitled')
        results.append(result)
    
    return sorted(results, key=lambda x: x['final_score'], reverse=True)


def get_low_confidence_nodes(graph: dict, threshold: float = 0.50) -> list:
    """Find nodes below confidence threshold."""
    scores = get_all_confidence_scores(graph)
    return [s for s in scores if s['final_score'] < threshold]


def get_needs_extraction(graph: dict) -> list:
    """Find evidence nodes without confidence_factors."""
    nodes = get_all_nodes(graph)
    needs = []
    
    for node_id, node in nodes.items():
        if node.get('node_type') == 'evidence':
            if not node.get('confidence_factors'):
                needs.append({
                    'id': node_id,
                    'title': node.get('title', 'Untitled'),
                    'domain': node.get('domain'),
                })
    
    return sorted(needs, key=lambda x: x['id'])


def persist_confidence_scores(graph: dict) -> dict:
    """
    Calculate confidence scores and persist them to the graph.
    
    Writes a 'confidence' property (float score) to each node that has
    confidence_factors (evidence nodes) or can derive confidence (other nodes).
    
    Returns summary of changes made.
    """
    nodes = get_all_nodes(graph)
    flat_connections = graph.get('connections', []) or []
    changes = {
        'updated': [],
        'errors': [],
        'skipped': [],
    }
    
    for node_id, node in nodes.items():
        try:
            result = calculate_node_confidence(node_id, nodes, flat_connections)
            
            # Skip circular nodes
            if result['label'] == 'circular':
                changes['errors'].append({
                    'node_id': node_id,
                    'error': 'Circular proof chain'
                })
                continue
            
            final_score = result['final_score']
            old_confidence = node.get('confidence')
            
            # Update the node in the graph
            # Need to find which section it's in
            if node_id in (graph.get('nodes', {}) or {}):
                graph['nodes'][node_id]['confidence'] = final_score
            elif node_id in (graph.get('extended_nodes', {}) or {}):
                graph['extended_nodes'][node_id]['confidence'] = final_score
            else:
                changes['errors'].append({
                    'node_id': node_id,
                    'error': 'Could not find node in graph sections'
                })
                continue
            
            changes['updated'].append({
                'node_id': node_id,
                'old': old_confidence,
                'new': final_score,
                'label': result['label'],
            })
            
        except Exception as e:
            changes['errors'].append({
                'node_id': node_id,
                'error': str(e)
            })
    
    return changes


def load_graph() -> dict:
    """Load the knowledge graph from YAML."""
    with open(GRAPH_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def save_graph(graph: dict) -> None:
    """Save the knowledge graph to YAML."""
    with open(GRAPH_PATH, 'w', encoding='utf-8') as f:
        yaml.dump(graph, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def get_all_nodes(graph: dict) -> dict:
    """Get all nodes from both 'nodes' and 'extended_nodes' sections."""
    nodes = graph.get('nodes', {}) or {}
    extended = graph.get('extended_nodes', {}) or {}
    # Merge, with extended_nodes taking precedence if duplicates
    return {**nodes, **extended}


def get_stats(graph: dict) -> dict:
    """Calculate graph statistics."""
    nodes = get_all_nodes(graph)
    untraced = graph.get('untraced', []) or []

    # Aggregate connections from node definitions (authoritative store)
    connection_set = set()
    for source_id, node in nodes.items():
        for conn in node.get('connections', []) or []:
            target = conn.get('target')
            conn_type = conn.get('type')
            if target and conn_type:
                connection_set.add((source_id, target, conn_type))
    
    # Count by status
    status_counts = defaultdict(int)
    domain_counts = defaultdict(int)
    trace_counts = defaultdict(int)
    
    for node_id, node in nodes.items():
        status_counts[node.get('status', 'unknown')] += 1
        domain_counts[node.get('domain', 'unknown')] += 1
        trace_counts[node.get('trace_status', 'unknown')] += 1
    
    return {
        'total_nodes': len(nodes),
        'total_connections': len(connection_set),
        'untraced_claims': len(untraced),
        'by_status': dict(status_counts),
        'by_domain': dict(domain_counts),
        'by_trace_status': dict(trace_counts),
    }


def detect_proof_cycles(nodes: dict) -> list:
    """
    Detect circular proof chains in the knowledge graph.
    
    Circular proofs are epistemologically invalid - A cannot prove B if B proves A.
    This function finds all cycles in proof-related connections.
    
    Args:
        nodes: Dictionary of node_id -> node data
        
    Returns:
        List of cycles, where each cycle is a list of node IDs forming the cycle
    """
    # Relationships that constitute "proof" or evidence support
    # These are the connections where confidence flows in the minimal scheme
    proof_relations = [
        'supports', 'supported_by', 'contradicts', 'contradicted_by',
        'develops', 'developed_by', 'integrates_into', 'integrated_from',
        'requires', 'required_by'
    ]

    # Collect proof edges and track by pair for inverse detection
    edges = []
    edges_by_pair = defaultdict(set)
    for node_id, node in nodes.items():
        for conn in node.get('connections', []):
            target = conn.get('target')
            rel_type = conn.get('type', '')
            if rel_type in proof_relations and target in nodes:
                edges.append((node_id, target, rel_type))
                edges_by_pair[(node_id, target)].add(rel_type)

    # Identify mutual inverse pairs (e.g., develops/developed_by) and ignore them for cycle checks
    to_skip = set()
    for src, tgt, rel in edges:
        inv = CONNECTION_INVERSES.get(rel)
        if inv and rel in proof_relations and inv in proof_relations:
            if inv in edges_by_pair.get((tgt, src), set()):
                to_skip.add((src, tgt, rel))
                to_skip.add((tgt, src, inv))

    # Build directed graph of proof relationships, excluding inverse pairs
    graph = {node_id: [] for node_id in nodes}
    for src, tgt, rel in edges:
        if (src, tgt, rel) in to_skip:
            continue
        graph[src].append((tgt, rel))
    
    # DFS-based cycle detection using coloring
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}
    cycles = []
    
    def dfs(node, path):
        color[node] = GRAY
        for neighbor, rel in graph[node]:
            if color[neighbor] == GRAY:
                # Found cycle - extract it
                try:
                    cycle_start = path.index(neighbor)
                    cycle = path[cycle_start:] + [neighbor]
                    cycles.append(cycle)
                except ValueError:
                    pass  # Shouldn't happen, but be safe
            elif color[neighbor] == WHITE:
                dfs(neighbor, path + [neighbor])
        color[node] = BLACK
    
    for node in graph:
        if color[node] == WHITE:
            dfs(node, [node])
    
    return cycles


def check_bidirectional_connections(nodes: dict) -> list:
    """
    Check for missing bidirectional connections.
    
    When node A connects to node B, there should generally be a reverse
    connection from B back to A (though the relationship type may differ).
    
    Args:
        nodes: Dictionary of node_id -> node data
        
    Returns:
        List of tuples (source, target, rel_type, expected_inverse) where reverse is missing
    """
    missing_reverse = []
    
    # Build set of all connections (source, target)
    all_connections = set()
    for node_id, node in nodes.items():
        for conn in node.get('connections', []):
            target = conn.get('target')
            if target and target in nodes:
                all_connections.add((node_id, target))
    
    # Check for missing reverse connections
    for source, target in all_connections:
        # Get the relationship type for the forward connection
        source_node = nodes[source]
        rel_type = None
        for conn in source_node.get('connections', []):
            if conn.get('target') == target:
                rel_type = conn.get('type')
                break

        expected_inverse = CONNECTION_INVERSES.get(rel_type)
        if not expected_inverse:
            continue  # No defined inverse; skip bidirectional check

        target_node = nodes[target]
        reverse_exists = any(
            conn.get('target') == source and conn.get('type') == expected_inverse
            for conn in target_node.get('connections', [])
        )
        
        if not reverse_exists:
            missing_reverse.append((source, target, rel_type, expected_inverse))
    
    return missing_reverse


def validate_connection_type(source_id: str, source_type: str, target_id: str, 
                              target_type: str, conn_type: str) -> dict:
    """
    Validate a single connection against the connection type rules.
    
    Returns:
        dict with 'valid' bool, 'error' str (if invalid), 'suggestion' str (if applicable)
    """
    key = (source_type, target_type)
    
    # Check if this node type pair has rules defined
    if key not in CONNECTION_TYPE_RULES:
        return {
            'valid': False,
            'error': f"No rules defined for {source_type} -> {target_type}",
            'suggestion': "Add rules to CONNECTION_TYPE_RULES or review node types",
        }
    
    allowed = CONNECTION_TYPE_RULES[key]
    
    if conn_type in allowed:
        return {'valid': True}
    
    # Connection type not allowed - suggest alternatives
    return {
        'valid': False,
        'error': f"'{conn_type}' not allowed for {source_type} -> {target_type}",
        'suggestion': f"Allowed types: {', '.join(sorted(allowed))}",
        'source_id': source_id,
        'target_id': target_id,
    }


def check_connection_types(nodes: dict) -> list:
    """
    Check all connections against the connection type rules matrix.
    
    Returns:
        List of validation issues with actionable details
    """
    issues = []
    
    for node_id, node in nodes.items():
        source_type = node.get('node_type', 'concept')
        
        for conn in node.get('connections', []):
            target_id = conn.get('target')
            conn_type = conn.get('type')
            
            if not target_id or target_id not in nodes:
                continue  # Handled by other validation
            
            target_node = nodes[target_id]
            target_type = target_node.get('node_type', 'concept')
            
            result = validate_connection_type(
                node_id, source_type, target_id, target_type, conn_type
            )
            
            if not result['valid']:
                issues.append({
                    'type': 'invalid_connection_type',
                    'source': node_id,
                    'source_type': source_type,
                    'target': target_id,
                    'target_type': target_type,
                    'connection_type': conn_type,
                    'error': result['error'],
                    'suggestion': result['suggestion'],
                })
    
    return issues


def check_missing_inverse_connections(nodes: dict) -> list:
    """
    Check for connections that should have a semantic inverse.
    
    When A --supports--> B exists, B --supported_by--> A should also exist.
    This ensures the bidirectional chain is complete.
    
    Returns:
        List of missing inverse connection recommendations
    """
    missing = []
    
    for node_id, node in nodes.items():
        for conn in node.get('connections', []):
            target_id = conn.get('target')
            conn_type = conn.get('type')
            
            if not target_id or target_id not in nodes:
                continue
            
            # Get expected inverse type
            expected_inverse = CONNECTION_INVERSES.get(conn_type)
            if not expected_inverse:
                continue  # No inverse defined for this type
            
            # Check if target has the inverse connection back
            target_node = nodes[target_id]
            has_inverse = any(
                tc.get('target') == node_id and tc.get('type') == expected_inverse
                for tc in target_node.get('connections', [])
            )
            
            if not has_inverse:
                # Also check if ANY connection back exists (might use different but valid type)
                has_any_reverse = any(
                    tc.get('target') == node_id
                    for tc in target_node.get('connections', [])
                )
                
                missing.append({
                    'source': node_id,
                    'target': target_id,
                    'connection_type': conn_type,
                    'expected_inverse': expected_inverse,
                    'has_any_reverse': has_any_reverse,
                    'fix': f"Add to {target_id}: {{ target: {node_id}, type: {expected_inverse} }}",
                })
    
    return missing


def check_chain_completeness(nodes: dict) -> list:
    """
    Check that nodes connect to the proper NODE TYPE LEVELS in the chain.
    
    Chain: Foundational → Concept → Hypothesis → Evidence
    
    Each node type must connect to adjacent levels:
    - Evidence → must connect to hypothesis (upward)
    - Hypothesis → must connect to concept (upward), should have evidence (downward)
    - Concept → must connect to foundational (upward), should have hypothesis (downward)
    - Foundational → should have concept (downward)
    - Synthesis → should have concept inputs
    
    Returns:
        List of chain completeness warnings
    """
    warnings = []

    # Build reverse index for quick inbound lookup
    inbound = {nid: [] for nid in nodes}
    for src_id, src_node in nodes.items():
        for conn in src_node.get('connections', []):
            tgt = conn.get('target')
            if tgt in inbound:
                inbound[tgt].append({
                    'from': src_id,
                    'from_type': src_node.get('node_type'),
                    'type': conn.get('type'),
                })

    for node_id, node in nodes.items():
        ntype = node.get('node_type', 'concept')
        conns = node.get('connections', [])
        inbound_list = inbound.get(node_id, [])

        if ntype == 'evidence':
            has_hyp = any(
                c.get('target') in nodes and nodes[c['target']].get('node_type') == 'hypothesis' and c.get('type') in {'supports', 'contradicts'}
                for c in conns
            )
            if not has_hyp:
                warnings.append({
                    'type': 'missing_upward_chain',
                    'node': node_id,
                    'node_type': ntype,
                    'warning': 'Evidence not connected to any hypothesis',
                    'fix': f"Add supports/contradicts from {node_id} to a hypothesis",
                })
            continue

        if ntype == 'hypothesis':
            has_concept_link = any(
                c.get('type') == 'developed_by' and c.get('target') in nodes and nodes[c['target']].get('node_type') == 'concept'
                for c in conns
            ) or any(
                inc.get('from_type') == 'concept' and inc.get('type') == 'develops'
                for inc in inbound_list
            )

            has_evidence = any(inc.get('from_type') == 'evidence' and inc.get('type') == 'supports' for inc in inbound_list)

            if not has_concept_link:
                warnings.append({
                    'type': 'missing_upward_chain',
                    'node': node_id,
                    'node_type': ntype,
                    'warning': 'Hypothesis not connected to any concept (developed_by/develops)',
                    'fix': f"Link {node_id} to a concept via developed_by (or add concept develops {node_id})",
                })
            if not has_evidence:
                warnings.append({
                    'type': 'missing_downward_chain',
                    'node': node_id,
                    'node_type': ntype,
                    'warning': 'Hypothesis has no supporting evidence',
                    'fix': f"Add evidence supports {node_id}",
                })
            continue

        if ntype == 'concept':
            has_foundational = any(
                inc.get('from_type') == 'foundational' and inc.get('type') == 'develops'
                for inc in inbound_list
            ) or any(
                c.get('type') == 'developed_by' and c.get('target') in nodes and nodes[c['target']].get('node_type') == 'foundational'
                for c in conns
            )

            has_hypothesis = any(
                c.get('type') == 'develops' and c.get('target') in nodes and nodes[c['target']].get('node_type') == 'hypothesis'
                for c in conns
            ) or any(
                inc.get('from_type') == 'hypothesis' and inc.get('type') == 'developed_by'
                for inc in inbound_list
            )

            if not has_foundational:
                warnings.append({
                    'type': 'missing_upward_chain',
                    'node': node_id,
                    'node_type': ntype,
                    'warning': 'Concept not connected to any foundational node',
                    'fix': f"Connect to a foundational via develops/developed_by",
                })
            if not has_hypothesis:
                warnings.append({
                    'type': 'missing_downward_chain',
                    'node': node_id,
                    'node_type': ntype,
                    'warning': 'Concept has no hypotheses developing from it',
                    'fix': f"Add develops from {node_id} to a hypothesis",
                })
            continue

        if ntype == 'foundational':
            has_concept = any(
                c.get('type') == 'develops' and c.get('target') in nodes and nodes[c['target']].get('node_type') == 'concept'
                for c in conns
            ) or any(
                inc.get('from_type') == 'concept' and inc.get('type') == 'developed_by'
                for inc in inbound_list
            )
            if not has_concept:
                warnings.append({
                    'type': 'missing_downward_chain',
                    'node': node_id,
                    'node_type': ntype,
                    'warning': 'Foundational has no concepts developing from it',
                    'fix': f"Add develops from {node_id} to a concept",
                })
            continue

        if ntype == 'synthesis':
            has_concept = any(
                inc.get('from_type') == 'concept' and inc.get('type') == 'integrates_into'
                for inc in inbound_list
            ) or any(
                c.get('type') == 'integrated_from' and c.get('target') in nodes and nodes[c['target']].get('node_type') == 'concept'
                for c in conns
            )
            if not has_concept:
                warnings.append({
                    'type': 'missing_downward_chain',
                    'node': node_id,
                    'node_type': ntype,
                    'warning': 'Synthesis has no concept inputs',
                    'fix': f"Add concept integrates_into {node_id} (or {node_id} integrated_from concept)",
                })
            continue

    return warnings


def get_node_chain_analysis(node_id: str, nodes: dict) -> dict:
    """
    Analyze a node's position in the development/epistemic chain.
    
    Returns detailed analysis of:
    - Upward chain (toward foundational)
    - Downward chain (toward evidence)
    - Chain completeness score
    """
    node = nodes.get(node_id, {})
    node_type = node.get('node_type', 'concept')
    
    # Build upward chain (toward foundational/concepts)
    upward_chain = []
    upward_visited = {node_id}
    upward_types = ['developed_by', 'integrated_from', 'required_by']
    
    def trace_upward(nid, depth=0):
        if depth > 10:  # Prevent infinite loops
            return
        n = nodes.get(nid, {})
        for conn in n.get('connections', []):
            if conn.get('type') in upward_types:
                target = conn.get('target')
                if target and target not in upward_visited and target in nodes:
                    upward_visited.add(target)
                    upward_chain.append({
                        'node': target,
                        'via': conn.get('type'),
                        'depth': depth + 1,
                        'type': nodes[target].get('node_type'),
                    })
                    trace_upward(target, depth + 1)
    
    trace_upward(node_id)
    
    # Build downward chain (toward evidence)
    downward_chain = []
    downward_visited = {node_id}
    downward_types = ['develops', 'integrates_into', 'requires', 'supports', 'contradicts']
    
    def trace_downward(nid, depth=0):
        if depth > 10:
            return
        n = nodes.get(nid, {})
        for conn in n.get('connections', []):
            if conn.get('type') in downward_types:
                target = conn.get('target')
                if target and target not in downward_visited and target in nodes:
                    downward_visited.add(target)
                    downward_chain.append({
                        'node': target,
                        'via': conn.get('type'),
                        'depth': depth + 1,
                        'type': nodes[target].get('node_type'),
                    })
                    trace_downward(target, depth + 1)
    
    trace_downward(node_id)
    
    # Analyze chain completeness
    has_foundational = any(c['type'] == 'foundational' for c in upward_chain)
    has_evidence = any(c['type'] == 'evidence' for c in downward_chain)
    
    # Calculate completeness score
    completeness = 0.0
    if node_type == 'foundational':
        completeness = 1.0 if downward_chain else 0.5
    elif node_type == 'evidence':
        completeness = 1.0 if upward_chain else 0.5
    else:
        # Middle nodes should have both directions
        if upward_chain and downward_chain:
            completeness = 1.0
        elif upward_chain or downward_chain:
            completeness = 0.5
        else:
            completeness = 0.0
    
    return {
        'node_id': node_id,
        'node_type': node_type,
        'upward_chain': upward_chain,
        'downward_chain': downward_chain,
        'has_foundational_path': has_foundational,
        'has_evidence_path': has_evidence,
        'chain_completeness': completeness,
        'is_isolated': not upward_chain and not downward_chain,
    }


def check_cardinality_rules(nodes: dict) -> list:
    """
    Check cardinality constraints on connections.
    
    EPISTEMIC SUPPORT should be MANY-TO-ONE:
    - Many evidence → one hypothesis
    - Many hypotheses → one concept
    - Many concepts → one foundational
    
    INTEGRATION should be MANY-TO-ONE:
    - Many concepts → one synthesis
    
    These are WARNINGS, not errors - the chain isn't broken, but
    indicates potential issues with confidence dilution or insufficient grounding.
    
    Returns:
        List of warning dictionaries
    """
    warnings = []
    
    # Track outbound epistemic connections per node
    epistemic_types = {'supports'}
    integration_types = {'integrates_into'}
    
    # Count outbound epistemic targets per node
    outbound_epistemic = {}  # node_id -> list of targets
    
    # Count inbound epistemic sources per node  
    inbound_epistemic = {}  # node_id -> list of sources
    
    # Count inbound integration sources per synthesis
    inbound_integration = {}  # node_id -> list of sources
    
    for node_id, node in nodes.items():
        node_type = node.get('node_type')
        
        for conn in node.get('connections', []):
            target = conn.get('target')
            conn_type = conn.get('type')
            
            if not target or target not in nodes:
                continue
            
            target_type = nodes[target].get('node_type')
            
            # Track epistemic outbound (supports/validates)
            if conn_type in epistemic_types:
                if node_id not in outbound_epistemic:
                    outbound_epistemic[node_id] = []
                outbound_epistemic[node_id].append({
                    'target': target,
                    'target_type': target_type,
                    'type': conn_type
                })
                
                # Track inbound for target
                if target not in inbound_epistemic:
                    inbound_epistemic[target] = []
                inbound_epistemic[target].append({
                    'source': node_id,
                    'source_type': node_type,
                    'type': conn_type
                })
            
            # Track integration (concept → synthesis)
            if conn_type in integration_types:
                if target not in inbound_integration:
                    inbound_integration[target] = []
                inbound_integration[target].append({
                    'source': node_id,
                    'source_type': node_type
                })
    
    # === CHECK: Evidence supporting too many targets ===
    # Thresholds
    EPISTEMIC_OUTBOUND_WARN = 3  # If evidence/hypothesis supports more than this, warn
    
    for node_id, targets in outbound_epistemic.items():
        node = nodes[node_id]
        node_type = node.get('node_type')
        
        # Only check evidence for "spreading too thin"
        if node_type == 'evidence':
            if len(targets) > EPISTEMIC_OUTBOUND_WARN:
                target_domains = set(nodes[t['target']].get('domain') for t in targets)
                warnings.append({
                    'node': node_id,
                    'node_type': node_type,
                    'warning_type': 'epistemic_spread',
                    'count': len(targets),
                    'threshold': EPISTEMIC_OUTBOUND_WARN,
                    'domains': len(target_domains),
                    'message': f"supports {len(targets)} targets (threshold: {EPISTEMIC_OUTBOUND_WARN}) across {len(target_domains)} domain(s) - consider splitting the evidence scope"
                })
    
    # === CHECK: Hypothesis with insufficient evidence ===
    # NOTE: A single strong evidence node IS valid. The confidence scoring system
    # reflects quality via confidence_factors. This check ensures at least ONE
    # evidence connection exists, not that multiple exist.
    EVIDENCE_SUPPORT_MIN = 1  # Hypothesis needs at least one evidence supporter
    
    for node_id, node in nodes.items():
        if node.get('node_type') == 'hypothesis':
            sources = inbound_epistemic.get(node_id, [])
            evidence_sources = [s for s in sources if s['source_type'] == 'evidence']
            
            if len(evidence_sources) < EVIDENCE_SUPPORT_MIN:
                warnings.append({
                    'node': node_id,
                    'node_type': 'hypothesis',
                    'warning_type': 'insufficient_evidence',
                    'count': len(evidence_sources),
                    'threshold': EVIDENCE_SUPPORT_MIN,
                    'message': f"has no evidence supporters - hypothesis is untested"
                })
    
    # === CHECK: Synthesis with insufficient concept inputs ===
    SYNTHESIS_INPUT_MIN = 2  # Synthesis should integrate at least this many concepts

    for node_id, node in nodes.items():
        if node.get('node_type') == 'synthesis':
            sources = inbound_integration.get(node_id, [])
            total_concept_inputs = len(sources)
            if total_concept_inputs < SYNTHESIS_INPUT_MIN:
                warnings.append({
                    'node': node_id,
                    'node_type': 'synthesis',
                    'warning_type': 'insufficient_integration',
                    'count': total_concept_inputs,
                    'threshold': SYNTHESIS_INPUT_MIN,
                    'message': f"integrates only {total_concept_inputs} concept(s) (minimum: {SYNTHESIS_INPUT_MIN}) - may not be true synthesis"
                })
    
    return warnings


def validate_graph(graph: dict, verbose: bool = False) -> dict:
    """
    Comprehensive graph validation. Returns structured report with all issues.
    
    Args:
        graph: The loaded knowledge graph
        verbose: If True, include informational messages not just errors
    
    Returns:
        dict with 'issues' list, 'warnings' list, 'summary' dict
    """
    issues = []      # Errors that must be fixed
    warnings = []    # Issues that should be addressed
    info = []        # Informational notes
    
    nodes = get_all_nodes(graph)
    metadata = graph.get('metadata', {})
    
    # Get valid values from metadata
    valid_domains = {d['id'] for d in metadata.get('domains', [])}
    valid_statuses = set(metadata.get('statuses', {}).keys())
    valid_relationships = set(metadata.get('relationship_types', {}).keys())
    valid_node_types = set(metadata.get('node_types', {}).keys())
    
    # Get valid enum values for confidence factors
    confidence_enums = metadata.get('confidence_factor_enums', {})
    valid_methodology = set(confidence_enums.get('methodology', {}).keys())
    valid_sample_size = set(confidence_enums.get('sample_size', {}).keys())
    valid_replication = set(confidence_enums.get('replication', {}).keys())
    valid_peer_review = set(confidence_enums.get('peer_review', {}).keys())
    valid_source_quality = set(confidence_enums.get('source_chain_quality', {}).keys())
    
    # Track statistics
    stats = {
        'total_nodes': len(nodes),
        'evidence_nodes': 0,
        'evidence_with_factors': 0,
        'evidence_missing_factors': 0,
        'nodes_with_critiques': 0,
        'nodes_never_reviewed': 0,
        'proof_breaking_open': 0,
        'orphan_nodes': 0,
        'missing_source_chain': 0,
        'missing_node_type': 0,
        'invalid_connections': 0,
        'circular_proof_chains': 0,
        'missing_bidirectional': 0,
    }
    
    # Required fields for all nodes
    required_fields = ['title', 'domain', 'node_type', 'status', 'definition', 'source_chain']

    # Allowed fields per node type (to constrain agent divergence)
    common_allowed = {
        'title', 'domain', 'node_type', 'status', 'definition', 'source_chain', 'connections',
        'trace_status', 'critic_notes', 'notes', 'created', 'updated', 'id', 'confidence'
    }
    evidence_allowed = common_allowed | {'confidence_factors'}
    
    for node_id, node in nodes.items():
        node_issues = []
        node_warnings = []
        
        # === STRUCTURAL VALIDATION ===

        # Enforce allowed fields per node_type to limit divergence
        node_keys = set(node.keys())
        node_type = node.get('node_type')
        if node_type == 'evidence':
            unknown_fields = node_keys - evidence_allowed
        else:
            unknown_fields = node_keys - common_allowed
        if unknown_fields:
            node_issues.append(f"Unknown fields present: {sorted(unknown_fields)}")
        
        # Check required fields
        for field in required_fields:
            if not node.get(field):
                if field == 'source_chain':
                    stats['missing_source_chain'] += 1
                    node_issues.append(f"Missing required field: {field}")
                elif field == 'node_type':
                    stats['missing_node_type'] += 1
                    node_issues.append(f"Missing required field: {field}")
                else:
                    node_issues.append(f"Missing required field: {field}")
        
        # Check domain validity
        domain = node.get('domain')
        if domain and domain not in valid_domains:
            node_issues.append(f"Invalid domain: '{domain}'")
        
        # Check status validity
        status = node.get('status')
        if status and status not in valid_statuses:
            node_issues.append(f"Invalid status: '{status}'")
        
        # Check node_type validity
        if node_type and node_type not in valid_node_types:
            node_issues.append(f"Invalid node_type: '{node_type}'")
        
        # Check connections
        for conn in node.get('connections', []):
            target = conn.get('target')
            conn_type = conn.get('type')
            
            if target and target not in nodes:
                stats['invalid_connections'] += 1
                node_issues.append(f"Connection to non-existent node: '{target}'")
            
            if conn_type and conn_type not in valid_relationships:
                node_issues.append(f"Invalid relationship type: '{conn_type}'")
            
            if not conn.get('note'):
                node_warnings.append(f"Connection to '{target}' missing note/explanation")
        
        # === EVIDENCE NODE VALIDATION ===
        
        if node_type == 'evidence':
            stats['evidence_nodes'] += 1
            
            factors = node.get('confidence_factors', {})
            if not factors:
                stats['evidence_missing_factors'] += 1
                node_warnings.append("Evidence node missing confidence_factors (run @confidence-extractor)")
            else:
                stats['evidence_with_factors'] += 1
                
                # Determine which track this node is on
                source_type = factors.get('source_type', 'external')  # Default to external for legacy
                
                if source_type == 'internal':
                    # INTERNAL TRACK: transparency + critic_reviewed
                    valid_transparency = ['full', 'high', 'moderate', 'low', 'minimal', 'na']
                    valid_data_quality = ['peer_reviewed_database', 'institutional_database', 
                                          'curated_corpus', 'mixed_sources', 'web_scraped', 'na']
                    valid_critic = ['reviewed_no_issues', 'reviewed_minor_issues', 
                                   'reviewed_major_issues', 'reviewed_unresolved', 'not_reviewed']
                    
                    factor_checks = [
                        ('methodology', valid_methodology, factors.get('methodology')),
                        ('sample_size', valid_sample_size, factors.get('sample_size')),
                        ('replication', valid_replication, factors.get('replication')),
                        ('methodological_transparency', valid_transparency, factors.get('methodological_transparency')),
                        ('source_data_quality', valid_data_quality, factors.get('source_data_quality')),
                        ('critic_reviewed', valid_critic, factors.get('critic_reviewed')),
                    ]
                else:
                    # EXTERNAL TRACK: peer_review + source_chain_quality
                    factor_checks = [
                        ('methodology', valid_methodology, factors.get('methodology')),
                        ('sample_size', valid_sample_size, factors.get('sample_size')),
                        ('replication', valid_replication, factors.get('replication')),
                        ('peer_review', valid_peer_review, factors.get('peer_review')),
                        ('source_chain_quality', valid_source_quality, factors.get('source_chain_quality')),
                    ]
                
                for factor_name, valid_values, actual_value in factor_checks:
                    if not actual_value:
                        node_warnings.append(f"confidence_factors.{factor_name} is missing")
                    elif valid_values and actual_value not in valid_values:
                        node_issues.append(f"Invalid confidence_factors.{factor_name}: '{actual_value}'")
        
        # === CRITIC NOTES VALIDATION ===
        
        critic_notes = node.get('critic_notes', {})
        if critic_notes:
            stats['nodes_with_critiques'] += 1
            
            # Check for required fields in critic_notes
            if not critic_notes.get('last_reviewed'):
                node_warnings.append("critic_notes missing 'last_reviewed' date")
            
            critiques = critic_notes.get('critiques', [])
            proof_breaking_count = 0
            detail_count = 0
            
            for i, critique in enumerate(critiques):
                if 'breaks_proof' not in critique:
                    node_warnings.append(f"Critique #{i+1} missing 'breaks_proof' flag")
                elif critique.get('breaks_proof') and critique.get('status') == 'open':
                    proof_breaking_count += 1
                elif not critique.get('breaks_proof') and critique.get('status') == 'open':
                    detail_count += 1
                
                if not critique.get('type'):
                    node_warnings.append(f"Critique #{i+1} missing 'type'")
                if not critique.get('description'):
                    node_warnings.append(f"Critique #{i+1} missing 'description'")
            
            # Check counts match
            recorded_pb = critic_notes.get('proof_breaking_open', 0)
            recorded_detail = critic_notes.get('detail_issues', 0)
            
            if recorded_pb != proof_breaking_count:
                node_warnings.append(f"proof_breaking_open count mismatch: recorded {recorded_pb}, actual {proof_breaking_count}")
            if recorded_detail != detail_count:
                node_warnings.append(f"detail_issues count mismatch: recorded {recorded_detail}, actual {detail_count}")
            
            stats['proof_breaking_open'] += proof_breaking_count
        else:
            stats['nodes_never_reviewed'] += 1
            if verbose:
                info.append(f"{node_id}: Never reviewed by critic")
        
        # === SOURCE CHAIN VALIDATION ===
        
        source_chain = node.get('source_chain', [])
        if source_chain:
            valid_source_types = {'P', 'S', 'T', 'E', 'W'}

            # Enforce provenance rule: non-evidence must have exactly one [T] entry
            if node_type != 'evidence':
                if len(source_chain) != 1:
                    node_issues.append("Non-evidence nodes must have exactly one [T] provenance entry")
                else:
                    src = source_chain[0]
                    if src.get('type') != 'T':
                        node_issues.append("Non-evidence provenance must be type 'T'")
                    if not src.get('ref'):
                        node_warnings.append("Provenance entry missing 'ref'")
            else:
                # Evidence nodes require full chain entries of valid types
                for i, source in enumerate(source_chain):
                    src_type = source.get('type')
                    if src_type not in valid_source_types:
                        node_warnings.append(f"Source #{i+1} has invalid type: '{src_type}'")
                    if not source.get('ref'):
                        node_warnings.append(f"Source #{i+1} missing 'ref'")
        
        # Check trace_status
        trace_status = node.get('trace_status')
        if trace_status == 'untraced':
            node_warnings.append("trace_status is 'untraced' - needs source verification")
        elif trace_status == 'partial':
            if verbose:
                info.append(f"{node_id}: Source chain partially traced")
        
        # Collect issues for this node
        if node_issues:
            for issue in node_issues:
                issues.append(f"{node_id}: {issue}")
        if node_warnings:
            for warning in node_warnings:
                warnings.append(f"{node_id}: {warning}")
    
    # === GRAPH-WIDE CHECKS ===
    
    # Check for orphan nodes
    connected_nodes = set()
    for node_id, node in nodes.items():
        for conn in node.get('connections', []):
            connected_nodes.add(node_id)
            target = conn.get('target')
            if target:
                connected_nodes.add(target)
    
    orphans = set(nodes.keys()) - connected_nodes
    if orphans and len(nodes) > 1:
        stats['orphan_nodes'] = len(orphans)
        for orphan in orphans:
            warnings.append(f"{orphan}: Orphan node (no connections)")
    
    # Check for circular proof chains
    cycles = detect_proof_cycles(nodes)
    stats['circular_proof_chains'] = len(cycles)
    if cycles:
        for cycle in cycles:
            cycle_str = ' -> '.join(cycle)
            issues.append(f"CIRCULAR PROOF: {cycle_str}")
    
    # Check for missing bidirectional connections
    missing_reverse = check_bidirectional_connections(nodes)
    stats['missing_bidirectional'] = len(missing_reverse)
    if missing_reverse:
        for source, target, rel_type, expected_inverse in missing_reverse:
            warnings.append(
                f"MISSING REVERSE: {source} -> {target} ({rel_type}) missing {target} -> {source} ({expected_inverse})"
            )
    
    # === NEW: CONNECTION TYPE VALIDATION ===
    connection_type_issues = check_connection_types(nodes)
    stats['invalid_connection_types'] = len(connection_type_issues)
    for issue in connection_type_issues:
        issues.append(
            f"INVALID CONNECTION TYPE: {issue['source']} ({issue['source_type']}) "
            f"--{issue['connection_type']}--> {issue['target']} ({issue['target_type']}). "
            f"{issue['suggestion']}"
        )
    
    # === NEW: MISSING INVERSE CONNECTIONS ===
    missing_inverses = check_missing_inverse_connections(nodes)
    stats['missing_inverse_connections'] = len(missing_inverses)
    # Only warn for connections that have NO reverse at all
    critical_missing = [m for m in missing_inverses if not m['has_any_reverse']]
    stats['critical_missing_inverses'] = len(critical_missing)
    for m in critical_missing:
        warnings.append(
            f"INCOMPLETE CHAIN: {m['source']} --{m['connection_type']}--> {m['target']} "
            f"has no reverse. {m['fix']}"
        )
    
    # === NEW: CHAIN COMPLETENESS ===
    chain_warnings = check_chain_completeness(nodes)
    stats['chain_completeness_warnings'] = len(chain_warnings)
    for cw in chain_warnings:
        warnings.append(
            f"CHAIN INCOMPLETE ({cw['node_type']}): {cw['node']} - {cw['warning']}. "
            f"Fix: {cw['fix']}"
        )
    
    # === NEW: CARDINALITY RULES ===
    cardinality_warnings = check_cardinality_rules(nodes)
    stats['cardinality_warnings'] = len(cardinality_warnings)
    
    # Group by warning type for cleaner output
    epistemic_spread = [w for w in cardinality_warnings if w['warning_type'] == 'epistemic_spread']
    insufficient_evidence = [w for w in cardinality_warnings if w['warning_type'] == 'insufficient_evidence']
    insufficient_integration = [w for w in cardinality_warnings if w['warning_type'] == 'insufficient_integration']
    
    stats['epistemic_spread_warnings'] = len(epistemic_spread)
    stats['insufficient_evidence_warnings'] = len(insufficient_evidence)
    stats['insufficient_integration_warnings'] = len(insufficient_integration)
    
    for cw in cardinality_warnings:
        warnings.append(
            f"CARDINALITY ({cw['warning_type']}): {cw['node']} ({cw['node_type']}) - {cw['message']}"
        )
    
    return {
        'issues': issues,
        'warnings': warnings,
        'info': info if verbose else [],
        'summary': stats,
        'passed': len(issues) == 0,
    }


def validate_graph_legacy(graph: dict) -> list:
    """Legacy validation function for backward compatibility."""
    result = validate_graph(graph)
    return result['issues'] + result['warnings']


def list_nodes(graph: dict, domain: str = None) -> list:
    """List all nodes, optionally filtered by domain."""
    nodes = get_all_nodes(graph)
    result = []
    
    for node_id, node in nodes.items():
        if domain is None or node.get('domain') == domain:
            result.append({
                'id': node_id,
                'title': node.get('title'),
                'domain': node.get('domain'),
                'status': node.get('status'),
                'connections': len(node.get('connections', []))
            })
    
    return sorted(result, key=lambda x: x['id'])


def export_to_markdown(graph: dict) -> str:
    """Export the graph to a readable markdown format."""
    nodes = get_all_nodes(graph)
    metadata = graph.get('metadata', {})
    stats = get_stats(graph)
    untraced = graph.get('untraced', []) or []
    
    lines = [
        "# Knowledge Graph",
        "",
        "> **Auto-generated from `knowledge_graph.yaml`** — Edit the YAML file, not this document.",
        "",
        f"*Last exported: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        "",
        "---",
        "",
        "## Statistics",
        "",
        "| Metric | Count |",
        "|--------|-------|",
        f"| Total Nodes | {stats['total_nodes']} |",
        f"| Total Connections | {stats['total_connections']} |",
        f"| Untraced Claims | {stats['untraced_claims']} |",
    ]
    
    if stats['by_status']:
        lines.append("")
        lines.append("### By Status")
        lines.append("")
        for status, count in stats['by_status'].items():
            lines.append(f"- **{status}**: {count}")
    
    if stats['by_domain']:
        lines.append("")
        lines.append("### By Domain")
        lines.append("")
        for domain, count in stats['by_domain'].items():
            domain_name = next((d['name'] for d in metadata.get('domains', []) if d['id'] == domain), domain)
            lines.append(f"- **{domain_name}** ({domain}): {count}")
    
    lines.extend([
        "",
        "---",
        "",
        "## Nodes",
        "",
    ])
    
    # Group nodes by domain
    by_domain = defaultdict(list)
    for node_id, node in nodes.items():
        by_domain[node.get('domain', 'unknown')].append((node_id, node))
    
    for domain_info in metadata.get('domains', []):
        domain_id = domain_info['id']
        domain_nodes = by_domain.get(domain_id, [])
        
        lines.append(f"### {domain_info['name']}")
        lines.append(f"*{domain_info['description']}*")
        lines.append("")
        
        if not domain_nodes:
            lines.append("*No nodes in this domain yet.*")
            lines.append("")
            continue
        
        for node_id, node in sorted(domain_nodes, key=lambda x: x[0]):
            lines.append(f"#### [{node_id}] {node.get('title', 'Untitled')}")
            lines.append("")
            lines.append(f"**Status**: {node.get('status', 'unknown')} | **Confidence**: {node.get('confidence', 'unknown')}")
            lines.append("")
            lines.append(f"> {node.get('definition', 'No definition provided.')}")
            lines.append("")
            
            # Source chain
            if node.get('source_chain'):
                lines.append("**Source Chain**:")
                for i, source in enumerate(node['source_chain'], 1):
                    lines.append(f"{i}. [{source.get('type', '?')}] {source.get('ref', 'Unknown')}")
                lines.append("")
            
            # Connections
            if node.get('connections'):
                lines.append("**Connections**:")
                for conn in node['connections']:
                    lines.append(f"- → `{conn.get('target')}` ({conn.get('type')}): {conn.get('note', '')}")
                lines.append("")
            
            lines.append("---")
            lines.append("")
    
    # Untraced claims
    if untraced:
        lines.extend([
            "## Untraced Claims",
            "",
            "*Claims needing source verification:*",
            "",
        ])
        for claim in untraced:
            lines.append(f"- **Claim**: {claim.get('claim', 'Unknown')}")
            lines.append(f"  - Found in: `{claim.get('found_in', 'Unknown')}`")
            lines.append(f"  - Needed: {claim.get('needed', 'Original source')}")
            lines.append("")
    
    return "\n".join(lines)


def add_connection(graph, source_id, target_id, conn_type, note=None, dry_run=False):
    """
    Add a connection with validation and automatic inverse creation.
    
    Returns:
        dict with 'success', 'messages', 'changes' keys
    """
    result = {'success': False, 'messages': [], 'changes': []}
    
    # Get all nodes for lookup
    all_nodes = {**graph.get('nodes', {}), **graph.get('extended_nodes', {})}
    
    # Validate source exists
    if source_id not in all_nodes:
        result['messages'].append(f"ERROR: Source node '{source_id}' not found")
        return result
    
    # Validate target exists
    if target_id not in all_nodes:
        result['messages'].append(f"ERROR: Target node '{target_id}' not found")
        return result
    
    source_node = all_nodes[source_id]
    target_node = all_nodes[target_id]
    source_type = source_node.get('node_type', 'unknown')
    target_type = target_node.get('node_type', 'unknown')
    
    # Validate connection type is allowed
    type_key = (source_type, target_type)
    allowed_types = CONNECTION_TYPE_RULES.get(type_key, set())
    
    if conn_type not in allowed_types:
        result['messages'].append(
            f"ERROR: Connection type '{conn_type}' not allowed from {source_type} to {target_type}"
        )
        result['messages'].append(f"  Allowed types: {', '.join(sorted(allowed_types)) if allowed_types else 'none'}")
        return result
    
    # Check if connection already exists
    source_conns = source_node.get('connections', [])
    for conn in source_conns:
        if conn.get('target') == target_id and conn.get('type') == conn_type:
            result['messages'].append(f"WARNING: Connection already exists: {source_id} --{conn_type}--> {target_id}")
            result['success'] = True
            return result
    
    # Determine inverse connection type
    inverse_type = CONNECTION_INVERSES.get(conn_type)
    if not inverse_type:
        result['messages'].append(f"WARNING: No inverse defined for '{conn_type}', adding one-way connection only")
    
    # Prepare the forward connection
    forward_conn = {'target': target_id, 'type': conn_type}
    if note:
        forward_conn['note'] = note
    
    # Prepare the inverse connection (if applicable)
    inverse_conn = None
    if inverse_type:
        # Check if inverse already exists
        target_conns = target_node.get('connections', [])
        inverse_exists = any(
            c.get('target') == source_id and c.get('type') == inverse_type 
            for c in target_conns
        )
        if not inverse_exists:
            inverse_conn = {'target': source_id, 'type': inverse_type}
            if note:
                inverse_conn['note'] = note
    
    # Report what will be done
    result['changes'].append(f"ADD: {source_id} --{conn_type}--> {target_id}")
    if inverse_conn:
        result['changes'].append(f"ADD: {target_id} --{inverse_type}--> {source_id} (auto-inverse)")
    elif inverse_type:
        result['messages'].append(f"INFO: Inverse connection already exists: {target_id} --{inverse_type}--> {source_id}")
    
    if dry_run:
        result['success'] = True
        result['messages'].append("DRY RUN: No changes applied")
        return result
    
    # Apply changes
    # Find which section the source is in and modify
    for section_name in ['nodes', 'extended_nodes']:
        section = graph.get(section_name, {})
        if source_id in section:
            if 'connections' not in section[source_id]:
                section[source_id]['connections'] = []
            section[source_id]['connections'].append(forward_conn)
            break
    
    # Add inverse connection if needed
    if inverse_conn:
        for section_name in ['nodes', 'extended_nodes']:
            section = graph.get(section_name, {})
            if target_id in section:
                if 'connections' not in section[target_id]:
                    section[target_id]['connections'] = []
                section[target_id]['connections'].append(inverse_conn)
                break
    
    result['success'] = True
    result['messages'].append("Changes applied successfully")
    return result


def fix_missing_inverses(graph, dry_run=False):
    """
    Find and fix all missing inverse connections.
    
    Returns:
        dict with 'fixed', 'skipped', 'messages' keys
    """
    result = {'fixed': [], 'skipped': [], 'messages': []}
    
    all_nodes = {**graph.get('nodes', {}), **graph.get('extended_nodes', {})}
    
    # Build a map of all existing connections for quick lookup
    existing_conns = set()
    for node_id, node in all_nodes.items():
        for conn in node.get('connections', []):
            target = conn.get('target')
            ctype = conn.get('type')
            if target and ctype:
                existing_conns.add((node_id, target, ctype))
    
    # Find missing inverses
    inverses_to_add = []
    for node_id, node in all_nodes.items():
        for conn in node.get('connections', []):
            target = conn.get('target')
            ctype = conn.get('type')
            if not target or not ctype:
                continue
            
            inverse_type = CONNECTION_INVERSES.get(ctype)
            if not inverse_type:
                continue
            
            # Check if inverse exists
            if (target, node_id, inverse_type) not in existing_conns:
                # Check if target exists
                if target not in all_nodes:
                    result['skipped'].append(f"{target} --{inverse_type}--> {node_id} (target not found)")
                    continue
                
                inverses_to_add.append({
                    'source': target,
                    'target': node_id,
                    'type': inverse_type,
                    'original': f"{node_id} --{ctype}--> {target}"
                })
    
    if dry_run:
        result['messages'].append(f"DRY RUN: Would add {len(inverses_to_add)} inverse connections")
        for inv in inverses_to_add:
            result['fixed'].append(f"WOULD ADD: {inv['source']} --{inv['type']}--> {inv['target']} (inverse of {inv['original']})")
        return result
    
    # Apply the fixes
    for inv in inverses_to_add:
        source_id = inv['source']
        # Find the section and add
        for section_name in ['nodes', 'extended_nodes']:
            section = graph.get(section_name, {})
            if source_id in section:
                if 'connections' not in section[source_id]:
                    section[source_id]['connections'] = []
                section[source_id]['connections'].append({
                    'target': inv['target'],
                    'type': inv['type']
                })
                result['fixed'].append(f"ADDED: {source_id} --{inv['type']}--> {inv['target']} (inverse of {inv['original']})")
                break
    
    result['messages'].append(f"Added {len(result['fixed'])} inverse connections")
    return result


# =============================================================================
# NODE CRUD HELPERS
# =============================================================================

def generate_node_id(domain: str, graph: dict) -> str:
    """Generate the next node ID for a domain using 3-digit zero padding."""
    nodes = get_all_nodes(graph)
    prefix = f"{domain}-"
    max_num = 0
    for node_id in nodes.keys():
        if node_id.startswith(prefix):
            suffix = node_id[len(prefix):]
            if suffix.isdigit():
                max_num = max(max_num, int(suffix))
    return f"{prefix}{max_num + 1:03d}"


def load_payload_source(inline: str = None, path: str = None) -> dict:
    """Load a YAML/JSON payload from inline text, stdin (@-), or file."""
    if inline:
        if inline.strip() == '@-':
            data = yaml.safe_load(sys.stdin.read())
        else:
            data = yaml.safe_load(inline)
    elif path:
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    else:
        raise ValueError("No payload provided; use --inline or --input")

    if not isinstance(data, dict):
        raise ValueError("Input payload must be a mapping")
    return data


def apply_graph_update(new_graph: dict, focus_nodes: list | None = None) -> dict:
    """Validate and save the graph; optionally focus warnings on specific nodes."""
    validation = validate_graph(new_graph, verbose=False)

    # When focus_nodes is provided (e.g., add-node/update-node), only surface warnings
    # that mention the affected node(s) plus a summary of suppressed items.
    warnings = validation['warnings']
    if focus_nodes:
        focus_set = set(focus_nodes)
        filtered = [w for w in warnings if any(fn in w for fn in focus_set)]
        suppressed = len(warnings) - len(filtered)
        warnings = filtered
        if suppressed:
            warnings.append(
                f"[INFO] {suppressed} warnings for other nodes suppressed; run 'python scripts/graph_utils.py validate' for full report."
            )

    if not validation['passed']:
        return {
            'success': False,
            'errors': validation['issues'],
            'warnings': warnings,
        }
    save_graph(new_graph)
    return {
        'success': True,
        'warnings': warnings,
        'summary': validation['summary'],
    }


def add_node(graph: dict, payload: dict, section: str = 'nodes', node_id: str = None) -> dict:
    """Add a node with automatic ID generation and validation."""
    metadata = graph.get('metadata', {})
    valid_domains = {d['id'] for d in metadata.get('domains', [])}
    valid_statuses = set(metadata.get('statuses', {}).keys())
    valid_node_types = set(metadata.get('node_types', {}).keys())

    domain = payload.get('domain')
    node_type = payload.get('node_type')
    status = payload.get('status')

    if not domain or domain not in valid_domains:
        return {'success': False, 'errors': [f"Invalid or missing domain: {domain}"]}
    if not node_type or node_type not in valid_node_types:
        return {'success': False, 'errors': [f"Invalid or missing node_type: {node_type}"]}
    if not status or status not in valid_statuses:
        return {'success': False, 'errors': [f"Invalid or missing status: {status}"]}
    if not payload.get('title') or not payload.get('definition'):
        return {'success': False, 'errors': ["Missing required fields: title/definition"]}

    target_section = graph.setdefault(section, {})
    assigned_id = node_id or payload.get('id') or generate_node_id(domain, graph)
    if assigned_id in target_section:
        return {'success': False, 'errors': [f"Node ID already exists in {section}: {assigned_id}"]}

    new_node = deepcopy(payload)
    new_node['id'] = assigned_id
    new_node.setdefault('source_chain', [])
    new_node.setdefault('connections', [])
    new_node.setdefault('created', datetime.now().strftime('%Y-%m-%d'))
    new_node['updated'] = datetime.now().strftime('%Y-%m-%d')
    new_node.setdefault('trace_status', 'untraced' if node_type == 'evidence' else 'complete')

    new_graph = deepcopy(graph)
    new_graph.setdefault(section, {})[assigned_id] = new_node

    return apply_graph_update(new_graph, focus_nodes=[assigned_id]) | {'node_id': assigned_id}


def update_node(graph: dict, node_id: str, payload: dict) -> dict:
    """Update an existing node with partial payload and revalidate."""
    for section_name in ['nodes', 'extended_nodes']:
        if node_id in graph.get(section_name, {}):
            new_graph = deepcopy(graph)
            node_ref = new_graph[section_name][node_id]
            merged = deepcopy(node_ref)
            merged.update(payload)

            # Prevent domain/node_type drift without explicit consistency
            if payload.get('domain') and payload.get('domain') != node_ref.get('domain'):
                return {'success': False, 'errors': ["Domain change not allowed via update-node (create a new node instead)"]}
            merged['updated'] = datetime.now().strftime('%Y-%m-%d')
            new_graph[section_name][node_id] = merged
            result = apply_graph_update(new_graph, focus_nodes=[node_id])
            result['node_id'] = node_id
            return result
    return {'success': False, 'errors': [f"Node not found: {node_id}"]}


def delete_node(graph: dict, node_id: str, prune: bool = True) -> dict:
    """Delete a node and optionally prune all references."""
    found_section = None
    for section_name in ['nodes', 'extended_nodes']:
        if node_id in graph.get(section_name, {}):
            found_section = section_name
            break
    if not found_section:
        return {'success': False, 'errors': [f"Node not found: {node_id}"]}

    new_graph = deepcopy(graph)
    del new_graph[found_section][node_id]

    if prune:
        for section in ['nodes', 'extended_nodes']:
            for _, node in new_graph.get(section, {}).items():
                conns = node.get('connections', []) or []
                node['connections'] = [c for c in conns if c.get('target') != node_id]

    return apply_graph_update(new_graph, focus_nodes=[node_id]) | {'node_id': node_id}


def get_node(graph: dict, node_id: str) -> dict:
    """Fetch a node from nodes/extended_nodes."""
    for section_name in ['nodes', 'extended_nodes']:
        section = graph.get(section_name, {})
        if node_id in section:
            return {'success': True, 'node': section[node_id], 'section': section_name}
    return {'success': False, 'errors': [f"Node not found: {node_id}"]}


def main():
    parser = argparse.ArgumentParser(description="Knowledge Graph Utilities")
    parser.add_argument('command', choices=[
        'stats', 'validate', 'audit', 'list', 'connections', 'untraced', 'export-md',
        'confidence', 'score', 'low-confidence', 'needs-extraction', 'persist-scores',
        'chain-check', 'warnings', 'add-connection', 'fix-inverses',
        'add-node', 'update-node', 'delete-node', 'get-node'
    ])
    parser.add_argument('--domain', '-d', help="Filter by domain ID")
    parser.add_argument('--json', '-j', action='store_true', help="Output as JSON")
    parser.add_argument('--threshold', '-t', type=float, default=0.50, 
                        help="Confidence threshold for low-confidence command")
    parser.add_argument('--verbose', '-v', action='store_true', help="Include informational messages")
    parser.add_argument('--output', '-o', help="Write output to file instead of console")
    parser.add_argument('--type', help="Warning type filter for warnings command (epistemic_spread, insufficient_evidence, insufficient_integration, invalid_connection, missing_inverse, chain_incomplete)")
    parser.add_argument('--limit', '-n', type=int, default=50, help="Max warnings to show (default: 50)")
    parser.add_argument('--dry-run', action='store_true', help="Preview changes without applying (for add-connection, fix-inverses)")
    parser.add_argument('--source', '-s', help="Source node ID (for add-connection)")
    parser.add_argument('--target', '-T', help="Target node ID (for add-connection)")
    parser.add_argument('--conn-type', '-c', help="Connection type (for add-connection)")
    parser.add_argument('--note', help="Optional note for connection (for add-connection)")
    parser.add_argument('--input', help="Path to YAML/JSON payload (for add-node, update-node)")
    parser.add_argument('--inline', help="Inline YAML/JSON payload for add-node/update-node. Use --inline @- to read from stdin.")
    parser.add_argument('--section', default='nodes', choices=['nodes', 'extended_nodes'], help="Graph section to target for add-node")
    parser.add_argument('--prune', action='store_true', help="Prune connections that reference a deleted node (delete-node)")
    parser.add_argument('--id', help="Optional node ID override when creating a node")
    parser.add_argument('node_id', nargs='?', help="Node ID for score command")
    
    args = parser.parse_args()
    
    graph = load_graph()
    
    # Helper for output (handles unicode on Windows)
    def output(text):
        if args.output:
            with open(args.output, 'a', encoding='utf-8') as f:
                f.write(text + '\n')
        else:
            # Handle unicode characters that Windows console can't display
            try:
                print(text)
            except UnicodeEncodeError:
                print(text.encode('ascii', 'replace').decode('ascii'))
    
    if args.output:
        # Clear output file
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"# Graph Utils Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
    
    if args.command == 'stats':
        stats = get_stats(graph)
        if args.json:
            output(json.dumps(stats, indent=2, cls=DateEncoder))
        else:
            output("\n=== Knowledge Graph Statistics ===\n")
            output(f"Total Nodes:       {stats['total_nodes']}")
            output(f"Total Connections: {stats['total_connections']}")
            output(f"Untraced Claims:   {stats['untraced_claims']}")
            output("\nBy Status:")
            for status, count in stats['by_status'].items():
                output(f"  {status}: {count}")
            output("\nBy Domain:")
            for domain, count in stats['by_domain'].items():
                output(f"  {domain}: {count}")
    
    elif args.command == 'validate':
        result = validate_graph(graph, verbose=args.verbose)
        if args.json:
            output(json.dumps(result, indent=2, cls=DateEncoder))
        else:
            if result['passed']:
                output("\n[PASS] Graph validation passed - no critical issues\n")
            else:
                output(f"\n[FAIL] Found {len(result['issues'])} critical issues\n")
            
            if result['issues']:
                output("=== ERRORS (must fix) ===\n")
                for issue in result['issues']:
                    output(f"  [!] {issue}")
            
            if result['warnings']:
                output(f"\n=== WARNINGS ({len(result['warnings'])}) ===\n")
                # Group warnings by type for cleaner output
                chain_warnings = [w for w in result['warnings'] if 'CHAIN INCOMPLETE' in w]
                inverse_warnings = [w for w in result['warnings'] if 'INCOMPLETE CHAIN:' in w and 'CHAIN INCOMPLETE' not in w]
                cardinality_warns = [w for w in result['warnings'] if 'CARDINALITY' in w]
                other_warnings = [w for w in result['warnings'] if w not in chain_warnings and w not in inverse_warnings and w not in cardinality_warns]
                
                if chain_warnings:
                    output(f"  --- Chain Completeness ({len(chain_warnings)}) ---")
                    for warning in chain_warnings[:5]:  # Show first 5
                        output(f"  [?] {warning}")
                    if len(chain_warnings) > 5:
                        output(f"  ... and {len(chain_warnings) - 5} more chain warnings")
                    output("")
                
                if inverse_warnings:
                    output(f"  --- Missing Inverse Connections ({len(inverse_warnings)}) ---")
                    for warning in inverse_warnings[:5]:  # Show first 5
                        output(f"  [?] {warning}")
                    if len(inverse_warnings) > 5:
                        output(f"  ... and {len(inverse_warnings) - 5} more inverse warnings")
                    output("")
                
                if cardinality_warns:
                    output(f"  --- Cardinality Warnings ({len(cardinality_warns)}) ---")
                    for warning in cardinality_warns[:10]:  # Show first 10
                        output(f"  [?] {warning}")
                    if len(cardinality_warns) > 10:
                        output(f"  ... and {len(cardinality_warns) - 10} more cardinality warnings")
                    output("")
                
                if other_warnings:
                    output(f"  --- Other Warnings ({len(other_warnings)}) ---")
                    for warning in other_warnings[:10]:  # Show first 10
                        output(f"  [?] {warning}")
                    if len(other_warnings) > 10:
                        output(f"  ... and {len(other_warnings) - 10} more warnings")
            
            # Print summary
            s = result['summary']
            output("\n=== Summary ===")
            output(f"  Total nodes:                {s['total_nodes']}")
            output(f"  Evidence nodes:             {s['evidence_nodes']}")
            output(f"    - With factors:           {s['evidence_with_factors']}")
            output(f"    - Missing factors:        {s['evidence_missing_factors']}")
            output(f"  Nodes with critiques:       {s['nodes_with_critiques']}")
            output(f"  Nodes never reviewed:       {s['nodes_never_reviewed']}")
            output(f"  Open proof-breaking:        {s['proof_breaking_open']}")
            output(f"  Orphan nodes:               {s['orphan_nodes']}")
            output("")
            output("  === Connection Validation ===")
            output(f"  Invalid connection types:   {s.get('invalid_connection_types', 0)}")
            output(f"  Missing inverse conns:      {s.get('missing_inverse_connections', 0)}")
            output(f"    - Critical (no reverse):  {s.get('critical_missing_inverses', 0)}")
            output(f"  Chain completeness warns:   {s.get('chain_completeness_warnings', 0)}")
            output("")
            output("  === Cardinality Warnings ===")
            output(f"  Total cardinality warns:    {s.get('cardinality_warnings', 0)}")
            output(f"    - Epistemic spread:       {s.get('epistemic_spread_warnings', 0)}")
            output(f"    - Insufficient evidence:  {s.get('insufficient_evidence_warnings', 0)}")
            output(f"    - Insufficient integ:     {s.get('insufficient_integration_warnings', 0)}")
    
    elif args.command == 'audit':
        # Full audit report - comprehensive analysis
        result = validate_graph(graph, verbose=True)
        nodes = get_all_nodes(graph)
        
        output("\n" + "=" * 60)
        output("  KNOWLEDGE GRAPH AUDIT REPORT")
        output(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        output("=" * 60)
        
        # Overall status
        s = result['summary']
        output(f"\n{'[PASS]' if result['passed'] else '[FAIL]'} Overall Status\n")
        
        # Statistics section
        output("=" * 40)
        output("  1. STATISTICS")
        output("=" * 40)
        output(f"  Total Nodes:              {s['total_nodes']}")
        output(f"  Evidence Nodes:           {s['evidence_nodes']}")
        output(f"  Orphan Nodes:             {s['orphan_nodes']}")
        
        # Evidence node status
        output("\n--- Evidence Node Status ---")
        output(f"  With confidence_factors:  {s['evidence_with_factors']}")
        output(f"  Missing factors:          {s['evidence_missing_factors']}")
        if s['evidence_nodes'] > 0:
            pct = (s['evidence_with_factors'] / s['evidence_nodes']) * 100
            output(f"  Completion:               {pct:.1f}%")
        
        # Critic status
        output("\n--- Critic Review Status ---")
        output(f"  Nodes with critiques:     {s['nodes_with_critiques']}")
        output(f"  Nodes never reviewed:     {s['nodes_never_reviewed']}")
        output(f"  Open proof-breaking:      {s['proof_breaking_open']}")
        if s['total_nodes'] > 0:
            pct = (s['nodes_with_critiques'] / s['total_nodes']) * 100
            output(f"  Review coverage:          {pct:.1f}%")
        
        # Circular proof chains (critical integrity issue)
        if s.get('circular_proof_chains', 0) > 0:
            output("\n--- CIRCULAR PROOF CHAINS ---")
            output(f"  [CRITICAL] {s['circular_proof_chains']} circular proof chains detected!")
            output("  Circular proofs are epistemologically invalid - must be resolved.")
        
        # Critical errors
        if result['issues']:
            output("\n" + "=" * 40)
            output("  2. CRITICAL ERRORS")
            output("=" * 40)
            for issue in result['issues']:
                output(f"  [!] {issue}")
        
        # Warnings by category
        if result['warnings']:
            output("\n" + "=" * 40)
            output("  3. WARNINGS BY CATEGORY")
            output("=" * 40)
            
            # Categorize warnings
            missing_factors = []
            missing_critiques = []
            connection_issues = []
            source_issues = []
            other = []
            
            for w in result['warnings']:
                if 'confidence_factors' in w:
                    missing_factors.append(w)
                elif 'critic' in w.lower() or 'critique' in w.lower() or 'proof_breaking' in w or 'detail_issues' in w:
                    missing_critiques.append(w)
                elif 'Connection' in w or 'connection' in w:
                    connection_issues.append(w)
                elif 'source' in w.lower() or 'trace' in w.lower():
                    source_issues.append(w)
                else:
                    other.append(w)
            
            if missing_factors:
                output(f"\n--- Missing Confidence Factors ({len(missing_factors)}) ---")
                for w in missing_factors[:10]:  # Show first 10
                    output(f"  {w}")
                if len(missing_factors) > 10:
                    output(f"  ... and {len(missing_factors) - 10} more")
            
            if missing_critiques:
                output(f"\n--- Critic Issues ({len(missing_critiques)}) ---")
                for w in missing_critiques[:10]:
                    output(f"  {w}")
                if len(missing_critiques) > 10:
                    output(f"  ... and {len(missing_critiques) - 10} more")
            
            if connection_issues:
                output(f"\n--- Connection Issues ({len(connection_issues)}) ---")
                for w in connection_issues[:10]:
                    output(f"  {w}")
                if len(connection_issues) > 10:
                    output(f"  ... and {len(connection_issues) - 10} more")
            
            if source_issues:
                output(f"\n--- Source Chain Issues ({len(source_issues)}) ---")
                for w in source_issues[:10]:
                    output(f"  {w}")
                if len(source_issues) > 10:
                    output(f"  ... and {len(source_issues) - 10} more")
            
            if other:
                output(f"\n--- Other Issues ({len(other)}) ---")
                for w in other[:10]:
                    output(f"  {w}")
                if len(other) > 10:
                    output(f"  ... and {len(other) - 10} more")
        
        # Action items
        output("\n" + "=" * 40)
        output("  4. RECOMMENDED ACTIONS")
        output("=" * 40)
        
        actions = []
        if s.get('circular_proof_chains', 0) > 0:
            actions.append(f"[CRITICAL] Break {s['circular_proof_chains']} circular proof chains (see errors above)")
        if s['evidence_missing_factors'] > 0:
            actions.append(f"Run @confidence-extractor on {s['evidence_missing_factors']} evidence nodes")
        if s['nodes_never_reviewed'] > 0:
            actions.append(f"Run @critic on {s['nodes_never_reviewed']} unreviewed nodes")
        if s['proof_breaking_open'] > 0:
            actions.append(f"Address {s['proof_breaking_open']} open proof-breaking critiques")
        if s['orphan_nodes'] > 0:
            actions.append(f"Connect {s['orphan_nodes']} orphan nodes to the graph")
        if s['missing_source_chain'] > 0:
            actions.append(f"Add source chains to {s['missing_source_chain']} nodes")
        
        if actions:
            for i, action in enumerate(actions, 1):
                output(f"  {i}. {action}")
        else:
            output("  No critical actions needed.")
        
        output("\n" + "=" * 60)
        output("  END OF AUDIT REPORT")
        output("=" * 60 + "\n")
    
    elif args.command == 'list':
        nodes_list = list_nodes(graph, args.domain)
        if args.json:
            output(json.dumps(nodes_list, indent=2, cls=DateEncoder))
        else:
            output(f"\n=== Nodes ({len(nodes_list)}) ===\n")
            for node in nodes_list:
                output(f"  [{node['id']}] {node['title']} ({node['status']}, {node['connections']} connections)")
    
    elif args.command == 'untraced':
        untraced = graph.get('untraced', []) or []
        if args.json:
            output(json.dumps(untraced, indent=2, cls=DateEncoder))
        else:
            output(f"\n=== Untraced Claims ({len(untraced)}) ===\n")
            for claim in untraced:
                output(f"  * {claim.get('claim', 'Unknown')}")
                output(f"    Found in: {claim.get('found_in', 'Unknown')}")
                output(f"    Needed: {claim.get('needed', 'Original source')}")
                output("")
    
    elif args.command == 'export-md':
        markdown = export_to_markdown(graph)
        with open(MARKDOWN_PATH, 'w', encoding='utf-8') as f:
            f.write(markdown)
        output(f"Exported to {MARKDOWN_PATH}")
    
    elif args.command == 'connections':
        nodes = get_all_nodes(graph)
        output("\n=== Connection Network ===\n")
        for node_id, node in nodes.items():
            conns = node.get('connections', [])
            if conns:
                output(f"[{node_id}] {node.get('title', 'Untitled')}")
                for conn in conns:
                    output(f"  -> {conn.get('type')} -> [{conn.get('target')}]")
                output("")
    
    elif args.command == 'confidence':
        scores = get_all_confidence_scores(graph)
        if args.json:
            output(json.dumps(scores, indent=2, cls=DateEncoder))
        else:
            output("\n=== Confidence Scores (highest first) ===\n")
            circular_count = sum(1 for s in scores if s['label'] == 'circular')
            if circular_count > 0:
                output(f"  [!] {circular_count} nodes blocked due to circular proof chains\n")
            for s in scores:
                icon = {"high": "[H]", "medium": "[M]", "low": "[L]", "preliminary": "[P]", "contested": "[!]", "circular": "[X]"}.get(s['label'], "[?]")
                title = s['title'][:50] if s['title'] else 'Untitled'
                output(f"  {icon} [{s['node_id']}] {s['final_score']:.2f} ({s['label']}) - {title}")
    
    elif args.command == 'score':
        if not args.node_id:
            output("Error: node_id required for score command")
            return
        nodes = get_all_nodes(graph)
        flat_connections = graph.get('connections', []) or []
        if args.node_id not in nodes:
            output(f"Error: Node '{args.node_id}' not found")
            return
        result = calculate_node_confidence(args.node_id, nodes, flat_connections)
        result['title'] = nodes[args.node_id].get('title', 'Untitled')
        if args.json:
            output(json.dumps(result, indent=2, cls=DateEncoder))
        else:
            output(f"\n=== Confidence Score: {args.node_id} ===\n")
            output(f"  Title:         {result['title']}")
            output(f"  Node Type:     {result['node_type']}")
            output(f"  Score Source:  {result['score_source']}")
            
            # Handle circular proof chain error
            if result['label'] == 'circular':
                output(f"\n  [!] BLOCKED: Node is part of circular proof chain")
                output(f"  Error:         {result.get('error', 'Circular dependency')}")
                if result.get('circular_chains'):
                    output(f"  Cycles:")
                    for chain in result['circular_chains']:
                        output(f"                 {chain}")
                output(f"\n  Confidence cannot be calculated until cycle is broken.")
            else:
                output(f"  Base Score:    {result['base_score']:.3f}")
                if result['cap_applied']:
                    output(f"  Cap Applied:   {result['cap_applied']:.2f} (due to node_type)")
                if result['proof_breaking_penalty']:
                    output(f"  Penalty:       -{result['proof_breaking_penalty']:.3f} (proof-breaking critiques)")
                output(f"  Final Score:   {result['final_score']:.3f}")
                output(f"  Label:         {result['label']}")
    
    elif args.command == 'low-confidence':
        low = get_low_confidence_nodes(graph, args.threshold)
        if args.json:
            output(json.dumps(low, indent=2, cls=DateEncoder))
        else:
            output(f"\n=== Low Confidence Nodes (below {args.threshold}) ===\n")
            if not low:
                output("  No nodes below threshold.")
            for s in low:
                icon = {"high": "[H]", "medium": "[M]", "low": "[L]", "preliminary": "[P]", "contested": "[!]"}.get(s['label'], "[?]")
                title = s['title'][:50] if s['title'] else 'Untitled'
                output(f"  {icon} [{s['node_id']}] {s['final_score']:.2f} ({s['label']}) - {title}")
    
    elif args.command == 'needs-extraction':
        needs = get_needs_extraction(graph)
        if args.json:
            output(json.dumps(needs, indent=2, cls=DateEncoder))
        else:
            output(f"\n=== Evidence Nodes Needing Confidence Extraction ({len(needs)}) ===\n")
            if not needs:
                output("  All evidence nodes have confidence_factors.")
            for n in needs:
                output(f"  [{n['id']}] {n['title']} ({n['domain']})")
    
    elif args.command == 'persist-scores':
        output("\n=== Persisting Confidence Scores ===\n")
        changes = persist_confidence_scores(graph)
        
        if args.json:
            output(json.dumps(changes, indent=2, cls=DateEncoder))
        else:
            output(f"Updated: {len(changes['updated'])} nodes")
            output(f"Errors:  {len(changes['errors'])} nodes")
            
            if changes['errors']:
                output("\nErrors:")
                for err in changes['errors']:
                    output(f"  [{err['node_id']}] {err['error']}")
            
            if args.verbose and changes['updated']:
                output("\nUpdated nodes:")
                for u in changes['updated']:
                    old_val = u['old']
                    if old_val is None:
                        old_str = "None"
                    elif isinstance(old_val, (int, float)):
                        old_str = f"{old_val:.2f}"
                    else:
                        old_str = str(old_val)  # Handle string confidence labels like "high"
                    output(f"  [{u['node_id']}] {old_str} -> {u['new']:.2f} ({u['label']})")
        
        # Save the graph
        save_graph(graph)
        output(f"\nSaved to {GRAPH_PATH}")
    
    elif args.command == 'chain-check':
        if not args.node_id:
            output("Error: node_id required for chain-check command")
            output("Usage: python graph_utils.py chain-check NODE_ID")
            return
        nodes = get_all_nodes(graph)
        if args.node_id not in nodes:
            output(f"Error: Node '{args.node_id}' not found")
            return
        
        analysis = get_node_chain_analysis(args.node_id, nodes)
        node = nodes[args.node_id]
        
        if args.json:
            output(json.dumps(analysis, indent=2, cls=DateEncoder))
        else:
            output(f"\n=== Chain Analysis: {args.node_id} ===\n")
            output(f"  Title:      {node.get('title', 'Untitled')}")
            output(f"  Node Type:  {analysis['node_type']}")
            output(f"  Completeness: {analysis['chain_completeness']*100:.0f}%")
            
            if analysis['is_isolated']:
                output("\n  [!] WARNING: Node is ISOLATED (no chain connections)")
            
            output("\n  --- Upward Chain (toward foundational) ---")
            if analysis['upward_chain']:
                for item in analysis['upward_chain']:
                    indent = "    " * item['depth']
                    output(f"  {indent}--{item['via']}--> [{item['node']}] ({item['type']})")
                if analysis['has_foundational_path']:
                    output("  [OK] Reaches foundational level")
                else:
                    output("  [?] Does not reach foundational level")
            else:
                output("  (no upward connections)")
            
            output("\n  --- Downward Chain (toward evidence) ---")
            if analysis['downward_chain']:
                for item in analysis['downward_chain']:
                    indent = "    " * item['depth']
                    output(f"  {indent}--{item['via']}--> [{item['node']}] ({item['type']})")
                if analysis['has_evidence_path']:
                    output("  [OK] Reaches evidence level")
                else:
                    output("  [?] Does not reach evidence level")
            else:
                output("  (no downward connections)")
            
            # Recommendations
            output("\n  --- Recommendations ---")
            if analysis['chain_completeness'] == 1.0:
                output("  [OK] Chain is complete")
            else:
                if analysis['node_type'] in ['concept', 'hypothesis'] and not analysis['has_evidence_path']:
                    output("  [!] Add evidence supports the hypothesis, and hypotheses must develop from the concept")
                if analysis['node_type'] in ['concept', 'hypothesis'] and not analysis['has_foundational_path']:
                    output("  [!] Link concept to foundational via develops/developed_by")
                if analysis['node_type'] == 'evidence' and not analysis['upward_chain']:
                    output("  [!] Add supports/contradicts from evidence to a hypothesis")
                if analysis['node_type'] == 'foundational' and not analysis['downward_chain']:
                    output("  [!] Add develops from foundational to concept")

    elif args.command == 'warnings':
        # Show specific warning types from validation
        nodes = get_all_nodes(graph)
        result = validate_graph(graph, verbose=True)
        
        # Categorize all warnings
        all_warnings = []
        for w in result['warnings']:
            if 'CARDINALITY' in w:
                if 'epistemic_spread' in w:
                    all_warnings.append({'type': 'epistemic_spread', 'msg': w})
                elif 'insufficient_evidence' in w:
                    all_warnings.append({'type': 'insufficient_evidence', 'msg': w})
                elif 'insufficient_integration' in w:
                    all_warnings.append({'type': 'insufficient_integration', 'msg': w})
            elif 'CHAIN INCOMPLETE' in w:
                all_warnings.append({'type': 'chain_incomplete', 'msg': w})
            elif 'MISSING REVERSE' in w or 'INCOMPLETE CHAIN:' in w:
                all_warnings.append({'type': 'missing_inverse', 'msg': w})
        
        # Add errors as warnings for unified view
        for i in result['issues']:
            if 'INVALID CONNECTION TYPE' in i:
                all_warnings.append({'type': 'invalid_connection', 'msg': i})
        
        # Filter by type if specified
        if args.type:
            filtered = [w for w in all_warnings if w['type'] == args.type]
        else:
            filtered = all_warnings
        
        # Count by type
        type_counts = {}
        for w in all_warnings:
            type_counts[w['type']] = type_counts.get(w['type'], 0) + 1
        
        output("\n=== Warning Types ===")
        for wtype, count in sorted(type_counts.items()):
            marker = " <--" if args.type == wtype else ""
            output(f"  {wtype}: {count}{marker}")
        output(f"\n  Total: {len(all_warnings)}")
        
        if args.type:
            output(f"\n=== {args.type} ({len(filtered)}) ===\n")
        else:
            output(f"\n=== All Warnings (showing {min(len(filtered), args.limit)} of {len(filtered)}) ===\n")
        
        for w in filtered[:args.limit]:
            output(f"  {w['msg']}")
        
        if len(filtered) > args.limit:
            output(f"\n  ... {len(filtered) - args.limit} more (use --limit/-n to show more)")

    elif args.command == 'add-connection':
        # Add a new connection with validation and auto-inverse
        if not args.source or not args.target or not args.conn_type:
            output("ERROR: add-connection requires --source, --target, and --conn-type")
            output("\nUsage: python graph_utils.py add-connection --source NODE_ID --target NODE_ID --conn-type TYPE [--note \"note\"] [--dry-run]")
            output("\nExample: python graph_utils.py add-connection -s SWED-001 -T CONSC-001 -c supports --dry-run")
            sys.exit(1)
        
        result = add_connection(graph, args.source, args.target, args.conn_type, 
                               note=args.note, dry_run=args.dry_run)
        
        if result['changes']:
            output("\n=== Changes ===")
            for change in result['changes']:
                output(f"  {change}")
        
        if result['messages']:
            output("\n=== Messages ===")
            for msg in result['messages']:
                output(f"  {msg}")
        
        if result['success'] and not args.dry_run:
            # Save the graph
            save_graph(graph)
            output(f"\nSaved to {GRAPH_PATH}")

    elif args.command == 'fix-inverses':
        # Fix all missing inverse connections
        result = fix_missing_inverses(graph, dry_run=args.dry_run)
        
        if result['fixed']:
            output(f"\n=== {'Would Fix' if args.dry_run else 'Fixed'} ({len(result['fixed'])}) ===")
            for fix in result['fixed'][:20]:
                output(f"  {fix}")
            if len(result['fixed']) > 20:
                output(f"  ... and {len(result['fixed']) - 20} more")
        
        if result['skipped']:
            output(f"\n=== Skipped ({len(result['skipped'])}) ===")
            for skip in result['skipped'][:10]:
                output(f"  {skip}")
            if len(result['skipped']) > 10:
                output(f"  ... and {len(result['skipped']) - 10} more")
        
        for msg in result['messages']:
            output(f"\n{msg}")

    elif args.command == 'add-node':
        if not args.inline and not args.input:
            output("ERROR: add-node requires --inline YAML or --input PATH")
            sys.exit(1)
        try:
            payload = load_payload_source(inline=args.inline, path=args.input)
        except Exception as e:
            output(f"ERROR: Failed to load payload: {e}")
            sys.exit(1)

        result = add_node(graph, payload, section=args.section, node_id=args.id)
        if not result.get('success'):
            for err in result.get('errors', []):
                output(f"[ERROR] {err}")
            for warn in result.get('warnings', []):
                output(f"[WARN] {warn}")
            sys.exit(1)

        output(f"Added node: {result.get('node_id')} (section: {args.section})")
        for warn in result.get('warnings', []):
            output(f"[WARN] {warn}")
        output("Validation: PASS")

    elif args.command == 'update-node':
        if not args.node_id or (not args.inline and not args.input):
            output("ERROR: update-node requires NODE_ID and --inline YAML or --input PATH")
            sys.exit(1)
        try:
            payload = load_payload_source(inline=args.inline, path=args.input)
        except Exception as e:
            output(f"ERROR: Failed to load payload: {e}")
            sys.exit(1)

        result = update_node(graph, args.node_id, payload)
        if not result.get('success'):
            for err in result.get('errors', []):
                output(f"[ERROR] {err}")
            for warn in result.get('warnings', []):
                output(f"[WARN] {warn}")
            sys.exit(1)

        output(f"Updated node: {result.get('node_id')}")
        for warn in result.get('warnings', []):
            output(f"[WARN] {warn}")
        output("Validation: PASS")

    elif args.command == 'delete-node':
        if not args.node_id:
            output("ERROR: delete-node requires NODE_ID")
            sys.exit(1)
        result = delete_node(graph, args.node_id, prune=args.prune)
        if not result.get('success'):
            for err in result.get('errors', []):
                output(f"[ERROR] {err}")
            sys.exit(1)
        output(f"Deleted node: {result.get('node_id')} (prune connections: {args.prune})")
        for warn in result.get('warnings', []):
            output(f"[WARN] {warn}")
        output("Validation: PASS")

    elif args.command == 'get-node':
        if not args.node_id:
            output("ERROR: get-node requires NODE_ID")
            sys.exit(1)
        result = get_node(graph, args.node_id)
        if not result.get('success'):
            for err in result.get('errors', []):
                output(f"[ERROR] {err}")
            sys.exit(1)
        node_data = result.get('node', {})
        if args.json:
            output(json.dumps({'node_id': args.node_id, 'section': result.get('section'), 'node': node_data}, indent=2, cls=DateEncoder))
        else:
            output(f"Node: {args.node_id} (section: {result.get('section')})")
            output(yaml.dump(node_data, sort_keys=False, allow_unicode=True))


if __name__ == '__main__':
    main()
