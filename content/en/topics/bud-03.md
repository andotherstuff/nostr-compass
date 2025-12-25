---
title: "BUD-03: User Server List"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-03 defines how users publish their preferred Blossom servers, enabling clients to discover where to upload and retrieve a user's media files.

## How It Works

Users publish a kind 10063 event listing their Blossom servers. Clients can then:
- Upload media to the user's preferred servers
- Discover where to find a user's blobs when given their pubkey

This enables author-based discovery as an alternative to embedding server URLs directly in content.

---

**Primary sources:**
- [BUD-03 Specification](https://github.com/hzrd149/blossom/blob/master/buds/03.md)

**See also:**
- [Blossom Protocol](/en/topics/blossom/)
- [NIP-51: Lists](/en/topics/nip-51/)
