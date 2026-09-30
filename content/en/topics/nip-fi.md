---
title: "Buzz NIP-FI: Federated Identity Assertions"
date: 2026-09-30
draft: false
categories:
  - Project Proposals
  - Identity
  - Relays
---

NIP-FI is Buzz's **project-specific** federated-identity assertion specification. The name does not imply adoption by the `nostr-protocol/nips` repository or interoperation with relays outside Buzz.

## HTTP ingress

For protected HTTP requests in enforcement mode, Buzz pairs a federated-identity assertion with a NIP-98 signed authorization event. The Nostr public key proven by the HTTP signature must match the key named in the assertion. Missing, mismatched, or unverifiable evidence is rejected. Buzz uses this pairing to connect an external identity issuer's authorization decision to the Nostr key making the request.

The [project specification revision](https://github.com/block/buzz/pull/7254) defines the enforcement model. The [merged HTTP ingress implementation](https://github.com/block/buzz/pull/7264) covers Buzz's protected HTTP surfaces, including relay bridge, media, workflow, and Git paths. The merge reports source tests; it does not mean another Nostr relay implements the same policy.

---

**Primary sources:**
- [Buzz NIP-FI specification revision](https://github.com/block/buzz/pull/7254)
- [Buzz HTTP ingress implementation](https://github.com/block/buzz/pull/7264)

**Mentioned in:**
- [Newsletter #42: Buzz identity controls](/en/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
