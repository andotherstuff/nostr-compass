---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 defines gift wrapping, a technique for hiding the sender of an event from relays and observers by wrapping it in layers of encryption with a disposable signing identity.

## Structure

A gift-wrapped event has three layers:

1. **Rumor** - The original event without a signature. Cannot be published to relays directly.
2. **Seal** (kind 13) - The rumor encrypted to the recipient, **signed by the real sender**. This proves authorship.
3. **Gift Wrap** (kind 1059) - The seal encrypted to the recipient, signed by a random one-time key.

## Important: Not Deniable

A common misconception is that gift wrap provides deniability. It does not. The seal layer IS signed by the real author. Recipients have cryptographic proof of who sent the message and could construct a zero-knowledge proof revealing the sender without exposing their own private key.

What gift wrap provides is **sender privacy from observers**: relays and third parties cannot determine who sent the message. But the recipient always knows.

## Use Cases

- Private direct messages (NIP-17)
- Friends-only notes (NIP-FR proposal)
- Push notification payloads (NIP-9a proposal)
- Any scenario requiring sender privacy from the network

---

**Primary sources:**
- [NIP-59 Specification](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Mentioned in:**
- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - Deep dive on gift wrap layers
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
