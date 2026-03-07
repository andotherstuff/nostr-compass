---
title: "NIP-50: Search"
date: 2025-12-31
draft: false
categories:
  - Protocol
  - Relay
---

NIP-50 defines a general search capability for Nostr relays. It adds full-text style querying on top of NIP-01's exact-match filters.

## How It Works

The protocol adds a `search` field to filter objects in `REQ` messages:

1. Clients submit a human-readable query string such as `best nostr apps`.
2. Relays interpret that query against event data, primarily the `content` field.
3. Results are sorted by match quality, not by `created_at`.
4. `limit` applies after relevance sorting.

Search filters can be combined with `kinds`, `ids`, authors, and other normal filter fields for more specific queries.

## Search Extensions

Relays may optionally support these extension parameters:

- `include:spam` - Disables default spam filtering
- `domain:<domain>` - Filters by verified NIP-05 domain
- `language:<code>` - Filters by ISO language code
- `sentiment:<value>` - Filters by negative, neutral, or positive sentiment
- `nsfw:<true/false>` - Includes or excludes NSFW content

Relays should ignore extensions they do not support, so clients need to treat them as hints, not guarantees.

## Interop Notes

- Clients should check relay capabilities via the `supported_nips` field
- Client-side verification of results is recommended
- Not all relays implement search; it remains an optional feature

Because ranking is implementation-defined, the same query can return different result sets on different relays. Clients that care about recall should query more than one search relay and merge results.

## Why It Matters

Structured filters work well when you already know the author, kind, or tag you want. Search is for the opposite case: discovery. That makes NIP-50 useful for app directories, long archives, and public note search, but it also means search quality depends heavily on each relay's indexing and spam filtering choices.

---

**Primary sources:**
- [NIP-50 Specification](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #4: NIP Updates](/en/newsletters/2026-01-07-newsletter/#nip-updates)

**See also:**
- [NIP-11: Relay Information](/en/topics/nip-11/)
