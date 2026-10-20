---
title: "NIP-35: Torrents"
date: 2026-10-21
draft: false
categories: ["NIPs"]
---

NIP-35 is a draft, optional NIP for torrent index events. A kind 2003 event carries a BitTorrent v1 infohash in an `x` tag along with file paths, and it may name trackers. The events hold index metadata, and peers fetch the file contents over BitTorrent. Comments on a torrent use kind 2004 and follow NIP-10 threading.

The number has an earlier history. Draft Wraps held NIP-35 until a 2024 renumbering moved that proposal to NIP-37. A reference to NIP-35 from before that change may mean Draft Wraps. Today the number belongs to Torrents.

The [current NIP-35 text](https://github.com/nostr-protocol/nips/blob/master/35.md) defines the event format. The [renumbering commit](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408) records the earlier assignment.

## Primary sources

- [NIP-35: Torrents](https://github.com/nostr-protocol/nips/blob/master/35.md)
- [nostr-protocol/nips commit 48674e5 (2024 renumbering)](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408)

## Mentioned in

- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#short-history)
