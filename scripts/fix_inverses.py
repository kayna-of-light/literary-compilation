#!/usr/bin/env python3
"""
Script to add missing inverse connections to the knowledge graph.
When A --supports--> B exists, adds B --supported_by--> A if missing.
Only adds inverses that are VALID for the target→source node type pair.
"""

import yaml
import argparse
from pathlib import Path

GRAPH_PATH = Path(__file__).parent.parent / 'graph' / 'knowledge_graph.yaml'

# Map connection types to their inverses
INVERSE_MAP = {
    'supports': 'supported_by',
    'supported_by': 'supports',
    'develops': 'developed_by',
    'developed_by': 'develops',
    'developed_from': 'develops_to',  # Handle existing developed_from
    'develops_to': 'developed_from',
    'validates': 'validated_by',
    'validated_by': 'validates',
    'instantiates': 'instantiated_by',
    'instantiated_by': 'instantiates',
    'integrates_into': 'integrated_from',
    'integrated_from': 'integrates_into',
    'requires': 'required_by',
    'required_by': 'requires',
    'produces': 'produced_by',
    'produced_by': 'produces',
    'explains': 'explained_by',
    'explained_by': 'explains',
    'contains': 'contained_by',
    'contained_by': 'contains',
    'contextualizes': 'contextualized_by',
    'contextualized_by': 'contextualizes',
    'follows': 'precedes',
    'precedes': 'follows',
    'complements': 'complemented_by',
    'complemented_by': 'complements',
    'describes': 'described_by',
    'described_by': 'describes',
    'addresses': 'addressed_by',
    'addressed_by': 'addresses',
    'reverses': 'reversed_by',
    'reversed_by': 'reverses',
    # Symmetric relations (inverse is same)
    'parallels': 'parallels',
    'contrasts': 'contrasts',
    'opposes': 'opposes',
    'contradicts': 'contradicts',  # Symmetric
    'intersects': 'intersects',    # Symmetric
}

# Valid connection types per (source_type, target_type) pair
# Only add inverses that would be valid
VALID_CONNECTIONS = {
    # Evidence level
    ('evidence', 'hypothesis'): ['supports', 'validates', 'parallels', 'contrasts', 'contradicts'],
    ('evidence', 'evidence'): ['parallels', 'contrasts', 'complements', 'complemented_by', 'contradicts'],
    ('evidence', 'concept'): ['parallels', 'contrasts', 'contradicts'],  # Chain skip - limited types
    ('evidence', 'foundational'): ['parallels', 'contrasts', 'contradicts'],  # Chain skip
    ('evidence', 'synthesis'): ['parallels', 'contrasts', 'contradicts'],  # Chain skip
    
    # Hypothesis level
    ('hypothesis', 'evidence'): ['explains', 'explained_by', 'parallels', 'contrasts', 'contradicts'],
    ('hypothesis', 'hypothesis'): ['develops', 'developed_by', 'parallels', 'contrasts', 'complements', 'complemented_by', 'contradicts'],
    ('hypothesis', 'concept'): ['developed_by', 'contrasts', 'contradicts', 'describes', 'described_by'],  # Hypothesis is developed BY concept
    ('hypothesis', 'foundational'): ['developed_by', 'contrasts', 'contradicts', 'describes', 'described_by'],  # Chain skip
    ('hypothesis', 'synthesis'): ['parallels', 'contrasts', 'contradicts'],  # Chain skip
    
    # Concept level
    ('concept', 'evidence'): ['explains', 'parallels', 'contrasts', 'contradicts'],
    ('concept', 'hypothesis'): ['develops', 'contrasts', 'contradicts', 'describes', 'described_by'],  # Concept develops hypothesis
    ('concept', 'concept'): ['develops', 'developed_by', 'parallels', 'contrasts', 'complements', 'complemented_by', 'requires', 'required_by', 'contradicts', 'describes', 'described_by', 'intersects'],
    ('concept', 'foundational'): ['developed_by', 'contrasts', 'contradicts', 'describes', 'described_by', 'intersects'],  # Concept is developed BY foundational
    ('concept', 'synthesis'): ['integrates_into', 'parallels', 'contrasts', 'contradicts', 'intersects'],  # Concept integrates into synthesis
    
    # Foundational level  
    ('foundational', 'evidence'): ['parallels', 'contrasts', 'contradicts'],  # Chain skip
    ('foundational', 'hypothesis'): ['contextualizes', 'contrasts', 'contradicts', 'describes', 'described_by'],  # Foundational contextualizes hypothesis
    ('foundational', 'concept'): ['develops', 'contrasts', 'contradicts', 'describes', 'described_by', 'addresses', 'addressed_by', 'intersects'],  # Foundational develops concept
    ('foundational', 'foundational'): ['parallels', 'contrasts', 'complements', 'complemented_by', 'develops', 'developed_by', 'contradicts', 'describes', 'described_by', 'intersects', 'addresses', 'addressed_by'],
    ('foundational', 'synthesis'): ['parallels', 'contrasts', 'contradicts', 'intersects'],  # Peer level
    
    # Synthesis level
    ('synthesis', 'evidence'): ['parallels', 'contrasts', 'contradicts'],  # Chain skip
    ('synthesis', 'hypothesis'): ['develops', 'contrasts', 'contradicts', 'describes', 'described_by'],  # Synthesis can develop hypothesis
    ('synthesis', 'concept'): ['integrated_from', 'parallels', 'contrasts', 'contradicts', 'describes', 'described_by', 'intersects', 'addresses', 'addressed_by'],  # Synthesis integrates FROM concepts
    ('synthesis', 'foundational'): ['parallels', 'contrasts', 'contradicts', 'intersects'],  # Peer level
    ('synthesis', 'synthesis'): ['complements', 'complemented_by', 'parallels', 'contrasts', 'contradicts', 'intersects'],
}


