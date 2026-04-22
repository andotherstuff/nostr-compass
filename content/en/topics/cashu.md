---
title: "Cashu: Ecash Protocol"
date: 2026-01-28
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu is a Chaumian ecash protocol built on Bitcoin and Lightning. Users hold bearer tokens issued by a mint, then transfer those tokens without exposing the full payment graph to the mint.

## How It Works

Cashu uses blind signatures to issue ecash tokens:

1. **Minting**: Users deposit Bitcoin/Lightning to a mint and receive blinded tokens
2. **Spending**: Tokens can be transferred peer-to-peer without mint involvement
3. **Redemption**: Recipients redeem tokens at the mint for Bitcoin/Lightning

The mint signs blinded secrets, so it can verify tokens later without seeing the original secrets at issuance time. That breaks the direct link between deposit and redemption inside the mint.

## Security And Trust Model

Cashu improves payment privacy, but it is still custodial. A mint can refuse redemptions, go offline, or lose backing funds.

Cashu proofs are bearer instruments. Whoever controls the proof can spend it. That makes proof handling closer to cash than to an account balance: backup, device compromise, or plaintext token leakage all matter immediately.

## Nostr Integration

Cashu integrates with Nostr in several ways:

- **Nutzaps**: Ecash tokens sent as zaps with enhanced privacy
- **Escrow**: HTLC-based payment escrow for services like ridesharing
- **Wallets**: Nostr-native wallets store encrypted Cashu tokens on relays
- **[NIP-87](/en/topics/nip-87/)**: Mint discovery and reviews via Nostr
- **[TollGate](/en/topics/tollgate/)**: Pay-per-use network access protocol that accepts Cashu ecash tokens for connectivity, defined in [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) as of the [v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)

## Tradeoffs

Cashu is fast because transfers happen off-chain and often off-mint until redemption. The tradeoff is interoperability and trust.

In practice, users often need the same mint, or they need a swap or bridge between mints. That is why Nostr applications frequently combine Cashu with mint discovery, wallet sync, and review systems.

---

**Primary sources:**
- [Cashu NUTs Repository](https://github.com/cashubtc/nuts)
- [NUT-00: Cryptography and models](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)
- [NIP-87 Specification](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Mentioned in:**
- [Newsletter #7](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #11](/en/newsletters/2026-02-25-newsletter/)
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/#tollgate-v010-stabilizes-pay-per-use-internet-over-nostr-and-cashu)

**See also:**
- [NIP-60: Cashu Wallet](/en/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/en/topics/nip-87/)
- [TollGate](/en/topics/tollgate/)
