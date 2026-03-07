---
title: "NIP-15: Nostr Marketplace"
date: 2026-01-28
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15 defines a protocol for decentralized marketplaces on Nostr, enabling merchants to list products and buyers to make purchases using Bitcoin and Lightning.

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

Payments and shipping are also only partly standardized. A client can understand stalls and products and still need custom logic for invoices, order state, or delivery tracking.

## Implementation Status

- **Plebeian Market** - Full-featured NIP-15 marketplace
- **Shopstr** - Permissionless Bitcoin commerce
- **Amethyst** - Integrated product listings in social feed

---

**Primary sources:**
- [NIP-15 Specification](https://github.com/nostr-protocol/nips/blob/master/15.md)

**Mentioned in:**
- [Newsletter #7: January 2024 Protocol Hardening](/en/newsletters/2026-01-28-newsletter/#january-2024-protocol-hardening)

**See also:**
- [NIP-44: Encrypted Payloads](/en/topics/nip-44/)
- [NIP-57: Lightning Zaps](/en/topics/nip-57/)
