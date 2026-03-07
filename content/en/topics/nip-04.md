---
title: "NIP-04: Encrypted Direct Messages (Deprecated)"
date: 2025-12-31
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-04 defines encrypted direct messages using kind 4 events and an ECDH-derived shared secret. It was Nostr's first DM scheme, but it is now legacy technology and new private messaging work has moved to NIP-17.

## How It Works

Messages use kind 4 events with this basic flow:

1. The sender derives a shared secret with secp256k1 ECDH.
2. The plaintext is encrypted with AES-256-CBC.
3. The event includes a `p` tag naming the recipient.
4. The ciphertext is encoded as base64 and stored in `content` together with the IV.

The event itself is still a normal signed Nostr event, so relays can see the outer metadata even though they cannot read the plaintext.

## Security and Privacy Limits

NIP-04 has significant privacy shortcomings:

- **Metadata leakage** - The sender's pubkey is publicly visible on every message
- **No sender privacy** - Anyone can see who is messaging whom
- **Exact timestamps** - Message timing is not randomized
- **Non-standard key handling** - The scheme uses only the X coordinate of the ECDH point, which made cross-library correctness harder and left little room for protocol evolution

The specification explicitly warns that it "does not go anywhere near the state-of-the-art in encrypted communication."

## Why It Was Replaced

NIP-04 encrypts message content, but it does not hide the social graph. Relay operators can still see who sent the event, who receives it, and when it was published. That is enough metadata to map conversations even without decrypting the payload.

NIP-17 addresses this by combining NIP-44 payload encryption with NIP-59 gift wrapping, which hides the sender from relays and random observers. New implementations should treat NIP-04 as compatibility-only.

## Implementation Status

Legacy clients and signers still expose NIP-04 encrypt/decrypt methods because old conversations and older apps remain in circulation. That compatibility layer matters for migration, but building new features on top of kind 4 events usually means carrying old privacy limits forward.

---

**Primary sources:**
- [NIP-04 Specification](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Mentioned in:**
- [Newsletter #4: NIP Deep Dive](/en/newsletters/2026-01-07-newsletter/#nip-04-encrypted-direct-messages-legacy)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-44: Encrypted Payloads](/en/topics/nip-44/)
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
- [NIP-59: Gift Wrap](/en/topics/nip-59/)
