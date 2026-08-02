import importlib.util
from datetime import date
from pathlib import Path
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).parents[1] / "scripts" / "fetch_monthly_history.py"


def load_module():
    spec = importlib.util.spec_from_file_location("fetch_monthly_history", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class FetchMonthlyHistoryTest(unittest.TestCase):
    def test_month_windows_cover_same_month_across_years(self):
        fetcher = load_module()
        windows = fetcher.month_windows(2, 2021, 2024)
        self.assertEqual((2021, "2021-02-01T00:00:00Z", "2021-03-01T00:00:00Z"), windows[0])
        self.assertEqual((2024, "2024-02-01T00:00:00Z", "2024-03-01T00:00:00Z"), windows[-1])

    def test_december_rolls_into_next_year(self):
        fetcher = load_module()
        self.assertEqual(
            [(2023, "2023-12-01T00:00:00Z", "2024-01-01T00:00:00Z")],
            fetcher.month_windows(12, 2023, 2023),
        )

    def test_normalize_pages_flattens_and_keeps_primary_fields(self):
        fetcher = load_module()
        pages = [[{
            "sha": "abc",
            "html_url": "https://github.com/org/repo/commit/abc",
            "commit": {
                "author": {"date": "2024-07-02T00:00:00Z", "name": "Dev"},
                "message": "Add relay support\n\nDetails",
            },
        }]]
        self.assertEqual(
            [{
                "sha": "abc",
                "date": "2024-07-02T00:00:00Z",
                "author": "Dev",
                "title": "Add relay support",
                "url": "https://github.com/org/repo/commit/abc",
            }],
            fetcher.normalize_pages(pages),
        )

    def test_gh_commits_uses_ndjson_for_older_gh_without_slurp(self):
        fetcher = load_module()
        row = {
            "sha": "abc",
            "html_url": "https://github.com/org/repo/commit/abc",
            "commit": {"author": {"date": "2024-07-02T00:00:00Z", "name": "Dev"}, "message": "Add relay support"},
        }
        completed = type("Completed", (), {"returncode": 0, "stdout": __import__("json").dumps(row) + "\n", "stderr": ""})()
        with patch.object(fetcher.subprocess, "run", return_value=completed) as run:
            commits = fetcher.gh_commits("org/repo", "2024-07-01T00:00:00Z", "2024-08-01T00:00:00Z")
        command = run.call_args.args[0]
        self.assertIn("--paginate", command)
        self.assertNotIn("--slurp", command)
        self.assertIn(".[] | @json", command)
        self.assertEqual("abc", commits[0]["sha"])


if __name__ == "__main__":
    unittest.main()
