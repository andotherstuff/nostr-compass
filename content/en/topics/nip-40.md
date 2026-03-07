---
title: "NIP-40: Expiration Timestamp"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-40 defines an expiration tag that tells relays when an event should be deleted.

## How It Works

Events include an `expiration` tag with a Unix timestamp:

```json
["expiration", "1734567890"]
```

After this time, relays should delete the event and refuse to serve it.

## Why It Matters

- Ephemeral content that should disappear after a set time
- Time-limited offers or announcements
- Listing expiration in marketplaces (e.g., Shopstr)
- Reducing relay storage requirements

Expiration is a retention hint, not a revocation system. It helps align relay behavior around stale content, but it does not guarantee erasure once another relay, client, or archive has already copied the event.

## Trust and Security Notes

- Relays are not required to honor expiration (but most do)
- Clients should not rely on expiration for security-critical content deletion
- Once content is fetched by another client, it may be cached or re-published
- Expiration does not hide that an event existed. Event ids, quotes, or off-relay copies may still survive after the timestamp passes

---

**Primary sources:**
- [NIP-40 Specification](https://github.com/nostr-protocol/nips/blob/master/40.md)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#rust-nostr-library)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
