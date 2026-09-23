"""Exact-window Compass #41 coverage regression (no network access)."""
import json
import unittest
from pathlib import Path

from scripts.check_selection_coverage import validate

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'data/source_runs/source_run_2026-09-23_tuesday-2026-09-23-codex-1.json'
LEDGER = ROOT / 'data/newsletter_workspace/selection_coverage_2026-09-23.json'
DRAFT = ROOT / 'content/en/newsletters/2026-09-23-newsletter.md'


class Compass41Coverage(unittest.TestCase):
    def test_exact_window_current_selection_has_truthful_pass(self):
        errors, receipt = validate(MANIFEST, LEDGER, DRAFT)
        self.assertEqual(errors, [])
        self.assertEqual(receipt['verdict'], 'PASS')
        ledger = json.loads(LEDGER.read_text())
        self.assertEqual(len(ledger['selected']), 35)
        self.assertEqual(receipt['selected_candidate_count'], 35)
        self.assertGreaterEqual(receipt['skipped_candidate_count'], 109)


if __name__ == '__main__':
    unittest.main()
