---
title: "MIP-05: Privacy-Preserving Push Notifications"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05 defines a protocol for push notifications that maintain user privacy, solving the problem that traditional push systems require servers to know device tokens and user identities.

## How It Works

- Device tokens are encrypted with ECDH+HKDF and ChaCha20-Poly1305
- Ephemeral keys prevent correlation between notifications
- A three-event gossip protocol (kinds 447-449) synchronizes encrypted tokens across group members
- Decoy tokens via NIP-59 gift wrapping hide group sizes

## Privacy Guarantees

- Push notification servers cannot identify users
- Group membership is not revealed by notification patterns
- Device tokens cannot be correlated across messages

## Event Kinds

- **Kind 447**: Encrypted device token publication
- **Kind 448**: Token synchronization request
- **Kind 449**: Token synchronization response

---

**Primary sources:**
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [Marmot Protocol](/en/topics/marmot/)
- [NIP-59: Gift Wrap](/en/topics/nip-59/)
