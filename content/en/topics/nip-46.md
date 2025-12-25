---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46 defines remote signing, allowing a signer application to hold keys while clients request signatures over Nostr relays.

## How It Works

1. Signer generates a connection URI (`bunker://` or `nostrconnect://`)
2. User pastes the URI into a client
3. Client sends signing requests as encrypted events to the signer's relay
4. Signer prompts user for approval, returns signed events

## Connection Methods

- **bunker://** - Signer-initiated connection
- **nostrconnect://** - Client-initiated connection via QR code or deep link

## Supported Operations

- `sign_event` - Sign an arbitrary event
- `get_public_key` - Retrieve the signer's public key
- `nip04_encrypt/decrypt` - NIP-04 encryption operations
- `nip44_encrypt/decrypt` - NIP-44 encryption operations

---

**Primary sources:**
- [NIP-46 Specification](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Mentioned in:**
- [Newsletter #1: Notable Code Changes](/en/newsletters/2025-12-17-newsletter/#amethyst-android)

**See also:**
- [NIP-55: Android Signer](/en/topics/nip-55/)
