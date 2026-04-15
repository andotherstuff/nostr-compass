---
title: "NIP-C7: Chat Messages"
date: 2026-04-15
draft: false
categories:
  - Protocol
  - Messaging
description: "NIP-C7 defines kind 9 as the dedicated event kind for chat messages in Nostr group and channel contexts."
---

NIP-C7 defines kind `9` as the event kind for chat messages. The goal is to separate chat-oriented traffic from general social feed traffic, so clients can apply different UX and moderation rules to each context.

## How It Works

A kind `9` event carries message content plus tags that identify the chat context. In [NIP-29](/en/topics/nip-29/) relay-based groups, the event includes an `h` tag with the group ID. Reply threading uses `q` tags that reference earlier events.

NIP-C7 is focused on where these events should be rendered. Instead of appearing in global note feeds like kind `1` text notes, kind `9` events are intended for chat-oriented views where conversation state and threading are explicit.

## Implementations

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) and [Coracle](https://github.com/coracle-social/coracle) use kind `9` in group chat workflows.
- [Amethyst](https://github.com/vitorpamplona/amethyst) includes kind `9` support in its messaging stack.
- [White Noise](https://github.com/marmot-protocol/whitenoise) uses NIP-C7 reply threading with `q` tags.

---

**Primary sources:**
- [NIP-C7 Specification](https://github.com/nostr-protocol/nips/blob/master/C7.md)
- [PR #2310: Restrict kind 9 to chat views](https://github.com/nostr-protocol/nips/pull/2310)

**Mentioned in:**
- [Newsletter #18: NIP Updates](/en/newsletters/2026-04-15-newsletter/#nip-updates)

**See also:**
- [NIP-29: Relay-based Groups](/en/topics/nip-29/)
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
