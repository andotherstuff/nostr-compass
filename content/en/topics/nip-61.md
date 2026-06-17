---
title: "NIP-61: Nutzaps"
date: 2026-06-17
draft: false
categories:
  - Zaps
  - Ecash
---

NIP-61 defines "nutzaps", peer-to-peer Cashu ecash payments delivered as Nostr events. A sender publishes a P2PK-locked Cashu token addressed to the recipient's Nostr key, and the recipient redeems it from the mint at their convenience. The proofs themselves carry the value, so a NIP-61 payment lands as a self-contained token that the recipient can redeem on their own schedule, with no Lightning channel or interactive handshake required.

## How it works

NIP-61 builds on two existing primitives: [NIP-60](/en/topics/nip-60/) Cashu wallets and Cashu's P2PK locks. The flow uses three event kinds.

**Mint recommendation (kind 10019):** a replaceable event the recipient publishes to announce which mints they accept nutzaps from and the Cashu public key used to lock proofs to them. Senders read this before sending so the locked token is one the recipient can redeem.

**Nutzap event (kind 9321):** the payment itself. It carries the Cashu proofs (P2PK-locked to the recipient's nutzap pubkey from kind 10019), the mint URL, optional `e` and `a` tags identifying the zapped note, and a `p` tag for the recipient. The recipient receives it through normal Nostr subscriptions, unlocks the proofs with the corresponding private key, and either holds them in their NIP-60 wallet or melts them to Lightning.

**Nutzap info (kind 7375):** cached state with the same shape as NIP-60 token events, recording redeemed nutzap proofs so the wallet does not double-count them on resync.

## Tradeoffs and trust model

A nutzap is a self-contained ecash token. As long as the recipient can later contact the mint, they can redeem the payment. The mint itself is the trusted custodian, the same trust model as NIP-60, and that custody choice is the explicit price of offline-capable, instant-finality micropayments. NIP-57 zaps require the receiver to run (or be hosted on) a Lightning node with a LNURL endpoint that accepts incoming HTLCs in real time. Phones with no Lightning channel, users behind firewalls, and recipients who happen to be offline all sit outside that model.

The kind 10019 advertisement is the social-layer trust gate. The sender chooses one of the recipient's accepted mints, which keeps the recipient's redemption path predictable. A sender who picks a mint outside the recipient's set risks an unredeemable token, so wallets read kind 10019 first.

## Workflow

1. Recipient publishes a kind 10019 announcing accepted mints and a nutzap pubkey
2. Sender reads kind 10019, mints proofs at one of the listed mints, and P2PK-locks them to the recipient's nutzap pubkey
3. Sender publishes a kind 9321 with the locked proofs, mint URL, and target tags
4. Recipient receives the kind 9321 via their normal Nostr subscription
5. Recipient unlocks the proofs using their nutzap private key and either holds them in their NIP-60 wallet or melts to Lightning

## Example nutzap event

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1750162800,
  "kind": 9321,
  "tags": [
    ["proof", "{\"amount\":21,\"secret\":\"...\",\"C\":\"...\",\"id\":\"...\"}"],
    ["u", "https://mint.example.com"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3"],
    ["p", "c5d8a4e3b2a1f0e9d8c7b6a5949382716050403020100ffeeddccbbaa99887766"]
  ],
  "content": "Great post!",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

## Implementations

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) ships nutzap rendering with per-mint balance views as part of its NIP-60/NIP-61 wallet surface ([PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075))

---

**Primary sources:**
- [NIP-61 Specification](https://github.com/nostr-protocol/nips/blob/master/61.md)
- [Amethyst PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075) - NIP-60 Cashu wallet and NIP-61 nutzap support

**Mentioned in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**See also:**
- [NIP-57: Zaps](/en/topics/nip-57/)
- [NIP-60: Cashu Wallet](/en/topics/nip-60/)
- [Cashu](/en/topics/cashu/)
