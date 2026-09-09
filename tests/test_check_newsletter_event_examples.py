import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("event_gate", ROOT / "scripts/check_newsletter_event_examples.py")
assert SPEC and SPEC.loader
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)

REAL_EVENT = {
    "id": "cbf64aa95627f3722915e9aad29d905ddac9b09e7a8808a7594732d90deaa6bb",
    "pubkey": "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
    "created_at": 1788953511,
    "kind": 1,
    "tags": [["p", "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a", "wss://multiplexer.huszonegy.world/"], ["t", "archetype"], ["q", "30402:91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a:Archetype-Workbook-Companion-Meet-your-King-Warrioir-Magician-Lover-today-oejbwe", "wss://nos.lol/"], ["zap", "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a", "wss://multiplexer.huszonegy.world/", "0.9"], ["zap", "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d", "wss://relay.nostr.band/", "0.1"], ["client", "Amethyst"]],
    "content": "You can check, read and use this Workbook already! You can also support and get it for few sats and support us in this project.\n\nI hope it'll help you in your Archetype Journey :)\n\n#archetype\n\nnostr:naddr1qpgyzunrdpjhg7tsv5k4wmmjdd3x7mmt94pk7mtsv9hxjmmw94xk2et594uk7atj949kjmn894tkzunjd9hkju3df4skw6trd9skut2vdamx2u3dw3hkgcte94hk26nzwajszrnhwden5te0dehhxtnvdakz7q3qjypkmmqcaetrcpld4m27la946cch2hrk7qr8xjehsu5j5h3uxy9qxpqqqpmvyqnrm7n",
    "sig": "aa9592e7c773271b9e9f980c8a7e17fda2ffd5a4483a1789e5dd4c4a83018ac576c5202b21b33b08770dcabe023f93998a41f1a0be4bf00e36cdde611d07915e",
}


def check(markdown: str):
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "newsletter.md"
        path.write_text(markdown)
        return gate.check_file(str(path))


class EventGateTests(unittest.TestCase):
    def test_nip21_only_does_not_require_event(self):
        self.assertEqual(check("## NIP Deep Dive: Links\n\n### URI links (NIP-21)\n\nMechanics.\n"), [])

    def test_nip27_requires_full_event_with_nostr_content(self):
        problems = check("## NIP Deep Dive: References\n\n### References (NIP-27)\n\nMechanics.\n")
        self.assertTrue(any("NIP-27" in problem for problem in problems))

    def test_regular_deep_dive_cannot_avoid_event_with_generic_headings(self):
        problems = check("## NIP Deep Dive: Portable References\n\n### Mechanics\n\nA detailed treatment with no numbered heading.\n")
        self.assertTrue(any("requires at least one complete" in problem for problem in problems))

    def test_nip21_comparison_that_covers_nip27_is_not_nip21_only(self):
        problems = check("## NIP Deep Dive: Links (NIP-21)\n\nThis also covers NIP-27 references in signed content.\n")
        self.assertTrue(any("NIP-27" in problem for problem in problems))

    def test_real_nip27_event_passes_id_and_signature(self):
        markdown = "## NIP Deep Dive: References\n\n### References (NIP-27)\n\nRecovered from `wss://nos.lol`.\n\n```json\n" + json.dumps(REAL_EVENT) + "\n```\n"
        self.assertEqual(check(markdown), [])

    def test_changed_content_breaks_id_and_signature(self):
        changed = {**REAL_EVENT, "content": REAL_EVENT["content"] + " changed"}
        markdown = "## NIP Deep Dive: References\n\n### References (NIP-27)\n\n```json\n" + json.dumps(changed) + "\n```\n"
        self.assertTrue(any("canonical NIP-01" in problem for problem in check(markdown)))


if __name__ == "__main__":
    unittest.main()
