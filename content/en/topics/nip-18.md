---
title: "NIP-18: Reposts"
date: 2025-12-17
draft: false
categories:
  - Social
  - Protocol
---

NIP-18 defines how to repost events, similar to retweets on other platforms.

## Structure

A repost is a kind 6 event (for kind 1 notes) or kind 16 (generic repost) containing:
- `e` tag referencing the reposted event
- `p` tag referencing the original author
- Optionally, the full original event in the `content` field

## Recent Changes

Improved support for reposting replaceable events with `a` tag support. This allows reposts of addressable events (kinds 30000-39999) to reference them by their address rather than a specific event ID.

---

**Primary sources:**
- [NIP-18 Specification](https://github.com/nostr-protocol/nips/blob/master/18.md)

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
