---
title: "NIP-57: Zaps"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 defines zaps, a way to send Lightning payments to Nostr users and content with cryptographic proof that the payment occurred.

## How It Works

1. Client fetches recipient's Lightning address from their kind 0 profile
2. Client requests an invoice from the recipient's LNURL server, including a zap request event
3. User pays the invoice
4. LNURL server publishes a kind 9735 zap receipt to Nostr relays
5. Clients display the zap on the recipient's content

## Zap Request (kind 9734)

The zap request is a signed event that proves who sent the zap and to what content. It includes:
- `p` tag with recipient pubkey
- `e` tag with event being zapped (optional)
- `amount` tag in millisatoshis
- `relays` tag listing where to publish the receipt

## Zap Receipt (kind 9735)

Published by the LNURL server after payment confirmation. Contains:
- The original zap request in a `description` tag
- `bolt11` tag with the paid invoice
- `preimage` tag proving payment

---

**Primary sources:**
- [NIP-57 Specification](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)

**See also:**
- [NIP-47: Nostr Wallet Connect](/en/topics/nip-47/)
