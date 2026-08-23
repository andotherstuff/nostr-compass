#!/usr/bin/env python3
"""Discover untracked Nostr applications from protocol and forge metadata."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import re
import subprocess
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


def normalize_url(value: object) -> str:
    if not isinstance(value, str) or not value:
        return ""
    value = value.strip().strip('"\'')
    if not value or any(character.isspace() or ord(character) < 32 or ord(character) == 127 for character in value):
        return ""
    scheme_match = re.match(r"^([A-Za-z][A-Za-z0-9+.-]*):", value)
    if scheme_match and scheme_match.group(1).casefold() not in {"http", "https"}:
        return ""
    if not scheme_match:
        if value.startswith(("/", ".", "#", "?")):
            return ""
        value = f"https://{value}"
    try:
        parts = urlsplit(value)
        host = parts.hostname
        port = parts.port
    except ValueError:
        return ""
    if parts.scheme.casefold() not in {"http", "https"} or not host or parts.username or parts.password:
        return ""
    if "." not in host and ":" not in host:
        return ""
    host = host.casefold()
    if host.startswith("www."):
        host = host[4:]
    netloc = f"[{host}]" if ":" in host and not host.startswith("[") else host
    if port is not None:
        netloc = f"{netloc}:{port}"
    path = parts.path.rstrip("/")
    if host == "github.com" and path.lower().endswith(".git"):
        path = path[:-4]
    return urlunsplit(("https", netloc, path, "", ""))


def parse_projects_index(text: str) -> dict[str, dict[str, str]]:
    repos: dict[str, str] = {}
    websites: dict[str, str] = {}
    names: dict[str, str] = {}
    current_name = ""
    for line in text.splitlines():
        name_match = re.match(r"^\s*-\s+name:\s*(.+?)\s*$", line)
        if name_match:
            current_name = name_match.group(1).strip().strip('"\'')
            names[current_name.casefold()] = current_name
            continue
        field_match = re.match(r"^\s+(repo|website):\s*(.+?)\s*$", line)
        if not field_match or not current_name:
            continue
        normalized = normalize_url(field_match.group(2))
        if not normalized:
            continue
        target = repos if field_match.group(1) == "repo" else websites
        target[normalized.casefold()] = current_name
    return {"repos": repos, "websites": websites, "names": names}


def parse_iso8601(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


APPLICATION_SIGNALS = {
    "app",
    "application",
    "board",
    "bot",
    "bridge",
    "browser",
    "chat",
    "client",
    "dashboard",
    "editor",
    "email",
    "extension",
    "feed",
    "forum",
    "gateway",
    "inbox",
    "mail",
    "market",
    "messenger",
    "mobile",
    "proxy",
    "pwa",
    "reader",
    "relay",
    "signer",
    "social",
    "tool",
    "wallet",
}


def has_explicit_nostr_application_signal(item: dict) -> bool:
    haystack = " ".join(
        [
            item.get("full_name") or "",
            item.get("description") or "",
            " ".join(item.get("topics") or []),
        ]
    ).casefold()
    if "nostr" not in haystack:
        return False
    words = set(re.findall(r"[a-z]+", haystack))
    return bool(words & APPLICATION_SIGNALS)


def github_candidates(
    items: list[dict],
    tracked: dict[str, dict[str, str]],
    seen_repos: set[str],
    since: datetime,
    *,
    first_run: bool,
    seen_owner_siblings: set[str] | None = None,
) -> tuple[list[dict], set[str]]:
    candidates: list[dict] = []
    updated_seen = {normalize_url(repo) for repo in seen_repos if repo}
    updated_owner_siblings = seen_owner_siblings if seen_owner_siblings is not None else set()
    normalized_owner_siblings = {normalize_url(repo) for repo in updated_owner_siblings if repo}
    updated_owner_siblings.clear()
    updated_owner_siblings.update(normalized_owner_siblings)
    for item in items:
        repository = normalize_url(item.get("html_url"))
        if not repository:
            continue
        homepage = normalize_url(item.get("homepage"))
        discovery_sources = item.get("_discovery_sources") or ["github_topic_active"]
        is_owner_sibling = "github_owner_sibling" in discovery_sources
        # A repository under an owner that already has a tracked project is
        # admitted on that provenance alone. Requiring the forge blurb to
        # advertise itself is what hid formstr-hq/nail, whose description
        # ("Nostr Email Bridge") named no recognised application noun.
        if not is_owner_sibling and not has_explicit_nostr_application_signal(item):
            continue
        if repository.casefold() in tracked["repos"] or (
            homepage and homepage.casefold() in tracked["websites"]
        ):
            continue
        created_at = parse_iso8601(item["created_at"])
        is_new = created_at >= since
        first_seen = repository not in updated_seen
        updated_seen.add(repository)
        if is_owner_sibling:
            # Keep owner-sibling discovery independent from the legacy active-
            # repository baseline. A repository may already be in seen_repos
            # because a topic/text query observed it before the owner sweep
            # existed; it still deserves one owner-provenance review. Thereafter
            # the dedicated set prevents it from reappearing every overlapping
            # weekly window.
            if repository in updated_owner_siblings:
                continue
            updated_owner_siblings.add(repository)
        elif not is_new and (first_run or not first_seen):
            continue
        source_types = discovery_sources
        if is_owner_sibling:
            pass
        elif is_new:
            source_types = ["github_topic_new" if source == "github_topic_active" else source for source in source_types]
        else:
            source_types = ["github_topic_first_seen"]
        candidates.append(
            {
                "name": item.get("full_name", "").split("/")[-1],
                "description": item.get("description") or "",
                "repository": repository,
                "website": homepage,
                "created_at": item.get("created_at"),
                "last_activity": item.get("pushed_at"),
                "stars": item.get("stargazers_count", 0),
                "topics": sorted(set(item.get("topics") or [])),
                "source_types": sorted(set(source_types)),
                "evidence_status": "unconfirmed",
                "evidence_level": "candidate-only",
                "review_flags": (
                    [
                        "sibling repository of an owner that already has a tracked project",
                        "owner provenance is not a Nostr-surface claim; verify behavior before tracking",
                    ]
                    if is_owner_sibling
                    else ["self-asserted forge metadata; verify Nostr behavior before tracking"]
                ),
            }
        )
    candidates.sort(key=lambda candidate: (candidate["created_at"] or "", candidate["repository"]), reverse=True)
    return candidates, updated_seen


def tag_values(event: dict, name: str) -> list[str]:
    return [
        tag[1]
        for tag in event.get("tags", [])
        if isinstance(tag, list)
        and len(tag) >= 2
        and tag[0] == name
        and isinstance(tag[1], str)
        and tag[1]
    ]


def parse_metadata(content: object) -> dict:
    if not isinstance(content, str):
        return {}
    try:
        value = json.loads(content or "{}")
    except json.JSONDecodeError:
        return {}
    return value if isinstance(value, dict) else {}


NOSTR_LISTING_PATTERNS = (
    r"\bnostr\b",
    r"\bnip[- ]?\d+\b",
    r"\bnwc\b",
    r"\bnutzaps?\b",
    r"\bblossom\b",
    r"\brelay (?:app|client|server|service)\b",
    r"\bsigned (?:nostr )?events?\b",
)


def has_nostr_listing_signal(name: object, summary: object, content: object) -> bool:
    text = " ".join(value if isinstance(value, str) else "" for value in (name, summary, content)).casefold()
    text = re.sub(r"\b(?:no|without)\s+(?:nostr|relay)\b", "", text)
    return any(re.search(pattern, text) for pattern in NOSTR_LISTING_PATTERNS)


def zapstore_candidates(events: list[dict], tracked: dict[str, dict[str, str]]) -> list[dict]:
    grouped: dict[tuple[str, str], list[dict]] = {}
    for event in events:
        if event.get("kind") != 32267 or not event.get("pubkey"):
            continue
        app_ids = tag_values(event, "d")
        if not app_ids or not app_ids[0].strip():
            continue
        grouped.setdefault((event["pubkey"], app_ids[0].strip()), []).append(event)

    candidates: list[dict] = []
    for (pubkey, app_id), versions in grouped.items():
        latest_created_at = max(int(event.get("created_at", 0)) for event in versions)
        latest_versions = [event for event in versions if int(event.get("created_at", 0)) == latest_created_at]
        latest = sorted(latest_versions, key=lambda event: event.get("id", ""))[-1]
        name = (tag_values(latest, "name") or [app_id])[0].strip()
        summary = (tag_values(latest, "summary") or [""])[0].strip()
        content = latest.get("content") if isinstance(latest.get("content"), str) else ""
        repository = normalize_url((tag_values(latest, "repository") or [""])[0])
        website = normalize_url((tag_values(latest, "url") or [""])[0])
        if not name or not (repository or website):
            continue
        if not has_nostr_listing_signal(name, summary, content):
            continue
        if repository and repository.casefold() in tracked["repos"]:
            continue
        if website and website.casefold() in tracked["websites"]:
            continue
        if name.casefold() in tracked["names"]:
            continue
        relays = sorted(
            {
                event["_relay"]
                for event in latest_versions
                if event.get("id") == latest.get("id") and event.get("_relay")
            }
        )
        candidates.append(
            {
                "name": name,
                "description": summary or content,
                "repository": repository,
                "website": website,
                "pubkeys": [pubkey],
                "event_id": latest.get("id"),
                "address": f"32267:{pubkey}:{app_id}",
                "created_at": latest_created_at,
                "source_relays": relays,
                "source_types": ["zapstore_listing"],
                "has_release_in_window": False,
                "relay_status": "multi-relay" if len(relays) >= 2 else "single-relay",
                "evidence_status": "unconfirmed",
                "evidence_level": "candidate-only",
                "review_flags": ["developer-signed listing without a joined release; verify product and repository ownership"],
            }
        )
    candidates.sort(key=lambda candidate: (candidate["created_at"], candidate["name"].casefold()), reverse=True)
    return candidates


def filter_verified_events(events: list[dict], validator) -> tuple[list[dict], list[str]]:
    validity: dict[str, bool] = {}
    rejected: list[str] = []
    for event in events:
        event_id = event.get("id") or ""
        if not event_id or event_id in validity:
            continue
        try:
            validity[event_id] = bool(validator(event))
        except (OSError, subprocess.SubprocessError, ValueError):
            validity[event_id] = False
        if not validity[event_id]:
            rejected.append(event_id)
    return [event for event in events if validity.get(event.get("id") or "", False)], rejected


def verify_nostr_event(event: dict) -> bool:
    raw_event = {key: value for key, value in event.items() if not key.startswith("_")}
    proc = subprocess.run(
        ["nak", "verify"],
        input=json.dumps(raw_event, separators=(",", ":")),
        capture_output=True,
        text=True,
        timeout=5,
        check=False,
    )
    return proc.returncode == 0


def nsite_references(event: dict) -> list[dict[str, str]]:
    references: list[dict[str, str]] = []
    for tag in event.get("tags", []):
        if len(tag) < 2 or tag[0] not in {"latest", "next"}:
            continue
        address = tag[1]
        if not isinstance(address, str) or not re.fullmatch(r"35128:[0-9a-fA-F]{64}:[^:\s]+", address):
            continue
        reference = {"relation": tag[0], "address": address}
        if len(tag) >= 3 and isinstance(tag[2], str) and tag[2].startswith("wss://") and not any(char.isspace() for char in tag[2]):
            reference["relay"] = tag[2]
        if reference not in references:
            references.append(reference)
    return references


def is_safe_handler_template(platform: str, value: object) -> bool:
    if not isinstance(value, str) or not value:
        return False
    if any(character.isspace() or ord(character) < 32 or ord(character) == 127 for character in value):
        return False
    if platform == "web":
        return bool(normalize_url(value))
    scheme_match = re.match(r"^([A-Za-z][A-Za-z0-9+.-]*):", value)
    if not scheme_match:
        return False
    return scheme_match.group(1).casefold() not in {"data", "file", "javascript", "vbscript"}


def nip89_candidates(events: list[dict], tracked: dict[str, dict[str, str]]) -> list[dict]:
    grouped: dict[tuple[str, str], list[dict]] = {}
    for event in events:
        if event.get("kind") != 31990 or not event.get("pubkey"):
            continue
        d_tags = tag_values(event, "d")
        if not d_tags:
            continue
        grouped.setdefault((event["pubkey"], d_tags[0]), []).append(event)

    candidates: list[dict] = []
    for (pubkey, d_tag), versions in grouped.items():
        latest_created_at = max(event.get("created_at", 0) for event in versions)
        latest_versions = [event for event in versions if event.get("created_at", 0) == latest_created_at]
        latest = max(latest_versions, key=lambda event: event.get("id", ""))
        supported_kinds = sorted(
            {
                int(value)
                for value in tag_values(latest, "k")
                if value.isdigit()
            }
        )
        if not supported_kinds or all(5000 <= kind < 6000 for kind in supported_kinds):
            continue

        metadata = parse_metadata(latest.get("content", ""))
        name = next(
            (
                value.strip()
                for value in (
                    metadata.get("name"),
                    metadata.get("display_name"),
                    metadata.get("displayName"),
                )
                if isinstance(value, str) and value.strip()
            ),
            "",
        )
        repository = normalize_url(metadata.get("repository") or metadata.get("repo") or metadata.get("github"))
        website = normalize_url(metadata.get("website") or metadata.get("url"))
        platform_tags = [
            {"platform": tag[0], "template": tag[1]}
            for tag in latest.get("tags", [])
            if isinstance(tag, list)
            and len(tag) >= 2
            and tag[0] in {"web", "ios", "android"}
            and is_safe_handler_template(tag[0], tag[1])
        ]
        if not name or not (repository or website or platform_tags):
            continue
        if repository and repository.casefold() in tracked["repos"]:
            continue
        if website and website.casefold() in tracked["websites"]:
            continue
        if name.casefold() in tracked["names"]:
            continue

        relays = sorted(
            {
                event["_relay"]
                for event in latest_versions
                if event.get("id") == latest.get("id") and event.get("_relay")
            }
        )
        candidates.append(
            {
                "name": name,
                "description": metadata.get("about") or metadata.get("description") or "",
                "repository": repository,
                "website": website,
                "platform_handlers": platform_tags,
                "nsite_references": nsite_references(latest),
                "pubkeys": [pubkey],
                "supported_kinds": supported_kinds,
                "event_id": latest.get("id"),
                "address": f"31990:{pubkey}:{d_tag}",
                "created_at": latest_created_at,
                "source_relays": relays,
                "source_types": ["nip89_handler"],
                "relay_status": "multi-relay" if len(relays) >= 2 else "single-relay",
                "evidence_status": "unconfirmed",
                "evidence_level": "candidate-only",
                "review_flags": ["self-published handler; verify repository ownership and released product"],
            }
        )
    candidates.sort(key=lambda candidate: (candidate["created_at"], candidate["name"].casefold()), reverse=True)
    return candidates


def candidate_aliases(candidate: dict) -> list[str]:
    aliases: list[str] = []
    repository = normalize_url(candidate.get("repository"))
    website = normalize_url(candidate.get("website"))
    if repository:
        aliases.append(f"repo:{repository.casefold()}")
    if website:
        aliases.append(f"website:{website.casefold()}")
    if not aliases:
        aliases.append(f"name:{candidate.get('name', '').casefold()}")
    return aliases


def candidate_key(candidate: dict) -> str:
    return candidate_aliases(candidate)[0]


def evidence_status_rank(value: object) -> int:
    ranks = {"rejected": 0, "unconfirmed": 1, "corroborated": 2}
    return ranks.get(value if isinstance(value, str) else "", -1)


def relay_status_rank(value: object) -> int:
    ranks = {"single-relay": 1, "multi-relay": 2}
    return ranks.get(value if isinstance(value, str) else "", -1)


def merge_candidate_fields(current: dict, candidate: dict, list_fields: set[str]) -> None:
    for field, value in candidate.items():
        if field in list_fields and isinstance(value, list):
            existing = current.setdefault(field, [])
            for item in value:
                if item not in existing:
                    existing.append(item)
        elif field == "evidence_status" and evidence_status_rank(value) > evidence_status_rank(current.get(field)):
            current[field] = value
        elif field == "relay_status" and relay_status_rank(value) > relay_status_rank(current.get(field)):
            current[field] = value
        elif not current.get(field) and value:
            current[field] = value


def merge_candidates(candidates: list[dict]) -> list[dict]:
    merged: dict[str, dict] = {}
    aliases_to_key: dict[str, str] = {}
    list_fields = {
        "source_types",
        "review_flags",
        "topics",
        "pubkeys",
        "supported_kinds",
        "source_relays",
        "platform_handlers",
        "nsite_references",
    }
    for candidate in candidates:
        aliases = candidate_aliases(candidate)
        matching_keys = list(dict.fromkeys(aliases_to_key[alias] for alias in aliases if alias in aliases_to_key))
        key = matching_keys[0] if matching_keys else candidate_key(candidate)
        if key not in merged:
            merged[key] = {
                field: list(value) if field in list_fields and isinstance(value, list) else value
                for field, value in candidate.items()
            }
        else:
            merge_candidate_fields(merged[key], candidate, list_fields)

        # A candidate can bridge records previously keyed by repo and website.
        for duplicate_key in matching_keys[1:]:
            if duplicate_key == key or duplicate_key not in merged:
                continue
            merge_candidate_fields(merged[key], merged.pop(duplicate_key), list_fields)
            for alias, mapped_key in list(aliases_to_key.items()):
                if mapped_key == duplicate_key:
                    aliases_to_key[alias] = key

        for alias in candidate_aliases(merged[key]):
            aliases_to_key[alias] = key
        for alias in aliases:
            aliases_to_key[alias] = key
    for candidate in merged.values():
        for field in list_fields:
            if field in candidate:
                if field in {"source_types", "topics", "pubkeys", "supported_kinds", "source_relays"}:
                    candidate[field] = sorted(candidate[field])
    return sorted(merged.values(), key=lambda candidate: (candidate.get("name", "").casefold(), candidate_key(candidate)))


def filter_protocol_updates(
    candidates: list[dict],
    seen_protocol_events: dict[str, str],
) -> tuple[list[dict], dict[str, str]]:
    updated = dict(seen_protocol_events)
    fresh: list[dict] = []
    for candidate in candidates:
        address = candidate.get("address")
        event_id = candidate.get("event_id")
        if not isinstance(address, str) or not address or not isinstance(event_id, str) or not event_id:
            continue
        if seen_protocol_events.get(address) == event_id:
            continue
        updated[address] = event_id
        fresh.append(candidate)
    return fresh, updated


def build_report(
    *,
    since: str,
    github_items: list[dict],
    nip89_events: list[dict],
    tracked: dict[str, dict[str, str]],
    seen_repos: set[str],
    first_run: bool,
    source_errors: dict[str, list[str]],
    zapstore_events: list[dict] | None = None,
    signature_rejections: dict[str, list[str]] | None = None,
    seen_protocol_events: dict[str, str] | None = None,
    seen_owner_siblings: set[str] | None = None,
) -> dict:
    since_dt = parse_iso8601(since)
    updated_owner_siblings = set(seen_owner_siblings or set())
    github, updated_seen = github_candidates(
        github_items,
        tracked,
        seen_repos,
        since_dt,
        first_run=first_run,
        seen_owner_siblings=updated_owner_siblings,
    )
    nip89 = nip89_candidates(nip89_events, tracked)
    zapstore = zapstore_candidates(zapstore_events or [], tracked)
    nip89, updated_protocol_events = filter_protocol_updates(nip89, seen_protocol_events or {})
    zapstore, updated_protocol_events = filter_protocol_updates(zapstore, updated_protocol_events)
    candidates = merge_candidates(github + nip89 + zapstore)
    signature_rejections = signature_rejections or {}
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "period": {"since": since},
        "source_status": {
            "github": "partial" if source_errors.get("github") else "ok",
            "nip89": "partial" if source_errors.get("nip89") else "ok",
            "zapstore": "partial" if source_errors.get("zapstore") else "ok",
        },
        "source_errors": source_errors,
        "signature_rejections": {
            source: {"count": len(event_ids), "event_ids": sorted(event_ids)}
            for source, event_ids in signature_rejections.items()
            if event_ids
        },
        "summary": {
            "source_records": {
                "github": len(github_items),
                "nip89": len({event.get("id") for event in nip89_events if event.get("id")}),
                "zapstore": len({event.get("id") for event in (zapstore_events or []) if event.get("id")}),
            },
            "github_candidates": len(github),
            "owner_sibling_candidates": len(
                [candidate for candidate in github if "github_owner_sibling" in (candidate.get("source_types") or [])]
            ),
            "tracked_owners_swept": min(len(tracked_github_owners(tracked)), OWNER_SIBLING_OWNER_LIMIT),
            "nip89_candidates": len(nip89),
            "zapstore_listing_candidates": len(zapstore),
            "candidate_count": len(candidates),
        },
        "review_policy": "candidate-only; never auto-add to projects.yml",
        "candidates": candidates,
        "_updated_seen_repositories": sorted(updated_seen),
        "_updated_seen_owner_siblings": sorted(updated_owner_siblings),
        "_updated_seen_protocol_events": updated_protocol_events,
    }


DEFAULT_RELAYS = [
    "wss://nos.lol",
    "wss://relay.primal.net",
    "wss://relay.snort.social",
    "wss://relay.nostr.net",
    "wss://nostr.mom",
]


def run_github_search(
    query: str,
    source: str,
    *,
    max_pages: int = 5,
    warnings: list[str] | None = None,
) -> list[dict]:
    items: list[dict] = []
    incomplete_results = False
    total_count = 0
    for page in range(1, max_pages + 1):
        command = [
            "gh",
            "api",
            "search/repositories",
            "-X",
            "GET",
            "-f",
            f"q={query}",
            "-f",
            "sort=updated",
            "-f",
            "order=desc",
            "-f",
            "per_page=100",
            "-f",
            f"page={page}",
        ]
        proc = subprocess.run(command, check=False, capture_output=True, text=True, timeout=60)
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr.strip() or f"gh exited {proc.returncode}")
        payload = json.loads(proc.stdout)
        incomplete_results = incomplete_results or bool(payload.get("incomplete_results"))
        page_items = payload.get("items", [])
        for item in page_items:
            item["_discovery_sources"] = [source]
        items.extend(page_items)
        total_count = min(int(payload.get("total_count", len(items))), 1000)
        if len(items) >= total_count or len(page_items) < 100:
            break
    if warnings is not None:
        if incomplete_results:
            warnings.append(f"{source}: GitHub search reported incomplete_results")
        if len(items) < total_count:
            warnings.append(f"{source}: GitHub search truncated at {len(items)} of {total_count} records")
    return items


def merge_github_results(result_sets: list[list[dict]]) -> list[dict]:
    merged: dict[str, dict] = {}
    for items in result_sets:
        for item in items:
            key = (item.get("full_name") or item.get("html_url") or "").casefold()
            if not key:
                continue
            if key not in merged:
                merged[key] = dict(item)
                merged[key]["_discovery_sources"] = list(item.get("_discovery_sources") or [])
                continue
            sources = merged[key].setdefault("_discovery_sources", [])
            for source in item.get("_discovery_sources") or []:
                if source not in sources:
                    sources.append(source)
    return list(merged.values())


def github_search_queries(since_day: str) -> list[tuple[str, str]]:
    return [
        (f"topic:nostr pushed:>={since_day} archived:false fork:false", "github_topic_active"),
        (f"nostr in:name,description created:>={since_day} archived:false fork:false", "github_text_new"),
        # created:>= only ever sees brand-new repositories. A repository created
        # months ago that starts shipping this week is equally newsworthy, so
        # sweep on activity as well as on creation.
        (f"nostr in:name,description pushed:>={since_day} archived:false fork:false", "github_text_active"),
    ]


# Backstop only. The sweep runs on the 5000/hour core REST budget, so the
# current tracked-owner count sits comfortably inside it; exceeding this is
# reported, never silently truncated.
OWNER_SIBLING_OWNER_LIMIT = 800


def tracked_github_owners(tracked: dict[str, dict[str, str]]) -> list[str]:
    """Distinct GitHub owners that already have at least one tracked repository."""
    owners: set[str] = set()
    for repository in tracked.get("repos", {}):
        match = re.match(r"^https?://(?:www\.)?github\.com/([^/]+)/[^/]+", repository)
        if match:
            owners.add(match.group(1).casefold())
    return sorted(owners)


def fetch_owner_repositories(
    owner: str,
    since_day: str,
    *,
    max_pages: int = 3,
    warnings: list[str] | None = None,
) -> list[dict]:
    """Repositories for one owner pushed on or after since_day, newest first.

    Uses the core REST listing rather than the search API: search costs 30
    requests per minute and cannot express "everything this owner touched"
    without one query per owner, while this endpoint sorts by push time so the
    walk stops as soon as it leaves the window.
    """
    collected: list[dict] = []
    for page in range(1, max_pages + 1):
        command = [
            "gh",
            "api",
            f"users/{owner}/repos?sort=pushed&direction=desc&type=public&per_page=100&page={page}",
        ]
        proc = subprocess.run(command, check=False, capture_output=True, text=True, timeout=60)
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr.strip() or f"gh exited {proc.returncode}")
        payload = json.loads(proc.stdout)
        if not isinstance(payload, list) or not payload:
            break
        stop = False
        for item in payload:
            pushed_at = item.get("pushed_at") or ""
            if pushed_at[:10] < since_day:
                stop = True
                break
            if item.get("private") or item.get("fork") or item.get("archived"):
                continue
            item["_discovery_sources"] = ["github_owner_sibling"]
            collected.append(item)
        if stop or len(payload) < 100:
            break
        if page == max_pages and warnings is not None:
            warnings.append(
                f"github_owner_sibling: {owner}: capped at {max_pages * 100} repositories while still inside window"
            )
    return collected


def fetch_owner_siblings(
    owners: list[str],
    since_day: str,
    *,
    warnings: list[str],
) -> list[dict]:
    """Sweep every tracked owner for repositories Compass does not track yet."""
    items: list[dict] = []
    for owner in owners:
        try:
            items.extend(fetch_owner_repositories(owner, since_day, warnings=warnings))
        except (RuntimeError, subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
            warnings.append(f"github_owner_sibling: {owner}: {exc}")
    return items


def fetch_github_discovery(
    since_day: str,
    tracked: dict[str, dict[str, str]] | None = None,
) -> tuple[list[dict], list[str]]:
    queries = github_search_queries(since_day)
    errors: list[str] = []
    owners = tracked_github_owners(tracked or {})
    if len(owners) > OWNER_SIBLING_OWNER_LIMIT:
        # Never truncate silently: a dropped owner is a project the sweep did
        # not look at, and the report has to say so.
        errors.append(
            f"github_owner_sibling: capped at {OWNER_SIBLING_OWNER_LIMIT} of {len(owners)} tracked owners; "
            f"not swept: {', '.join(owners[OWNER_SIBLING_OWNER_LIMIT:])}"
        )
        owners = owners[:OWNER_SIBLING_OWNER_LIMIT]
    results: list[list[dict]] = []
    if owners:
        results.append(fetch_owner_siblings(owners, since_day, warnings=errors))
    for query, source in queries:
        query_warnings: list[str] = []
        try:
            results.append(run_github_search(query, source, warnings=query_warnings))
        except (RuntimeError, subprocess.TimeoutExpired, json.JSONDecodeError) as exc:
            errors.append(f"{source}: {exc}")
        errors.extend(query_warnings)
    return merge_github_results(results), errors


def query_relay_kind(
    relay: str,
    kind: int,
    since_timestamp: int,
    *,
    page_size: int = 200,
    max_pages: int = 5,
) -> list[dict]:
    events: list[dict] = []
    until_timestamp: int | None = None
    for _ in range(max_pages):
        command = [
            "nak",
            "req",
            "-q",
            "-k",
            str(kind),
            "--since",
            str(since_timestamp),
            "--limit",
            str(page_size),
        ]
        if until_timestamp is not None:
            command.extend(["--until", str(until_timestamp)])
        command.append(relay)
        proc = subprocess.run(command, check=False, capture_output=True, text=True, timeout=25)
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr.strip() or f"nak exited {proc.returncode}")
        page: list[dict] = []
        for line in proc.stdout.splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if (
                isinstance(event, dict)
                and isinstance(event.get("id"), str)
                and event.get("id")
                and event.get("kind") == kind
                and isinstance(event.get("created_at"), int)
                and not isinstance(event.get("created_at"), bool)
            ):
                event["_relay"] = relay
                page.append(event)
        events.extend(page)
        if len(page) < page_size:
            break
        oldest = min(int(event.get("created_at", 0)) for event in page)
        if oldest <= since_timestamp:
            break
        until_timestamp = oldest - 1
    unique: dict[tuple[str, str], dict] = {}
    for event in events:
        unique[(event["id"], event["_relay"])] = event
    return list(unique.values())


def query_nip89_relay(relay: str, since_timestamp: int) -> list[dict]:
    return query_relay_kind(relay, 31990, since_timestamp)


def fetch_relay_kind_discovery(
    kind: int,
    since_timestamp: int,
    relays: list[str],
) -> tuple[list[dict], list[str], list[str]]:
    events: list[dict] = []
    errors: list[str] = []
    with ThreadPoolExecutor(max_workers=min(5, len(relays))) as executor:
        futures = {
            executor.submit(query_relay_kind, relay, kind, since_timestamp): relay
            for relay in relays
        }
        for future in as_completed(futures):
            relay = futures[future]
            try:
                events.extend(future.result())
            except (RuntimeError, subprocess.TimeoutExpired) as exc:
                errors.append(f"{relay}: {exc}")
    verified, rejected = filter_verified_events(events, verify_nostr_event)
    return verified, sorted(errors), rejected


def fetch_nip89_discovery(since_timestamp: int, relays: list[str]) -> tuple[list[dict], list[str], list[str]]:
    return fetch_relay_kind_discovery(31990, since_timestamp, relays)


def fetch_zapstore_discovery(since_timestamp: int) -> tuple[list[dict], list[str], list[str]]:
    return fetch_relay_kind_discovery(32267, since_timestamp, ["wss://relay.zapstore.dev"])


def load_json_list(path: Path) -> list[dict]:
    value = json.loads(path.read_text())
    if not isinstance(value, list):
        raise ValueError(f"fixture must contain a JSON list: {path}")
    return value


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since-days", type=int, default=8)
    parser.add_argument("--today", help="UTC date override for reproducible runs (YYYY-MM-DD)")
    parser.add_argument("--projects-file", type=Path, default=root / "data/projects.yml")
    parser.add_argument("--output-dir", type=Path, default=root / "data/app_discovery")
    parser.add_argument("--state-file", type=Path, default=root / "data/app_discovery/seen_repos.json")
    parser.add_argument("--relay", action="append", dest="relays")
    parser.add_argument("--github-fixture", type=Path)
    parser.add_argument("--nip89-fixture", type=Path)
    parser.add_argument("--zapstore-fixture", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    today = date.fromisoformat(args.today) if args.today else datetime.now(timezone.utc).date()
    since_day = today - timedelta(days=args.since_days)
    since_dt = datetime.combine(since_day, time.min, timezone.utc)
    source_errors: dict[str, list[str]] = {}

    tracked = parse_projects_index(args.projects_file.read_text())

    if args.github_fixture:
        github_items = load_json_list(args.github_fixture)
        github_errors: list[str] = []
    else:
        github_items, github_errors = fetch_github_discovery(since_day.isoformat(), tracked)
    if github_errors:
        source_errors["github"] = github_errors

    if args.nip89_fixture:
        nip89_events = load_json_list(args.nip89_fixture)
        nip89_errors: list[str] = []
        nip89_rejections: list[str] = []
    else:
        nip89_events, nip89_errors, nip89_rejections = fetch_nip89_discovery(
            int(since_dt.timestamp()), args.relays or DEFAULT_RELAYS
        )
    if nip89_errors:
        source_errors["nip89"] = nip89_errors

    if args.zapstore_fixture:
        zapstore_events = load_json_list(args.zapstore_fixture)
        zapstore_errors: list[str] = []
        zapstore_rejections: list[str] = []
    else:
        zapstore_events, zapstore_errors, zapstore_rejections = fetch_zapstore_discovery(int(since_dt.timestamp()))
    if zapstore_errors:
        source_errors["zapstore"] = zapstore_errors

    signature_rejections = {
        "nip89": nip89_rejections,
        "zapstore": zapstore_rejections,
    }

    first_run = not args.state_file.exists()
    if first_run:
        seen_repos: set[str] = set()
        seen_owner_siblings: set[str] = set()
        seen_protocol_events: dict[str, str] = {}
    else:
        state = json.loads(args.state_file.read_text())
        seen_repos = set(state.get("repositories", []))
        raw_protocol_events = state.get("protocol_events", {})
        raw_owner_siblings = state.get("owner_sibling_repositories", [])
        seen_owner_siblings = {
            repository
            for repository in raw_owner_siblings
            if isinstance(repository, str) and normalize_url(repository)
        } if isinstance(raw_owner_siblings, list) else set()
        seen_protocol_events = {
            address: event_id
            for address, event_id in raw_protocol_events.items()
            if isinstance(address, str) and isinstance(event_id, str)
        } if isinstance(raw_protocol_events, dict) else {}

    report = build_report(
        since=since_dt.isoformat(),
        github_items=github_items,
        nip89_events=nip89_events,
        zapstore_events=zapstore_events,
        tracked=tracked,
        seen_repos=seen_repos,
        first_run=first_run,
        source_errors=source_errors,
        signature_rejections=signature_rejections,
        seen_protocol_events=seen_protocol_events,
        seen_owner_siblings=seen_owner_siblings,
    )
    updated_seen = report.pop("_updated_seen_repositories")
    updated_owner_siblings = report.pop("_updated_seen_owner_siblings")
    updated_protocol_events = report.pop("_updated_seen_protocol_events")
    report["period"]["through"] = today.isoformat()
    report["period"]["days"] = args.since_days

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / f"discovery_{today.isoformat()}.json"
    output_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    args.state_file.parent.mkdir(parents=True, exist_ok=True)
    args.state_file.write_text(
        json.dumps(
            {
                "updated_at": datetime.now(timezone.utc).isoformat(),
                "repositories": updated_seen,
                "owner_sibling_repositories": updated_owner_siblings,
                "protocol_events": updated_protocol_events,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )

    print(f"App discovery candidates: {report['summary']['candidate_count']}")
    print(
        f"GitHub: {report['summary']['github_candidates']}; "
        f"NIP-89: {report['summary']['nip89_candidates']}; "
        f"Zapstore listings: {report['summary']['zapstore_listing_candidates']}"
    )
    print(f"Saved: {output_path}")
    if (
        not github_items
        and not nip89_events
        and not zapstore_events
        and source_errors.get("github")
        and source_errors.get("nip89")
        and source_errors.get("zapstore")
    ):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
