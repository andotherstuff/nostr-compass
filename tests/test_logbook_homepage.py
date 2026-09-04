from html.parser import HTMLParser
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).parents[1]
LANGUAGES = ("en", "es", "pt", "de", "fr", "it", "ja", "ko", "zh", "nl")
LOGBOOK_URL = "https://npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923.nsite.lol/#/login"


class LogbookSectionParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.section_depth = 0
        self.sections = 0
        self.links = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "section" and "home-logbook" in attributes.get("class", "").split():
            self.sections += 1
            self.section_depth = 1
        elif self.section_depth:
            self.section_depth += 1
            if tag == "a":
                self.links.append(attributes)

    def handle_endtag(self, tag):
        if self.section_depth:
            self.section_depth -= 1

    def handle_data(self, data):
        if self.section_depth and data.strip():
            self.text.append(data.strip())


class LogbookHomepageTests(unittest.TestCase):
    def test_logbook_is_linked_and_described_on_each_homepage(self):
        with tempfile.TemporaryDirectory() as destination:
            subprocess.run(
                ["hugo", "--destination", destination, "--quiet"],
                cwd=ROOT,
                check=True,
            )

            for language in LANGUAGES:
                with self.subTest(language=language):
                    parser = LogbookSectionParser()
                    parser.feed((Path(destination) / language / "index.html").read_text())

                    self.assertEqual(1, parser.sections)
                    self.assertEqual([LOGBOOK_URL], [link.get("href") for link in parser.links])
                    self.assertTrue(any("Logbook" in text for text in parser.text))
                    self.assertGreater(len(" ".join(parser.text)), len("Logbook"))
                    self.assertNotIn("target", parser.links[0])


if __name__ == "__main__":
    unittest.main()