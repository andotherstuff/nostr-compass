---
title: "NIP-51: Lists"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Social
---

NIP-51 defines various list types for organizing references to events, users, and content in Nostr.

## List Kinds

- **Kind 10000**: Mute list (users, threads, or words to hide)
- **Kind 10001**: Pin list (events to feature on profile)
- **Kind 30000**: Follow sets (categorized follow lists)
- **Kind 30003**: Bookmark sets
- **Kind 30004**: Curation sets (articles)
- **Kind 30005**: Video sets
- **Kind 30006**: Picture sets
- **Kind 30015**: Interest sets (hashtags)
- **Kind 30030**: Emoji sets

## Structure

Lists use tags to reference content:
- `p` tags for pubkeys
- `e` tags for events
- `a` tags for addressable events
- `t` tags for hashtags
- `word` tags for muted words

## Public vs Private

Lists can have public tags (visible to everyone) and encrypted content (private). Private items are encrypted using NIP-44 and stored in the event's `content` field. The encryption uses the author's own keys (encrypting to yourself).

This allows features like public bookmarks with private notes, or a mute list where muted items are hidden from others.

## Recent Changes

- Hashtag and URL tags removed from generic bookmarks; hashtags now use kind 30015
- Kind 30006 added for curated picture sets

---

**Primary sources:**
- [NIP-51 Specification](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)

**See also:**
- [NIP-02: Follow List](/en/topics/nip-02/)
