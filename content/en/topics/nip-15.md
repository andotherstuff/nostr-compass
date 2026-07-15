---
title: "NIP-15: Nostr Marketplace"
date: 2026-01-28
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15 defines a protocol for decentralized marketplaces on Nostr, enabling merchants to list products and buyers to make purchases using Bitcoin and Lightning. It is legacy at this point: the clients that once ran on it, Shopstr among them, have moved to [NIP-99](/en/topics/nip-99/) classified listings plus the [Gamma Markets](/en/topics/gamma-markets/) commerce conventions as the active spec, since NIP-99's single addressable listing event replaces the stall-plus-product model below without requiring a stall to be created first.

## How It Works

### Merchant Stalls (Kind 30017)

Merchants create stalls as addressable events:

```json
{
  "kind": 30017,
  "tags": [
    ["d", "my-stall"],
    ["name", "Bob's Electronics"],
    ["description", "Quality used electronics"],
    ["currency", "sat"],
    ["shipping", "{...shipping options...}"]
  ]
}
```

### Products (Kind 30018)

Products are listed within stalls:

```json
{
  "kind": 30018,
  "tags": [
    ["d", "product-123"],
    ["stall_id", "my-stall"],
    ["name", "Raspberry Pi 4"],
    ["price", "50000"],
    ["quantity", "5"],
    ["images", "https://..."]
  ]
}
```

## Purchase Flow

1. Buyer browses products across multiple stalls
2. Buyer sends encrypted order message to merchant
3. Merchant responds with Lightning invoice
4. Buyer pays invoice
5. Merchant ships product

## Why It Matters

- **Decentralized**: No central marketplace operator
- **Interoperable**: Any NIP-15 client can browse any merchant
- **Private**: Orders are encrypted between buyer and seller
- **Bitcoin-native**: Lightning payments built-in

The practical gain is portability. A merchant can publish catalog data once and let multiple clients render it, instead of being locked into one marketplace front end.

## Tradeoffs

NIP-15 standardizes listings, not trust. Buyers still need to decide whether a merchant is legitimate, whether inventory is real, and how disputes get handled. The protocol gives common data structures and message flow, but reputation and fulfillment remain application-level problems.

Payments and shipping are also only partly standardized. A client can understand stalls and products and still need custom logic for invoices, order state, or delivery tracking. In practice, that gap is what pushed marketplace developers toward NIP-99 plus Gamma Markets instead of continuing to extend NIP-15's stall model.

## Implementation Status

- **Plebeian Market** - Full-featured NIP-15 marketplace
- **Shopstr** - Permissionless Bitcoin commerce; has since moved its active listings to NIP-99
- **Amethyst** - Integrated product listings in social feed

---

**Primary sources:**
- [NIP-15 Specification](https://github.com/nostr-protocol/nips/blob/master/15.md)

**Mentioned in:**
- [Newsletter #7: January 2024 Protocol Hardening](/en/newsletters/2026-01-28-newsletter/#january-2024-protocol-hardening)
- [Newsletter #31: NIP Deep Dive: NIP-99 and the Gamma Markets commerce extension](/en/newsletters/2026-07-15-newsletter/#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)

**See also:**
- [NIP-44: Encrypted Payloads](/en/topics/nip-44/)
- [NIP-57: Lightning Zaps](/en/topics/nip-57/)
- [NIP-99: Classified Listings](/en/topics/nip-99/) - the active spec that superseded NIP-15's stall model
- [Gamma Markets](/en/topics/gamma-markets/)
