---
title: "NIP-62: Vanish Requests"
date: 2026-01-13
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 defines vanish requests, a mechanism for users to request that relays delete their content. While relays are not obligated to honor these requests, supporting NIP-62 gives users more control over their published data and provides a standardized way to signal deletion intent across the network.

## How It Works

A vanish request is a kind 62 event signed by the user who wants their content removed. The request can target specific events by including their IDs in `e` tags, or it can request deletion of all content from that pubkey by omitting the `e` tags entirely.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 62,
  "tags": [
    ["e", "event1234...", "wss://relay.example.com"],
    ["e", "event5678...", "wss://relay.example.com"]
  ],
  "content": "Removing old posts",
  "sig": "sig1234..."
}
```

The `content` field optionally contains a human-readable reason for the deletion request. Relay hints in the `e` tags tell relays where the original events were published, though relays may honor requests regardless of whether they have the specified events.

## Relay Behavior

Relays that support NIP-62 should delete the specified events from their storage and stop serving them to subscribers. The vanish request itself may be retained as a record that deletion was requested, which helps prevent deleted events from being re-imported from other relays.

When a vanish request omits all `e` tags, relays interpret this as a request to remove all events from that pubkey. This is a more drastic action and relays may handle it differently, for instance by marking the pubkey as "vanished" and refusing to accept or serve any of its events going forward.

Relays are not required to support NIP-62. The Nostr network is decentralized, and each relay operator decides their own data retention policies. Users should not assume their content will be deleted everywhere simply because they published a vanish request.

## Privacy Considerations

Vanish requests are a best-effort deletion mechanism, not a guarantee of privacy. Even after publishing a vanish request, copies of the content may exist elsewhere in the network including on other relays that don't support NIP-62, in local caches on client devices, in third-party archives or search engines, and in backups.

The request itself is also a signed Nostr event, meaning it becomes part of your public record. Anyone who sees the vanish request knows you deleted something, even if they cannot see what was deleted.

For content that must remain private, consider using encrypted messaging like [NIP-17](/en/topics/nip-17/) rather than relying on deletion after the fact.

---

**Primary sources:**
- [NIP-62 Specification](https://github.com/nostr-protocol/nips/blob/master/62.md)

**Mentioned in:**
- [Newsletter #5: Notable Code Changes](/en/newsletters/2026-01-13-newsletter/#rust-nostr-library)
