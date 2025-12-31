---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 defines a protocol for connecting Nostr applications to Lightning wallets, enabling payments without exposing wallet credentials to every app.

## How It Works

A wallet (like Zeus) runs an NWC service that listens for payment requests on specific Nostr relays. Apps connect using a connection string that includes the wallet's pubkey and relay information. Payment requests and responses are encrypted between the app and wallet.

## Use Cases

- **Zapping** - Send sats to posts, profiles, or content creators
- **Payments** - Pay Lightning invoices from any Nostr app
- **Subscriptions** - Recurring payments for premium content

## Key Features

- **Budget controls** - Set spending limits per connection
- **Custom relays** - Use your own relay for wallet communication
- **Parallel payments** - Process multiple zaps simultaneously for batch operations

---

**Primary sources:**
- [NIP-47 Specification](https://github.com/nostr-protocol/nips/blob/master/47.md)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Releases](/en/newsletters/2025-12-24-newsletter/#releases)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-57: Zaps](/en/topics/nip-57/)
