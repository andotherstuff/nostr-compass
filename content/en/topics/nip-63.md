---
title: "NIP-63: Paywall / Premium Content"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Monetization
---

NIP-63 is a proposed standard for handling gated content within the Nostr protocol, allowing creators to require payment before revealing content.

## How It Works

Content creators can publish events where the full content is encrypted or hidden behind a paywall. After payment verification, the content is unlocked for the paying user.

The proposal is intentionally about the protocol surface for premium content, not about mandating a single payment rail or business model. That keeps it flexible, but it also means wallets, clients, and publishers still need to agree on the unlock flow in practice.

## Why It Matters

Without a shared format, every Nostr paywall system becomes its own silo. A common NIP would let one client publish premium content and another client understand that the content is gated, what needs to be paid, and when it should be revealed.

That does not guarantee portability yet. NIP-63 is still a proposal in [PR #2156](https://github.com/nostr-protocol/nips/pull/2156), so implementations can still diverge while the design is under discussion.

## Use Cases

- Subscriber-only articles
- Premium media content
- Pay-per-view events
- Exclusive access to creators

## Tradeoffs

Paywall metadata can be public even when the premium payload is not. That gives clients enough information to present an offer, but it also means the existence of paid content is visible to anyone who can read the event.

Creators also need to think about what happens after unlock. Once plaintext is shown to a paying user, the protocol cannot stop that user from copying it elsewhere.

---

**Primary sources:**
- [NIP-63 Proposal (PR #2156)](https://github.com/nostr-protocol/nips/pull/2156)

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**See also:**
- [NIP-57: Zaps](/en/topics/nip-57/)
