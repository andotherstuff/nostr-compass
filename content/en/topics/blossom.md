---
title: "Blossom Protocol"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

Blossom is a media hosting protocol for Nostr that provides decentralized file storage with content-addressable URLs.

## How It Works

Files are stored on Blossom servers and addressed by their SHA256 hash. This means:
- The same file always has the same URL across all servers
- Files can be retrieved from any server that has them
- Clients can verify file integrity by checking the hash

## Features

- Content-addressable storage
- Multiple server redundancy
- Author discovery via BUD-03
- Custom URI scheme via BUD-10
- Cursor-based pagination on `/list` endpoint

---

**Primary sources:**
- [Blossom Repository](https://github.com/hzrd149/blossom)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Notable Code Changes](/en/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)

**See also:**
- [BUD-03: User Server List](/en/topics/bud-03/)
- [BUD-10: Blossom URI Scheme](/en/topics/bud-10/)
