---
title: 'Nostr Compass #26'
date: 2026-06-10
publishDate: 2026-06-10
draft: false
type: newsletters
---

The Marmot Protocol organization opens three new repos for a v2 protocol draft and a native client lineage: a Rust workspace named `darkmatter`, a SwiftUI iOS app `darkmatter-ios`, and a Kotlin/Compose Android app `darkmatter-android`. The original Flutter Whitenoise is archived. Chama compresses seventeen releases into one week and crosses the standalone-app line at v3.0.0 before landing a full trade-room UI redraw and per-seller storefronts in v3.1.0, on top of holder-only Shamir shares, arbiter substitution, full-world community routing, and end-to-end trade notifications. Coracle launches a paid hosted-relay service backed by the open-source Caravel and zooid stack, with deep Flotilla integration planned. Angor flips to mainnet by default in v0.2.30 and lands a 3-user UAT funding test in v0.2.29. Amethyst lands 41 unreleased PRs continuing the NIP-32 / NIP-F4 / Tor work from last week. NIP-67 (EOSE completeness hint) and NIP-50 autocomplete merge, closing two long-standing correctness gaps in the core relay protocol. NIP-GART proposes a privacy-preserving wire format for emergency alerts, and NIP-46 picks up a logout method.

## Top stories

### Marmot v2 (Dark Matter): protocol redraft, native clients, archived Flutter app

