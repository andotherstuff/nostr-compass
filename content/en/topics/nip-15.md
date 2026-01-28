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

## Key Features

- **Decentralized**: No central marketplace operator
- **Interoperable**: Any NIP-15 client can browse any merchant
- **Private**: Orders are encrypted between buyer and seller
- **Bitcoin-native**: Lightning payments built-in

## Implementations

- **Plebeian Market** - Full-featured NIP-15 marketplace
- **Shopstr** - Permissionless Bitcoin commerce
- **Amethyst** - Integrated product listings in social feed

## Related

- [NIP-44](/en/topics/nip-44/) - Encrypted messages for orders
- [NIP-57](/en/topics/nip-57/) - Lightning Zaps
