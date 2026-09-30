# Compass #42 — selection review

The source pass and triage files fix the exact window. Each item below cleared direct primary evidence, material progress, a Nostr surface, and a distinct continuity delta. Scores use significance, user impact, novelty, evidence, and explanatory value (0–2 each). The month-end retrospective is the scheduled September synthesis and includes current 2026 changes.

## Holoboard adds Nostr promotion commands and an Android app — 9/10

Holoboard is a board for finding Nostr notes through a ranking that can be boosted with Lightning payments. The original posts remain Nostr events; Holoboard serves its ranking and appearance data through its own HTTP API. That distinction matters if a reader expects the board's ordering to be a relay-native feed.

Primary links: https://holoboard.space, https://github.com/ptrio42/holoboard.space/blob/main/CHANGELOG.md#2026-09-23, https://github.com/ptrio42/holoboard.space/blob/main/CHANGELOG.md, https://github.com/ptrio42/holoboard.space/blob/main/relay/README.md, https://zapstore.dev/apps/space.holoboard.app

## fips-pub-domains tests signed public names for a mesh — 9/10

fips-pub-domains is a new resolver and naming experiment that binds public domain names to nodes on FIPS, an encrypted mesh that uses Nostr messages for peer discovery. Its first release combines those claims with DNS TXT records, optional DNSSEC validation, locally pinned bindings, a Linux resolver daemon, and Android integration with fips2go, the FIPS client for phones. A sig

Primary links: https://github.com/fr34aky/fips-pub-domains, https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0, https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0, https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1, https://github.com/fr34aky/fips2go/pull/55, https://github.com/fr34aky/fips2go/pull/59, https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md, https://github.com/nostr-protocol/nips/pull/2487, https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md

## Marmot MDK 0.11.0 makes account history gaps visible — 9/10

Marmot MDK, the Rust runtime and generated bindings for MLS-encrypted Nostr group messaging, follows last week's durable-send release with version 0.11.0. Account recovery now declares a history gap complete only after every required relay finishes an untruncated event comparison; an unproven gap produces a durable notice that a host can show to the user. A full delivery queue

Primary links: https://github.com/marmot-protocol/mdk, https://github.com/marmot-protocol/mdk/releases/tag/v0.11.0, https://github.com/marmot-protocol/mdk/blob/v0.11.0/docs/release/0.11.0.md

## Myco 0.8.0–0.8.1 gives nearby apps their own Nostr store — 9/10

Myco is an Android app for exchanging small Nostr programs, called napplets, with nearby phones, including when they are offline. Version 0.8.0 gives each installation a guest Nostr identity and permits login with an existing key or Amber, an Android signer that approves signatures without sharing the account key. It also replaces the Discover tab with an app store that is itse

Primary links: https://github.com/Origami74/myco, https://github.com/Origami74/myco/releases/tag/v0.8.0, https://github.com/Origami74/myco/releases/tag/v0.8.1

## nostream 3.1.0 adjusts relay proof of work to load — 8/10

nostream is a TypeScript Nostr relay backed by PostgreSQL. Version 3.1.0 can raise or lower the event proof-of-work threshold between operator-set limits as its observed event rate changes. The setting is off by default, uses each worker's measured rate, and leaves the existing static public-key threshold independent, so operators must opt in before senders see a different admi

Primary links: https://github.com/Cameri/nostream, https://github.com/cameri/nostream/releases/tag/v3.1.0, https://github.com/Cameri/nostream/releases/tag/v3.1.0

## Nostr double ratchet 0.0.171–0.0.172 closes a removed-member gap — 8/10

Nostr double ratchet is a TypeScript library for encrypted private chats carried by Nostr. Version 0.0.171 rotates a group's sender key after membership changes so someone removed with the old keys cannot decrypt later messages from an updated sender, even after that sender restarts. It also refuses sends or key rotation by a removed local owner and aborts a send if membership

Primary links: https://github.com/irislib/nostr-double-ratchet, https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.171, https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.172

## Scramble 0.7.4–0.7.5 fetches the messages a new group member should see — 8/10

Scramble is a cross-platform Marmot group messenger with a native Android interface. In version 0.7.5, each group gets its own relay history cutoff: previously the most active conversation's cutoff was applied to every group, so a newly joined one could remain empty because its post-join messages were never requested. The reconnect path receives the same fix, and a group with n