Three new repos surfaced under the [marmot-protocol](https://github.com/marmot-protocol) GitHub organization this week, together forming the early-progress shape of a Marmot v2 protocol draft and a native-client lineage that replaces the Flutter app line. [`darkmatter`](https://github.com/marmot-protocol/darkmatter) (Rust, created May 13, thirty-four commits in the past seven days) holds the v2 protocol draft in `spec/`, an OpenMLS-backed CGKA engine in `crates/cgka-engine`, a conformance simulator with property tests, and a Tamarin formal model for convergence proofs. [`darkmatter-ios`](https://github.com/marmot-protocol/darkmatter-ios) (Swift, created May 25) is a SwiftUI client backed by a vendored `MarmotKit` UniFFI xcframework generated out of the Rust workspace. [`darkmatter-android`](https://github.com/marmot-protocol/darkmatter-android) (Kotlin/Jetpack Compose, created May 25) sits on the same Rust bindings. The original Flutter Whitenoise has been marked [`whitenoise-archive`](https://github.com/marmot-protocol/whitenoise-archive) ("ARCHIVED: This was the original White Noise Flutter app"); a new [`whitenoise`](https://github.com/marmot-protocol/whitenoise) Dart repo carries the active Flutter line in parallel.

Read this as early progress toward a more reliable Marmot, not a finished pivot. The darkmatter README labels itself "Candidate Marmot v2 protocol draft, CGKA engine, and conformance workspace" and says directly: "MDK remains the deployed Rust protocol implementation until this draft and engine are adopted." Inside the workspace, the cgka-engine crate is tagged `0.1.0`, "single internal consumer, not semver-stable." Every spec page carries "Status: draft for internal review". Three stars on the workspace repo and zero on the iOS and Android apps confirm the work is pre-announce. Direction, scope, and discipline are the signal here; production readiness is not the claim.

The protocol draft makes the v1-to-v2 deltas concrete. MIP-01's monolithic `marmot_group_data` MLS extension, which has carried group name, description, admin pubkeys, Nostr group routing id, relay list, group image data, and disappearing-message settings under one umbrella since the start of Marmot, gets [split into versioned app components](https://github.com/marmot-protocol/darkmatter/blob/master/spec/mip-coverage.md): `marmot.group.profile.v1` for name and description, `marmot.group.admin-policy.v1` for admin pubkeys, `marmot.transport.nostr.routing.v1` for the random `nostr_group_id` and the canonical relay list, `marmot.group.blossom.image.v1` for image hash, encryption key, nonce, and upload key, and `marmot.group.message-retention.v1` for disappearing-message seconds. Each component owns its exact bytes and its own versioning path, so a future feature can rev one component without forcing the rest of the group state to retread MLS extension consensus. MIP-00 credentials also gain a new foundation document `account-identity-proof-v1.md`, called out as "new in v2 and breaking". The identity proof now lives on its own surface, separate from KeyPackage construction.

The library deltas back the spec rework. `cgka-engine` is the new local group state machine: it wraps OpenMLS, owns the `Stable`, `PendingPublish`, `Merging`, and `Recovering` epoch states, translates intents into MLS commits, returns typed `IngestOutcome` and `GroupEvent` values for every inbound transport envelope, and explicitly ships no transport and no persistence. A `TransportPeeler` trait separates Nostr from the engine, and a `StorageProvider` trait separates SQLite (via `storage-sqlite`, SQLCipher-backed) from the engine. Today's MDK packs all of this together; splitting the layers lets one engine sit under a Nostr-relay transport now and the also-shipped [QUIC stream and broker transports](https://github.com/marmot-protocol/darkmatter/blob/master/docs/quic-broker-deployment.md) later, with no rewrite of the convergence model. Convergence itself is documented as `distributed-convergence.md` and proved in a Tamarin model that covers deterministic branch selection, policy-gated eligibility, retained-anchor replay, stale-branch rejection, delivery reordering, duplication, app-output invalidation, welcome/commit handoff, proposal consumption, and outbound gating while syncing. Rust property tests then check that the engine follows the same rules with real OpenMLS objects and the simulator harness. Formal-methods reliability work of this scope is absent from the current Marmot stack.

Both native clients drop Flutter for platform-native UI toolkits. [`darkmatter-ios`](https://github.com/marmot-protocol/darkmatter-ios) is pure SwiftUI with a Notification Service Extension that decrypts MIP-05 push wakes on device, vendors a generated `MarmotKit` Swift package built from the Rust workspace, and registers under the `dev.ipf.darkmatter` bundle ID and app group. [`darkmatter-android`](https://github.com/marmot-protocol/darkmatter-android) is Kotlin and Jetpack Compose, with a `just`-driven build that produces a signed `arm64-v8a` APK and reads telemetry endpoints from `local.properties`. The Android README states the architectural principle directly: "Dark Matter owns protocol data and stores it in SQLite. The Android app should render that data, manage Android platform behavior, and keep UI lifecycle state. The Android app should not become a second database for Dark Matter data." That mirrors the boundary discipline the cgka-engine README enforces in the Rust layer, applied to the UI layer.

Native clients matter for Marmot because the protocol's most-cited weakness has been mobile reliability under uneven delivery conditions: missed-deadline notification wakes, MLS commit races during network flaps, background-fetch limits that strand epoch advances. SwiftUI and Compose give the clients direct access to platform background-processing primitives that Flutter reaches through a plugin bridge, and the UniFFI binding path keeps protocol logic in one Rust workspace shipped as a static library on both platforms. The Flutter Whitenoise line continues in the unarchived [`whitenoise`](https://github.com/marmot-protocol/whitenoise) repo, so the announcement is additive: a new native-client lineage runs alongside the Flutter app while the v2 spec converges. Production cutover from MDK or the current Whitenoise app waits on the draft, engine, and clients reaching production-ready releases.

### Chama v2.0.0 through v3.1.0: standalone P2P escrow in one week

The Nostr-native P2P escrow client introduced in Newsletter #25 at v1.3.0 shipped seventeen tagged releases over the past seven days, ending at [v3.1.0](https://github.com/jesuspirate/chama/releases/tag/v3.1.0) on June 9 with a trade-room UI redraw and per-seller storefronts. The version trail tells the story: [v2.0.0](https://github.com/jesuspirate/chama/releases/tag/v2.0.0) is the BREAKING base, then [v2.0.1](https://github.com/jesuspirate/chama/releases/tag/v2.0.1), [v2.0.2](https://github.com/jesuspirate/chama/releases/tag/v2.0.2), and [v2.0.3](https://github.com/jesuspirate/chama/releases/tag/v2.0.3) close Fedi WebView funding-rail gaps; [v2.1.0](https://github.com/jesuspirate/chama/releases/tag/v2.1.0), [v2.2.0](https://github.com/jesuspirate/chama/releases/tag/v2.2.0), [v2.3.0](https://github.com/jesuspirate/chama/releases/tag/v2.3.0), and [v2.3.1](https://github.com/jesuspirate/chama/releases/tag/v2.3.1) harden the arbiter layer; [v2.4.0](https://github.com/jesuspirate/chama/releases/tag/v2.4.0), [v2.5.0](https://github.com/jesuspirate/chama/releases/tag/v2.5.0), and [v2.6.0](https://github.com/jesuspirate/chama/releases/tag/v2.6.0) add self-custody surfaces and world-wide community routing; [v2.7.0](https://github.com/jesuspirate/chama/releases/tag/v2.7.0), [v2.8.0](https://github.com/jesuspirate/chama/releases/tag/v2.8.0), [v2.9.0](https://github.com/jesuspirate/chama/releases/tag/v2.9.0), and [v2.10.0](https://github.com/jesuspirate/chama/releases/tag/v2.10.0) layer in plain-English key copy, group applications, dispute-deadline arbitration, and reputation. [v3.0.0](https://github.com/jesuspirate/chama/releases/tag/v3.0.0) ties the package together with end-to-end trade notifications, and [v3.1.0](https://github.com/jesuspirate/chama/releases/tag/v3.1.0) on June 9 redraws the trade screen around a Reserved → Locked → Settled progress spine, role-colored action cards, and a per-seller storefront listing class (curated swaps, loanbooks, and bills) that ships sats commerce without BTCPay or Zaprite.

The architectural pivot lives in v2.0.0. The escrow LOCK format changed so each share of a 2-of-3 Shamir split is encrypted only to its holder (sharePolicy `holder-only-v1`). The federation's bearer ecash no longer reconstructs from a single participant alone, closing a path where a malicious party with both their own share and a federation-held share could complete the trade without consent. Pre-2.0 clients fail loudly with "can't find your share"; the trade cannot complete on a stale client, and no funds are lost in the process. A v2.0 lock requires every party on v2.x to settle. v2.0.0 also added multi-unit storefronts and a sats-only Market view.

v2.1.0 introduced arbiter substitution: the arbiter share at Shamir index 2 is now encrypted to a deterministic priority order over the community arbiter pool, so an absent arbiter can be replaced without stranding the trade. v2.2.0 proved the substitution worked in the wild on a ₿121 trade and added healing-substitution backups. v2.3.0 closed the last arbiter front-running gap by checking listing-arbiter community membership at lock time, and v2.3.1 closed the sibling race where an auto-assigned arbiter slot was a preview until the lock seated them.

The self-custody surfaces arrived in v2.4.0 (BIP-39 recovery phrase for the Fedimint ecash wallet, stored encrypted on Nostr) and v2.5.0 (master nsec backup that owns the Nostr identity and the wallet seed). v2.6.0 reworked onboarding around a global community picker so users in countries without a local Chama get routed to the closest federation; earlier builds bounced the user with no fallback. v2.7.0 rewrote the recovery-key screen in plain English ("the only key to your account and the money in it; Chama never sees it and can't reset it; if you lose it, no one can get your account back"). v2.8.0 added group applications, dark/light theming, and added two new event kinds (38120 roster, 38121 application). v2.9.0 changed dispute resolution at deadline: contested trades that hit their expiry now resolve by arbiter ruling; previous behavior auto-refunded. The release is marked COORDINATED so all parties in a dispute must update. v2.10.0 added per-trade thumb-up/thumb-down ratings as a new event kind 38123.

v3.0.0 is the milestone where the app stops needing a coordinating community to operate. End-to-end trade notifications ping the user only on actionable state transitions: counterparty locked the sats, payout ready to claim, dispute requires the user's ruling as arbiter, or trade settled or expired. One toggle in the Me screen turns notifications on or off, and the permission prompt fires only when the toggle is enabled. The fire-once dedup keeps a state reload from triggering an alert storm. A wrong-chama guardrail bug was also closed in [PR #103](https://github.com/jesuspirate/chama/pull/103), where earlier versions could stamp a listing with one chama's label but another chama's federation. Windows and Linux desktop bundles ship with the release; the macOS dmg is held back until signing and notarization land.

Chama now joins Mostro and Shopstr as a Nostr-native marketplace, distinguished by serverless architecture, Fedimint-backed 2-of-3 Shamir escrow, holder-only share encryption, and the only one of the three that ships a self-contained desktop and mobile client without a coordinating community.

### Coracle Hosting: paid relay service plus open-source Caravel stack

On June 3 Hodlbod [announced Coracle Hosting](https://nos.lol/e/f8586160cd12df479c261397353c99e6f3e4d870b616382e1b4338bad3ab498a) at [hosting.coracle.social](https://hosting.coracle.social), a hosted community-relay service that accepts recurring lightning payments over NWC or card. The service is powered by [Caravel](https://gitea.coracle.social/coracle/caravel), Coracle's billing and provisioning frontend, and [zooid](https://gitea.coracle.social/coracle/zooid), a relay runtime that hosts many virtual relays on a single machine. Both are open source on Coracle's self-hosted gitea. Caravel ships with optional [livekit](https://livekit.io) and [Blossom](/en/topics/blossom/) integration that operators can toggle per relay. A free tier with member-count limits lets operators evaluate the service before committing payment details.

Hodlbod is candid about the business model: monetize open source by selling a hosted version of a stack that anyone else can also run. The competitive moat is the [Flotilla](https://flotilla.social) integration, which is the next planned step. Flotilla owns the user surface, so the hosted option served from inside Flotilla becomes the default path for any user who prefers managed infrastructure. Hodlbod offered to add other Caravel operators to Flotilla's alternative-hosting picker if they reach out, keeping the door open to a federated hosting market.

Caravel joins [relay.tools](https://relay.tools) as a public Nostr relay-provisioning platform with paid member tiers. relay.tools predates Caravel and ships as the dominant relay-creator service today, with its own directory of community relays and paid-member or moderator join flows. Caravel's distinguishing feature is the coordinated stack: the relay runtime (zooid), the billing and provisioning frontend (Caravel itself), and the client-side picker (Flotilla integration, still in flight) ship as one design. The other distinguishing feature is zooid's many-relays-per-process density, where customer relays share a single host process so the operator amortizes hosting costs across many small communities. This is the same density argument that made shared web hosting viable in the early 2000s, applied to Nostr's relay layer.

## Releases

### Angor v0.2.29 and v0.2.30: mainnet default and 3-user UAT funding test

[Angor v0.2.29](https://github.com/block-core/angor/releases/tag/v0.2.29) on June 4 and [v0.2.30](https://github.com/block-core/angor/releases/tag/v0.2.30) on June 8 are the two releases this week for the decentralized Bitcoin-and-Nostr funding protocol. v0.2.30's headline change is [PR #893](https://github.com/block-core/angor/pull/893), which flips the default network to mainnet. Angor still ships as an unstable alpha release, but the default-mainnet switch signals the protocol is past the testnet-only phase for the desktop and mobile clients. v0.2.30 also lands a single-tap mobile create-project flow with image upload and scroll reset ([PR #889](https://github.com/block-core/angor/pull/889)) and resolves a race condition where the lightning invoice spinner could hang ([PR #890](https://github.com/block-core/angor/pull/890)).

v0.2.29 added an end-to-end UAT test in [PR #881](https://github.com/block-core/angor/pull/881) covering 3-user send funds over 10 rounds with unconfirmed spends, the first multi-user funding-flow test in the Angor test suite. The release also added an implementation plan for an Angor CLI and MCP server ([PR #792](https://github.com/block-core/angor/pull/792)), with CLI improvements for MCP testing workflow in [PR #880](https://github.com/block-core/angor/pull/880). [PR #885](https://github.com/block-core/angor/pull/885) by DavidGershony fixed a Boltz lightning invoice that used the wrong network after a runtime network switch, a bug that would have surfaced in production after the v0.2.30 mainnet default. Settings now offer an optional recovery-wallet file purge during data wipe ([PR #883](https://github.com/block-core/angor/pull/883)).

### Sprout v0.3.15: ephemeral channel TTL refresh and ACP slash commands

[Sprout v0.3.15](https://github.com/block/sprout/releases/tag/v0.3.15), released June 10, is the eighth release in a run that started with v0.3.7 on June 2. Newsletter #25 covered the v0.3.1 through v0.3.6 run with the mesh-llm integration and channel sections work; v0.3.7 through v0.3.15 are downstream of that, focused on polish and a few user-facing additions. The most user-visible change is a TTL refresh for ephemeral channels in [PR #902](https://github.com/block/sprout/pull/902): when a user unarchives an ephemeral channel, Sprout extends the channel's time-to-live so the unarchive does not immediately re-archive under the original expiry timer. Mobile custom emojis arrive in [PR #906](https://github.com/block/sprout/pull/906) alongside a settings redesign, and reaction counts now animate on change ([PR #904](https://github.com/block/sprout/pull/904)).

[PR #905](https://github.com/block/sprout/pull/905) fixes a long-standing gap where multi-word display names broke and [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) `nostr:npub` mention extraction silently dropped. A directory-backed team UI for desktop ships in [PR #912](https://github.com/block/sprout/pull/912) with install, sync, and reveal commands. Slash commands now pass through to [ACP](https://agentclientprotocol.com) connectors in [PR #919](https://github.com/block/sprout/pull/919), letting Sprout forward `/help`-style commands directly to agent runtimes while the Sprout UI stays out of the path.

### Wisp v1.1.1: Spark wallet integration and nsec paste guard

[Wisp v1.1.1](https://github.com/barrydeen/wisp/releases/tag/v1.1.1), released June 5, lands a two-tier wallet Connect screen with [Spark](https://www.spark.money) sub-screen in [PR #548](https://github.com/barrydeen/wisp/pull/548) and dashboard parity with the iOS wallet UI in [PR #549](https://github.com/barrydeen/wisp/pull/549). The release includes a system-wide [nsec paste guard](https://github.com/barrydeen/wisp/pull/553) that detects an `nsec1`-prefixed paste anywhere in the app and blocks the field from accepting it, closing one of the most-cited footguns in Nostr UX. QR-scan login plus a watch-only mode for `npub` and `nprofile` ships in [PR #552](https://github.com/barrydeen/wisp/pull/552), letting a user browse a profile read-only. Zap messages now render as mini-posts in the engagement drawer ([PR #559](https://github.com/barrydeen/wisp/pull/559)) so zap notes carry their text alongside the sat amount. A web-of-trust filter on thread replies lands in [PR #583](https://github.com/barrydeen/wisp/pull/583), letting users hide reply spam from accounts outside their follow graph.

### Nostria v3.1.46 and nospeak 1.1.3: notification rework and ICE restart

[Nostria v3.1.46](https://github.com/nostria-app/nostria/releases/tag/v3.1.46) on June 7 ends a three-release run that reworked the notification counter to count only new notifications since the last view, eliminating a long-standing inflation where loading older notifications by scrolling bumped the badge count. [Nostria v3.1.45](https://github.com/nostria-app/nostria/releases/tag/v3.1.45) fixed a split-payment bug affecting lightning and QR-code payments and dropped a previously planned translucent UI as unviable on Android's compositor.

[nospeak v1.1.3](https://github.com/psic4t/nospeak/releases/tag/v1.1.3) on June 4 adds ICE restart on FAILED state for 1-on-1 voice calls. Standard WebRTC behavior drops a call when ICE candidates time out without an alternative path; the ICE-restart path renegotiates candidates so the call recovers from transient NAT or network changes. Android calls now keep the screen on during video calls.

## Unreleased changes

### Amethyst: 41 PRs continuing the NIP-32 / NIP-F4 / Tor track

Amethyst merged 41 PRs this week without cutting a release tag, on top of last week's 52 PRs and the [NIP-32](/en/topics/nip-32/) hashtag labeling and [NIP-F4](/en/topics/nip-f4/) podcast work covered in Newsletter #25. The active branch continues to accumulate features for the next tagged release, layering polish onto last week's headline additions: hashtag labeler discovery, podcast screen, music tracks and playlists, Tor self-heal watchdog, ephemeral signers for anonymous uploads, and onchain zaps with NIP-05 filtering. Amethyst's PR throughput remains the highest of any Nostr client, and the unreleased queue is the de-facto roadmap for what other Android Nostr clients will need to match.

### Damus: relay tracking from OK messages and v1.17 changelog

[Damus PR #3786](https://github.com/damus-io/damus/pull/3786), merged June 3, adds successful `OK` messages from a relay to the post-relay list. Earlier Damus builds populated the seen-relays list only when receiving a generic message from the relay, which meant a relay that acknowledged the post but delivered no events back was invisible to the user. The change matters for users who want to confirm their post landed on their preferred outbox relay. [PR #3796](https://github.com/damus-io/damus/pull/3796) fixes an `AttributeGraph` cycle on Profile View, and [PR #3725](https://github.com/damus-io/damus/pull/3725) lands the v1.17 changelog ahead of the next tagged release.

### Shopstr: NIP-34 dual-publishing

Shopstr's [shopstr repo on ngit](https://relay.ngit.dev/npub1u350hpq840naxzkkle4gmdtvzanfxmjd9m9tytn5355aua7jh2cqgfuw39/shopstr.git) was announced on Nostr this week as a [NIP-34](/en/topics/nip-34/) git repo, joining ngit's tracked repos. The shop client's GitHub repo remains the primary development surface; the NIP-34 announcement makes a parallel git-over-Nostr collaboration path available. This is the second major Nostr marketplace project to dual-publish to NIP-34 after [Mostro](https://relay.ngit.dev/), and continues the gradual migration of project metadata onto Nostr's git transport.

### Hermes-Marmot: AI agent gateway over MLS

[hermes-marmot](https://github.com/notmandatory/hermes-marmot), a plugin for the [Hermes Agent](https://github.com/NousResearch/hermes-agent), connects an AI agent's messaging surface to [Marmot](/en/topics/marmot/) (MLS-over-Nostr) groups using [mdk-python](https://github.com/marmot-protocol/mdk-python), the Python bindings to the Rust Marmot Development Kit. The plugin lets a user DM an AI agent from any Nostr client that speaks kind 445 MLS messages, including [Whitenoise](https://whitenoise.chat). Inbound DMs use [NIP-59](/en/topics/nip-59/) gift-wrap unwrapping via [nostr-sdk](https://github.com/rust-nostr/nostr) Python bindings, and inbound welcomes flow through `UnwrappedGift.from_gift_wrap` to `mdk.process_welcome` and `mdk.accept_welcome`. Access control runs through `MARMOT_ALLOWED_USERS` (a comma-separated npub allowlist) or `MARMOT_ALLOW_ALL_USERS=true` for open dev access.

The repo is new (last updated May 27) and small. Its significance is architectural: it is the first public bridge between an LLM agent runtime and an MLS-encrypted Nostr messaging channel, and the first production use of mdk-python beyond Whitenoise itself. The pattern points toward agent-to-agent communication where both endpoints hold MLS keys and the relay sees only ciphertext.

## NIP updates and protocol spec work

### NIP-67 EOSE completeness hint (PR #2317) merged

[PR #2317](https://github.com/nostr-protocol/nips/pull/2317) by mattn merged on June 6, adding [NIP-67](/en/topics/nip-67/) to the protocol. The NIP extends the `EOSE` relay message with an optional third element: `["EOSE", <subscription_id>, "finish"]` signals that every stored event matching the filter has been delivered, while a bare `["EOSE", <subscription_id>]` carries no completeness claim. A relay that omits the hint is telling the client there may be more; a relay that omits the NIP-67 advertisement in NIP-11 keeps today's behavior under the existing legacy heuristic. The change is backward compatible in both directions: legacy clients ignore the trailing array element, and legacy relays omit it.

The motivation in the merged spec is two-fold. First, silent data loss: a client asks for the last 500 notes against a relay with a 300-event internal cap, the relay returns 300 events, and the client (using the standard `received < limit` heuristic) concludes the result is complete. The 201st through Nth oldest matching notes stay on the relay unread, with the client blind to that fact. Second, mandatory wasted round trips: when a relay caps responses at 300 events, any subscription that exhausts the cap requires a second `REQ` with `until=<oldest_created_at>` purely to confirm completion, even when the filter happens to match exactly 300 events. Both failure modes are paid by every client on every cap-exhausted subscription. The `"finish"` hint is one optional string on one existing message and eliminates both costs.

### NIP-50 autocomplete extension (PR #2357) merged

[PR #2357](https://github.com/nostr-protocol/nips/pull/2357) by Alex Gleason merged on June 6, adding an `autocomplete:true/false` token to [NIP-50](/en/topics/nip-50/) search. The extension lets a client mark a query as a typeahead lookup so the relay uses prefix matching, with full-text search as the default for queries without the token. Ditto's relay implements it for follow packs, lists, and any event with a `title` tag, returning matches against the title prefix; the default search path runs full-text scoring. Without this token, autocomplete-style UIs had no way to communicate the prefix-search intent and relays had to guess from query shape. The token is a per-search hint, not a relay-wide capability, so a relay can implement it for one event class (titles) without claiming general autocomplete support.

### NIP-GART emergency alerts and location broadcasts (PR #2374)

[PR #2374](https://github.com/nostr-protocol/nips/pull/2374) by disinqa, opened June 9, defines a privacy-preserving wire format on Nostr for emergency alerts and location broadcasts addressed to a group of trusted recipients. The stated design goal is hiding sender identity, group membership, and payload from relay operators while keeping the events replay-safe and signature-verifiable end to end. NIP number is still TBD, proposal is early-draft. Use case is the standard emergency-alert pattern: a user under threat broadcasts a location ping that only a pre-shared group of trusted contacts can decrypt, with the relay blind to sender, recipient set, and payload. Wire-format details live in the PR and will likely evolve as maintainers review.

### NIP-46 logout method (PR #2373)

[PR #2373](https://github.com/nostr-protocol/nips/pull/2373) by hzrd149, opened June 8, adds a `logout` method to [NIP-46](/en/topics/nip-46/) so a client can tell a bunker explicitly that the session is ended. Until now, the only way to end a bunker session was to wait for the session timeout or stop using the connection, both of which leave the bunker holding session state for a client that is gone. The proposal is short (one new method) and is the kind of housekeeping change that makes long-lived bunker integrations cleaner.

### NIP-95 hybrid relay-P2P proposal circulated as long-form

A long-form [NIP-95 specification](https://github.com/nostr-protocol/nips) circulated as a `kind:30023` post from npub `91bea5cd9361504c409aaf459516988f68a2fcd482762fd969a7cdc71df4451c` on June 4 under the title *Protocolo Híbrido Relay-P2P via WebRTC*. The Portuguese-language document defines a hybrid peer-to-peer relay protocol where Nostr clients connect to each other directly via WebRTC for live messaging while continuing to use relays for stored-event retrieval and offline delivery. The author explicitly framed the spec as "LLM-ready," providing message definitions, logical flows, data schemas, and state rules at a level of detail that lets an AI model generate working client or server code. The proposal has not yet landed as a NIP PR; circulation via `kind:30023` is the customary precursor to a formal nostr-protocol/nips pull request.

### NIP-44 v3 picks up a second signer: Clave ports the spec

[Amber's v6.2.0 NIP-44 v3 rollout from last week](/en/newsletters/2026-06-03-newsletter/#nip-44-v3-amber-implementation-ahead-of-spec) shipped ahead of any merged NIPs PR, leaving v3 as an Amber-specific extension that other clients had to mirror to interop. That single-implementation framing changed this week. [Clave](https://github.com/DocNR/clave), the push-based iOS NIP-46 remote signer, landed an independent NIP-44 v3 port on June 3 and 4 across eight commits. Cryptographic primitives ship in three commits: [HKDF + ECDH keys layer](https://github.com/DocNR/clave/commit/99ca5a5aacb501d1666c489fcdea30187c7853fa), [the v3 padding algorithm](https://github.com/DocNR/clave/commit/8808cdca54d32b4ae57856bd4b07ed73a45e8e5c), and a [top-level public API plus encryption Context](https://github.com/DocNR/clave/commit/ae1f506a53cb2c8aa16523540dbe790876c1839e). On top of those, the NIP-46 surface follows in [RPC dispatch wiring inside LightSigner](https://github.com/DocNR/clave/commit/f37aa1afc8368862fc3ebac533408442349bfc38) and a [PendingRequest schema that carries the v3 context (kind plus scope)](https://github.com/DocNR/clave/commit/e51bcb49fc61cfa89b6030d61b203e046aeddb0a), so the signer can record which event kind and use case the v3 payload was approved for.

Clave diverges from Amber on the user-facing surface. A [permission grant schema with sensitivity tiers](https://github.com/DocNR/clave/commit/0a8b7de63c1f2994a80a66bf139ec519fab12877) lets users grant v3 encryption for a particular event kind and scope at a chosen sensitivity level. On first encounter, [v3-context-aware approval prompts with a one-time explainer card](https://github.com/DocNR/clave/commit/2cf563cb15b0406f5e8aaa0b4e34b887ff1896a1) introduce v3 to users. The work is in main and is [wired into the Xcode project](https://github.com/DocNR/clave/commit/4bd0c26d7cf308386ef15e5d96ee5673d6db2d4a) but is unreleased; the most recent tagged build is [v0.2.0-build79](https://github.com/DocNR/clave/releases/tag/v0.2.0-build79) from May 12.

Two independent implementations land NIP-44 v3 in production paths before the NIPs PR merges, which strengthens the case for the underlying wire format the protocol PR will formalize. Cross-implementation interop testing now becomes the path to spec convergence, with Amber's Android approval surface and Clave's iOS sensitivity-tier model as the two reference points. Other remote signers wiring v3 (nsec.app's noauth has been dormant since May 2025, and other bunkers have not announced v3 work) would tighten the consensus further.

### NIP-34 activity: Iris adopts the stack with a new hashtree transport

Iris published NIP-34 repo announcements for [`hashtree`](https://njump.me/nevent1qqs8kmy7a9dn5awurlp9q26lsaetl7dc4wauzdl8ww68dzmn09e074gpzfmhxue69uhhgetdwqhxjunfwvh8gmc850du0) on June 8 and [`iris-apps`](https://njump.me/nevent1qqsq4grx000f6p0r8hdv4lqhcgn7707vmktv2j528kn0ldps4y9g49qpzfmhxue69uhhgetdwqhxjunfwvh8gmcmq47as), [`iris-drive`](https://njump.me/nevent1qqsyj5r0tyqvpp9v7qnras90u6kzqtpqx6ktntwym66m8qyngvf59vqpzfmhxue69uhhgetdwqhxjunfwvh8gmcpts6pf), and [`iris-chat-rs`](https://njump.me/nevent1qqs0x98hpsv8vmrxvwm2rs9exxttrue5qv5p2n2sqjeylz2kgdmd7tgpzfmhxue69uhhgetdwqhxjunfwvh8gmca8783s) on June 9, advertising clone URLs under a new `htree://` scheme served from `wss://temp.iris.to`. The hashtree transport is a content-addressed alternative to GRASP-routed clones, and these four announcements are its first public uses. The repos carry empty descriptions and the architectural details are still emerging, but the choice to publish via NIP-34 announcement (over a custom Iris-internal manifest) signals Iris is committing to the broader NIP-34 git-over-Nostr stack.

## NIP deep dive: NIP-67 (EOSE Completeness Hint)

[NIP-67](/en/topics/nip-67/) closes one of the longest-standing correctness gaps in [NIP-01](/en/topics/nip-01/). The original spec defines `EOSE` as the boundary between stored events and live subscription events for a `REQ`, but it never specified whether the relay had finished delivering all stored matches or had stopped partway because of an internal cap. Every relay enforces a per-subscription cap (commonly 300 to 1000 events) independent of the client's `limit`, and clients have had no way to observe that cap.

The standard workaround was to compare the received count against the requested `limit`. If `received < limit`, treat the result as complete; otherwise paginate with `until=<oldest_created_at>`. Both branches are broken. The `received < limit` branch silently truncates: a client asking for 500 notes against a relay capped at 300 sees 300 events, concludes the result is complete because `300 < 500`, and never fetches the rest. Held events on the relay cannot signal "more available" through any existing message. Pagination as the second branch is wasteful: a filter that matches exactly the cap requires a second `REQ` to confirm completeness, returning zero events while consuming a full filter scan on the relay.

NIP-67's fix is one optional string on the `EOSE` message:

```
["EOSE", "<sub_id>", "finish"]   // explicit: all stored events delivered
["EOSE", "<sub_id>"]              // no completeness claim
```

A relay that advertises NIP-67 in [NIP-11](/en/topics/nip-11/) `supported_nips` and emits a bare `EOSE` is telling the client there is more. A relay that omits the advertisement keeps today's behavior, and the client falls back to the existing heuristic. Legacy clients ignore the trailing array element. Backward compatibility holds in both directions, with no new verbs or event kinds.

What makes NIP-67 worth examining is the scope it deliberately restricts. The spec defines no cursor or pagination token, so `until`-based pagination remains the mechanism. Relay caps stay where they are, and the NIP requires no exposure of them. NIP-67 preserves the meaning of `EOSE` as the stored-to-live boundary and only adds a yes-or-no signal at the boundary: "I have more for you" versus "that's everything." This minimal surface is why the PR merged after a relatively short review period for a NIP-01 extension, and why mattn explicitly notes in the PR that AI translation was used for the English text. The change is small enough that the translation uncertainty does not matter.

Example NIP-67-aware exchange between a client and a cap-enforcing relay. NIP-11 advertisement from the relay:

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1781136000,
  "kind": 11,
  "tags": [],
  "content": "{\"supported_nips\":[1,11,50,67]}",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

The wire-level exchange that follows:

```
→ ["REQ", "abc", {"kinds":[1],"limit":500}]
← [...300 EVENT messages...]
← ["EOSE", "abc"]               // no "finish": cap hit, more available
→ ["REQ", "def", {"kinds":[1],"limit":300,"until":1780900000}]
← [...178 EVENT messages...]
← ["EOSE", "def", "finish"]     // explicit complete
```

The 178-event response would previously have triggered a third `REQ` to confirm completion. With NIP-67 the client stops there.

NIP-67 is also notable as a NIP-01 amendment landing with rare consensus. Most NIP-01 changes attract long debate threads because the protocol's tiny surface is load-bearing for every implementation. NIP-67 merged after an extended review period (roughly seven weeks from open to merge), suggesting that when a NIP-01 change is small enough and the failure mode is concrete enough (silent data loss, mandatory wasted round trip), the protocol's maintainers are willing to extend the core message vocabulary.

## NIP deep dive: NIP-50 (Search)

[NIP-50](/en/topics/nip-50/) defines the `search` filter field in `REQ` messages, letting clients ask a relay to filter events by full-text match against a query string. The merged base spec is deliberately minimal: the `search` field is a string, each relay decides its own search semantics (which fields are indexed, how scoring works, whether stemming applies), and relays advertise NIP-50 support in their NIP-11 document. Clients control the search algorithm only through the query string itself.

This minimalism is both NIP-50's strength and its constraint. The strength is that any relay can implement search at any quality level: a basic substring scan satisfies the spec, and a relay running Elasticsearch or Meilisearch satisfies it equally. The constraint is that clients lack a way to express search intent. A profile-mention typeahead UI wants prefix matching against display names; a full-text content search wants tokenized full-text scoring across the note body. The same `search` field carries both, and the relay must guess from query shape.

[PR #2357](https://github.com/nostr-protocol/nips/pull/2357) adds the first NIP-50 extension token: `autocomplete:true` or `autocomplete:false` embedded in the search query signals which mode the client wants. Ditto's relay implements the token for follow packs, lists, and any event with a `title` tag, switching to prefix matching when `autocomplete:true` is present. The token lives inline in the query (separate filter fields stay untouched), so it travels with the search string and requires no wire-protocol bump:

```
search: "fiat autocomplete:true"
```

Token-shaped hints like this are how NIP-50 has always handled relay-specific dialects. Relays already supported tokens like `language:en` and `domain:example.com`. Each remains relay-specific, with each relay documenting its own dialect. NIP-50's PR #2357 elevates `autocomplete` from a relay-private token to a spec-blessed one, paving the way for typeahead-aware search across relays.

Example NIP-50 `REQ` with the autocomplete token, targeting a relay that indexes kind 0 profile titles:

```json
{
  "id": "b7c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f7081a2b3c4d5e6f70819a2b3c4d5",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1781136000,
  "kind": 1,
  "tags": [
    ["client", "example-mention-picker"]
  ],
  "content": "Sent search: kinds=[0], search=\"fiat autocomplete:true\", limit=10",
  "sig": "12d3e4f5061728394a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f7081a2b3c4d5e6f70819a2b3c4d5e6f7081a2b3c4d5e6f708192"
}
```

The actual wire-level REQ:

```
["REQ", "mention-picker", {"kinds":[0],"search":"fiat autocomplete:true","limit":10}]
```

A relay that does not recognize the token treats `autocomplete:true` as part of the literal search string and falls back to full-text matching, returning correct (if differently ranked) results. The graceful degradation makes the token safe to include unconditionally for clients that prefer prefix matching when available.

The next likely NIP-50 extension is per-kind ranking control: a hint that says "rank by `created_at` descending" versus the default relevance score. Several relays already accept `sort:newest` as a relay-private token, and the same elevation path that brought `autocomplete` into the spec applies. Search remains one of the few Nostr primitives where relays compete on result quality; reliability of delivery is the same across all conforming relays. Incremental tokens let clients exploit that quality competition without forcing relays to ship a heavyweight new spec.
