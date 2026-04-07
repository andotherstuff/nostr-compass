---
title: "NIP-5D: Nostr Web Applets"
date: 2026-04-08
description: "Defines a postMessage protocol for sandboxed web applications running in iframes to communicate with a Nostr hosting application."
---

NIP-5D defines a `postMessage` protocol for sandboxed web applications ("napplets") running in iframes to communicate with a hosting application ("shell"). It extends [NIP-5A](/en/topics/nip-5a/) (Static Websites) with a runtime communication layer that gives web apps access to Nostr functionality without exposing the user's private key.

## How It Works

A shell application loads a napplet in a sandboxed iframe. The napplet communicates with the shell through the browser's `postMessage` API using a structured message protocol. The shell provides the napplet with Nostr signing, relay access, and user context through this message channel. The iframe sandbox prevents the napplet from accessing the user's private key directly, so the shell acts as a gatekeeper for all Nostr operations.

## Use Cases

- **Interactive Nostr apps**: Build apps that read and write Nostr events without requiring users to paste their nsec
- **App marketplace**: Distribute interactive web applications through Nostr events
- **Sandboxed extensions**: Add functionality to Nostr clients through third-party napplets

---

**Primary sources:**
- [NIP-5D PR #2303](https://github.com/nostr-protocol/nips/pull/2303) - Nostr Web Applets proposal

**Mentioned in:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/#nip-updates)

**See also:**
- [NIP-5A (Static Websites)](/en/topics/nip-5a/)
- [NIP-5C (Scrolls)](/en/topics/nip-5c/)
