---
title: "Concord Protocol"
date: 2026-07-15
draft: false
categories:
  - Protocol
  - Messaging
---

Concord is an open, MIT-licensed protocol for end-to-end encrypted communities and channels on Nostr, defined by the [CORD-01 through CORD-07 specs](https://github.com/concord-protocol/concord). [Vector](https://github.com/VectorPrivacy/Vector) adopted it as the default transport for its Group Chats feature starting in v0.4.0, calling it "our custom messaging protocol" in its own release notes, but the spec itself is published separately from Vector and already has independent implementations.

## How It Works

Concord splits what a Discord-style community server normally does into pieces that need to trust nobody: relays only ever store encrypted blobs addressed to rotating labels, holding a room's key is what makes someone a member, and authority over roles, kicks, and bans is a signed roster rooted in the owner's identity that every client verifies locally instead of trusting a server to enforce it. Control, chat, and guestbook traffic rides as [NIP-59](/en/topics/nip-59/) gift-wrapped events over ordinary relays. The spec is split into seven CORD documents: private streams (01), communities and membership (02), channels (03), roles (04), invites (05), rekeying and re-founding to cut off removed members (06), and audio/video via a blind token broker (07).

## Why It Matters

Concord is positioned against Marmot, not as a variant of it: Marmot's MLS-based ratcheting is built for small, high-stakes groups with per-device key packages, while Concord targets large, casual, high-churn public communities where that ratcheting overhead does not scale. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) retired Marmot for its own Group Chats in favor of Concord, and [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) shipped "Concord v2" days later with privacy and stability improvements. Within the same week, [Amethyst merged its own clean-room, wire-compatible Concord implementation](https://github.com/vitorpamplona/amethyst/pull/3566), and Soapbox's Discord-style client [Armada](https://gitlab.com/soapbox-pub/armada) already builds its Communities feature on the same spec as a reference implementation. Three independent clients converging on one open spec within days of each other is a faster path to real cross-client interop than Marmot saw early on, and worth tracking against how much of the rest of the group-chat ecosystem stays consolidated around Marmot instead.

## Implementations

- [Vector](https://github.com/VectorPrivacy/Vector) - single-binary, privacy-first Nostr messenger; first shipping Concord client, in v0.4.0
- [Armada](https://gitlab.com/soapbox-pub/armada) (Soapbox) - Discord-style community client; reference implementation, backend in the separate `armada-relay` repo
- [Amethyst](https://github.com/vitorpamplona/amethyst) - feature-rich Android and multiplatform Nostr client; clean-room reimplementation wire-compatible with Armada ([PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566))

---

**Primary sources:**
- [Concord protocol specs (CORD-01 to CORD-07)](https://github.com/concord-protocol/concord)
- [Vector v0.4.0 release notes](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)
- [Vector v0.4.1 release notes](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1)
- [Amethyst PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566)

**Mentioned in:**
- [Newsletter #31: Vector v0.4.0 moves Group Chats from Marmot to Concord, and Amethyst ships its own Concord client days later](/en/newsletters/2026-07-15-newsletter/#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later)
- [Newsletter #31: Amethyst ships a clean-room Concord implementation for end-to-end encrypted communities](/en/newsletters/2026-07-15-newsletter/#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities)

**See also:**
- [Marmot Protocol](/en/topics/marmot/)
- [MLS (Message Layer Security)](/en/topics/mls/)
- [NIP-46: Nostr Connect](/en/topics/nip-46/)
