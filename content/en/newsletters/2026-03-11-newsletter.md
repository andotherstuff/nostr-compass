---
title: 'Nostr Compass #13'
date: 2026-03-11
publishDate: 2026-03-11
draft: false
type: newsletters
description: 'Shopstr and Milk Market add MCP commerce surfaces, NIP-42 relay auth lands in Amber and strfry, Route96 ships AI labeling, Samizdat releases Android alpha, NIP-91 merges.'
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** [Shopstr](https://github.com/shopstr-eng/shopstr) and [Milk Market](https://github.com/shopstr-eng/milk-market) add MCP surfaces for agent-driven commerce, while [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber), and [strfry](https://github.com/hoytech/strfry) add [NIP-42](/en/topics/nip-42/) (Authentication of Clients to Relays) relay-auth and protected-event support across app, signer, and relay software. [Route96](https://github.com/v0l/route96) ships two releases around AI labeling, moderation queues, perceptual hashing, and machine-readable server docs. [Samizdat](https://github.com/satsdisco/samizdat), already live on the web, released its first Android alpha and later added [NIP-55](/en/topics/nip-55/) (Android Signer Application) signer support. [Formstr](https://github.com/formstr-hq/nostr-forms) adds signup through [NIP-49](/en/topics/nip-49/) (Private Key Encryption), [Amethyst](https://github.com/vitorpamplona/amethyst) ships Namecoin-based [NIP-05](/en/topics/nip-05/) (Domain Verification) resolution work, [Mostro](https://github.com/MostroP2P/mostro) ships [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4), and the NIPs repo merges [NIP-91](/en/topics/nip-91/) (AND Operator for Filters) and defensive guidance for [NIP-66](/en/topics/nip-66/) (Relay Discovery and Liveness Monitoring).

## News

### Shopstr and Milk Market Open MCP Commerce Surfaces

[Shopstr](https://github.com/shopstr-eng/shopstr), the peer-to-peer marketplace with Lightning and Cashu payments, merged [PR #234](https://github.com/shopstr-eng/shopstr/pull/234) ([commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)), adding an MCP server with API-key authentication for agent account management. The change adds `.well-known/agent.json` for agent discovery, MCP onboarding and status endpoints, order creation and payment-verification routes, dedicated purchase and read tools, and a settings screen for API keys. [PR #236](https://github.com/shopstr-eng/shopstr/pull/236) extends that with seller-side actions for messages, addresses, order updates, and product-spec selection. A security fix in [PR #235](https://github.com/shopstr-eng/shopstr/pull/235) replaces single-iteration SHA-256 API key hashing with salted PBKDF2 at 100,000 iterations.

Agents can read [NIP-99](/en/topics/nip-99/) (Classified Listings) listings and move through checkout using the existing [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) and [NIP-60](/en/topics/nip-60/) (Cashu Wallet) payment flows without scraping pages or reverse-engineering client behavior.

[Milk Market](https://github.com/shopstr-eng/milk-market), a food marketplace on Nostr at [milk.market](https://milk.market), landed the same MCP and API-key foundation in [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3). [PR #10](https://github.com/shopstr-eng/milk-market/pull/10) adds subscription orders, shipping address changes post-purchase, and multi-merchant and multi-currency checkout handling for Stripe and other fiat payment paths. A follow-up [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) fixes a startup database initialization bug where the failed relay publishes table was not created on fresh installs, causing 500 errors on first load. The agent-facing interface works with Bitcoin-native checkout on Shopstr or mixed fiat and Bitcoin checkout on Milk Market.

### NIP-42 Relay Auth Across Bunker, Signer, and Relay

[OAuth Bunker](https://github.com/flox1an/oauth-bunker), a [NIP-46](/en/topics/nip-46/) (Nostr Connect) bunker that bridges OAuth providers to Nostr signing, added [NIP-07](/en/topics/nip-07/) (Browser Extension Signer) login, automatic single-identity selection, and cleanup for deleted identities ([commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). When only one identity exists, the bunker now selects it automatically instead of prompting. Deleting an identity also removes its dangling assignments and connections. [Commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) adds an `ALWAYS_ALLOWED_KINDS` configuration path for assigned users, defaulting to kind `30078` app-specific data, so delegated identities can write to app-specific storage without per-event approval.

[Amber](https://github.com/greenart7c3/Amber), the primary [NIP-55](/en/topics/nip-55/) signer for Android, shipped [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4) with four pre-releases across the week. [PR #317](https://github.com/greenart7c3/Amber/pull/317) adds [NIP-42](/en/topics/nip-42/) relay authentication handling for kind `22242` requests. The implementation adds a new database column tracking relay-specific permissions with a unique index on `(pkKey, type, kind, relay)`. Users see a dedicated auth screen where they can grant or deny per relay or across all relays with a wildcard `*` scope, and persist that choice. Wildcard permissions clear all relay-specific entries for a kind. [PR #318](https://github.com/greenart7c3/Amber/pull/318) follows up by refactoring multi-event request screens to display details inline using composable cards instead of navigating to a separate screen. The release also updates default profile relays, adds bottom-sheet request display, and fixes a crash on MediaTek devices by disabling StrongBox keystore.

On the relay side, [strfry PR #156](https://github.com/hoytech/strfry/pull/156) implements NIP-42 auth handling for [NIP-70](/en/topics/nip-70/) (Protected Events), and [PR #176](https://github.com/hoytech/strfry/pull/176) rejects reposts that embed protected events.

### Notedeck Adds NIP-11 Relay Limits and Agentium Features

[Notedeck](https://github.com/damus-io/notedeck), the native desktop client by the Damus team, merged 14 PRs this week. [PR #1316](https://github.com/damus-io/notedeck/pull/1316) adds [NIP-11](/en/topics/nip-11/) (Relay Information Document) relay limitation fetching, so all outbox relays now respect `max_message_length` and `max_subscriptions` from the relay info document. The implementation includes background job processing, exponential backoff with jitter for connection retries, and custom HTTP Accept headers. [PR #1312](https://github.com/damus-io/notedeck/pull/1312) fixes a bug where DMs sometimes failed to load after account switching, and [PR #1333](https://github.com/damus-io/notedeck/pull/1333) adds a backoff mechanism to multicast relay communication to prevent broadcast spam on errors.

The Agentium subsystem (Notedeck's built-in coding agent UI, internally called "Dave") received clipboard image paste, named run configurations that sync across devices via kind `31991` events ([NIP-33](/en/topics/nip-33/) (Parameterized Replaceable Events)), a git worktree creator, and a model picker for selecting backends per session ([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). [PR #1338](https://github.com/damus-io/notedeck/pull/1338) integrates `egui_kittest` for headless UI testing, and [PR #1339](https://github.com/damus-io/notedeck/pull/1339) adds a dashboard card tracking new contact list creations by client. An open [PR #1314](https://github.com/damus-io/notedeck/pull/1314) ports Amethyst's Namecoin NIP-05 resolution to Notedeck with ElectrumX lookups, SOCKS5 Tor routing, and search bar integration.

### diVine Ships v1.0.6 with E2E Test Infrastructure and NIP-49 Import

[diVine](https://github.com/divinevideo/divine-mobile), the short-form looping video client restoring Vine archives at [divine.video](https://divine.video), shipped [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6) with 127 merged PRs. The release adds [NIP-49](/en/topics/nip-49/) account import, external [NIP-05](/en/topics/nip-05/) support, multi-account handling, macOS and experimental Linux builds, and a redesigned drafts and clips library backed by local storage.

On the engineering side, [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) adds a full E2E integration test infrastructure using Patrol for native UI automation against a Docker backend stack (relay, API, Blossom, Postgres, Redis, ClickHouse). Five auth journey tests cover registration, verification, password reset, session expiry, and token refresh. [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) switches video loading from HLS-first to direct MP4 with automatic HLS fallback, reducing load times from 30-60 seconds to near-instant. [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) caches the home feed API response to SharedPreferences for instant cold-start display. [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) enforces `ai-generated` content labels as hidden in feeds, and [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) adds a safety setting to show only diVine-hosted videos. The Hive-to-Drift profile cache migration continues across [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883), and [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903), replacing ~1,074 lines of Hive code with Drift DAOs.

### Vector v0.3.2 Ships NIP-77 Negentropy Sync and MLS Improvements

[Vector](https://github.com/VectorPrivacy/Vector), a privacy-focused desktop messenger using MLS group encryption with [NIP-17](/en/topics/nip-17/) (Private Direct Messages) and [NIP-44](/en/topics/nip-44/) (Encrypted Payloads) encryption, shipped [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2). The headline change is NIP-77 negentropy for MLS group sync ([commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)), which catches up on missed messages significantly faster using parallel boot. The release also adds a rebuilt audio engine with full Linux support, image spoilers with blurred previews, clickable hyperlinks with rich link previews, `@mention` pings with `@everyone` for group admins, emoji shortcode autocomplete, group muting, tap-to-react on existing reactions, and cancellable file uploads. Vector explicitly filters out NIP-17 group chat events ([commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)), using MLS exclusively for group encryption.

## Releases

### Route96 v0.5.0 and v0.5.1

[Route96](https://github.com/v0l/route96), a media server that supports Blossom and [NIP-96](/en/topics/nip-96/) (HTTP File Storage), shipped [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) and [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1). v0.5.0 adds automated AI labeling, retroactive backfill for unlabeled uploads, moderation queues for flagged files, EXIF-based privacy rejection, and banned-hash handling.

v0.5.1 adds perceptual image hashes, locality-sensitive hashing for similar-image lookup, batch admin endpoints, and a published [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1) describing the server's Blossom and NIP-96 API surface for agent tooling. [PR #58](https://github.com/v0l/route96/pull/58) moves background workers onto fully async Tokio tasks, and [commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) adds backoff to avoid hot loops.

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat), a long-form reader and publisher available at [samizdat.press](https://samizdat.press), shipped its first Android build in [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha). The app opens to a curated Press page of long-form Nostr articles with bottom tab navigation across Press, Feed, Saved, and Write views. The Android build adds native key storage through Android Keystore encryption with biometric unlock, handles `nostr:` URIs and `samizdat.press` deep links, and supports signer handoff via the Android app chooser (Amber, Primal, etc.) instead of requiring direct key import. Pull-to-refresh, safe-area handling across screen sizes, and native share, clipboard, haptics, and splash-screen integrations are now part of the Android shell rather than the web wrapper.

[Commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) adds intent-based [NIP-55](/en/topics/nip-55/) signing for Amber and Primal flows, and [commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) replaces a JavaScript bridge workaround with a native Capacitor plugin using `startActivityForResult`. The app requires Android 7.0+ (API 24), ships as a debug APK in this alpha, and still lacks push notifications. Publishing currently depends on a signer app, while `nsec` login covers local reading and account access.

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), a decentralized calendar app with [NIP-59](/en/topics/nip-59/) (Gift Wrap) private event sharing available at [calendar.formstr.app](https://calendar.formstr.app), shipped [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0) with [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38). The release extends recurring-event handling for [NIP-52](/en/topics/nip-52/) (Calendar Events), moving past the v0.1.0 single-event foundation. The underlying changes also touch local event storage, signer handling, and Android notification plumbing. This is the second active application from the Formstr organization following last month's repository migration.

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro), the peer-to-peer Bitcoin exchange built on Nostr, released [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4). The dispute-session restore ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) and auto-close ([PR #606](https://github.com/MostroP2P/mostro/pull/606)) fixes [covered last week](/en/newsletters/2026-03-04-newsletter/) are included. New in this release: [PR #625](https://github.com/MostroP2P/mostro/pull/625) adds a `days` field to user rating events of kind `38384`, [PR #612](https://github.com/MostroP2P/mostro/pull/612) adds expiration to those rating events, and [PR #614](https://github.com/MostroP2P/mostro/pull/614) switches order events to configured expiration settings instead of a hardcoded 24-hour window. [PR #622](https://github.com/MostroP2P/mostro/pull/622) adds an idempotency check to prevent duplicate development-fee payments.

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile), the Flutter client for the Mostro P2P exchange, shipped [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1) with 11 new features and 11 bug fixes. The release adds encrypted multimedia rendering in dispute chat ([PR #514](https://github.com/MostroP2P/mobile/pull/514)), auto-close of dispute UI when orders reach terminal state ([PR #503](https://github.com/MostroP2P/mobile/pull/503)), QR scanning for NWC wallet import ([commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), French translations, and FCM push notification handling. [PR #496](https://github.com/MostroP2P/mobile/pull/496) fixes a Schnorr signature padding bug by pinning the bip340 dependency to v0.2.0.

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main), the Telegram-style messaging client with Cashu support, shipped [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release) focused on Linux desktop fixes: AppImage dock icons, emoji rendering, context menu freezes, and reply/copy UI hangs. The release also fixes image upload issues and npub.cash integration. [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) eliminates unnecessary UI rebuilds by removing a 3-second polling timer that forced glassmorphic repaints while doing nothing, and unblocks login initialization by running the event cache load concurrently instead of blocking relay, contacts, and channel startup.

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android), a FROST threshold signer for Android with [NIP-55](/en/topics/nip-55/) and [NIP-46](/en/topics/nip-46/) support, shipped [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) and [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1). v0.6.0 adds wallet descriptor coordination and management UI, a backup/restore flow with biometric authentication ([PR #184](https://github.com/privkeyio/keep-android/pull/184)), nsec recovery from threshold shares ([PR #187](https://github.com/privkeyio/keep-android/pull/187)), cross-platform animated QR frame generation via Rust UniFFI ([PR #188](https://github.com/privkeyio/keep-android/pull/188)), and a signing audit trail with chain verification ([PR #189](https://github.com/privkeyio/keep-android/pull/189)). v0.6.1 switches the license from AGPL-3.0 to MIT ([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump), the static gateway for viewing Nostr content at [njump.me](https://njump.me), shipped [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0) with a breaking change in `note1` code parsing and an update to the underlying nostr library.

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr), a decentralized road event reporting app using Nostr, shipped its initial demo release [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1). The app displays road events on a map using vector tiles from openfreemap.org.

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core), an e-bill application with a Nostr transport layer and dedicated relay at [bit.cr](https://www.bit.cr/), shipped [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3). [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) adds `payment_actions` and `bill_state` fields to the API for payment and acceptance state, and [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) fixes signing address handling for anonymous signers.

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat), a chat application built on the Marmot protocol's .NET MLS and C# libraries, shipped [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3). The release adds external signer support for Amber and [NIP-46](/en/topics/nip-46/) flows ([commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), moves MLS state persistence into the MLS service to eliminate crash-window data loss ([commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)), and publishes Windows, Linux, and Android builds through a new CI pipeline.

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal), a Kotlin Multiplatform trading copilot for Nostr, shipped [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0). The release packages shared KMP modules for domain logic, chart rendering, Nostr authentication and publishing, Blossom [NIP-96](/en/topics/nip-96/) upload support, and ONNX-based AI inference hooks across Desktop and Android shells. The published architecture also includes a FastAPI AI service for chart screenshot analysis, model training pipelines, and a risk engine that produces structured trade plans with sizing and warnings. Login supports either raw `nsec` keys or external signers, and the output flow ends in Nostr event publishing rather than local-only analysis.

## Project Updates

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms), the Google Forms alternative on Nostr, merged [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) ([commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)), adding a signup flow using [NIP-49](/en/topics/nip-49/) (Private Key Encryption) encrypted private keys. Before this change, users needed either a [NIP-07](/en/topics/nip-07/) browser extension or a raw `nsec` paste to use Formstr. The new flow generates a key pair client-side, encrypts the private key with a user-chosen password via NIP-49's scrypt + XChaCha20-Poly1305 scheme, and stores the resulting `ncryptsec` string. Users can then log back in with their password without installing a signer extension. Key management stays client-side throughout.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), the feature-rich Android client, merged four PRs shipping the Namecoin-backed [NIP-05](/en/topics/nip-05/) resolution work that was [open last week](/en/newsletters/2026-03-04-newsletter/). [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) adds censorship-resistant NIP-05 verification via ElectrumX for `.bit`, `d/`, and `id/` identifiers. When Amethyst detects one of these suffixes in a NIP-05 field, it queries an ElectrumX-NMC server for the name's transaction history, parses the `NAME_UPDATE` script from the latest output to extract the Nostr pubkey, and rejects names older than 36,000 blocks (Namecoin's expiry window). ElectrumX connections route through SOCKS5 when Tor is enabled, with dynamic server selection between clearnet and `.onion` endpoints. An LRU cache with a one-hour TTL prevents repeated blockchain queries.

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) fixes race conditions and resolver correctness in that flow. [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) lets new users import a follow list during signup from either ordinary NIP-05 identifiers or Namecoin-backed ones. [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) adds custom ElectrumX server settings so users can choose which server handles their lookups.

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb), a library providing helper methods for storing Nostr events in IndexedDB, merged [PR #6](https://github.com/hzrd149/nostr-idb/pull/6) adding support for [NIP-91](/en/topics/nip-91/) AND tag filters. The change adds intersection semantics to the client-side filter matching so IndexedDB queries can require all listed tag values rather than any one. [PR #8](https://github.com/hzrd149/nostr-idb/pull/8) updates the library to the latest NIP-DB interface, and a follow-up [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) fixes a subscribe deadlock and removes nostr-tools as a production dependency.

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve), an archive-first Nostr indexer with ClickHouse analytics, merged [PR #8](https://github.com/andotherstuff/pensieve/pull/8) adding per-entry cache TTL enforcement and per-key miss coalescing to reduce API CPU spikes. The highest-cost time-series endpoints (engagement stats, hourly activity, per-kind activity) now use 10-minute server-side TTLs instead of triggering synchronized recompute storms.

### Blossom

[Blossom](https://github.com/hzrd149/blossom), the decentralized media-hosting protocol and server stack, merged two BUD-11 authorization updates. [PR #91](https://github.com/hzrd149/blossom/pull/91) moves optional authorization into its own BUD and clarifies the role of the `x` and `server` tags. [PR #93](https://github.com/hzrd149/blossom/pull/93) cleans up endpoint-specific auth behavior and formalizes the `X-SHA-256` header for upload verification. The two PRs consolidate auth logic into BUD-11 and remove ambiguities around request hashing for upload, delete, and media-management flows.

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-91](/en/topics/nip-91/) (AND Operator for Filters)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)): Adds intersection semantics for tag filters, letting relays answer queries that require all listed tag values instead of any one of them. Reduces client-side post-filtering and bandwidth on tag-heavy queries.

- **[NIP-66](/en/topics/nip-66/) (Relay Discovery and Liveness Monitoring): Defensive Measures** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)): Following the [outbox benchmark work covered last week](/en/newsletters/2026-03-04-newsletter/), the spec now adds warnings around unhappy paths for relay monitoring data. Clients must not require kind `30166` monitoring events in order to function. A monitor can be wrong, stale, or malicious. Clients are expected to cross-check sources and avoid cutting off large parts of a user's relay graph based on a single feed.

- **[NIP-39](/en/topics/nip-39/) (External Identities in Profiles): kind 10011 Registry Cleanup** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)): Adds the kind `10011` reference directly to the spec, aligning with Amethyst's implementation [covered last week](/en/newsletters/2026-03-04-newsletter/).

**Open PRs and Discussions:**

- **[NIP-70](/en/topics/nip-70/) (Protected Events): Reject reposts that embed protected events** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)): If a relay enforces NIP-70 on the original event but accepts reposts carrying the same content, the `-` tag has no practical effect. This PR adds the rule that relays must also reject kind 6 and kind 16 reposts of protected events. [strfry PR #176](https://github.com/hoytech/strfry/pull/176) already implements this.

- **[NIP-71](/en/topics/nip-71/) (Video Events): Multiple Audio Tracks** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)): Adds audio `imeta` tags for alternate tracks, language variants, and audio-only streams. A client could keep a stable video file while switching audio languages, or serve audio as a separate track for podcast-like content.

