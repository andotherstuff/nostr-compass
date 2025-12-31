---
title: "Quartz"
date: 2025-12-31
draft: false
categories:
  - Library
  - Development
---

Quartz is a Kotlin Multiplatform library for Nostr developed by Vitor Pamplona. Originally extracted from the Amethyst Android client, Quartz provides reusable Nostr protocol implementations across JVM, Android, iOS, and Linux platforms.

## How It Works

Quartz provides core Nostr functionality as a shared library:

- **Event Handling**: Parsing, validation, and creation of Nostr events
- **Cryptography**: Secp256k1 signing, NIP-44 encryption, key management
- **Relay Communication**: Connection management, message ordering, subscription handling
- **NIP Support**: Implementation of common NIPs including NIP-06, NIP-19, NIP-44, and more

## Key Features

- **Kotlin Multiplatform**: Single codebase compiles to multiple targets
- **Platform Targets**: Android, JVM, iOS (ARM64, Simulator), Linux
- **Performance Optimized**: Efficient event processing and cryptographic operations
- **Blossom Integration**: Support for media uploads via Blossom protocol
- **OpenTimestamp**: Full Kotlin port of timestamp verification

## Architecture

The library uses a modular source set structure:
- `commonMain`: Shared code for all platforms
- `jvmAndroid`: Code shared between JVM and Android
- `androidMain`: Android-specific implementations
- `jvmMain`: Desktop JVM implementations
- `iosMain`: iOS-specific implementations

## OpenSats Grant

In December 2025, OpenSats announced funding for Quartz as part of their fourteenth wave of Nostr grants. The grant supports continued development toward enabling Amethyst on iOS through the same Kotlin Multiplatform approach that already powers the Android and desktop versions.

---

**Primary sources:**
- [Quartz on Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Amethyst Repository](https://github.com/vitorpamplona/amethyst)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: News](/en/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Amethyst Notable Changes](/en/newsletters/2025-12-31-newsletter/#amethyst-android)

**See also:**
- [Blossom Protocol](/en/topics/blossom/)
