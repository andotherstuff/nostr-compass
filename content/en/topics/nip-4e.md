---
title: "NIP-4E: Decoupling Encryption from Identity"
date: 2026-07-15
draft: false
categories:
  - NIP
  - Protocol
  - Encryption
---

NIP-4E is an open draft, proposed by fiatjaf, for sharing private data between a user's own devices without every device holding that user's main Nostr identity key. It is not merged and remains a `draft`/`optional` proposal.

## The Problem It Addresses

Many existing NIPs, including NIP-51 lists and NIP-60 Cashu wallets, encrypt data from a user to themselves using the identity key so it can be read back later on any device. That breaks down when the identity key isn't directly accessible, for example when a remote signer is protected by FROST threshold shares, MuSig2, or a hosted secure enclave, since encrypting and decrypting then requires a round trip to that signer every time. It also makes offline encryption impossible whenever the signing key lives in a remote bunker.

## How It Works

NIP-4E separates a per-device "client key" from a shared "encryption key" that is not the user's identity key:

1. The first client a user sets up generates a random encryption keypair and announces its public half in a `kind:10044` event signed by the user's identity key.
2. Any other client that wants to encrypt or decrypt data for that user computes its Diffie-Hellman shared secret against the announced encryption key rather than the identity key.
3. When a second device installs a new client, that client generates its own local "client key" and publishes a `kind:4454` announcement (also signed by the user's identity key) asking the first client to share the encryption key with it.
4. The original client detects the new `kind:4454` announcement, encrypts the shared encryption key to the new client's key using [NIP-44](/en/topics/nip-44/), and publishes it so the new client can decrypt and use it going forward.

The result is that encryption and decryption never require asking the identity-key signer at all once a client holds the shared encryption key locally, and a remote-signer setup (FROST, MuSig2, hosted enclave) can be used for identity while ordinary encryption stays fast and works offline.

## Why It Matters

NIP-4E is cited as the foundation for other proposals that need a drive-wide or account-wide symmetric key without depending on a remote signer for every encrypt/decrypt call, including a private encrypted drive proposal ([PR #2412](https://github.com/nostr-protocol/nips/pull/2412)) and a narrower NIP-17-specific version of the same idea ([PR #2361](https://github.com/nostr-protocol/nips/pull/2361)). Both remain open alongside NIP-4E itself, making this an active, unsettled area of the protocol rather than a finished building block.

---

**Primary sources:**
- [NIP-4E draft, PR #1647](https://github.com/nostr-protocol/nips/pull/1647)

**Mentioned in:**
- [Newsletter #31: Open: private encrypted drive extends NIP-4E](/en/newsletters/2026-07-15-newsletter/#open-private-encrypted-drive-extends-nip-4e)

**See also:**
- [NIP-44: Encrypted Payloads](/en/topics/nip-44/)
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
- [NIP-46: Nostr Connect](/en/topics/nip-46/)
- [FROST](/en/topics/frost/)
