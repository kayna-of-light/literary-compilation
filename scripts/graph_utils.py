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

Options:
    -j, --json       Output as JSON
    -v, --verbose    Include informational messages
    -o, --output     Write output to file
    -d, --domain     Filter by domain ID
    -t, --threshold  Confidence threshold (default: 0.50)
"""

import yaml
import json
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime

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
    Calculate derived confidence from evidence base.
    Used for non-evidence nodes.
    
    NON-RECURSIVE approach: Only looks at direct connections to evidence nodes
    or uses persisted confidence of connected non-evidence nodes.
    
    Args:
        node_id: The node to calculate confidence for
        nodes: Dictionary of all nodes
        flat_connections: Optional flat list of [source, type, target] connections
        visited: For cycle prevention (not used in non-recursive approach)
    """
    if visited is None:
        visited = set()
    
    if node_id in visited:
        return 0.0  # Prevent cycles
    visited.add(node_id)
    
    node = nodes.get(node_id, {})
    node_type = node.get('node_type', 'concept')
    
    # Evidence nodes use intrinsic confidence
    if node_type == 'evidence':
        factors = node.get('confidence_factors', {})
        return calculate_intrinsic_confidence(factors)
    
    # Non-evidence nodes derive from connections
    embedded_connections = node.get('connections', [])
    evidence_scores = []
    
    # === FORWARD: connections FROM this node TO others (embedded only) ===
    # Connection types where the TARGET provides epistemic support to SOURCE
    forward_support = ['supported_by', 'validated_by', 'developed_from', 'revealed_by', 'produced_by']
    forward_weaker = ['instantiated_by']
    
    for conn in embedded_connections:
        target_id = conn.get('target')
        conn_type = conn.get('type')
        
        if not target_id or target_id not in nodes:
            continue
            
        target_node = nodes[target_id]
        target_type = target_node.get('node_type', 'concept')
        
        # Get target score - evidence uses intrinsic, others use persisted
        if target_type == 'evidence':
            factors = target_node.get('confidence_factors', {})
            target_score = calculate_intrinsic_confidence(factors)
        else:
            target_score = target_node.get('confidence', 0.30)
        
        if target_score > 0.30:
            if conn_type in forward_support:
                if target_type == 'evidence':
                    evidence_scores.append(target_score)
                else:
                    evidence_scores.append(target_score * 0.85)
            elif conn_type in forward_weaker:
                evidence_scores.append(target_score * 0.7)
    
    # === BACKWARD: connections FROM other nodes TO this node ===
    inverse_support = ['supports', 'validates']
    
    # Check embedded connections in nodes
    for other_id, other_node in nodes.items():
        if other_id == node_id:
            continue
        
        other_type = other_node.get('node_type', 'concept')
        
        for conn in other_node.get('connections', []):
            if conn.get('target') != node_id:
                continue
                
            conn_type = conn.get('type')
            
            if conn_type not in inverse_support:
                continue
            
            # Get other score - evidence uses intrinsic, others use persisted
            if other_type == 'evidence':
                factors = other_node.get('confidence_factors', {})
                other_score = calculate_intrinsic_confidence(factors)
            else:
                other_score = other_node.get('confidence', 0.30)
            
            if other_score > 0.30 and other_score not in evidence_scores:
                if other_type == 'evidence':
                    evidence_scores.append(other_score)
                else:
                    evidence_scores.append(other_score * 0.85)
    
    # ALSO check flat connections list (format: [source, type, target])
    if flat_connections:
        for conn in flat_connections:
            if not isinstance(conn, list) or len(conn) != 3:
                continue
            source_id, conn_type, target_id = conn
            
            # Only supports/validates pointing TO this node
            if target_id != node_id:
                continue
            if conn_type not in inverse_support:
                continue
            if source_id not in nodes:
                continue
            
            source_node = nodes[source_id]
            source_type = source_node.get('node_type', 'concept')
            
            # Get source score
            if source_type == 'evidence':
                factors = source_node.get('confidence_factors', {})
                source_score = calculate_intrinsic_confidence(factors)
            else:
                source_score = source_node.get('confidence', 0.30)
            
            if source_score > 0.30 and source_score not in evidence_scores:
                if source_type == 'evidence':
                    evidence_scores.append(source_score)
                else:
                    evidence_scores.append(source_score * 0.85)
    
    if evidence_scores:
        # PRINCIPLE: Strong evidence establishes the claim
        base_score = max(evidence_scores)
        
        # Stream bonus for multiple strong streams
        strong_streams = [s for s in evidence_scores if s >= 0.60]
        if len(strong_streams) > 1:
            stream_bonus = min(0.1, (len(strong_streams) - 1) * 0.03)
        else:
            stream_bonus = 0.0
        return min(1.0, base_score + stream_bonus)
    
    return 0.30  # No evidence connections


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
    connections = graph.get('connections', []) or []
    untraced = graph.get('untraced', []) or []
    
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
        'total_connections': len(connections),
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
    # These are the connections where confidence flows
    proof_relations = ['supports', 'validates', 'instantiates', 'requires']
    
    # Build directed graph of proof relationships
    graph = {node_id: [] for node_id in nodes}
    
    for node_id, node in nodes.items():
        for conn in node.get('connections', []):
            target = conn.get('target')
            rel_type = conn.get('type', '')
            # These relations mean: this node contributes to target's proof
            if rel_type in proof_relations and target in nodes:
                graph[node_id].append((target, rel_type))
    
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
        List of tuples (source, target, rel_type) where reverse is missing
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
        # Check if there's a connection back from target to source
        target_node = nodes[target]
        reverse_exists = any(
            conn.get('target') == source 
            for conn in target_node.get('connections', [])
        )
        
        if not reverse_exists:
            # Get the relationship type for the forward connection
            source_node = nodes[source]
            rel_type = None
            for conn in source_node.get('connections', []):
                if conn.get('target') == target:
                    rel_type = conn.get('type')
                    break
            
            missing_reverse.append((source, target, rel_type))
    
    return missing_reverse


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
    
    for node_id, node in nodes.items():
        node_issues = []
        node_warnings = []
        
        # === STRUCTURAL VALIDATION ===
        
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
        node_type = node.get('node_type')
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
        for source, target, rel_type in missing_reverse:
            warnings.append(f"MISSING REVERSE: {source} -> {target} ({rel_type}) has no reverse connection")
    
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


