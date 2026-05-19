---
title: 'Nostr Compass #23'
date: 2026-05-21
publishDate: 2026-05-21
draft: false
type: newsletters
---

Primal 3.5 ships a rebuilt Android shell, Amethyst adds onchain Bitcoin zaps, White Noise gains markdown rendering and deep links, Keycast passes a security audit, and AgentNoise lets you control local AI coding agents over Marmot-encrypted chat. Hostr launches a P2P rental accommodation platform on Nostr with four draft NIPs covering listings, reservations, and EVM-based escrow. Angor migrates encrypted messaging from NIP-04 to NIP-44, Dart NDK adds NIP-77 and a web signer, Alby js-sdk v8 ships native NWC multi-relay reconnect, and KeyChat patches a forward secrecy gap in Signal one-time prekey deletion. On the protocol side, Mostro's anti-abuse bond reaches Phase 2, Wisp ships private replies and gift-wrapped reactions, and a Namecoin NIP-05 implementation wave touches half a dozen clients in a single week.

## Top Stories

### Primal 3.5 for Android

Primal, the social client backed by its own caching relay infrastructure, shipped [3.5.9](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.9) this week with a rebuilt application shell. The redesign replaces the previous navigation structure with an updated layout and a new Explore screen, giving the main discovery surface its own dedicated home. The release adds audio playback for link previews, so audio files embedded in notes play inline without leaving the feed. NIP-05 verification badges now display inline on profiles, surfacing identity confirmation at a glance. Notification filtering received an overhaul, letting users narrow which event types reach their notification list. The editor gained better event-link handling, and the underlying database layer received stability fixes.

### White Noise: markdown, deep links, and audio metadata

