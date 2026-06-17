---
title: "CLINK: Common Lightning Interface for Nostr Keys"
date: 2026-06-17
draft: false
categories:
  - Payments
  - Lightning
---

CLINK (Common Lightning Interface for Nostr Keys) is a proposed payment-request format that lets a sender pay any Nostr-keyed identity using a single noffer interface. A CLINK noffer encodes the recipient's Nostr public key plus enough routing metadata for the sender's wallet to construct a Lightning payment, on-chain payment, or future settlement primitive that resolves to the recipient. The recipient publishes one noffer per identity, and senders pay it without knowing whether the receiving wallet settles over Lightning, on-chain, or another rail.

## How it works

A CLINK noffer is a structured payment request that the sender's wallet decodes into a concrete payment instruction. The noffer carries:

- The recipient's Nostr public key as the canonical identity root
- One or more payment endpoints (Lightning node URI, on-chain address derivation hint, future rails)
- Optional metadata for the payment (memo, amount, expiry)
- A signature from the recipient binding the noffer to their Nostr identity

A sending wallet that supports CLINK reads the noffer, picks the rail it can serve (a Lightning-only wallet pays the Lightning endpoint, a multi-rail wallet picks the cheapest path), and submits the payment. The recipient's wallet acknowledges receipt by publishing or fetching the corresponding completion event, with the Nostr public key acting as the durable identity across rails.

## Why a Nostr-keyed interface

LNURL and BOLT-12 already exist as Lightning payment-request formats, and Bitcoin has a well-known address format for on-chain settlement. CLINK does not replace either. It adds a Nostr-key-rooted layer so a sender can address a recipient by their Nostr identity and let the wallet resolve which underlying rail to use. A user who switches Lightning providers, opens a new mint, or migrates their on-chain wallet republishes their noffer with the same Nostr key, and senders do not need to update their address books.

For Zeus Pay (which generates a CLINK noffer for every account), this means a sender can pay any Zeus user by Nostr key alone. For Amethyst's on-chain zap driver, the CLINK verification state machine confirms that the signed noffer on chain matches the Nostr pubkey claimed in the zap request, closing a forgery path against unsigned on-chain zaps.

## Implementations

- [Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) ships CLINK noffer payment support, with Zeus Pay generating a CLINK noffer for every account so a sender can pay any Zeus user by Nostr key alone
- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) ships a CLINK driver for on-chain zap verification with a verification state machine and reverify driver ([PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039), [PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177), [PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182))

---

**Primary sources:**
- [Zeus v13.1.0-rc1 release notes](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) - CLINK noffer ship
- [Amethyst PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039) - NIP-BC on-chain zaps verification state machine and reverify driver
- [Amethyst PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177) - Implement CLINK (Common Lightning Interface for Nostr Keys)
- [Amethyst PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182) - Add kotlinx-serialization support for CLINK protocol DTOs

**Mentioned in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #27: Zeus v13.1.0-rc1 ships CLINK noffers and queue-less NWC](/en/newsletters/2026-06-17-newsletter/#zeus-v1310-rc1-ships-clink-noffers-and-queue-less-nwc)

**See also:**
- [NIP-57: Zaps](/en/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/en/topics/nip-47/)
