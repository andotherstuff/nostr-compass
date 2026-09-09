import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("selection_gate", ROOT / "scripts/check_selection_coverage.py")
assert SPEC and SPEC.loader
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SelectionCoverageTests(unittest.TestCase):
    def fixture(self):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        manifest_path, ledger_path, draft_path = root / "manifest.json", root / "ledger.json", root / "draft.md"
        manifest = {
            "schema_version": 2,
            "pass_id": "pass-001",
            "finalized": True,
            "expected_families": ["projects", "recap"],
            "families": {
                "projects": {"status": "complete", "candidate_ids": ["repo:a", "repo:noise"], "dispositions": {"repo:a": {"decision": "include", "reason": "active exact-window project"}, "repo:noise": {"decision": "skip", "reason": "outside source window"}}},
                "recap": {"status": "complete", "candidate_ids": ["event:1"], "dispositions": {"event:1": {"decision": "include", "reason": "signed roundup event"}}},
            },
        }
        manifest_path.write_text(json.dumps(manifest))
        draft_path.write_text("[Alpha](https://example.com/alpha) is useful.\n[Beta](https://example.com/beta) is useful.\n")
        candidate = lambda candidate_id, name, url: {
            "candidate_id": candidate_id,
            "name": name,
            "hard_gate": {field: True for field in gate.HARD_GATES},
            "scores": {axis: 2 for axis in gate.SCORE_AXES},
            "triage": "GREEN",
            "final_disposition": "include",
            "reason": "Material shipped Nostr behavior with direct primary evidence.",
            "primary_sources": [url],
            "draft_sources": [url],
        }
        ledger = {
            "schema_version": 1,
            "source_pass_id": "pass-001",
            "source_manifest_sha256": digest(manifest_path),
            "draft_sha256": digest(draft_path),
            "selection_policy": {"minimum_score": 8, "maximum_score": 10, "require_no_zero_axis": True, "fixed_item_cap": None, "qualified_items_must_publish": True},
            "hard_gate_fields": list(gate.HARD_GATES),
            "score_axes": list(gate.SCORE_AXES),
            "source_expansion": [
                {"source_id": "projects:repo:a", "candidate_ids": ["project:alpha"]},
                {"source_id": "recap:event:1", "candidate_ids": ["project:alpha", "project:beta"]},
            ],
            "candidates": [candidate("project:alpha", "Alpha", "https://example.com/alpha"), candidate("project:beta", "Beta", "https://example.com/beta")],
            "final": True,
        }
        ledger_path.write_text(json.dumps(ledger))
        return temp, manifest_path, ledger_path, draft_path, ledger

    def test_complete_aggregate_expansion_passes(self):
        temp, manifest, ledger, draft, _ = self.fixture()
        self.addCleanup(temp.cleanup)
        errors, receipt = gate.validate(manifest, ledger, draft)
        self.assertEqual(errors, [])
        self.assertEqual(receipt["qualified_candidate_count"], 2)

    def test_missing_retained_source_fails(self):
        temp, manifest, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        ledger["source_expansion"].pop()
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest, ledger_path, draft)
        self.assertTrue(any("missing from triage" in error for error in errors))

    def test_qualified_green_candidate_cannot_be_dropped(self):
        temp, manifest, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        ledger["candidates"][0]["final_disposition"] = "skip"
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest, ledger_path, draft)
        self.assertTrue(any("was dropped" in error for error in errors))

    def test_low_signal_candidate_cannot_be_published(self):
        temp, manifest, ledger_path, draft, ledger = self.fixture()
        self.addCleanup(temp.cleanup)
        ledger["candidates"][0]["scores"]["novelty"] = 0
        ledger["candidates"][0]["triage"] = "MAYBE"
        ledger_path.write_text(json.dumps(ledger))
        errors, _ = gate.validate(manifest, ledger_path, draft)
        self.assertTrue(any("sub-threshold" in error for error in errors))

    def test_changed_draft_invalidates_ledger(self):
        temp, manifest, ledger, draft, _ = self.fixture()
        self.addCleanup(temp.cleanup)
        draft.write_text(draft.read_text() + "changed\n")
        errors, _ = gate.validate(manifest, ledger, draft)
        self.assertTrue(any("exact draft" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
