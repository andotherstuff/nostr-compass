---
title: "NIP-57: Zaps"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 defines zaps, a way to attach Lightning payments to Nostr identities and content. It standardizes both the request for a zap-enabled invoice and the receipt event that wallets publish after payment.

## How It Works

1. Client discovers the recipient's LNURL endpoint from profile metadata or a `zap` tag on the target event.
2. Client sends a signed kind `9734` zap request to the recipient's LNURL callback, not to relays.
3. User pays the invoice.
4. The recipient's wallet server publishes a kind `9735` zap receipt to the relays listed in the zap request.
5. Clients validate and display the zap.

## Zap Request (kind 9734)

The zap request is a signed event that identifies the payer and the intended target. It usually includes:

- `p` tag with recipient pubkey
- `e` tag with event being zapped (optional)
- `amount` tag in millisatoshis
- `relays` tag listing where to publish the receipt

Addressable content can use an `a` tag instead of, or alongside, an `e` tag. The optional `k` tag records the target kind.

## Zap Receipt (kind 9735)

Published by the recipient's wallet server after payment confirmation. It contains:

- The original zap request in a `description` tag
- `bolt11` tag with the paid invoice
- `preimage` tag proving payment

Clients should validate the receipt against the recipient's LNURL `nostrPubkey`, the invoice amount, and the original zap request. A receipt without that validation is only a claim.

## Trust and Tradeoffs

Zaps are useful because they make payments visible inside the social graph, but the receipt is still created by the recipient's wallet infrastructure. The spec itself notes that a zap receipt is not a universal proof of payment. It is best understood as a wallet-signed statement that an invoice tied to a zap request was paid.

---

**Primary sources:**
- [NIP-57 Specification](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#amethyst-android)
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)

**See also:**
- [NIP-47: Nostr Wallet Connect](/en/topics/nip-47/)
