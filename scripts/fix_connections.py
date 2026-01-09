#!/usr/bin/env python3
"""
Script to fix invalid connection types in the knowledge graph.
Run with --dry-run to preview changes, without to apply them.
"""

import yaml
import sys
import argparse
from pathlib import Path

GRAPH_PATH = Path(__file__).parent.parent / 'graph' / 'knowledge_graph.yaml'

# Conversion rules: (source_type, target_type, old_conn) -> new_conn
# Based on what makes semantic sense given the chain rules
CONVERSION_RULES = {
    # ===== EVIDENCE → HIGHER LEVELS (chain skip violations) =====
    # Evidence → Foundational: supports is invalid (chain skip)
    ('evidence', 'foundational', 'supports'): 'parallels',
    ('evidence', 'foundational', 'validates'): 'parallels',
    ('evidence', 'foundational', 'develops'): 'parallels',
    ('evidence', 'foundational', 'instantiates'): 'parallels',
    
    # Evidence → Concept: supports is invalid (chain skip)
    ('evidence', 'concept', 'supports'): 'parallels',
    ('evidence', 'concept', 'validates'): 'parallels',
    ('evidence', 'concept', 'develops'): 'parallels',
    ('evidence', 'concept', 'instantiates'): 'parallels',
    
    # Evidence → Synthesis: supports is invalid (chain skip)
    ('evidence', 'synthesis', 'supports'): 'parallels',
    ('evidence', 'synthesis', 'validates'): 'parallels',
    ('evidence', 'synthesis', 'instantiates'): 'parallels',
    
    # ===== FOUNDATIONAL → LOWER LEVELS (wrong direction) =====
    # Foundational → Hypothesis: can't skip concept level
    ('foundational', 'hypothesis', 'supports'): 'contextualizes',
    ('foundational', 'hypothesis', 'develops'): 'contextualizes',
    ('foundational', 'hypothesis', 'produces'): 'contextualizes',
    ('foundational', 'hypothesis', 'instantiated_by'): 'contextualizes',
    
    # Foundational → Concept
    ('foundational', 'concept', 'instantiated_by'): 'developed_by',
    ('foundational', 'concept', 'supported_by'): 'developed_by',
    ('foundational', 'concept', 'supports'): 'develops',  # Wrong direction, should be develops
    
    # Foundational → Evidence
    ('foundational', 'evidence', 'instantiated_by'): 'parallels',
    ('foundational', 'evidence', 'supported_by'): 'parallels',
    ('foundational', 'evidence', 'validated_by'): 'parallels',
    ('foundational', 'evidence', 'develops'): 'contextualizes',
    ('foundational', 'evidence', 'supports'): 'parallels',
    
    # Foundational → Synthesis (peer relationship)
    ('foundational', 'synthesis', 'develops'): 'parallels',
    ('foundational', 'synthesis', 'produces'): 'parallels',
    ('foundational', 'synthesis', 'instantiated_by'): 'parallels',
    ('foundational', 'synthesis', 'supported_by'): 'parallels',
    
    # ===== CONCEPT → OTHER LEVELS =====
    # Concept → Evidence: wrong direction
    ('concept', 'evidence', 'supports'): 'explains',
    ('concept', 'evidence', 'develops'): 'explains',
    ('concept', 'evidence', 'produces'): 'explains',
    ('concept', 'evidence', 'supported_by'): 'explained_by',  # Wrong direction
    
    # Concept → Foundational
    ('concept', 'foundational', 'contradicts'): 'contrasts',
    ('concept', 'foundational', 'required_by'): 'developed_by',
    ('concept', 'foundational', 'opposes'): 'contrasts',
    
    # Concept → Hypothesis
    ('concept', 'hypothesis', 'instantiates'): 'develops',
    ('concept', 'hypothesis', 'supports'): 'develops',  # Should use develops instead
    ('concept', 'hypothesis', 'supported_by'): 'developed_by',  # Wrong direction
    ('concept', 'hypothesis', 'developed_from'): 'develops',  # Concept develops hypothesis, not from
    ('concept', 'hypothesis', 'contradicts'): 'contrasts',  # Use contrasts for same-level
    ('concept', 'hypothesis', 'complements'): 'develops',  # Concept to hypothesis is development
    
    # Concept → Concept (peer level)
    ('concept', 'concept', 'instantiates'): 'develops',  # Between peers, use develops not instantiates
    ('concept', 'concept', 'instantiated_by'): 'developed_by',
    
    # Concept → Synthesis
    ('concept', 'synthesis', 'instantiates'): 'integrates_into',
    ('concept', 'synthesis', 'instantiated_by'): 'integrated_from',
    ('concept', 'synthesis', 'supported_by'): 'integrated_from',
    
    # ===== HYPOTHESIS → OTHER LEVELS =====
    # Hypothesis → Foundational: chain skip
    ('hypothesis', 'foundational', 'supports'): 'developed_by',
    ('hypothesis', 'foundational', 'validates'): 'developed_by',
    ('hypothesis', 'foundational', 'instantiates'): 'developed_by',
    
    # Hypothesis → Concept: WRONG DIRECTION! Concept develops hypothesis, not reverse
    ('hypothesis', 'concept', 'develops'): 'developed_by',  # Reverse it
    ('hypothesis', 'concept', 'produces'): 'developed_by',
    ('hypothesis', 'concept', 'requires'): 'developed_by',  # Hypothesis is developed by concept
    ('hypothesis', 'concept', 'complements'): 'developed_by',  # Cross-level, use development relation
    
    # Hypothesis → Evidence: wrong direction
    ('hypothesis', 'evidence', 'supports'): 'explains',
    ('hypothesis', 'evidence', 'develops'): 'explains',
    
    # Hypothesis → Synthesis: chain skip (must go through concept)
    ('hypothesis', 'synthesis', 'supports'): 'parallels',
    ('hypothesis', 'synthesis', 'instantiates'): 'parallels',
    ('hypothesis', 'synthesis', 'develops'): 'parallels',  # Can't develop synthesis directly
    
    # ===== SYNTHESIS → OTHER LEVELS =====
    # Synthesis → Foundational (peer relationship)
    ('synthesis', 'foundational', 'supports'): 'parallels',
    ('synthesis', 'foundational', 'instantiates'): 'parallels',
    ('synthesis', 'foundational', 'validates'): 'parallels',
    ('synthesis', 'foundational', 'develops'): 'parallels',
    
    # Synthesis → Concept: synthesis draws FROM concepts
    ('synthesis', 'concept', 'instantiated_by'): 'integrated_from',
    ('synthesis', 'concept', 'supported_by'): 'integrated_from',
    ('synthesis', 'concept', 'supports'): 'integrated_from',  # Should draw from, not support
    ('synthesis', 'concept', 'instantiates'): 'integrated_from',  # Same: draw from
    
    # Synthesis → Hypothesis
    ('synthesis', 'hypothesis', 'supports'): 'develops',
    ('synthesis', 'hypothesis', 'instantiated_by'): 'develops',
    
    # Synthesis → Evidence: wrong direction
    ('synthesis', 'evidence', 'supported_by'): 'parallels',
    ('synthesis', 'evidence', 'validated_by'): 'parallels',
    ('synthesis', 'evidence', 'supports'): 'parallels',
    ('synthesis', 'evidence', 'requires'): 'parallels',  # Evidence doesn't require synthesis
    
    # Synthesis → Synthesis
    ('synthesis', 'synthesis', 'supports'): 'complements',
    
    # ===== FOUNDATIONAL → FOUNDATIONAL =====
    ('foundational', 'foundational', 'instantiates'): 'develops',
    ('foundational', 'foundational', 'instantiated_by'): 'developed_by',
    ('foundational', 'foundational', 'validates'): 'parallels',  # Peer level
    
    # ===== FOUNDATIONAL → CONCEPT (more) =====
    ('foundational', 'concept', 'instantiates'): 'develops',  # Should be develops
    ('foundational', 'concept', 'opposes'): 'contrasts',
    ('foundational', 'concept', 'developed_by'): 'develops',  # Wrong direction
    ('foundational', 'evidence', 'validated_by'): 'parallels',
    
    # ===== CONCEPT → HYPOTHESIS (more) =====
    ('concept', 'hypothesis', 'developed_by'): 'develops',  # Wrong direction - concept develops hypothesis
    
    # ===== CONCEPT → SYNTHESIS (more) =====
    ('concept', 'synthesis', 'integrated_from'): 'integrates_into',  # Wrong direction
    
    # ===== CONCEPT → EVIDENCE (more) =====
    ('concept', 'evidence', 'explained_by'): 'explains',  # Wrong direction
    ('concept', 'evidence', 'validated_by'): 'explains',  # Wrong direction
    
    # ===== CONCEPT → FOUNDATIONAL =====
    ('concept', 'foundational', 'develops'): 'developed_by',  # Wrong direction
    
    # ===== EVIDENCE → HYPOTHESIS =====
    ('evidence', 'hypothesis', 'develops'): 'supports',  # Evidence supports hypothesis, not develops
    ('evidence', 'hypothesis', 'developed_by'): 'supports',  # Wrong direction
    ('evidence', 'hypothesis', 'explained_by'): 'supports',  # Wrong direction - evidence supports, doesn't get explained
    ('evidence', 'hypothesis', 'contextualized_by'): 'supports',  # Wrong direction
    
    # ===== EVIDENCE → CONCEPT =====
    ('evidence', 'concept', 'developed_by'): 'parallels',  # Chain skip
    ('evidence', 'concept', 'contradicts'): 'contrasts',  # Use contrasts
    ('evidence', 'concept', 'requires'): 'parallels',  # Can't require across chain skip
    ('evidence', 'concept', 'produced_by'): 'parallels',  # Chain skip
    ('evidence', 'concept', 'reveals'): 'parallels',  # Chain skip
    ('evidence', 'concept', 'explained_by'): 'parallels',  # Chain skip - evidence doesn't get explained by concept
    
    # ===== EVIDENCE → SYNTHESIS =====
    ('evidence', 'synthesis', 'develops'): 'parallels',  # Chain skip
    ('evidence', 'synthesis', 'explained_by'): 'parallels',  # Chain skip
    
    # ===== EVIDENCE → FOUNDATIONAL =====
    ('evidence', 'foundational', 'contextualized_by'): 'parallels',  # Chain skip
    
    # ===== EVIDENCE → HYPOTHESIS =====
    ('evidence', 'hypothesis', 'requires'): 'supports',  # Evidence supports
    ('evidence', 'hypothesis', 'contained_by'): 'supports',
    ('evidence', 'hypothesis', 'complements'): 'supports',
    
    # ===== EVIDENCE → EVIDENCE =====
    ('evidence', 'evidence', 'instantiates'): 'parallels',  # Use parallels for peer
    ('evidence', 'evidence', 'addresses'): 'parallels',  # Not valid type
    ('evidence', 'evidence', 'contextualizes'): 'parallels',  # Use parallels
    ('evidence', 'evidence', 'operationalizes'): 'parallels',
    ('evidence', 'evidence', 'explains'): 'parallels',  # Peer level
    ('evidence', 'evidence', 'applies'): 'parallels',
    
    # ===== HYPOTHESIS → CONCEPT =====
    ('hypothesis', 'concept', 'contradicts'): 'contrasts',  # Use contrasts
    ('hypothesis', 'concept', 'opposes'): 'contrasts',
    ('hypothesis', 'concept', 'supported_by'): 'developed_by',  # Wrong direction
    ('hypothesis', 'concept', 'validates'): 'developed_by',  # Wrong direction
    ('hypothesis', 'concept', 'revealed_by'): 'developed_by',
    ('hypothesis', 'concept', 'required_by'): 'developed_by',
    ('hypothesis', 'concept', 'produced_by'): 'developed_by',
    ('hypothesis', 'concept', 'contained'): 'developed_by',
    ('hypothesis', 'concept', 'contains'): 'developed_by',
    ('hypothesis', 'concept', 'contextualized_by'): 'developed_by',  # Hypothesis is developed by concept
    ('hypothesis', 'concept', 'explained_by'): 'developed_by',  # Same
    
    # ===== HYPOTHESIS → HYPOTHESIS =====
    ('hypothesis', 'hypothesis', 'instantiates'): 'develops',  # Use develops for peers
    ('hypothesis', 'hypothesis', 'produced_by'): 'developed_by',
    ('hypothesis', 'hypothesis', 'produces'): 'develops',
    ('hypothesis', 'hypothesis', 'contextualized_by'): 'parallels',  # Peer level
    ('hypothesis', 'hypothesis', 'explained_by'): 'develops',
    
    # ===== HYPOTHESIS → FOUNDATIONAL =====
    ('hypothesis', 'foundational', 'contradicts'): 'contrasts',  # Use contrasts
    ('hypothesis', 'foundational', 'requires'): 'developed_by',  # Chain skip
    ('hypothesis', 'foundational', 'produces'): 'developed_by',
    ('hypothesis', 'foundational', 'supported_by'): 'developed_by',
    ('hypothesis', 'foundational', 'contextualized_by'): 'developed_by',  # Wrong direction
    ('hypothesis', 'foundational', 'explained_by'): 'developed_by',  # Wrong direction
    
    # ===== HYPOTHESIS → EVIDENCE =====
    ('hypothesis', 'evidence', 'validates'): 'explains',  # Wrong direction
    ('hypothesis', 'evidence', 'contains'): 'explains',
    ('hypothesis', 'evidence', 'opposes'): 'contrasts',  # Use contrasts for cross-level opposition
    ('hypothesis', 'evidence', 'contradicts'): 'contrasts',  # Hypothesis contrasts evidence, doesn't contradict
    
    # ===== HYPOTHESIS → SYNTHESIS =====
    ('hypothesis', 'synthesis', 'supported_by'): 'parallels',  # Chain skip
    ('hypothesis', 'synthesis', 'produced_by'): 'parallels',
    ('hypothesis', 'synthesis', 'developed_by'): 'parallels',  # Chain skip
    ('hypothesis', 'synthesis', 'contextualized_by'): 'parallels',  # Chain skip
    
    # ===== SYNTHESIS → CONCEPT =====
    ('synthesis', 'concept', 'opposes'): 'contrasts',
    ('synthesis', 'concept', 'produced_by'): 'integrated_from',
    ('synthesis', 'concept', 'developed_by'): 'integrated_from',
    ('synthesis', 'concept', 'precedes'): 'integrated_from',  # Wrong direction
    ('synthesis', 'concept', 'validates'): 'integrated_from',  # Wrong direction
    ('synthesis', 'concept', 'reveals'): 'integrated_from',
    ('synthesis', 'concept', 'explained_by'): 'integrated_from',  # Synthesis integrates from concept
    
    # ===== SYNTHESIS → EVIDENCE =====
    ('synthesis', 'evidence', 'instantiated_by'): 'parallels',
    ('synthesis', 'evidence', 'develops'): 'parallels',
    ('synthesis', 'evidence', 'validates'): 'parallels',
    
    # ===== SYNTHESIS → FOUNDATIONAL =====
    ('synthesis', 'foundational', 'produced_by'): 'parallels',  # Peer level
    ('synthesis', 'foundational', 'supported_by'): 'parallels',
    
    # ===== SYNTHESIS → HYPOTHESIS =====
    ('synthesis', 'hypothesis', 'validated_by'): 'develops',
    ('synthesis', 'hypothesis', 'validates'): 'develops',
    ('synthesis', 'hypothesis', 'instantiates'): 'develops',
    ('synthesis', 'hypothesis', 'opposes'): 'contrasts',
    ('synthesis', 'hypothesis', 'produces'): 'develops',
    ('synthesis', 'hypothesis', 'supported_by'): 'develops',  # Wrong direction
    
    # ===== SYNTHESIS → SYNTHESIS =====
    ('synthesis', 'synthesis', 'supported_by'): 'complements',
    ('synthesis', 'synthesis', 'instantiates'): 'complements',
    ('synthesis', 'synthesis', 'validates'): 'complements',
    
    # ===== SYNTHESIS → EVIDENCE =====
    ('synthesis', 'evidence', 'contextualized_by'): 'parallels',  # Chain skip
    
    # ===== FOUNDATIONAL → FOUNDATIONAL =====
    ('foundational', 'foundational', 'validated_by'): 'parallels',
    ('foundational', 'foundational', 'supports'): 'parallels',
    
    # ===== FOUNDATIONAL → HYPOTHESIS =====
    ('foundational', 'hypothesis', 'validated_by'): 'contextualizes',
    ('foundational', 'hypothesis', 'supported_by'): 'contextualizes',
    ('foundational', 'hypothesis', 'opposes'): 'contrasts',
    ('foundational', 'hypothesis', 'contradicts'): 'contrasts',
    ('foundational', 'hypothesis', 'develops'): 'contextualizes',  # Foundational contextualizes, doesn't develop hypothesis directly
    
    # ===== FOUNDATIONAL → CONCEPT =====
    ('foundational', 'concept', 'validates'): 'develops',
    ('foundational', 'concept', 'produced_by'): 'develops',
    ('foundational', 'concept', 'contradicts'): 'contrasts',
    ('foundational', 'concept', 'complements'): 'develops',
    ('foundational', 'concept', 'developed_by'): 'develops',  # Wrong direction - foundational develops concept
    
    # ===== FOUNDATIONAL → EVIDENCE =====
    ('foundational', 'evidence', 'contextualized_by'): 'parallels',  # Chain skip
    
    # ===== FOUNDATIONAL → SYNTHESIS =====
    ('foundational', 'synthesis', 'validated_by'): 'parallels',
    
    # ===== CONCEPT → CONCEPT =====
    ('concept', 'concept', 'produces'): 'develops',
    ('concept', 'concept', 'produced_by'): 'developed_by',
    ('concept', 'concept', 'applies'): 'develops',
    ('concept', 'concept', 'operationalizes'): 'develops',
    
    # ===== CONCEPT → EVIDENCE =====
    ('concept', 'evidence', 'complements'): 'explains',
    ('concept', 'evidence', 'contains'): 'explains',
    ('concept', 'evidence', 'instantiated_by'): 'explains',
    ('concept', 'evidence', 'precedes'): 'explains',
    ('concept', 'evidence', 'requires'): 'explains',
    
    # ===== CONCEPT → FOUNDATIONAL =====
    ('concept', 'foundational', 'requires'): 'developed_by',
    ('concept', 'foundational', 'supported_by'): 'developed_by',
    ('concept', 'foundational', 'developed_from'): 'developed_by',
    ('concept', 'foundational', 'produces'): 'developed_by',
    ('concept', 'foundational', 'explained_by'): 'developed_by',  # Concept is developed by foundational
    
    # ===== CONCEPT → HYPOTHESIS =====
    ('concept', 'hypothesis', 'instantiated_by'): 'develops',
    ('concept', 'hypothesis', 'opposes'): 'contrasts',
    ('concept', 'hypothesis', 'revealed_by'): 'develops',
    ('concept', 'hypothesis', 'explained_by'): 'develops',  # Concept develops hypothesis
    
    # ===== CONCEPT → CONCEPT =====
    ('concept', 'concept', 'contextualized_by'): 'parallels',  # Peer level
    ('concept', 'concept', 'explained_by'): 'develops',  # One concept develops another
    
    # ===== CONCEPT → SYNTHESIS =====
    ('concept', 'synthesis', 'developed_by'): 'integrates_into',
    ('concept', 'synthesis', 'reveals'): 'integrates_into',
    ('concept', 'synthesis', 'complements'): 'integrates_into',
    ('concept', 'synthesis', 'opposes'): 'contrasts',
}

