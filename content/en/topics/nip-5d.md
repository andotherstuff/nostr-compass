---
title: "NIP-5D: Nostr Web Applets"
date: 2026-04-08
description: "Open proposal for a postMessage protocol between sandboxed web applets and a Nostr host shell."
---

NIP-5D is an open proposal for a `postMessage` protocol through which sandboxed web applications ("napplets") running in iframes could communicate with a hosting application ("shell"). The draft would extend [NIP-5A](/en/topics/nip-5a/) (Static Websites) with a runtime communication layer that gives web apps access to Nostr functionality without exposing the user's private key.

## How It Works

Under the proposal, a shell application would load a napplet in a sandboxed iframe. The napplet would communicate with the shell through the browser's `postMessage` API using a structured message protocol. The shell would provide signing, relay access, and user context through this channel while keeping the user's private key outside the iframe.

## Use Cases

- **Interactive Nostr apps**: Build apps that read and write Nostr events without requiring users to paste their nsec
- **App marketplace**: Distribute interactive web applications through Nostr events
- **Sandboxed extensions**: Add functionality to Nostr clients through third-party napplets

---

**Primary sources:**
- [NIP-5D PR #2303](https://github.com/nostr-protocol/nips/pull/2303) - Nostr Web Applets proposal

**Mentioned in:**
- [Newsletter #37: NAPs](/en/newsletters/2026-08-26-newsletter/#naps)
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/#nip-updates)

**See also:**
- [NIP-5A (Static Websites)](/en/topics/nip-5a/)
- [NIP-5C (Scrolls)](/en/topics/nip-5c/)
