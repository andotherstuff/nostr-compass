---
title: "NIP-38: User Statuses"
date: 2026-08-26
description: "Defines short-lived user status events, including general and music-status categories."
---

NIP-38 defines kind 30315 addressable events for short user statuses. A `d` tag identifies the status category, such as `general` or `music`, while optional `r` and `p` tags can link to a URL or identify an artist. Clients can use the event's `expiration` tag to stop displaying stale statuses.

## How It Works

A user publishes a kind 30315 event with status text in `content`. The event is addressable by pubkey, kind, and `d` tag, so a newer event in the same category replaces the older one. An empty content field clears that status.

---

**Primary sources:**
- [NIP-38 specification](https://github.com/nostr-protocol/nips/blob/master/38.md) - User statuses

**Mentioned in:**
- [Newsletter #37: NoorNote v1.3.6: profile statuses and classified listings](/en/newsletters/2026-08-26-newsletter/#noornote-v136-profile-statuses-and-classified-listings)
