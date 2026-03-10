---
title: "NIP-96: HTTP File Storage"
date: 2026-02-11
draft: false
categories:
  - NIPs
  - Media
---

NIP-96 defines how Nostr clients upload, download, and manage files on HTTP media servers. It is now marked "unrecommended" in favor of Blossom, but it still matters because existing servers and clients continue to support it during the transition.

## How It Works

A client discovers a file server's capabilities by fetching `/.well-known/nostr/nip96.json`. That document advertises the upload API URL, optional download URL, supported content types, size limits, and whether the server supports media transformations or delegated hosting.

To upload, the client sends a `multipart/form-data` POST to the API URL with a [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) authorization header. The server responds with a NIP-94-shaped metadata object that includes the file URL plus tags such as `ox` for the original hash and, when applicable, `x` for the transformed file that will actually be served.

Downloads use `GET <api_url>/<sha256-hash>` with optional query parameters such as image width. Deletion uses `DELETE` with NIP-98 auth. Users publish kind `10096` events to declare their preferred upload servers.

## Data Model Details

One useful detail is that NIP-96 identifies files by the original file hash, even when the server transforms the upload. That lets a client delete or redownload the asset by the same stable identifier, while still getting server-generated thumbnails or recompressed variants when available.

The well-known document also supports `delegated_to_url`, which lets a relay point clients at a separate HTTP storage server. That kept relay software from having to implement the full media API itself.

## Why It Was Deprecated

NIP-96 tied file URLs to specific servers. If a server went down, every Nostr note referencing that server's URLs lost its media. Blossom inverts this by making the SHA-256 hash of the file content the canonical identifier. Any Blossom server hosting the same file serves it at the same hash path, making content portable across servers by default.

Blossom also simplifies the API: plain PUT for uploads, GET for downloads, and signed Nostr events (not HTTP headers) for authorization. The deprecation happened in September 2025 via [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## Interop Notes

Servers like nostr.build and void.cat supported NIP-96 and have added or migrated to Blossom endpoints. Clients are at various stages: [Angor v0.2.5](https://github.com/block-core/angor/releases/tag/v0.2.5) added NIP-96 server configuration while [ZSP v0.3.1](https://github.com/zapstore/zsp/releases/tag/v0.3.1) uploads exclusively to Blossom servers. The coexistence will continue until remaining NIP-96 implementations complete migration.

Kind 10096 server preference events remain useful while clients still support NIP-96 upload backends. NIP-94 file metadata (kind 1063 events) describes file properties regardless of which upload protocol created them.

---

**Primary sources:**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**Mentioned in:**
- [Newsletter #9: NIP Deep Dive](/en/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-96-http-file-storage-and-the-transition-to-blossom)
- [Newsletter #13: Route96 v0.5.0 and v0.5.1](/en/newsletters/2026-03-11-newsletter/#route96-v050-and-v051)

**See also:**
- [Blossom Protocol](/en/topics/blossom/)
- [NIP-94: File Metadata](/en/topics/nip-94/)
