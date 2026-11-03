---
title: "NIP-5D: Nostr Web Applets"
date: 2026-04-08
description: "Open proposal for a postMessage protocol between sandboxed web applets and a Nostr host shell."
---

NIP-5D is an open proposal for a `postMessage` protocol through which sandboxed web applications ("napplets") running in iframes could communicate with a hosting application ("shell"). The draft would extend [NIP-5A](/en/topics/nip-5a/) (Static Websites) with a runtime communication layer that gives web apps access to Nostr functionality without exposing the user's private key.

## How It Works

Under the proposal, a shell application would load a napplet in a sandboxed iframe. The napplet would communicate with the shell over a private `MessagePort` using a structured message protocol. The shell would provide signing, relay access, and user context through this channel while keeping the user's private key outside the iframe.

## Identity and transport

The [November 1 revision of the open proposal](https://github.com/nostr-protocol/nips/commit/c041f84667c1781c3c1d5bfbd970943131b38cc9) binds napplet identity to a private port tied to one document. Before any untrusted napplet script runs, the shell's bootstrap creates a `MessageChannel`. The first validated hello then associates the verified artifact identity with that bound port. The iframe's `Window` survives navigation, so it serves only for this handoff and never identifies the napplet afterward.

On a second hello, a message arriving through the window, a new load, or a port error, the shell must close the port explicitly, revoke the napplet's grants and session, and remove the frame. The same teardown applies on every navigation, and the shell never rebinds an existing frame to a new session.

The revision makes bootstrap privacy a conformance requirement because the browser does not guarantee it. A browser permits a reachable port to be transferred across origins, and a port can outlive the document that held it, so the bootstrap must keep the retained port unreachable from napplet code. Data already released to a napplet can still leave through a navigation URL and cannot be recalled, and the draft does not claim that a Content Security Policy blocks every exfiltration path. The existing manifest, blob hash, and source immutability mechanics are unchanged.

## Use Cases

- **Interactive Nostr apps**: Build apps that read and write Nostr events without requiring users to paste their nsec
- **App marketplace**: Distribute interactive web applications through Nostr events
- **Sandboxed extensions**: Add functionality to Nostr clients through third-party napplets

## Implementations

[Myco v0.7.0](https://github.com/Origami74/myco/releases/tag/v0.7.0) implements a NIP-5D napplet runtime inside its Android FIPS mesh application. Napplets run in sandboxed frames and request user-approved identity, relay, outbox, mesh, picture, and file capabilities through the host. NIP-5D remains an open proposal, so Myco's implementation is current experimental evidence, not a final interoperability guarantee.

---

**Primary sources:**
- [NIP-5D PR #2303](https://github.com/nostr-protocol/nips/pull/2303) - Nostr Web Applets proposal
- [NIP-5D November 1 revision](https://github.com/nostr-protocol/nips/commit/c041f84667c1781c3c1d5bfbd970943131b38cc9) - Napplet identity bound to a private document port
- [Myco v0.7.0](https://github.com/Origami74/myco/releases/tag/v0.7.0) - Sandboxed napplet runtime and permission model

**Mentioned in:**
- [Newsletter #47: Napplet identity moves to private document ports](/en/newsletters/2026-11-04-newsletter/#napplet-identity-moves-from-reusable-windows-to-private-document-ports)
- [Newsletter #46 (2026-10-28): amethyst](/en/newsletters/2026-10-28-newsletter/#amethyst)
- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#kehto---web-runtime)
- [Newsletter #44](/en/newsletters/2026-10-14-newsletter/#soyli)
- [Newsletter #40: Myco 0.7.0](/en/newsletters/2026-09-16-newsletter/#myco-070-runs-napplets-and-file-sharing-over-a-multi-path-fips-mesh)
- [Newsletter #37: NAPs](/en/newsletters/2026-08-26-newsletter/#naps)
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/#nip-updates)

**See also:**
- [NIP-5A (Static Websites)](/en/topics/nip-5a/)
- [NIP-5C (Scrolls)](/en/topics/nip-5c/)
