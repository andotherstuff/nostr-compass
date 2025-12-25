---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 defines gift wrapping, a technique for hiding the sender of an event by wrapping it in layers of encryption with a disposable identity.

## Structure

A gift-wrapped event has three layers:

1. **Rumor** - The original unsigned event content
2. **Seal** (kind 13) - The rumor encrypted to the recipient, signed by the real sender
3. **Gift Wrap** (kind 1059) - The seal encrypted to the recipient, signed by a random disposable key

The outer layer uses a random keypair generated just for this message, so observers cannot link it to the sender.

## Why Three Layers?

- The **rumor** contains the actual content
- The **seal** proves the real sender (only visible to recipient)
- The **gift wrap** hides the sender from relays and observers

## Deletion Support

Gift wrap events can now be deleted via NIP-09/NIP-62 deletion requests. This was added to allow users to remove wrapped messages from relays.

## Use Cases

- Private direct messages (NIP-17)
- Anonymous tips or whistleblowing
- Any scenario where sender privacy is important

---

**Primary sources:**
- [NIP-59 Specification](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**See also:**
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
