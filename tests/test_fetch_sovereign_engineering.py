import importlib.util
import json
from pathlib import Path
import unittest

SCRIPT = Path(__file__).parents[1] / "scripts" / "fetch_sovereign_engineering.py"


def load_module():
    spec = importlib.util.spec_from_file_location("sec_fetch", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


INDEX_HTML = """
<a href='/projects/SEC-07'><h3>SEC-07</h3></a>
<a href='/#apply'><h3>SEC-08</h3></a>
"""

COHORT_HTML = """
<h2>Fanal</h2><p>A small FIPS node.</p>
<a href='https://github.com/oleksky/fanal'>GitHub</a>
<h2>LoRa Range Test</h2>
<a href='https://gitworkshop.dev/example/range-test'>Repository</a>
"""


class SovereignEngineeringFetchTests(unittest.TestCase):
    def test_index_finds_current_and_latest_archived_cohort(self):
        mod = load_module()
        result = mod.parse_projects_index(INDEX_HTML)
        self.assertEqual(result["current_cohort"], "SEC-08")
        self.assertEqual(result["latest_archive"], "SEC-07")
        self.assertIn("/projects/SEC-07", result["archive_paths"])

    def test_cohort_parser_groups_repository_links_by_project(self):
        mod = load_module()
        projects = mod.parse_cohort_projects(COHORT_HTML)
        self.assertEqual([p["name"] for p in projects], ["Fanal", "LoRa Range Test"])
        self.assertEqual(projects[0]["repositories"], ["https://github.com/oleksky/fanal"])
        self.assertEqual(projects[1]["repositories"], ["https://gitworkshop.dev/example/range-test"])

    def test_nostr_events_are_deduplicated_and_project_tags_extracted(self):
        mod = load_module()
        event = {
            "id": "abc",
            "created_at": 10,
            "content": "FIPS update #SEC08 #SovEng #FIPS",
            "tags": [["t", "SEC08"], ["t", "SovEng"], ["t", "fips"], ["t", "FIPS"], ["t", "DemoDay"]],
        }
        result = mod.normalize_nostr_events([event, event], "SEC-08")
        self.assertEqual(len(result["events"]), 1)
        self.assertEqual(result["project_tags"], ["FIPS"])


if __name__ == "__main__":
    unittest.main()
