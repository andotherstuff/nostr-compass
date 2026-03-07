---
title: "MIP-05: Privacy-Preserving Push Notifications"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05 defines a push-notification protocol for Marmot clients that tries to preserve privacy in a setting where ordinary mobile push systems usually expose device tokens and account relationships.

## How It Works

- Device tokens are encrypted with ECDH+HKDF and ChaCha20-Poly1305
- Ephemeral keys prevent correlation between notifications
- A three-event gossip protocol (kinds 447-449) synchronizes encrypted tokens across group members
- Decoy tokens via NIP-59 gift wrapping hide group sizes

## Privacy Model

- Push notification servers cannot identify users
- Group membership is not revealed by notification patterns
- Device tokens cannot be correlated across messages

The concrete improvement is that the push provider sees opaque delivery tokens, not a direct map from group member to device. That does not make notifications anonymous in an absolute sense, but it reduces how much the push layer learns by default.

## Event Kinds

- **Kind 447**: Encrypted device token publication
- **Kind 448**: Token synchronization request
- **Kind 449**: Token synchronization response

## Tradeoffs

MIP-05 adds privacy by adding coordination work. Clients have to synchronize encrypted token state across group members, and decoy tokens increase message overhead on purpose.

That means implementers need to balance delivery reliability against metadata protection. The protocol is useful precisely because it treats push as a privacy problem, not just a transport convenience.

---

**Primary sources:**
- [MIP-05 Specification](https://github.com/marmot-protocol/marmot/blob/master/05.md)
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)
- [White Noise v0.2.1 release](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [Marmot Protocol](/en/topics/marmot/)
- [NIP-59: Gift Wrap](/en/topics/nip-59/)
