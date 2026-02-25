---
title: "NIP-90"
date: 2026-02-25
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 defines Data Vending Machines (DVMs), a marketplace protocol for requesting and paying for computational work on Nostr.

## How It Works

Clients publish job request events (kinds 5000-5999) specifying the work needed. Service providers monitor for requests matching their capabilities and publish results after completing the computation. Payment happens through Lightning or other mechanisms negotiated in the job flow.

Job kinds define different computation types: text generation, image generation, translation, content discovery, and more. Each kind specifies the expected input/output format.

## Key Features

- Decentralized compute marketplace
- Kind-based job type system
- Provider competition on price and quality
- Extensible for new computation types

---

**Primary sources:**
- [NIP-90 Specification](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Mentioned in:**
- [Newsletter #11: NIP-AC DVM Agent Coordination](/en/newsletters/2026-02-25-newsletter/#nip-updates)

**See also:**
- [NIP-85: Trusted Assertions](/en/topics/nip-85/)
