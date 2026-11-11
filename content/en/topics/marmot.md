---
title: "Marmot Protocol"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot is a protocol for end-to-end encrypted group messaging on Nostr. It pairs Nostr's identity and relay network with MLS, which manages group keys and gives groups forward secrecy plus post-compromise security.

## How it works

Nostr supplies identity and relay-based event distribution, and Marmot layers MLS on top for group membership changes and message encryption. [NIP-17](/en/topics/nip-17/) focuses on one-to-one messaging, while Marmot is built for groups whose membership and keys change over time.

## What MLS adds

MLS gives Marmot properties that Nostr's direct-message schemes do not provide on their own. Group state evolves through authenticated membership changes with defined removal semantics, and later key updates let a group recover after a compromise.

Nostr handles identity and transport in an open network. MLS handles authenticated group key agreement. Marmot specifies how the two fit together.

## Implementation status

The protocol remains experimental, but it now has multiple implementations and active application use. [MDK](https://github.com/marmot-protocol/mdk) is the main Rust reference stack and [marmot-ts](https://github.com/marmot-protocol/marmot-ts) brings the model to TypeScript. Applications such as [White Noise](https://github.com/marmot-protocol/whitenoise), [Amethyst](https://github.com/vitorpamplona/amethyst), Pika, and Vector have been using Marmot-compatible components.

Recent work has focused on hardening and interop. Audit-driven fixes landed in early 2026, and MIP-03 introduced deterministic commit resolution so clients can converge when concurrent group state changes race across relays.

[MDK 0.9.9](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.9) preserves manual chat-pin order and adds terminal group disbanding. That release also exposes richer reply and ambient group context to agent integrations.

[MDK 0.11.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.11.0) adds qualified account-history recovery with durable notices for unproven gaps. It also introduces a database-backed delivery queue and carries encrypted group polls along with an Android native-library update. Applications need the matching generated bindings and native libraries, and account databases cannot be downgraded after the schema migration.

In April 2026, Amethyst brought its embedded MDK into line with the MIP-01 and MIP-05 wire formats. [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) added VarInt encoding of TLS-style length prefixes and round-trip validation against MDK test vectors. [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) added MIP-00 KeyPackage Relay List support, and [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) closed remaining admin-gate and media-handling gaps flagged by cross-client testing against White Noise. [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466) corrected MLS commit framing so encrypted welcome bytes match mdk-core output, and [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471) fixed an outer-layer decryption bug that caused state divergence between co-admins. Follow-up [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) adds validation of MLS commit cryptography, and [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) ships `amy`, a CLI interface for Marmot and MLS group operations driven from Amethyst's implementation.

MDK landed [PR #261](https://github.com/marmot-protocol/mdk/pull/261) to compute a group's `RequiredCapabilities` as the LCD of invitee capabilities (unblocking mixed-version invites between Amethyst and White Noise), [PR #262](https://github.com/marmot-protocol/mdk/pull/262) to parse invitee key packages before persisting the creator's signer, [PR #264](https://github.com/marmot-protocol/mdk/pull/264) to converge the SelfUpdate wire format across implementations, and [PR #265](https://github.com/marmot-protocol/mdk/pull/265) to expose a `group_required_proposals` accessor.

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) is in the middle of a multi-phase refactor from global singletons to per-account `AccountSession` views: [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) established the `AccountSession` and `AccountManager` scaffolding, and follow-on phases have migrated relay handles, drafts and settings, message ops, group read and write, membership, push notifications, key-package reads, group creation, and, as of [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770), session-scoped event dispatch. [marmot-ts PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68) migrates the TypeScript client to addressable kind `30443` key packages.

[White Noise Android's September 30 release](https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.30) brings encrypted group polls into its Android interface and shows notices when history recovery remains incomplete. Account-specific disappearing-message defaults apply to new conversations. [Later MDK source work](https://github.com/marmot-protocol/mdk/pull/2105) adds tagged custom-emoji sends and media reactions, separately from the tagged runtime release.

## Draft linked-device and account-sync work

The Marmot repository has merged a series of draft specification sections for using one account from several devices, and that draft text alone does not show application support. MDK has since merged a [default-off development device-groups capability](https://github.com/marmot-protocol/mdk/pull/2922) that lets daemon-backed `wn` commands run device-group pairing through the existing pairing flow, provided matching persistent development binaries are used. Ordinary releases keep it off, and the change claims neither mobile or binding activation nor physical-device testing.

MDK source also includes [experimental linked-device Welcome resend and history-only backup restore for current memberships](https://github.com/marmot-protocol/mdk/pull/2905). A newly merged [MDK repair](https://github.com/marmot-protocol/mdk/pull/2936) now matches the [Marmot heartbeat rule](https://github.com/marmot-protocol/marmot/pull/497). Repair falls due once the current target's heartbeat shows activity at least 10 minutes after the latest accepted publication, and then the exact retained Welcome is resent without a new Add, KeyPackage or history. The resend stays default-off, and an unknown publication time blocks it. Heartbeat cadence or the target's clock lag can delay it by an hour or more, and a bounded keyset scan may spend one maintenance turn wrapping before repair is checked again, so completion has no overall upper bound. It is not an ordinary app feature.

[The device roster draft](https://github.com/marmot-protocol/marmot/pull/452) adds a roster component and a per-account device group. The device group lists the roster component, under the experimental identifier `0x800e`, in its RequiredCapabilities. The separate experimental identifier `0x800f` names the device-tag component. A new device [pairs with an existing one by comparing seven emoji](https://github.com/marmot-protocol/marmot/pull/454) and then [joins the device group](https://github.com/marmot-protocol/marmot/pull/456). [Private KeyPackages](https://github.com/marmot-protocol/marmot/pull/459) let a linked device add its siblings to existing chats, and each added sibling receives a [sibling Welcome](https://github.com/marmot-protocol/marmot/pull/471). [Small-state sync](https://github.com/marmot-protocol/marmot/pull/466) shares compact account state between the devices.

Message history uses separate drafts. [History keys and history deliveries](https://github.com/marmot-protocol/marmot/pull/467) define encrypted history for an account's devices. Inline delivery remains available for history bundles, and [the history bundle draft](https://github.com/marmot-protocol/marmot/pull/483) permits Blossom as an optional alternative transport. [Backup writing](https://github.com/marmot-protocol/marmot/pull/487) seals backups to a [recovery key](https://github.com/marmot-protocol/marmot/pull/476). Encryption protects bundle and backup contents, but any Blossom server that carries them can still observe uploads and fetches.

[Removing a device](https://github.com/marmot-protocol/marmot/pull/472) and [cleanup after a device leaves the roster](https://github.com/marmot-protocol/marmot/pull/486) define how the remaining devices retire it and its keys. Removal cannot recall messages or history the device already received.

[PR #480](https://github.com/marmot-protocol/marmot/pull/480) narrows compromise handling to the warning raised by a device's own-slot check. It removes the rejected-KeyPackage and anomaly event kind from earlier drafts and leaves compromise of the account signing key out of scope. The change also breaks the experimental roster encoding, so device groups built on earlier drafts must be recreated and cannot be upgraded in place.

---

**Primary sources:**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)
- [MLS Protocol](https://messaginglayersecurity.rocks/)
- [Marmot Development Kit (MDK)](https://github.com/marmot-protocol/mdk)
- [MDK 0.9.9](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.9) - Chat-pin ordering and terminal group disbanding, with agent context additions
- [MDK 0.11.0 release notes](https://github.com/marmot-protocol/mdk/blob/v0.11.0/docs/release/0.11.0.md)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)
- [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)
- [White Noise client](https://github.com/marmot-protocol/whitenoise)
- [Amethyst PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) - MIP-01/MIP-05 wire format alignment
- [Amethyst PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) - MIP-00 KeyPackage Relay List
- [Amethyst PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) - Amy CLI
- [Marmot PR #452](https://github.com/marmot-protocol/marmot/pull/452) - Device roster component and device group (draft)
- [Marmot PR #454](https://github.com/marmot-protocol/marmot/pull/454) - Device pairing (draft)
- [Marmot PR #456](https://github.com/marmot-protocol/marmot/pull/456) - Linking a device into the device group (draft)
- [Marmot PR #459](https://github.com/marmot-protocol/marmot/pull/459) - Slot announcements with the own-slot check; private KeyPackages (draft)
- [Marmot PR #466](https://github.com/marmot-protocol/marmot/pull/466) - Small-state sync between an account's devices (draft)
- [Marmot PR #467](https://github.com/marmot-protocol/marmot/pull/467) - History keys and history deliveries (draft)
- [Marmot PR #480](https://github.com/marmot-protocol/marmot/pull/480) - Compromise handling narrowed to the own-slot warning (draft)
- [Marmot PR #483](https://github.com/marmot-protocol/marmot/pull/483) - History bundles with optional Blossom delivery (draft)
- [Marmot PR #487](https://github.com/marmot-protocol/marmot/pull/487) - Writing backups (draft)

- [Marmot invitation-generation and Welcome repair specification](https://github.com/marmot-protocol/marmot/pull/497)
- [MDK heartbeat-based Welcome repair](https://github.com/marmot-protocol/mdk/pull/2936)

**Mentioned in:**
- [Newsletter #48: Marmot projects at bitcoin++ Seoul](/en/newsletters/2026-11-11-newsletter/#marmot-projects-at-bitcoin-seoul)
- [Newsletter #47: MDK heartbeat-based Welcome repair](/en/newsletters/2026-11-04-newsletter/#marmot-protocol-mdk)
- [Newsletter #46: Marmot adopts multiple devices per account](/en/newsletters/2026-10-28-newsletter/#marmot-adopts-multiple-devices-per-account)
- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#amethyst)
- [Newsletter #44](/en/newsletters/2026-10-14-newsletter/#mdk)
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #4](/en/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Amethyst MIP compliance](/en/newsletters/2026-04-22-newsletter/#amethyst-ships-marmot-mip-compliance-nip-72-communities-and-live-stream-zap-goals)
- [Newsletter #19: MDK interop work](/en/newsletters/2026-04-22-newsletter/#mdk-adds-mixed-version-invite-support-and-selfupdate-wire-format-convergence)
- [Newsletter #19: whitenoise-rs session refactor](/en/newsletters/2026-04-22-newsletter/#whitenoise-rs-refactors-to-session-scoped-account-views)
- [Newsletter #23: White Noise](/en/newsletters/2026-05-21-newsletter/#white-noise-markdown-deep-links-and-audio-metadata)
- [Newsletter #27: ZapBook builds 4 through 27 add Marmot key publication](/en/newsletters/2026-06-17-newsletter/#zapbook-builds-4-through-27-ship-multi-account-marmot-key-publication-and-circle-re-invitations)
- [Newsletter #31: Vector v0.4.0 moves Group Chats from Marmot to Concord, and Amethyst ships its own Concord client days later](/en/newsletters/2026-07-15-newsletter/#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later)
- [Newsletter #31: Bitcoin-Safe reaches Flathub, spotlighting its Nostr Sync & Chat plugin](/en/newsletters/2026-07-15-newsletter/#bitcoin-safe-reaches-flathub-spotlighting-its-nostr-sync--chat-plugin)
- [Newsletter #33: Tagged releases](/en/newsletters/2026-07-29-newsletter/#tagged-releases)
- [Newsletter #37: Heterodyne specifies portable personas and encrypted social communication](/en/newsletters/2026-08-26-newsletter/#heterodyne-specifies-portable-personas-and-encrypted-social-communication)
- [Newsletter #38: MDK v0.9.15](/en/newsletters/2026-09-02-newsletter/#mdk-v0915-newest-keypackages-membership-activity-and-durable-sends)
- [Newsletter #40: Marmot Protocol and MDK 0.10.0](/en/newsletters/2026-09-16-newsletter/#marmot-protocol-and-mdk-reach-v0100)
- [Newsletter #41: MDK 0.10.4 durable local sends](/en/newsletters/2026-09-23-newsletter/#marmot-protocol-0104-makes-local-sends-durable)
- [Newsletter #42: MDK 0.11.0 recovery](/en/newsletters/2026-09-30-newsletter/#marmot-mdk-0110-makes-account-history-gaps-visible)
- [Newsletter #42: White Noise Android](/en/newsletters/2026-09-30-newsletter/#white-noise-android-adds-group-polls-and-account-specific-disappearing-message-defaults)
- [Newsletter #42: MDK source work](/en/newsletters/2026-09-30-newsletter/#marmot-mdk-extends-polls-custom-emoji-and-account-metadata)
- [Newsletter #42: Moyu workspace client](/en/newsletters/2026-09-30-newsletter/#moyu-opens-a-marmot-workspace-client)

**See also:**
- [MLS (Message Layer Security)](/en/topics/mls/)
- [MIP-05: Privacy-Preserving Push Notifications](/en/topics/mip-05/)
- [NIP-17: Private Direct Messages](/en/topics/nip-17/)
- [NIP-59: Gift Wrap](/en/topics/nip-59/)
- [Concord Protocol](/en/topics/concord-protocol/)
