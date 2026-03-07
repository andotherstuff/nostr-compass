---
title: "NIP-19: Bech32-Encoded Entities"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-19 defines human-friendly formats for sharing Nostr identifiers. These bech32-encoded strings are used for display and sharing but are never used in the protocol itself (which uses hex).

## How It Works

Raw hex keys are error-prone to copy and visually indistinguishable. Bech32 encoding adds a human-readable prefix and checksum, making it clear what type of data you are looking at and catching many copy errors.

The basic forms encode a single 32-byte value:

- **npub** - Public key (your identity, safe to share)
- **nsec** - Private key (keep secret, used for signing)
- **note** - Event ID (references a specific event)

Example: The hex pubkey `3bf0c63f...` becomes `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

The extended forms use TLV encoding so they can carry lookup hints alongside the identifier itself:

- **nprofile** - Profile with relay hints
- **nevent** - Event with relay hints, author pubkey, and kind
- **naddr** - Addressable event reference with pubkey, kind, `d` tag, and relay hints

## Why It Matters

Relay hints are not authoritative, but they often decide whether a client can fetch a shared event on the first try. This is why `nevent`, `nprofile`, and `naddr` are usually better sharing formats than bare `note` or `npub` values when content lives outside the recipient's current relay set.

Another practical distinction is stability. `note` points to one immutable event id, while `naddr` points to an addressable event that can be replaced over time. For long-form content, calendars, or repository announcements, `naddr` is usually the right link type.

## Implementation Notes

- Use bech32 only for human interfaces: display, copy/paste, QR codes, URLs
- Never use bech32 formats in protocol messages, events, or NIP-05 responses
- All protocol communication must use hex encoding
- When generating nevent/nprofile/naddr, include relay hints for better discoverability
- Treat `nsec` as secret material everywhere. A client should never display it by default, log it, or include it in support exports

---

**Primary sources:**
- [NIP-19 Specification](https://github.com/nostr-protocol/nips/blob/master/19.md)

**Mentioned in:**
- [Newsletter #1: NIP Deep Dive](/en/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#damus-ios)
- [Newsletter #4: Relay Hint Support](/en/newsletters/2026-01-07-newsletter/)
- [Newsletter #8: Damus iOS](/en/newsletters/2026-02-04-newsletter/#damus-ios)
- [Newsletter #11: notecrumbs](/en/newsletters/2026-02-25-newsletter/)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
- [NIP-10: Reply Threads](/en/topics/nip-10/)