Primary links: https://github.com/DavidGershony/Scramble, https://github.com/DavidGershony/Scramble/releases/tag/v0.7.5, https://github.com/DavidGershony/Scramble/releases/tag/v0.7.4

## Amber 6.6.6 repairs remote-signer connection secrets — 8/10

Amber is an Android signer that approves Nostr event signatures without handing an application's account key to it. After last week's backup-encryption change, version 6.6.6 fixes its `nostrconnect` parser: a connection parameter containing `=`, such as a padded secret, had been altered before Amber answered. That made NDK-based clients fail their secret check even when the sig

Primary links: https://github.com/greenart7c3/Amber, https://github.com/greenart7c3/Amber/releases/tag/v6.6.6

## FIPS 0.5.2 stops a Nostr discovery privacy leak — 8/10

FIPS is an encrypted mesh that uses Nostr identities and relay messages to discover peers. Its 0.5.2 maintenance release stops signing NAT-traversal deletion requests with the node's routing key, which had linked that key to traversal traffic on relays. It also updates the TLS library used for relay connections to a version that fixes a published security advisory and repairs s

Primary links: https://github.com/jmcorgan/fips, https://github.com/jmcorgan/fips/releases/tag/v0.5.2

## napplet soyLI 0.23.1–0.23.4 repairs backend publishing and signer approval — 8/10

napplet.soy's soyLI is the creator and publishing toolkit for small sandboxed Nostr programs. After last week's shared-creations release, version 0.23.1 makes backend manifests, handlers, and schemas part of creator checks and multiplayer previews. It keeps portable provider configuration in the project manifest while leaving private identity bindings and development databases

Primary links: https://github.com/zeSchlausKwab/napplet-soy, https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.1, https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.2, https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.4

## Dart NDK dev.7–dev.9 keeps Blossom auth scoped and signer replies moving — 8/10

Dart NDK is a Flutter and Dart library for Nostr relay access, signing, wallet requests, and media operations. Following last week's prerelease, 0.10.0-dev.7 changes Blossom media requests to stay anonymous until a server refuses them, then authorizes through an explicit policy that says which identity an operation may reveal. It carries that authorization through the request p

Primary links: https://github.com/relaystr/ndk, https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.7, https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.9, https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.8

## Mostro Core 0.16.0 removes the old gift-wrap transport — 8/10

Mostro Core supplies the message protocol used by Mostro's Nostr-based peer-to-peer trading clients and coordinator. Version 0.16.0 removes its protocol-v1 gift-wrap transport and its old wrap and unwrap functions, leaving the newer transport as the library path. That is a breaking change for applications still constructing or reading v1 messages through this library.

Primary links: https://github.com/MostroP2P/mostro-core, https://github.com/MostroP2P/mostro-core/releases/tag/v0.16.0, https://github.com/MostroP2P/mostro-core/releases/tag/v0.15.1

## Cambium 0.6.0–0.7.1 enrolls an unlock phone through relay messages — 8/10

Cambium is an Android signing companion for a Heartwood hardware key that can also unlock the board after a restart. Version 0.6.0 lets a phone enroll for unlock through the board's Nostr relays without a USB cable; the user compares five request words on the phone, the board, and Sapwood, the board's enrollment interface, before pressing the board's button. Newly announced rel

Primary links: https://github.com/forgesworn/cambium, https://github.com/forgesworn/cambium/releases/tag/v0.6.0, https://github.com/forgesworn/cambium/releases/tag/v0.7.0, https://github.com/forgesworn/cambium/releases/tag/v0.7.1

## Bray 3.5.0–3.5.2 limits agent-initiated Nostr wallet spending — 8/10

Bray is a Nostr tool server that lets an AI assistant request relay, identity, and wallet actions through a scoped interface. Its 3.5.0 release adds a cap on each Nostr Wallet Connect payment and a persisted daily budget, with human confirmation where the assistant host supports it. Serving separate spending connections now requires an explicit wallet-service setting, rechecks

Primary links: https://github.com/forgesworn/bray, https://github.com/forgesworn/bray/releases/tag/v3.5.0, https://github.com/forgesworn/bray/releases/tag/v3.5.2

## Mafrend 1.3.0-alpha moves private map groups to current Marmot — 8/10

Mafrend is a map-based Nostr social app that lets people explore places and chat around destinations. Its 1.3.0-alpha release upgrades private groups to a newer Marmot encrypted-group specification and adds profile views from chats and reviews. The group format is incompatible with older alpha chats; users should treat this as an alpha migration with a compatibility break.

