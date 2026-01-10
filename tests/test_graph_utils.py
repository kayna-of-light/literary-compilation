import sys
from copy import deepcopy
from pathlib import Path
from unittest import TestCase, main
from unittest.mock import patch
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "scripts"
sys.path.append(str(SCRIPT_DIR))
import graph_utils as gu  # noqa: E402


def load_metadata():
    with open(ROOT / "graph" / "knowledge_graph.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["metadata"]


def build_chain_graph(include_connections=True, include_synthesis=False):
    metadata = load_metadata()
    nodes = {
        "CROSS-001": {
            "title": "Foundational Anchor",
            "domain": "CROSS",
            "node_type": "foundational",
            "status": "preliminary",
            "definition": "Anchor premise for chain testing.",
            "source_chain": [{"type": "T", "ref": "tests/foundational.md"}],
            "trace_status": "complete",
            "connections": [],
        },
        "CROSS-002": {
            "title": "Concept Node",
            "domain": "CROSS",
            "node_type": "concept",
            "status": "preliminary",
            "definition": "Concept derived from anchor.",
            "source_chain": [{"type": "T", "ref": "tests/concept.md"}],
            "trace_status": "complete",
            "connections": [],
        },
        "CROSS-003": {
            "title": "Hypothesis Node",
            "domain": "CROSS",
            "node_type": "hypothesis",
            "status": "preliminary",
            "definition": "Hypothesis derived from concept.",
            "source_chain": [{"type": "T", "ref": "tests/hypothesis.md"}],
            "trace_status": "complete",
            "connections": [],
        },
        "CROSS-004": {
            "title": "Evidence Node",
            "domain": "CROSS",
            "node_type": "evidence",
            "status": "validated",
            "definition": "Empirical support for hypothesis.",
            "source_chain": [{"type": "E", "ref": "Study/Case"}],
            "trace_status": "complete",
            "confidence_factors": {
                "source_type": "external",
                "methodology": "observational",
                "sample_size": "small_10-99",
                "replication": "single_study",
                "peer_review": "peer_reviewed_journal",
                "source_chain_quality": "primary_verified",
            },
            "connections": [],
        },
    }

    if include_synthesis:
        nodes["CROSS-005"] = {
            "title": "Synthesis Node",
            "domain": "CROSS",
            "node_type": "synthesis",
            "status": "preliminary",
            "definition": "Synthesis integrating concepts.",
            "source_chain": [{"type": "T", "ref": "tests/synthesis.md"}],
            "trace_status": "complete",
            "connections": [],
        }

    if include_connections:
        nodes["CROSS-001"]["connections"].append(
            {"target": "CROSS-002", "type": "develops", "note": "Anchors concept"}
        )
        nodes["CROSS-002"]["connections"].extend(
            [
                {"target": "CROSS-001", "type": "developed_by", "note": "Derived from anchor"},
                {"target": "CROSS-003", "type": "develops", "note": "Generates hypothesis"},
            ]
        )
        nodes["CROSS-003"]["connections"].extend(
            [
                {"target": "CROSS-002", "type": "developed_by", "note": "Derived from concept"},
                {"target": "CROSS-004", "type": "supported_by", "note": "Supported by evidence"},
            ]
        )
        nodes["CROSS-004"]["connections"].append(
            {"target": "CROSS-003", "type": "supports", "note": "Supports hypothesis"}
        )
        if include_synthesis:
            nodes["CROSS-002"]["connections"].append(
                {"target": "CROSS-005", "type": "integrates_into", "note": "Concept feeds synthesis"}
            )
            nodes["CROSS-005"]["connections"].append(
                {"target": "CROSS-002", "type": "integrated_from", "note": "Pulls from concept"}
            )

    return {"metadata": metadata, "nodes": nodes, "extended_nodes": {}}


class GraphUtilsCrudTests(TestCase):
    def setUp(self):
        self.base_graph = build_chain_graph()
        self.saved_graphs = []
        self.save_patch = patch("graph_utils.save_graph", side_effect=lambda g: self.saved_graphs.append(deepcopy(g)))
        self.save_patch.start()

    def tearDown(self):
        self.save_patch.stop()

    def test_add_node_autogenerates_id(self):
        graph = deepcopy(self.base_graph)
        payload = {
            "domain": "CROSS",
            "node_type": "concept",
            "status": "preliminary",
            "title": "Auto-ID Concept",
            "definition": "New concept node",
            "source_chain": [{"type": "T", "ref": "tests/new-concept.md"}],
        }
        result = gu.add_node(graph, payload, section="nodes")
        self.assertTrue(result["success"])
        self.assertEqual(result["node_id"], "CROSS-005")
        saved = self.saved_graphs[-1]
        self.assertIn("CROSS-005", saved["nodes"])

    def test_add_node_invalid_domain(self):
        graph = deepcopy(self.base_graph)
        payload = {
            "domain": "INVALID",
            "node_type": "concept",
            "status": "preliminary",
            "title": "Broken",
            "definition": "Should fail",
            "source_chain": [{"type": "T", "ref": "tests/broken.md"}],
        }
        result = gu.add_node(graph, payload, section="nodes")
        self.assertFalse(result["success"])
        self.assertTrue(any("Invalid or missing domain" in err for err in result.get("errors", [])))

    def test_add_node_missing_required_fields(self):
        graph = deepcopy(self.base_graph)
        payload = {"domain": "CROSS", "node_type": "concept", "status": "preliminary"}
        result = gu.add_node(graph, payload, section="nodes")
        self.assertFalse(result["success"])
        self.assertTrue(any("Missing required fields" in err for err in result.get("errors", [])))

    def test_update_node_merges_and_updates(self):
        graph = deepcopy(self.base_graph)
        before = graph["nodes"]["CROSS-002"].get("updated")
        result = gu.update_node(graph, "CROSS-002", {"title": "Updated Concept"})
        self.assertTrue(result["success"])
        saved = self.saved_graphs[-1]
        self.assertEqual(saved["nodes"]["CROSS-002"]["title"], "Updated Concept")
        self.assertNotEqual(saved["nodes"]["CROSS-002"].get("updated"), before)

    def test_update_node_rejects_domain_change(self):
        graph = deepcopy(self.base_graph)
        result = gu.update_node(graph, "CROSS-002", {"domain": "BIBL"})
        self.assertFalse(result["success"])
        self.assertTrue(any("Domain change not allowed" in err for err in result.get("errors", [])))

    def test_delete_node_prunes_references(self):
        graph = deepcopy(self.base_graph)
        result = gu.delete_node(graph, "CROSS-004", prune=True)
        self.assertTrue(result["success"])
        saved = self.saved_graphs[-1]
        self.assertNotIn("CROSS-004", saved["nodes"])
        hypo_conns = saved["nodes"]["CROSS-003"].get("connections", [])
        self.assertFalse(any(conn.get("target") == "CROSS-004" for conn in hypo_conns))

    def test_delete_node_without_prune_fails_validation(self):
        graph = deepcopy(self.base_graph)
        result = gu.delete_node(graph, "CROSS-004", prune=False)
        self.assertFalse(result["success"])
        self.assertTrue(any("Connection to non-existent node" in err for err in result.get("errors", [])))

    def test_get_node_success_and_section(self):
        result = gu.get_node(self.base_graph, "CROSS-001")
        self.assertTrue(result["success"])
        self.assertEqual(result["section"], "nodes")
        self.assertEqual(result["node"]["title"], "Foundational Anchor")

    def test_get_node_missing(self):
        result = gu.get_node(self.base_graph, "CROSS-999")
        self.assertFalse(result["success"])
        self.assertTrue(any("Node not found" in err for err in result.get("errors", [])))

    def test_apply_graph_update_reports_validation_failure(self):
        graph = deepcopy(self.base_graph)
        with patch(
            "graph_utils.validate_graph",
            return_value={"passed": False, "issues": ["boom"], "warnings": [], "summary": {}},
        ):
            result = gu.apply_graph_update(graph)
            self.assertFalse(result["success"])
            self.assertIn("boom", result["errors"])

    def test_add_connection_with_auto_inverse(self):
        graph = build_chain_graph(include_connections=False)
        res = gu.add_connection(graph, "CROSS-001", "CROSS-002", "develops", note="Anchors concept")
        self.assertTrue(res["success"])
        self.assertTrue(any(c["type"] == "develops" for c in graph["nodes"]["CROSS-001"]["connections"]))
        self.assertTrue(
            any(c["type"] == "developed_by" and c["target"] == "CROSS-001" for c in graph["nodes"]["CROSS-002"].get("connections", []))
        )

    def test_add_connection_invalid_type(self):
        graph = build_chain_graph(include_connections=False)
        res = gu.add_connection(graph, "CROSS-001", "CROSS-004", "supports")
        self.assertFalse(res["success"])
        self.assertTrue(any("not allowed" in msg for msg in res.get("messages", [])))

    def test_document_processing_flow_happy_path(self):
        graph = {"metadata": load_metadata(), "nodes": {}, "extended_nodes": {}}
        foundational_payload = {
            "domain": "CROSS",
            "node_type": "foundational",
            "status": "preliminary",
            "title": "Doc Flow Foundational",
            "definition": "Anchor for pipeline test.",
            "source_chain": [{"type": "T", "ref": "docs/foundational.md"}],
        }
        concept_payload = {
            "domain": "CROSS",
            "node_type": "concept",
            "status": "preliminary",
            "title": "Doc Flow Concept",
            "definition": "Concept for pipeline test.",
            "source_chain": [{"type": "T", "ref": "docs/concept.md"}],
            "connections": [],
        }
        hypothesis_payload = {
            "domain": "CROSS",
            "node_type": "hypothesis",
            "status": "preliminary",
            "title": "Doc Flow Hypothesis",
            "definition": "Hypothesis under test.",
            "source_chain": [{"type": "T", "ref": "docs/hypothesis.md"}],
            "connections": [],
        }
        evidence_payload = {
            "domain": "CROSS",
            "node_type": "evidence",
            "status": "validated",
            "title": "Doc Flow Evidence",
            "definition": "Evidence supporting hypothesis.",
            "source_chain": [{"type": "E", "ref": "docs/evidence.md"}],
            "trace_status": "complete",
            "confidence_factors": {
                "source_type": "external",
                "methodology": "observational",
                "sample_size": "small_10-99",
                "replication": "single_study",
                "peer_review": "peer_reviewed_journal",
                "source_chain_quality": "primary_verified",
            },
            "connections": [],
        }

        self.saved_graphs.clear()
        add_result = gu.add_node(graph, foundational_payload)
        self.assertTrue(add_result["success"])
        graph = deepcopy(self.saved_graphs[-1])

        concept_payload["connections"].append(
            {"target": add_result["node_id"], "type": "developed_by", "note": "Linked to real ID"}
        )
        concept_result = gu.add_node(graph, concept_payload)
        self.assertTrue(concept_result["success"])
        graph = deepcopy(self.saved_graphs[-1])

        hypothesis_payload["connections"].append(
            {"target": concept_result["node_id"], "type": "developed_by", "note": "Linked to concept"}
        )
        hypothesis_result = gu.add_node(graph, hypothesis_payload)
        self.assertTrue(hypothesis_result["success"])
        graph = deepcopy(self.saved_graphs[-1])

        evidence_payload["connections"].append(
            {"target": hypothesis_result["node_id"], "type": "supports", "note": "Linked to hypothesis"}
        )
        evidence_result = gu.add_node(graph, evidence_payload)
        self.assertTrue(evidence_result["success"])
        graph = deepcopy(self.saved_graphs[-1])

        validation = gu.validate_graph(graph)
        self.assertTrue(validation["passed"])
        self.assertFalse(validation["issues"])

    def test_synthesis_chain_validation(self):
        graph = build_chain_graph(include_connections=True, include_synthesis=True)
        result = gu.validate_graph(graph)
        self.assertTrue(result["passed"])
        self.assertFalse(result["issues"])
        syn_conns = graph["nodes"]["CROSS-005"].get("connections", [])
        self.assertTrue(any(c.get("type") == "integrated_from" for c in syn_conns))

    def test_update_node_adds_critic_and_confidence(self):
        graph = deepcopy(self.base_graph)
        critic_block = {
            "last_reviewed": "2026-01-10",
            "critiques": [
                {
                    "id": 1,
                    "type": "definition-issue",
                    "description": "Needs clarity",
                    "breaks_proof": False,
                    "status": "open",
                }
            ],
            "proof_breaking_open": 0,
            "detail_issues": 1,
        }
        confidence_block = {
            "source_type": "internal",
            "methodology": "observational",
            "sample_size": "small_10-99",
            "replication": "single_study",
            "methodological_transparency": "high",
            "source_data_quality": "curated_corpus",
            "critic_reviewed": "not_reviewed",
        }
        result = gu.update_node(
            graph,
            "CROSS-004",
            {"critic_notes": critic_block, "confidence_factors": confidence_block},
        )
        self.assertTrue(result["success"])
        saved = self.saved_graphs[-1]
        ev = saved["nodes"]["CROSS-004"]
        self.assertEqual(ev["critic_notes"]["detail_issues"], 1)
        self.assertEqual(ev["confidence_factors"]["methodological_transparency"], "high")

    def test_update_node_source_chain_rules(self):
        graph = deepcopy(self.base_graph)
        # Evidence can accept multiple sources
        res_ok = gu.update_node(
            graph,
            "CROSS-004",
            {"source_chain": [{"type": "E", "ref": "Study/Case"}, {"type": "P", "ref": "Primary"}]},
        )
        self.assertTrue(res_ok["success"])

        # Non-evidence must retain single [T] provenance
        res_fail = gu.update_node(
            graph,
            "CROSS-002",
            {"source_chain": [{"type": "T", "ref": "tests/concept.md"}, {"type": "S", "ref": "Secondary"}]},
        )
        self.assertFalse(res_fail["success"])
        self.assertTrue(any("Non-evidence" in err for err in res_fail.get("errors", [])))

    def test_validate_warns_missing_inverse(self):
        graph = build_chain_graph(include_connections=True)
        # Drop the inverse to trigger missing_inverse warning
        conns = graph["nodes"]["CROSS-003"]["connections"]
        graph["nodes"]["CROSS-003"]["connections"] = [c for c in conns if c.get("type") != "developed_by"]
        result = gu.validate_graph(graph)
        self.assertTrue(result["passed"])
        self.assertTrue(any("INCOMPLETE CHAIN" in w or "reverse" in w for w in result["warnings"]))

    def test_validate_errors_on_invalid_connection_type(self):
        graph = build_chain_graph(include_connections=False)
        graph["nodes"]["CROSS-001"]["connections"] = [
            {"target": "CROSS-002", "type": "supports", "note": "Bad type"}
        ]
        result = gu.validate_graph(graph)
        self.assertFalse(result["passed"])
        self.assertTrue(any("invalid connection type" in issue.lower() or "not allowed" in issue.lower() for issue in result["issues"]))

    def test_validate_warns_missing_confidence_factors(self):
        graph = build_chain_graph(include_connections=True)
        graph["nodes"]["CROSS-004"].pop("confidence_factors", None)
        result = gu.validate_graph(graph)
        self.assertTrue(result["passed"])
        self.assertTrue(any("confidence_factors" in w for w in result["warnings"]))

    def test_validate_errors_on_non_evidence_provenance(self):
        graph = build_chain_graph(include_connections=True)
        graph["nodes"]["CROSS-002"]["source_chain"] = [
            {"type": "T", "ref": "tests/concept.md"},
            {"type": "S", "ref": "Secondary"},
        ]
        result = gu.validate_graph(graph)
        self.assertFalse(result["passed"])
        self.assertTrue(any("Non-evidence" in issue for issue in result["issues"]))

    def test_validate_warns_orphan_nodes(self):
        graph = build_chain_graph(include_connections=False)
        result = gu.validate_graph(graph)
        self.assertTrue(result["passed"])
        self.assertTrue(any("Orphan node" in w for w in result["warnings"]))

    def test_validate_errors_on_circular_proof_chain(self):
        graph = build_chain_graph(include_connections=True)
        # Add two concepts with mutual requires to form a cycle
        graph["nodes"]["CROSS-007"] = {
            "title": "Concept Two",
            "domain": "CROSS",
            "node_type": "concept",
            "status": "preliminary",
            "definition": "Second concept",
            "source_chain": [{"type": "T", "ref": "tests/concept2.md"}],
            "trace_status": "complete",
            "connections": [],
        }
        graph["nodes"]["CROSS-002"]["connections"].append(
            {"target": "CROSS-007", "type": "requires", "note": "Mutual dep"}
        )
        graph["nodes"]["CROSS-007"]["connections"].append(
            {"target": "CROSS-002", "type": "requires", "note": "Mutual dep"}
        )
        result = gu.validate_graph(graph)
        self.assertFalse(result["passed"])
        self.assertTrue(any("CIRCULAR PROOF" in issue for issue in result["issues"]))

    def test_validate_errors_on_invalid_domain_status_type(self):
        graph = build_chain_graph(include_connections=False)
        node = graph["nodes"]["CROSS-002"]
        node["domain"] = "BAD"
        node["status"] = "BAD"
        node["node_type"] = "BAD"
        result = gu.validate_graph(graph)
        self.assertFalse(result["passed"])
        self.assertTrue(any("Invalid domain" in issue for issue in result["issues"]))
        self.assertTrue(any("Invalid status" in issue for issue in result["issues"]))
        self.assertTrue(any("Invalid node_type" in issue for issue in result["issues"]))

    def test_validate_errors_on_unknown_fields(self):
        graph = build_chain_graph(include_connections=False)
        graph["nodes"]["CROSS-002"]["alien"] = "nope"
        result = gu.validate_graph(graph)
        self.assertFalse(result["passed"])
        self.assertTrue(any("Unknown fields" in issue for issue in result["issues"]))

    def test_validate_warns_missing_connection_note(self):
        graph = build_chain_graph(include_connections=False)
        graph["nodes"]["CROSS-001"]["connections"] = [
            {"target": "CROSS-002", "type": "develops"}
        ]
        result = gu.validate_graph(graph)
        self.assertTrue(result["passed"])
        self.assertTrue(any("missing note" in w.lower() for w in result["warnings"]))

    def test_validate_cardinality_warnings(self):
        graph = build_chain_graph(include_connections=True)
        # Evidence supports four hypotheses to trigger epistemic_spread warning
        for idx in range(6, 10):
            hid = f"CROSS-0{idx}"
            graph["nodes"][hid] = {
                "title": f"Hypothesis {idx}",
                "domain": "CROSS",
                "node_type": "hypothesis",
                "status": "preliminary",
                "definition": "Extra hypo",
                "source_chain": [{"type": "T", "ref": f"tests/hypo-{idx}.md"}],
                "trace_status": "complete",
                "connections": [
                    {"target": "CROSS-002", "type": "developed_by", "note": "Derived from concept"},
                    {"target": "CROSS-004", "type": "supported_by", "note": "Shared evidence"},
                ],
            }
            graph["nodes"]["CROSS-004"]["connections"].append(
                {"target": hid, "type": "supports", "note": "Shared"}
            )
        result = gu.validate_graph(graph)
        self.assertTrue(result["passed"])
        self.assertTrue(any("epistemic_spread" in w for w in result["warnings"]))

    def test_validate_warns_missing_ref_in_source_chain(self):
        graph = build_chain_graph(include_connections=True)
        graph["nodes"]["CROSS-004"]["source_chain"] = [{"type": "E"}]
        result = gu.validate_graph(graph)
        self.assertTrue(result["passed"])
        self.assertTrue(any("missing 'ref'" in w.lower() for w in result["warnings"]))

    def test_validate_critic_count_mismatch(self):
        graph = build_chain_graph(include_connections=True)
        graph["nodes"]["CROSS-004"]["critic_notes"] = {
            "last_reviewed": "2026-01-10",
            "proof_breaking_open": 0,
            "detail_issues": 0,
            "critiques": [
                {
                    "id": 1,
                    "type": "definition-issue",
                    "description": "Needs clarity",
                    "breaks_proof": False,
                    "status": "open",
                }
            ],
        }
        result = gu.validate_graph(graph)
        self.assertTrue(result["passed"])
        self.assertTrue(any("count mismatch" in w for w in result["warnings"]))

    def test_delete_node_without_prune_multiple_inbounds(self):
        graph = build_chain_graph(include_connections=True)
        # Add another inbound to the evidence to ensure multiple dangling refs
        graph["nodes"]["CROSS-006"] = {
            "title": "Second Hypothesis",
            "domain": "CROSS",
            "node_type": "hypothesis",
            "status": "preliminary",
            "definition": "Extra hypothesis",
            "source_chain": [{"type": "T", "ref": "tests/second-hypo.md"}],
            "trace_status": "complete",
            "connections": [
                {"target": "CROSS-004", "type": "supported_by", "note": "Same evidence"},
                {"target": "CROSS-002", "type": "developed_by", "note": "From concept"},
            ],
        }
        res = gu.delete_node(graph, "CROSS-004", prune=False)
        self.assertFalse(res["success"])
        self.assertTrue(any("Connection to non-existent node" in err for err in res.get("errors", [])))

    def test_validate_insufficient_integration(self):
        graph = build_chain_graph(include_connections=True, include_synthesis=True)
        # Remove concept input to trigger insufficient_integration for synthesis
        graph["nodes"]["CROSS-005"]["connections"] = []
        result = gu.validate_graph(graph)
        self.assertTrue(result["passed"])
        self.assertTrue(any("insufficient_integration" in w for w in result["warnings"]))

    def test_validate_insufficient_evidence(self):
        graph = build_chain_graph(include_connections=True)
        # Remove evidence link so hypothesis has zero evidence
        graph["nodes"]["CROSS-004"]["connections"] = []
        graph["nodes"]["CROSS-003"]["connections"] = [
            {"target": "CROSS-002", "type": "developed_by", "note": "Derived from concept"}
        ]
        result = gu.validate_graph(graph)
        self.assertTrue(result["passed"])
        self.assertTrue(any("insufficient_evidence" in w for w in result["warnings"]))


if __name__ == "__main__":
    main()
