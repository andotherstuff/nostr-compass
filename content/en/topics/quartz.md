---
title: "Quartz"
date: 2025-12-31
draft: false
categories:
  - Library
  - Development
---

Quartz is a Kotlin Multiplatform Nostr library developed by Vitor Pamplona. It is the shared protocol and data layer behind Amethyst's push toward Android, desktop, and eventually iOS from one codebase.

## How It Works

Quartz provides core Nostr functionality as a shared library:

- **Event Handling**: Parsing, validation, and creation of Nostr events
- **Cryptography**: Secp256k1 signing, NIP-44 encryption, key management
- **Relay Communication**: Connection management, message ordering, subscription handling
- **NIP Support**: Implementation of common NIPs including NIP-06, NIP-19, NIP-44, and more

## Why It Matters

Quartz moves protocol-heavy logic out of a single app and into a reusable library. That matters because relay handling, event parsing, encryption, and storage rules become easier to share across clients instead of being reimplemented per platform.

The concrete result already showed up in Amethyst's desktop work. The grant-backed refactor moved shared code into Kotlin Multiplatform modules such as `commonMain`, `jvmAndroid`, and `jvmMain`, making desktop support a library and module problem instead of a full rewrite.

## Architecture

The library uses a modular source set structure:
- `commonMain`: Shared code for all platforms
- `jvmAndroid`: Code shared between JVM and Android
- `androidMain`: Android-specific implementations
- `jvmMain`: Desktop JVM implementations
- `iosMain`: iOS-specific implementations

## Current Status

In December 2025, OpenSats announced funding for Quartz in its fourteenth wave of Nostr grants. The repo exists as a standalone library, but much of the visible progress so far has landed through Amethyst PRs that convert app modules into multiplatform code and track feature parity across targets.

---

**Primary sources:**
- [Quartz Repository](https://github.com/vitorpamplona/quartz)
- [Quartz on Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Amethyst Repository](https://github.com/vitorpamplona/amethyst)
- [OpenSats Fourteenth Wave of Nostr Grants](https://opensats.org/blog/fourteenth-wave-of-nostr-grants)

**Mentioned in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: News](/en/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Amethyst Notable Changes](/en/newsletters/2025-12-31-newsletter/#amethyst-android)

**See also:**
- [Blossom Protocol](/en/topics/blossom/)
