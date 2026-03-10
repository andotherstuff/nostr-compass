---
title: "NIP-55: Android Signer Application"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55 defines how Android apps request signing and encryption operations from a separate signer application. It gives Android clients a native alternative to browser extensions and remote bunkers.

## How It Works

NIP-55 uses two Android mechanisms:

- **Intents** for foreground flows with explicit user approval
- **Content resolvers** for background flows after the user grants persistent permission

The usual connection flow starts with `get_public_key`. The signer returns both the user pubkey and the signer package name, and the client is expected to cache both. Repeating `get_public_key` in background loops is a common implementation mistake the spec explicitly warns against.

## Key Operations

- **get_public_key** - Retrieve the user's pubkey and signer package name
- **sign_event** - Sign a Nostr event
- **nip04_encrypt/decrypt** - Encrypt or decrypt NIP-04 messages
- **nip44_encrypt/decrypt** - Encrypt or decrypt NIP-44 messages
- **decrypt_zap_event** - Decrypt zap-related event payloads

## Security and UX Notes

NIP-55 keeps keys on-device, but it still depends on Android app boundaries and signer permission handling. Content resolver support gives a much smoother UX than repeated intent prompts, but only after the user has granted durable approval to that client.

For web apps on Android, NIP-55 is less ergonomic than NIP-46. Browser-based flows cannot receive direct background responses the way native Android apps can, so many implementations fall back to callback URLs, clipboard transfer, or manual paste.

---

**Primary sources:**
- [NIP-55 Specification](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Mentioned in:**
- [Newsletter #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #4: NIP Updates](/en/newsletters/2026-01-07-newsletter/#nip-updates)
- [Newsletter #11: NIP Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-55-android-signer-application)
- [Newsletter #13: Samizdat v1.0.0-alpha](/en/newsletters/2026-03-11-newsletter/#samizdat-v100-alpha)

**See also:**
- [NIP-46: Nostr Connect](/en/topics/nip-46/)
