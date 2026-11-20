---
title: "NIP-0D (proposed): Relay Onion Discovery"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

NIP-0D is the identifier proposed in open pull request [#2550](https://github.com/nostr-protocol/nips/pull/2550). It has not been merged. The draft lets a relay advertise an onion address for clients that cannot reach the relay's clearnet host from a Tor exit. A relay can send an `Onion-Location` header over TLS, or it can publish a `_onion.<relay host>` DNS TXT record. Clients should prefer the header. When they follow an advertisement, clients keep the original path, map `http(s)` to `ws(s)` and connect only to the onion target. Falling back to clearnet is permitted as a MAY.

For DNS discovery, the draft advises DNSSEC or a trusted resolver. It also warns that a TXT lookup made outside Tor reveals interest in the relay. NIP-42 AUTH may use either identity, and clients treat the advertised pair as a single relay. The author reports one working relay, but general rollout has not been shown. This is relay-side discovery. It is a separate topic from client-side Tor support.

**Primary sources:**
- [NIPs PR #2550: relay onion discovery](https://github.com/nostr-protocol/nips/pull/2550)

**Mentioned in:**
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#nostr-protocol-nips-2550)

**See also:**
- [NIP-42: Client authentication](/en/topics/nip-42/)
- [NIP-11: Relay information document](/en/topics/nip-11/)
- [NIP-01: Basic protocol](/en/topics/nip-01/)
