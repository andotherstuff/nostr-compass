import importlib.util
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "sync_newsletter_sections.py"


def load_module():
    spec = importlib.util.spec_from_file_location("sync_newsletter_sections", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SCRIPT}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class SyncNewsletterSectionsTests(unittest.TestCase):
    def setUp(self):
        self.mod = load_module()
        self.canonical = """## Top Stories

Top.

## Tagged Releases

Releases.

## In Development

Development.

## Protocol and Spec Work

Protocol.
"""

    def test_newly_discovered_round_trips_when_present(self):
        newsletter = self.canonical.replace(
            "## Protocol and Spec Work",
            "## Newly Discovered\n\n### Nail bridges Nostr and email\n\nCandidate.\n\n## Protocol and Spec Work",
        )
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            written = self.mod.synchronize(newsletter, output)
            path = output / "newly-discovered.md"

            self.assertIn(path, written)
            self.assertEqual(
                path.read_text(),
                "## Newly Discovered\n\n### Nail bridges Nostr and email\n\nCandidate.\n\nGATE: PENDING REVIEW\n",
            )

    def test_absent_newly_discovered_removes_stale_optional_artifact(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            stale = output / "newly-discovered.md"
            stale.write_text("stale\n")

            written = self.mod.synchronize(self.canonical, output)

            self.assertNotIn(stale, written)
            self.assertFalse(stale.exists())


if __name__ == "__main__":
    unittest.main()
