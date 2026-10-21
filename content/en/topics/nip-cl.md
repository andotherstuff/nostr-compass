---
title: "Buzz NIP-CL: Channel identity and discovery"
date: 2026-10-21
draft: false
categories: ["NIPs"]
---

Buzz NIP-CL is a draft relay specification from the Buzz project, outside the accepted NIPs in nostr-protocol/nips.

It adds identity facts to relay-signed NIP-29 channel-state events (kinds 39000 to 39002), so clients of implementing relays can find channels with ordinary NIP-01 filters. The relay places `t` tags for the channel type and each label, then a `P` tag with the creator's hex pubkey, ahead of any other `t` or `P` tag. Labels let a plugin or agent find channels it created. Ordinary chat lists exclude system channels, though explicit discovery queries can request them.

Primary source: the [NIP-CL specification](https://github.com/block/buzz/blob/main/docs/nips/NIP-CL.md) in the Buzz repository.

## Primary sources

- [Buzz NIP-CL: Channel Identity and Discovery](https://github.com/block/buzz/blob/main/docs/nips/NIP-CL.md)

## Mentioned in

- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#buzz)
