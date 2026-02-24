---
title: "NIP-09"
date: 2026-02-25
draft: false
categories:
  - NIP
  - Protocol
---

NIP-09 defines Event Deletion, a mechanism for users to request that relays remove their previously published events.

## How It Works

Users publish kind 5 events containing `e` tags referencing the event IDs they want deleted. Relays that support NIP-09 should stop serving the referenced events and may delete them from storage.

Deletion is a request, not a guarantee. Relays may ignore deletion requests, and events may have already propagated to relays that do not support deletion. Users should not rely on NIP-09 for privacy-sensitive content removal.

## Key Features

- Kind 5 deletion request events
- Reference deleted events by ID via e tags
- Optional reason field for deletion context
- Relay compliance is voluntary

---

**Primary sources:**
- [NIP-09 Specification](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Mentioned in:**
- [Newsletter #11: NIP-60 Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)

**See also:**
- [NIP-60: Cashu Wallet](/en/topics/nip-60/)
