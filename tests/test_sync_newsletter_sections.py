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

## Releases

Releases.

## Unreleased Changes

Development.

## NIP Updates and Protocol Spec Work

Protocol.
"""

    def test_newly_discovered_is_folded_into_top_stories_not_round_tripped(self):
        newsletter = self.canonical.replace(
            "## NIP Updates and Protocol Spec Work",
            "## Newly Discovered\n\n### Nail bridges Nostr and email\n\nCandidate.\n\n## NIP Updates and Protocol Spec Work",
        )
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            written = self.mod.synchronize(newsletter, output)
            path = output / "newly-discovered.md"

            self.assertNotIn(path, written)
            self.assertFalse(path.exists())

    def test_absent_newly_discovered_removes_stale_optional_artifact(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            stale = output / "newly-discovered.md"
            stale.write_text("stale\n")

            written = self.mod.synchronize(self.canonical, output)

            self.assertNotIn(stale, written)
            self.assertFalse(stale.exists())

    def test_modern_headings_and_writer_provenance_are_preserved(self):
        newsletter = self.canonical.replace("## Releases", "## Tagged Releases")
        newsletter = newsletter.replace("## Unreleased Changes", "## In Development")
        newsletter = newsletter.replace(
            "## NIP Updates and Protocol Spec Work", "## Protocol and Spec Work"
        )
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            lead = output / "lead-stories.md"
            lead.write_text("old\n\nwriter_model: claude-opus-5\n\nGATE: PASS\n")

            written = self.mod.synchronize(newsletter, output)

            self.assertIn(lead, written)
            self.assertIn("writer_model: claude-opus-5", lead.read_text())
            self.assertTrue((output / "tagged-releases.md").exists())
            self.assertTrue((output / "unreleased-changes.md").exists())
            self.assertTrue((output / "protocol-work.md").exists())


if __name__ == "__main__":
    unittest.main()
