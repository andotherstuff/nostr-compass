---
title: "NIP-22: Comments"
date: 2026-01-28
draft: false
categories:
  - NIP
  - Social
---

NIP-22 defines a standard for commenting on any addressable Nostr content, enabling threaded discussions on articles, videos, calendar events, and other addressable events.

## How It Works

Comments use kind 1111 events with tags referencing the content being commented on:

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["E", "root-event-id", "wss://relay.example"],
    ["K", "30023"]
  ],
  "content": "Great article!"
}
```

## Tag Structure

- **`A` tag**: References the addressable event being commented on (kind:pubkey:d-tag format)
- **`E` tag**: References the root event ID for threading
- **`K` tag**: Indicates the kind of the root event
- **`e` tag**: References parent comment for nested replies

## Difference from Kind 1

While kind 1 notes can reply to other notes, NIP-22 comments are specifically designed for:

- Addressable content (articles, videos, calendar events)
- Maintaining clear parent-child relationships
- Enabling moderation and threading on long-form content

## Use Cases

- Article discussions
- Video comments
- [NIP-52](/en/topics/nip-52/) calendar event discussions
- Wiki page talk pages
- Any addressable event type

## Related

- [NIP-01](/en/topics/nip-01/) - Basic Protocol (kind 1 notes)
- [NIP-52](/en/topics/nip-52/) - Calendar Events
