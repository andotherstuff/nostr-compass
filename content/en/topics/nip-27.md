---
title: "NIP-27 (Text Note References)"
date: 2026-02-04
description: "NIP-27 defines how to reference profiles, notes, and other entities within note content using nostr: URI scheme."
draft: false
categories:
  - NIP
  - Social
---

NIP-27 specifies how to embed references to Nostr entities within the content of text notes. References use the `nostr:` URI scheme followed by a bech32-encoded identifier (npub, note, nevent, nprofile, naddr).

## How It Works

When composing a note that mentions another user or references another event, the reference is embedded directly in the content:

```
Check out this post by nostr:npub1... about nostr:note1...
```

Clients parse these references and render them appropriately, typically as clickable links or inline profile cards. The referenced entities may also be mirrored into event tags for indexing or notifications, but the spec leaves that optional.

The NIP also covers hashtag parsing. Tags prefixed with `#` are extracted and added to the event's `t` tags for searchability.

## Reference Types

- `nostr:npub1...` - Reference to a user profile
- `nostr:note1...` - Reference to a specific note event
- `nostr:nevent1...` - Reference to an event with relay hints
- `nostr:nprofile1...` - Reference to a profile with relay hints
- `nostr:naddr1...` - Reference to an addressable event

## Why It Matters

NIP-27 separates what people read from what clients store. A user can type `@name` in a rich composer, but the published event can still contain a stable `nostr:nprofile...` reference in `content`. That makes the reference portable across clients without depending on one app's mention syntax.

Another practical benefit is resilience. A raw `nostr:nevent...` or `nostr:naddr...` embedded in text still carries enough information for another client to reconstruct the target even if it has never seen the original local rendering.

## Interop Notes

- Use [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) form in the content itself: `nostr:<bech32-id>`
- Add `p` or `q` tags only when your client wants mention notifications or stronger event indexing
- Do not assume every inline reference should become a reply relationship. The spec leaves that choice to the client

---

**Primary sources:**

- [NIP-27 Specification](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Bech32 Encoded Entities)](/en/topics/nip-19/) - Defines the encoding formats used in references

**Mentioned in:**

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - nostr-tools fix for hashtag parsing after newlines

**See also:**
- [NIP-18: Reposts](/en/topics/nip-18/)
- [NIP-19: Bech32-Encoded Entities](/en/topics/nip-19/)
