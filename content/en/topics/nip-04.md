---
title: "NIP-04: Encrypted Direct Messages (Deprecated)"
date: 2025-12-31
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-04 defines encrypted direct messages using AES-256-CBC encryption. It was the original method for private messaging on Nostr but has been deprecated in favor of NIP-17 due to significant privacy limitations.

## How It Works

Messages use kind 4 events with the following encryption scheme:
1. A shared secret is generated using ECDH with the recipient's public key and sender's private key
2. The message is encrypted with AES-256-CBC
3. The ciphertext is base64-encoded with the initialization vector appended
4. A `p` tag identifies the recipient's public key

## Security Limitations

NIP-04 has significant privacy shortcomings:

- **Metadata leakage** - The sender's pubkey is publicly visible on every message
- **No sender privacy** - Anyone can see who is messaging whom
- **Exact timestamps** - Message timing is not randomized
- **Non-standard implementation** - Uses only the X coordinate of the ECDH point rather than the standard SHA256 hash

The specification explicitly warns that it "does not go anywhere near the state-of-the-art in encrypted communication."

## Deprecation Status

NIP-04 is deprecated in favor of NIP-17, which uses NIP-59 gift wrapping to hide the sender's identity. New implementations should use NIP-17 for private messaging.

---

**Primary sources:**
- [NIP-04 Specification](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
- [NIP-59: Gift Wrap](/en/topics/nip-59/)
