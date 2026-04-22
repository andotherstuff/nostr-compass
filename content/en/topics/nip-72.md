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

Users submit posts to a community by tagging their events with an `a` tag pointing to the community definition. These posts are not yet visible to community readers. A moderator reviews the submission and, if approved, publishes a kind 4550 approval event that wraps the original post. Clients that display the community only show posts that have a corresponding approval event from a recognized moderator.

This approval model means communities are read-filtered, not write-restricted. Anyone can submit a post, but only approved posts appear in the community feed. Moderators act as curators rather than gatekeepers of the underlying data.

## Considerations

Because approval events are separate Nostr events, moderation decisions are transparent and auditable. A post rejected by one community can still be approved by another. The same content can exist in multiple communities with independent moderation.

Relay support matters for community functionality. Clients need to query for both the community definition and approval events, which requires relays that index these event kinds efficiently.

Compared to [NIP-29](/en/topics/nip-29/) relay-based groups, where the relay is the authority for both membership and moderation, NIP-72 lives in plain Nostr events. Any relay that carries kinds `34550`, `4550`, and the submission kinds can serve a community, and moderation is visible and forkable. The tradeoff is that unapproved submissions are only hidden at the client-render layer, so NIP-29 remains the better fit when spam must stay off the wire entirely.

## Implementations

- [noStrudel](https://github.com/hzrd149/nostrudel) has long-standing NIP-72 community support, including a pending submission queue for moderators.
- [Amethyst](https://github.com/vitorpamplona/amethyst) added first-class community creation and management in [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468): authoring the kind `34550` community definition, adding moderators and relay hints, submitting posts with an `a` tag, and managing pending approvals via kind `4550` events.

---

**Primary sources:**
- [NIP-72 Specification](https://github.com/nostr-protocol/nips/blob/master/72.md) - Moderated Communities
- [Amethyst PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) - NIP-72 community creation and moderation

**Mentioned in:**
- [Newsletter #15](/en/newsletters/2026-03-25-newsletter/)
- [Newsletter #19: Amethyst community support](/en/newsletters/2026-04-22-newsletter/#amethyst-ships-marmot-mip-compliance-nip-72-communities-and-live-stream-zap-goals)
- [Newsletter #19: NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/#nip-deep-dive-nip-72-moderated-communities)

**See also:**
- [NIP-29: Relay-based Groups](/en/topics/nip-29/)