def main():
    parser = argparse.ArgumentParser(description="Knowledge Graph Utilities")
    parser.add_argument('command', choices=[
        'stats', 'validate', 'audit', 'list', 'connections', 'untraced', 'export-md',
        'confidence', 'score', 'low-confidence', 'needs-extraction', 'persist-scores'
    ])
    parser.add_argument('--domain', '-d', help="Filter by domain ID")
    parser.add_argument('--json', '-j', action='store_true', help="Output as JSON")
    parser.add_argument('--threshold', '-t', type=float, default=0.50, 
                        help="Confidence threshold for low-confidence command")
    parser.add_argument('--verbose', '-v', action='store_true', help="Include informational messages")
    parser.add_argument('--output', '-o', help="Write output to file instead of console")
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
            output(json.dumps(stats, indent=2))
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
            output(json.dumps(result, indent=2))
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
                for warning in result['warnings']:
                    output(f"  [?] {warning}")
            
            # Print summary
            s = result['summary']
            output("\n=== Summary ===")
            output(f"  Total nodes:              {s['total_nodes']}")
            output(f"  Evidence nodes:           {s['evidence_nodes']}")
            output(f"    - With factors:         {s['evidence_with_factors']}")
            output(f"    - Missing factors:      {s['evidence_missing_factors']}")
            output(f"  Nodes with critiques:     {s['nodes_with_critiques']}")
            output(f"  Nodes never reviewed:     {s['nodes_never_reviewed']}")
            output(f"  Open proof-breaking:      {s['proof_breaking_open']}")
            output(f"  Orphan nodes:             {s['orphan_nodes']}")
    
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
            output(json.dumps(nodes_list, indent=2))
        else:
            output(f"\n=== Nodes ({len(nodes_list)}) ===\n")
            for node in nodes_list:
                output(f"  [{node['id']}] {node['title']} ({node['status']}, {node['connections']} connections)")
    
    elif args.command == 'untraced':
        untraced = graph.get('untraced', []) or []
        if args.json:
            output(json.dumps(untraced, indent=2))
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
            output(json.dumps(scores, indent=2))
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
            output(json.dumps(result, indent=2))
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
            output(json.dumps(low, indent=2))
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
            output(json.dumps(needs, indent=2))
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
            output(json.dumps(changes, indent=2))
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


if __name__ == '__main__':
    main()
