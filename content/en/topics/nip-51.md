---
title: "NIP-51: Lists"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Social
---

NIP-51 defines list events for organizing users, events, relays, hashtags, and other references. It is the main protocol for bookmarks, mute lists, follow sets, relay sets, and several other user-curated collections.

## Standard Lists and Sets

- **Standard lists** use replaceable event kinds such as kind `10000` mute lists, kind `10003` bookmarks, and kind `10007` search relays.
- **Sets** use addressable kinds with `d` tags, such as kind `30000` follow sets, kind `30003` bookmark sets, and kind `30030` emoji sets.

The distinction matters in client behavior. Standard lists imply one canonical list per user and kind. Sets imply many named collections, so clients must preserve each list's `d` tag.

## Structure

Lists use tags to reference content:

- `p` tags for pubkeys
- `e` tags for events
- `a` tags for addressable events
- `t` tags for hashtags
- `word` tags for muted words
- `relay` tags for relay URLs in relay-oriented list kinds

Some list kinds have narrower allowed tag shapes than others. For example, relay-oriented lists use `relay` tags, while bookmarks are expected to point to notes or addressable events. Clients that treat every NIP-51 list as arbitrary free-form tags will lose interoperability.

## Public vs Private

Lists can have public tags and private items. Private items are serialized as a JSON array that mirrors the `tags` structure, encrypted, and stored in the event `content`. The current spec uses NIP-44 for this self-encryption model, with NIP-04 only as legacy compatibility.

That split lets users publish a visible list shell while hiding some entries. A bookmark list can stay public while private notes or private bookmarks remain in encrypted content.

## Useful Kinds

- **Kind 10000**: mute list for pubkeys, threads, hashtags, and muted words
- **Kind 10003**: bookmarks for notes and addressable content
- **Kind 10007**: preferred search relays
- **Kind 30002**: relay sets for named relay groups
- **Kind 30006**: picture curation sets
- **Kind 39089**: starter packs for shareable follow bundles

Recent spec changes moved hashtags out of generic bookmarks and into interest sets, and added kind `30006` for picture curation. Both changes reduce ambiguity in how clients interpret list contents.

---

**Primary sources:**
- [NIP-51 Specification](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #5: NIP Deep Dive](/en/newsletters/2026-01-13-newsletter/#nip-deep-dive-nip-51-and-nip-65)
- [Newsletter #8: njump Adds NIP-51 Support](/en/newsletters/2026-02-04-newsletter/#njump)

**See also:**
- [NIP-02: Follow List](/en/topics/nip-02/)
