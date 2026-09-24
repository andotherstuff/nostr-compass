---
title: "Nostr Compass #38"
date: 2026-09-02
publishDate: 2026-09-02
draft: false
type: newsletters
description: "Voca 1.0 brings verified Nostr reading to an offline text-to-speech app, nostream expands relay-side job routing and authentication, Napstr publishes Tor-based audio catalogues, MDK 0.9.17 trims group-maintenance cost, the core NIPs merge a pagination hint and highlight tags alongside NWC transaction totals, and the NIP Deep Dive explains reposts and reactions."
---

Welcome back to [Nostr Compass](https://nostrcompass.org), your weekly guide to Nostr.

**This week:** [Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) 1.0 brings verified Nostr notes and long-form subscriptions to an offline Android reader that speaks articles aloud, [nostream](https://github.com/cameri/nostream) expands relay-side job routing and authenticated operation, [NDK for Dart](https://github.com/relaystr/ndk) fixes negentropy and multi-relay request lifetimes, [Divine Mobile](https://github.com/divinevideo/divine-mobile) makes wrapped-message deletion and signing deterministic, [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay) protects gift-wrap inboxes by default, [Amethyst](https://github.com/vitorpamplona/amethyst) ships portable highlights, and [Mostro](https://github.com/MostroP2P/mostro) verifies signed orders before its spam gate. [Napstr](https://github.com/lnbits/napstr) publishes audio catalogues and seeder heartbeats over Nostr while transferring files through Tor. Releases cover [MDK](https://github.com/marmot-protocol/mdk) and [pakstr](https://git.nostrdev.com/stuff/pakstr); protocol work merges an [NIP-67](/en/topics/nip-67/) pagination hint and an [NIP-84](/en/topics/nip-84/) highlight tag scheme in the [NIPs repository](https://github.com/nostr-protocol/nips) while [Nostr Wallet Connect](https://github.com/nostr-wallet-connect/nwc) adds transaction totals; and the NIP Deep Dive traces reposts and reactions across their event shapes and current implementations.
## Top Stories

### Voca 1.0 reads verified Nostr notes and subscriptions aloud on Android

[Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) is an offline Android reader that speaks articles, PDFs, Markdown files, and Nostr notes in the phone's own text-to-speech voice while the spoken sentence stays lit on the page. Its [1.0 release](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en), [published on 2026-08-27](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) under its own [project key](https://njump.me/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu), makes Nostr a first-class source: paste a note address, an event identifier, an npub, a profile, or an ordinary web link with a Nostr entity inside it, and the app decodes the reference, fetches the signed event from relays, and reads the author's text rather than the web page built around it.

Two verified behaviors define the Nostr integration, both described in [Voca's signed 1.0 announcement](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en). First, every fetched event is checked against its recomputed id and its BIP-340 Schnorr signature before it is persisted, using the bootstrap relays, the author's [NIP-65](/en/topics/nip-65/) relay list (a signed, replaceable kind `10002` event where an author lists the relays they read and write), and hints carried inside the reference itself, so a relay can decline to answer but cannot put words in an author's mouth. Second, adding an author's npub puts their [NIP-23](/en/topics/nip-23/) long-form articles (addressable kind `30023` posts with titles, summaries, and images) into a single on-device inbox beside RSS and Atom feeds. The 1.1.0 update, [announced on 2026-08-28](https://gitworkshop.dev/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu/voca) and published to [Zapstore](https://zapstore.dev) on 2026-08-29, puts sentence-level scrolling on time, smooths long documents, and recovers the home-screen widget after manual scrolling, resizing, process restarts, and upgrades.


### nostream expands relay-side DVM routing and authenticated operation

After [August 19's job-ingestion work](/en/newsletters/2026-08-19-newsletter/#nostream-adds-a-relay-monitor-and-mints-invite-codes), [nostream](https://github.com/cameri/nostream), a TypeScript relay implementation, [stores and serves NIP-89 application handler events](https://github.com/cameri/nostream/pull/737). [NIP-89](/en/topics/nip-89/) (application handler discovery) uses kind `31989` recommendations and kind `31990` handler information, both already in the parameterized-replaceable range, so a client can query those kinds and receive a replacement when a `d` tag collides. The relay does not publish handler information for its own workers.

Pending [NIP-90](/en/topics/nip-90/) (data vending machine) jobs now [reach a worker process and return as result events](https://github.com/cameri/nostream/pull/734). On success the relay signs a kind 6000-6999 result with its own key. A timeout or worker crash marks the job failed instead of leaving it submitted.

Authenticated sessions and admin HTTP calls sit on different boundaries. [NIP-42](/en/topics/nip-42/) (client authentication to relays) [tracks the authenticated pubkey per socket](https://github.com/cameri/nostream/pull/716), can require AUTH before clients publish events, and advertises that requirement in the [NIP-11](/en/topics/nip-11/) (relay information) document, with both controls off by default. Separately, [admin API routes can accept NIP-98 signed HTTP authorization](https://github.com/cameri/nostream/pull/730). [NIP-98](/en/topics/nip-98/) (HTTP authentication with signed events) stays off until an operator enables it and names the allowed pubkeys.

### NDK for Dart fixes negentropy, multi-relay request lifetimes, and signature verification

A [NIP-77](/en/topics/nip-77/) (negentropy set-reconciliation) run in [NDK](https://github.com/relaystr/ndk), a Dart development kit for Nostr, returned the wrong have and need sets without erroring, because the codec did not speak [negentropy](/en/topics/negentropy/) protocol v1. The [v1 encoding fix](https://github.com/relaystr/ndk/pull/722) now returns the ids held by the relay and the ids it still needs.

Identical filters sent to different relays [were collapsing into one request](https://github.com/relaystr/ndk/pull/705). Requests with the same filter now stay distinct when they target different relays or have different lifetimes, so a short query cannot mix another relay's events into the result or leave a live subscription stalled.

The same kit [verifies a signature once and keeps that result](https://github.com/relaystr/ndk/pull/726). A later duplicate delivery no longer spends another check or overwrites the stored verified event.

### Divine Mobile makes wrapped direct-message deletion and signing deterministic

Wrapped [NIP-09](/en/topics/nip-09/) (event deletion request) kind `5` events that targeted a message never applied in [Divine Mobile](https://github.com/divinevideo/divine-mobile), a mobile short-video client that publishes through Nostr. The client [now resolves each deletion against the named message](https://github.com/divinevideo/divine-mobile/pull/8174) instead of treating anything that is not a reaction as already processed. A second [delete-for-everyone request while the first was still in flight](https://github.com/divinevideo/divine-mobile/pull/8164) used to vanish with no error and no kind `5` on the wire; concurrent deletes now each publish.

After the previously covered 1.0.22 release, sending the same 1:1 [NIP-17](/en/topics/nip-17/) (gift-wrapped private DMs) text twice in one second [built one rumor id](https://github.com/divinevideo/divine-mobile/pull/8163), so the second send disappeared; each send now carries a token inside the [NIP-59](/en/topics/nip-59/) (gift wrap) rumor so the ids differ.

A caller that had already signed a kind `4` or kind `5` event [kept that signature](https://github.com/divinevideo/divine-mobile/pull/8173), instead of having a client tag appended afterward, which changed the id and made relays reject the event as invalid.

### Conduit Relay hardens its NIP-42 protected inbox

Kind `1059` gift wraps are stored for one recipient. [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay), a Go relay that keeps those wraps in a recipient-protected inbox, [defaults to enforce mode](https://github.com/Conduit-BTC/conduit-relay/pull/8): a kind `1059` query must present [NIP-42](/en/topics/nip-42/) authentication as that recipient, or the relay rejects the request. Mixed-kind filters, wildcards, counts, and [negentropy](/en/topics/negentropy/) over those wraps are `restricted`, so another AUTH cannot turn them into a dump of someone else's inbox.

The same [protected-inbox merge](https://github.com/Conduit-BTC/conduit-relay/pull/8) requires a canonical event id on the transmitted AUTH event and accepts an otherwise-valid NIP-42 event whether or not `content` is empty. Challenge-only still offers AUTH without blocking the read; disabled admits freely. The library default is enforce.

### Amethyst ships NIP-84 highlights and fixes two relay-facing failure paths

Following last week's [Blossom authorization work](/en/newsletters/2026-08-26-newsletter/#amethyst-moves-blossom-authorization-off-image-loading-threads), [Amethyst](https://github.com/vitorpamplona/amethyst), an Android Nostr client, ships [v1.14.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0) with [NIP-84](/en/topics/nip-84/) (portable highlights). A selected passage becomes a kind `9802` event from the composer, a highlights feed, or a share into the app.

The release adds [NIP-29](/en/topics/nip-29/) channel deletion and archival controls ([PR #3812](https://github.com/vitorpamplona/amethyst/pull/3812)) and measures relay behavior through the traffic the client already makes, then extends those [NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) probes with streaming, read, write, and URL checks ([PR #3836](https://github.com/vitorpamplona/amethyst/pull/3836), [PR #3857](https://github.com/vitorpamplona/amethyst/pull/3857)). Amethyst also removes a SharedKeyCache hash-collision vulnerability and compares message-authentication codes in constant time ([PR #3833](https://github.com/vitorpamplona/amethyst/pull/3833)), repairs a race that could lose connect-time AUTH delivery ([PR #3838](https://github.com/vitorpamplona/amethyst/pull/3838)), stripes subscription-state locking to end an ANR convoy ([PR #3851](https://github.com/vitorpamplona/amethyst/pull/3851)), and compares every subscription filter instead of only the first ([PR #3856](https://github.com/vitorpamplona/amethyst/pull/3856)).

[Newsletter #36 covered these relay-authentication, backup, and public-chat changes previously](/en/newsletters/2026-08-19-newsletter/#amethyst-rebuilds-its-relay-authentication-decision-flow); v1.14.0 has now shipped them together. Concord soft bans close authority gaps found by an audit ([PR #3885](https://github.com/vitorpamplona/amethyst/pull/3885)). Relay authentication has a redesigned permission flow ([PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899)), waits for challenge resolution instead of timing out ([PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905)), defaults new accounts to authenticate ([PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931)), honors that preference on relays outside the account's normal set ([PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937)), and keeps session grants across reconnects ([PR #3955](https://github.com/vitorpamplona/amethyst/pull/3955)). A guided first-run and Settings flow makes key backups discoverable ([PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909)), Cashu proof backfill and history paging stop wallet balances from being truncated ([PR #3941](https://github.com/vitorpamplona/amethyst/pull/3941)), and public chats can now be muted ([PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939)).

After that tag, [trusted lists](https://github.com/vitorpamplona/amethyst/pull/3983) in kinds `30392` through `30395` are [NIP-50](/en/topics/nip-50/) (full-text search) indexed by title only, so a list named in prose can be found without indexing member hex ids. Wallet refusals that arrived over [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) [now show their error instead of looking like a tap that did nothing](https://github.com/vitorpamplona/amethyst/pull/3987), including `QUOTA_EXCEEDED` and `RESTRICTED`, plus a timeout when the wallet never answers.

### Mostro validates signed orders before expensive work and preserves order audit events

After [v0.18.1's Cashu escrow foundation](/en/newsletters/2026-08-12-newsletter/#mostro-0181-starts-a-cashu-escrow-path-and-hardens-the-daemon), [Mostro](https://github.com/MostroP2P/mostro), a peer-to-peer exchange daemon that coordinates orders over Nostr, tagged [v0.18.5](https://github.com/MostroP2P/mostro/releases/tag/v0.18.5), which defaults transport to [NIP-44](/en/topics/nip-44/) (payload encryption) and keeps gift wrap as an explicit opt-in.

The release anchors waiting-state timeouts to the recorded take time so a maker bond is not slashed on the wrong clock ([PR #879](https://github.com/MostroP2P/mostro/pull/879)), dispatches each settled-order buyer payout at most once ([PR #881](https://github.com/MostroP2P/mostro/pull/881)), and moves those payouts through bounded, non-blocking `send_payment` waits ([PR #883](https://github.com/MostroP2P/mostro/pull/883)). An attempted change to pay the timeout-slash winner ([PR #875](https://github.com/MostroP2P/mostro/pull/875)) was reverted before the same tag shipped ([PR #885](https://github.com/MostroP2P/mostro/pull/885)). Mostro also stops republishing an unchanged pending order book every hour and at startup ([PR #888](https://github.com/MostroP2P/mostro/pull/888)), and its kind `38386` dispute events now carry a `created_at` tag for downstream ordering ([PR #878](https://github.com/MostroP2P/mostro/pull/878)).

After that tag, a [signature check now runs before the spam gate](https://github.com/MostroP2P/mostro/pull/892). An event id does not commit to `sig`, so a copy of a victim's kind `14` with a broken signature could occupy the replay slot and silently drop the valid message; the daemon verifies first and drops an invalid wrap instead of warning and continuing.

Fee-audit events of kind `8383` were carrying a [NIP-40](/en/topics/nip-40/) (expiration timestamp) of 15 days. They now [keep a one-year expiration](https://github.com/MostroP2P/mostro/pull/924), matching their role as a public payment record. On a Cashu-enabled node, taking an order [asks the seller over Nostr to lock a 2-of-3 escrow](https://github.com/MostroP2P/mostro/pull/830), publishes the waiting order event, and skips creation of a Lightning hold invoice. That completes the request path; it does not by itself close every escrow or marketplace-abuse case.

### Napstr publishes audio catalogues on Nostr and transfers files over Tor

[Napstr](https://github.com/lnbits/napstr) is a desktop audio-sharing client that publishes searchable catalogues and live seeders on Nostr, then transfers the files through a bundled Tor process with no direct-IP fallback. [Version 0.2.0](https://github.com/lnbits/napstr/releases/tag/v0.2.0) keeps profiles and catalogue metadata public, and it keeps requests, transfer credentials, file contents, and peer IP addresses off the relays.

Discovery uses two addressable event kinds in the [Napstr repository](https://github.com/lnbits/napstr). Kind `30421` catalogue entries name a file by its SHA-256 digest, public basename, size, and audio format, and an author withdraws a file by replacing that coordinate with a deleted marker. Kind `30422` availability heartbeats expire after ten minutes and list the file IDs the author is prepared to seed, so a catalogue row is live only while an unexpired heartbeat still contains that digest.

Public conversation uses [NIP-C7](/en/topics/nip-c7/) (kind 9 chat messages) instead of a relay-owned group. The [Napstr repository](https://github.com/lnbits/napstr) defines a shared public room plus a per-track discussion keyed to the file digest. Those messages are signed and public. They do not carry onion addresses, transfer credentials, or file bytes.

A download starts as a [NIP-17](/en/topics/nip-17/) (gift-wrapped private DMs) negotiation. The [Napstr repository](https://github.com/lnbits/napstr) wraps a request, an offer, or a refusal inside a kind `14` rumor, so relays do not see the temporary v3 onion hostname or the one-use capability that an accepted offer returns. Bundled Tor then moves the bytes over that onion, verifies the complete SHA-256 digest, and re-validates the audio before the file becomes playable.

The [v0.1.7 to v0.2.0 comparison](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) adds audiobook collections and Napstrfy, an optional Android companion. Kind `30423` manifests list ordered chapters that remain ordinary catalogue files, so a client that ignores the collection can still fetch each chapter. Napstr creates a non-destructive local Audiobooks folder for that purpose. Napstrfy pairs to a running desktop with a one-use QR code, then searches and requests downloads through that desktop's existing Nostr and Tor services without receiving the desktop secret key.

The same [comparison](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) times out a companion handshake that does not complete. A seeder copies and hashes the shared file before it serves bytes, writes incoming data into a private temporary file, confines audiobook destinations to a real child of the Napstr folder, and aborts if that destination changes during the transfer.

## Releases

### MDK v0.9.17: newest KeyPackages, membership activity, and durable sends

[Newsletter #37 covered MDK 0.9.14 and 0.9.15](/en/newsletters/2026-08-26-newsletter/#mdk-v0914-and-v0915-keypackage-selection-epoch-gap-recovery-and-split-relay-roles), including the change in the [MDK repository](https://github.com/marmot-protocol/mdk) from oldest-first KeyPackage selection to the newest valid current-profile package, the epoch-gap recovery gates, account cleanup, and the split between discovery and operational relays. Those fixes remain the base for the two releases that followed, so a stale package no longer blocks a member who has already published a usable one.

[Membership and admin events now advance the chat list](https://github.com/marmot-protocol/mdk/pull/1551) the way a new message does: preview text, ordering, unread counts, and read markers update when people join, leave, or change roles, and the local system actor is not treated as a Nostr profile. Reconnects and restarts [reuse one send identity for a retried durable outbound text](https://github.com/marmot-protocol/mdk/pull/1516), so the same group message is not published twice.

The two releases since then concentrate on the cost of keeping large groups healthy. [Version 0.9.16](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.16) [measures epoch divergence from the current epoch rather than a high-water mark](https://github.com/marmot-protocol/mdk/pull/1559), keeps refused inbound events fetchable ([PR #1565](https://github.com/marmot-protocol/mdk/pull/1565)), scopes replay rollback to canonical group state ([PR #1563](https://github.com/marmot-protocol/mdk/pull/1563)), and introduces [marmot-c](https://github.com/marmot-protocol/mdk/pull/1545), a macro-generated C ABI over the UniFFI bindings that lets hosts embed the engine directly. [Version 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.17) then folds pass-admission scans into [one member walk instead of a pass per member](https://github.com/marmot-protocol/mdk/pull/1617), [probes whether a group state is contested without seeding the full history graph](https://github.com/marmot-protocol/mdk/pull/1620), [cuts the deferred-peel sweep's idle-poll cost](https://github.com/marmot-protocol/mdk/pull/1621), and [applies the batched component read to the three projection sites the first pass missed](https://github.com/marmot-protocol/mdk/pull/1622). The matching [marmot-c 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/marmotc-v0.9.17) and [WN Agent 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.17) artifacts are built from the same commit, so embedders get the cheaper maintenance paths together.


### pakstr v0.16.0: kind-32267 identifiers on publish

After [last week's 0.13.0 through 0.15.0 Zapstore publication pipeline](/en/newsletters/2026-08-26-newsletter/#pakstr-0130-through-0150-makes-zapstore-publication-explicit), [pakstr](https://git.nostrdev.com/stuff/pakstr), a CLI that packages a web app into a signed Android APK and publishes it with a Nostr key, [logs the kind `32267` application-event IDs](https://git.nostrdev.com/stuff/pakstr/pulls/67) it looks up, publishes, or replaces. [Version 0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0) prints both the previous and new IDs when stale listing metadata triggers a republish, so a publisher can confirm which listing event is live on the relay.

The same [identifier log](https://git.nostrdev.com/stuff/pakstr/pulls/67) records the ID found during lookup before any replace, then the ID of the event that landed, so a no-op reuse appears as a repeated ID. That is the tagged change in [0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0); the Content-Digest, publish-before-upload, and publisher-validation behavior already shipped in the earlier tags.

## Unreleased Changes

### Zap Cooking scopes bunker relays and signs paid endpoints

Reloading a bunker session on [Zap Cooking](https://github.com/zapcooking/frontend), a recipe site built on Nostr long-form events, used to publish the encrypted [NIP-46](/en/topics/nip-46/) (remote signing over relays) conversation to every relay the page already used. [Scoping signer traffic to the bunker's own relays](https://github.com/zapcooking/frontend/pull/633) now applies that restriction on session restore and on nostrconnect pairing, the signer-initiated connection flow, matching the bunker-URL login path. It refuses to install an empty relay set from a malformed stored record, so relays that only host recipes no longer learn that the same pubkey keeps an active bunker session.

[Signed HTTP authentication](https://github.com/zapcooking/frontend/pull/630) now gates the paid cooking-assistant chat, the cookbook introduction, and gated-recipe updates under [NIP-98](/en/topics/nip-98/) (HTTP authentication with a signed Nostr event). The server reads the request body once, verifies the signature against that exact payload, and takes identity from the verified auth event instead of a public key supplied in the body. The chat preview still works with no header, while a present but invalid signature is rejected and the cookbook introduction always requires a signature. Updating a gated recipe now also requires that the verified key match the stored author; anyone else is told the recipe does not exist, so the endpoint does not confirm which paid records exist.

### nostrord repairs wrapped DMs and shared event links

After last week's [v2.9.0](/en/newsletters/2026-08-26-newsletter/#nostrord-v290-relay-scoped-group-state-and-media), [nostrord](https://github.com/nostrord/nostrord), a cross-platform client for relay-hosted communities, merged delivery fixes so a [NIP-17](/en/topics/nip-17/) (gift-wrapped private DM) sent from one device reaches the same account elsewhere. [Publishing the sender's self-copy independently](https://github.com/nostrord/nostrord/pull/295) stops the recipient wrap's first relay acceptance from dropping the copy other devices fetch. That same change resends a wrap after [NIP-42](/en/topics/nip-42/) (client authentication to relays) completes, and it marks the send successful on the first relay acceptance so one failing host cannot stall the rest. [Retrying parked gift wraps](https://github.com/nostrord/nostrord/pull/297) that failed [NIP-59](/en/topics/nip-59/) (gift wrap) decryption now happens on a timer, so a bunker that stays connected no longer leaves those messages mi... [truncated]

A [NIP-C7](/en/topics/nip-c7/) (kind `9` chat messages) reply repeats its parent as a leading [NIP-19](/en/topics/nip-19/) (bech32-encoded entities) `nevent` pointer beside the `q` tag. [Dropping that leading parent pointer](https://github.com/nostrord/nostrord/pull/292) when it opens the body and names the reply parent lets the row render as a single reply quote, while a pointer mid-body or a pointer that is the whole body still renders as a quote card. [Quoted-event links now encode `nevent`](https://github.com/nostrord/nostrord/pull/293) with the author, kind, and the relay the quote was read from, so a [NIP-29](/en/topics/nip-29/) (relay-managed groups) event shared into a DM can be fetched by another client instead of a bare note identifier that carries no lookup hints.

## NIP Updates and Protocol Spec Work

### Nostr Implementation Possibilities

Two specification merges landed in the core [NIPs repository](https://github.com/nostr-protocol/nips) this week.

[NIP-67](/en/topics/nip-67/) defines hints a relay can append to an `EOSE` (end of stored events) message so a client knows whether to keep paginating. The [merged `"auth"` hint](https://github.com/nostr-protocol/nips/pull/2371) adds a third value beside `finish` and `more`: a relay may now signal that additional stored events could become visible if the user authenticates, and it must send the [NIP-42](/en/topics/nip-42/) (relay authentication) `AUTH` challenge before the `EOSE` that carries the hint. The [accompanying NIP-42 addition](https://github.com/nostr-protocol/nips/pull/2371) defines the same flow from the client side, so a client that receives an `EOSE` with `auth` already holds the challenge it needs to answer.

[NIP-84](/en/topics/nip-84/) (portable highlights, the kind `9802` events Amethyst shipped support for above) [merged a tag-scheme update](https://github.com/nostr-protocol/nips/pull/2454): highlights may now tag their source with structured `i` tags per [NIP-73](/en/topics/nip-73/) (external content identifiers) in addition to `a`/`e` tags for Nostr events and `r` tags for anything else, and quote highlights moved from a MUST to a SHOULD on rendering like a quote repost.

### Nostr Wallet Connect

A `list_transactions` response can report how many transactions match the request, not how many rows the current page returned. [Merged optional `total_count`](https://github.com/nostr-wallet-connect/nwc/pull/4) on NWC-05 (the wallet-history extension) in the [NWC extension repository](https://github.com/nostr-wallet-connect/nwc) adds that field to the response used with [NIP-47](/en/topics/nip-47/) (encrypted remote wallet control over Nostr).

The [commit that adds `total_count`](https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67) documents it as an optional integer: the total number of transactions matching the request filters.

The [commit that excludes pagination from the count](https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e) states that this total excludes pagination, so it counts all matching transactions across every page.

## NIP Deep Dive: Reposts and Reactions

A contact can put an existing note back in front of their followers, and they can attach a compact like, dislike, or emoji without writing a reply. [NIP-18](/en/topics/nip-18/) (reposts) publishes that redistribution as its own signed event. [NIP-25](/en/topics/nip-25/) (reactions) publishes the compact response as a separate signed event. Both remain `draft` `optional` files on the [canonical repost specification](https://github.com/nostr-protocol/nips/blob/master/18.md) and the [canonical reaction specification](https://github.com/nostr-protocol/nips/blob/master/25.md): they are present in the NIPs repository and implemented by clients, while still labeled non-final.

### Reposts (NIP-18)

Followers receive a signed pointer to a kind 1 text note someone already published when a client writes a kind 6 event. [The repost specification](https://github.com/nostr-protocol/nips/blob/master/18.md) sets `kind` to 6, puts the stringified JSON of that note in `content` (empty `content` is allowed and not recommended), requires an `e` tag whose value is the note's `id` and whose third entry is a relay URL where the note can be fetched, and says the event SHOULD also carry a `p` tag with the original author's `pubkey`. A repost of a [NIP-70](/en/topics/nip-70/) (protected events) event SHOULD keep `content` empty so the protected payload is not copied into the new event.

A quote is a citation inside some other event, not a kind 6 wrapper. When a client mentions a [NIP-21](/en/topics/nip-21/) (`nostr:` URI) `nevent`, `note`, or `naddr`, it must convert that mention into a `q` tag of the form `["q", "<event-id> or <event-address>", "<relay-url>", "<pubkey-if-a-regular-event>"]`. [Quote-repost tags](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts) keep those citations out of reply threads and let clients pull and count the quotes on a post.

Kind 6 is reserved for kind 1 notes. A kind 16 generic repost can wrap any event kind other than kind 1. It SHOULD include a `k` tag whose value is the stringified kind of the inner event. When that inner event is replaceable, the generic repost SHOULD add an `a` tag with the `kind:pubkey:d-tag` coordinate; if that `a` tag is absent, the repost targets one specific version and `content` must hold the full JSON string of that version. [The generic-repost rules](https://github.com/nostr-protocol/nips/blob/master/18.md#generic-reposts) keep long-form, addressable, and other non-note events from being published as if they were kind 1.

The following kind 6 event is a live repost recovered from `wss://relay.damus.io` at assembly time ([open the event](https://njump.me/nevent1qqs88k8xgv2d3d3yymawaa24f22a0kqqvknpur0p05vq9e5r4y74xjspz3mhxue69uhhyetvv9ujuerpd46hxtnfdu7elvca)):

```json
{
  "kind": 6,
  "id": "73d8e64314d8b62426faeef5554a95d7d80065a61e0de17d1802e683a93d534a",
  "pubkey": "a60e79e0edad5100d7543b669e513dbc1c2170e8e9b74fdb8e971afd1e0e6813",
  "created_at": 1787768621,
  "tags": [
    [
      "e",
      "38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976"
    ],
    [
      "p",
      "34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095"
    ],
    [
      "client",
      "Primal iOS"
    ]
  ],
  "content": "{\"pubkey\":\"34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095\",\"sig\":\"8c0271f7b438083ce491c391335598e0cbceee0758177cf98f7894531033cb5153704b01009590f3d4e9cdfadd5bbf73fc5eea54186fcbac6d30744e0e6c1cd6\",\"id\":\"38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976\",\"tags\":[[\"r\",\"https:\/\/stacker.news\/items\/1555439\"],[\"client\",\"Damus\"]],\"created_at\":1787766056,\"content\":\"🚨 Attention CLN (Core Lightning) node runners 🚨\n\nhttps:\/\/stacker.news\/items\/1555439\",\"kind\":1}",
  "sig": "b6b97fa377cfdb651e2850f65f2ccb12ca0724c0de0fc0e39e9721f850abdfd31f5d5567517a51d988145c2a2de9ae9540b02eecf7352e554022870d5e8c64a5"
}
```

Its `kind` is 6, the `e` tag points to the reposted note, the `p` tag identifies that note's author, and `content` carries the original kind 1 event as stringified JSON. This relay-recovered event omits the relay hint that the [NIP-18 specification](https://github.com/nostr-protocol/nips/blob/master/18.md) marks as required, illustrating why readers and clients must validate real events and allow for producers that omit fields.

### Reactions (NIP-25)

A post can collect signed likes, dislikes, and emoji without those marks entering the reply thread. [The reaction specification](https://github.com/nostr-protocol/nips/blob/master/25.md) defines that mark as a kind 7 event whose `content` MUST carry the reaction value. `+` or an empty string MUST be read as a like or upvote. `-` MUST be read as a dislike or downvote. An emoji or a [NIP-30](/en/topics/nip-30/) (custom emoji) shortcode SHOULD NOT be read as a like or dislike, and a client MAY display that emoji on the post.

The target is in the tags, not inferred from `content`. There MUST be an `e` tag set to the target event `id`, and that tag SHOULD include a relay hint; extra `e` tags are not recommended, and if they appear the target `id` must be last. There SHOULD be a `p` tag for the target author, last if several `p` tags appear. An addressable target SHOULD also get an `a` tag with `kind:pubkey:d-tag` coordinates. The `e` and `a` tags SHOULD include relay and pubkey hints, the `p` tags SHOULD include relay hints, and a `k` tag MAY carry the stringified kind of the reacted event. [Those tag rules](https://github.com/nostr-protocol/nips/blob/master/25.md#tags) let a client fetch the target and notify its author from the reaction event alone.

A client MAY put a single `:shortcode:` in `content` and one `emoji` tag that maps that shortcode to an image URL, following the [custom-emoji reaction rules](https://github.com/nostr-protocol/nips/blob/master/25.md#custom-emoji-reaction). If the target is not a native Nostr event, the reaction MUST be kind 17 and MUST carry [NIP-73](/en/topics/nip-73/) (external content IDs) `k` and `i` tags, as in the [external-content reaction rules](https://github.com/nostr-protocol/nips/blob/master/25.md#external-content-reactions). Kind 17 is a reaction to a website, podcast episode, or other external object. It is not a kind 7 event-to-event reaction and it is not a repost.

The following kind 7 event is a live reaction recovered from `wss://relay.damus.io` at assembly time ([open the event](https://njump.me/nevent1qqsytac63l00k7kyaphkfwqqn94wglmx78v6zhqtytg65w5k957luccpz3mhxue69uhhyetvv9ujuerpd46hxtnfdus63jym)):

```json
{
  "kind": 7,
  "id": "45f71a8fdefb7ac4e86f64b800996ae47f66f1d9a15c0b22d1aa3a962d3dfe63",
  "pubkey": "0755cc2b972c3cbcae36913109c50b36b3fe110fa38a76dc37d1f01c5305496a",
  "created_at": 1787768605,
  "tags": [
    [
      "e",
      "519de32071d71bb2ab8b71a07e03eb9a256b6a59f9b08877b156c80966d5c320"
    ],
    [
      "a",
      "34236:5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb:2ddda68516f4729d3ef55a1eb01fe028253393212493a34816ad8eb79f97a3b7"
    ],
    [
      "p",
      "5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb"
    ],
    [
      "k",
      "34236"
    ],
    [
      "client",
      "Divine",
      "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile",
      "wss://relay.divine.video"
    ]
  ],
  "content": "+",
  "sig": "3c081756c7a73e2ee8aa10fadf3b5009390d5ac9a72078ba03701c42af91022ef275df7cb17724689a23dca4e29ff1a7cd5e3a24135d021983e2726a28b00b1e"
}
```

Its `content` is `+`, the conventional like from [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md). The `e` tag names the reacted-to event; the `a` tag adds its addressable coordinate; the `p` tag identifies its author; and the optional `k` tag records the target's kind as a string.

### Current client implementations

[Amethyst](https://github.com/vitorpamplona/amethyst), an Android Nostr client, defines the [repost event type](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip18Reposts/RepostEvent.kt) and the [reaction event type](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt) in its current protocol layer.

[Snort](https://github.com/v0l/snort), a web Nostr client, implements [NIP-18 helpers that include quote-link tag handling](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip18.ts) and [creates NIP-25 event-reaction tags](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip25.ts).

[Ditto](https://github.com/soapbox-pub/ditto), a combined Mastodon server and Nostr relay, [publishes kind 16 generic reposts with a `k` tag and an `a` coordinate on addressable targets](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/components/RepostMenu.tsx) and [applies kind 7 reaction semantics by treating the last `e` tag as the target event](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/lib/nostrEvents.ts).

### How They Work Together

A kind 6 or kind 16 event redistributes an existing event into the reposter's followers' feeds, either by embedding that event's JSON or by pointing at a replaceable coordinate. A `q` tag marks a quote inside some other event so thread reconstruction can count citations without treating the quoting event as a reply, which is the split drawn in the [quote-repost section](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts). A kind 7 event leaves the original event in place and attaches only the reaction value plus target tags, which is the contract in the [reaction specification](https://github.com/nostr-protocol/nips/blob/master/25.md). Clients that fetch one pubkey therefore see that pubkey's reposts as new kind 6 or 16 events and that pubkey's opinions as kind 7 events on other people's posts.

---

Send a NIP-17 DM to share a project or news item through the [Nostr Compass project](https://github.com/andotherstuff/nostr-compass).