Primary links: https://github.com/DestBro/mafrend-zapstore, https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.3.0-alpha

## Sonar alpha.15–alpha.15.1 repairs encrypted-group publishing — 8/10

Sonar is a private messenger that can carry conversations over Bluetooth mesh and Nostr. Alpha.15 adds emoji reactions to messages and private local-time sharing inside encrypted chats, with a setting to revoke that sharing. Its wallet switches to Cashu, but that payment change is separate from the messaging update.

Primary links: https://github.com/hedwig-corp/bitchat-to-sonar, https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.15, https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.15.1

## Elisym's commerce packages introduce private Nostr orders — 8/10

Elisym is a Nostr-based agent toolkit now building a signed-event commerce flow. Its first `commerce` package defines store products, owner authorization, privately wrapped orders and receipts, and offer verification for the checkout and merchant components. A later commerce 0.2.0 tag derives an order's payment reference from that order, tying the payment lookup to the signed p

Primary links: https://github.com/elisymlabs/elisym, https://github.com/elisymlabs/elisym/releases/tag/%40elisym/pay-core%400.1.1, https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0

## Flotilla 1.11.2 unsticks signers and incomplete relay feeds — 8/10

Flotilla is a Nostr client for conversations, rooms, and shared spaces. Version 1.11.2 gives a user a way out when startup stalls waiting for a remote signer, and signs out a session whose local application data has been cleared. A room can now display its messages before its wider space finishes synchronizing, while feeds no longer omit posts simply because one relay answered

Primary links: https://github.com/coracle-social/flotilla, https://github.com/coracle-social/flotilla/releases/tag/1.11.2

## Ditto 2.42.3 shows relay delivery and tightens account boundaries — 8/10

Ditto is a Nostr social client that lets users choose and authenticate to their relays. In version 2.42.3, a post's Event Details shows which user and author relays hold it; Broadcast targets only the missing ones. The release also points out unresponsive read relays and gives them a retry control, making a missing post easier to diagnose without sending it everywhere again.

Primary links: https://gitlab.com/soapbox-pub/ditto, https://gitlab.com/soapbox-pub/ditto/-/releases/v2.42.3

## Iris Chat 2026.9.24.4 brings calls into encrypted conversations — 8/10

Iris Chat is an end-to-end encrypted Nostr messenger using the double-ratchet family of chat protocols. Its September 24 release adds voice and video calls with compatible contacts, including over an existing local connection when the internet is unavailable. A user can lower video quality, answer video as voice, and handle an incoming call through Android's call interface; ans

Primary links: https://github.com/irislib/iris-chat-rs, https://github.com/irislib/iris-chat-rs/releases/tag/v2026.9.24.4, https://github.com/irislib/iris-chat-rs/releases/tag/v2026.9.24.5

## LibreNostr 0.6.0–0.7.0 routes relays through built-in Tor — 8/10

LibreNostr is an Android Nostr client with configurable relay and privacy settings. Version 0.6.0 bundles an Arti-based Tor engine on ARM64 and applies the chosen Direct, Tor-for-everything, or `.onion`-only mode to relay WebSockets, HTTP requests, media, uploads, and web pages. Strict Tor mode fails closed when Tor is unavailable and never silently sends a request directly; ch

Primary links: https://github.com/Lwb89dev/librenostr, https://github.com/Lwb89dev/librenostr/releases/tag/v0.6.0, https://github.com/Lwb89dev/librenostr/releases/tag/v0.6.2, https://github.com/Lwb89dev/librenostr/releases/tag/v0.7.0

## Newlay 0.3.45 streams large relay queries instead of closing them — 8/10

Newlay is an Android-hosted Nostr relay and related local services. Its signed 0.3.45 release announcement says that large query results now stream with backpressure instead of closing the client's connection. The embedded Git host prunes superseded packs after pushes, while its Cordn encrypted-messaging coordinator accepts oversized client requests and sends an abort frame whe

Primary links: https://code.relay.tools/opensauce/newlay, https://primal.net/e/b8380ae1bf30492129727ec59e27e2ae8a4cf9ad08e7361826a9ba8be88a227a

## ngit-grasp 3.0.5 keeps Git pushes and relay sync moving — 8/10

