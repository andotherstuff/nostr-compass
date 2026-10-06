#!/usr/bin/env python3
"""Prepare an authored email digest without changing the full newsletter."""

from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import tempfile
from urllib.parse import unquote, urlsplit

import yaml

BASE_URL = "https://nostrcompass.org"
LINK = re.compile(r'(?<!\\)(!?\[[^\[\]\n]*\]\()([^\s()\[\]]+)([ \t]*\))')


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def document(raw: str) -> tuple[dict, str]:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", raw, re.S)
    if not match:
        raise ValueError("Expected YAML frontmatter and a Markdown body")
    metadata = yaml.safe_load(match[1])
    if not isinstance(metadata, dict):
        raise ValueError("Frontmatter must be a mapping")
    return metadata, match[2]


class RenderedEdition(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids: set[str] = set()
        self.h1: list[str] = []
        self.in_h1 = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"])
        if tag == "h1":
            self.in_h1 = True

    def handle_endtag(self, tag):
        if tag == "h1":
            self.in_h1 = False

    def handle_data(self, data):
        if self.in_h1:
            self.h1.append(data)


def prepare(newsletter: Path, digest: Path, rendered_html: Path) -> tuple[str, dict]:
    """Validate source binding and rendered anchors; return email and evidence."""
    source_bytes = newsletter.read_bytes()
    digest_bytes = digest.read_bytes()
    source, _ = document(source_bytes.decode("utf-8"))
    meta, body = document(digest_bytes.decode("utf-8"))
    filename = re.fullmatch(r"(\d{4}-\d{2}-\d{2})-newsletter\.md", newsletter.name)
    title = source.get("title", "")
    number = re.fullmatch(r"Nostr Compass #(\d+)", title) if isinstance(title, str) else None
    if not filename or not number or source.get("type") != "newsletters":
        raise ValueError("Newsletter input must be the canonical full newsletter (<date>-newsletter.md, Nostr Compass #N, type newsletters)")
    date = filename[1]
    issue = int(number[1])
    source_date = source.get("date")
    if str(source_date) != date:
        raise ValueError("Newsletter frontmatter date does not match its filename")
    if meta.get("type") != "email-digest" or meta.get("issue") != issue or str(meta.get("edition")) != date:
        raise ValueError("Digest type, issue or edition differs from the full newsletter")
    if meta.get("newsletter_sha256") != sha256(source_bytes):
        raise ValueError("Digest is stale: review it against the current full newsletter")
    if not body.strip():
        raise ValueError("Digest body is empty")
    if "`" in body or "~~~" in body or re.search(r"(?m)^(?: {4}|\t)[ \t]*\S", body) or re.search(r"<[A-Za-z/!]", body):
        raise ValueError("Email digest uses prose and Markdown links, without code blocks or HTML")
    page = RenderedEdition()
    html_bytes = rendered_html.read_bytes()
    page.feed(html_bytes.decode("utf-8"))
    if "".join(page.h1).strip() != title:
        raise ValueError("Rendered HTML is not the matching newsletter")
    article_path = f"/en/newsletters/{date}-newsletter/"
    article_url = BASE_URL + article_path
    article_links: list[str] = []

    def absolute(match):
        start, target, end = match.groups()
        if start.startswith("!"):
            raise ValueError("Email digest does not embed images")
        if "(" in target or "\\" in target:
            raise ValueError("Encode parentheses in URL targets and use forward slashes")
        if target.startswith("#"):
            target = article_url + target
        elif target.startswith("/en/"):
            target = BASE_URL + target
        parsed = urlsplit(target)
        if parsed.scheme not in {"https", "mailto", "nostr"} or (parsed.scheme == "https" and not parsed.netloc):
            raise ValueError(f"Email link needs an absolute supported URL: {target}")
        article_paths = {article_path, article_path.rstrip("/"), article_path + "index.html"}
        if (parsed.hostname or "").lower() in {"nostrcompass.org", "www.nostrcompass.org"} and parsed.path in article_paths:
            if parsed.fragment and unquote(parsed.fragment) not in page.ids:
                raise ValueError(f"Digest section is absent from rendered newsletter: {parsed.fragment}")
            article_links.append(target)
        return start + target + end

    email = LINK.sub(absolute, body).strip() + "\n"
    # Unsupported Markdown link forms must not silently escape URL checks.
    if re.search(r"(?<!\\)[\[\]]", LINK.sub("", email)):
        raise ValueError("Use inline Markdown links with URL targets; reference or nested links are unsupported")
    if re.search(r"(?i)\b(?:https?://|www\.)", LINK.sub("", email)):
        raise ValueError("Put web URLs in inline Markdown links so their destinations can be checked")
    if not article_links:
        raise ValueError("Digest must link readers to the matching full edition")
    visible = LINK.sub(lambda m: m[1][1:-2] if not m[1].startswith("!") else "", email)
    visible = re.sub(r"(?m)^\s*(?:#{1,6}|[-*+]|\d+\.|>)\s+", "", visible)
    words = len(re.findall(r"\S+", visible))
    if words > 1200:
        raise ValueError(f"Digest has {words} words; shorten the email to at most 1,200")
    receipt = {
        "schema_version": 1,
        "receipt_type": "email-digest-preparation",
        "issue": issue,
        "edition": date,
        "newsletter_path": str(newsletter.resolve()),
        "newsletter_sha256": sha256(source_bytes),
        "digest_path": str(digest.resolve()),
        "digest_sha256": sha256(digest_bytes),
        "rendered_html_path": str(rendered_html.resolve()),
        "rendered_html_sha256": sha256(html_bytes),
        "email_sha256": sha256(email.encode("utf-8")),
        "words": words,
        "article_links": article_links,
        "checks": ["matching full edition", "exact source hash", "absolute links", "rendered section anchors", "maximum 1200 words"],
        "editorial_review_required": True,
        "sent": False,
    }
    # This helper has no write path to either canonical input.
    if newsletter.read_bytes() != source_bytes or digest.read_bytes() != digest_bytes or rendered_html.read_bytes() != html_bytes:
        raise ValueError("Inputs changed during digest preparation")
    return email, receipt


def write_atomic(path: Path, value: str) -> None:
    """Replace a local output, without writing through a hard link to an input."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(value)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--newsletter", required=True, type=Path)
    parser.add_argument("--digest", required=True, type=Path)
    parser.add_argument("--rendered-html", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--receipt", required=True, type=Path)
    args = parser.parse_args()
    try:
        inputs = {p.resolve() for p in [args.newsletter, args.digest, args.rendered_html]}
        outputs = [args.output.resolve(), args.receipt.resolve()]
        if len(set(outputs)) != 2 or inputs.intersection(outputs):
            raise ValueError("Email outputs must be separate from every input")
        if any(re.fullmatch(r"\d{4}-\d{2}-\d{2}-newsletter\.md", p.name) for p in outputs):
            raise ValueError("Email output must not use a canonical newsletter filename")
        email, receipt = prepare(args.newsletter, args.digest, args.rendered_html)
        write_atomic(args.output, email)
        write_atomic(args.receipt, json.dumps(receipt, indent=2) + "\n")
    except (ValueError, OSError, yaml.YAMLError) as error:
        parser.exit(1, f"Email digest not prepared: {error}\n")
    print(f"Email digest prepared: {receipt['words']} words; editorial review and send remain separate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
