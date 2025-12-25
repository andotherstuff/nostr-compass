---
title: "NIP-55: Android Signer Application"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55 defines how Android applications can request signing operations from a dedicated signer app, allowing users to keep their private keys in one secure location while using multiple Nostr clients.

## How It Works

NIP-55 uses Android's content provider interface to expose signing operations. A signer app registers as a content provider, and other Nostr apps can request signatures without ever accessing the private key directly.

The flow:
1. Client app calls the signer's content provider
2. Signer shows approval UI to the user
3. User approves or denies the request
4. Signer returns the signature (or rejection) to the client

## Key Operations

- **get_public_key** - Retrieve the user's public key (call once during initial connection)
- **sign_event** - Sign a Nostr event
- **nip04_encrypt/decrypt** - Encrypt or decrypt NIP-04 messages
- **nip44_encrypt/decrypt** - Encrypt or decrypt NIP-44 messages

## Connection Initiation

A common implementation mistake is calling `get_public_key` repeatedly from background processes. The spec recommends calling it only once during initial connection setup, then caching the result.

---

**Primary sources:**
- [NIP-55 Specification](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Mentioned in:**
- [Newsletter #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)

**See also:**
- [NIP-46: Nostr Connect](/en/topics/nip-46/)
