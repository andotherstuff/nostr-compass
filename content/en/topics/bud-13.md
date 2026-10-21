---
title: "BUD-13: Path-based Blossom uploads"
date: 2026-10-21
draft: false
categories:
  - Protocols
---

BUD-13 is an optional draft Blossom specification for uploading a blob with `PUT /<sha256>`, where the path carries the lowercase hex hash of the body. The server hashes the exact bytes it receives. On a hash mismatch it returns `409 Conflict` and must discard the blob. Clients probe `OPTIONS /<sha256>`, and support is indicated when both `Allow` and `Access-Control-Allow-Methods` include `PUT`. The draft also defines optional `POST /<sha256>` mirroring from remote sources. Route96 merged an implementation in its PR #101 that hashes each upload in a request-owned temporary file before commit and keeps legacy endpoints. The upstream draft remains open as PR #100 after that merge.

## Primary sources

- [hzrd149/blossom PR #100: BUD-13 proposal](https://github.com/hzrd149/blossom/pull/100)
- [BUD-13 draft at commit 1fff6e4](https://github.com/hzrd149/blossom/blob/1fff6e47c29612ef5dd2e1158f9c511069417672/buds/13.md)
- [v0l/route96 PR #101: path-based uploads](https://github.com/v0l/route96/pull/101)

## Mentioned in

- [Newsletter #45](/en/newsletters/2026-10-21-newsletter/#route96)