ngit-grasp is a self-hosted Nostr relay and Git server for signed repository collaboration. Its signed 3.0.5 release announcement moves slow history reconciliation out of the shared live-sync actor, allowing relay subscriptions to start while earlier events are checked. It backs off separately for rate limits, incomplete history queries, mailbox reads, and identity lookups, so

Primary links: https://gitworkshop.dev/danconwaydev.com/ngit-grasp, https://primal.net/e/6ff00b9230e4523e6f14aaf6e5088f91e5696be38b9304a4e1cef384e3318d41

## Armada 0.63.0 carries push alerts across signer types — 8/10

Armada is a Nostr client for encrypted communities, channels, and direct messages. Following last week's media-privacy release, its signed 0.63.0 announcement describes a new browser push path that works while the app is closed for extension and remote-signer logins as well as other account types. Tenna, a host app that embeds Armada, also gains background notifications for its

Primary links: https://github.com/soapbox-pub/armada, https://primal.net/e/34021b55504d74c5d04f55dbfea87f31168a7c4582f35113d7ec063894d19e56

## deed 0.3.0–0.3.2 makes Zig Nostr publishing steadier — 8/10

deed is a Zig command-line tool for reading and publishing Nostr events. Its September 24 version 0.3.2 adds an agent skill and fixes relay ping deadlines; the preceding 0.3.1 and 0.3.0 releases improve performance and publication reliability. The three tags describe one early tool series. The visible Nostr benefit is a steadier relay connection and event-publishing path for sc

Primary links: https://github.com/zig-nostr/deed, https://github.com/zig-nostr/deed/releases/tag/v0.3.2, https://github.com/zig-nostr/deed/releases/tag/v0.3.1, https://github.com/zig-nostr/deed/releases/tag/v0.3.0

## Amethyst repairs encrypted-group interoperability — 8/10

Amethyst is an Android Nostr client with Marmot encrypted-group support. White Noise is another Marmot messenger; an interoperability batch tested with its clients addresses group administration, deletion wording, and other behavior exposed when the two clients share a conversation. More pointed fixes send reactions and deletions inside the Marmot group instead of as separate N

Primary links: https://github.com/vitorpamplona/amethyst, https://github.com/vitorpamplona/amethyst/pull/4245, https://github.com/vitorpamplona/amethyst/pull/4233, https://github.com/vitorpamplona/amethyst/pull/4240, https://github.com/vitorpamplona/amethyst/pull/4201, https://github.com/vitorpamplona/amethyst/pull/4231, https://github.com/vitorpamplona/amethyst/pull/4174

## Divine adds encrypted video to direct messages — 8/10

Divine is a Nostr video client. NIP-17 carries private messages in encrypted gift wraps that hide their sender from relays. Divine's merged video-message work encrypts an attached video on the device, uploads ciphertext, and sends the decryption key inside that private message. A recipient can verify and decrypt the file for playback or save it. A separate history-restore fix k

Primary links: https://github.com/divinevideo/divine-mobile, https://github.com/divinevideo/divine-mobile/pull/9486, https://github.com/divinevideo/divine-mobile/pull/9446

## Buzz extends its relay's channel and identity controls — 8/10

Buzz is a Nostr-based workspace with its own relay and clients. Its merged channel-artifact implementation gives an editable record one channel home and a revision chain; conflicting edits cannot both become the head. The project's NIP-AR label refers to its own proposal and implementation, not an established Nostr standard.

Primary links: https://github.com/block/buzz, https://github.com/block/buzz/pull/7919, https://github.com/block/buzz/pull/7264, https://github.com/block/buzz/pull/7849

## Conduit advances checkout after relay acceptance — 8/10

Conduit is a Nostr marketplace that sends private order messages to merchants. Progressive relay publishing distinguishes the first positive relay acknowledgement from completion of all relay attempts, and a checkout follow-up persists that first acknowledgement before proceeding. A relay's acceptance means the signed order reached a relay; it does not prove a merchant read or

Primary links: https://github.com/Conduit-BTC/conduit-mono, https://github.com/Conduit-BTC/conduit-mono/pull/483, https://github.com/Conduit-BTC/conduit-mono/pull/488, https://github.com/Conduit-BTC/conduit-mono/pull/529, https://github.com/Conduit-BTC/conduit-mono/pull/533

## Mostro removes its first-generation daemon transport — 8/10

