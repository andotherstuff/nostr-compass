---
title: "BUD-03: User Server List"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-03 defines how a user publishes their preferred Blossom servers, so clients know where to upload blobs and where to look when a media URL stops working.

## How It Works

Users publish a replaceable kind `10063` event with one or more `server` tags. Each tag contains a full Blossom server URL.

Clients can then:
- upload blobs to the user's preferred servers
- discover likely blob locations from the author's pubkey
- retry retrieval from the listed servers when an older URL breaks

## Reader-Useful Details

The order of `server` tags matters. The spec says users should list their most trusted or reliable servers first, and clients must at least try the first server for uploads. That means BUD-03 is not just a directory, it is also a weak preference signal.

The retrieval guidance is also practical: when a client extracts a blob hash from a URL, it should use the last 64-character hex string in the path. This helps clients recover blobs from both standard Blossom URLs and non-standard CDN-style URLs that still embed the hash.

---

**Primary sources:**
- [BUD-03 Specification](https://github.com/hzrd149/blossom/blob/master/buds/03.md)
- [Blossom Repository](https://github.com/hzrd149/blossom)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)

**See also:**
- [Blossom Protocol](/en/topics/blossom/)
- [NIP-51: Lists](/en/topics/nip-51/)
