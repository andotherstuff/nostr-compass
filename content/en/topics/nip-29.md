---
title: "NIP-29: Relay-based Groups"
date: 2025-12-24
draft: false
categories:
  - Social
  - Groups
---

NIP-29 defines relay-based groups, where a relay manages group membership, permissions, and message visibility.

## How It Works

Groups are keyed by a relay host plus a group id, and the relay is the authority for membership and moderation. User-created events sent into a group carry an `h` tag with the group id. Relay-generated metadata uses addressable events signed by the relay's own key.

The core metadata event is kind 39000, while kinds 39001 through 39003 describe admins, members, and supported roles. Moderation actions happen through 9000-series events such as `put-user`, `remove-user`, `edit-metadata`, and `create-invite`.

## Access Model

- **private**: Only members can read group messages
- **closed**: Join requests are ignored unless the relay uses invite-code handling
- **hidden**: Relay hides group metadata from non-members, making the group undiscoverable
- **restricted**: Only members can write messages to the group

These tags are independent. A group can be readable by everyone but writable only by members, or fully hidden from non-members. That separation matters because clients should not treat "private" as a blanket shorthand for every access rule.

## Trust Model

NIP-29 is not a trustless group protocol. The hosting relay decides which moderation events are valid, which roles exist, whether member lists are visible, and whether old or out-of-context messages are accepted. A client can verify signatures and timeline references, but it still relies on relay policy for the group's actual state.

That makes migration and forking possible, but not automatic. The same group id can exist on different relays with different histories or rules, so the relay URL is part of the group's identity in practice.

## Useful Implementation Notes

- Clients should treat the relay URL as the group host key. A January 2026 clarification made this explicit in the spec and removed ambiguity about using a pubkey instead
- Group state is reconstructed from moderation history, while 39000-series relay events are informative snapshots of that state
- Timeline `previous` references are there to prevent out-of-context rebroadcasting across relay forks, not just to improve UI threading

---

**Primary sources:**
- [NIP-29 Specification](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - Clarified `private`, `closed`, and `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - Clarified relay URL as the relay key
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - Added `unallowpubkey` and `unbanpubkey`

**Mentioned in:**
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #6: NIP Updates](/en/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #11: NIP Updates](/en/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12: NIP Updates](/en/newsletters/2026-03-04-newsletter/#nip-updates)

**See also:**
- [NIP-11: Relay Information Document](/en/topics/nip-11/)
