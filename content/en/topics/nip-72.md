---
title: "NIP-72: Moderated Communities"
date: 2026-03-25
draft: false
categories:
  - NIPs
  - Communities
---

NIP-72 defines moderated communities on Nostr. Communities provide a way to organize posts around a shared topic or group, with moderators who approve content before it becomes visible to members.

## How It Works

A community is defined by a kind 34550 event published by its creator. This event contains the community name, description, rules, and a list of moderator pubkeys. The event uses a replaceable event format (kind 30000-39999 range), so the community definition can be updated over time.

```json
{
  "kind": 34550,
  "tags": [
    ["d", "example-community"],
    ["name", "Example Community"],
    ["description", "A community for discussing examples"],
    ["p", "<moderator_pubkey>", "", "moderator"],
    ["relay", "wss://relay.example.com", "moderator"]
  ],
  "content": "",
  "pubkey": "<creator_pubkey>",
  "created_at": 1742860800,
  "sig": "<signature>"
}
```

Users submit posts to a community by tagging their events with an `a` tag pointing to the community definition. These posts are not yet visible to community readers. A moderator reviews the submission and, if approved, publishes a kind 4549 approval event that wraps the original post. Clients that display the community only show posts that have a corresponding approval event from a recognized moderator.

This approval model means communities are read-filtered, not write-restricted. Anyone can submit a post, but only approved posts appear in the community feed. Moderators act as curators rather than gatekeepers of the underlying data.

## Considerations

Because approval events are separate Nostr events, moderation decisions are transparent and auditable. A post rejected by one community can still be approved by another. The same content can exist in multiple communities with independent moderation.

Relay support matters for community functionality. Clients need to query for both the community definition and approval events, which requires relays that index these event kinds efficiently.

---

**Primary sources:**
- [NIP-72 Specification](https://github.com/nostr-protocol/nips/blob/master/72.md) - Moderated Communities

**Mentioned in:**
- [Newsletter #15](/en/newsletters/2026-03-25-newsletter/)
