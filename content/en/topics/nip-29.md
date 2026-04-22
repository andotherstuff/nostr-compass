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

## Recent Spec Work

- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) and hodlbod's [Flotilla 1.7.3/1.7.4 release notes](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4) propose kind-9 wrapping of non-chat content types (calendar events, polls, other payloads) so the room context is preserved when those objects are sent into a group.
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) extends the spec with a subgroup hierarchy so a single group can host multiple parallel channels without spawning independent groups on the same relay; the subgroup identifier piggybacks on the existing `h` tag, preserving single-`h`-tag messages for older clients.
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) defines explicit permissions on the kind `39003` role event so each role becomes a named set of granted operations (invite, add-user, remove-user, edit-metadata, delete-event, add-permission) with an optional time-bound expiry.

## Implementations

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) is hodlbod's primary NIP-29 client; [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3) and [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4) shipped kind-9 wrapping, polls, [NIP-46](/en/topics/nip-46/) login via the Aegis URL scheme, native share support for space invites, room mentions, mobile clipboard image paste, drafts, and video in calls.
- [Wisp](https://github.com/barrydeen/wisp) added NIP-29 group configuration for flags, invites, roles, and AUTH prompts in [PR #471](https://github.com/barrydeen/wisp/pull/471) and hardened AUTH sequencing before group `9021`, `9007`, and `9009` events in [PR #478](https://github.com/barrydeen/wisp/pull/478).

---

**Primary sources:**
- [NIP-29 Specification](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - Clarified `private`, `closed`, and `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - Clarified relay URL as the relay key
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - Added `unallowpubkey` and `unbanpubkey`
- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) - Kind-9 wrapping for non-chat content
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) - Subgroups spec
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) - Explicit role permissions on kind 39003
- [Flotilla 1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)
- [Wisp PR #471](https://github.com/barrydeen/wisp/pull/471) - NIP-29 group configuration

**Mentioned in:**
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #6: NIP Updates](/en/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #11: NIP Updates](/en/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12: NIP Updates](/en/newsletters/2026-03-04-newsletter/#nip-updates)
- [Newsletter #19: Flotilla 1.7.3/1.7.4](/en/newsletters/2026-04-22-newsletter/#flotilla-173-and-174-add-kind-9-wrapping-for-richer-nip-29-rooms)
- [Newsletter #19: Wisp NIP-29 config](/en/newsletters/2026-04-22-newsletter/#wisp-v0180-beta-adds-normie-mode-for-you-feed-and-nip-29-group-config)
- [Newsletter #19: NIP Updates (subgroups, role permissions)](/en/newsletters/2026-04-22-newsletter/#nip-updates)

**See also:**
- [NIP-11: Relay Information Document](/en/topics/nip-11/)
