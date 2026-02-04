---
title: "NIP-27 (Text Note References)"
date: 2026-02-04
description: "NIP-27 defines how to reference profiles, notes, and other entities within note content using nostr: URI scheme."
---

NIP-27 specifies how to embed references to Nostr entities within the content of text notes. References use the `nostr:` URI scheme followed by a bech32-encoded identifier (npub, note, nevent, nprofile, naddr).

## How It Works

When composing a note that mentions another user or references another event, the reference is embedded directly in the content:

```
Check out this post by nostr:npub1... about nostr:note1...
```

Clients parse these references and render them appropriately, typically as clickable links or inline profile cards. The referenced entities are also added to the event's tags for indexing and notification purposes.

The NIP also covers hashtag parsing. Tags prefixed with `#` are extracted and added to the event's `t` tags for searchability.

## Reference Types

- `nostr:npub1...` - Reference to a user profile
- `nostr:note1...` - Reference to a specific note event
- `nostr:nevent1...` - Reference to an event with relay hints
- `nostr:nprofile1...` - Reference to a profile with relay hints
- `nostr:naddr1...` - Reference to an addressable event

## Implementations

All major Nostr clients implement NIP-27:
- Text parsers extract references during composition
- Renderers display references as interactive elements
- Notification systems use the associated tags

## Primary Sources

- [NIP-27 Specification](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Bech32 Encoded Entities)](/en/topics/nip-19/) - Defines the encoding formats used in references

## Mentioned In

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - nostr-tools fix for hashtag parsing after newlines
