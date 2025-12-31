---
title: "NIP-50: Search"
date: 2025-12-31
draft: false
categories:
  - Protocol
  - Relay
---

NIP-50 defines a generalized search capability for Nostr relays, allowing clients to perform full-text searches beyond structured queries by tags or IDs.

## How It Works

The protocol adds a `search` field to filter objects in REQ messages:

1. Clients submit human-readable search queries (e.g., "best nostr apps")
2. Relays interpret and match queries against event data, primarily the `content` field
3. Results are ranked by relevance rather than chronological order
4. The `limit` filter applies after relevance sorting

Search filters can be combined with other constraints like `kinds` and `ids` for more specific queries.

## Search Extensions

Relays may optionally support these extension parameters:

- `include:spam` - Disables default spam filtering
- `domain:<domain>` - Filters by verified NIP-05 domain
- `language:<code>` - Filters by ISO language code
- `sentiment:<value>` - Filters by negative/neutral/positive sentiment
- `nsfw:<true/false>` - Includes or excludes NSFW content

## Client Considerations

- Clients should check relay capabilities via the `supported_nips` field
- Client-side verification of results is recommended
- Not all relays implement search; it remains an optional feature

---

**Primary sources:**
- [NIP-50 Specification](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-11: Relay Information](/en/topics/nip-11/)
