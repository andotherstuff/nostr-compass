---
title: "BUD-10: Blossom URI Scheme"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-10 defines the `blossom:` URI scheme, a portable blob reference that can carry server hints, author hints, and expected size alongside the file hash.

## URI Format

```
blossom:<sha256>.<ext>?xs=<server>&as=<pubkey>&sz=<bytes>
```

The spec requires a lowercase 64-character SHA-256 hash and a file extension. If the extension is unknown, clients should fall back to `.bin`.

## How Resolution Works

Clients should resolve a `blossom:` URI in stages:

1. Try any `xs` server hints in the order they appear
2. If `as` author pubkeys are present, fetch each author's [BUD-03](/en/topics/bud-03/) server list and try those servers
3. Fall back to well-known servers or local cache if needed

That ordering is useful because it lets a sender attach immediate hints for fast retrieval while still giving receivers a recovery path if those hints go stale.

## Why It Matters

`blossom:` URIs work more like magnet links than ordinary media URLs. They describe what blob to fetch and include clues about where to find it, instead of assuming one host will remain available forever.

The optional `sz` field adds a concrete integrity check beyond the hash. Clients can verify expected size before or after download, which helps catch incomplete transfers and improves UX for large media.

---

**Primary sources:**
- [BUD-10 Specification](https://github.com/hzrd149/blossom/blob/master/buds/10.md)
- [Blossom Repository](https://github.com/hzrd149/blossom)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)

**See also:**
- [Blossom Protocol](/en/topics/blossom/)
- [BUD-03: User Server List](/en/topics/bud-03/)
