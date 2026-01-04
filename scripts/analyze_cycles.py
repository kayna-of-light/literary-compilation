#!/usr/bin/env python3
"""Analyze circular proof chains in the knowledge graph."""

import yaml

with open('graph/knowledge_graph.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

nodes = data.get('nodes', {})
extended = data.get('extended_nodes', {})
nodes.update(extended)

# The 17 cycles to analyze (pairs form bidirectional relationships)
cycles = [
    ['CROSS-001', 'SWED-001'],
    ['SWED-001', 'SWED-004'],
    ['SWED-004', 'MYTH-003'],
    ['CROSS-002', 'SWED-002'],
    ['SWED-002', 'EARLY-004'],
    ['EARLY-004', 'SWED-008'],
    ['CROSS-003', 'CONSC-001'],
    ['CONSC-001', 'CONSC-002'],
    ['CROSS-003', 'CONSC-001', 'CONSC-002', 'CONSC-020'],
    ['SWED-005', 'GNOS-001'],
    ['SWED-005', 'EARLY-003'],
    ['BIBL-001', 'BIBL-002'],
    ['EARLY-002', 'EARLY-010', 'EARLY-007'],
    ['BIBL-002', 'EARLY-002', 'BIBL-004'],
    ['BIBL-015', 'BIBL-016'],
    ['BIBL-018', 'BIBL-019'],
    ['CONSC-031', 'CONSC-034'],
]

print('=' * 80)
print('CIRCULAR PROOF CHAIN ANALYSIS')
print('=' * 80)

for i, cycle in enumerate(cycles, 1):
    cycle_str = ' <-> '.join(cycle)
    print(f'\n--- Cycle {i}: {cycle_str} ---\n')
    
    # For each node in the cycle, show its connections to other cycle members
    for node_id in cycle:
        node = nodes.get(node_id, {})
        title = node.get('title', 'Unknown')[:50]
        conns = node.get('connections', [])
        
        print(f'  [{node_id}] {title}')
        
        # Show connections to other cycle members
        for conn in conns:
            target = conn.get('target')
            if target in cycle and target != node_id:
                rel_type = conn.get('type', 'unknown')
                note = conn.get('note', '')
                note_display = note[:55] + '...' if len(note) > 55 else note
                print(f'    --({rel_type})--> [{target}]')
                if note:
                    print(f'       "{note_display}"')
        print()
