#!/usr/bin/env python3
"""
Knowledge Graph Utilities for The Divine Bricolage

Provides functions for querying, validating, and visualizing the knowledge graph.

Usage:
    python graph_utils.py stats          # Show graph statistics
    python graph_utils.py validate       # Check graph integrity
    python graph_utils.py list [domain]  # List nodes (optionally by domain)
    python graph_utils.py connections    # Show connection network
    python graph_utils.py untraced       # List claims needing source tracing
    python graph_utils.py export-md      # Export to markdown for GitHub viewing
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
GRAPH_PATH = REPO_ROOT / "docs" / "knowledge_graph.yaml"
MARKDOWN_PATH = REPO_ROOT / "docs" / "knowledge_graph.md"


def load_graph() -> dict:
    """Load the knowledge graph from YAML."""
    with open(GRAPH_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def save_graph(graph: dict) -> None:
    """Save the knowledge graph to YAML."""
    with open(GRAPH_PATH, 'w', encoding='utf-8') as f:
        yaml.dump(graph, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def get_stats(graph: dict) -> dict:
    """Calculate graph statistics."""
    nodes = graph.get('nodes', {}) or {}
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


def validate_graph(graph: dict) -> list:
    """Validate graph integrity, return list of issues."""
    issues = []
    nodes = graph.get('nodes', {}) or {}
    metadata = graph.get('metadata', {})
    
    valid_domains = {d['id'] for d in metadata.get('domains', [])}
    valid_statuses = set(metadata.get('statuses', {}).keys())
    valid_relationships = set(metadata.get('relationship_types', {}).keys())
    
    for node_id, node in nodes.items():
        # Check domain
        if node.get('domain') not in valid_domains:
            issues.append(f"{node_id}: Invalid domain '{node.get('domain')}'")
        
        # Check status
        if node.get('status') not in valid_statuses:
            issues.append(f"{node_id}: Invalid status '{node.get('status')}'")
        
        # Check source chain exists
        if not node.get('source_chain'):
            issues.append(f"{node_id}: Missing source chain")
        
        # Check connections reference valid nodes
        for conn in node.get('connections', []):
            target = conn.get('target')
            if target and target not in nodes:
                issues.append(f"{node_id}: Connection to non-existent node '{target}'")
            if conn.get('type') not in valid_relationships:
                issues.append(f"{node_id}: Invalid relationship type '{conn.get('type')}'")
    
    # Check for orphan nodes (no connections)
    connected_nodes = set()
    for node_id, node in nodes.items():
        for conn in node.get('connections', []):
            connected_nodes.add(node_id)
            connected_nodes.add(conn.get('target'))
    
    orphans = set(nodes.keys()) - connected_nodes
    if orphans and len(nodes) > 1:
        for orphan in orphans:
            issues.append(f"{orphan}: Orphan node (no connections)")
    
    return issues


def list_nodes(graph: dict, domain: str = None) -> list:
    """List all nodes, optionally filtered by domain."""
    nodes = graph.get('nodes', {}) or {}
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
    nodes = graph.get('nodes', {}) or {}
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
    parser.add_argument('command', choices=['stats', 'validate', 'list', 'connections', 'untraced', 'export-md'])
    parser.add_argument('--domain', '-d', help="Filter by domain ID")
    parser.add_argument('--json', '-j', action='store_true', help="Output as JSON")
    
    args = parser.parse_args()
    
    graph = load_graph()
    
    if args.command == 'stats':
        stats = get_stats(graph)
        if args.json:
            print(json.dumps(stats, indent=2))
        else:
            print("\n=== Knowledge Graph Statistics ===\n")
            print(f"Total Nodes:       {stats['total_nodes']}")
            print(f"Total Connections: {stats['total_connections']}")
            print(f"Untraced Claims:   {stats['untraced_claims']}")
            print("\nBy Status:")
            for status, count in stats['by_status'].items():
                print(f"  {status}: {count}")
            print("\nBy Domain:")
            for domain, count in stats['by_domain'].items():
                print(f"  {domain}: {count}")
    
    elif args.command == 'validate':
        issues = validate_graph(graph)
        if issues:
            print(f"\n=== Found {len(issues)} issues ===\n")
            for issue in issues:
                print(f"  ⚠ {issue}")
        else:
            print("\n✓ Graph validation passed - no issues found\n")
    
    elif args.command == 'list':
        nodes = list_nodes(graph, args.domain)
        if args.json:
            print(json.dumps(nodes, indent=2))
        else:
            print(f"\n=== Nodes ({len(nodes)}) ===\n")
            for node in nodes:
                print(f"  [{node['id']}] {node['title']} ({node['status']}, {node['connections']} connections)")
    
    elif args.command == 'untraced':
        untraced = graph.get('untraced', []) or []
        if args.json:
            print(json.dumps(untraced, indent=2))
        else:
            print(f"\n=== Untraced Claims ({len(untraced)}) ===\n")
            for claim in untraced:
                print(f"  • {claim.get('claim', 'Unknown')}")
                print(f"    Found in: {claim.get('found_in', 'Unknown')}")
                print(f"    Needed: {claim.get('needed', 'Original source')}")
                print()
    
    elif args.command == 'export-md':
        markdown = export_to_markdown(graph)
        with open(MARKDOWN_PATH, 'w', encoding='utf-8') as f:
            f.write(markdown)
        print(f"✓ Exported to {MARKDOWN_PATH}")
    
    elif args.command == 'connections':
        nodes = graph.get('nodes', {}) or {}
        print("\n=== Connection Network ===\n")
        for node_id, node in nodes.items():
            conns = node.get('connections', [])
            if conns:
                print(f"[{node_id}] {node.get('title', 'Untitled')}")
                for conn in conns:
                    print(f"  → {conn.get('type')} → [{conn.get('target')}]")
                print()


if __name__ == '__main__':
    main()
