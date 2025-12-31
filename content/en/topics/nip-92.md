---
title: "NIP-92: Media Attachments"
date: 2025-12-31
draft: false
categories:
  - Media
  - Protocol
---

NIP-92 enables users to attach media files to Nostr events by including URLs alongside inline metadata tags that describe those resources.

## How It Works

1. User places media URLs directly in event content (e.g., in a kind 1 text note)
2. A matching `imeta` (inline metadata) tag provides details about each URL
3. Clients can replace imeta URLs with rich previews based on the metadata
4. Metadata is typically auto-generated when files are uploaded during composition

## The imeta Tag

Each `imeta` tag must have a `url` and at least one other field. Supported fields include:

- `url` - The media URL (required)
- `m` - MIME type of the file
- `dim` - Image dimensions (width x height)
- `blurhash` - Blurhash for preview generation
- `alt` - Alt text description for accessibility
- `x` - SHA-256 hash (from NIP-94)
- `fallback` - Alternative URLs if primary fails

## Example

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**Primary sources:**
- [NIP-92 Specification](https://github.com/nostr-protocol/nips/blob/master/92.md)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-94: File Metadata](/en/topics/nip-94/)
