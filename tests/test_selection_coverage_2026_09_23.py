"""Exact-draft Compass #41 coverage regression (no network access)."""
import json
import unittest
from pathlib import Path

from scripts.check_selection_coverage import validate

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/source_runs/source_run_2026-09-23_wednesday-2026-09-23-codex-recovery-1.json"
LEDGER = ROOT / "data/newsletter_workspace/selection_coverage_wednesday_2026-09-23.json"
DRAFT = ROOT / "content/en/newsletters/2026-09-23-newsletter.md"


class Compass41Coverage(unittest.TestCase):
    def test_final_editorial_selection_binds_current_draft(self):
        errors, receipt = validate(MANIFEST, LEDGER, DRAFT)
        self.assertEqual(errors, [])
        self.assertEqual(receipt["verdict"], "PASS")
        ledger = json.loads(LEDGER.read_text())
        self.assertEqual(len(ledger["selected"]), 72)
        self.assertEqual(receipt["selected_candidate_count"], 72)
        self.assertEqual(receipt["editorial_candidate_count"], 230)
        self.assertEqual(receipt["skipped_candidate_count"], 158)
        final = ledger["source_reconciliation"]["final_cutoff"]
        self.assertEqual(final["merged_pr_count"], 6)
        self.assertEqual(final["signed_store_release_count"], 2)


if __name__ == "__main__":
    unittest.main()
