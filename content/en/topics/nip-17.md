---
title: "NIP-17: Private Direct Messages"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17 defines private direct messages using NIP-59 gift wrapping for sender privacy. Unlike NIP-04 DMs which expose the sender, NIP-17 messages hide who sent the message. The recipient remains visible in the outer gift wrap.

## How It Works

Messages are wrapped in multiple encryption layers:
1. The actual message content (kind 14)
2. A seal that encrypts the content to the recipient
3. A gift wrap that hides the sender's identity

The outer gift wrap uses a random, disposable keypair so relays and observers cannot determine who sent the message.

## Message Structure

- **Kind 14** - The actual DM content (inside the seal)
- Uses NIP-44 encryption for the content
- Supports reactions (kind 7) within DM conversations

## Privacy Guarantees

- Relays cannot see the sender (hidden by gift wrap's disposable keypair)
- Recipient is visible (in the `p` tag of the gift wrap)
- Message timestamps are randomized within a window
- No visible threading or conversation grouping on the relay

## Comparison to NIP-04

NIP-04 DMs encrypt content but leave metadata visible:
- Sender pubkey is public
- Recipient pubkey is in the `p` tag
- Timestamps are exact

NIP-17 hides the sender at the cost of more complex implementation.

---

**Primary sources:**
- [NIP-17 Specification](https://github.com/nostr-protocol/nips/blob/master/17.md)

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)

**See also:**
- [NIP-59: Gift Wrap](/en/topics/nip-59/)
