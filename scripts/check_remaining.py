#!/usr/bin/env python3
"""Check remaining cycles."""
import yaml

with open('graph/knowledge_graph.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

nodes = {**data.get('nodes', {}), **data.get('extended_nodes', {})}

remaining = [
    ['SWED-004', 'MYTH-003'],
    ['BIBL-002', 'EARLY-002', 'BIBL-004'],
    ['BIBL-015', 'BIBL-016'],
]

for cycle in remaining:
    print(f'Cycle: {cycle}')
    for node_id in cycle:
        node = nodes.get(node_id, {})
        print(f'  [{node_id}]')
        for conn in node.get('connections', []):
            if conn.get('target') in cycle:
                rel = conn.get('type')
                tgt = conn.get('target')
                print(f'    --({rel})--> [{tgt}]')
    print()
