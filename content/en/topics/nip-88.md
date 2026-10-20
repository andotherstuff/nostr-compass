---
title: "NIP-88: Polls"
date: 2026-10-21
draft: false
categories: ["NIPs"]
---

NIP-88 is a draft, optional NIP merged in the nostr-protocol/nips repository. A kind 1068 poll puts its label in `content` and lists choices as `option` tags, each pairing an alphanumeric ID with a label. `relay` tags name where responses go. `polltype` selects `singlechoice`, the default, or `multiplechoice`, and `endsAt` sets the cutoff.

A kind 1018 response references the poll with an `e` tag and lists chosen IDs in `response` tags. Clients publish it to the poll's relays. Tallies count one vote per pubkey, using the latest within poll limits. Proof of one vote per person or a secret ballot requires separate mechanisms.

Primary source: the [NIP-88 text](https://github.com/nostr-protocol/nips/blob/master/88.md). Newsletter 45 covers the Feather implementation.

## Primary sources

- [NIP-88: Polls](https://github.com/nostr-protocol/nips/blob/master/88.md)

## Mentioned in

- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#feather)