Mostro coordinates peer-to-peer Bitcoin trades using Nostr messages. NIP-59 defines gift wraps that obscure the sender and contents of a relayed event. A merged daemon change removes Mostro's first-generation gift-wrap protocol path and expects the newer transport. Operators still on first-generation clients will need a compatible daemon version; the source merge does not estab

Primary links: https://github.com/MostroP2P/mostro, https://github.com/MostroP2P/mostro/pull/1004, https://github.com/MostroP2P/mostro/pull/1000

## Elisym builds a Nostr commerce checkout — 8/10

Elisym is developing a commerce toolkit that signs products and carries private order and receipt messages over Nostr. Its merged commerce package defines offer verification and gift-wrapped order events; a checkout interface handles offer review, wallet payment, and delivery status, while a self-hosted merchant node packages the store side. The project calls kind `30490` provi

Primary links: https://github.com/elisymlabs/elisym, https://github.com/elisymlabs/elisym/pull/120, https://github.com/elisymlabs/elisym/pull/131, https://github.com/elisymlabs/elisym/pull/133

## nostter improves signer checks and event retrieval — 8/10

nostter is a Nostr social client. Its merged signer-capability change asks whether a usable signer is present before offering follow and reaction actions. New pin tags carry the author's key and a known relay hint without guessing one, and replaceable-event cache ordering follows NIP-01's timestamp and event-ID tie-break. NIP-01 defines the core Nostr event rules, including how

Primary links: https://github.com/SnowCait/nostter, https://github.com/SnowCait/nostter/pull/2573, https://github.com/SnowCait/nostter/pull/2611, https://github.com/SnowCait/nostter/pull/2608

## Pensieve prepares isolated archive reconciliation — 8/10

Pensieve is a Nostr archive and recovery tool. Its merged isolated negentropy runtime gives synchronization a bounded worker and durable completion behavior. The feature is opt-in and the PR explicitly says no production service or configuration was activated; this is groundwork for a safer recovery path, not evidence of a running deployment.

Primary links: https://github.com/andotherstuff/pensieve, https://github.com/andotherstuff/pensieve/pull/60

## ContextVM avoids duplicate calls across relays — 8/10

ContextVM's TypeScript SDK carries tool and resource requests as Nostr events. Its merged inbound deduplication fix recognizes one plaintext request by event ID even when multiple relays or a reconnect deliver it again, matching the existing wrapped-message path. The PR reports one non-idempotent tool running three times for a single call before the fix. A companion resource-no

Primary links: https://github.com/ContextVM/sdk, https://github.com/ContextVM/sdk/pull/103, https://github.com/ContextVM/sdk/pull/101

## Cyberspace revises the DECK-0003 object rules — 8/10

Cyberspace develops the DECK-0003 format for structured Nostr objects and encrypted region bags, which Amethyst began implementing in last week's issue. New parts and hidden-object rules and bag references let a bag refer to a separately published object instead of embedding every part. A later correction says that an event-ID reference cannot reliably pin an old version of an

Primary links: https://github.com/arkin0x/cyberspace, https://github.com/arkin0x/cyberspace/pull/36, https://github.com/arkin0x/cyberspace/pull/38, https://github.com/arkin0x/cyberspace/pull/40

## Wisp fixes replies to Nostr comments — 8/10

Wisp is a Nostr client with relay-routing and wallet features. After last week's released NIP-22 comment support, a merged follow-up makes a reply to a NIP-22 comment a comment event too, with the proper parent and root references; the previous path always published an ordinary note. NIP-22 lets comments attach to many Nostr content types. The fix merged after Wisp's 1.2.5 tag,

Primary links: https://github.com/barrydeen/wisp, https://github.com/barrydeen/wisp/pull/667

## Cordn sends coordinator locations to a second device — 8/10

Cordn coordinates encrypted group messaging over Nostr. Its merged multi-device specification change carries a group's coordinator relay hints in the replicated group document. A newly seeded device can then find a coordinator that is absent from default relays, instead of appearing to join a group whose backlog and live messages it cannot fetch. This is protocol-document work

Primary links: https://github.com/Cordn-msg/cordn, https://github.com/Cordn-msg/cordn/pull/9

## Nostr Atlas opens a directory for checkable identities — 8/10

Nostr Atlas is a new directory that presents Nostr profiles alongside claims to external accounts. Its merged site publication separates the directory from the project's component demo, and the site responds publicly. A claim-flow merge lets an X account owner publish a signed NIP-39 proof with a browser signer, while profile enrichment reads kind-0 Nostr metadata only after th

