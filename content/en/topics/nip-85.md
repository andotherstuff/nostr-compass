---
title: "NIP-85"
date: 2026-02-18
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85 defines Trusted Assertions, a system for delegating expensive calculations to trusted service providers who publish signed results as Nostr events.

## How It Works

Web of Trust scores, engagement metrics, and other computed values require crawling many relays and processing large event volumes. This work is impractical on mobile devices. NIP-85 lets specialized providers perform these calculations and publish results that clients can query.

Service providers advertise their capabilities via kind 30085 events. Clients discover providers by querying for these announcements from pubkeys the user already follows or trusts. Results come as kind 30382 events signed by the provider.

## Key Features

- Delegated computation for resource-intensive metrics
- Provider discovery through social graph
- Signed assertions for verifiable results
- Client-side trust decisions

---

**Primary sources:**
- [NIP-85 Specification](https://github.com/nostr-protocol/nips/blob/master/85.md)

**Mentioned in:**
- [Newsletter #10: NIP-85 Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #11: NIP-85 Service Provider Discoverability](/en/newsletters/2026-02-25-newsletter/#nip-updates)

**See also:**
- [Web of Trust](/en/topics/web-of-trust/)
