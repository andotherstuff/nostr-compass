---
title: "NIP-26: Delegated Event Signing"
date: 2026-09-30
draft: false
categories:
  - NIPs
  - Identity
---

NIP-26 documents a way for one Nostr key to authorize another key to sign a limited set of events. Its current specification is marked **draft** and **unrecommended**, so it records an earlier design rather than advice for a new integration.

## How it works

The account key signs a delegation token naming the delegate key and conditions. The conditions can restrict event kinds and `created_at` times. The delegate signs the event with its own key and attaches the token in a `delegation` tag. A reader must verify both the event signature and the delegation token against those conditions. Relays that support the scheme can also search by delegator.

The model lets an application publish without holding the account's primary signing key. Its extra validation and relay-search requirements explain why implementations cannot treat an ordinary event signature as sufficient proof of a delegated identity. The [current specification](https://github.com/nostr-protocol/nips/blob/master/26.md) explicitly marks the approach unrecommended.

---

**Primary sources:**
- [NIP-26 specification and current status](https://github.com/nostr-protocol/nips/blob/master/26.md)
- [September 2022 delegated-signing text](https://github.com/nostr-protocol/nips/commit/b62aa418d)

**Mentioned in:**
- [Newsletter #42: September 2022](/en/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)