Primary links: https://nostr-atlas.web.app, https://github.com/saiy2k/nostr-components/pull/148, https://github.com/saiy2k/nostr-components/pull/144, https://github.com/saiy2k/nostr-components/pull/146

## nostr-java adds media hosting tools and preserves tag positions — 8/10

nostr-java is a Java library and MCP tool set for Nostr applications. Its merged Blossom tools let a caller upload, find, list, and delete hash-addressed media and manage the user's server list. A separate publishing fix keeps empty tag values in place: Nostr tags are positional, so dropping an empty relay hint could shift a marker into the wrong field and make the published ev

Primary links: https://github.com/tcheeric/nostr-java, https://github.com/tcheeric/nostr-java/pull/557, https://github.com/tcheeric/nostr-java/pull/558

## Zap Cooking changes how account history can be recovered — 8/10

Zap Cooking is a recipe-sharing Nostr client. Its merged Lazarus recovery work replaces a backup built on NIP-78 application-specific data events with an approach that scans relay-retained versions of replaceable events to detect overwritten follows, mutes, or profiles. Lazarus remains a draft protocol; recovery depends on relays that retained the older versions, and a merged w

Primary links: https://github.com/zapcooking/frontend, https://github.com/zapcooking/frontend/pull/753, https://github.com/zapcooking/frontend/pull/743, https://github.com/zapcooking/frontend/pull/752

## Opal brings remote signing to Omarchy — 9/10

Opal is a desktop Nostr signer built for the Omarchy Linux environment. Its September 28 version 0.3.3 follows the first public series with NIP-46 remote-signing support, a local keyring, and a permission interface for requests from connected apps. NIP-46 keeps the account key with the signer while a separate client asks it to approve operations. This is an early release of a p

Primary links: https://github.com/derekross/opal, https://github.com/derekross/opal/releases/tag/v0.3.3

## WatchTower opens a NIP-86 relay control panel — 8/10

WatchTower is a newly published panel for relay administration through NIP-86, the protocol for authenticated relay management requests. A public instance responds, giving operators a place to inspect the interface. The repository was created September 22; a reachable site does not establish that its authorization flows have been independently audited or that it works with ever

Primary links: https://github.com/iqbqioza/watchtower, https://watchtower.nostrfy.org

## Hubstr Blossom opens a personal media origin — 8/10

The newly published Hubstr Blossom server lets a Nostr client upload images, video, and files to a self-hosted Blossom endpoint, then put those URLs in events. Its README documents local content-hash storage, a SQLite index, signed kind-24242 authorization for changes, and a range of Blossom operations for upload, mirroring, listings, and deletion. Public reads let other client

Primary links: https://github.com/johninnis/hubstr-blossom

## Meshstr experiments with a permissionless relay mesh — 8/10

Meshstr is an alpha design for Nostr relays to negotiate peer budgets and exchange signed usage receipts. Its first implementation includes a write-policy bridge for strfry, a Nostr relay, added September 27, with a socket fix the next day. The repository describes DIDComm negotiation and NIP-77 reconciliation, which lets peers compare event sets without exchanging their full i

Primary links: https://gitlab.pocketlabs.dev/meshstr/meshstr, https://gitlab.pocketlabs.dev/meshstr/meshstr/-/commit/6d609fc99f

## Dossier shows what a public Nostr history can reveal — 9/10

Dossier is a new browser-side self-audit tool for a person's Nostr and Lightning footprint, with a public demo. It gathers visible profile links, zap trails, posting times, metadata from old NIP-04 encrypted direct messages, and media metadata such as photo EXIF; it can also show where a relay still serves an event someone tried to delete. NIP-07 signer support lets a user auth

Primary links: https://github.com/satanrayshe/dossier, https://satanrayshe.github.io/dossier/

## NIP-39 extends identity proofs to Bluesky and Discord — 8/10

NIP-39 lets a Nostr account point to proof that it controls an identity on another platform. A change merged September 27 gives new proofs one recommended sentence and tells verifiers to accept older proofs that contain the account's npub, even when their wording differs. It also documents Bluesky posts and Discord messages as proof locations. A Discord claim can only be checke

Primary links: https://github.com/nostr-protocol/nips/pull/2486

## NIP-86 adds invite-code management for relay administrators — 8/10

