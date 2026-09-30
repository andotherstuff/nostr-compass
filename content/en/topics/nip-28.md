---
title: "NIP-28: Public Chat"
date: 2026-09-30
draft: false
categories:
  - NIPs
  - Social
---

NIP-28 describes public chat channels, channel messages, and client-side moderation as Nostr events. The current specification is marked **draft** and **unrecommended** and points implementers toward NIP-29 for current relay-based groups.

## Event model

Kind `40` creates a channel; kind `41` updates its metadata; kind `42` carries a message. Kinds `43` and `44` let a user hide a message or mute another user in their client. Message tags refer to the channel creation event and can identify the message being answered. Relays need not enforce those client-side hide and mute choices.

The [September 2022 specification change](https://github.com/nostr-protocol/nips/commit/3423a6dfb) made a public chat room a shared protocol subject. That historical role remains useful to understand even though the [present specification](https://github.com/nostr-protocol/nips/blob/master/28.md) recommends a different route for new implementations.

---

**Primary sources:**
- [NIP-28 specification and current status](https://github.com/nostr-protocol/nips/blob/master/28.md)
- [September 2022 public-chat change](https://github.com/nostr-protocol/nips/commit/3423a6dfb)

**Mentioned in:**
- [Newsletter #42: September 2022](/en/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)

**See also:**
- [NIP-29: Relay-Based Groups](/en/topics/nip-29/)
