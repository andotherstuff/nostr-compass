---
title: "Cashu: Ecash Protocol"
date: 2026-01-28
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu is a Chaumian ecash protocol built on Bitcoin and Lightning Network, enabling private, instant, and low-fee payments through cryptographic tokens.

## How It Works

Cashu uses blind signatures to create untraceable ecash tokens:

1. **Minting**: Users deposit Bitcoin/Lightning to a mint and receive blinded tokens
2. **Spending**: Tokens can be transferred peer-to-peer without mint involvement
3. **Redemption**: Recipients redeem tokens at the mint for Bitcoin/Lightning

The mint cannot link deposits to redemptions due to the blinding process, providing strong privacy guarantees.

## Key Properties

- **Privacy**: Mint cannot track token transfers between users
- **Instant**: Transfers happen offline, no blockchain confirmation needed
- **Low-fee**: No on-chain fees for token transfers
- **Custodial**: Users trust the mint to honor redemptions

## Nostr Integration

Cashu integrates with Nostr in several ways:

- **Nutzaps**: Ecash tokens sent as zaps with enhanced privacy
- **Escrow**: HTLC-based payment escrow for services like ridesharing
- **Wallets**: Nostr-native wallets store encrypted Cashu tokens on relays
- **[NIP-87](/en/topics/nip-87/)**: Mint discovery and reviews via Nostr

## Trust Model

Unlike self-custodial Bitcoin, Cashu requires trusting mint operators. Users should:
- Use reputable, well-reviewed mints
- Keep small balances appropriate to the trust level
- Understand mints can exit-scam or go offline, taking funds with them

## Related

- [NIP-87](/en/topics/nip-87/) - Cashu Mint Recommendations
- [NIP-60](/en/topics/nip-60/) - Nostr Wallet