Compass described in the July 8 issue the NIP-86 invitation proposal while it was open; it has now merged. NIP-86 defines a standard relay-management API, and NIP-43 defines how restricted relays announce membership and process admission requests. The September 24 merge adds `listclaims`, `createclaim`, and `deleteclaim` so an administrator can list, issue, and revoke invite co

Primary links: https://github.com/nostr-protocol/nips/pull/2408, https://github.com/nostr-protocol/nips/blob/5b9920982ae1f4061328c1b09a90360da28d13c8/86.md

## NIP-51 moves favorite follow sets to an unused event kind — 8/10

NIP-51 defines public and private lists, including a list of a user's favorite follow sets. Compass described the kind-collision proposal in the July 22 issue; it has now merged. The September 27 correction assigns that favorites list kind `10021` because the earlier number was already in use. Its `a` tags still point to kind `30000` follow sets. The change resolves a number co

Primary links: https://github.com/nostr-protocol/nips/pull/2417

## NIP-DB proposes verified domain names for key-addressed services — 8/10

The open NIP-DB proposal, submitted September 28, describes Nostr events that bind an ordinary Internet domain to the key serving it over a key-addressed network such as FIPS, an encrypted mesh that addresses nodes by Nostr public key. A domain owner can establish the binding with a DNS TXT record or a DNSSEC proof carried with the claim; clients would pin a verified result for

Primary links: https://github.com/nostr-protocol/nips/pull/2487, https://github.com/fr34aky/fips-pub-domains

## A private-feed draft explores encrypted groups of recipients — 8/10

A new multi-recipient envelope proposal, opened September 29, sketches private notes, replies, and connections whose intended recipients can find an event without exposing their ordinary public keys in its visible tags. It proposes opaque pairwise alias tags derived from shared secrets and provisional event kinds, including a way to wrap another Nostr event for hundreds of read

Primary links: https://github.com/nostr-protocol/nips/pull/2488

## A Blossom proposal lets other people announce mirrored media — 8/10

An open NIP proposal describes a way for someone who mirrors another author's Blossom blob to announce that copy through Nostr. A client could then look for the copy if the original server loses the blob. Discussion has also raised checking the mirror's current BUD-03 server list when an announced server hint has gone stale. This is a proposed discovery path, not a guarantee th

Primary links: https://github.com/nostr-protocol/nips/pull/2478

## Road-event reports seek a shared Nostr format — 8/10

The open Road Event Reports proposal describes reports and confirmations for potholes, closures, cameras, and other road conditions. It uses location tags and NIP-40's expiration timestamp, which tells relays when to stop serving an event, so a report need not remain current indefinitely. The author based revisions on a sample of events recovered from public relays and on the e

Primary links: https://github.com/nostr-protocol/nips/pull/2479, https://github.com/jooray/roadstr

## Six Years of Nostr Septembers — 8/10

A September 4 BUber commit explored a taxi-matching concept using Nostr events. It showed how a signed, relay-carried request could coordinate people without assigning the whole service to one server. The source is a concept, and it does not establish a launched ride service.

Primary links: https://github.com/arcbtc/buber/commit/7a66d400f2, https://github.com/emeceve/loquaz/commit/d885d93d22, https://github.com/nostr-protocol/nips/commit/3423a6dfb, https://github.com/nostr-protocol/nips/commit/b62aa418d, https://github.com/nostr-protocol/nips/blob/master/26.md, https://github.com/damus-io/damus/blob/master/CHANGELOG.md#16-18---2023-09-21, https://github.com/nostr-protocol/nips/commit/44c21c9d8, https://github.com/nostr-protocol/nips/commit/3b5d3ca67, https://github.com/damus-io/damus/blob/master/CHANGELOG.md#1101---2024-09-22, https://github.com/nostr-protocol/nips/commit/ea36ec9ed, https://github.com/nostr-protocol/nips/commit/79786bb7b, https://github.com/nostr-protocol/nips/commit/4c5d5fff9, https://github.com/nostr-protocol/nips/commit/400d975da, https://github.com/nostr-protocol/nips/commit/6631b3eb1, https://github.com/nostr-protocol/nips/commit/0046368a7

GATE: FAIL — The four independent Stage 4 selection reviews required by OrchestratorAgent.md have no edition-2026-09-30 receipts; deterministic source/selection coverage passes but cannot substitute for those reviews.
