#!/usr/bin/env python3
"""Fetch Sovereign Engineering cohorts and tagged Nostr activity."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import date, datetime, time, timedelta, timezone
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

BASE_URL = "https://sovereignengineering.io"
DEFAULT_RELAYS = [
    "wss://relay.damus.io",
    "wss://nos.lol",
    "wss://relay.primal.net",
    "wss://relay.nostr.band",
]
REPO_HOSTS = {"github.com", "gitlab.com", "codeberg.org", "gitworkshop.dev"}
COHORT_RE = re.compile(r"^SEC-(\d+)$", re.I)
COHORT_TAG_RE = re.compile(r"^SEC-?(\d+)$", re.I)


class StructuredHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.active: tuple[str, str | None] | None = None
        self.buffer: list[str] = []
        self.items: list[tuple[str, str, str | None]] = []
        self.anchor_href: str | None = None
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "svg", "noscript"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        values = dict(attrs)
        if tag == "a":
            self.anchor_href = values.get("href")
        if tag in {"h1", "h2", "h3", "h4", "p", "a"}:
            self.active = (tag, self.anchor_href)
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if not self.skip_depth and self.active:
            self.buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "svg", "noscript"}:
            if self.skip_depth:
                self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if self.active and self.active[0] == tag:
            text = " ".join("".join(self.buffer).split())
            if text:
                self.items.append((tag, text, self.active[1]))
            self.active = None
            self.buffer = []
        if tag == "a":
            self.anchor_href = None


def parse_html(text: str) -> list[tuple[str, str, str | None]]:
    parser = StructuredHTMLParser()
    parser.feed(text)
    return parser.items


def cohort_sort_key(label: str) -> int:
    match = COHORT_RE.match(label)
    return int(match.group(1)) if match else -1


def parse_projects_index(text: str) -> dict:
    cohorts: dict[str, str | None] = {}
    for tag, label, href in parse_html(text):
        if tag == "h3" and COHORT_RE.match(label):
            cohorts[label.upper()] = href
    labels = sorted(cohorts, key=cohort_sort_key)
    archive_paths = sorted(
        {
            href
            for href in cohorts.values()
            if href and re.fullmatch(r"/projects/SEC-\d+", href, re.I)
        },
        key=lambda path: cohort_sort_key(path.rsplit("/", 1)[-1]),
    )
    return {
        "current_cohort": labels[-1] if labels else None,
        "latest_archive": archive_paths[-1].rsplit("/", 1)[-1].upper() if archive_paths else None,
        "archive_paths": archive_paths,
    }


def is_repository_url(url: str) -> bool:
    return urlparse(url).netloc.lower() in REPO_HOSTS


def parse_cohort_projects(text: str) -> list[dict]:
    projects: list[dict] = []
    current: dict | None = None
    for tag, label, href in parse_html(text):
        if tag == "h2":
            current = {"name": label, "repositories": [], "links": []}
            projects.append(current)
        elif tag == "a" and current and href and href.startswith(("http://", "https://")):
            if href not in current["links"]:
                current["links"].append(href)
            if is_repository_url(href) and href not in current["repositories"]:
                current["repositories"].append(href)
    return [project for project in projects if project["links"]]


def normalize_nostr_events(events: list[dict], current_cohort: str | None) -> dict:
    unique = {event.get("id"): event for event in events if event.get("id")}
    normalized = sorted(unique.values(), key=lambda event: event.get("created_at", 0), reverse=True)
    project_tags: dict[str, str] = {}
    excluded = {"soveng", "demoday"}
    if current_cohort:
        excluded.add(current_cohort.replace("-", "").lower())
    for event in normalized:
        for tag in event.get("tags", []):
            if len(tag) >= 2 and tag[0] == "t":
                value = tag[1]
                if value.lower() not in excluded and not COHORT_TAG_RE.match(value):
                    key = value.lower()
                    prior = project_tags.get(key)
                    if prior is None or (value.isupper() and not prior.isupper()):
                        project_tags[key] = value
    return {
        "project_tags": sorted(project_tags.values(), key=str.lower),
        "events": normalized,
    }


def fetch_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": "NostrCompass/1.0"})
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", "replace")


def query_tagged_events(tags: list[str], since: str, until: str, relays: list[str]) -> list[dict]:
    cmd = ["nak", "req", "-q", "-k", "1", "-s", since, "-u", until, "-l", "500"]
    for tag in tags:
        cmd.extend(["-t", f"t={tag}"])
    cmd.extend(relays)
    proc = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=90)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"nak exited {proc.returncode}")
    events = []
    for line in proc.stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict) and event.get("id"):
            events.append(event)
    return events


def inclusive_until(value: str) -> str:
    day = date.fromisoformat(value) + timedelta(days=1)
    return datetime.combine(day, time.min, timezone.utc).isoformat()


def collect(since: str, until: str, relays: list[str]) -> dict:
    index = parse_projects_index(fetch_text(f"{BASE_URL}/projects"))
    archive_projects = []
    if index["latest_archive"]:
        archive_url = f"{BASE_URL}/projects/{index['latest_archive']}"
        archive_projects = parse_cohort_projects(fetch_text(archive_url))
    current_tag = index["current_cohort"].replace("-", "") if index["current_cohort"] else None
    tags = ["SovEng", "soveng"]
    if current_tag:
        tags.extend([current_tag, current_tag.lower()])
    events = query_tagged_events(tags, since, inclusive_until(until), relays)
    nostr = normalize_nostr_events(events, index["current_cohort"])
    return {
        "source": f"{BASE_URL}/projects",
        **index,
        "latest_archive_projects": archive_projects,
        "nostr": {
            "tags": tags,
            "relays": relays,
            **nostr,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--since", required=True)
    parser.add_argument("--until", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--relay", action="append", dest="relays")
    args = parser.parse_args()
    result = collect(args.since, args.until, args.relays or DEFAULT_RELAYS)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(
        f"SEC {result['current_cohort']}: {len(result['latest_archive_projects'])} archived projects, "
        f"{len(result['nostr']['events'])} tagged events"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
