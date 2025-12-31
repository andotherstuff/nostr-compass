---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
draft: false
categories:
  - Cryptography
  - Protocol
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) is a threshold signature scheme that allows a group of participants to collaboratively produce valid Schnorr signatures without any single party holding the complete private key.

## How It Works

FROST enables T-of-N threshold signing, where T participants out of N total keyholders must cooperate to produce a valid signature. The protocol operates in two rounds:

1. **Commitment Round**: Each participant generates and shares cryptographic commitments
2. **Signature Round**: Participants combine their partial signatures into a final aggregate signature

The resulting signature is indistinguishable from a standard Schnorr signature, maintaining backward compatibility with existing verification systems.

## Key Properties

- **Threshold Security**: No single participant can sign alone; T parties must cooperate
- **Round Efficiency**: Only two rounds of communication required for signing
- **Forgery Protection**: Novel techniques protect against attacks on prior threshold schemes
- **Signature Aggregation**: Multiple signatures combine into a single compact signature
- **Privacy**: Final signatures reveal nothing about which T participants signed

## Use Cases in Nostr

In the context of Nostr, FROST enables:

- **Quorum Governance**: Groups can share an nsec through T-of-N schemes, where members can represent themselves or delegate to councils
- **Multi-sig Administration**: Community moderation requiring multiple admin signatures
- **Decentralized Key Management**: Distributing trust across multiple parties for critical operations

## Standardization

FROST was standardized as RFC 9591 in June 2024, titled "The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures."

---

**Primary sources:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [University of Waterloo CrySP](https://crysp.uwaterloo.ca/software/frost/)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**Mentioned in:**
- [Newsletter #3: NIPs Repository](/en/newsletters/2025-12-31-newsletter/#nips-repository)

**See also:**
- [NIP-XX Quorum Proposal](https://github.com/nostr-protocol/nips/pull/2179)
