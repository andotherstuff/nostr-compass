---
title: "NIP-29: Relay-based Groups"
date: 2025-12-24
draft: false
categories:
  - Social
  - Groups
---

NIP-29 defines relay-based groups, where a relay manages group membership, permissions, and message visibility.

## Group Access Tags

- **private**: Only members can read group messages
- **closed**: Join requests are ignored (invitation-only)
- **hidden**: Relay hides group metadata from non-members, making the group undiscoverable
- **restricted**: Only members can write messages to the group

These tags can be combined. A group can be `restricted` (write-limited) but not `hidden` (still discoverable). Omitting a tag enables the opposite behavior: no `private` means anyone can read, no `closed` means join requests are honored.

## How It Works

The relay is the authority for group operations:
- Maintains member list and roles
- Enforces write permissions
- Controls what non-members can see

Clients send group messages to the relay, which validates membership before accepting them.

## Privacy Considerations

- `hidden` groups provide the strongest discoverability protection: they don't appear in searches or relay listings
- `private` groups hide message content from non-members
- `closed` groups simply ignore join requests; combine with `private` or `hidden` for stronger access control
- `restricted` controls who can write, independent of read access

---

**Primary sources:**
- [NIP-29 Specification](https://github.com/nostr-protocol/nips/blob/master/29.md)

**Mentioned in:**
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
