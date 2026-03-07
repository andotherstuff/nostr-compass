---
title: "NIP-02: Follow List"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-02 defines kind 3 events, which store a user's follow list. This event is the base input for home feeds, reply notifications, and many relay selection strategies.

## How It Works

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

## Why It Matters

To construct a home feed, clients fetch the user's kind 3, extract all `p` tag pubkeys, then subscribe to kind 1 events from those authors:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

The relay returns matching notes, and the client renders them. The relay hints in kind 3 help clients know which relays to query for each followed user.

This event is also where stale social state shows up first. If a user's latest kind 3 is missing on the relays you query, their feed can look empty even though their follows still exist elsewhere. Clients that merge results from multiple relays usually recover better than clients that trust a single relay.

## Petnames and Identity

The petname field enables a decentralized naming scheme. Rather than trusting whatever name a user claims in their profile, you can assign your own label. A client might display "alice (My Sister)" where "alice" comes from her kind 0 profile and "My Sister" is your petname. This provides context that global usernames cannot.

## Interop Notes

Because kind 3 events are replaceable and must be complete, clients should preserve unknown tags when updating. If another client added tags your client doesn't understand, blindly overwriting would lose that data.

The same caution applies to relay hints and petnames. They are optional fields, but dropping them on write can silently make another client's experience worse. A safe update path is: load the latest known kind 3, modify only the tags you understand, keep the rest, then republish the full event.

---

**Primary sources:**
- [NIP-02 Specification](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Mentioned in:**
- [Newsletter #2: NIP Deep Dive](/en/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
- [NIP-10: Text Note Threading](/en/topics/nip-10/)
- [NIP-65: Relay List Metadata](/en/topics/nip-65/)
