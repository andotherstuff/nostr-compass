---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46 defines remote signing over Nostr relays. A client talks to a separate signer, often called a bunker, so signing keys can stay outside the app the user is actively using.

## How It Works

1. The client generates a local keypair used only for the bunker session.
2. The connection is established with either a `bunker://` or `nostrconnect://` URI.
3. Client and signer exchange encrypted kind `24133` request and response events over relays.
4. After connecting, the client calls `get_public_key` to learn the actual user pubkey it is signing for.

## Connection Methods

- **bunker://** - Signer-initiated connection
- **nostrconnect://** - Client-initiated connection via QR code or deep link

`nostrconnect://` flows include a required shared secret so the client can verify that the first response really came from the intended signer. That prevents simple connection spoofing.

## Supported Operations

- `sign_event` - Sign an arbitrary event
- `get_public_key` - Retrieve the user's pubkey from the signer
- `nip04_encrypt/decrypt` - NIP-04 encryption operations
- `nip44_encrypt/decrypt` - NIP-44 encryption operations
- `switch_relays` - Ask the signer for an updated relay set

Many implementations also use permission strings such as `sign_event:1` or `nip44_encrypt` during setup so the signer can approve a narrow scope instead of full access.

## Relay and Trust Model

NIP-46 moves private keys out of the client, but it does not remove trust from the signer. The signer can approve, deny, or delay requests, and it sees every operation the client asks it to perform. Relay choice also matters because the protocol depends on request and response delivery over relays both sides can reach.

The `switch_relays` method exists so the signer can move the session to a different relay set over time. Clients that ignore it will work less reliably when signer relay preferences change.

---

**Primary sources:**
- [NIP-46 Specification](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Mentioned in:**
- [Newsletter #1: Notable Code Changes](/en/newsletters/2025-12-17-newsletter/#amethyst-android)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #4: Primal Android Becomes a Full Signing Hub](/en/newsletters/2026-01-07-newsletter/#primal-android-becomes-a-full-signing-hub)
- [Newsletter #12: NDK Collaborative Events and NIP-46 Timeout](/en/newsletters/2026-03-04-newsletter/#ndk-collaborative-events-and-nip-46-timeout)

**See also:**
- [NIP-55: Android Signer](/en/topics/nip-55/)
