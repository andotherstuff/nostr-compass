---
title: "NIP-69: Peer-to-Peer Trading"
date: 2025-12-17
draft: false
categories:
  - Trading
  - Protocol
---

NIP-69 defines a protocol for peer-to-peer trading over Nostr, creating a unified order book across multiple platforms rather than fragmented liquidity pools.

## Event Kind

- **Kind 38383** - P2P order events

## Order Structure

Orders use tags to specify trade parameters:

- `d` - Order ID
- `k` - Order type (buy/sell)
- `f` - Fiat currency (ISO 4217 code)
- `amt` - Bitcoin amount in satoshis
- `fa` - Fiat amount
- `pm` - Payment methods accepted
- `premium` - Price premium/discount percentage
- `network` - Settlement layer (onchain, lightning, liquid)
- `expiration` - When the order expires

## Order Lifecycle

Orders progress through statuses:
- `pending` - Open and available for matching
- `in-progress` - Trade initiated with counterparty
- `success` - Trade completed
- `canceled` - Withdrawn by maker
- `expired` - Past expiration time

## Security

The `bond` tag specifies a security deposit that both parties must pay, providing protection against abandonment or fraud.

---

**Primary sources:**
- [NIP-69 Specification](https://github.com/nostr-protocol/nips/blob/master/69.md)

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)
