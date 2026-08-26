---
title: "NIP-25: Reactions"
date: 2026-07-29
draft: false
categories:
  - Protocol
  - Social
---

NIP-25 defines reactions as kind `7` events. It gives clients a shared event form for attaching an emoji or other short reaction to a note, article, listing, or other referenced event.

## How It Works

A reaction event carries its reaction text in `content` and references the target through the target event's `e` tag. When the target is addressable, the reaction also includes its `a` tag. It also includes `p` tags for the referenced event's author, which lets relays and clients route notifications without inferring recipients from the event content.

The default reaction is `+`, so clients can treat an empty reaction content as a positive response. Other emoji are valid reaction values. The specification also permits `-` for a negative reaction, which the July 2022 follow-up added after the original introduction.

Clients should preserve the target reference and author tags when creating a reaction. A reaction is an ordinary signed event, so it can travel through normal relay subscriptions and be rendered by any client that recognizes kind `7`.

## Implementations

NIP-25 is widely implemented by Nostr clients and libraries as part of ordinary note interaction. Its simple kind-and-tags model lets clients display counts, individual reactions, and notifications without a separate transport protocol.

---

**Primary sources:**
- [NIP-25 Specification](https://github.com/nostr-protocol/nips/blob/master/25.md)
- [Introduction commit](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88)
- [Downvote follow-up](https://github.com/nostr-protocol/nips/commit/89bb08ba8683)

**Mentioned in:**
- [Newsletter #33: Six Years of Nostr Julys](/en/newsletters/2026-07-29-newsletter/#six-years-of-nostr-julys)
- [Newsletter #37: Marmot](/en/newsletters/2026-08-26-newsletter/#marmot)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
- [NIP-10: Text Note Threading](/en/topics/nip-10/)
