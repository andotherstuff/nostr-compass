---
title: "Gamma Markets"
date: 2026-07-15
draft: false
categories:
  - Commerce
  - Marketplace
  - Protocol
---

Gamma Markets is a set of e-commerce conventions built directly on top of [NIP-99](/en/topics/nip-99/) classified listings, developed collaboratively by a working group of Nostr marketplace developers: the teams behind Shopstr, Cypher, Plebeian Market, and Conduit Market. It fills in the shipping, order-flow, collection, and review conventions that NIP-99 itself leaves undefined.

## How It Works

Gamma Markets adds five event kinds around NIP-99's existing kind `30402` listing event, without changing that event's shape:

- **Kind 30405** - product collections, grouping multiple listings together via `a` tags
- **Kind 30406** - shipping options, with per-country pricing and optional weight- or distance-based cost rules
- **Kind 16** - order messages: creation (type 1), payment requests (type 2), status updates (type 3), and shipping updates (type 4)
- **Kind 14** - general buyer/merchant communication
- **Kind 17** - payment receipts
- **Kind 31555** - product reviews, addressed to a specific seller pubkey and listing `d` tag

A merchant's payment preferences are declared via a `payment_preference` tag on their kind `0` profile metadata, and clients discover compatible apps through [NIP-89](/en/topics/nip-89/) application recommendations. Order communication builds on [NIP-17](/en/topics/nip-17/) private messages, with no new encryption scheme of its own.

The spec's defining design choice is that nothing cascades: a listing that belongs to a collection, or that uses a shipping option, references it explicitly with an `a` tag instead of inheriting its parent's settings automatically. That is a deliberate departure from the older [NIP-15](/en/topics/nip-15/) stall model, where a product silently inherited its stall's currency and shipping table.

### Example: order creation (kind 16, type 1)

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

## Why It Matters

NIP-99 alone standardizes only the listing itself, a signed, addressable classified ad. Before Gamma Markets, every client building real e-commerce on NIP-99 invented its own private conventions for shipping, checkout, and reviews, which meant two NIP-99-compliant clients could each render a listing correctly but had no shared way to complete an order between them. Gamma Markets closes that gap without touching the NIP-99 listing format itself, so existing NIP-99 listings remain valid without modification.

## Implementations

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Nostr marketplace, one of the four projects that authored the spec
- [Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) - marketplace protocol building its own order-state and checkout flow in the same design space

---

**Primary sources:**
- [Gamma Markets spec repository](https://github.com/GammaMarkets/market-spec)
- [NIP-99 e-commerce use case extension, PR #1784](https://github.com/nostr-protocol/nips/pull/1784) - merged link from the canonical NIP-99 document to the Gamma Markets spec

**Mentioned in:**
- [Newsletter #31: NIP Deep Dive: NIP-99 and the Gamma Markets commerce extension](/en/newsletters/2026-07-15-newsletter/#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)

**See also:**
- [NIP-99: Classified Listings](/en/topics/nip-99/)
- [NIP-15: Nostr Marketplace](/en/topics/nip-15/)
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
