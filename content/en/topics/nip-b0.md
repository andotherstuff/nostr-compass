---
title: "NIP-B0: Web Bookmarks"
date: 2026-05-28
draft: false
categories:
  - Protocol
  - Social
---

NIP-B0 defines a parameterized replaceable event (kind 39701) that publishes web bookmarks as first-class Nostr events. The proposal lets users build curated bookmark collections that can be discovered, zapped, and re-published across clients without depending on a central bookmark service.

## How it works

A bookmark is a kind 39701 event whose `d` tag is the canonical URL of the bookmarked page. Replaceable semantics let the author update their own bookmark for that URL (re-tagging, updating the title, marking it stale) without producing duplicate events. The content field carries the author's note about the bookmark; tags carry title, description, image, and `t` topic tags for discovery.

```json
{
  "kind": 39701,
  "tags": [
    ["d", "https://example.com/an-article-worth-saving"],
    ["title", "Article Title"],
    ["t", "nostr"],
    ["t", "protocol"],
    ["published_at", "1717000000"]
  ],
  "content": "Useful primer on the topic.",
  "pubkey": "...",
  "sig": "..."
}
```

The `d` tag identifies the bookmark uniquely per author, so two users can both bookmark the same URL with their own annotations and tag sets.

## Discovery and curation

Because every bookmark is a first-class event, any Nostr client can render a feed of bookmarks by subscribing to kind 39701 events filtered by tags or authors. Curator-driven workflows become natural: a curator publishes a list of bookmarks, readers follow the curator's pubkey, and the bookmarks flow through any relay that carries them. There is no central directory.

## Implementations

- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) — Reference web client with a three-box architecture (curator, indexer, viewer) and a tier system funded by direct-to-curator NIP-57 zaps. Implements NIP-B0 alongside NIP-07, NIP-46, NIP-57, NIP-44, NIP-98, NIP-65, and Blossom BUD-01/BUD-04 for file storage.

## Trust and security notes

- Bookmarks are public by default; do not publish private reading lists this way
- Re-publishing relies on relays continuing to carry the events; ephemeral relays will drop bookmarks
- The `published_at` tag is publisher-asserted, not verifiable

---

**Primary sources:**
- [NIP-B0 proposed specification](https://github.com/nostr-protocol/nips/pull/2089) — Tracks the proposed kind 39701 web bookmark event
- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) — Reference implementation with curator tier system

**Mentioned in:**
- [Newsletter #24: deepmarks NIP-B0 bookmarks with curator-monetized publishing](/en/newsletters/2026-05-28-newsletter/#deepmarks-nip-b0-bookmarks-with-curator-monetized-publishing)

**See also:**
- [NIP-57: Lightning Zaps](/en/topics/nip-57/)
- [NIP-65: Relay List Metadata](/en/topics/nip-65/)
