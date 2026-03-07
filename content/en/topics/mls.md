---
title: "MLS (Message Layer Security)"
date: 2025-12-31
draft: false
categories:
  - Cryptography
  - Protocol
  - Messaging
  - Privacy
---

Message Layer Security (MLS) is an IETF protocol for end-to-end encrypted group messaging. It provides forward secrecy and post-compromise security for groups that may change membership over time.

## How It Works

MLS uses a tree-based key agreement structure called TreeKEM:

1. **Key Packages**: Each participant publishes a key package containing their identity and encryption keys
2. **Group State**: A ratchet tree maintains the group's cryptographic state
3. **Commits**: Members update the tree when joining, leaving, or rotating keys
4. **Message Encryption**: Content is encrypted using keys derived from the shared group secret

## Why It Matters

MLS solves a problem that pairwise encryption does not solve well: keeping group membership and encryption state coherent as members join, leave, or rotate keys asynchronously.

Its tree structure is the practical insight. Updates do not require every participant to renegotiate pairwise with everyone else, so the protocol scales much better than ad hoc group-key schemes.

## Standardization

- **RFC 9420** (July 2023): Core MLS protocol specification
- **RFC 9750** (April 2025): MLS architecture for system integration

## Adoption In Nostr

Several Nostr applications use MLS for secure group messaging:

- **KeyChat**: MLS-based encrypted messaging app for mobile and desktop
- **White Noise**: Private messaging using MLS with Marmot protocol integration
- **Marmot Protocol**: Nostr extension providing MLS-based group encryption

MLS offers stronger group-security guarantees than [NIP-04](/en/topics/nip-04/) or [NIP-44](/en/topics/nip-44/) alone, especially when membership changes frequently.

## Tradeoffs

MLS is not a full messaging product. Applications still need identity, transport, spam resistance, storage, and conflict handling around the protocol.

That is why Nostr projects such as Marmot add extra rules on top of MLS. The cryptography is standardized, but the surrounding application protocol still matters for interoperability.

---

**Primary sources:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**Mentioned in:**
- [Newsletter #3: Releases](/en/newsletters/2025-12-31-newsletter/#releases)
- [Newsletter #10](/en/newsletters/2026-02-18-newsletter/)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**See also:**
- [Marmot Protocol](/en/topics/marmot/)
- [MIP-05: Privacy-Preserving Push Notifications](/en/topics/mip-05/)
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
- [NIP-44: Encrypted Payloads](/en/topics/nip-44/)
