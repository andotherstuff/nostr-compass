import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "fetch_spec_updates.py"


def load_module():
    spec = importlib.util.spec_from_file_location("fetch_spec_updates", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SpecUpdateTests(unittest.TestCase):
    def test_family_with_no_activity_is_preserved_as_quiet(self):
        fetcher = load_module()

        result = fetcher.family_result(
            {"id": "gamma", "name": "Gamma Markets", "repo": "GammaMarkets/market-spec"},
            commits=[],
            pulls=[],
            since="2026-07-21T00:00:00Z",
            until="2026-07-29T00:00:00Z",
        )

        self.assertEqual("quiet", result["status"])
        self.assertEqual([], result["commits"])
        self.assertEqual([], result["pull_requests"])

    def test_pull_request_updated_in_window_is_included(self):
        fetcher = load_module()
        pull = {
            "number": 94,
            "title": "Add microphone capture",
            "html_url": "https://github.com/napplet/naps/pull/94",
            "created_at": "2026-07-28T16:42:15Z",
            "updated_at": "2026-07-28T17:46:08Z",
            "merged_at": None,
            "state": "open",
        }

        result = fetcher.family_result(
            {"id": "nap", "name": "Napplet NAPs", "repo": "napplet/naps"},
            commits=[],
            pulls=[pull],
            since="2026-07-21T00:00:00Z",
            until="2026-07-29T00:00:00Z",
        )

        self.assertEqual("active", result["status"])
        self.assertEqual(94, result["pull_requests"][0]["number"])


if __name__ == "__main__":
    unittest.main()
