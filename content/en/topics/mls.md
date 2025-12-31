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

Message Layer Security (MLS) is an IETF-standardized protocol for end-to-end encrypted group messaging. It provides efficient key establishment with forward secrecy and post-compromise security for groups ranging from two to thousands of participants.

## How It Works

MLS uses a tree-based key agreement structure called TreeKEM:

1. **Key Packages**: Each participant publishes a key package containing their identity and encryption keys
2. **Group State**: A ratchet tree maintains the group's cryptographic state
3. **Commits**: Members update the tree when joining, leaving, or rotating keys
4. **Message Encryption**: Content is encrypted using keys derived from the shared group secret

## Key Security Properties

- **Forward Secrecy**: Past messages remain secure even if current keys are compromised
- **Post-Compromise Security**: Future messages become secure again after key rotation
- **Membership Authentication**: All group members are cryptographically verified
- **Asynchronous Operation**: Members can join/leave without all participants being online
- **Scalability**: Efficient for groups up to 50,000 participants

## Standardization

- **RFC 9420** (July 2023): Core MLS protocol specification
- **RFC 9750** (April 2025): MLS architecture for system integration

## Adoption in Nostr

Several Nostr applications use MLS for secure group messaging:

- **KeyChat**: MLS-based encrypted messaging app for mobile and desktop
- **White Noise**: Private messaging using MLS with Marmot protocol integration
- **Marmot Protocol**: Nostr extension providing MLS-based group encryption

MLS offers stronger security guarantees than NIP-04 or NIP-44 alone, particularly for group chats where members join and leave dynamically.

## Industry Adoption

Beyond Nostr, MLS is being adopted by:
- Google Messages (RCS with MLS via GSMA Universal Profile 3.0)
- Apple Messages (RCS support announced for MLS)
- Cisco WebEx, Wickr, Matrix

---

**Primary sources:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**Mentioned in:**
- [Newsletter #3: Releases](/en/newsletters/2025-12-31-newsletter/#releases)

**See also:**
- [Marmot Protocol](/en/topics/marmot/)
- [MIP-05: Privacy-Preserving Push Notifications](/en/topics/mip-05/)
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
- [NIP-44: Encrypted Payloads](/en/topics/nip-44/)
