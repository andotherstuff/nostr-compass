---
title: "Concord Protocol"
date: 2026-07-15
draft: false
categories:
  - Protocol
  - Messaging
---

Concord Protocol is [Vector](https://github.com/VectorPrivacy/Vector)'s in-house replacement for [Marmot](/en/topics/marmot/) (MLS-over-Nostr) as the transport for its Group Chats feature, introduced in Vector v0.4.0. It is proprietary to Vector rather than a shared spec other clients implement.

## How It Works

Concord Protocol was built by the Vector team to replace Marmot as the default Group Chats transport starting in [v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0). Existing Marmot group history does not carry over to Concord groups; Vector's release notes tell users to back up any Marmot group data before upgrading. The full technical design has not been separately published as a standalone spec document; what is public so far comes from the v0.4.0 release notes and changelog.

## Why It Matters

Vector's move is notable mainly for what it is not: Marmot is Nostr's most widely adopted MLS-based group-messaging design, with [MDK](https://github.com/marmot-protocol/mdk), [White Noise](https://github.com/marmot-protocol/whitenoise), Amethyst, and others building on it. Vector stepping away from Marmot for its own Concord Protocol, in the same week MDK shipped a hardening release, is a real fork in direction rather than a routine feature update, and worth tracking against how much of the rest of the group-chat ecosystem stays consolidated around Marmot.

## Implementations

- [Vector](https://github.com/VectorPrivacy/Vector) - single-binary, privacy-first Nostr messenger; the only known Concord Protocol implementation

---

**Primary sources:**
- [Vector v0.4.0 release notes](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)

**Mentioned in:**
- [Newsletter #31: Vector v0.4.0 moves Group Chats from Marmot to a custom Concord Protocol](/en/newsletters/2026-07-15-newsletter/#vector-v040-moves-group-chats-from-marmot-to-a-custom-concord-protocol)

**See also:**
- [Marmot Protocol](/en/topics/marmot/)
- [MLS (Message Layer Security)](/en/topics/mls/)
- [NIP-46: Nostr Connect](/en/topics/nip-46/)
