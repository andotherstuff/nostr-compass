---
title: "NIP-FE Proposal: HTTP Relay Commands"
date: 2026-09-30
draft: false
categories:
  - Project Proposals
  - Relays
---

Amethyst uses the provisional label NIP-FE for relay commands over HTTP in its Geode relay and Quartz client work. The label is not an assigned NIP or evidence of adoption across Nostr relays.

## Transport

Instead of opening a WebSocket connection, a client posts one `REQ`, `COUNT`, or `EVENT` frame to a relay HTTP endpoint. The response streams relay frames as newline-delimited JSON. A client must distinguish a completed answer from a cut-off stream, and an authenticated request still uses signed Nostr HTTP authorization. The transport changes how commands reach a relay; it does not change the underlying event signature or event content.

Amethyst's [merged implementation](https://github.com/vitorpamplona/amethyst/pull/4231) adds the Geode route, Quartz client support, body and concurrency limits, and tests of framing and authorization. It is source-level implementation evidence, not proof that independent relays have implemented the same proposal.

## Naming collision

An unrelated [draft pull request in the NIPs repository](https://github.com/nostr-protocol/nips/pull/2488) also uses **NIP-FE**, this time for private feeds built on a proposed multi-recipient envelope. That work is open and describes a different problem from Amethyst's HTTP transport. Neither provisional use establishes that the label has been assigned to an accepted specification; readers should identify the proposal by its source and subject.

---

**Primary sources:**
- [Amethyst Geode and Quartz implementation PR](https://github.com/vitorpamplona/amethyst/pull/4231)
- [Amethyst repository](https://github.com/vitorpamplona/amethyst)
- [Open private-feeds draft also using NIP-FE](https://github.com/nostr-protocol/nips/pull/2488)

**Mentioned in:**
- [Newsletter #42: Amethyst relay commands](/en/newsletters/2026-09-30-newsletter/#amethyst-repairs-encrypted-group-interoperability)
