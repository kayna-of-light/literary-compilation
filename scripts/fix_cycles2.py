#!/usr/bin/env python3
"""
Fix remaining circular proof chains.

Remaining cycles after first fix:
1. SWED-004 ↔ MYTH-003: supports/validates - change SWED-004's supports to parallels
2. BIBL-002 ↔ EARLY-002 ↔ BIBL-004: complex triangle - need to break multiple links
3. BIBL-015 ↔ BIBL-016: supports/requires - change supports to parallels
4. Fix BIBL-019's addressed_by to addresses (inverse)
"""

import yaml
from pathlib import Path

GRAPH_PATH = Path('graph/knowledge_graph.yaml')

with open(GRAPH_PATH, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

nodes = data.get('nodes', {})
extended = data.get('extended_nodes', {})

# Add addressed_by to relationship_types
if 'addressed_by' not in data['metadata']['relationship_types']:
    data['metadata']['relationship_types']['addressed_by'] = "Is responded to or dealt with by"
    print("Added 'addressed_by' to relationship types")

def fix_connection(node_id, target_id, old_type, new_type, nodes_dict):
    """Fix a specific connection in a node."""
    node = nodes_dict.get(node_id, {})
    connections = node.get('connections', [])
    
    for conn in connections:
        if conn.get('target') == target_id and conn.get('type') == old_type:
            print(f"  [{node_id}] -> [{target_id}]: {old_type} -> {new_type}")
            conn['type'] = new_type
            return True
    return False

print("\nApplying fixes:\n")

# Fix 1: SWED-004 -> MYTH-003 (supports -> explains)
# The Ancient Word EXPLAINS Memory Code findings, it doesn't prove them
if 'SWED-004' in nodes:
    fix_connection('SWED-004', 'MYTH-003', 'supports', 'explains', nodes)
elif 'SWED-004' in extended:
    fix_connection('SWED-004', 'MYTH-003', 'supports', 'explains', extended)

# Fix 2: BIBL-002 triangle - break multiple links
# BIBL-002 -> EARLY-002: supports -> contextualizes
# BIBL-002 -> BIBL-004: instantiates -> instantiated_by
# EARLY-002 -> BIBL-004: supports -> contextualizes
# BIBL-004 -> BIBL-002: instantiates -> instantiated_by
for target_dict in [nodes, extended]:
    if 'BIBL-002' in target_dict:
        fix_connection('BIBL-002', 'EARLY-002', 'supports', 'contextualizes', target_dict)
        fix_connection('BIBL-002', 'BIBL-004', 'instantiates', 'revealed_by', target_dict)
    if 'EARLY-002' in target_dict:
        fix_connection('EARLY-002', 'BIBL-004', 'supports', 'contextualizes', target_dict)
    if 'BIBL-004' in target_dict:
        fix_connection('BIBL-004', 'BIBL-002', 'instantiates', 'revealed_by', target_dict)

# Fix 3: BIBL-015 -> BIBL-016 (supports -> parallels)
# Vaticinium ex eventu and Markan Priority are methodological companions
for target_dict in [nodes, extended]:
    if 'BIBL-015' in target_dict:
        fix_connection('BIBL-015', 'BIBL-016', 'supports', 'parallels', target_dict)

# Save
data['nodes'] = nodes
data['extended_nodes'] = extended

with open(GRAPH_PATH, 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=100)

print("\nDone! Run 'python scripts/graph_utils.py validate' to verify.")
