---
title: "NIP-32: Labeling"
date: 2026-01-21
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-32 defines a standard for attaching labels to Nostr events, users, and other entities. Labels provide structured metadata that clients can use for categorization, content warnings, reputation systems, and moderation.

## How It Works

Labels use kind 1985 events with an `L` tag defining the label namespace and `l` tags applying specific labels within that namespace. The labeled entity is referenced through standard tags like `e` (events), `p` (pubkeys), or `r` (relay URLs).

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Contains explicit imagery"
}
```

The namespace system prevents label collisions. A "spam" label in the "ugc-moderation" namespace has different semantics than "spam" in the "relay-report" namespace. This enables multiple label systems to coexist without interference.

## Why It Matters

The key design choice is that labels are assertions, not facts built into the protocol. A kind 1985 event says that some actor labeled something in some namespace. Clients still need a trust policy for deciding whose labels to show, hide, or ignore.

That makes NIP-32 useful well beyond moderation. The same structure can carry content warnings, verification markers, classification systems, or relay reputation data without forcing all clients into one global vocabulary.

## Use Cases

Content moderation systems use labels to mark spam, illegal content, or policy violations. Reputation systems attach trust scores or verification status to pubkeys. Media platforms apply content warnings such as NSFW, violence, or spoilers. Relay operators use labels for appeals and dispute resolution.

The Trusted Relay Assertions proposal uses NIP-32 labels for relay appeals. When operators dispute trust scores, they publish kind 1985 events with `L = relay-appeal` and labels such as `spam`, `censorship`, or `score`.

## Interop Notes

Clients differ in how they consume labels. Some treat labels from followed users as recommendations, while others query specialized labeling services. The decentralized design lets users choose which labelers to trust, but it also means a label with no visible trust context can be misleading.

---

**Primary sources:**
- [NIP-32 Specification](https://github.com/nostr-protocol/nips/blob/master/32.md) - Labeling standard

**Mentioned in:**
- [Newsletter #6: NIP Updates](/en/newsletters/2026-01-21-newsletter/#nip-updates)

**See also:**
- [Trusted Relay Assertions](/en/topics/trusted-relay-assertions/)
- [NIP-51: Lists](/en/topics/nip-51/)
