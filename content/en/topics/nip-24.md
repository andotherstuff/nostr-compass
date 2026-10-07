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

The spec also marks two older fields as deprecated: `displayName` and `username` should be ignored or removed. Authors should always include `name` even when they also supply `display_name`. Malformed-field recovery remains client policy; a signature authenticates the exact payload, including incorrect field types.

## Standard Tags

NIP-24 also standardizes general-purpose tags:
- `r`: Web URL reference
- `i`: External identifier
- `title`: Name for various event types
- `t`: Hashtag (must be lowercase)

These generic meanings apply when a more specific NIP supplies no other meaning. Kind-3 relay-map content is deprecated in favor of [NIP-65 relay lists](/en/topics/nip-65/). Partial birthdays can omit year, month or day; any supplied details remain public.

## Why It Matters

NIP-24 is mostly about convergence. These fields and tags were already appearing across clients, so the spec gives them consistent names and meanings. That reduces small but annoying incompatibilities such as clients disagreeing on whether a banner lives under `banner` or some app-specific key.

One practical point for implementers is that kind 0 remains a hot path in most clients. Extra metadata should stay lightweight. If a field needs its own fetch pattern or independent update cycle, it probably belongs in a separate event kind instead of bloating profile metadata.

---

**Primary sources:**
- [NIP-24 Specification](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Mentioned in:**
- [Newsletter #43](/en/newsletters/2026-10-07-newsletter/#nip-deep-dive-nip-05-and-nip-24)
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #42: September 2023 metadata](/en/newsletters/2026-09-30-newsletter/#september-2023-clients-grow-up-around-relay-discovery-and-metadata)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
