---
title: "NIP-19: Bech32-Encoded Entities"
shortname: nip-19
title-aliases:
  - Bech32 Encoding
  - npub
  - nsec
  - note
  - nevent
  - nprofile
  - naddr

categories:
  - Protocol
  - Identity

primary_sources:
  - title: NIP-19 Specification
    link: https://github.com/nostr-protocol/nips/blob/master/19.md

compass_mentions:
  - title: "Newsletter #1: NIP Deep Dive"
    url: /en/newsletters/2025/12/17/#nip-19-bech32-encoded-identifiers
    feature: true

see_also:
  - title: NIP-01 (Basic Protocol)
    link: /en/topics/nip-01/
  - title: NIP-21 (nostr: URI scheme)
    link: https://github.com/nostr-protocol/nips/blob/master/21.md
---

NIP-19 defines human-friendly formats for sharing Nostr identifiers. These bech32-encoded strings are used for display and sharing but are never used in the protocol itself (which uses hex).

## Why Bech32?

Raw hex keys are error-prone to copy and visually indistinguishable. Bech32 encoding adds a human-readable prefix and checksum, making it immediately clear what type of data you're looking at.

## Basic Formats

These encode raw 32-byte values:

- **npub** - Public key (your identity, safe to share)
- **nsec** - Private key (keep secret, used for signing)
- **note** - Event ID (references a specific event)

Example: The hex pubkey `3bf0c63f...` becomes `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

## Shareable Identifiers

These use TLV (Type-Length-Value) encoding to include metadata:

- **nprofile** - Profile with relay hints (helps clients find the user)
- **nevent** - Event with relay hints, author pubkey, and kind
- **naddr** - Addressable event reference (pubkey + kind + d-tag + relays)

These solve the discovery problem: when someone shares a note ID, how do clients know which relay has it? By bundling relay hints into the identifier, shared links become more reliable.

## Implementation Notes

- Use bech32 only for human interfaces: display, copy/paste, QR codes, URLs
- Never use bech32 formats in protocol messages, events, or NIP-05 responses
- All protocol communication must use hex encoding
- When generating nevent/nprofile/naddr, include relay hints for better discoverability
