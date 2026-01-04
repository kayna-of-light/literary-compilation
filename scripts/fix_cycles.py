#!/usr/bin/env python3
"""
Fix circular proof chains in the knowledge graph.

This script implements the analyzed fixes for the 17 circular proof chains.
The key insight is that many "circular proofs" are actually:
1. Parallel relationships (mutual support, not proof)
2. Inverse relationships (A requires B, B is required_by A - same fact twice)
3. Wrong relationship types (e.g., "instantiates" used bidirectionally)

Changes made (relationship type changed FROM -> TO):
1. SWED-001 -> CROSS-001: supports -> required_by (inverse of requires)
2. SWED-001 <-> SWED-004: requires/requires -> parallels (mutual interdependence)
3. MYTH-003 -> SWED-004: supports -> validates (empirical validates concept)
4. SWED-002 -> CROSS-002: supports -> required_by
5. EARLY-004 -> SWED-002: instantiates -> instantiated_by (direction fix)
6. EARLY-004 <-> SWED-008: instantiates/instantiates -> parallels (mutual aspects)
7. CROSS-003 -> CONSC-001: supports -> required_by
8. CONSC-001 -> CONSC-002: supports -> supported_by (CDE supported BY DOPS)
9. (Fixed by 7 & 8, plus CONSC-020 below)
10. GNOS-001 -> SWED-005: instantiates -> instantiated_by
11. SWED-005 -> EARLY-003: instantiates -> instantiated_by (Pauline instantiates Proprium)
12. BIBL-002 -> BIBL-001: instantiates -> instantiated_by
13. Early church nodes: supports -> contextualizes (historical context, not proof)
14. EARLY-002 -> BIBL-002: develops -> developed_by
15. BIBL-016 -> BIBL-015: requires -> requires (keep - asymmetric already)
16. BIBL-019 -> BIBL-018: supports -> addressed_by
17. CONSC-031 -> CONSC-034: requires -> contains
"""

import yaml
import re
from pathlib import Path

GRAPH_PATH = Path('graph/knowledge_graph.yaml')

# Load the graph
with open(GRAPH_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Parse YAML
data = yaml.safe_load(content)
nodes = data.get('nodes', {})
extended = data.get('extended_nodes', {})

def find_and_fix_connection(node_id, target_id, old_type, new_type, nodes_dict):
    """Fix a specific connection in a node."""
    node = nodes_dict.get(node_id, {})
    connections = node.get('connections', [])
    changed = False
    
    for conn in connections:
        if conn.get('target') == target_id and conn.get('type') == old_type:
            print(f"  [{node_id}] -> [{target_id}]: {old_type} -> {new_type}")
            conn['type'] = new_type
            changed = True
            break
    
    return changed

print("=" * 60)
print("FIXING CIRCULAR PROOF CHAINS")
print("=" * 60)

changes = [
    # Cycle 1: CROSS-001 <-> SWED-001
    ('SWED-001', 'CROSS-001', 'supports', 'required_by'),
    
    # Cycle 2: SWED-001 <-> SWED-004 (make parallel - mutual interdependence)
    ('SWED-001', 'SWED-004', 'requires', 'parallels'),
    ('SWED-004', 'SWED-001', 'requires', 'parallels'),
    
    # Cycle 3: SWED-004 <-> MYTH-003
    ('MYTH-003', 'SWED-004', 'supports', 'validates'),
    
    # Cycle 4: CROSS-002 <-> SWED-002
    ('SWED-002', 'CROSS-002', 'supports', 'required_by'),
    
    # Cycle 5: SWED-002 <-> EARLY-004
    ('EARLY-004', 'SWED-002', 'instantiates', 'instantiated_by'),
    
    # Cycle 6: EARLY-004 <-> SWED-008 (make parallel)
    ('EARLY-004', 'SWED-008', 'instantiates', 'parallels'),
    ('SWED-008', 'EARLY-004', 'instantiates', 'parallels'),
    
    # Cycle 7: CROSS-003 <-> CONSC-001
    ('CROSS-003', 'CONSC-001', 'supports', 'required_by'),
    
    # Cycle 8: CONSC-001 <-> CONSC-002
    ('CONSC-001', 'CONSC-002', 'supports', 'supported_by'),
    
    # Cycle 10: SWED-005 <-> GNOS-001
    ('GNOS-001', 'SWED-005', 'instantiates', 'instantiated_by'),
    
    # Cycle 11: SWED-005 <-> EARLY-003
    ('SWED-005', 'EARLY-003', 'instantiates', 'instantiated_by'),
    
    # Cycle 12: BIBL-001 <-> BIBL-002
    ('BIBL-002', 'BIBL-001', 'instantiates', 'instantiated_by'),
    
    # Cycle 13: EARLY-002 <-> EARLY-010 <-> EARLY-007
    ('EARLY-002', 'EARLY-010', 'supports', 'contextualizes'),
    ('EARLY-010', 'EARLY-007', 'supports', 'contextualizes'),
    ('EARLY-007', 'EARLY-002', 'supports', 'contextualizes'),
    
    # Cycle 14: BIBL-002 <-> EARLY-002 <-> BIBL-004
    ('EARLY-002', 'BIBL-002', 'develops', 'developed_by'),
    
    # Cycle 16: BIBL-018 <-> BIBL-019
    ('BIBL-019', 'BIBL-018', 'supports', 'addressed_by'),
    
    # Cycle 17: CONSC-031 <-> CONSC-034
    ('CONSC-031', 'CONSC-034', 'requires', 'contains'),
]

print("\nApplying changes:\n")
change_count = 0

for node_id, target_id, old_type, new_type in changes:
    # Check in nodes first
    if node_id in nodes:
        if find_and_fix_connection(node_id, target_id, old_type, new_type, nodes):
            change_count += 1
    # Check in extended_nodes
    elif node_id in extended:
        if find_and_fix_connection(node_id, target_id, old_type, new_type, extended):
            change_count += 1
    else:
        print(f"  WARNING: Node {node_id} not found!")

print(f"\nTotal changes: {change_count}")

# Reconstruct the YAML file
data['nodes'] = nodes
data['extended_nodes'] = extended

print("\nSaving updated graph...")

with open(GRAPH_PATH, 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=100)

print("Done!")
print("\nRun 'python scripts/graph_utils.py validate' to verify fixes.")
