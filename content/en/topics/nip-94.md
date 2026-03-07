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

NIP-94 uses kind `1063` as a standalone metadata event for a file. The event `content` holds a human-readable description, while tags carry machine-readable fields such as download URL, MIME type, hashes, dimensions, and preview hints.

That separation matters because the metadata event can be indexed, filtered, and reused independently of any note that links to the file. A client can treat a kind `1063` event as the canonical description of an asset instead of scraping metadata from free-form post text.

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
- `service` - Storage protocol or service type, such as NIP-96

The `ox` and `x` tags are easy to overlook but useful in practice. `ox` identifies the original uploaded file, while `x` can identify the transformed version a server actually serves. When a media host compresses or resizes uploads, clients can still preserve the original-file identity without pretending the transformed blob is byte-for-byte identical.

## When To Use It

NIP-94 is designed for file-sharing applications rather than social or longform content clients. Suggested applications include:

- Torrent indexing relays
- Portfolio-sharing platforms (similar to Pinterest)
- Software configuration and update distribution
- Media libraries and archives

If the file metadata only needs to decorate a URL embedded inside another event, [NIP-92: Media Attachments](/en/topics/nip-92/) is lighter. NIP-94 is the better choice when the file itself should be queryable as a first-class object.

## Interop Notes

NIP-94 works across storage backends. A file can be uploaded through [NIP-96: HTTP File Storage](/en/topics/nip-96/), Blossom, or another service, then still described with the same kind `1063` event shape. That is why the metadata format keeps outliving any single upload protocol.

---

**Primary sources:**
- [NIP-94 Specification](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-92: Media Attachments](/en/topics/nip-92/)
- [Blossom](/en/topics/blossom/)
