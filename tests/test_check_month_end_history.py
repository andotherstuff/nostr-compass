import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).parents[1] / "scripts" / "check_month_end_history.py"


def load_module():
    spec = importlib.util.spec_from_file_location("check_month_end_history", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def good_issue(date="2026-07-29"):
    intro = (
        "[July's repository record](https://github.com/nostr-protocol/nips/commits/master/) "
        "traces Nostr from early identity plumbing through relay growth, application expansion, "
        "payment interoperability, and mature multi-device state. " * 5
    )
    years = []
    for year in range(2021, 2027):
        years.append(
            f"### July {year}\n\n"
            f"By {year}, one milestone moved the protocol into a new stage through "
            f"[source A](https://github.com/example/project/commit/{year}aaa). "
            + "The implementation exposed a concrete interoperability boundary. " * 9
            + "\n\n"
            f"That shift became a foundation for the next cycle through "
            f"[source B](https://github.com/example/project/commit/{year}bbb). "
            + "Clients and relays could now build on a shared contract instead of private assumptions. " * 9
        )
    year_sections = "\n\n".join(years)
    return f"""---
date: {date}
---

## Six Years of Nostr Julys

{intro}

{year_sections}
"""


class MonthEndHistoryTest(unittest.TestCase):
    def test_last_weekly_issue_is_detected_independent_of_weekday(self):
        checker = load_module()
        self.assertTrue(checker.is_final_weekly_issue(checker.parse_issue_date("---\ndate: 2026-05-28\n---")))
        self.assertFalse(checker.is_final_weekly_issue(checker.parse_issue_date("---\ndate: 2026-05-21\n---")))

    def test_complete_progressive_history_passes(self):
        checker = load_module()
        self.assertEqual([], checker.review(good_issue()))

    def test_deep_dive_or_wrong_title_fails(self):
        checker = load_module()
        bad = good_issue().replace("## Six Years of Nostr Julys", "## NIP Deep Dive: July")
        findings = checker.review(bad)
        self.assertTrue(any("title" in item.lower() or "deep dive" in item.lower() for item in findings))

    def test_one_paragraph_per_year_laundry_list_fails(self):
        checker = load_module()
        bad = good_issue()
        for year in range(2021, 2027):
            marker = f"\n\nThat shift became a foundation for the next cycle through [source B](https://github.com/example/project/commit/{year}bbb). "
            start = bad.index(marker)
            end = bad.find("\n\n### ", start)
            if end == -1:
                end = len(bad)
            bad = bad[:start] + bad[end:]
        findings = checker.review(bad)
        self.assertTrue(any("two sourced prose paragraphs" in item for item in findings))

    def test_unsourced_or_non_progressive_paragraph_fails(self):
        checker = load_module()
        bad = good_issue().replace("[source B](https://github.com/example/project/commit/2024bbb)", "source B")
        findings = checker.review(bad)
        self.assertTrue(any("July 2024" in item and "source" in item.lower() for item in findings))

    def test_regular_week_does_not_require_history(self):
        checker = load_module()
        regular = "---\ndate: 2026-07-22\n---\n\n## Protocol work\n\nNo history this week."
        self.assertEqual([], checker.review(regular))


if __name__ == "__main__":
    unittest.main()
