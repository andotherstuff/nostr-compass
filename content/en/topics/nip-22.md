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

Comments use kind 1111 events with plaintext `content`. Root scope tags are uppercase, and parent-reply tags are lowercase:

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["K", "30023"],
    ["P", "<root-pubkey>", "wss://relay.example"],
    ["a", "30023:pubkey:article-id", "wss://relay.example"],
    ["e", "<parent-event-id>", "wss://relay.example", "<parent-pubkey>"],
    ["k", "30023"],
    ["p", "<parent-pubkey>", "wss://relay.example"]
  ],
  "content": "Great article!"
}
```

## Tag Structure

- **`A` / `E` / `I`** - Root scope of the discussion: addressable event, event id, or external identifier
- **`K`** - Kind or root scope type for that root item
- **`P`** - Author of the root event when one exists
- **`a` / `e` / `i`** - Immediate parent being replied to
- **`k`** - Kind or scope type of the parent item
- **`p`** - Author of the parent item

For top-level comments, the root and parent usually point at the same target. For replies to comments, the root stays fixed while the lowercase parent tags move to the specific comment being answered.

## Interop Notes

NIP-22 comments are not a generic replacement for kind 1 replies. The spec explicitly says comments must not be used to reply to kind 1 notes. For note-to-note threads, clients should keep using [NIP-10](/en/topics/nip-10/).

Another useful distinction is scope. NIP-22 can anchor discussion to non-note resources through `I` and `i` tags, including URLs and other external identifiers from [NIP-73](/en/topics/nip-73/). That gives clients a standard way to attach comment threads to web pages, podcasts, or other off-Nostr objects.

## Use Cases

- Article discussions
- Video comments
- [NIP-52](/en/topics/nip-52/) calendar event discussions
- Wiki page talk pages
- Comments on external resources identified through `I` tags

---

**Primary sources:**
- [NIP-22 Specification](https://github.com/nostr-protocol/nips/blob/master/22.md)

**Mentioned in:**
- [Newsletter #7: Notedeck](/en/newsletters/2026-01-28-newsletter/#notedeck)
- [Newsletter #10: AI Agent NIPs Arrive](/en/newsletters/2026-02-18-newsletter/#ai-agent-nips-arrive)
- [Newsletter #12: diVine](/en/newsletters/2026-03-04-newsletter/#divine)

**See also:**
- [NIP-10: Reply Threads](/en/topics/nip-10/)
- [NIP-52: Calendar Events](/en/topics/nip-52/)
- [NIP-73: External Content IDs](/en/topics/nip-73/)
