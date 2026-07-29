import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).parents[1] / "scripts" / "check_topic_backlinks.py"


def load_module():
    spec = importlib.util.spec_from_file_location("check_topic_backlinks", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TopicBacklinkTests(unittest.TestCase):
    def test_accepts_existing_topic_sources_and_rendered_backlink_anchor(self):
        checker = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            topics = root / "topics"
            topics.mkdir()
            (topics / "nip-29.md").write_text(
                "**Primary sources:**\n- [Spec](https://example.com)\n\n"
                "**Mentioned in:**\n- [Issue](/en/newsletters/2026-07-29-newsletter/#tagged-releases)\n"
            )
            newsletter = root / "2026-07-29-newsletter.md"
            newsletter.write_text("[NIP-29](/en/topics/nip-29/)\n")
            rendered = root / "index.html"
            rendered.write_text('<h2 id="tagged-releases">Tagged Releases</h2>')

            findings, stats = checker.review(newsletter, topics, rendered)

            self.assertEqual([], findings)
            self.assertEqual(1, stats["topics"])
            self.assertEqual(1, stats["backlinks"])

    def test_accepts_unquoted_minified_rendered_backlink_anchor(self):
        checker = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            topics = root / "topics"
            topics.mkdir()
            (topics / "nip-29.md").write_text(
                "**Primary sources:**\n- [Spec](https://example.com)\n\n"
                "**Mentioned in:**\n- [Issue](/en/newsletters/2026-07-29-newsletter/#tagged-releases)\n"
            )
            newsletter = root / "2026-07-29-newsletter.md"
            newsletter.write_text("[NIP-29](/en/topics/nip-29/)\n")
            rendered = root / "index.html"
            rendered.write_text("<h2 id=tagged-releases>Tagged Releases</h2>")

            findings, stats = checker.review(newsletter, topics, rendered)

            self.assertEqual([], findings)
            self.assertEqual(1, stats["topics"])
            self.assertEqual(1, stats["backlinks"])

    def test_rejects_stale_backlink_fragment(self):
        checker = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            topics = root / "topics"
            topics.mkdir()
            (topics / "nip-29.md").write_text(
                "**Primary sources:**\n- [Spec](https://example.com)\n\n"
                "- [Issue](/en/newsletters/2026-07-29-newsletter/#shipping-this-week)\n"
            )
            newsletter = root / "2026-07-29-newsletter.md"
            newsletter.write_text("[NIP-29](/en/topics/nip-29/)\n")
            rendered = root / "index.html"
            rendered.write_text('<h2 id="tagged-releases">Tagged Releases</h2>')

            findings, _ = checker.review(newsletter, topics, rendered)

            self.assertTrue(any("shipping-this-week" in finding for finding in findings))


if __name__ == "__main__":
    unittest.main()
