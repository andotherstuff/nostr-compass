---
title: "NIP-24: Extra Metadata Fields"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-24 defines additional optional fields for kind 0 user metadata beyond the basic name, about, and picture.

## Extra Metadata Fields

- **display_name**: An alternative, bigger name with richer characters than `name`
- **website**: A web URL related to the event author
- **banner**: URL to a wide (~1024x768) picture for optional background display
- **bot**: Boolean indicating content is entirely or partially automated
- **birthday**: Object with optional year, month, and day fields

The spec also marks two older fields as deprecated: `displayName` should become `display_name`, and `username` should become `name`. Clients still see these in the wild, so a tolerant parser helps with backwards compatibility even if a writer should not emit them.

## Standard Tags

NIP-24 also standardizes general-purpose tags:
- `r`: Web URL reference
- `i`: External identifier
- `title`: Name for various event types
- `t`: Hashtag (must be lowercase)

## Why It Matters

NIP-24 is mostly about convergence. These fields and tags were already appearing across clients, so the spec gives them consistent names and meanings. That reduces small but annoying incompatibilities such as clients disagreeing on whether a banner lives under `banner` or some app-specific key.

One practical point for implementers is that kind 0 remains a hot path in most clients. Extra metadata should stay lightweight. If a field needs its own fetch pattern or independent update cycle, it probably belongs in a separate event kind instead of bloating profile metadata.

---

**Primary sources:**
- [NIP-24 Specification](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
