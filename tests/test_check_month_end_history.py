import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).parents[1] / "scripts" / "check_month_end_history.py"


def load_module():
    spec = importlib.util.spec_from_file_location("check_month_end_history", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GOOD = """---
date: 2026-07-29
---

## Six Years of Nostr Julys

### July 2021

First claim with [source](https://github.com/example/repo/commit/1).

Second claim with [source](https://github.com/example/repo/commit/2).

### July 2022

First claim with [source](https://github.com/example/repo/commit/3).

Second claim with [source](https://github.com/example/repo/commit/4).

### July 2023

First claim with [source](https://github.com/example/repo/commit/5).

Second claim with [source](https://github.com/example/repo/commit/6).

### July 2024

First claim with [source](https://github.com/example/repo/commit/7).

Second claim with [source](https://github.com/example/repo/commit/8).

### July 2025

First claim with [source](https://github.com/example/repo/commit/9).

Second claim with [source](https://github.com/example/repo/commit/10).

### July 2026

First claim with [source](https://github.com/example/repo/commit/11).

Second claim with [source](https://github.com/example/repo/commit/12).
"""


class MonthEndHistoryTests(unittest.TestCase):
    def test_accepts_complete_month_end_history(self):
        checker = load_module()
        self.assertEqual([], checker.review(GOOD))

    def test_rejects_deep_dive_label(self):
        checker = load_module()
        findings = checker.review(GOOD.replace("## Six Years of Nostr Julys", "## NIP Deep Dive: Six Years of Nostr Julys"))
        self.assertTrue(any("NIP Deep Dive" in item for item in findings))

    def test_requires_two_linked_paragraphs_per_year(self):
        checker = load_module()
        broken = GOOD.replace("Second claim with [source](https://github.com/example/repo/commit/8).", "Second claim without a source.")
        findings = checker.review(broken)
        self.assertTrue(any("July 2024" in item and "primary-source" in item for item in findings))

    def test_regular_issue_is_not_subject_to_history_gate(self):
        checker = load_module()
        regular = GOOD.replace("2026-07-29", "2026-07-22").replace("## Six Years of Nostr Julys", "## NIP Deep Dive: NIP-11 and NIP-66")
        self.assertEqual([], checker.review(regular))

    def test_last_weekly_issue_is_month_end_even_when_not_wednesday(self):
        checker = load_module()
        thursday_issue = """---
date: 2026-05-28
---

## NIP Deep Dive: NIP-11 and NIP-66
"""
        findings = checker.review(thursday_issue)
        self.assertTrue(any("NIP Deep Dive" in finding for finding in findings))


if __name__ == "__main__":
    unittest.main()
