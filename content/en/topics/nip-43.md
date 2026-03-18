---
title: "NIP-43: Relay Access Metadata and Requests"
date: 2026-03-18
draft: false
categories:
  - Protocol
  - Relay
  - Access Control
---

NIP-43 defines how relays publish membership information and how users request admission, invites, or removal from restricted relays. It gives relay access control a standard event surface instead of forcing every private or semi-private relay to invent its own join protocol.

## How It Works

The spec combines several event kinds:

- kind `13534` publishes a relay membership list
- kind `8000` announces that a member was added
- kind `8001` announces that a member was removed
- kind `28934` lets a user submit a join request with a claim code
- kind `28935` lets a relay return an invite code on demand
- kind `28936` lets a user request that their own access be revoked

Membership state is intentionally not derived from one event alone. A client may need to consult both the relay-signed membership events and the member's own events before deciding whether access is current.

## Why It Matters

NIP-43 gives restricted relays a standard way to express admission and membership state. That matters for group systems, invite-only communities, and relays that need machine-readable onboarding without dropping down to out-of-band web forms or manual operator workflows.

The open clarification in [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) tightens one practical point: relays should maintain one authoritative membership state per pubkey. That helps clients avoid ambiguous replay histories where an old add or remove event can be misread as current state.

## Interop Notes

NIP-43 depends on the relay advertising support through its [NIP-11](/en/topics/nip-11/) document. Join requests, invite requests, and leave requests should only be sent to relays that explicitly say they support this NIP.

Because the events sit in relay-controlled and user-controlled spaces at the same time, implementations need clear conflict rules. That is why the membership-state clarification matters more than it first appears.

---

**Primary sources:**
- [NIP-43 Specification](https://github.com/nostr-protocol/nips/blob/master/43.md)
- [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) - Clarify membership state handling

**Mentioned in:**
- [Newsletter #14: NIP Updates](/en/newsletters/2026-03-18-newsletter/#nip-updates)

**See also:**
- [NIP-11: Relay Information Document](/en/topics/nip-11/)
- [NIP-42: Authentication of Clients to Relays](/en/topics/nip-42/)
