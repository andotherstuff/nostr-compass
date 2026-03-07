---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
draft: false
categories:
  - Cryptography
  - Protocol
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) is a threshold signature scheme that lets a group produce one valid Schnorr signature without any participant holding the full private key.

## How It Works

FROST enables T-of-N signing. Any threshold set of participants can cooperate to produce a signature for the group's public key.

The signing protocol uses two rounds:

1. **Commitment Round**: Each participant generates and shares cryptographic commitments
2. **Signature Round**: Participants combine their partial signatures into a final aggregate signature

The final output verifies like an ordinary Schnorr signature. Verifiers see one signature under one public key, not a list of cosigners.

## Security Notes

Nonce handling is critical. The RFC is explicit that signing nonces are one-time use. Reuse can leak key material.

The RFC also does not standardize distributed key generation. It specifies the signing protocol itself and includes trusted-dealer key generation only as an appendix. In practice, the safety of a FROST deployment depends on both the signing flow and how shares were created and stored.

## Use Cases in Nostr

In the context of Nostr, FROST can support:

- **Quorum Governance**: Groups can share an nsec through T-of-N schemes, where members can represent themselves or delegate to councils
- **Multi-sig Administration**: Community moderation requiring multiple admin signatures
- **Decentralized Key Management**: Distributing trust across multiple parties for critical operations

## Status

FROST is specified in [RFC 9591](https://datatracker.ietf.org/doc/rfc9591/), published on the IRTF stream in June 2024. That gives the protocol a stable public specification, but it is not an IETF standards-track RFC.

---

**Primary sources:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**Mentioned in:**
- [Newsletter #3: NIPs Repository](/en/newsletters/2025-12-31-newsletter/#nips-repository)
- [Newsletter #8](/en/newsletters/2026-02-04-newsletter/)
- [Newsletter #10](/en/newsletters/2026-02-18-newsletter/)

**See also:**
- [NIP-46: Nostr Connect](/en/topics/nip-46/)
- [NIP-55: Android Signer Application](/en/topics/nip-55/)