# Some connections need the inverse updated when we fix them
INVERSE_MAP = {
    'supports': 'supported_by',
    'supported_by': 'supports',
    'develops': 'developed_by',
    'developed_by': 'develops',
    'validates': 'validated_by',
    'validated_by': 'validates',
    'instantiates': 'instantiated_by',
    'instantiated_by': 'instantiates',
    'integrates_into': 'integrated_from',
    'integrated_from': 'integrates_into',
    'parallels': 'parallels',
    'contrasts': 'contrasts',
    'complements': 'complemented_by',
    'complemented_by': 'complements',
    'contextualizes': 'contextualized_by',
    'explains': 'explained_by',
}


def load_graph():
    with open(GRAPH_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def save_graph(graph):
    with open(GRAPH_PATH, 'w', encoding='utf-8') as f:
        yaml.dump(graph, f, allow_unicode=True, default_flow_style=False, sort_keys=False, width=120)


def get_node_type(nodes, node_id):
    if node_id in nodes:
        return nodes[node_id].get('node_type', 'unknown')
    return 'unknown'


def fix_connections(dry_run=True, verbose=False):
    """Fix invalid connection types based on conversion rules."""
    graph = load_graph()
    # Merge both nodes sections for lookup
    all_nodes = {**graph.get('nodes', {}), **graph.get('extended_nodes', {})}
    
    changes = []
    skipped = []
    
    # Process both sections
    for section_name in ['nodes', 'extended_nodes']:
        section = graph.get(section_name, {})
        if not section:
            continue
            
        for node_id, node in section.items():
            if 'connections' not in node:
                continue
                
            source_type = get_node_type(all_nodes, node_id)
            
            for conn in node['connections']:
                target_id = conn.get('target')
                conn_type = conn.get('type')
                target_type = get_node_type(all_nodes, target_id)
                
                # Check if this connection needs fixing
                key = (source_type, target_type, conn_type)
                if key in CONVERSION_RULES:
                    new_type = CONVERSION_RULES[key]
                    changes.append({
                        'source': node_id,
                        'source_type': source_type,
                        'target': target_id,
                        'target_type': target_type,
                        'old': conn_type,
                        'new': new_type
                    })
                    
                    if not dry_run:
                        conn['type'] = new_type
    
    # Summary
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Connection Type Fixes")
    print("=" * 60)
    
    # Group by conversion type
    by_conversion = {}
    for c in changes:
        key = f"{c['source_type']}→{c['target_type']}: {c['old']} → {c['new']}"
        if key not in by_conversion:
            by_conversion[key] = []
        by_conversion[key].append(c)
    
    for conv_type, items in sorted(by_conversion.items()):
        print(f"\n{conv_type} ({len(items)} changes)")
        if verbose:
            for item in items[:5]:
                print(f"  {item['source']} → {item['target']}")
            if len(items) > 5:
                print(f"  ... and {len(items) - 5} more")
    
    print(f"\n{'=' * 60}")
    print(f"Total changes: {len(changes)}")
    
    if not dry_run:
        save_graph(graph)
        print(f"Saved to {GRAPH_PATH}")
    else:
        print("\nRun without --dry-run to apply changes")
    
    return changes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fix invalid connection types')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without applying')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show individual changes')
    args = parser.parse_args()
    
    fix_connections(dry_run=args.dry_run, verbose=args.verbose)
