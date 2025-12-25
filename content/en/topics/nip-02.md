---
title: "NIP-02: Follow List"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-02 defines kind 3 events, which store your follow list. This simple mechanism powers the social graph that makes timelines possible.

## Structure

A kind 3 event contains `p` tags listing followed pubkeys:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Each `p` tag has four positions: the tag name, the followed pubkey (hex), an optional relay URL hint, and an optional "petname" (a local nickname). The relay hint tells other clients where to find that user's events. The petname lets you assign memorable names to contacts without relying on their self-declared display names.

## Replaceable Behavior

Kind 3 falls in the replaceable range (0, 3, 10000-19999), so relays keep only the latest version per pubkey. When you follow someone new, your client publishes a complete new kind 3 containing all your follows plus the new one. This means follow lists must be complete each time; you can't publish incremental updates.

## Building Timelines

To construct a home feed, clients fetch the user's kind 3, extract all `p` tag pubkeys, then subscribe to kind 1 events from those authors:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

The relay returns matching notes, and the client renders them. The relay hints in kind 3 help clients know which relays to query for each followed user.

## Petnames and Identity

The petname field enables a decentralized naming scheme. Rather than trusting whatever name a user claims in their profile, you can assign your own label. A client might display "alice (My Sister)" where "alice" comes from her kind 0 profile and "My Sister" is your petname. This provides context that global usernames cannot.

## Practical Considerations

Because kind 3 events are replaceable and must be complete, clients should preserve unknown tags when updating. If another client added tags your client doesn't understand, blindly overwriting would lose that data. Append new follows rather than rebuilding from scratch.

---

**Primary sources:**
- [NIP-02 Specification](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Mentioned in:**
- [Newsletter #2: NIP Deep Dive](/en/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
