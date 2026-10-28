---
title: "Buzz NIP-AP: Agent personas"
date: 2026-10-21
draft: false
categories: ["NIPs"]
---

Buzz NIP-AP is a draft Buzz project specification outside the accepted NIPs in nostr-protocol/nips.

It defines kind 30175 persona events, addressable definitions for instantiating an AI agent, keyed by a plaintext `d` slug. Kind 30178 holds a team-catalog projection. Implementing relays gate both kinds: authors read their own events, and other readers see an event in queries, live delivery, search, counts, or id lookups only if it carries `["shared", "true"]`. Sharing a team exposes every member's embedded projection and instructions, including members with unshared personas. The gate controls access without encrypting content; the relay operator can still read it.

Primary source: the [NIP-AP specification](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md) in the Buzz repository.

## Primary sources

- [Buzz NIP-AP: Agent Personas](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md)

## Mentioned in

- [Newsletter #46 (2026-10-28): buzz](/en/newsletters/2026-10-28-newsletter/#buzz)

- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#buzz)
