---
title: "NIP-49: Private Key Encryption"
date: 2026-03-11
draft: false
categories:
  - NIPs
  - Key Management
  - Security
---

NIP-49 defines how a client can encrypt a user's private key with a password and encode the result as an `ncryptsec` string. The goal is portability with stronger defaults than storing a raw `nsec`, while still keeping the encrypted key easy to move between clients.

## How It Works

The client starts with the raw 32-byte secp256k1 private key, not a hex or bech32 string. It derives a temporary symmetric key from the user's password with scrypt, using a per-key random salt and an adjustable work factor stored as `LOG_N`. It then encrypts the private key with XChaCha20-Poly1305, prepends versioning and key-handling metadata, and bech32-encodes the result under the `ncryptsec` prefix.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

The event above is an example container, not a NIP-49 requirement. NIP-49 standardizes the encrypted key format itself, not a dedicated event kind for publishing it. Clients can store an `ncryptsec` locally, sync it through app-specific storage, or present it as a backup export.

## Security Model

NIP-49 does two things at once. It turns a user password into a proper encryption key, and it slows down brute-force recovery attempts with a memory-hard KDF. The work factor matters. Higher `LOG_N` values make decryption slower for legitimate users, but they also raise the cost of offline guessing for attackers.

The format also carries a one-byte flag describing whether the key has ever been handled insecurely before encryption. That does not change the ciphertext itself, but it gives clients a way to distinguish a newly generated protected backup from a key that was already pasted around in plaintext before being wrapped.

## Implementation Notes

- Passwords are normalized to Unicode NFKC before key derivation so the same password can be entered consistently across clients.
- XChaCha20-Poly1305 uses a 24-byte nonce and authenticated encryption, so tampering with the ciphertext fails cleanly during decryption.
- The symmetric key should be zeroed and discarded after use.
- The spec does not recommend posting encrypted keys to public relays, because collecting many encrypted keys improves an attacker's offline cracking position.

## Implementations

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Adds signup compatibility using NIP-49 encrypted private keys

---

**Primary sources:**
- [NIP-49 Specification](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Client-side signup flow using NIP-49

**Mentioned in:**
- [Newsletter #13: Formstr](/en/newsletters/2026-03-11-newsletter/#formstr)
- [Newsletter #13: NIP Deep Dive](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49-private-key-encryption)

**See also:**
- [NIP-46: Nostr Connect](/en/topics/nip-46/)
- [NIP-55: Android Signer Application](/en/topics/nip-55/)
