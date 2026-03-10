---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
draft: false
categories:
  - Wallet
  - Ecash
---

NIP-60 defines how Cashu-based ecash wallets operate within Nostr. Wallet information is stored on relays, enabling portable wallets that work across different applications without requiring separate accounts.

## How It Works

NIP-60 uses three core event types stored on relays, plus one optional helper event for pending quotes:

**Wallet Event (kind 17375):** A replaceable event containing encrypted wallet configuration, including mint URLs and a private key for receiving payments. This key is separate from the user's Nostr identity key.

**Token Events (kind 7375):** Store encrypted unspent Cashu proofs. When proofs are spent, the client deletes the old event and creates a new one with any remaining proofs.

**Spending History (kind 7376):** Optional transaction records showing fund movements, with encrypted content and references to created/destroyed token events.

**Quote Events (kind 7374):** Optional encrypted state for pending mint quotes. The spec recommends short-lived events with expiration tags, mainly for cases where local state is not enough.

## State Model

NIP-60 is about wallet state synchronization, not about the act of receiving money. The wallet event tells a client which mints and wallet key to use, while token events are the actual balance state because they contain the unspent proofs.

That distinction matters for interoperability. Two clients can show the same wallet only if they interpret token rollover the same way: spend proofs, publish replacement proofs, and delete the spent token event through [NIP-09](/en/topics/nip-09/) so other clients do not keep counting spent proofs as balance.

## Why It Matters

- **Ease of use** - New users can receive ecash immediately without external account setup
- **Interoperability** - Wallet data follows users across different Nostr applications
- **Privacy** - All wallet data is encrypted to the user's keys
- **Proof management** - Tracks wallet state transitions so clients can converge on the same balance

## Interop Notes

Clients first look for wallet relay information through kind 10019 and fall back to the user's [NIP-65](/en/topics/nip-65/) relay list if no dedicated wallet relay list is present. That fallback is useful, but it also means wallet portability still depends on relays actually storing and serving the encrypted wallet events.

The spec also requires the wallet private key to stay separate from the user's Nostr identity key. That keeps wallet receipt handling isolated from the main signing key and reduces the chance that one key gets reused for two different purposes.

## Workflow

1. Client fetches wallet configuration from wallet relays or the user's relay list
2. Token events are loaded and decrypted to get available funds
3. Spending creates new token events and deletes old ones
4. Optional history events record transactions for user reference

---

**Primary sources:**
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #11: NIP Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**See also:**
- [NIP-57: Zaps](/en/topics/nip-57/)
- [NIP-09: Event Deletion Request](/en/topics/nip-09/)
- [NIP-47: Nostr Wallet Connect](/en/topics/nip-47/)
