---
title: "BUD-10: Blossom URI Scheme"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-10 defines a custom URI scheme for Blossom that embeds all information needed to retrieve a file from any available server.

## URI Format

```
blossom:<sha256>.<ext>?size=<bytes>&server=<url>&server=<url>&pubkey=<hex>
```

Components:
- **sha256**: File hash (required)
- **ext**: File extension
- **size**: File size in bytes
- **server**: One or more server hints
- **pubkey**: Author pubkeys for BUD-03 server discovery

## Benefits

- More resilient than static HTTP URLs
- Automatic fallback across multiple servers
- Author-based discovery via pubkey hints
- Self-verifying (hash ensures integrity)

---

**Primary sources:**
- [BUD-10 PR](https://github.com/hzrd149/blossom/pull/84)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)

**See also:**
- [Blossom Protocol](/en/topics/blossom/)
- [BUD-03: User Server List](/en/topics/bud-03/)
