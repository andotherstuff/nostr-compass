---
title: "Blossom Protocol"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

Blossom is a media hosting protocol for Nostr that stores blobs on ordinary HTTP servers and addresses them by SHA-256 hash instead of server-assigned IDs.

## How It Works

Blossom servers expose a small HTTP interface for blob retrieval, upload, and management. The canonical identifier is the file hash, so the same blob keeps the same address on every compliant server.

- `GET /<sha256>` retrieves a blob by hash
- `PUT /upload` uploads a blob
- kind `24242` Nostr events authorize uploads and management actions
- kind `10063` events, defined in [BUD-03](/en/topics/bud-03/), let users publish their preferred servers

Because the hash is the identifier, clients can verify integrity locally after download and can try another server without changing the underlying reference.

## Why It Matters

Blossom separates blob storage from social events. A note or profile can point at media without tying that media to one host's URL design.

This also changes failure handling. If a server disappears, clients can fetch the same hash from a mirror, a cache, or a server discovered through the author's [BUD-03](/en/topics/bud-03/) list. That is a practical improvement over media systems where the original host URL is the only locator.

## Interop Notes

Blossom is modular. Core retrieval and upload behavior lives in BUD-01 and BUD-02, while mirroring, media optimization, authorization, and URI sharing are split into separate BUDs.

That split lets clients implement the minimum needed for basic interoperability, then add optional pieces such as [BUD-10](/en/topics/bud-10/) URI hints or local caching as support matures.

---

**Primary sources:**
- [Blossom Repository](https://github.com/hzrd149/blossom)
- [BUD-01: Server requirements and blob retrieval](https://github.com/hzrd149/blossom/blob/master/buds/01.md)
- [BUD-02: Blob upload and management](https://github.com/hzrd149/blossom/blob/master/buds/02.md)
- [Local Blossom Cache guide](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md)
- [Hanami for Android](https://github.com/Letdown2491/hanami-android) - NIP-55 signer bridge and NIP-98 Blossom sessions
- [Formstr Drive 0.0.2](https://github.com/formstr-hq/formstr-drive/releases/tag/v0.0.2) - chunked Blossom storage and authenticated deletion
- [Code Call 0.2.66](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.66) - encrypted Blossom attachments for remote work sessions

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Notable Code Changes](/en/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)
- [Newsletter #10: Blossom local cache layer emerges](/en/newsletters/2026-02-18-newsletter/#blossom-local-cache-layer-emerges)
- [Newsletter #33: Lead stories](/en/newsletters/2026-07-29-newsletter/#top-stories)
- [Newsletter #36: Morganite 0.0.4: verifying a blob before it is cached](/en/newsletters/2026-08-19-newsletter/#morganite-004-verifying-a-blob-before-it-is-cached)
- [Newsletter #37: Postr launches as a small Android composer](/en/newsletters/2026-08-26-newsletter/#postr-launches-as-a-small-android-composer)

**See also:**
- [BUD-03: User Server List](/en/topics/bud-03/)
- [BUD-10: Blossom URI Scheme](/en/topics/bud-10/)
