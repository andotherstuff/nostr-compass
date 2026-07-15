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

Concord splits what a Discord-style community server normally does into pieces that need to trust nobody: relays only ever store encrypted blobs addressed to rotating labels, holding a room's key is what makes someone a member, and authority over roles, kicks, and bans is a signed roster rooted in the owner's identity that every client verifies locally instead of trusting a server to enforce it. Every durable event rides the same three-layer envelope: a kind 1059 wrap signed by the plane's own derived stream key, containing a seal signed by the author's real key, containing an unsigned rumor that carries the functional event. A chat message rumor is a plain kind 9 event:

```json
{
  "kind": 9,
  "pubkey": "<author>",
  "content": "Hey chat!",
  "tags": [
    ["channel", "<channel_id>"],
    ["epoch", "0"]
  ]
}
```

Control, chat, and guestbook traffic each get their own [NIP-59](/en/topics/nip-59/) gift-wrapped plane, so a relay holding all three still cannot tell a control message from a chat message from a guestbook entry without the room key. The spec is split into seven CORD documents: private streams (01), communities and membership (02), channels (03), roles (04), invites (05), rekeying and re-founding to cut off removed members (06), and audio/video via a blind token broker (07). Membership itself has no server-side list: whoever can decrypt the plane is a member, and removing someone for real means rolling the community to a new key epoch and handing it only to who is left, instead of deleting a row from a table.

## How It Differs from Marmot

Concord and [Marmot](/en/topics/marmot/) solve encrypted group messaging on Nostr with different cryptography for different group shapes, and the Concord project's own comparison is explicit about the split: Marmot layers [MLS](/en/topics/mls/) on top of Nostr for forward secrecy and post-compromise security, using per-device key packages and ordered commits that advance the whole group in lockstep. That buys strong guarantees, at a cost that scales with membership changes, well suited to small, high-stakes groups where joins and leaves are rare. Concord instead gives every member the same room key and re-keys the whole room on removal instead of ratcheting per commit, trading some of MLS's cryptographic guarantees for a model that stays cheap as a community grows into the hundreds or thousands of casual, high-churn members, the shape Discord-style communities actually take.

## Why Vector Switched

Vector's own [v0.4.0 release notes](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) describe Concord only as "our custom messaging protocol" for Group Chats, without stating the reasoning directly. The fit with Concord's own published rationale is clear regardless: Group Chats in a client like Vector are exactly the large, open, frequently-changing-membership case where Marmot's per-device MLS state becomes the more expensive path, and Concord's asynchronous, fold-anytime design is built for that case instead. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) retired Marmot for Group Chats in favor of Concord, and existing Marmot group history did not carry over in the switch. [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) shipped "Concord v2" four days later with privacy and stability improvements. Within the same week, [Amethyst merged its own clean-room, wire-compatible Concord implementation](https://github.com/vitorpamplona/amethyst/pull/3566), and Soapbox's Discord-style client [Armada](https://gitlab.com/soapbox-pub/armada) already builds its Communities feature on the same spec as a reference implementation. Three independent clients converging on one open spec within days of each other is a fast path to real cross-client interop, worth tracking against how much of the rest of Nostr's group-chat clients stay on Marmot instead.

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
