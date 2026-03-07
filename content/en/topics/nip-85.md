---
title: "NIP-85: Trusted Assertions"
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

Trusted Assertions are addressable events. The `d` tag identifies the subject being scored, and the event kind identifies what sort of subject it is: pubkeys (30382), regular events (30383), addressable events (30384), and NIP-73 identifiers (30385).

Users declare which providers they trust through kind 10040. Those provider lists can be public in tags or encrypted in the event content with [NIP-44](/en/topics/nip-44/), which matters when a user does not want to publish their trust inputs openly.

## Why It Matters

The useful insight in NIP-85 is that it standardizes outputs, not algorithms. Two providers can both publish a `rank` tag for the same pubkey while using different Web of Trust formulas, mute handling, relay coverage, or anti-spam heuristics. Clients stay interoperable because the result format matches even when the computation does not.

That is a better fit for Nostr than pretending there will be one canonical ranking service. Users choose whose assertions they trust.

## Trust Model

Service providers must sign their own assertion events, and the spec recommends different service keys for different algorithms or user-specific viewpoints. That keeps a provider from collapsing unrelated ranking systems into one opaque identity.

Trust still stays local. Signed output proves which provider published a score, not that the score is correct. Clients need policy around which provider keys to use, which relays to fetch from, and how to handle conflicting assertions.

## Interop Notes

NIP-85 extends beyond people and posts. Kind 30385 lets providers score NIP-73 external identifiers such as books, websites, hashtags, and locations. That creates a path for interoperable reputation and engagement data around subjects outside Nostr itself.

---

**Primary sources:**
- [NIP-85 Specification](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #2223](https://github.com/nostr-protocol/nips/pull/2223) - Service provider discoverability guidance

**Mentioned in:**
- [Newsletter #10: NIP-85 Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #11: NIP-85 Service Provider Discoverability](/en/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12: Protocol Recap](/en/newsletters/2026-03-04-newsletter/)

**See also:**
- [NIP-44: Encrypted Payloads](/en/topics/nip-44/)
- [NIP-73: External Content IDs](/en/topics/nip-73/)
- [Web of Trust](/en/topics/web-of-trust/)
