import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).parents[1] / "scripts" / "prepare_email_digest.py"
spec = importlib.util.spec_from_file_location("prepare_email_digest", SCRIPT)
digest_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(digest_module)


class EmailDigestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.newsletter = self.root / "2026-10-07-newsletter.md"
        self.newsletter.write_text("---\ntitle: 'Nostr Compass #43'\ndate: 2026-10-07\ntype: newsletters\n---\n## Top Stories\n\n### Relay recovery\n\nFull technical evidence.\n\n## NIP Deep Dive\n\nComplete explanation and event example.\n")
        self.original = self.newsletter.read_bytes()
        self.digest = self.root / "email_digest_2026-10-07.md"
        self.html = self.root / "index.html"
        self.html.write_text('<h1>Nostr Compass #43</h1><h3 id=relay-recovery>Relay recovery</h3>')
        self.write_digest("[Relay recovery](#relay-recovery) improves reconnect behavior. [Learn the protocol](/en/topics/nip-05/).")

    def write_digest(self, body, source_hash=None):
        self.digest.write_text(f"---\ntype: email-digest\nissue: 43\nedition: 2026-10-07\nnewsletter_sha256: {source_hash or digest_module.sha256(self.original)}\n---\n{body}\n")

    def prepare(self):
        return digest_module.prepare(self.newsletter, self.digest, self.html)

    def test_email_preparation_preserves_full_source_bytes(self):
        email, receipt = self.prepare()
        self.assertIn("https://nostrcompass.org/en/newsletters/2026-10-07-newsletter/#relay-recovery", email)
        self.assertIn("https://nostrcompass.org/en/topics/nip-05/", email)
        self.assertEqual(self.original, self.newsletter.read_bytes())
        self.assertEqual(receipt["newsletter_sha256"], digest_module.sha256(self.original))
        self.assertFalse(receipt["sent"])
        self.assertTrue(receipt["editorial_review_required"])

    def test_source_edit_invalidates_digest(self):
        self.newsletter.write_bytes(self.original + b"\nA late update.\n")
        with self.assertRaisesRegex(ValueError, "stale"):
            self.prepare()

    def test_missing_actual_rendered_anchor_is_rejected(self):
        self.write_digest("[Missing detail](#not-rendered).")
        with self.assertRaisesRegex(ValueError, "absent"):
            self.prepare()

    def test_article_url_variants_cannot_bypass_anchor_validation(self):
        urls = ["/en/newsletters/2026-10-07-newsletter", "https://NostrCompass.org/en/newsletters/2026-10-07-newsletter/", "https://www.nostrcompass.org/en/newsletters/2026-10-07-newsletter/index.html"]
        for url in urls:
            with self.subTest(url=url):
                self.write_digest(f"[Read the section]({url}#missing). [Full issue](#relay-recovery).")
                with self.assertRaisesRegex(ValueError, "absent"):
                    self.prepare()
                self.write_digest(f"[Read the section]({url}#relay-recovery).")
                _, receipt = self.prepare()
                self.assertEqual(len(receipt["article_links"]), 1)

    def test_wrong_issue_or_html_cannot_be_used(self):
        self.digest.write_text(self.digest.read_text().replace("issue: 43", "issue: 44"))
        with self.assertRaisesRegex(ValueError, "differs"):
            self.prepare()
        self.write_digest("[Read the full issue](#relay-recovery).")
        self.html.write_text("<h1>Nostr Compass #44</h1><h3 id=relay-recovery>Detail</h3>")
        with self.assertRaisesRegex(ValueError, "matching newsletter"):
            self.prepare()

    def test_link_only_to_unrelated_issue_is_not_enough(self):
        self.write_digest("[Old issue](/en/newsletters/2026-09-30-newsletter/).")
        with self.assertRaisesRegex(ValueError, "matching full edition"):
            self.prepare()

    def test_word_budget_counts_link_labels_not_url_length(self):
        self.write_digest("[Read the full issue](#relay-recovery) now.")
        _, receipt = self.prepare()
        self.assertEqual(receipt["words"], 5)
        self.write_digest("[Read the issue](#relay-recovery). " + "word " * 1200)
        with self.assertRaisesRegex(ValueError, "at most"):
            self.prepare()

    def test_relative_and_reference_links_cannot_escape_checks(self):
        for bad in ["[Bad](../topics/nip-05/)", "[Bad][ref]\n\n[ref]: /en/topics/nip-05/", "[Bad](#relay-recovery(nested))", "[Bad](https://example.org/Foo_(bar))"]:
            with self.subTest(bad=bad):
                self.write_digest("[Full issue](#relay-recovery). " + bad)
                with self.assertRaises(ValueError):
                    self.prepare()

    def test_unsupported_email_content_is_rejected(self):
        for bad in ["<a href='/en/'>HTML</a>", "![Image](https://example.org/image.png)", "[Insecure](http://example.org/)", "```code```", "~~~code~~~", "\n    indented code", "\n\tindented code"]:
            with self.subTest(bad=bad):
                self.write_digest("[Full issue](#relay-recovery). " + bad)
                with self.assertRaises(ValueError):
                    self.prepare()

    def test_malformed_links_cannot_swallow_words_or_other_links(self):
        for bad in ["[Full](#relay-recovery " + "word " * 1500 + ")", "[Full](#relay-recovery\nmissing closer then (later)", "[Full](#relay-recovery text [Bad](http://example.org/))", '[Full](#relay-recovery "unsupported title")']:
            with self.subTest(bad=bad[:80]):
                self.write_digest("[Valid full issue](#relay-recovery). " + bad)
                with self.assertRaises(ValueError):
                    self.prepare()

    def test_web_urls_must_use_checked_inline_links(self):
        for bare in ["http://example.org/", "https://example.org/", "www.example.org"]:
            with self.subTest(bare=bare):
                self.write_digest("[Full issue](#relay-recovery). " + bare)
                with self.assertRaisesRegex(ValueError, "web URLs"):
                    self.prepare()

    def test_plain_comparison_is_not_mistaken_for_html(self):
        self.write_digest("[Full issue](#relay-recovery). A < B.")
        email, _ = self.prepare()
        self.assertIn("A < B.", email)

    def test_literal_links_do_not_count_as_full_edition_navigation(self):
        for literal in [r"\[Full](#relay-recovery)", "`[Full](#relay-recovery)`"]:
            with self.subTest(literal=literal):
                self.write_digest(literal)
                with self.assertRaises(ValueError):
                    self.prepare()

    def test_cli_receipt_matches_email_and_hardlinked_source_is_preserved(self):
        output = self.root / "email_ready.md"
        os.link(self.newsletter, output)
        receipt_path = self.root / "receipt.json"
        run = subprocess.run([sys.executable, str(SCRIPT), "--newsletter", str(self.newsletter), "--digest", str(self.digest), "--rendered-html", str(self.html), "--output", str(output), "--receipt", str(receipt_path)], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        receipt = json.loads(receipt_path.read_text())
        self.assertEqual(receipt["email_sha256"], digest_module.sha256(output.read_bytes()))
        self.assertEqual(self.original, self.newsletter.read_bytes())
        self.assertFalse(receipt["sent"])
        self.assertEqual(list(self.root.glob("*-newsletter.md")), [self.newsletter])

    def test_cli_cannot_overwrite_podcast_input_or_create_second_canonical_issue(self):
        for output in [self.newsletter, self.root / "2026-10-14-newsletter.md"]:
            run = subprocess.run([sys.executable, str(SCRIPT), "--newsletter", str(self.newsletter), "--digest", str(self.digest), "--rendered-html", str(self.html), "--output", str(output), "--receipt", str(self.root / "receipt.json")], capture_output=True, text=True)
            self.assertEqual(run.returncode, 1)
            self.assertEqual(self.newsletter.read_bytes(), self.original)
        self.assertEqual(list(self.root.glob("*-newsletter.md")), [self.newsletter])


if __name__ == "__main__":
    unittest.main()
