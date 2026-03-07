---
title: "NIP-18: Reposts"
date: 2025-12-17
draft: false
categories:
  - Social
  - Protocol
---

NIP-18 defines how to repost events, similar to retweets on other platforms.

## How It Works

A repost is a kind 6 event (for kind 1 notes) or kind 16 (generic repost) containing:
- `e` tag referencing the reposted event
- `p` tag referencing the original author
- Optionally, the full original event in the `content` field

Kind 6 is specific to text notes. Kind 16 exists so clients can repost other event types without pretending everything is a kind 1 note.

## Interop Notes

Improved support for reposting replaceable events with `a` tag support. This allows reposts of addressable events (kinds 30000-39999) to reference them by their address rather than a specific event ID.

That distinction matters because addressable events can be updated over time. Reposting by `a` coordinate lets clients point to the current version of an addressable event, while reposting by event ID freezes a specific historical instance.

## Why It Matters

Reposts are more than a UI share button. They are part of how content moves across social graphs, how clients count engagement, and how relay hint data propagates through the network. If a client mishandles repost tags, thread reconstruction and event fetching can break in subtle ways.

---

**Primary sources:**
- [NIP-18 Specification](https://github.com/nostr-protocol/nips/blob/master/18.md)
- [PR #2132](https://github.com/nostr-protocol/nips/pull/2132) - `a` tag support for generic reposts

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #8: News](/en/newsletters/2026-02-04-newsletter/#news)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
- [NIP-10: Text Note Threading](/en/topics/nip-10/)
