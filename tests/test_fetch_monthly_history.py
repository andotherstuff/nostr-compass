import importlib.util
import json
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
    def test_versioned_registry_covers_every_historical_research_domain(self):
        fetcher = load_module()
        config_path = Path(__file__).parents[1] / "data" / "monthly_history_sources.json"
        config = json.loads(config_path.read_text())
        fetcher.validate_config(config)
        categories = {source["category"] for source in config["repositories"]}
        self.assertEqual(set(config["required_categories"]), categories)
        self.assertGreaterEqual(config["registry_version"], 2)

    def test_registry_validation_rejects_missing_domain_and_duplicate_repo(self):
        fetcher = load_module()
        config = {
            "registry_version": 2,
            "required_categories": ["protocol_specs", "clients_products"],
            "repositories": [
                {"repo": "org/repo", "category": "protocol_specs", "focus": "spec"},
                {"repo": "org/repo", "category": "protocol_specs", "focus": "duplicate"},
            ],
        }
        with self.assertRaisesRegex(ValueError, "duplicate repositories"):
            fetcher.validate_config(config)

    def test_registry_validation_rejects_missing_and_unknown_categories(self):
        fetcher = load_module()
        missing = {
            "registry_version": 2,
            "required_categories": ["protocol_specs", "clients_products"],
            "repositories": [
                {"repo": "org/spec", "category": "protocol_specs", "focus": "spec"},
            ],
        }
        with self.assertRaisesRegex(ValueError, "category mismatch"):
            fetcher.validate_config(missing)
        unknown = {
            "registry_version": 2,
            "required_categories": ["protocol_specs"],
            "repositories": [
                {"repo": "org/spec", "category": "protocol_specs", "focus": "spec"},
                {"repo": "org/other", "category": "unknown", "focus": "other"},
            ],
        }
        with self.assertRaisesRegex(ValueError, "category mismatch"):
            fetcher.validate_config(unknown)

    def test_collect_preserves_registry_version_and_category_coverage(self):
        fetcher = load_module()
        config = {
            "registry_version": 2,
            "required_categories": ["protocol_specs", "clients_products"],
            "repositories": [
                {"repo": "org/spec", "category": "protocol_specs", "focus": "spec"},
                {"repo": "org/client", "category": "clients_products", "focus": "client"},
            ],
        }
        with patch.object(fetcher, "gh_commits", return_value=[]):
            report = fetcher.collect(config, 8, 2021, 2021)
        self.assertEqual(2, report["registry_version"])
        self.assertEqual(
            {"protocol_specs": ["org/spec"], "clients_products": ["org/client"]},
            report["category_coverage"],
        )

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
