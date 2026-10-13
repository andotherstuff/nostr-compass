---
title: "Nostr Compass #44"
date: 2026-10-14
publishDate: 2026-10-14
draft: false
type: newsletters
description: "Desktop Amethyst, Amber security fixes, private attachments, authenticated software installs, and content warnings and status."
---

**[Amethyst](#amethyst)** brings its Android interface to desktop and adds native Wayland support. **[Amber](#amber)** fixes permission revocation, copied-secret clearing and a settings change that could lose keys. **[Keep](#keep-android)** tightens automatic signing permissions, while **[MDK](#mdk)** ships streaming private attachments and oldest-first message catch-up. **[Zap Cooking](#zap-cooking)** merges safeguards for follow-list edits and authenticated membership. [Release details](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0) follow, alongside protocol changes and public-status mechanics.

## Top Stories

### Amethyst

[Amethyst v1.18.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.18.0) brings the Android social client's shared interface to desktop, with custom feeds, wide-window decks, opt-in locks, encrypted media and [Blossom uploads](/en/topics/blossom/). Provider scores from [NIP-85, trusted assertions](/en/topics/nip-85/), are indexed locally for requests, notifications and badges, with user-selected providers and thresholds.

Today's [v1.19.0 release](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0) adds native Wayland support and desktop video compression using separately installed FFmpeg and ffprobe. Key-storage fixes address repeated keychain prompts and Linux keyring failures. Calendar collections and RSVPs gain rendering, and the Android login interface adds [NIP-46 remote signing](/en/topics/nip-46/). Parallel opening of encrypted envelopes precedes serial indexing, while relay reconnection and feed-author relay-list handling are corrected. The [relay client honors rate-limit backoff](https://github.com/vitorpamplona/amethyst/pull/4422) before resuming subscriptions or publications.

The [trust-provider relay change](https://github.com/vitorpamplona/amethyst/pull/4437) treats provider relays from the user's kind 10040 list as own, trusted relays. Those connections use a direct route by default; Tor requires enabling the trusted-relays setting. The main client's [NIP-42 relay authentication](/en/topics/nip-42/) can disclose the user's public key to these relays.

### Amber

[Amber 6.6.9](https://github.com/greenart7c3/Amber/releases/tag/v6.6.9) fixes three security flaws in the Android Nostr signer. [Revoked permissions](https://github.com/greenart7c3/Amber/security/advisories/GHSA-8f7m-9g64-vrjw) no longer survive a cache race, and explicit rejections override fully trusted status. [Copied secrets](https://github.com/greenart7c3/Amber/security/advisories/GHSA-g62f-m6pm-jv9p) receive a system-scheduled clipboard clear after 60 seconds, including when the process is killed; contents remain readable during that interval, and newer copied text may also be cleared. Changing [“require unlocked device”](https://github.com/greenart7c3/Amber/security/advisories/GHSA-wv7c-hq2j-ppc5) preserves the old wrapping key until secret migration completes, while previously lost keys remain lost. The release repairs multi-request nostrconnect approvals and replies on the URI's specified relays. Users of 6.6.8 and earlier should update.

### Keep Android

[Keep Android v1.3.0](https://github.com/privkeyio/keep-android/releases/tag/v1.3.0), a [FROST threshold signer](/en/topics/frost/), adds on-device distributed key generation and authenticated recovery of interrupted share operations. It also handles devices without StrongBox support. With threshold signing, participating devices hold shares of the signing secret and cooperate to produce a signature; the setup and recovery steps determine which devices can participate.

[Version 1.3.1](https://github.com/privkeyio/keep-android/releases/tag/v1.3.1) prevents automatic signing from overriding remembered refusals, Ask permissions, expired approvals or failed permission reads. Expiry removes background approval while retaining denials. The [per-app policy migration](https://github.com/privkeyio/keep-android/pull/532) moves permissions into the core-owned store while preserving stricter decisions.

### Chama

[Chama v6.4.21](https://github.com/jesuspirate/chama/releases/tag/v6.4.21) [authenticates the native wallet bridge](https://github.com/jesuspirate/chama/pull/29) used by its Nostr-mediated trade application, disables production URL-based bridge redirection and validates payout amounts. It also refuses to wipe a wallet whose contents cannot be read.

[Version 6.4.22](https://github.com/jesuspirate/chama/releases/tag/v6.4.22) hardens replay against outsider events, checks successor relationships, rejects empty arbiter pools and derives refund timing from the signed LOCK time. Its consensus changes apply to CREATE events signed from November 1, 2026; the client protections apply immediately. The release notes retain caveats about listing-selected federations and dust payouts. Subsequent [signer and recovery changes](https://github.com/jesuspirate/chama/releases/tag/v6.4.23) add protected-seed readers and recoverable late locks, while [v6.4.24](https://github.com/jesuspirate/chama/releases/tag/v6.4.24) improves large trade lists.

### Zap Cooking

The recipe and social client [Zap Cooking merges safeguards for follow-list edits](https://github.com/zapcooking/frontend/pull/795) against incomplete, stale or unexpectedly shrinking reads. Follow actions share one guarded update path that preserves existing tags and content. Signer identity is checked before publication. Its [membership authorization fix](https://github.com/zapcooking/frontend/pull/802) uses the public key signing the authenticated request. A [route that exposed an administrative secret was removed](https://github.com/zapcooking/frontend/pull/801); deployment still requires secret rotation, which a merged change alone cannot establish. Later [thread and bookmark repairs](https://github.com/zapcooking/frontend/pull/833) preserve the real reply root and recover failed bookmark writes. [Recipe tag fields](https://github.com/zapcooking/frontend/pull/836) no longer send keystrokes to profile or NIP-50 search services or leave the editor with unsaved changes.

## Tagged Releases

### MDK

[MDK v0.13.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.13.0), the runtime for [Marmot encrypted groups](/en/topics/marmot/), adds streaming and resumable private attachments with progress and cancellation. It also sends private [NIP-56 reports](/en/topics/nip-56/) to the deployment operator through [NIP-59 gift wraps](/en/topics/nip-59/), omitting message, group and relay identifiers. Catch-up processes oldest-first batches of up to 256 events and preserves relay CLOSED refusals. SOCKS5 routing covers relays, media and discovery services without a direct fallback.

The [release guide](https://github.com/marmot-protocol/mdk/blob/v0.13.0/docs/release/0.13.0.md) requires bindings, headers and native artifacts to move together. Database schemas advance from 101 to 107 without a downgrade path. Host secret storage needs migration. MarmotKit and C artifacts are stable; WN Agent remains a prerelease and workspace crates are unpublished on crates.io. History arriving more than five [MLS epochs](/en/topics/mls/) late can still be undecryptable without an incomplete-history notice, and authenticated agent clients retain access to the whole API.

The release also [retries profile, follow-list and relay-list saves left pending after the first acknowledgement](https://github.com/marmot-protocol/mdk/pull/2228); these background retries do not survive restart. [Invitation lookup checks KeyPackage deletion and expiry on discovery relays](https://github.com/marmot-protocol/mdk/pull/2211), whose answers cannot prove the recipient still holds its private KeyPackage material. [Activity-reaction targets](https://github.com/marmot-protocol/mdk/pull/2187) now derive consistently from authenticated actors and individual group commits; older actorless history remains incomplete.

Later master work [closes leaked relay subscriptions and pages activation replays clamped to 500 events](https://github.com/marmot-protocol/mdk/pull/2274). [Epoch-gap recovery](https://github.com/marmot-protocol/mdk/pull/2298) fetches a failed comparison relay's newest 256 events without certifying complete history. [Self-update commits retry every missed group relay](https://github.com/marmot-protocol/mdk/pull/2275). New advisory checks cover [known stale epochs](https://github.com/marmot-protocol/mdk/pull/2273) and [commits still owed to relays](https://github.com/marmot-protocol/mdk/pull/2288); users can acknowledge the risk, so these do not guarantee that a group cannot fork.

[Storage-blocked attachment downloads](https://github.com/marmot-protocol/mdk/pull/2249) retain resumable progress when free space is insufficient. Large explicit downloads use a file sink, with staging and checkpoints requiring roughly five to six times the body size in free space. [Verified public-event previews](https://github.com/marmot-protocol/mdk/pull/2304) gain a bounded encrypted account cache, while [obsolete-only KeyPackage results](https://github.com/marmot-protocol/mdk/pull/2305) become distinguishable from incomplete relay lookups. These are later source changes requiring matching host adoption; event-ID previews from completed fetches do not recheck later deletions.

The agent bridges also [bound backend output](https://github.com/marmot-protocol/mdk/pull/2103) to prevent oversized replies from exhausting memory, and [accept the connector's actual deletion response](https://github.com/marmot-protocol/mdk/pull/2301). Previously delivered text remains delivered when an output limit stops a turn.

### Myco

[Myco v0.11.0](https://github.com/Origami74/myco/releases/tag/v0.11.0) adds USB links between phones or fips desktops and adopts [the current proposed NIP-5D manifest format](https://github.com/Origami74/myco/pull/135), with signed artifact and icon hashes. Older phones can still pair but need updating to open these napplets. Its [download-policy changes](https://github.com/Origami74/myco/pull/133) distinguish Internet, mesh and user-configured HTTP destinations. Author-provided hints and redirects cannot probe local networks under the Internet policy, while destinations configured by the user remain unrestricted. The software client also [discovers blobs on the author's BUD-03 Blossom servers](https://github.com/Origami74/myco/pull/134). That improves artifact discovery but exposes installation traffic to those servers. These HTTP changes do not establish equivalent protections for WebSocket connections. [Nearby mesh availability checks](https://github.com/Origami74/myco/pull/132) probe peers for blobs without downloading them or contacting public Blossom servers. These bounded HEAD requests require mesh permission; a holder count does not prove the whole artifact remains available.

The release also [races upstream DNS servers](https://github.com/Origami74/myco/pull/137) to avoid roaming-carrier timeouts blocking relay and artifact lookups. Outbox publications target every listed write relay, with slower destinations delivered in the background. Internet mesh remains off by default, and web pictures are not retained across restarts.

### Unfiltered

[Unfiltered 1.0.13](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.13) adds read/write relay lists and outbox routing to its Android photo client. Its [release notes](https://njump.me/nevent1qqsy8287ykdstql8ec2udgr8slj3czzkkdkjjc36xwn4lnjrrhggfwgu8dmj2) describe relay roles, and accounts without a list begin with three public defaults. Nearby uses coarse geohashes and adjacent cells; adding location to a post is opt-in and off by default. Those tags still reveal an area publicly. The inspected publish result means queued to a socket, with relay acceptance still unconfirmed.

### monostr

[monostr 0.17.0](https://github.com/schmidt1024/monostr/releases/tag/v0.17.0) lets users receive Monero tips through a personal watcher, while [0.18.0](https://github.com/schmidt1024/monostr/releases/tag/v0.18.0) hides new setups’ tip amounts and notification sender names by default. Pictures default to tap-to-load, and optional Primal counts and client tags are disabled. A hosted watcher still learns every incoming payment to the registered wallet through its private view key. Public receipts retain the recipient, time and referenced post even when amounts are hidden.

### Grocery

[Grocery 1.0.2](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.2) combines shared encrypted shopping lists with passkey-backed Nostr identities and per-list Marmot chat. Lists can be joined by pasting a bearer key, which grants reading and editing. Passkey login depends on browser and provider support for WebAuthn’s pseudo-random-function extension; member tags remain visible to relays. [Version 1.0.3](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.3) preserves lists across reopening by caching decrypted contents locally, fixing cases where only the key survived until a relay re-delivered the list.

### Roadstr

[Roadstr 1.1.0](https://github.com/roadstrapp/roadstr-app/releases/tag/v1.1.0) reads another Roadstr client’s kinds 1315/1316 with their intended lifetimes and confirmation rules. A compact codec preserves reconstructible signed reports for an experimental MeshCore radio and relay bridge. Compatible publishing and radio transmission are off by default, with consent before sharing. Radio reports expose position, time and the signing public key to anyone in range. Tests used simulated radios; real hardware, Android BLE and public-relay publication remain unverified.

### OUTKAST

[OUTKAST 1.1.3](https://github.com/Lwb89dev/outkast/releases/tag/v1.1.3) improves article comments and quoted-post handling in its Android client. Article comments use kind 1111 with the article as root and the comment as parent, while ordinary note replies remain kind 1. Quote discovery accepts both q tags and older link-bearing e mentions; newly published quotes add q tags. Failed publication rolls back optimistic reactions.

### Bookshelf

[Bookshelf 0.1.28](https://github.com/decent-newsroom/bookshelf-app/releases/tag/v0.1.28) describes [reading nested](https://njump.me/nevent1qqs8pukgjrnuzryv0z67lze2y0jsshepdckuss25qggvwn5skxqfa7gslzul0) kind-30040 publication indexes containing both chapters and child indexes in publisher order. Offline copies retain that hierarchy and bookmarks tied to each occurrence. Refreshing fetches current revisions by coordinate, but keeps the previous download when results are incomplete, older or unsuccessful. Rebroadcasting preserves original signed descendants. Bounded expansion and readable partial branches prevent missing structure from being presented as a completed book.

### Ditto

[Ditto 2.45.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.45.0) replaces Global with Discover across its content feeds. Discover draws from people followed by the user’s follows and ranks posts by shared connections, excluding the user and accounts already followed. Logged-out users and accounts without follows see a selected starter network instead. This changes the scope of default discovery to a social neighbourhood; spam resistance and the trustworthiness of those accounts remain separate questions.

### Postr

[Postr 1.1.2](https://njump.me/nevent1qqsf4uu87v5r7awyfhktjqnuc9m6xzfngpvr7gj37zca05sx7lk03vqy4wq7x) keeps selected profile identities attached to mentions through saved drafts and publication. The composer freezes the account, text, mentions and attachments during signing and sending, retaining incoming shares until that operation finishes. Retries preserve the original signed event, including older pending posts. Typing a name after @ is insufficient: users must select a profile, and identities already lost from old drafts need to be selected again.

### Nostrautica

[Nostrautica Android 0.11.0](https://github.com/jooray/nostrautica/releases/tag/android-v0.11.0) links communities to their meetups. Approval for a linked event can also grant community membership without a second approval; the join form discloses this and lets applicants opt out. Existing attendees receive a one-tap invitation. Events retain their own participants, matching and chat while the community lists its events. Release notes describe support for different event and community coordinators, without establishing independent interoperability or encryption testing.

### Minibits

[Minibits v0.4.4 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.4-beta.1) repairs Android [Nostr Wallet Connect](/en/topics/nip-47/) payment processing that could stop while the wallet was backgrounded and accumulate into an application-not-responding failure. The native release bundles five months of earlier over-the-air changes. [Version 0.4.5 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.5-beta.1) fixes Android-to-iOS NFC transfer; future over-the-air updates require this version. These are release-reported fixes, with background processing still dependent on the phone's lifecycle restrictions.

### NoorNote

[NoorNote v1.9.0](https://github.com/77elements/noornote/releases/tag/v1.9.0) lets users publish recipes from its article editor, open shared recipe packs and browse recipes from followed authors. Website cards and profile grids covered last week now ship in the release, alongside relay rate-limit handling and direct Android `nostr:` links. Website links remain distinct from verifying a site's contents; gateway access exposes a clicked request to that gateway.

### Gittr

[Gittr v1.0.2](https://github.com/arbadacarbaYK/gittr/releases/tag/v1.0.2) packages its Nostr Git forge for Android, using Amber through [NIP-46 remote signing](/en/topics/nip-46/). The APK opens the existing hosted `gittr.space` application, so users still depend on its served browser code and availability. Browser-extension signing is unavailable inside this wrapper; self-hosting remains a separate Git deployment.

### Dart NDK

[Dart NDK 0.11.0 development zero](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.0) brings the Dart and Flutter toolkit's [authentication-consent handler](https://github.com/relaystr/ndk/pull/862) and NIP-46 signer relay switching into a prerelease. These changes were covered last week as merged work and have now been released. The signer can follow a replacement relay list, which applications must persist. [Development one](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.1) adds support for lettered NIP identifiers in relay information. Both releases carry breaking integration changes.

### Cambium

[Cambium v0.9.0](https://github.com/forgesworn/cambium/releases/tag/v0.9.0) gives native Android apps [four approval choices](https://github.com/forgesworn/cambium/pull/32): once, one hour, one day or indefinitely. Grants are scoped by operation and event kind. Cambium forwards requests to a Heartwood hardware signer through remote signing; Heartwood still decides which requests it signs. Website approvals remain one-shot. Paired signers gain test and reconnect controls, supported transport-relay updates and redacted diagnostics. [NIP-55, Android signing](/en/topics/nip-55/), batches preserve request order and individual rejections, with visible one-shot consent for ambiguous reused intents.

### Grain

[Grain v0.8.1](https://github.com/0ceanSlim/grain/releases/tag/v0.8.1) repairs its Go client library's [NIP-42 relay authentication](/en/topics/nip-42/) for applications serving multiple users. Each `UserContext` owns private authenticated connections, relay preferences and connection holds; the shared pool never authenticates. The library validates incoming IDs and signatures, checks subscription matches and serializes tag and time filters correctly. Authenticated callers must migrate to `UserContext`. Relay storage and serving are unchanged, and authentication still requires a challenge when the connection opens.

### Nmail

[Nmail v0.18.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.18.0), an encrypted mail client, places unfamiliar senders in Requests and blocked senders in Spam. Acceptance and blocking synchronize across devices. Existing inbox senders need acceptance, with Accept all available; Spam stays silent and waiting requests avoid repeated sender alerts. Replies use the receiving identity. Private-relay management, device-lock checks before copying synchronization codes, shared themes, richer contact preservation and a Windows installer accompany mailbox restoration fixes after reset or login.

### Meiso

[Meiso v1.5.0](https://github.com/higedamc/meiso/releases/tag/v1.5.0) ships encrypted comments and unread indicators for its Nostr-synchronized task manager. Comments use addressable kind 35002 events with [NIP-44 encryption](/en/topics/nip-44/), keeping their task association inside the ciphertext. The release [fixes offline sends](https://github.com/higedamc/meiso/pull/212), reconnect catch-up, startup with saved relays and propagation of empty lists. It also prevents partial synchronization from deleting tasks. The unread and catch-up features do not add a notification service for a closed application.

### Haps

[Haps v0.1.13](https://github.com/mmalmi/haps/releases/tag/v0.1.13), an experimental software installer, requires an audit of the exact release from the user's [web of trust](/en/topics/web-of-trust/) by default. Audits can compare pinned source and rebuilt artifacts, and remain private or be published. [Version 0.1.14](https://github.com/mmalmi/haps/releases/tag/v0.1.14) asks users to confirm the publisher when installing by bare name; automation must specify one. Audits supply evidence, while native programs and build recipes still execute without a sandbox. The audit requirement can be bypassed for one operation; signature, integrity and publisher-confirmation checks remain.

### Sidecar

[Sidecar v1.16.0](https://github.com/dmnyc/sidecar/releases/tag/v1.16.0) adds [livestream discovery and playback](https://github.com/dmnyc/sidecar/pull/479) to its browser-extension social client, with signed chat, reactions and zaps. Saved stream bookmarks support encrypted account backup and restore, and private notification mutes let users control alerts. Search gains follow and mute controls; automatic locking and wallet-history refresh changes accompany them.

### Ants

The search interface [Ants v0.7.0](https://github.com/dergigi/ants/releases/tag/v0.7.0) [routes structured searches](https://github.com/dergigi/ants/pull/316) to authors' advertised write relays and mentioned users' read relays through [NIP-65 relay lists](/en/topics/nip-65/), without login. Discovery limits the number of identities and relays consulted, and stops on cancellation or timeout. Missing lists retain fallback routing. Text queries still use verified [NIP-50 search relays](/en/topics/nip-50/).

### soyLI

[soyLI v0.27.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.27.0), a napplet publisher and player for proposed [NIP-5D applications](/en/topics/nip-5d/), adds keyboard bindings and forkless proposals through GRASP, a Git hosting service, with exact-revision retry checks. Its [v0.26.0 release](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.0) distributes signed releases to verified outbox relays after primary publication; deletion tracks attempted destinations but cannot recall unknown copies. [Version 0.26.1](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.1) raises read, play and review budgets to 100 MiB while retaining a 25 MiB limit for new builds and publication. Later [direct presentation metadata](https://github.com/zeSchlausKwab/napplet-soy/pull/14) places author covers and clips directly on signed manifests, retiring the companion event. Frozen older jobs remain supported; this versioned Soy extension requires compatible readers and is not part of the pinned NIP-5D specification.

### nostream

The relay server [nostream v3.3.0](https://github.com/cameri/nostream/releases/tag/v3.3.0) adds [NIP-66 relay monitoring](/en/topics/nip-66/) probes for WebSocket read and write round-trip times, optional authentication detection and mirror-target discovery. It warns when observed behavior disagrees with [NIP-11 relay information](/en/topics/nip-11/). Rate-limited OK responses can include an optional fifth element containing a millisecond backoff. [Version 3.4.0](https://github.com/cameri/nostream/releases/tag/v3.4.0) adds a fourth, millisecond backoff element to [CLOSED responses](https://github.com/cameri/nostream/pull/821) when IP message limits reject `REQ` or `COUNT`. It ships the [PostgreSQL negentropy reconciliation core](https://github.com/cameri/nostream/pull/809) and ordered event inventory; [NIP-77](/en/topics/nip-77/) relay wire messages and capability advertising remain separate work.

### Bark

[Bark v1.3.15](https://github.com/forgesworn/bark/releases/tag/v1.3.15) gives remote-signing approvals keyboard controls, explicit event and identity review, and [one, five or ten minutes to decide](https://github.com/forgesworn/bark/pull/52). Background enforcement rejects expired decisions and queued requests; failed decision delivery keeps the popup open for retry. [Version 1.3.17](https://github.com/forgesworn/bark/releases/tag/v1.3.17) makes [NIP-07 browser signing](/en/topics/nip-07/) available when the signer handshake completes, while optional diagnostics continue. It restores bridges on existing tabs after updates.

### Mostro

[Mostro v0.19.3](https://github.com/MostroP2P/mostro/releases/tag/v0.19.3) answers identity-authenticated requests for the user's own reputation, even without an open order. The peer-to-peer exchange sends replies privately to the requesting trade key, and a [merged CLI command](https://github.com/MostroP2P/mostro-cli/pull/203) exposes that query. Reputation import remains a preview whose imports are unimplemented; operators should leave it disabled. [Later merged work](https://github.com/MostroP2P/mostro/pull/1057) publishes the Lightning escrow guardian margin and rejects unsafe configurations; its 18-block minimum assumes LND's default hold-expiry setting.

### Elisym

[Elisym's commerce 0.11.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.11.0) supports fees deducted from merchant revenue, with a signed store-profile tag declaring split-payment support and incompatible stores refused when a fee applies. [Merged admin work](https://github.com/elisymlabs/elisym/pull/170) reads orders and listings from Nostr relays. It asks for the store's secret key, requiring trust in served browser code and extensions; the local admin remains available. Hosted deployment and mainnet fee activation remain unverified. [Merchant-node 0.10.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/merchant-node%400.10.0) upgrades its ledger without downgrade support.

### Routstrd

[Routstrd v0.4.16](https://github.com/Routstr/routstrd/releases/tag/v0.4.16) prevents a timed-out [Nostr Wallet Connect](/en/topics/nip-47/) refill from immediately producing another payable invoice. It [checks the existing mint operation](https://github.com/Routstr/routstrd/pull/144) until payment succeeds or fails; an unavailable status keeps the refill paused. The inference gateway enables providers by Nostr review label, with experimental labels requiring explicit opt-in. [Version 0.4.17](https://github.com/Routstr/routstrd/releases/tag/v0.4.17) includes the supporting SDK. The unsettled-operation guard remains in memory, so restarting the daemon loses that protection.

### Buzz

[Buzz desktop 0.5.28](https://github.com/block/buzz/releases/tag/desktop-v0.5.28) lets authenticated staff [browse and moderate every community](https://github.com/block/buzz/pull/8027) on a relay without switching connections. Administrative actions retain the reviewed community, relay and signer; disabled authentication leaves the console available for reading. Separately [merged relay work](https://github.com/block/buzz/pull/8197) hides properly tagged deletion events for private author records across queries and live delivery. That server repair requires deployment and leaves previously disclosed copies and historical untagged deletion records outside the fix.

### Earthly

[Earthly v0.1.21](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.21) lets users [embed public Nostr map datasets on websites](https://github.com/zeSchlausKwab/earthly/pull/35), with a preview and controls for appearance and initial camera position. Its Maps MCP integration creates and publishes maps from chat, then generates sharing links or embeds. The integration remains a personal connected-plugin pilot. Embeds support inline datasets up to 300 features and 48 KiB; private, unpublished and blob-backed datasets are excluded.

### Milk Market

[Milk Market's mobile v0.3.0](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.0) brings full storefront design editors to its seller app, with the same sections and fields as the web editor. Per-product page design can override theme and section choices, including metadata and social images. The release adds checks to keep mobile and web configurations aligned. [Version 0.3.1](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.1) corrects contrast in the mobile preview card; Android downloads are attached to the releases, with iOS availability on TestFlight.

### Zeus

[Zeus v13.2.3](https://github.com/ZeusLN/zeus/releases/tag/v13.2.3) includes the [LDK routing-fee repair](https://github.com/ZeusLN/zeus/pull/4353) covered last week, which has now shipped. Its LDK-backed Nostr Wallet Connect service can include reported routing fees in responses and spending records. Budget checks still cover the invoice amount before settlement, with rounded fees debited afterward and a separate 1,000-satoshi routing-fee cap. The release also updates embedded LND and includes rust-lightning security fixes; live NWC device validation remains unverified. Later [merged Zaplocker removal](https://github.com/ZeusLN/zeus/pull/4933) retires its Nostr attestation and redemption flow. Upgrading with payments still held by that server removes redemption; senders must wait for hold-invoice expiry and refund. That retirement is outside v13.2.3; rollout depends on disabling the server and warning existing users.

## In Development

### nosvelte

[nosvelte's event-verifier fix](https://github.com/akiomik/nosvelte/pull/162) checks an event's supplied ID against the canonical hash of its fields before verifying the signature. The Svelte library's default verifier previously accepted correctly signed fields carrying a substituted ID, allowing content to occupy another event identity and interfere with replacement handling. The merged change applies to version-one request and send paths using the default verifier; it does not certify the legacy export or custom verifiers under [NIP-01's event format](/en/topics/nip-01/). A later [request-filter repair](https://github.com/akiomik/nosvelte/pull/171) checks and copies relay event fields before matching them. Malformed data can no longer end the default provider's subscription or discard its next valid event. Caller-supplied engine clients can retain earlier dependency matching behavior.

### nostter

nostter [restricts externally supplied relay hints](https://github.com/SnowCait/nostter/pull/2684) to secure WebSocket URLs, rejecting local hostnames and non-global IP addresses. Account-selected local relays and remote-signer URLs retain their existing paths; DNS rebinding remains outside the check. The web client also [reads experimental separated content-warning payloads](https://github.com/SnowCait/nostter/pull/2680) only after the reader presses Show, checking the referenced event ID, matching author and a `k` tag matching the original event kind. Reactions and replies target the original event. These merged changes leave its current [NIP-36](/en/topics/nip-36/) publishing format unchanged.

### Coracle

[Coracle's list editor](https://github.com/coracle-social/coracle/pull/679) restores editing and deletion by waiting for asynchronous decoding before rendering the form. Previously, editing lost the list's fields and neither saving nor deletion published an event.

### Routstr Core

[Routstr Core’s current version 0.5.0 source](https://github.com/Routstr/routstr-core/releases/tag/v0.5.0) [stops logging autogenerated Nostr private keys](https://github.com/Routstr/routstr-core/pull/812) and [preserves the first-boot public identity](https://github.com/Routstr/routstr-core/pull/818). [Provider announcements](https://github.com/Routstr/routstr-core/pull/823) exclude localhost and literal private or link-local HTTP addresses; hostnames are not resolved for this check. The current tag includes work merged after its recorded October 7 publication date, so historical binaries and deployments remain unverified. Previously exposed logs still require operator review.

### Alby Hub

[Alby Hub's invoice-authorization change](https://github.com/getAlby/hub/pull/2629) limits settlement and cancellation to invoices created by the requesting app. The self-hosted wallet exposes app connections through [NIP-47, Nostr Wallet Connect](/en/topics/nip-47/); a connection's ability to manage its invoices must not grant authority over another app's invoices. A separate [isolated-connection privacy fix](https://github.com/getAlby/hub/pull/2621) removes the principal wallet's Lightning address from browser success paths for isolated connections.

### nak

[nak's merged relay command](https://github.com/fiatjaf/nak/pull/222) probes connection, read and write timings and relay information, then prints unsigned kind 30166 discovery events. Piping those results into `nak event` supplies signing and publication, making scheduled [NIP-66 relay monitoring](/en/topics/nip-66/) possible with the same terminal tool. Observed authentication or restriction responses override advertised relay information. Write probes use an ephemeral event signed by a throwaway key; kind 10166 monitor announcements remain a separate operation.

### Kehto

[Kehto's manifest verification](https://github.com/kehto/web/pull/277) checks current single-artifact signed manifests and artifact bytes before execution, with legacy parsing kept separate. The napplet shell also [verifies recommended handlers](https://github.com/kehto/web/pull/294), asks users about conflicts with saved choices and consumes an accepted invocation URL to prevent repeated delivery. Manifest verification checks publisher identity and artifact bytes; it does not establish that the application code is safe. [Gamepad snapshots](https://github.com/kehto/web/pull/297) now follow focus and visibility. Paja/playground frames block direct native gamepad, HID and USB access before application code runs, leaving mediated access to the host. Consumers need the corresponding host packages; shell readiness is a separate capability. A later [Paja admission change](https://github.com/kehto/web/pull/305) warns about unavailable experimental required domains but permits loading; those domains still expose no APIs or grants.

### napplet SDK

[The napplet SDK implements URI-based invocation and retained delivery](https://github.com/napplet/web/pull/228). [Publishing metadata survives in standalone HTML](https://github.com/napplet/web/pull/226), and [optional application references](https://github.com/napplet/web/pull/239) connect manifests to signed listings and screenshots without changing artifact hashes. The application-reference format remains a proposal. Reference-shell tests leave production discovery, installation and signature verification to hosts.

### rust-nostr

The Rust Nostr library [rust-nostr preserves partial download progress alongside terminal relay errors](https://github.com/nostrdevkit/nostr/pull/1483). The failed relay remains in the failed set, so callers can use events already received without losing the evidence that synchronization stopped early.

### Pensieve

[Pensieve's reconciliation safety fix](https://github.com/andotherstuff/pensieve/pull/92) follows its [missing-event exclusion work](https://github.com/andotherstuff/pensieve/pull/90). The relay and archive tooling re-requests exact missing IDs before classifying failures, preventing capped query tails from becoming false exclusions. Pause accounting is per job, and already-archived events are handled separately. A completed job can retain explicit missing-event records; completion alone does not establish a complete archive.

[Continuous Premium Primal reconciliation](https://github.com/andotherstuff/pensieve/pull/84) was enabled October 12. The operator's [deployment record](https://github.com/andotherstuff/pensieve/pull/93) reports both repaired binaries deployed and failure-based pausing enabled October 13. Later [exclusion carry-forward](https://github.com/andotherstuff/pensieve/pull/95) reuses only original proven exclusions for the same relay and overlapping window, excluding chained carries and newly mixed IDs; its [deployment was recorded that afternoon](https://github.com/andotherstuff/pensieve/pull/97). The [archive preflight and cache-stall repair](https://github.com/andotherstuff/pensieve/pull/98) was [deployed October 14](https://github.com/andotherstuff/pensieve/pull/99). A later [carry-priority fix](https://github.com/andotherstuff/pensieve/pull/103) is merged but not yet deployed in its source record.

### njump

The Nostr web viewer [njump restores embedded relay defaults](https://github.com/fiatjaf/njump/pull/173) when no override file is supplied. It also [isolates concurrent Markdown renderers](https://github.com/fiatjaf/njump/pull/171) and [response headers during timeouts](https://github.com/fiatjaf/njump/pull/169), fixing races that could crash the process while rendering quoted long-form events or serving concurrent requests. These are merged server changes; live deployment remains unverified.

### Nostr Components

[Nostr Components' zap-signing repair](https://github.com/saiy2k/nostr-components/pull/187) stops the payment flow when the selected signer refuses. The embeddable social widgets no longer substitute a random anonymous identity after rejection. Their [receipt aggregation](https://github.com/saiy2k/nostr-components/pull/197) validates [NIP-57 zap receipts](/en/topics/nip-57/) before deduplicating relay copies, invoices and request IDs.

### rx-nostr

The reactive client library [rx-nostr's version-four verification changes](https://github.com/penpenpng/rx-nostr/pull/207) check canonical event structure, IDs and signatures consistently across JavaScript and WebAssembly. An empty request condition list matches nothing and completes; legacy sending reports failure when it has no destination. Publication observers cannot change settlement, and disposed request descendants cannot restart. [Finite query segments](https://github.com/penpenpng/rx-nostr/pull/213) allow backward queries to complete after all supplied segments finish. These changes are included in [4.0.0 beta 2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%404.0.0-beta.2), a prerelease with breaking API changes.

### eHagaki

The social client [eHagaki adds staged outbox delivery](https://github.com/Lokuyow/ehagaki/pull/268), freezing author relay targets before signing. Its sensitive-post flow sends each relay the payload before its referencing structure, using that relay's own acknowledgement; payload-only success retains the composer. A [full post-history scan](https://github.com/Lokuyow/ehagaki/pull/312) saves verified results incrementally. Ambiguous ranges remain unconfirmed even when the scan is displayed as completed, with an explanatory information control. [Citrine local-relay support](https://github.com/Lokuyow/ehagaki/pull/315) preserves verified browsing ranges and archives exact signed events after successful external publication. Local acknowledgements do not turn a failed external send into success, and this adds no offline publishing queue. [Uploaded-media management](https://github.com/Lokuyow/ehagaki/pull/321) lists and deletes uploaded images and videos on supported NIP-96 and Blossom servers. A [later database migration](https://github.com/Lokuyow/ehagaki/pull/325) resets cached display and post history while retaining drafts and deletion requests. It also prevents older queued sync results from repopulating history after a clear.

### Formstr

[Formstr's submission-result fix](https://github.com/formstr-hq/nostr-forms/pull/508) rejects a form response when no relay accepts it. The Nostr forms application shows relay outcomes and offers retry while preserving filled answers. Webhooks and confirmation pages wait for acceptance, and the SDK receives the same check. A relay acknowledgement still differs from guaranteed long-term storage, but total publication failure no longer produces a success message.

### Auditable Voting

[Auditable Voting adds optional private-worker ballot batching](https://github.com/tidley/auditable-voting/pull/35). Organiser-signed definitions select a worker identity, DM relays and release threshold or deadline. Voters send [NIP-17 gift-wrapped ballots](/en/topics/nip-17/) and authenticate receipts against that worker; delegations must authorise both queueing and release. Released ballots use the worker's identity. The worker can read submissions, and deadline batches can be small. If no valid private route resolves, the inspected client falls back to public submission. This is merged development work.

### MintRadar

[MintRadar adds opt-in gift-wrapped alerts](https://github.com/hroomnik007/MintRadar/pull/122) for mint or melt problems, outdated software and lost support for those operations. Its Cashu mint directory [connects watchlist controls](https://github.com/hroomnik007/MintRadar/pull/123) to those notification settings and confirms them after the server responds. Atomic claims prevent overlapping probes from sending the same alert, and unsuccessful relay publication releases the claim for retry. [NIP-17 private messages](/en/topics/nip-17/) protect the notification contents; relay acceptance leaves recipient reading unconfirmed.

### Nostr Docs

[Nostr Docs' local-relay migration](https://github.com/formstr-hq/nostr-docs/pull/65) routes the collaborative Markdown editor's reads and writes through a Web Worker with an IndexedDB event cache and retry outbox. Document titles and tags survive reloads, and successive metadata edits receive increasing timestamps so two edits in one second remain distinct. Existing encryption-key storage stays intact. The network-pool fallback lacks worker outbox durability, and accepting a queued publication does not establish relay acceptance.

### Pakstr

[Pakstr's native local signer](https://git.nostrdev.com/stuff/pakstr/pulls/105) lets its Android application shell create a Nostr account on the device. The key stays in the native layer, encrypted with an Android Keystore-protected wrapping key. Signing results are verified before returning to the web application. The shell supports [NIP-07 browser signing](/en/topics/nip-07/) and encrypted requests. Signer selection opens lazily when needed and coordinates concurrent requests.

### Nostr WoT SDK

The web-of-trust library [Nostr WoT SDK extends authentication consent](https://github.com/nostr-wot/nostr-wot-sdk/pull/15) to typed native and remote requesters. Stored denials are checked before prompts, and reusable consent is bound to the requesting transport and destination. Web requests remain one-shot by default. Its [managed Blossom uploads](https://github.com/nostr-wot/nostr-wot-sdk/pull/13) validate immutable bytes, support cancellation and stop when the active session changes, with server-bound authentication and redirect restrictions.

### NosTube

[NosTube v0.2.49](https://github.com/flox1an/nostube/releases/tag/v0.2.49) supplies desktop installers. Separately, merged server work [adds durable scheduled publication](https://github.com/flox1an/nostube/pull/126). Events are signed before their due time, stored in SQLite and published by a worker that catches up after downtime. Its [editing and deletion flow](https://github.com/flox1an/nostube/pull/124) tracks tombstones, mirror delivery and owned-file cleanup. [First-run setup](https://github.com/flox1an/nostube/pull/134) distinguishes a user's browser signer from a server-managed channel key. Historical unowned blobs remain outside automatic cleanup.

### diVine

[diVine 1.0.24](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.24) adds private clip collaboration with credits and checks of signed capture or edit provenance. Viewer-selected translated captions fall back to the originals while translation is pending or unverified. These provenance checks do not guarantee an unedited recording.

The short-video client's [routing changes](https://github.com/divinevideo/divine-mobile/pull/9884) consult recipients' inbox relays for text and video chat messages and preserve uncertain delivery outcomes. [Sender-copy handling](https://github.com/divinevideo/divine-mobile/pull/10006) lets users' own group messages appear on their other devices; previously discarded copies require reimporting the account. [Cancelled partial group sends](https://github.com/divinevideo/divine-mobile/pull/10031) retain “Not sent to everyone” records; cancellation is terminal and those records cannot retry. Group creation and recognition of new peer-started rooms remain [behind an off-by-default flag](https://github.com/divinevideo/divine-mobile/pull/10020).

Subsequent main-branch changes [keep interrupted database-restore copies outside the temporary cache](https://github.com/divinevideo/divine-mobile/pull/10118) and [preserve scheduled posts, queued reports, profile edits and removed-chat records during rebuilding](https://github.com/divinevideo/divine-mobile/pull/10115). [Send deadlines include relay reconnection](https://github.com/divinevideo/divine-mobile/pull/10127), reducing the abandoned-send retry threshold from 160 to 137 seconds. [Indexer inbox lookups use a separate bounded pool](https://github.com/divinevideo/divine-mobile/pull/10116) to avoid waiting behind feed reads, and [follow controls preserve the chosen action](https://github.com/divinevideo/divine-mobile/pull/10147) if the contact list changes before confirmation. These later merges leave less time for relay acknowledgement during slow reconnects; database repairs cannot restore previously lost data. Later [opt-in recording copies](https://github.com/divinevideo/divine-mobile/pull/10110) let Android and iOS gallery backup preserve newly recorded clips. Copies without signed provenance are warned and cannot be reimported; this is off by default and needs additional storage.

### Conduit

The commerce applications in [Conduit gain a shared durable inbox](https://github.com/Conduit-BTC/conduit-mono/pull/616), retaining encrypted message delivery and recovery across Market and Merchant. Recipient-relay acceptance survives a failed sender self-copy, with recovery reusing the same bytes to avoid a second semantic send. [Shared signer-backed wallets](https://github.com/Conduit-BTC/conduit-mono/pull/635) connect both applications. That recovery path trusts the signer with recovery plaintext; source integration alone establishes neither a live deployment nor funded acceptance testing. [Independent relay grants](https://github.com/Conduit-BTC/conduit-mono/pull/645) survive when several account routes share a URL. Disabling one route no longer erases another signed relay-list or inbox grant, and authentication-required or incomplete reads retain an unavailable outcome. The [merged payment router](https://github.com/Conduit-BTC/conduit-mono/pull/613) splits one buyer-approved funding payment into merchant and supplier Lightning payouts, then the Conduit fee, with exact-intent reconciliation and encrypted recovery through the shared Nostr inbox. Production and staging execution remain disabled; provider completion does not prove receiver claim or payment retirement.

### Bitcredit

[Bitcredit's persistence encryption](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1041) protects its electronic-bill application's identity, company and bill keys, including the Nostr resend queue, using the personal identity's mnemonic. Initialization requires a matching mnemonic. [Instance management](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1043) lets testnet and mainnet instances keep their background Nostr subscriptions running independently on one device.

## New Projects

### Submarine

[Submarine 0.1.0](https://github.com/nogringo/submarine/releases/tag/v0.1.0) releases a password manager whose encrypted vaults sync over Nostr. It supports external signers and retains concurrent item versions, with Bitwarden JSON import and export. Changes are saved locally before waiting for relay acceptance. Android, desktop and CLI downloads accompany the release. The project calls it young and advises a proven manager for critical passwords; the tagged protocol specification is still empty. Its [web storage](https://github.com/nogringo/submarine/blob/v0.1.0/apps/app/README.md) keeps the encryption key alongside the protected data.

### cl-marmot

[cl-marmot](https://github.com/modus-lisp/cl-marmot/blob/5dd9dea97ece82b0e4cc08f0c893397fbb333a5b/README.md) adds a Common Lisp implementation of MLS group chat over Nostr. October 9 code adds competing-commit convergence and encrypted Blossom attachments, with author-reported interoperability tests against MDK’s wn command-line client. The implementation is unaudited, and account keys and message logs lack encryption at rest. Timed convergence windows, replay beyond the rollback horizon and disbanding remain unimplemented; the inspected harness uses disposable local relays.

### nalgorithm Android

[nalgorithm's Android release](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.0) builds a preference-ranked Nostr feed and a background audio digest that can be played offline. Users choose hosted, Lightning-priced inference or own-key inference requested from the phone; these are separate routes. Login supports Amber through remote signing. Follow-up releases [repair own-key ranking and follow-list discovery](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.1), then [preserve likes from working relays when another relay fails](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.2) and improve digest recovery. [Version 1.0.3](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.3) reorders model setup and reports missing connection-test inputs.

## Protocol and Spec Work

### Authenticated napplet endpoints

In the NAP specifications for napplet applications, [NAP-INC endpoint identifiers](https://github.com/napplet/naps/pull/104), merged October 9, replace bare handler names with authenticated identifiers. Equal names from different publishers no longer identify the same peer. The runtime still mediates communication, and root or snapshot manifests need no named `d` coordinate.

### Handler recommendations in invocation links

[The invocation-link recommendation](https://github.com/napplet/naps/pull/99), also merged October 9, allows an optional `#naddr` handler recommendation. A shell can offer discovery and installation, with ordinary resolution as a fallback. Saved preferences and shell policy take precedence. A recommended handler therefore supplies a discovery hint without replacing the user's existing choice or transferring installation authority to the link's sender.

### Delivery acceptance and application work

[The intent advertisement and delivery changes](https://github.com/napplet/naps/pull/91) derive roles and intents from the same verified manifest, using publisher-safe identifiers. Delivery acceptance no longer depends on the source application staying alive. An `ok: true` response accepts responsibility for delivery; it does not mean the destination's application work has finished. Retry and restart behavior remains runtime policy under this merged specification change.

### Cyberspace action chains

[Cyberspace's revised chain rules](https://github.com/arkin0x/cyberspace/pull/48) make a fork invalidate a signed action chain from its spawn and require clients to confirm the live head before signing another action. The Nostr-backed world adds [140 signed synthetic chains](https://github.com/arkin0x/cyberspace/pull/49) with normative verdicts for implementations. [Copy-credit rules](https://github.com/arkin0x/cyberspace/pull/47) use `q` references to the original object and notify its author for public remixes; sealed copies omit that notification. These are merged project specifications, with deployed verifier coverage unverified.

### Relay persistence acknowledgements

[The open persistence proposal](https://github.com/nostr-protocol/nips/pull/2496) introduces persisted acknowledgements, PROOF queries and optional signed kind 1797 relay attestations. A signature makes a storage claim attributable to a relay; it does not prove continued retention. Queries also disclose which events interest the client.

### Shared pins for Marmot groups

[Marmot's open pinning proposal](https://github.com/marmot-protocol/marmot/pull/434) defines authenticated shared state for up to 64 message references, with member and administrator permissions. Effective changes require an MLS Commit and epoch transition, and every resulting member leaf must support the feature. Pins do not copy message bodies or extend retention, so unavailable targets remain unresolved. The supplied fixtures assume authenticated state; they do not demonstrate cryptographic processing or convergence across clients.

## NIP Deep Dive: NIP-36 and NIP-38

### Content warnings before display

[NIP-36, sensitive content](/en/topics/nip-36/), lets authors add a `content-warning` tag to an event, optionally including a reason. A client may hide the content until the reader chooses to reveal it. The [specification](https://github.com/nostr-protocol/nips/blob/master/36.md) leaves the interface to clients and permits supplemental label tags. Adding a warning does not change who can read the event. In a public post, relays and other clients still receive its content.

[Amethyst's warning-tag parser](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) recognizes the tag and treats a missing or blank reason as unspecified. [Coracle's composer](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/views/NoteCreate.svelte) writes the reason into the tag; its [content view](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) respects the reader's sensitive-content setting and offers a reveal action. [noStrudel's note view](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) applies its own warning preference and expanded state before showing the warning interface.

[NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md) does not encrypt events or require concealment. An absent warning says nothing about the content; clients decide how warnings affect previews and reveal controls.

### Profile status and expiration

[NIP-38, user statuses](/en/topics/nip-38/), uses addressable kind 30315 events. The author, kind and `d` tag identify a status coordinate; `general` and `music` have defined meanings. A newer event replaces the previous status at that coordinate, while a different `d` value remains separate. Empty content clears a status. The [specification](https://github.com/nostr-protocol/nips/blob/master/38.md) also permits references to URLs, profiles, events and addresses.

This signed [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) event shows an expired general status. The author's original spelling is preserved.

```json
{
  "kind": 30315,
  "id": "8848719ae347e705afbbdbfa3a9f5dcca5dd31c4f39182503bf84de5e362bcf4",
  "pubkey": "f13fdeecd852acebaa77dbc18806a051eaa7ea2214c157a3495982d7535a77f3",
  "created_at": 1791983702,
  "tags": [
    [
      "d",
      "general"
    ],
    [
      "expiration",
      "1791984600"
    ]
  ],
  "content": "I'm listening 📩 on 3 ralys",
  "sig": "b5c98a578773f0199cb833d4b916aac115f2b13474a61e81fdca7316b848d397d7d8ad86d299abee4721f404b7b8a1af26e8c53143457ad14d2fb933b21daf85"
}
```

[Damus's status model](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/damus/Features/Status/Models/UserStatus.swift) handles general and music statuses with expiration. [Nostria's status service](https://github.com/nostria-app/nostria/blob/e861946f4ef4e70f3ec49997a4be27615b9b6f5e/src/app/services/user-status.service.ts) ignores empty or expired values and publishes music statuses using track duration; its normal subscriptions request only general and music types. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip38UserStatus/UserStatusEvent.kt) preserves the `d` identifier when clearing a status. Custom types therefore need agreement beyond the shared wire structure.

Statuses are public author statements. They do not prove online presence or that somebody listened to a track. Publishing music or availability can disclose habits, and optional expiration limits stale display without promising deletion. [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) remains a draft, optional specification, as does NIP-36. Clients can implement either independently, with their display settings determining what readers see.
