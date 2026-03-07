---
title: "NIP-44: Encrypted Payloads"
date: 2025-12-31
draft: false
categories:
  - NIP
  - Cryptography
  - Privacy
---

NIP-44 defines a versioned encryption standard for Nostr payloads, replacing the flawed NIP-04 encryption scheme with modern cryptographic primitives.

## How It Works

NIP-44 version 2 uses a multi-step encryption process:

1. **Key Agreement**: ECDH (secp256k1) between sender and recipient public keys produces a shared secret
2. **Key Derivation**: HKDF-extract with SHA256 and salt `nip44-v2` creates a conversation key
3. **Per-Message Keys**: HKDF-expand derives ChaCha key, nonce, and HMAC key from a random nonce
4. **Padding**: Content is padded to hide message length
5. **Encryption**: ChaCha20 encrypts the padded content
6. **Authentication**: HMAC-SHA256 provides message integrity

The output is a versioned base64 payload that goes inside a normal signed Nostr event. The spec requires clients to validate the outer NIP-01 event signature before decrypting the inner NIP-44 payload.

## Cryptographic Choices

- **ChaCha20** over AES: Faster, better multi-key attack resistance
- **HMAC-SHA256** over Poly1305: Polynomial MACs are easier to forge
- **SHA256**: Consistent with existing Nostr primitives
- **Versioned Format**: Allows future algorithm upgrades

## Security Properties

- **Authenticated Encryption**: Messages cannot be tampered with
- **Length Hiding**: Padding obscures message size
- **Conversation Keys**: Same key for ongoing conversations reduces computation
- **Audited**: Cure53 security audit found no exploitable vulnerabilities

## Implementation Notes

NIP-44 is not a drop-in replacement for NIP-04 payloads. It defines an encryption format, not a direct-message event kind. Protocols such as [NIP-17](/en/topics/nip-17/) and [NIP-59](/en/topics/nip-59/) define how encrypted payloads are used in actual message flows.

The plaintext input is UTF-8 text with a length from 1 to 65535 bytes. That is a real constraint for implementers: if your application needs to encrypt arbitrary binary blobs, you need an additional encoding or a different container format.

## Limitations

NIP-44 does not provide:
- **Forward Secrecy**: Compromised keys expose past messages
- **Post-Compromise Security**: Recovery after key compromise
- **Deniability**: Messages are provably signed by specific keys
- **Metadata Hiding**: Relay architecture limits privacy

For high-security needs, NIP-104 (double ratchet) or MLS-based protocols like Marmot offer stronger guarantees.

## History

NIP-44 revision 3 was merged in December 2023 following an independent Cure53 security audit. It forms the cryptographic foundation for NIP-17 private DMs and NIP-59 gift wrapping.

---

**Primary sources:**
- [NIP-44 Specification](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44 Reference Implementations](https://github.com/paulmillr/nip44)
- [Cure53 Audit Report](https://cure53.de/audit-report_nip44-implementations.pdf)

**Mentioned in:**
- [Newsletter #4: NIP Deep Dive](/en/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Newsletter #3: December 2023](/en/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [Newsletter #3: December 2024](/en/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)
- [Newsletter #12: Marmot](/en/newsletters/2026-03-04-newsletter/#marmot-development-kit-ships-first-public-release)

**See also:**
- [NIP-04: Encrypted Direct Messages (deprecated)](/en/topics/nip-04/)
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
- [NIP-59: Gift Wrap](/en/topics/nip-59/)
- [NIP-104: Double Ratchet Encryption](/en/topics/nip-104/)
- [MLS: Message Layer Security](/en/topics/mls/)
