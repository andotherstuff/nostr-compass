## Tagged Releases

### Nostr WoT

Signing policies now apply global rules, site/account overrides and exact-origin defaults for [NIP-98 HTTP authentication](/en/topics/nip-98/), with denials taking precedence and money requests reviewed individually in the [extension release](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.10). Nostr WoT's trust and signing tools also gain a [published bunker responder](https://registry.npmjs.org/@nostr-wot%2fbunker/0.2.0) for [NIP-46 remote signing](/en/topics/nip-46/), with verified replay bounds and authenticated pairing state. Hosts still own approvals, key storage and durable revocation state.

[Account Archive](https://github.com/nostr-wot/nostr-wot-extension/pull/39) in [v0.8.11](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.11) synchronizes original signed events across relays with checkpoints and encrypted local storage. [Version 0.8.12](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.12) makes exported archive files passwordless while checking signatures and account ownership on import; older encrypted exports remain supported. Exported files and encrypted local storage have different privacy boundaries.

### Scramble

Still-sealed messages arriving ahead of the current group epoch now survive restarts and replay when the epoch advances in [Scramble v0.7.9](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.9). The group messenger also binds KeyPackage identifiers before relay exposure. Recovery is bounded by a 256-envelope cap per group and a retention window.

### Sonar

Active conversations gain [chat catchup](https://github.com/hedwig-corp/bitchat-to-sonar/pull/649), while [queue isolation and bounded push-token sharing](https://github.com/hedwig-corp/bitchat-to-sonar/pull/657) improve how Sonar, a chat application, handles background work. These changes ship in [v0.1-alpha.15.4](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.15.4); relay caps and queue overflow still limit catchup.

### Chama

Creator checks now compare the full creator identity when known, discard provisional link claims after failed loads and refuse ambiguous fresh legacy links in [Chama v6.4.20](https://github.com/jesuspirate/chama/releases/tag/v6.4.20). The Nostr peer-to-peer escrow client also [waits for relay acknowledgement before on-chain locking](https://github.com/jesuspirate/chama/releases/tag/v6.4.19). Cold-start wakes after swiping the app away have regressed in v6.4.20.

### Mostro

Funded hold invoices are protected from cancellation, failed lookups are deferred and bonds are paid exactly in [Mostro v0.19.1](https://github.com/MostroP2P/mostro/releases/tag/v0.19.1), the peer-to-peer trading daemon. Core progress adds [weighted imported reputation](https://github.com/MostroP2P/mostro-core/pull/177) and [signed reputation validation](https://github.com/MostroP2P/mostro-core/pull/181), with issuer trust left to callers. Unreleased main-branch work adds [Cashu ecash discovery and order creation](https://github.com/MostroP2P/mostro/pull/1045) plus [taking orders and locking escrow](https://github.com/MostroP2P/mostro/pull/1047); release, cancellation and dispute operations remain rejected. Additional unreleased main-branch [payer declarations](https://github.com/MostroP2P/mostro/commit/bd6a723248e60dfa8b4657e4c50c38b489ab96ec) let buyers exchange a fiat-account hash bound to the current trade. It is disabled by default and unavailable in Cashu mode; guessable account hashes do not prove identity.

Main-branch [Mostro core user-info messages](https://github.com/MostroP2P/mostro-core/pull/185) add a restore-only request and reply for a user's own reputation, including rating, review count, operating days and first-trade date. Daemon identity-proof and lookup integration remain separate.

### Earthly

Map, Story and Atlas authoring now share [native Chrome WebMCP browser-agent operations](https://github.com/zeSchlausKwab/earthly/pull/31), with [confirmation tied to the exact preview and account revision](https://github.com/zeSchlausKwab/earthly/pull/33). Earthly, a map-based publishing tool, adds [signed-byte recovery and explicit draft-preserving rebase](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.15). Chrome support remains experimental, and later observation of a publication is distinct from an acknowledgement whose outcome was unknown.

### nostream

Multiple tag constraints and per-filter limits now produce correct query results through the [filter-query repair](https://github.com/cameri/nostream/pull/792) included in nostream v3.2.0. The Nostr relay's [release](https://github.com/cameri/nostream/releases/tag/v3.2.0) also includes optional HAProxy/readiness support and Redis fanout. Existing sockets do not migrate during cutover, and Redis unavailability can drop fanout messages.

### Grain

Event serialization and replacement preflight checks improve in [Grain v0.8.0](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0), a Nostr relay. Malformed subscription and count constraints now fail without widening queries, while newly tracked late backfills use receipt time for purging. Replacement preflight is not a durable commit: deletion can still precede asynchronous ingestion, leaving a write gap.

### Ditto

Ditto, a Nostr social client, adds file posts and a tap-to-load 3D attachment viewer in [v2.43.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.43.0), with 200 MiB download limits. [v2.44.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.44.0) adds [event-native 3D objects](https://gitlab.com/soapbox-pub/ditto/-/commit/2be9431f9c89a84c94c250430fe34fcff6fd1641), customizable Blobbi rooms and addressable videos, plus NSFW and blocked-term filtering in public feeds and search. Release notes also report interrupted-wallet repairs and add Lightning-address fallback for failed Lightning URLs. Zap invoice amounts must match, but description-hash mismatches only warn: automatic payment can proceed with unverified sender or post binding. [v2.44.1](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.44.1) reads notifications from account-declared inbox relays with per-relay paging, retrieves own saved lists from write relays and repairs WebLN payment-provider handling. List edits use the latest observed event; withheld or stale relay copies remain a limit. Separate relay-source [mention parsing](https://gitlab.com/soapbox-pub/ditto-relay/-/commit/8a4537a86a3f662cd30debd50fa2a3d5a23ab1c6) continues past truncated references.

### Nostr Double Ratchet journals received controls

Private control messages now share a durable journal row with advanced receiver state in [the TypeScript v0.0.176 release](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.176). The encrypted messaging library retains them until the application's durable acknowledgement, enabling replay after failure or restart. Callbacks must be idempotent and validate authorized siblings; newly ratcheted AppKeys labels do not retroactively protect older records.

### nostr-social-graph

Private-contact edits now persist before notification, with owner-bound controls, fieldwise clocks and exact pending acknowledgements in [nostr-social-graph v2.0.3](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.3). The social-graph library retains rejected handoffs for bounded retries. Callers must provide authenticated, durable sibling transport; a ready status means acceptance into an outbox, not delivery to every device.

### nostr-pubsub

Ordinary subscriptions start immediately, followed by optional bounded [NIP-77 inventory reconciliation](/en/topics/nip-77/) in [nostr-pubsub TypeScript v0.5.14](https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.14). The subscription library fetches missing event IDs over the existing relay socket and verifies events through the normal admission path. Reconciliation does not upload local-only events or change history-completion semantics.

The separate [Rust FIPS package v0.5.20](https://crates.io/api/v1/crates/nostr-pubsub-fips/0.5.20) [preserves pending replies and subscriptions](https://github.com/mmalmi/nostr-pubsub/commit/03dab368850b391b8874e42b19521311e3ebdfd7) when an inbound peer becomes a discovered outgoing peer, reusing its established stream. Physical-link changes and advertised service restarts still reset that stream.

### FIPS

Missing routed sessions can recover through authenticated discovery after a browser restart that retains identity in [FIPS runtime v0.0.53](https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.53). The Nostr-keyed transport bounds recovery attempts and checks for a usable route before signaling. Recovery completion can clear pending state only in its original node generation, preventing stale work from clearing a replacement node's state.

Later [TypeScript runtime v0.0.56](https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.56) restricts nonforwarding browser nodes to advertising their own identity and refreshes cached routing announcements after a fresh authenticated responder carrier. Wire formats, identity checks and session authentication remain unchanged.

Separate Rust source changes [adopt pending key sessions only after authentication](https://github.com/jmcorgan/fips/commit/06312d0c3a5410eb165703afc50a3c6793f25879), even when key-epoch bits match. [Failed decryptions no longer evict live peers](https://github.com/jmcorgan/fips/commit/a52b54b246baffde4d3e97cf3505ef36e601726c) using public receiver indices; authenticated liveness still determines expiry. [Session backoff](https://github.com/jmcorgan/fips/commit/c7fee893c6bf1ee93f55877f08ccb20b0083803f) temporarily refuses repeated silent sessions, while [BLE connection arbitration](https://github.com/jmcorgan/fips/commit/29c89c20374b9cd52989b3f1124802725c398968) addresses shared-connection races. [Rekey guards](https://github.com/jmcorgan/fips/commit/7dde5bf628e7c22f1a0a45c174655b44f804dbe6) reject copied setup messages and off-link attempts, [age and drain floors](https://github.com/jmcorgan/fips/commit/027c3ab3246c0f46be5af0808a7bcfa1567e0e5b) protect session transitions, and [bounded child-filter checks](https://github.com/jmcorgan/fips/commit/ba441c282186a085adcbcab1bf0f625d9e2ec98e) reject apparent echoes with threshold exemptions. These are development changes, with no new Rust release or device validation established.

### Elisym

Elisym, a merchant payment tool, adds [webhook signature and freshness verification](https://github.com/elisymlabs/elisym/pull/166) in [commerce 0.9.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.9.0), [merchant-node 0.9.1](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/merchant-node%400.9.1) and [MCP 0.32.1](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/mcp%400.32.1), an AI-tool interface using the Model Context Protocol. [Checkout changes](https://github.com/elisymlabs/elisym/pull/165) reset closed or reloaded modals while existing payments continue, checking unresolved payments before another wallet request. Those pages lose the order’s onPaid callback; signed backend webhooks remain authoritative. A [durable paid-order webhook outbox](https://github.com/elisymlabs/elisym/pull/155) queues signed retries alongside ledger changes. [Receipts travel over Nostr](https://github.com/elisymlabs/elisym/pull/161), but fulfilment and event-ID deduplication remain merchant-owned; payment completion does not confirm delivery.

### Hashtree

Remote blocks can retain peer-readable provenance after restart through [durable verified-block sharing](https://github.com/mmalmi/hashtree/commit/94918ff549c9c1b716fdd899d2bcccf689bc3128), included in [Hashtree runtime v0.5.19](https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.19). The content-addressed sharing runtime persists hash-verified bytes and authorization before returning. A full or unavailable cache still permits a valid download, but durable sharing cannot be promised for that read.

Later Rust source adds [automatic, bounded peer archive intake](https://github.com/mmalmi/hashtree/commit/6eafa7049e1e78e38391342c2baa7d2061f29e92) alongside relay catchup, using an ephemeral identity and verified events. Peer observations cannot satisfy missing required relay coverage. [Interrupted appends resume](https://github.com/mmalmi/hashtree/commit/849dd9e03a616b0df56c86026545a86d49a9de74) only from matching durable input; author coverage advances after the whole author is durable.

A [standalone Git reader](https://github.com/mmalmi/hashtree/commit/78c4d2f504ff0a5cd956e750203a35ec0e28e877) combines bounded relay observations with public signed index roots while preserving original signatures. Unreachable sources remain distinct from absent repositories. An [explicit expected release root](https://github.com/mmalmi/hashtree/commit/5d2d81c92881aa9934c8c39df9220c7a341bcec0) preserves existing history or stops on conflict; it does not guarantee concurrent publication safety.

### Amethyst

[Amethyst v1.17.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.17.0), an Android Nostr client, includes [document-bound browser signing](https://github.com/vitorpamplona/amethyst/pull/4260) through [NIP-07 browser signing](/en/topics/nip-07/) and [profile updates](https://github.com/vitorpamplona/amethyst/pull/4320). Departed-document messages are discarded; Tor-required pages fail closed on proxy failure, but WebView proxy settings affect other views process-wide. Later merged [QR safety changes](https://github.com/vitorpamplona/amethyst/pull/4359) require confirmation before opening an ambiguous 64-character hex scan as a public profile, avoiding automatic transmission of possible private-key bytes to relays. [Software-release handling](https://github.com/vitorpamplona/amethyst/pull/4355) trusts app branding and downloads only from its publisher or a declared maintainer, and separates stable versions from prereleases.

Later development [limits browser signing prompts](https://github.com/vitorpamplona/amethyst/pull/4352) to 120 seconds and always asks before signing reports. [Encrypted-message history](https://github.com/vitorpamplona/amethyst/pull/4338) now pages only the visible account, prioritizes its DM relay list and offers bounded searches with retry controls. [Relay-hint and search repairs](https://github.com/vitorpamplona/amethyst/pull/4335) reject malformed relay URLs, stop indexing encrypted emoji-pack contents and stop linking anonymous or private zap sender keys; expanded public-text search requires existing stores to be reindexed. The [amy command-line client](https://github.com/vitorpamplona/amethyst/pull/4342) adds posting, threads and deletion while restricting group content to its host relay and refusing group reposts or quotes. The Android app’s own group-repost path remains unchanged. [Paired clients](https://github.com/vitorpamplona/amethyst/commit/9d78ecb0642a3271a2ce5eb386f91e5ef753995c) using [NIP-46, Nostr's remote-signing protocol](/en/topics/nip-46/) bypass the unpaired-client rate limiter; unpaired traffic remains limited to 10 requests per author and 100 combined per minute. Queue and concurrency bounds and per-request authorization remain.

### My Signet

Per-app phone approval is available, default off, in [My Signet v0.18.2](https://github.com/forgesworn/signet-app/releases/tag/v0.18.2), a hardware-signer companion. It requires an imported Heartwood hardware-signer operator key, compatible firmware and a connected, unlocked inbox. Possession of that phone key authorizes enabled requests without touching hardware; "Approve once" can permit the same event kind for ten minutes, while wallet pairing and login codes still require the hardware button.

### Nsync

Signed Nostr address announcements now help paired devices find each other in [Nsync v0.3.0](https://github.com/alanbimbati/Nsync/releases/tag/v0.3.0), a Syncthing-based file synchronizer. Pairing binds each Nostr identity to a Syncthing device ID, and receivers require newer announcements. Files still transfer through Syncthing; relay announcements expose address and online-timing metadata, even with public-IP announcement disabled.

### PsstPsst

[PsstPsst v26.10.1](https://github.com/CodyTseng/psstpsst/releases/tag/v26.10.1) adds small private groups for text, reactions and files through [PsstPsst's group-send implementation](https://github.com/CodyTseng/psstpsst/blob/9da073ad10ad786799e27f4735852b0e2f519814/src/lib/nostr/group-messaging.ts). The messenger extends [NIP-17 private messaging](/en/topics/nip-17/) and [NIP-59 gift wrapping](/en/topics/nip-59/) with encrypted group identifiers and membership actions, using per-recipient [NIP-44 encryption](/en/topics/nip-44/). These extensions remain draft and optional: other clients may split rooms, and any current member can publish membership changes.

### Write Nostr

Encrypted draft and account-settings sync arrives in [Write Nostr's v0.4.11 changes](https://github.com/imattau/write_nostr/compare/v0.4.4...v0.4.11). The writing client commits a draft revision only after every chunk and its head record reach at least one common accepting relay, preserving local content on incomplete or invalid recovery. Signers without NIP-44 support retain local drafts but cannot use encrypted sync.

### Flotilla

Screen sharing joins existing calls through [Flotilla's cross-platform sharing implementation](https://gitea.coracle.social/api/v1/repos/coracle/flotilla/git/commits/e6d4e18f0b68111077a1eba3457661fbc27eabda), released in [Flotilla 1.12.0](https://gitea.coracle.social/coracle/flotilla/releases/tag/1.12.0). The community chat client provides web, Electron and native adapters, including Android MediaProjection and an iOS broadcast-extension path. The release also preserves drafts when sending fails, allowing users to retry without rewriting their message.

### Blitz Wallet

Native Android background handling for [NIP-47 wallet requests](/en/topics/nip-47/) arrives in the [Blitz Wallet Android prerelease](https://github.com/BlitzWallet/BlitzWallet/releases/tag/Android-v0.7.16-pre3). The Lightning wallet shares SQL-backed budget reservations, payment-hash claims and uncertain-payment markers with JavaScript handling, alongside startup fallback and background crash containment. Firebase Cloud Messaging is required, and Android may still need JavaScript execution or an open app.

### Sidecar

Selected web text can be published as [NIP-84 highlights](/en/topics/nip-84/) in [Sidecar v1.15.6](https://github.com/dmnyc/sidecar/releases/tag/v1.15.6). The browser extension's [v1.15.8 composer changes](https://github.com/dmnyc/sidecar/releases/tag/v1.15.8) align mention and quote tags, convert pasted identifiers and skip unanswered relays after 12 seconds, so delivery can remain partial. The [server-discovery repair](https://github.com/dmnyc/sidecar/pull/478) in [v1.15.9](https://github.com/dmnyc/sidecar/releases/tag/v1.15.9) finds Blossom servers through account-declared relays, including write-only relays, and retries failed discovery on the next upload. The same fix covers profile images; nostr.build remains the fallback.

### BuhoGO

BuhoGO, a Bitcoin wallet, releases [1.10.0](https://zapstore.dev/apps/mybuho.buhogo). [Purchased NIP-05 identity names](/en/topics/nip-05/) now survive restarts and delayed relay replies through [durable profile synchronization](https://github.com/Buho-Ecosystem/Buho_go/pull/323). Activation continues after checkout closes, and verified recovery requires no second payment; newer username choices remain authoritative. Android installations older than 1.9.1 use another signing key: back up recovery phrases before uninstalling and reinstalling.

### Staircase

Staircase, an MLS group-chat client over Nostr, releases [0.1.20](https://zapstore.dev/apps/tools.relay.staircase). Its [forwarding and synchronization changes](https://code.relay.tools/opensauce/staircase/-/compare/v0.1.19...v0.1.20) re-encrypt forwarded attachments; captions default off, with no original author, chat or reply metadata. Folders stay local unless multi-device sync encrypts them under derived keys. Search excludes deleted messages and covers device-held history. New accounts use cordn.feeds.relay.tools; existing coordinators remain. Startup key-package reconciliation survives leaving onboarding.

### KithMoot

KithMoot, an encrypted room messenger over Nostr, releases [0.6.62](https://zapstore.dev/apps/dev.forgesworn.kithmoot). [Queued messages](https://github.com/forgesworn/kithmoot-android/pull/177) retry oldest first using their original signed events. Never-sent messages remain editable or deletable; possibly delivered messages can only leave the local pending list. [Saved-room synchronization](https://github.com/forgesworn/kithmoot-android/pull/175) republishes missing relay records using their original signed events, preserving deletion records.

Later merged [0.6.63 preparation](https://github.com/forgesworn/kithmoot-android/pull/195) adds [VMLS rooms on user-operated Bothy servers](https://github.com/forgesworn/kithmoot-android/pull/189), with Nostr invitations and signer-authorized access grants. This preview has no persistent VMLS message history. [Compromised-device removal](https://github.com/forgesworn/kithmoot-android/pull/194) holds new sends and joins until witnessed, revokes keeper-owned grants without grace, and retries unconfirmed revocations; existing traffic may arrive first. Tor-only rooms pause server traffic. Signing, publication and handset acceptance remain pending; downgrades discard removal journals and compromise marks.

Rooms have no end by default; when one is chosen, [self-destruct defaults on](https://github.com/forgesworn/kithmoot-android/pull/192), with a read-only alternative. Cleanup runs with background ringing or delivery enabled, otherwise at next start. It requests deletion of this device's signed events and attempts local cleanup; failed stores, relays or recipients may retain copies. Without a reachable relay, cleanup retries while retaining its signing key.

### Nostr Vault

Nostr Vault, an Android client with an on-device relay, releases [2.7.2](https://zapstore.dev/apps/com.nostrvault.app) with marketplace listings, polls, article highlights and nostrconnect signer pairing. Release notes also report cross-device DM catchup and signature checks; [NIP-29 relay groups](/en/topics/nip-29/) are removed. These are publisher-reported release behaviors, without independent security or background-delivery validation.

### Private Provider

[Private Provider](https://zapstore.dev/apps/xyz.privateprovider) is an Android AI coding workspace that builds APKs on the phone and publishes Nostr repositories through ngit. [Version 0.7.2](https://njump.me/nevent1qqs0yvswv6w9yvz2vv02dgul5hyuppuu0vngcm9gj8lpa3jtem20llspz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzqnjky26htndmf4w76zf7frrge5lhynad23c59uxpkzhv9u4j5zewhq40ud) lets the in-app agent, Pi, request issues, comments and pull requests with explicit command approval and signatures from the Amber Android signer. [0.7.5](https://njump.me/nevent1qqsf6aufz2g20m6uyyqchc86uyhrda5xxw0xxyuw7t6q49ssahz2ksgpz3mhxue69uhhyetvv9ujumn8d96zuer9wcpzqnjky26htndmf4w76zf7frrge5lhynad23c59uxpkzhv9u4j5zew0fpk4h) pins Blossom and Zapstore publication targets in a committed manifest and rejects tag/commit mismatches. Wallet recovery remains unavailable; the documentation cautions users to keep only small balances.

### Haps v0.1.11: social-graph package discovery

[Haps v0.1.11](https://github.com/mmalmi/haps/releases/tag/v0.1.11), a Nostr-key package publisher and installer, adds signed immutable bootstrap discovery and publisher-maintained catalogs, preserving custom sources and publisher pins. Search and bare-name installs require a publisher or release voucher from the user's social graph, excluding muted or overmuted people. Explicit `npub/package` installs warn outside that graph; trusted warnings block installation. The installer [retains its verified selection](https://github.com/mmalmi/haps/commit/f8f999123465b1bb64bf41a1903746bf5fa64459). Signatures establish authorship, not safety: native programs and build recipes remain unsandboxed; package formats remain unstable.

### soyLI

soyLI [v0.25.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.25.0), a toolkit for publishing sandboxed Nostr apps, uses creators' own [NIP-34 Git repositories](/en/topics/nip-34/), checking signed refs and clone reachability again on resume. It avoids duplicate repositories and retains linked source on deletion. Remote dynamic backends still require soyLI-managed source. [Earlier changes](https://github.com/zeSchlausKwab/napplet-soy/commit/8f809650b2fe4d1fd4f6bf045159d28868a893ae) accept [NIP-22 replies](/en/topics/nip-22/) with extra mentions and prevent a relay-handshake timeout race from terminating the web process.

### fips2go

fips2go, an Android mesh client using Nostr-signed domain bindings, releases [0.9.4](https://github.com/fr34aky/fips2go/releases/tag/v0.9.4) and [0.9.5](https://github.com/fr34aky/fips2go/releases/tag/v0.9.5). [Fallback TTLs](https://github.com/fr34aky/fips-pub-domains/pull/21) [follow retries](https://github.com/fr34aky/fips2go/pull/74), initially 20 seconds, tripling to three hours. [Cached mesh answers](https://github.com/fr34aky/fips-pub-domains/pull/23) [avoid parallel DNS](https://github.com/fr34aky/fips2go/pull/79); ordinary fallback still queries upstreams. [First denials](https://github.com/fr34aky/fips-pub-domains/pull/22) release fallback while validation continues. Its resolver supports [configured offline witness quorums](https://github.com/fr34aky/fips-pub-domains/pull/12), [excluding self-vouching](https://github.com/fr34aky/fips-pub-domains/pull/17); pins and DNS retain precedence. Desktop operators may [disable plain probes](https://github.com/fr34aky/fips-pub-domains/pull/20) with DNSSEC; default probing remains enabled. Phone probing follows connectivity validation. Denials do not authenticate targets.

writer_model: actual=openai-codex/gpt-6.1-sol, receipt=/opt/data/task-artifacts/compass-direct-2026-10-07/writer-tagged_releases-cap6000/receipt.json; final root edits verified in assembled draft 4f46a95e8d1bad2c63d2e7b67b35c387bded0c07ac10b97c6ca12298922f354b

GATE: PENDING REVIEW
