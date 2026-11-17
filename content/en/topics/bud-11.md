---
title: "BUD-11: Blossom Delegation (Proposed)"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

BUD-11 is an open Blossom proposal, [#118](https://github.com/hzrd149/blossom/pull/118), that would let a storage owner delegate limited rights to another signing key. Blossom servers store files by hash and authorize requests with kind 24242 Nostr events. Under the proposal, the owner signs a kind 24244 token. The token names one actor, lists explicit verbs, requires server scopes and sets an expiry. The actor puts the token inside its own kind 24242 authorization. The server scopes and hash scopes of the two events intersect. Storage ownership stays with the delegator.

The owner revokes a delegation with a marker blob under their direct control. While the marker exists, the delegation is disabled. Deleting the marker turns the delegation back on. Tokens must not be published to relays. Mailstr attachments motivated the proposal. It is unmerged, and no server or client has been shown to conform to it.

**Primary sources:**
- [Blossom PR #118: BUD-11 delegation](https://github.com/hzrd149/blossom/pull/118)

**Mentioned in:**
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#hzrd149-blossom-118)

**See also:**
- [Blossom](/en/topics/blossom/)
- [BUD-04: Mirroring](/en/topics/bud-04/)
- [Scoped Data Grants](/en/topics/scoped-data-grants/)