- **[NIP-11](/en/topics/nip-11/) (Relay Information Document) and [NIP-66](/en/topics/nip-66/) Relay Attributes** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)): Adds a structured `attributes` field to relay information documents, giving clients and discovery tools machine-readable metadata beyond the current free-text description.

## NIP Deep Dive: NIP-49 (Private Key Encryption)

[NIP-49](/en/topics/nip-49/) defines how a client encrypts a private key with a password and encodes the result as an `ncryptsec` bech32 string. [Formstr](#formstr) uses NIP-49 in its new signup flow.

The format is not tied to a dedicated event kind. A client starts with the raw 32-byte secp256k1 private key, derives a symmetric key from the user's password with scrypt, encrypts the key using XChaCha20-Poly1305, then wraps the result into a bech32 `ncryptsec` string. A one-byte flag records whether the key was ever known to have been handled insecurely before encryption.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

The JSON event above is an application-level example, not a NIP-49 requirement. The NIP standardizes the encrypted key format. A client can store the `ncryptsec` locally, sync it through app-specific storage, or export it as a backup string. Passwords are normalized to Unicode NFKC before key derivation so the same password decrypts consistently across clients and platforms.

The one-byte key-security flag has three defined values: `0x00` means the key's handling history is unknown, `0x01` means the key is known to have been handled insecurely (e.g., pasted as plaintext in a web form before encryption), and `0x02` means the key was generated and encrypted in a safe context and has never been exposed. Clients can use this to show warnings when importing keys with a known-insecure history.

NIP-49 protects keys better than plain `nsec` export, but the encryption is only as strong as the password and the configured scrypt cost. Higher `LOG_N` values make offline guessing harder but slow down legitimate decrypt operations. The spec warns against publishing encrypted keys to public relays, since attackers benefit from collecting ciphertext for offline cracking. For comparison, [NIP-46](/en/topics/nip-46/) remote signing avoids exposing keys entirely, and [NIP-55](/en/topics/nip-55/) Android signing keeps keys inside a dedicated signer app. NIP-49 fills a different slot: portable encrypted backup for users who manage their own keys.

Implementations include [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) for signup, [Amber](https://github.com/greenart7c3/Amber) for ncryptsec backup and restore, [diVine v1.0.6](#divine-ships-v106-with-e2e-test-infrastructure-and-nip-49-import) for account import, [Keep v0.6.0](#keep-v060) for FROST share export, and key management tools like [nsec.app](https://nsec.app) and [Alby](https://github.com/getAlby/hub).

## NIP Deep Dive: NIP-70 (Protected Events)

[NIP-70](/en/topics/nip-70/) defines protected events. When an event carries the tag `["-"]`, a relay must reject it unless the relay requires [NIP-42](/en/topics/nip-42/) authentication and the authenticated pubkey matches the event author.

The NIP-42 auth flow works as follows: the relay sends an `AUTH` challenge containing a random string, and the client responds with a signed kind `22242` event whose tags include the relay URL and the challenge. The relay verifies the signature and checks that the pubkey in the auth event matches the pubkey in the protected event being published. If the pubkeys do not match, the relay rejects the event with a `restricted` message prefix.

The event content can still be public. The `-` tag only controls who can publish the event to a relay that honors the tag. This covers [NIP-29](/en/topics/nip-29/) (Simple Groups) semi-closed feeds, member-only relay spaces, and other contexts where the author wants to limit redistribution through the relay graph. NIP-70 is a single-tag convention, not a new event kind, so any existing event kind can carry the `-` tag.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

Even if a relay blocks third-party publishing of the original event, someone can republish the content inside a repost. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) addresses this by requiring relays to also reject kind 6 and kind 16 reposts of protected events. [strfry PR #156](https://github.com/hoytech/strfry/pull/156) adds NIP-42 auth handling for protected events, and [strfry PR #176](https://github.com/hoytech/strfry/pull/176) blocks reposts that embed protected content.

NIP-70 controls relay behavior. A recipient can still copy the content elsewhere, and the spec says so. The `-` tag gives relays a machine-readable signal to refuse republication. For comparison, [NIP-62](/en/topics/nip-62/) (Request to Vanish) asks relays to delete data after the fact, while NIP-70 prevents unauthorized publishing at ingest time. The two are complementary: an author can mark events as protected to limit spread, and later request deletion if they want the content removed from relays that did accept it.

---

That's it for this week. Building something or have news to share? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via [NIP-17](/en/topics/nip-17/) DM</a> or find us on Nostr.
