---
title: "NIP-69: Peer-to-Peer Trading"
date: 2025-12-17
draft: false
categories:
  - Trading
  - Protocol
---

NIP-69 defines a protocol for peer-to-peer trading over Nostr, creating a unified order book across multiple platforms rather than fragmented liquidity pools.

## How It Works

NIP-69 uses addressable kind 38383 events for buy and sell orders. The addressable format matters because an order can move through several states over time while keeping the same logical identity through its `d` tag.

## Order Structure

Orders use tags to specify trade parameters:

- `d` - Order ID
- `k` - Order type (buy/sell)
- `f` - Fiat currency (ISO 4217 code)
- `amt` - Bitcoin amount in satoshis
- `fa` - Fiat amount
- `pm` - Payment methods accepted
- `premium` - Price premium/discount percentage
- `network` - Bitcoin network (mainnet, testnet, signet, regtest)
- `layer` - Settlement layer (onchain, lightning, liquid)
- `expiration` - When the order expires

## Order Lifecycle

Orders progress through statuses:
- `pending` - Open and available for matching
- `in-progress` - Trade initiated with counterparty
- `success` - Trade completed
- `canceled` - Withdrawn by maker
- `expired` - Past expiration time

The spec distinguishes two time limits. `expires_at` marks when a pending order should stop being considered open, while `expiration` gives relays a timestamp they can use with [NIP-40](/en/topics/nip-40/) to remove stale order events entirely.

## Why It Matters

NIP-69 is an interoperability play. Mostro, lnp2pBot, RoboSats, Peach, and other P2P trading systems can expose orders into one shared event format instead of keeping liquidity trapped inside separate apps.

The optional `g` tag also makes local, face-to-face trading possible without changing the rest of the order schema. That is useful because local cash trades need geographic filtering, while online Lightning trades do not.

## Security and Trust

The `bond` tag specifies a security deposit that both parties must pay, providing protection against abandonment or fraud.

That does not remove counterparty risk. Payment disputes, fiat fraud, reputation, and custody rules still live at the application layer. NIP-69 standardizes order publication, not dispute resolution.

---

**Primary sources:**
- [NIP-69 Specification](https://github.com/nostr-protocol/nips/blob/master/69.md)
- [Mostro Protocol Specification](https://mostro.network/protocol/)

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)

**See also:**
- [NIP-40: Expiration Timestamp](/en/topics/nip-40/)
