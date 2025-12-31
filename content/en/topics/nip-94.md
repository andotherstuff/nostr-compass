---
title: "NIP-94: File Metadata"
date: 2025-12-31
draft: false
categories:
  - Media
  - Protocol
---

NIP-94 defines a file metadata event (kind 1063) for organizing and classifying shared files on Nostr, enabling relays to filter and organize content effectively.

## How It Works

1. User uploads a file to a hosting service
2. A kind 1063 event is published with metadata about the file
3. The event content contains a human-readable description
4. Structured tags provide machine-readable metadata
5. Specialized clients can organize and display files systematically

## Required and Optional Tags

**Core tags:**
- `url` - Download link for the file
- `m` - MIME type (lowercase format required)
- `x` - SHA-256 hash of the file

**Optional tags:**
- `ox` - SHA-256 hash of the original file before server transformations
- `size` - File size in bytes
- `dim` - Dimensions (width x height) for images/video
- `magnet` - Magnet URI for torrent distribution
- `i` - Torrent infohash
- `blurhash` - Placeholder image for previews
- `thumb` - Thumbnail URL
- `image` - Preview image URL
- `summary` - Text excerpt
- `alt` - Accessibility description
- `fallback` - Alternative download sources

## Use Cases

NIP-94 is designed for file-sharing applications rather than social or longform content clients. Suggested applications include:

- Torrent indexing relays
- Portfolio-sharing platforms (similar to Pinterest)
- Software configuration and update distribution
- Media libraries and archives

---

**Primary sources:**
- [NIP-94 Specification](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-92: Media Attachments](/en/topics/nip-92/)
- [Blossom](/en/topics/blossom/)