def load_graph():
    with open(GRAPH_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def save_graph(graph):
    with open(GRAPH_PATH, 'w', encoding='utf-8') as f:
        yaml.dump(graph, f, allow_unicode=True, default_flow_style=False, sort_keys=False, width=120)


def get_existing_connections(node):
    """Get set of (target, type) tuples for a node's connections."""
    return {(c.get('target'), c.get('type')) for c in node.get('connections', [])}


def fix_inverse_connections(dry_run=True, verbose=False):
    """Add missing inverse connections (only valid ones)."""
    graph = load_graph()
    
    # Merge both node sections
    all_nodes = {}
    for section in ['nodes', 'extended_nodes']:
        if section in graph and graph[section]:
            all_nodes.update(graph[section])
    
    additions = []
    skipped = []
    
    # For each connection, check if inverse exists
    for source_id, source_node in all_nodes.items():
        for conn in source_node.get('connections', []):
            target_id = conn.get('target')
            conn_type = conn.get('type')
            
            if not target_id or target_id not in all_nodes:
                continue
            
            # Get expected inverse type
            inverse_type = INVERSE_MAP.get(conn_type)
            if not inverse_type:
                continue
            
            # Get node types for validity check
            source_type = source_node.get('node_type', 'concept')
            target_type = all_nodes[target_id].get('node_type', 'concept')
            
            # Check if the inverse would be VALID for target→source
            valid_types = VALID_CONNECTIONS.get((target_type, source_type), [])
            if inverse_type not in valid_types:
                skipped.append({
                    'from': target_id,
                    'to': source_id,
                    'type': inverse_type,
                    'reason': f"Invalid for {target_type}→{source_type}"
                })
                continue
            
            # Check if target has the inverse connection back
            target_node = all_nodes[target_id]
            existing = get_existing_connections(target_node)
            
            if (source_id, inverse_type) not in existing:
                # For symmetric relations, also check if same type exists
                if inverse_type == conn_type and (source_id, conn_type) in existing:
                    continue
                
                additions.append({
                    'target_node': target_id,
                    'target_type': target_type,
                    'add_target': source_id,
                    'source_type': source_type,
                    'add_type': inverse_type,
                    'because': f"{source_id} --{conn_type}--> {target_id}",
                    'note': conn.get('note', 'Inverse connection')
                })
    
    # Remove duplicates (same addition from multiple paths)
    seen = set()
    unique_additions = []
    for a in additions:
        key = (a['target_node'], a['add_target'], a['add_type'])
        if key not in seen:
            seen.add(key)
            unique_additions.append(a)
    
    additions = unique_additions
    
    # Apply additions
    if not dry_run:
        for add in additions:
            target_id = add['target_node']
            
            # Find which section the target is in
            for section in ['nodes', 'extended_nodes']:
                if section in graph and graph[section] and target_id in graph[section]:
                    node = graph[section][target_id]
                    if 'connections' not in node:
                        node['connections'] = []
                    
                    node['connections'].append({
                        'target': add['add_target'],
                        'type': add['add_type'],
                        'note': f"Inverse of: {add['because']}"
                    })
                    break
    
    # Summary
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Inverse Connection Additions")
    print("=" * 60)
    
    if skipped and verbose:
        print(f"\nSkipped {len(skipped)} invalid inverses")
    
    # Group by inverse type
    by_type = {}
    for a in additions:
        key = a['add_type']
        if key not in by_type:
            by_type[key] = []
        by_type[key].append(a)
    
    for inv_type, items in sorted(by_type.items(), key=lambda x: -len(x[1])):
        print(f"\n{inv_type}: {len(items)} additions")
        if verbose:
            for item in items[:5]:
                print(f"  {item['target_node']} <--{item['add_type']}-- {item['add_target']}")
            if len(items) > 5:
                print(f"  ... and {len(items) - 5} more")
    
    print(f"\n{'=' * 60}")
    print(f"Total additions: {len(additions)}")
    
    if not dry_run:
        save_graph(graph)
        print(f"Saved to {GRAPH_PATH}")
    else:
        print("\nRun without --dry-run to apply changes")
    
    return additions


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add missing inverse connections')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without applying')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show individual changes')
    args = parser.parse_args()
    
    fix_inverse_connections(dry_run=args.dry_run, verbose=args.verbose)
