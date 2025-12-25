---
title: "Marmot Protocol"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot is a protocol for end-to-end encrypted group messaging built on Nostr, using the Message Layer Security (MLS) standard for forward secrecy and post-compromise security.

## How It Works

Marmot extends Nostr with MLS-based encryption for group chats. Unlike NIP-17 DMs which are one-to-one, Marmot handles secure group communication where members can join and leave while maintaining encryption guarantees.

## Key Features

- Forward secrecy and post-compromise security via MLS
- Group key management for dynamic membership
- Privacy-preserving push notifications via MIP-05

---

**Primary sources:**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)

**See also:**
- [MIP-05: Privacy-Preserving Push Notifications](/en/topics/mip-05/)
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
- [NIP-59: Gift Wrap](/en/topics/nip-59/)
