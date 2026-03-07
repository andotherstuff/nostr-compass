---
title: "NIP-09: Event Deletion Request"
date: 2026-02-25
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-09 defines a way for authors to request deletion of events they previously published. It is a relay-side deletion signal, not a network-wide erase function.

## How It Works

Users publish kind 5 events containing references to events they want deleted. Relays that support NIP-09 should stop serving matching events from the same author and may remove them from storage.

Deletion is a request, not a guarantee. Relays may ignore deletion requests, and events may already have propagated to relays that do not support deletion. Users should not rely on NIP-09 for privacy-sensitive content removal.

## Why It Matters

NIP-09 gives clients and relays a common way to express "this event should no longer appear," which is useful for accidental posts, wallet state rollover, and moderation workflows. But the author can only request deletion of their own events. It is not a general-purpose takedown mechanism for third-party content.

## Tradeoffs

The weak point is propagation. Once an event has been mirrored across multiple relays, deletion becomes best-effort. Some relays will delete it, some will tombstone it, and some will keep serving it indefinitely. Clients that present deletion as final are overstating what the protocol guarantees.

Another practical issue is references. Users and apps may still hold the deleted event locally, or quote it elsewhere, even after a compliant relay stops serving it.

---

**Primary sources:**
- [NIP-09 Specification](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Mentioned in:**
- [Newsletter #11: NIP-60 Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)
- [Newsletter #12: News](/en/newsletters/2026-03-04-newsletter/#news)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
- [NIP-60: Cashu Wallet](/en/topics/nip-60/)
