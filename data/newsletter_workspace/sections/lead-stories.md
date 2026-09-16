## Top Stories

### Marmot Protocol and MDK reach v0.10.0

[Marmot Protocol’s MDK v0.10.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.0) adds bounded chat-list and conversation windows, independent account-attention summaries, revision-safe drafts, and viewer reaction state for applications building MLS-based encrypted groups over Nostr. It also restores account-scoped user blocking and counts pending invitations without counting them again as unread messages.

The [v0.10.0 release series](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.0) fixes recovery when a device is removed and re-added, when traffic arrives before its Welcome, and when peel replay is interrupted. It reduces relay synchronization and subscription churn, queues media operations while transfer slots are busy, and pins forensic-audit uploads to validated destinations on every attempt.

The same [MDK source commit](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.0) ships Rust, C, Swift, Kotlin, command-line, and agent artifacts as one compatibility cohort. Account databases advance through migrations 70–75, so applications must update generated source and native libraries together, preserve complete Apple framework bundles, back up before migration, and avoid downgrading a migrated database.

### Myco 0.7.0 runs napplets and file sharing over a multi-path FIPS mesh

[Myco v0.7.0](https://github.com/Origami74/myco/releases/tag/v0.7.0) turns the Android mesh application into a host for napplets, single-file Nostr programs described by the open [NIP-5D proposal](/en/topics/nip-5d/). Each napplet runs in a sandbox without direct network or storage access and requests identity, relay, outbox, mesh, picture, or file capabilities through Myco. The install sheet shows those permissions before approval, users can change them later, and updates that request broader access return to the permission gate.

[Myco v0.7.0](https://github.com/Origami74/myco/releases/tag/v0.7.0) also sends arbitrary files to paired phones through the system share sheet or a Circle contact. The receiving phone approves the transfer before Myco writes it to `Downloads/Myco`, and the payload is encrypted to that phone’s key. Local-network discovery uses UDP when both phones share Wi-Fi and retains Bluetooth for offline paths; retries cover lost control messages, while a silence timer bounds stalled large transfers.

[Myco now keeps simultaneous FIPS links](https://github.com/Origami74/myco/releases/tag/v0.7.0) to a peer, probes standby paths, and moves traffic when the active Bluetooth, Wi-Fi Aware, or local-network link degrades. The work builds on FIPS’s experimental multi-path branch. Version 0.7.0 remains wire-compatible with 0.6.1 for existing app exchange, messaging, and pairing, but multi-path links form only between two updated phones. The embedded relay also moves to LMDB and migrates earlier event stores on first launch.

### Dart NDK changes relay, cache, and account behavior

[Dart NDK v0.10.0-dev.3](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.3) is a development release of the Dart client library, with breaking changes across relay handling, caching, authentication, and account streams. Client maintainers should expect code and behavioral migration work, especially where an application assumes that cached events, hidden events, or account updates follow the previous release line’s semantics.

The [v0.10.0 development series](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.3) also improves cache and Rust verifier performance and changes metadata, deletion-coordinate, event-visibility, signer-authentication, and NWC payment behavior. Packed Rust event verification reduces verification overhead, while the new `loadHiddenEvents` cache behavior is explicitly breaking.

Because this is [v0.10.0-dev.3](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.3), not a stable v0.10.0 release, application teams should pin versions and test migrations deliberately. Relay reconnection, cache hydration, signer authentication, wallet handling, and account-stream ordering are the highest-value paths to exercise before moving production clients.

### Keycast publishes its rebuilt signer release candidate

[Keycast v2.0.0-rc.1](https://github.com/marmot-protocol/keycast/releases/tag/v2.0.0-rc.1) is the first numbered release of the rebuilt self-hosted NIP-46 remote signer. The release candidate adds multiplexed NIP-46 support, shared and per-key relay routing, durable request handling, encrypted key storage, invitations, sessions, and team workspaces.

Signing policy and recovery receive equal weight in [v2.0.0-rc.1](https://github.com/marmot-protocol/keycast/releases/tag/v2.0.0-rc.1). Operators can configure signing policies, inspect audit history, create encrypted backups, recover deployments, and rotate the root key. The project also documents coordinated and verified release provenance across its API, signer, and web components.

The release remains a [release candidate](https://github.com/marmot-protocol/keycast/releases/tag/v2.0.0-rc.1), so operators should not infer final compatibility or production readiness from the version number alone. Testing should cover interrupted request recovery, relay-routing failures, policy enforcement, backup restoration, and key rotation before replacing an existing signer service.

writer_model: preferred=gemini-3.1-pro, actual=openai-codex/gpt-5.6-sol, receipt=data/newsletter_workspace/writer_receipt_2026-09-16.json

GATE: PENDING REVIEW
