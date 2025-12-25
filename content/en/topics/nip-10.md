---
title: "NIP-10: Text Note Threading"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-10 specifies how kind 1 notes reference each other to form reply threads. Understanding this is essential for building conversation views.

## The Problem

When someone replies to a note, clients need to know: What is this a reply to? What's the root of the conversation? Who should be notified? NIP-10 answers these questions through `e` tags (event references) and `p` tags (pubkey mentions).

## Marked Tags (Preferred)

Modern clients use explicit markers in `e` tags:

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "Great point! I agree.",
  "sig": "b7d3f..."
}
```

The `root` marker points to the original note that started the thread. The `reply` marker points to the specific note being answered. If replying directly to the root, use only `root` (no `reply` tag needed). The distinction matters for rendering: the `reply` determines indentation in a thread view, while `root` groups all replies together.

## Threading Rules

- **Direct reply to root:** One `e` tag with `root` marker
- **Reply to a reply:** Two `e` tags, one `root` and one `reply`
- The `root` stays constant throughout the thread; `reply` changes based on what you're responding to

## Pubkey Tags for Notifications

Include `p` tags for everyone who should be notified. At minimum, tag the author of the note you're replying to. Convention is to also include all `p` tags from the parent event (so everyone in the conversation stays in the loop), plus any users you @mention in your content.

## Relay Hints

The third position in `e` and `p` tags can contain a relay URL where that event or user's content might be found. This helps clients fetch the referenced content even if they're not connected to the original relay.

## Deprecated Positional Tags

Early Nostr implementations inferred meaning from tag position rather than markers: first `e` tag was root, last was reply, middle ones were mentions. This approach is deprecated because it creates ambiguity. If you see `e` tags without markers, they're likely from older clients. Modern implementations should always use explicit markers.

## Building Thread Views

To display a thread, fetch the root event, then query for all events with an `e` tag referencing that root:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Sort results by `created_at` and use `reply` markers to build the tree structure. Events whose `reply` points to the root are top-level replies; events whose `reply` points to another reply are nested responses.

---

**Primary sources:**
- [NIP-10 Specification](https://github.com/nostr-protocol/nips/blob/master/10.md)

**Mentioned in:**
- [Newsletter #2: NIP Deep Dive](/en/newsletters/2025-12-24-newsletter/#nip-10-text-note-threading)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
