#!/usr/bin/env python3
"""
Batch add confidence_factors to evidence nodes.

This script adds confidence factors based on analyzed source chains.
Each factor is an enum value that graph_utils.py converts to scores.
"""

import yaml
from pathlib import Path

GRAPH_PATH = Path('graph/knowledge_graph.yaml')

with open(GRAPH_PATH, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

nodes = data.get('nodes', {})
extended = data.get('extended_nodes', {})

# Confidence factors for evidence nodes
# Based on analysis of source chains and research methodology

CONFIDENCE_FACTORS = {
    # ========== CONSCIOUSNESS STUDIES (CONSC) ==========
    
    "CONSC-002": {  # DOPS Past-Life Memory Research
        "methodology": "retrospective",  # Case collection with protocols, not RCT
        "sample_size": "large_1000+",     # 2,500+ documented cases
        "replication": "internal_replicated",  # Stevenson → Tucker continuation
        "peer_review": "peer_reviewed_book",  # Academic press publications
        "source_chain_quality": "primary_verified"  # Direct citations to studies
    },
    
    "CONSC-003": {  # Life Review Phenomenon
        "methodology": "retrospective",  # Analysis of NDE reports
        "sample_size": "large_1000+",     # Part of larger NDE databases
        "replication": "independent_replicated",  # Multiple researchers globally
        "peer_review": "peer_reviewed_journal",  # JNDS, JSPR publications
        "source_chain_quality": "primary_verified"
    },
    
    "CONSC-004": {  # NDE Phenomenology
        "methodology": "prospective",  # van Lommel had prospective design
        "sample_size": "large_1000+",     # Multiple studies combined
        "replication": "independent_replicated",  # Parnia, van Lommel, Greyson
        "peer_review": "peer_reviewed_journal",  # Lancet, Resuscitation
        "source_chain_quality": "primary_verified"
    },
    
    "CONSC-017": {  # NDE Multi-Axial Framework
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "internal_replicated",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"  # Framework synthesis
    },
    
    "CONSC-019": {  # Group NDE Phenomenology
        "methodology": "case_study",  # Rare phenomenon, individual cases
        "sample_size": "minimal_<10",  # Very few documented group NDEs
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "CONSC-021": {  # CFT Empirical Validation
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "CONSC-022": {  # Unknown Presence (61.8%)
        "methodology": "retrospective",
        "sample_size": "medium_100-999",  # From NDE database
        "replication": "internal_replicated",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "CONSC-023": {  # Life Review No Condemnation (84.8%)
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "internal_replicated",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "CONSC-024": {  # Theological Framework Mismatch
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "internal_replicated",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "CONSC-025": {  # Cross-Religious Fear Loss (60-63%)
        "methodology": "retrospective",
        "sample_size": "large_1000+",  # NDERF dataset
        "replication": "independent_replicated",  # Multiple studies
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "CONSC-026": {  # Being of Light Entity Evidence
        "methodology": "retrospective",
        "sample_size": "large_1000+",
        "replication": "independent_replicated",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "CONSC-027": {  # Being of Light Authority
        "methodology": "retrospective",
        "sample_size": "large_1000+",
        "replication": "independent_replicated",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "CONSC-028": {  # Normative Path Continuation
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "tertiary"  # Framework analysis
    },
    
    "CONSC-029": {  # Pure Projection Model Weakened
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "internal_replicated",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "CONSC-030": {  # Empathetic Life Review (25.7%)
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "internal_replicated",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "CONSC-031": {  # Threefold Path Distribution
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "tertiary"  # Framework synthesis
    },
    
    "CONSC-032": {  # Volunteer Soul Commissioning
        "methodology": "retrospective",
        "sample_size": "small_10-99",  # Subset of NDEs
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "tertiary"
    },
    
    "CONSC-033": {  # Normative Path Four-Stage
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "tertiary"
    },
    
    "CONSC-034": {  # Restorative Incarnation Violent Death >70%
        "methodology": "retrospective",
        "sample_size": "large_1000+",  # DOPS corpus
        "replication": "internal_replicated",
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "primary_verified"
    },
    
    "CONSC-035": {  # ML Predictive (74.5%)
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "tertiary"
    },
    
    "CONSC-036": {  # Demographic Non-Prediction
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "tertiary"
    },
    
    "CONSC-037": {  # Enhanced Transformation (d=0.59)
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "tertiary"
    },
    
    "CONSC-038": {  # Telepathic Discriminator (V=0.261)
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "tertiary"
    },
    
    "CONSC-039": {  # Mission Typology 10 Categories
        "methodology": "retrospective",
        "sample_size": "small_10-99",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "tertiary"
    },
    
    "CONSC-040": {  # Type A/B DOPS Gold Standard
        "methodology": "retrospective",
        "sample_size": "large_1000+",
        "replication": "internal_replicated",
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "primary_verified"
    },
    
    "CONSC-041": {  # Birthmark 88% Verification
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "internal_replicated",
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "primary_verified"
    },
    
    "CONSC-044": {  # NDE Entity Ecosystem
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "CONSC-045": {  # Correspondential Validation from NDE
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "tertiary"  # Framework application
    },
    
    "CONSC-046": {  # Restorative Return DOPS Audit
        "methodology": "retrospective",
        "sample_size": "large_1000+",
        "replication": "internal_replicated",
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "secondary"  # Gemini audit
    },
    
    "CONSC-047": {  # SOCS Selection Bias
        "methodology": "retrospective",
        "sample_size": "large_1000+",
        "replication": "internal_replicated",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "CONSC-048": {  # Ohkado Reverse Cases
        "methodology": "case_study",
        "sample_size": "small_10-99",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "CONSC-049": {  # VPE Protocol
        "methodology": "theoretical",  # Proposed protocol
        "sample_size": "na",
        "replication": "na",
        "peer_review": "unpublished",  # Framework proposal
        "source_chain_quality": "tertiary"
    },
    
    "CONSC-050": {  # COPET Proposal
        "methodology": "theoretical",
        "sample_size": "na",
        "replication": "na",
        "peer_review": "unpublished",
        "source_chain_quality": "tertiary"
    },
    
    "CONSC-051": {  # Return Reason Discriminant
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "tertiary"
    },
    
    "CONSC-052": {  # Pre-Birth Indicator Hierarchy
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "tertiary"
    },
    
    "CONSC-053": {  # Soul Path Population Distribution
        "methodology": "retrospective",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "unpublished",  # Framework synthesis
        "source_chain_quality": "tertiary"
    },
    
    "CONSC-054": {  # Spontaneous Remission
        "methodology": "case_study",
        "sample_size": "medium_100-999",
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    # ========== BIBLICAL SCHOLARSHIP (BIBL) ==========
    
    "BIBL-006": {  # Western Non-Interpolations
        "methodology": "textual_critical",
        "sample_size": "population",  # All NT manuscripts
        "replication": "independent_replicated",  # Westcott-Hort, NA28
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "primary_verified"
    },
    
    "BIBL-011": {  # Criterion of Temptation
        "methodology": "textual_critical",
        "sample_size": "na",  # Methodological principle
        "replication": "internal_replicated",
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "primary_verified"
    },
    
    "BIBL-013": {  # 4.2 Kiloyear Event
        "methodology": "observational",  # Climate/archaeological data
        "sample_size": "population",  # Global evidence
        "replication": "independent_replicated",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    "BIBL-019": {  # Minor Agreements Problem
        "methodology": "textual_critical",
        "sample_size": "population",  # Synoptic corpus
        "replication": "independent_replicated",
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "primary_verified"
    },
    
    "BIBL-021": {  # Historical Jesus Bedrock
        "methodology": "textual_critical",
        "sample_size": "population",
        "replication": "independent_replicated",  # Scholarly consensus
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "primary_verified"
    },
    
    # ========== EARLY CHRISTIAN HISTORY (EARLY) ==========
    
    "EARLY-010": {  # James the Just
        "methodology": "textual_critical",
        "sample_size": "population",  # All relevant texts
        "replication": "independent_replicated",
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "primary_verified"
    },
    
    "EARLY-011": {  # Historical Mariamene
        "methodology": "textual_critical",
        "sample_size": "small_10-99",  # Limited sources
        "replication": "single_study",
        "peer_review": "peer_reviewed_journal",
        "source_chain_quality": "secondary"
    },
    
    # ========== MYTHOLOGICAL STUDIES (MYTH) ==========
    
    "MYTH-005": {  # Enochic Literature
        "methodology": "textual_critical",
        "sample_size": "population",  # All Enochic texts
        "replication": "independent_replicated",
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "primary_verified"
    },
    
    "MYTH-008": {  # Echoes of Ancient Word
        "methodology": "textual_critical",
        "sample_size": "population",
        "replication": "single_study",
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "secondary"
    },
    
    "MYTH-011": {  # Archangelic Hierarchy Evolution
        "methodology": "textual_critical",
        "sample_size": "population",
        "replication": "independent_replicated",
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "secondary"
    },
    
    "MYTH-014": {  # Enochian 364-Day Calendar
        "methodology": "textual_critical",
        "sample_size": "na",  # Single textual tradition
        "replication": "independent_replicated",
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "primary_verified"
    },
    
    "MYTH-017": {  # Dispensational Animal Sequence
        "methodology": "textual_critical",
        "sample_size": "na",
        "replication": "single_study",
        "peer_review": "peer_reviewed_book",
        "source_chain_quality": "secondary"
    },
}

def add_confidence_factors(node_id, factors, nodes_dict):
    """Add confidence_factors to a node."""
    if node_id not in nodes_dict:
        return False
    
    nodes_dict[node_id]['confidence_factors'] = factors
    return True

print("=" * 60)
print("ADDING CONFIDENCE FACTORS TO EVIDENCE NODES")
print("=" * 60)

count = 0
for node_id, factors in CONFIDENCE_FACTORS.items():
    # Try nodes first
    if node_id in nodes:
        if add_confidence_factors(node_id, factors, nodes):
            print(f"  [+] {node_id}: Added confidence_factors")
            count += 1
    # Try extended_nodes
    elif node_id in extended:
        if add_confidence_factors(node_id, factors, extended):
            print(f"  [+] {node_id}: Added confidence_factors (extended)")
            count += 1
    else:
        print(f"  [?] {node_id}: Not found!")

print(f"\nTotal nodes updated: {count}")

# Save
data['nodes'] = nodes
data['extended_nodes'] = extended

with open(GRAPH_PATH, 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=100)

print("\nSaved. Run 'python scripts/graph_utils.py validate' to verify.")
