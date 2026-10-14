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

writer_model: direct-codex

GATE: PASS (source-owner content review; full publication receipts are separate)
