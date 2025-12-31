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

NIP-60 uses three types of events stored on relays:

**Wallet Event (kind 17375):** A replaceable event containing encrypted wallet configuration, including mint URLs and a private key for receiving payments. This key is separate from the user's Nostr identity key.

**Token Events (kind 7375):** Store encrypted unspent Cashu proofs. When proofs are spent, the client deletes the old event and creates a new one with any remaining proofs.

**Spending History (kind 7376):** Optional transaction records showing fund movements, with encrypted content and references to created/destroyed token events.

## Key Features

- **Ease of use** - New users can receive ecash immediately without external account setup
- **Interoperability** - Wallet data follows users across different Nostr applications
- **Privacy** - All wallet data is encrypted to the user's keys
- **Proof management** - Tracks which token events were spent to prevent double-spending

## Workflow

1. Client fetches wallet configuration from relays
2. Token events are loaded and decrypted to get available funds
3. Spending creates new token events and deletes old ones
4. Optional history events record transactions for user reference

---

**Primary sources:**
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-57: Zaps](/en/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/en/topics/nip-47/)
