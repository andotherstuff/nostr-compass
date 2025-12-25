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

## Standard Tags

NIP-24 also standardizes general-purpose tags:
- `r`: Web URL reference
- `i`: External identifier
- `title`: Name for various event types
- `t`: Hashtag (must be lowercase)

---

**Primary sources:**
- [NIP-24 Specification](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Mentioned in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