White Noise, the Marmot-encrypted group messaging app built on Nostr and MLS ([RFC 9420](https://www.rfc-editor.org/rfc/rfc9420)), had one of its busiest weeks yet across the frontend and backend repositories.

On the frontend, [PR #665](https://github.com/marmot-protocol/whitenoise/pull/665) adds full markdown rendering for chat messages, so bold, italic, code blocks, and links now render natively in the message view. [PR #675](https://github.com/marmot-protocol/whitenoise/pull/675) enables the leave-group flow that was previously blocked for non-last admins, and [PR #661](https://github.com/marmot-protocol/whitenoise/pull/661) adds native deep link support for `whitenoise://` and `whitenoise-staging://` URIs covering users, chats, and settings, without requiring any HTTP redirect infrastructure.

On the backend in whitenoise-rs, [PR #835](https://github.com/marmot-protocol/whitenoise-rs/pull/835) makes key package rotation work properly by reusing the `d_tag` slot for kind:30443 publishes, enabling NIP-33 replaceable event semantics so successive key package rotations replace the previous event on relays, keeping only the current key package. [PR #833](https://github.com/marmot-protocol/whitenoise-rs/pull/833) extends `FileMetadata` with optional `duration_ms` and `waveform` fields for audio attachments, coordinated with MDK's [PR #300](https://github.com/marmot-protocol/mdk/pull/300) which adds the same fields to MIP-04 media tags. A new `whitenoise-markdown` crate ([PR #836](https://github.com/marmot-protocol/whitenoise-rs/pull/836)) replaces the previous nostr-sdk token parser with a dedicated markdown rendering library.

The Marmot protocol spec itself received a security fix in [PR #68](https://github.com/marmot-protocol/marmot/pull/68), which closes a security issue by explicitly specifying HKDF-SHA256 for image key derivations in MIP-01, removing ambiguity that could lead to implementation divergence. In MDK, [PR #307](https://github.com/marmot-protocol/mdk/pull/307) sanitizes welcome failure reasons and caps stored length, closing a separate security finding.

### Amethyst v1.10.0: Onchain Bitcoin Zaps

Amethyst shipped four releases this week, with [v1.10.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.10.0) as the headline. The release adds support for NIP-BC onchain Bitcoin zaps, enabling users to send, receive, and display zaps settled directly onchain via Bitcoin transactions. Earlier releases in the run fixed Blossom blob detection to reject non-compliant filenames ([v1.09.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.09.2)), patched ProGuard rules for desktop builds, and merged pull request [#2977](https://github.com/vitorpamplona/amethyst/pull/2977) to show onchain Bitcoin zappers as a dedicated ₿ row in the expanded reactions gallery. An in-progress on-chain transaction history screen with pagination landed in [PR #2974](https://github.com/vitorpamplona/amethyst/pull/2974).

### AgentNoise: control coding agents over White Noise

[AgentNoise](https://github.com/nvk/agentnoise) by nvk is a Rust-native desktop helper that lets you use a phone running White Noise as the control surface for local Codex and Claude coding agent sessions. The tool listens to one or more White Noise chats, authenticates senders through a first-pairing PIN flow, and launches local coding agents through the configured launcher. Sending `/claude <prompt>` from your phone opens a new White Noise work session named after the machine hostname and a short prompt summary, then streams progress updates and final output back to that chat. It is intentionally Rust-first and keeps Node out of the trusted bridge path. The project reached [v0.1.24](https://github.com/nvk/agentnoise/releases/tag/v0.1.24) this week, adding shorter phone-readable replies, job references by short unique prefix, and an opt-in local session watcher. AgentNoise drives the `wn` and `wnd` CLIs from `marmot-protocol/whitenoise-rs` as subprocesses, so it shares its Nostr transport with the White Noise client itself.

### Keycast security audit complete

[Keycast](https://github.com/marmot-protocol/keycast), the team-oriented NIP-46 remote signing server that stores Nostr private keys encrypted at rest in SQLite, completed a security audit in May 2026. The hardening pass addressed auth, permission, data integrity, and dependency issues, and the results are documented in [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md). Changes include: NIP-98 HTTP auth now requires exactly one `u` tag and one `method` tag, rejects stale timestamps, and validates `payload` hashes; the `ALLOWED_PUBKEYS` allowlist is parsed exactly and enforced server-side; empty policies now default-deny sign/encrypt/decrypt requests; foreign-key enforcement is enabled on SQLite connections; and nested app routes such as `/teams/:id` are protected server-side. A SQL migration normalizes old allowed-kinds permission JSON on startup. The project is still early-stage and the audit notes residual items before trusting it with real team keys.

### Scramble: Marmot client for desktop and Android

[Scramble](https://github.com/DavidGershony/Scramble) (formerly OpenChat) is a .NET/Avalonia desktop and Android client for the [Marmot Protocol](/en/topics/marmot/), implementing MIPs 00-04: KeyPackage publishing (kind:30443), group metadata with the NostrGroupData MLS extension, NIP-59 gift-wrapped welcome events (kind:444), ChaCha20-Poly1305 encrypted messages (kind:445), and Blossom encrypted media attachments. It is fully interoperable with White Noise and any other Marmot-compatible client.

The project shipped 13 releases this week, with multi-device support as the main feature. Each device generates a unique KeyPackage slot (a `d`-tag on kind:30443). On startup, Scramble fetches the user's own KeyPackages from relays, detects peer device slot IDs, and automatically adds them to existing MLS groups using the staged commit flow. Auto-add is restricted to groups where the current user is admin; non-admin groups are skipped with guidance to ask the group admin. A forward-secrecy disclosure banner informs newly-linked devices that old messages are unavailable. A slot ID reconciliation pass (`TryReconcileSlotId`) handles devices migrated from pre-multi-device versions by matching relay KeyPackage bytes against local key material to adopt the correct `d`-tag. External signer reconnect for Amber and NIP-46 users was also fixed: the `IsConnected` guard that blocked `ExternalSignerService`'s built-in auto-reconnect was removed at all nine call sites in `NostrService`.

### Hostr: P2P rental accommodation on Nostr

[Hostr](https://hostr.network) ([source](https://github.com/sudonym-btc/hostr)) is a peer-to-peer rental accommodation platform built entirely on Nostr. It covers the full Airbnb-style flow (searching and listing properties, negotiating reservations, and settling payments) using four draft NIPs the project is developing in parallel with the application.

The accommodation NIP extends [NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md) classified listings (kind:30402 active, kind:30403 draft) with accommodation-specific tags for type (`room`, `house`, `apartment`, `villa`, `hotel`, `hostel`, `resort`), check-in/check-out times, minimum stay, and H3 geospatial cell indexes for location-based search at configurable precision. The reservation NIP defines a full negotiation and lifecycle protocol: kind:32122 replaceable reservation events carry a `d` trade ID, a listing anchor `a` tag, and participant `p` tags with roles (`buyer`, `seller`, `escrow`); kind:1327 structured message rumors deliver private negotiate-stage counteroffers via NIP-59 gift wraps so the negotiation stays off public relays; kind:1326 append-only transition events create a public audit trail once a reservation commits. Buyer privacy is preserved through per-trade temporary Nostr keys bound to the buyer's real identity via encrypted `participant_proof` tags. The escrow NIP defines kind:30303 escrow service advertisements and kind:17388 user trust declarations; the reference implementation uses EVM smart contracts on Rootstock, with `contractBytecodeHash` allowing clients to verify the deployed contract matches a known audited implementation. The marketplace listing NIP defines generic tags shared across all NIP-99 marketplace profiles, including `instantBook`, `negotiable`, `quantity`, `securityDeposit`, `cancellationPolicy`, and `maxDisputePeriod`. This week the project prepared its app store submission and merged MCP client identity support for agent-facing automation.

Two new entries appeared on the Shakespeare MiniApps platform this week: [InkPress](https://inkpress.shakespeare.wtf), an AI magazine generator that publishes structured magazine-style content as Nostr events, and [PressStr](https://pressstr.shakespeare.wtf), a writing and publishing platform for the Soapbox stack.

## Shipping this week

### ngit v2.4.4

**ngit** shipped [v2.4.4](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.4), adding `ngit sync --trust-server` (`-t`) for cases where a git server is fast-forward ahead of Nostr state. When this situation is detected, sync reports the affected refs and requires the flag to sign and publish an updated state event; a `nostr.trust-server-domains` git config setting provides a semicolon-separated allowlist for servers that should be trusted automatically without the flag.

### Amber v6.1.0-pre3 adds PSBT signing

**Amber** released [v6.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre3) with improved layout for new app connections, crash fixes, and a select/deselect all option on the permissions screen. [PR #438](https://github.com/greenart7c3/Amber/pull/438) adds PSBT signing support through both the Intent-based and NIP-46 relay-based paths, allowing Amber to sign Partially Signed Bitcoin Transactions without exposing the nsec to the requesting app.

### Wisp v1.1.0 ships private replies and drops Amber support

**Wisp** released [v1.1.0](https://github.com/barrydeen/wisp/releases/tag/v1.1.0) with private replies via NIP-17 gift wrap ([PR #540](https://github.com/barrydeen/wisp/pull/540)), gift-wrapped reactions and DIP-03 zaps on private replies ([PR #543](https://github.com/barrydeen/wisp/pull/543)), auto-translate for notes ([PR #523](https://github.com/barrydeen/wisp/pull/523)), and a register-style fiat input on the zap dialog. [PR #541](https://github.com/barrydeen/wisp/pull/541) migrates private zaps from a homegrown DM-relay plaintext scheme to DIP-03 with proper DM-relay routing. The same release cycle removed NIP-55 remote signer support ([PR #531](https://github.com/barrydeen/wisp/pull/531)), dropping Amber and other external signer integrations, and removed the bundled local relay ([PR #533](https://github.com/barrydeen/wisp/pull/533)). Wisp is a Nostr social client for Android.

### Calendar by Formstr v1.5.4 fixes gift wrap for new participants

**Calendar by Formstr** shipped [v1.5.4](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.4) (the latest in a v1.5.2 → v1.5.4 sequence). [PR #160](https://github.com/formstr-hq/nostr-calendar/pull/160) fixes a bug where editing a private calendar event with new participants published the updated event with the new pubkeys in `p` tags but never created or delivered gift wrap invitations to those participants, breaking the invite flow for last-minute additions. [PR #156](https://github.com/formstr-hq/nostr-calendar/pull/156) adds error handling around private event decryption so clients no longer throw on undecryptable events, and [PR #138](https://github.com/formstr-hq/nostr-calendar/pull/138) corrects recurring event times that were drifting across timezones.

### Applesauce v6.1.0 adds NIP-34 git casts and NIP-51 lookup relays

**Applesauce** released [v6.1.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%406.1.0) across its packages with significant NIP-34 (git-over-Nostr) support: applesauce-common adds new `GitRepository`, `GitGraspList`, and `FavoriteGitRepos` casts plus matching factories, and exposes `User.favoriteGitRepos$`, `User.gitAuthors$`, and `User.graspServers$` reactive properties so applications can list a user's followed git repos, repo maintainers, and configured GRASP servers directly from the same User object. The same release adds support for NIP-51 kind 10086 lookup relay lists, a recent addition to the relay-list family used to discover where to find specific data. applesauce-core gains `replaceableAddress` on `EventCast` for NIP-01 replaceable address lookup, plus `pointer`, `kind`, and a `getReplaceableAddressForEvent` helper, and adds a `timeline$()` method on the base `User` cast. [PR #73](https://github.com/hzrd149/applesauce/pull/73) fixes pool manual methods silently dropping offline relays.

### Sprout v0.0.16 ships Sprig binary and huddle protocol v2

**Sprout** by Block, a self-hosted Nostr-relay-based team workspace where humans and AI agents share the same rooms and event log, shipped [v0.0.16](https://github.com/block/sprout/releases/tag/v0.0.16) of the desktop app alongside rolling builds of the new Sprig all-in-one binary ([PR #605](https://github.com/block/sprout/pull/605)), which bundles the ACP harness, agent, and developer MCP into a single busybox-style binary for easy deployment. The `--no-memory` flag added in [PR #611](https://github.com/block/sprout/pull/611) lets operators disable NIP-AE core memory injection for the ACP harness. On the realtime side, [PR #609](https://github.com/block/sprout/pull/609) extends the huddle voice protocol to a v2 frame header supporting up to 10 simultaneous peers.

### Nostrord v1.0.3 adds OS keychain and multi-account

**Nostrord** released [v1.0.3](https://github.com/nostrord/nostrord/releases/tag/v1.0.3) with local key storage hardened using OS keychain and passphrase fallback, multi-account support, and a tappable bunker QR code that opens the signer app on Android.

### Angor migrates to NIP-44 and ships security hardening

**Angor**, the Bitcoin crowdfunding app built on Nostr and Taproot, shipped three unstable releases this week ([v0.2.24](https://github.com/block-core/angor/releases/tag/v0.2.24), [v0.2.25](https://github.com/block-core/angor/releases/tag/v0.2.25), and [v0.2.26](https://github.com/block-core/angor/releases/tag/v0.2.26)) with a set of security hardening and Nostr integration changes. [PR #860](https://github.com/block-core/angor/pull/860) migrates Nostr encrypted messaging from NIP-04 to NIP-44, replacing the deprecated XOR-based scheme with ChaCha20-Poly1305 encryption. [PR #861](https://github.com/block-core/angor/pull/861) allows Blossom media uploads without a selected wallet by using an ephemeral Nostr auth key, unblocking uploads for users who have not yet connected a wallet. The security series addressed several hardened categories: [PR #854](https://github.com/block-core/angor/pull/854) adds type safety for AngorKey and mnemonic memory protection, [PR #856](https://github.com/block-core/angor/pull/856) enforces protocol-level validation for timelocks, fee rates, dust thresholds, and penalty rules, and [PR #851](https://github.com/block-core/angor/pull/851) applies non-breaking hardening across eight medium and low severity categories. [PR #859](https://github.com/block-core/angor/pull/859) fixes GrapheneOS compatibility by enabling AOT compilation and removing runtime code generation, and [PR #855](https://github.com/block-core/angor/pull/855) prevents wallet loss on Android swipe-kill by persisting wallet state before the OS terminates the process.

### Alby js-sdk v8.0 ships NWC multi-relay reconnect

**Alby js-sdk** released the v8.0 line ([v8.0.1](https://github.com/getAlby/js-sdk/releases/tag/v8.0.1) through [v8.0.3](https://github.com/getAlby/js-sdk/releases/tag/v8.0.3)) with NWC multi-relay subscription support. [PR #516](https://github.com/getAlby/js-sdk/pull/516) updates the nostr-tools dependency and enables native auto-reconnect across multiple relays, replacing the previous polling approach with relay-native reconnection logic. [PR #542](https://github.com/getAlby/js-sdk/pull/542) replaces all `console.debug` calls with an injectable logger interface so application developers can route SDK diagnostics through their own logging infrastructure. The release drops the WebSocket polyfill, requiring Node.js 22 or higher for server-side consumers. v8.0.2 added a fix for a utils crypto import bug that broke certain bundlers.

### KeyChat v1.41.1 fixes forward secrecy

**KeyChat**, a messaging app that combines the Signal protocol with Nostr relay transport, released [v1.41.1+6513](https://github.com/keychat-io/keychat-app/releases/tag/v1.41.1+6513). The headline fix enforces forward secrecy by deleting Signal one-time prekeys immediately after a successful decryption, closing a gap where a retained prekey could be used to decrypt past messages if the device was later compromised. The release also adds URL preview for messages consisting of a single link, centralizes media auto-download under a new `FileDownloadManager` with a 20 MB automatic threshold, and refactors NIP-11 relay info fetching to force refresh on cold start so paid relay fee configurations always load correctly.

## In Development

**Citrine** merged [PR #151](https://github.com/greenart7c3/Citrine/pull/151) implementing NIP-70 enforcement: the Android relay now blocks reposts that embed protected event content, as the spec requires. [PR #149](https://github.com/greenart7c3/Citrine/pull/149) adds display and copy actions for multiple connection addresses, localhost, local Wi-Fi, and Tor, from the relay settings screen. [PR #141](https://github.com/greenart7c3/Citrine/pull/141) adds NIP-42 AUTH challenge handling through external signer integration with Amber.

**Mostro** reached Phase 2 of its anti-abuse bond rollout. [PR #737](https://github.com/MostroP2P/mostro/pull/737) lands solver-directed dispute slash logic: admin handlers now consume the `BondResolution` payload from mostro-core, allowing an admin to slash either party's bond when resolving a dispute. Phase 1.5, merged in [PR #736](https://github.com/MostroP2P/mostro/pull/736), introduced a dedicated `PayBondInvoice` action and `WaitingTakerBond` status, separating the taker's anti-abuse bond payment from the buyer's trade payout. The mobile client added the full Phase 1.5 UX in [PR #592](https://github.com/MostroP2P/mobile/pull/592). Mostro is a peer-to-peer Bitcoin exchange protocol built on Nostr.

**Damus** merged [PR #3773](https://github.com/damus-io/damus/pull/3773) restoring the relay signal indicator, and [PR #3775](https://github.com/damus-io/damus/pull/3775) fixes relays that refused to reconnect after an initial connection failure.

**rust-nostr** merged [PR #1358](https://github.com/rust-nostr/nostr/pull/1358) adding event finalization traits and NIP-specific event builders, making it easier to construct correctly-typed events for specific protocol functions. [PR #1363](https://github.com/rust-nostr/nostr/pull/1363) backports a fix ensuring the NIP-46 signer subscribes to notifications before sending the connect response, closing a race condition where client messages arriving immediately after connect could be missed.

**dart-nostr** merged [PR #44](https://github.com/ethicnology/dart-nostr/pull/44) adding a Namecoin `.bit` relay resolver and TLSA pin records, enabling Flutter applications to resolve `wss://example.bit/` relay URLs through Namecoin DNS to their actual WebSocket addresses.

**Dart NDK** (the Dart/Flutter Nostr development kit, now at `relaystr/ndk`) merged [PR #464](https://github.com/relaystr/ndk/pull/464) implementing NIP-77, the offline event signing protocol. On the signer side, [PR #602](https://github.com/relaystr/ndk/pull/602) and [PR #601](https://github.com/relaystr/ndk/pull/601) add a web-specific event signer and a `PlatformEventVerifier` abstraction, letting Flutter web apps use the platform signer without a separate code path; [PR #604](https://github.com/relaystr/ndk/pull/604) introduces an event signer factory for runtime signer selection. [PR #608](https://github.com/relaystr/ndk/pull/608) adds `getDmRelays()` to fetch a user's NIP-17 DM relay list (kind:10050), and [PR #600](https://github.com/relaystr/ndk/pull/600) fixes NIP-46 signed field preservation so remote signers do not lose fields on round-trip.

**Pages by Form\*** ([repo](https://github.com/formstr-hq/nostr-docs)), Formstr's Nostr-native collaborative document app hosted at [pages.formstr.app](https://pages.formstr.app), merged four PRs this week tightening the encrypted-attachment and document-management flows. [PR #37](https://github.com/formstr-hq/nostr-docs/pull/37) fixes missing images in DOCX, HTML, and PDF exports by inlining encrypted attachments: it fetches `<encrypted-file>` blobs from Blossom servers, decrypts them with AES-GCM 256-bit using the stored key and nonce, validates the image MIME type, and converts them to base64 data URLs so exports preserve images that only exist on Blossom in encrypted form. [PR #39](https://github.com/formstr-hq/nostr-docs/pull/39) adds a local document search mechanism, [PR #38](https://github.com/formstr-hq/nostr-docs/pull/38) cleans up the rename flow, and [PR #40](https://github.com/formstr-hq/nostr-docs/pull/40) fixes shared backup handling.

**Zap Cooking** merged [PR #396](https://github.com/zapcooking/frontend/pull/396), the first phase of a feed overhaul that lays down feed-rendering primitives without any user-visible change yet. The PR introduces a NIP-92 `imeta` tag parser that reads the `url`, `m` (MIME), `dim` (dimensions), `blurhash`, `alt`, `x` (file hash), and `fallback` slots, plus a hand-ported canonical blurhash decoder (~200 LOC) that produces PNG data URLs via canvas with an SSR-safe null fallback. When `imeta` tags are absent the parser falls back to extracting raw image and video URLs from the event content using the same heuristics the current feed already uses.

**Nurunuru** (ぬるぬる, `tami1A84/null--nostr`), a Nostr client with native Android, iOS, and Web variants sharing a Rust FFI engine, merged its v1.5.0 Native → Web sync in [PR #176](https://github.com/tami1A84/null--nostr/pull/176). The sync brings several feature additions to the Web build that already shipped on Android v1.4.9 and iOS 1.0.4: the [NotificationModal](https://github.com/tami1A84/null--nostr/pull/176) now surfaces birthday notifications, mutual-follow zap detection, and custom-emoji reaction notifications; the reaction picker drops the Unicode default-reactions quick-row and centers the UX on custom emoji; the recommendation engine in `lib/recommendation.js` filters out users without icons or display names and prioritizes Following entries with Recommended loading in the background. Voice input is the one feature going the other direction: the Web build already uses ElevenLabs Scribe streaming, and v1.5.0 partial-syncs the Native side to the OS-standard `SpeechRecognizer` (Android) and `SFSpeechRecognizer` + `AVAudioEngine` (iOS) while the full Native Scribe integration is deferred to v1.6.

## Protocol and spec work

**PR [#2251](https://github.com/nostr-protocol/nips/pull/2251)** tightens the NIP-70 protected events spec: it now explicitly states that reposts embedding the full content of a protected event must be rejected by relays. NIP-70 defines the `-` tag that signals a note author does not consent to having their note republished. The original spec covered relay filtering behavior, but left the repost case ambiguous. This PR closes that gap. Citrine's [PR #151](https://github.com/greenart7c3/Citrine/pull/151) implements the enforcement on the relay side this same week.

**PR [#1653](https://github.com/nostr-protocol/nips/pull/1653)** proposes a Drafts NIP for saving and syncing private draft events. The proposal uses replaceable events with a `draft` status and NIP-44 encryption to the author's own key, letting clients save works in progress to relays without those events being visible to anyone else. The draft event carries the full intended-publication event as encrypted content, including its eventual kind and tags.

**Snapshots ([PR #2279](https://github.com/nostr-protocol/nips/pull/2279))** is an open proposal to define an immutable snapshot event for preserving one exact version of a replaceable Nostr event. The snapshot event carries the full content of the replaceable event at a given point in time, with an `a` tag linking it back to the replaceable event's address so all historical versions are queryable together. This makes it possible for observers to inspect historical state even after relays stop retaining old versions.

**Namecoin NIP-05 wave:** This week saw a coordinated push to add `.bit` NIP-05 resolution to Nostr clients. The NIP discussion feed captured open-source PRs against Aegis ([#14](https://github.com/ZharlieW/Aegis/pull/14), which adds sign-time verification at the signer), nostter ([#2128](https://github.com/SnowCait/nostter/pull/2128)), and dart-nostr ([#44](https://github.com/ethicnology/dart-nostr/pull/44)), alongside an upstream NIP draft ([PR #2349](https://github.com/nostr-protocol/nips/pull/2349)). The Aegis PR is notable for placing verification on the producer side: the signer checks the Namecoin chain before signing any kind:0 event that claims a `.bit` identity and warns the user on mismatch, catching the problem before the event reaches any relay.

## NIP Deep Dive: NIP-07 (window.nostr for Web Browsers)

[NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md) defines the `window.nostr` interface that browser extensions expose to web applications. It is the most widely deployed signer interface on the web, implemented by extensions including Alby, nos2x, Flamingo, and horse.

The interface has two required methods and several optional ones. `window.nostr.getPublicKey()` returns the user's public key as a hex string without ever exposing the private key to the calling page. `window.nostr.signEvent(event)` takes a partial event with `created_at`, `kind`, `tags`, and `content`, and returns the complete signed event with `id`, `pubkey`, and `sig` added. The key point is that the private key never leaves the extension's isolated context; the web application submits an unsigned event and receives back a signed one.

The optional methods cover encryption: `window.nostr.nip04.encrypt` and `window.nostr.nip04.decrypt` for the older NIP-04 scheme (now deprecated), and `window.nostr.nip44.encrypt` and `window.nostr.nip44.decrypt` for the current NIP-44 scheme. Extensions that support NIP-44 can therefore handle both direct message encryption and any other application that needs pubkey-keyed encryption without the calling page seeing the nsec.

The spec also includes a recommendation to extension authors: load scripts with `"run_at": "document_end"` in the extension manifest so `window.nostr` is available synchronously when the page loads, avoiding race conditions where a client checks `window.nostr` before the extension has injected it.

A key example of NIP-07 in action is the Keycast project covered above. The Keycast web frontend uses NIP-07 to sign NIP-98 HTTP auth events: the SvelteKit app never handles the user's nsec directly. It calls `window.nostr.signEvent` to produce the auth header, then sends that header to the Keycast API. This architecture means the key material stays in the browser extension throughout the entire team key management flow.

```json
{
  "id": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 1,
  "tags": [],
  "content": "Hello from a NIP-07 signed event",
  "sig": "0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2cdd"
}
```

## NIP Deep Dive: NIP-39 (external identities in profiles)

[NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md) defines how a Nostr user can declare control over external platform identities in their profile. Each declaration uses an `i` tag inside a kind:10011 event, asserting ownership of a specific account on another platform together with a proof that can be independently verified.

Each tag follows the format `["i", "platform:identity", "proof"]`, where `platform:identity` combines the platform name and username with a colon separator (`github:semisol`, `twitter:semisol_public`). `proof` points to a verifiable artifact on the platform itself.

For GitHub, the proof is a Gist ID. The user creates a public Gist from their GitHub account containing the text `Verifying that I control the following Nostr public key: npub1...`. A client verifying the claim fetches `https://gist.github.com/<identity>/<proof>` and checks that the Gist was authored by the claimed GitHub username and contains the expected pubkey. For Twitter the proof is a tweet ID, for Mastodon a post ID, and for Telegram a message reference in a public group.

The identity provider name must contain only `a-z`, `0-9`, and the characters `._-/`, and must not contain `:`. Identity names should be normalized to lowercase, with the primary alias used when multiple exist.

The Namecoin `.bit` NIP-05 discussion happening this week shows NIP-39's role in the broader identity stack: it provides a standardized, relay-agnostic way to cross-reference a Nostr key with an established identity elsewhere, without requiring any central verification authority. A client can independently verify the proof by fetching a public artifact on the named platform, and the proof is bound to the specific Nostr pubkey in the Gist or tweet text, not a generic platform credential.

```json
{
  "id": "b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 10011,
  "tags": [
    ["i", "github:semisol", "9721ce4ee4fceb91c9711ca2a6c9a5ab"],
    ["i", "twitter:semisol_public", "1619358434134196225"],
    ["i", "mastodon:bitcoinhackers.org/@semisol", "109775066355589974"]
  ],
  "content": "",
  "sig": "1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3eff"
}
```

---

That's it for this week. If you're building something or have news to share, DM us on Nostr or find us at [nostrcompass.org](https://nostrcompass.org).
