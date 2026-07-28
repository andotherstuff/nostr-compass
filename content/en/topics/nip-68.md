---
title: "NIP-68: Picture-first Feeds"
date: 2026-07-29
draft: false
categories:
  - Media
  - Protocol
---

NIP-68 defines addressable picture events. It gives clients a portable way to publish image metadata, captions, labels, and references to image files while keeping the event itself separate from blob storage.

## How It Works

A picture uses kind `20` and carries a `title` tag with a description in `content`. The `imeta` tag describes each image with fields such as `url`, `m` for MIME type, `dim` for dimensions, `alt` text, and an optional SHA-256 hash. Multiple `imeta` tags let one event represent an image set.

The event can include `p` tags for people depicted or credited, `t` tags for topics, and ordinary Nostr references. It can also include media-type, hash, location, and content-warning tags so clients can filter and render image posts consistently.

NIP-68 does not prescribe a storage backend. Clients can reference ordinary HTTPS URLs or a content-addressed system such as Blossom, as long as they publish enough `imeta` metadata for another client to display and verify the image.

## Implementations

[NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0) added NIP-68 image tagging alongside its image-oriented client features.

---

**Primary sources:**
- [NIP-68 Specification](https://github.com/nostr-protocol/nips/blob/master/68.md)
- [NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0)

**Mentioned in:**
- [Newsletter #33: Tagged releases](/en/newsletters/2026-07-29-newsletter/#tagged-releases)

**See also:**
- [Blossom Protocol](/en/topics/blossom/)
- [NIP-94: File Metadata](/en/topics/nip-94/)
