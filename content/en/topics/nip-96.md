---
title: "NIP-96: HTTP File Storage"
date: 2026-02-11
draft: false
categories:
  - NIPs
  - Media
---

NIP-96 defined how Nostr clients upload, download, and manage files on HTTP media servers. Now marked as "unrecommended" in favor of Blossom, NIP-96 remains relevant as projects navigate the transition between the two media standards.

## How It Works

A client discovers a file server's capabilities by fetching `/.well-known/nostr/nip96.json`, which returns the API URL, supported content types, size limits, and available media transformations.

To upload, the client sends a `multipart/form-data` POST to the API URL with a NIP-98 authorization header (a signed Nostr event proving the uploader's identity). The server returns a NIP-94 file metadata structure containing the file URL, SHA-256 hashes, MIME type, and dimensions.

Downloads use GET requests to `<api_url>/<sha256-hash>`, with optional query parameters for server-side transforms like image resizing. Deletion uses DELETE with NIP-98 auth. Users publish kind 10096 events to declare their preferred upload servers.

## Why It Was Deprecated

NIP-96 tied file URLs to specific servers. If a server went down, every Nostr note referencing that server's URLs lost its media. Blossom inverts this by making the SHA-256 hash of the file content the canonical identifier. Any Blossom server hosting the same file serves it at the same hash path, making content portable across servers by default.

Blossom also simplifies the API: plain PUT for uploads, GET for downloads, and signed Nostr events (not HTTP headers) for authorization. The deprecation happened in September 2025 via [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## The Transition

Servers like nostr.build and void.cat supported NIP-96 and have added or migrated to Blossom endpoints. Clients are at various stages: Angor v0.2.5 added NIP-96 server configuration while ZSP v0.3.1 uploads exclusively to Blossom servers. The coexistence will continue until remaining NIP-96 implementations complete migration.

Kind 10096 server preference events remain useful for Blossom server selection. NIP-94 file metadata (kind 1063 events) describes file properties regardless of which upload protocol created them.

---

**Primary sources:**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**Mentioned in:**
- [Newsletter #9: NIP Deep Dive](/en/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-96-http-file-storage-and-the-transition-to-blossom)

**See also:**
- [Blossom Protocol](/en/topics/blossom/)
- [NIP-94: File Metadata](/en/topics/nip-94/)
