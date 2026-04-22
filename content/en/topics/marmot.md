---
title: "Marmot Protocol"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot is a protocol for end-to-end encrypted group messaging on Nostr. It combines Nostr's identity and relay network with MLS for group key management, forward secrecy, and post-compromise security.

## How It Works

Marmot uses Nostr for identity, relay transport, and event distribution, then layers MLS on top for group membership changes and message encryption. Unlike [NIP-17](/en/topics/nip-17/), which focuses on one-to-one messaging, Marmot is built for groups where members join, leave, or rotate keys over time.

## Why It Matters

MLS gives Marmot properties that Nostr's direct-message schemes do not provide on their own: group state evolution, member removal semantics, and recovery after compromise through later key updates.

That division of labor is the useful insight. Nostr solves identity and transport in an open network. MLS solves authenticated group key agreement. Marmot is the glue layer between them.

## Implementation Status

The protocol remains experimental, but it now has multiple implementations and active application use. [MDK](https://github.com/marmot-protocol/mdk) is the main Rust reference stack, [marmot-ts](https://github.com/marmot-protocol/marmot-ts) brings the model to TypeScript, and applications such as [White Noise](https://github.com/marmot-protocol/whitenoise), [Amethyst](https://github.com/vitorpamplona/amethyst), Pika, and Vector have been using Marmot-compatible components.

Recent work has focused on hardening and interop. Audit-driven fixes landed in early 2026, and MIP-03 introduced deterministic commit resolution so clients can converge when concurrent group state changes race across relays.

In April 2026, Amethyst brought its embedded MDK into line with the MIP-01 and MIP-05 wire formats: [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) added VarInt encoding of TLS-style length prefixes and round-trip validation against MDK test vectors, [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) added MIP-00 KeyPackage Relay List support, and [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) closed remaining admin-gate and media-handling gaps flagged by cross-client testing against White Noise. [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466) corrected MLS commit framing so encrypted welcome bytes match mdk-core output, and [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471) fixed an outer-layer decryption bug that caused state divergence between co-admins. Follow-up [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) adds comprehensive MLS commit cryptography validation, and [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) ships `amy`, a CLI interface for Marmot and MLS group operations driven from Amethyst's implementation.

MDK landed [PR #261](https://github.com/marmot-protocol/mdk/pull/261) to compute a group's `RequiredCapabilities` as the LCD of invitee capabilities (unblocking mixed-version invites between Amethyst and White Noise), [PR #262](https://github.com/marmot-protocol/mdk/pull/262) to parse invitee key packages before persisting the creator's signer, [PR #264](https://github.com/marmot-protocol/mdk/pull/264) to converge the SelfUpdate wire format across implementations, and [PR #265](https://github.com/marmot-protocol/mdk/pull/265) to expose a `group_required_proposals` accessor.

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) is in the middle of a multi-phase refactor from global singletons to per-account `AccountSession` views: [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) established the `AccountSession` and `AccountManager` scaffolding, and follow-on phases have migrated relay handles, drafts and settings, message ops, group read and write, membership, push notifications, key-package reads, group creation, and, as of [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770), session-scoped event dispatch. [marmot-ts PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68) migrates the TypeScript client to addressable kind `30443` key packages.

---

**Primary sources:**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)
- [MLS Protocol](https://messaginglayersecurity.rocks/)
- [Marmot Development Kit (MDK)](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)
- [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)
- [White Noise client](https://github.com/marmot-protocol/whitenoise)
- [Amethyst PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) - MIP-01/MIP-05 wire format alignment
- [Amethyst PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) - MIP-00 KeyPackage Relay List
- [Amethyst PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) - Amy CLI

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #4](/en/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Amethyst MIP compliance](/en/newsletters/2026-04-22-newsletter/#amethyst-ships-marmot-mip-compliance-nip-72-communities-and-live-stream-zap-goals)
- [Newsletter #19: MDK interop work](/en/newsletters/2026-04-22-newsletter/#mdk-adds-mixed-version-invite-support-and-selfupdate-wire-format-convergence)
- [Newsletter #19: whitenoise-rs session refactor](/en/newsletters/2026-04-22-newsletter/#whitenoise-rs-refactors-to-session-scoped-account-views)

**See also:**
- [MLS (Message Layer Security)](/en/topics/mls/)
- [MIP-05: Privacy-Preserving Push Notifications](/en/topics/mip-05/)
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
- [NIP-59: Gift Wrap](/en/topics/nip-59/)
