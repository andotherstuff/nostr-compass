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

A validating client should check four things before displaying a receipt as a zap: the receipt's signature matches the `nostrPubkey` advertised in the recipient's LNURL response, the `bolt11` invoice amount matches the `amount` tag in the embedded zap request, the invoice's description hash commits to the stringified zap request, and the `preimage` hashes to the invoice's `payment_hash`. Clients that render tallied zap counts without performing these checks are trivially spoofable by an attacker who publishes forged kind `9735` events.

## Private and Anonymous Zaps

Private zaps add a confidentiality layer on top. A sender can encrypt the zap request's `content` for the recipient and include an `anon` tag on the outer request, so the relay network sees the payment target but cannot read the attached note. An anonymous zap goes one step further: the client generates a fresh ephemeral keypair for the zap request itself, so the receipt still proves a payment happened but the recipient cannot link the zap back to the sender's long-lived pubkey.

## Zap Goals and Splits

NIP-57 underpins the zap-goal system specified in [NIP-75](/en/topics/nip-75/). A goal is a kind `9041` event that declares a target amount and a relay set where receipts count, and clients tally goal progress by summing validated `bolt11` amounts of matched kind `9735` events.

Zap splits, defined in an appendix to the NIP, let a recipient publish a kind `0` profile with multiple weighted `zap` tags so a single zap payment is divided among several pubkeys atomically. [Amethyst](https://github.com/vitorpamplona/amethyst), [Damus](https://github.com/damus-io/damus), and [noStrudel](https://github.com/hzrd149/nostrudel) implement split-paying end-to-end.

## Current Implementation and Proposal Work

[Earthly 0.0.9](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.0.9) repaired zap-request construction and receipt handling for collaborative map entities. Separately, [PR #2421](https://github.com/nostr-protocol/nips/pull/2421) proposes BOLT12 zaps with signed intent events and payer proofs, allowing clients to verify settlement without a recipient-operated receipt publisher.

---

**Primary sources:**
- [NIP-57 Specification](https://github.com/nostr-protocol/nips/blob/master/57.md)
- [PR #2421](https://github.com/nostr-protocol/nips/pull/2421) - BOLT12 zap proposal
- [Earthly 0.0.9](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.0.9) - Client implementation fixes

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#amethyst-android)
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #19: NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/#nip-deep-dive-nip-57-zaps)
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/en/newsletters/2026-06-17-newsletter/#amethyst-v1-12-0-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #31: Wired and TAO add NIP-57 creator revenue sharing](/en/newsletters/2026-07-15-newsletter/#wired-and-tao-add-nip-57-creator-revenue-sharing)
- [Newsletter #33: Tagged releases](/en/newsletters/2026-07-29-newsletter/#tagged-releases)
- [Newsletter #33: Protocol work and NIP updates](/en/newsletters/2026-07-29-newsletter/#protocol-and-spec-work)
- [Newsletter #34: BOLT12 zap proposal](/en/newsletters/2026-08-05-newsletter/#payments-and-wallet-connections)

**See also:**
- [NIP-47: Nostr Wallet Connect](/en/topics/nip-47/)
- [NIP-75: Zap Goals](/en/topics/nip-75/)
- [NIP-53: Live Activities](/en/topics/nip-53/)
