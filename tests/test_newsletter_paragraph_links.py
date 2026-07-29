import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_newsletter_paragraph_links.py"


def load_module():
    spec = importlib.util.spec_from_file_location("check_newsletter_paragraph_links", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ParagraphLinkTests(unittest.TestCase):
    def test_flags_prose_paragraph_with_only_internal_links(self):
        checker = load_module()
        markdown = """---\ntitle: Test\n---\n\n## News\n\nThis paragraph cites [NIP-29](/en/topics/nip-29/) but no repository.\n"""

        findings = checker.review(markdown)

        self.assertEqual(1, len(findings))
        self.assertIn("This paragraph cites", findings[0].text)

    def test_accepts_repository_release_or_pull_request_link(self):
        checker = load_module()
        markdown = """## News\n\n[Release](https://github.com/example/app/releases/tag/v1.0.0) shipped.\n\nThe fix is in [PR #4](https://github.com/example/app/pull/4).\n"""

        self.assertEqual([], checker.review(markdown))

    def test_accepts_self_hosted_repository_commit_link(self):
        checker = load_module()
        markdown = """## News

The fix is in a [self-hosted commit](https://git.example.org/team/app/commit/abc123).
"""

        self.assertEqual([], checker.review(markdown))

    def test_ignores_headings_lists_and_code_blocks(self):
        checker = load_module()
        markdown = """## News\n\n- status line without a repository\n\n```json\n{\"kind\": 1}\n```\n"""

        self.assertEqual([], checker.review(markdown))


if __name__ == "__main__":
    unittest.main()
