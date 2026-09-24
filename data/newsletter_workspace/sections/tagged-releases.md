## Tagged Releases

### White Noise Android 2026.9.21 improves encrypted-chat reliability and sharing

[White Noise Android](https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.21) is a Nostr-based messenger for private Marmot-encrypted group conversations. Its September 21 release improves message delivery, voice dictation, text-to-speech, conversation navigation, account switching, and AMOLED appearance. It also adds shareable profile and invite QR cards and group actions from profiles.

### Nostr Mail Client 0.16.0 adds per-recipient delivery choices

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client) is a web, desktop, and Android mail client that exchanges messages through Nostr relays while supporting conventional email delivery. [Version 0.16.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.16.0) lets a sender choose SMTP or Nostr delivery for each recipient and strips location, capture time, and device metadata from photos and videos before upload.

The [release](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.16.0) also requires every account to establish a relay list, keeps at least one relay configured, and adds safer permanent deletion from trash. Those changes make routing and attachment privacy explicit at the point where a mixed email/Nostr message leaves the device.

### Amber 6.6.5 separates backup encryption from app permissions

[Amber](https://github.com/greenart7c3/Amber) is an Android signer that keeps Nostr private keys outside the applications requesting signatures or encryption. NIP-44 standardizes encrypted payloads between Nostr keys, while NIP-46 lets an application request signing and encryption from a remote signer over relays. [Version 6.6.5](https://github.com/greenart7c3/Amber/releases/tag/v6.6.5) encrypts application backups with a dedicated key derived from the account key, preventing an application with remembered NIP-44 decryption permission from reading backup payloads that contain local keys or per-app NIP-46 secrets.

The [migration path](https://github.com/greenart7c3/Amber/releases/tag/v6.6.5) can still restore older identity-encrypted backups until the next publish replaces them, and the release fixes a restore prompt that disappeared after logout when backup publishing was disabled. Users receive both a tighter permission boundary and a recovery path for existing backups.

### Amethyst 1.16.0 hardens Blossom signing and adds BOLT12 offers

[Amethyst](https://github.com/vitorpamplona/amethyst) is an Android Nostr client with media, wallet, and signer integrations. [Version 1.16.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.16.0) fixes fast Blossom read authorization so concurrent media requests share one in-flight signer operation and recheck the token cache before asking for another signature. The tagged release also restores standard padded Base64 for Blossom auth tokens.

[Version 1.16.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.16.0) also supports BOLT12 offers in profile payments and the zap picker, with BOLT11 fallback when an offer is refused. Users gain an offer-based payment path while existing invoice-based payments remain available.

### Alby Extension 3.15.0 hardens website-initiated requests

[Alby Extension](https://github.com/getAlby/lightning-browser-extension) is a browser wallet and Nostr signer that grants websites scoped Lightning and signing capabilities. [Version 3.15.0](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.15.0) blocks website-supplied LNURLs from local or private network addresses, requires cross-host LNURL-auth confirmation, and removes remembered approval for raw Schnorr-signing methods.

The [security release](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.15.0) also debits allowance budgets before sending concurrent payments and removes the generic WebLN request method. Integrators must use dedicated WebLN methods, while users gain clearer boundaries around network targets, authentication hosts, and site spending limits.

### LaWallet NWC 2.7.1 unifies zap receipts across wallets

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) is an open-source Lightning wallet service that exposes accounts to applications through Nostr Wallet Connect. NIP-57 standardizes signed Lightning zap requests and settlement receipts for Nostr profiles and events. [Version 2.7.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.7.0) decouples that receipt publication from wallet-specific settlement paths so every supported NWC wallet can emit zap receipts, then [2.7.1](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.7.1) brings receive and activity screens onto the same receipt flow as sends.

The [2.7.1 package](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.7.1) also aligns StartOS storage and backup layout between sideload and community packages. Operators upgrading the first 2.7.0 sideload need the corrected package before relying on the database volume transition.

### NoorNote 1.6.0–1.7.0 adds calendars and booking

[NoorNote](https://github.com/77elements/noornote) is a Nostr notes application with optional productivity modules and local reminders. [Version 1.6.0](https://github.com/77elements/noornote/releases/tag/v1.6.0) adds public and encrypted calendar events, month, week, and list views, Android reminders, and interactive timeline cards for shared events.

[Version 1.6.1](https://github.com/77elements/noornote/releases/tag/v1.6.1) reorganizes addons into a per-account dashboard and fixes URLs containing `naddr` or `npub` identifiers being misread as cards or mentions. These fixes make addon controls easier to find and keep Nostr identifiers intact inside ordinary links.

[Version 1.7.0](https://github.com/77elements/noornote/releases/tag/v1.7.0) lets an account share available appointment slots and receive bookings and cancellations by direct message. It also imports and exports calendar data as `.ics`, preserves the web NWC wallet connection after IndexedDB eviction, and avoids false mentions in links containing npubs.

### Citrine 3.2.0 bounds relay-aggregator memory

[Citrine](https://github.com/greenart7c3/Citrine) is an Android Nostr relay that gives other applications a local event store and relay interface. [Version 3.2.0](https://github.com/greenart7c3/Citrine/releases/tag/v3.2.0) streams matching events in batches, caps aggregator fan-out at 200 relays, and bounds caches to prevent large queries from exhausting memory.

The [release](https://github.com/greenart7c3/Citrine/releases/tag/v3.2.0) also exposes out-of-memory failures in the in-app log and lets operators hide the event graph. A phone acting as both relay and aggregator now fails more visibly and holds a defined memory boundary.

### Wisp 1.2.4 routes threads through inbox relays

[Wisp](https://github.com/barrydeen/wisp) is a privacy-oriented Nostr client with built-in Cashu and Lightning wallet support. NIP-22 defines generic kind `1111` comments that can reply to many kinds of Nostr content. [Version 1.2.4](https://github.com/barrydeen/wisp/releases/tag/v1.2.4) sends thread and notification reads only to inbox relays, treats those comments as replies, and lets users withdraw their full wallet balance on chain.

[Version 1.2.4](https://github.com/barrydeen/wisp/releases/tag/v1.2.4) limits thread reads to inbox relays, reducing unnecessary relay exposure. Its NIP-22 handling keeps comments visible in threads, counts, and notifications.

### nostr-wot-extension 0.8.3 adds scoped NWC connections

[nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension) is a browser signer and identity extension with wallet payments and local web-of-trust analysis. [Version 0.8.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.0) restores its experimental web-of-trust API as a menu-only opt-in with local, remote, and hybrid query modes, scalable graph synchronization, mute-aware scoring, and per-account storage controls.

The [release](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.0) also requires confirmation before replacing a known follow list with zero or one contact, even when a saved permission or remote signer is present. That guard uses verified relay, signed-event, and synchronized graph history to make destructive follow-list changes harder to approve silently.

[Version 0.8.3](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.3) creates separate Nostr Wallet Connect connections for applications using its LNbits wallet. Each can have a name, daily spending limit, and expiry, with local secret storage, budget visibility, and revocation. The project's live test covered connection creation, revocation, and a signed `get_info` exchange, not a real payment; browser-store publication is separate from the source release.

### pakstr 0.22.0–0.24.0 adds Android signer handoff

[pakstr](https://git.nostrdev.com/stuff/pakstr) packages web applications with native Nostr capabilities. Last week's issue covered its 0.21.x packaging sequence. The new [0.22.0 release](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.22.0) adds NIP-55 signing through the NIP-46 bunker, letting an Android application hand signing requests to an external signer. [Version 0.23.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.23.0) then persists the runtime API address across restarts.

[Version 0.24.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.24.0) publishes the Zapstore icon; that cosmetic change is not the signer milestone. NostrAppShell entries point to the same package series, so they are covered here once.

### Nail 0.2.2 makes mail attachments fail soft

[Nail](https://github.com/formstr-hq/nail) is a bridge and application that carries Nostr messages into email workflows. [Version 0.2.2](https://github.com/formstr-hq/nail/releases/tag/v0.2.2) retries a message without attachments when a relay refuses the attachment payload, adds a size ceiling to prevent bridge restarts, and changes the default bridge relay.

The [application update](https://github.com/formstr-hq/nail/releases/tag/v0.2.2) also restores link opening and opt-in image viewing. Delivery can now degrade to the message body instead of losing the entire email when its attachment path fails.

### Mostro CLI 0.16.2 removes its legacy chat transport

[Mostro CLI](https://github.com/MostroP2P/mostro-cli) is a terminal client for coordinating peer-to-peer Bitcoin trades through Mostro's Nostr protocol. [Version 0.16.2](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.2) removes the version-one gift-wrap dual-read and dual-write path, migrates peer chat to the current envelope, and lets a trader reach the solver through dispute chat.

The [release](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.2) also adds an operator command for cancelling pending orders. Deployments should update client and coordinator expectations together because the old chat transport is no longer a fallback.

### Dart NDK dev.4–dev.5 adds signed app updates and hardens relay delivery

[Dart NDK](https://github.com/relaystr/ndk) is a Dart client library for relay connections, signing, caching, wallet operations, and Nostr application state. NIP-82 standardizes signed application-release metadata and downloadable artifacts. [Version 0.10.0-dev.4](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.4) adds NIP-82 application-update support; [dev.5](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.5) makes Cashu quote recovery resumable and lets a broadcast declare the identity to which it may be attributed.

Across [the dev.5 release](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.5), the library avoids anonymous connections when a broadcast requires authentication and stops waking relays for deliveries parked on a missing identity. Applications adopting this prerelease should allow for migration work in their broadcast and wallet integrations.

### BitBlik 0.11.0 brings disputes into the app

[BitBlik](https://github.com/bit-blik/bitblik) is a mobile peer-to-peer Bitcoin trading client that coordinates orders and chat over Nostr. [Version 0.11.0](https://github.com/bit-blik/bitblik/releases/tag/v0.11.0) adds coordinator dispute chat, BOLT12 payouts where supported, Android self-updates sourced from NIP-82 release events, and wallet backup and recovery fixes.

The [release](https://github.com/bit-blik/bitblik/releases/tag/v0.11.0) also handles refunds after dispute rulings and preserves wallet state during Neko recovery. Traders can now remain inside the client for the dispute conversation instead of switching to a separate coordinator channel.

### Scramble 0.7.2 changes MLS engines and offers two Android views

[Scramble](https://github.com/DavidGershony/Scramble) is a Nostr-based encrypted group-chat application. Its [0.7.0 release](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.0) replaces the former MLS engine with Dark Matter, restores encryption at rest for group state, and prevents Android cloud backup of the profile database. The migration has an important limit: groups created in 0.6.x do **not** appear after upgrading, although the account key, contacts, relays, and signer pairing remain.

[Version 0.7.2](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.2) ships Avalonia and native Android view layers with the same app ID and release certificate, so one can install over the other without clearing the new-engine account and chats. They cannot be installed side by side. The native view still lacks some device-management settings; the project's release notes say protocol interop is tested but do not claim a real-device group conversation test for the 0.7.0 migration.

### Morganite 0.0.5 makes onion Blossom media seekable

[Morganite](https://github.com/greenart7c3/Morganite) is an Android Blossom media cache for Nostr clients. [Version 0.0.5](https://github.com/greenart7c3/Morganite/releases/tag/v0.0.5) fetches blobs from Tor `.onion` Blossom servers with Tor-aware retries and honors HTTP Range requests on a cache miss. A player can seek into an uncached video while Morganite fills the full cache in the background instead of storing only disjoint requested slices.

### Bitcredit 0.5.16 recovers stalled Nostr bill events

[Bitcredit E-Bills](https://github.com/BitcreditProtocol/Bitcredit-Core) carries bill, company, and identity chains through Nostr events. [Version 0.5.16](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.16) repairs event-signature serialization compatibility after its Nostr 0.45 dependency upgrade, exposes failed resend-queue entries for inspection and requeue, and resynchronizes missing chain metadata before retrying a block publication. Those changes target both upgraded-data compatibility and messages that would otherwise remain stuck.

### fips-ts 0.0.43 protects concurrent FIPS sessions

[fips-ts](https://github.com/mmalmi/fips-ts) supplies the shared TypeScript FIPS mesh runtime used by compatible clients. Its [runtime 0.0.43 release](https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.43) preserves an authenticated identity when concurrent setup or an aliased WebRTC transport hands a session over, while rejecting a different identity. It also prevents canceled negotiations and late callbacks from replacing a working connection. This is library-level connection reliability, separate from fips2go's client-side bootstrap and discovery changes.

### Bookshelf 0.1.25 makes signed book reviews editable

[Bookshelf](https://github.com/decent-newsroom/bookshelf-app) is a Nostr-connected Android reader with community book ratings and private highlights. [Version 0.1.25](https://github.com/decent-newsroom/bookshelf-app/releases/tag/v0.1.25) lets readers revise their signed rating and written review through a durable outbox. The app displays cached ratings immediately, refreshes them online, and replaces older revisions by the newest event for the same book and author.

The [release diff](https://github.com/decent-newsroom/bookshelf-app/compare/v0.1.24...v0.1.25) includes the review editor, revision cache, relay synchronization, and tests. It also normalizes pasted `nostr:naddr` references before searching for a book's publication coordinates.

### Cordn 0.5.0 queues encrypted messages offline

[Cordn](https://github.com/Cordn-msg/cordn-web) is an encrypted Nostr group-chat client. [Version 0.5.0](https://github.com/Cordn-msg/cordn-web/releases/tag/v0.5.0) queues text sends in a durable offline outbox, makes failed entries terminal until a successful confirmation sweep, and resumes coordinator chats in order. It also checks a signer's NIP-44 capability before offering an encrypted action, surfacing unsupported signers instead of failing silently.

### 21Meetup 1.6.6 restores multi-hop trust paths

[21Meetup](https://github.com/louisthecat86/Einundzwanzig-Meetup-App) issues Nostr-backed attendance badges for in-person events. [Version 1.6.6](https://github.com/louisthecat86/Einundzwanzig-Meetup-App/releases/tag/v1.6.6) restores second- and third-degree trust paths by fetching contacts' meetup records in bounded stages. Failed badge publications can be retried, and a send counts as successful only after a relay acknowledges it. Multi-day events now count as one attendance badge instead of one per day.

### TWENTY ONE Companion 1.13.0 explains public Nostr RSVPs

[TWENTY ONE Companion](https://github.com/HolgerHatGarKeineNode/twenty-one-companion) combines Nostr rooms and articles with meetup listings. [Version 1.13.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.13.0) saves pinned rooms and articles to relays, showing a pin as local until a relay confirms it. Eligible meetup RSVPs are signed public Nostr events; the app warns that third-party relays may retain them even after a user declines. A contact-list preview now refuses to publish if the list changed after review.

### Armada 0.61.0 adds media privacy and member controls

[Armada](https://github.com/soapbox-pub/armada) is a Nostr-based encrypted community client. [Version 0.61.0](https://primal.net/e/122a06dbab02d207b3aa793b0fedd06fd59d36178a7b9ae5971cfc3b7f3eb6ce) adds an opt-in image proxy list so a sender's media host need not learn a reader's address. Staff can kick, ban, or unban a member from a profile card, and a private-channel key granted with a role now applies without a separate invite. The proxy is off by default; operators choose and rotate their own servers.

### Ditto 2.40.0 brings Top 8 rankings to Nostr profiles

[Ditto](https://gitlab.com/soapbox-pub/ditto) is a social client on Nostr. [Version 2.40.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.40.0) lets a user rank eight favorite people on their profile. Reordering stays local until Save, then the ranked list appears on the profile and its update can appear as a card in followers' feeds. That turns a profile preference into a shared social-graph signal with an explicit publish step.

### XM Arcade 1.1.3 binds mini-app approval to one run

[XM Arcade](https://gitworkshop.dev/r/xm-arcade) runs small games and mini-apps within a Nostr group context. [Version 1.1.3](https://primal.net/e/dec0edda9ff464b4b7598032318cb48e17cf496e29d05031d1f1629409039a4c) binds a post approval to an opaque run token, the request, app, account, group, and channel. Expired or replayed approvals no longer authorize another mini-app run. The update also persists trusted group-key epoch state across restart.

### Zzub 0.0.15–0.0.16 expands mobile project boards

[Zzub](https://primal.net/e/70c5efeea2e9314329b8951346d83ad0688b74607a108e8bc820caae545196c2) is a Nostr-based project and code-review client. Its 0.0.15 release adds status columns, sorting and filtering, threaded comments, named assignees, and approve or request-changes actions to its phone boards. A built-in Git client opens source and files-changed diffs from a pull-request card, bringing the existing desktop review flow onto the phone.

[Version 0.0.16](https://primal.net/e/d9ad994bfadc1152b4c77a4fd3eb6be1746eca9d2626008d341bf31d06988872) restores the full announced Projects list after the previous device-local scoping hid it. The release adds an @mention selector to card comments, shows mentions as chips, and gives the project screen Tasks and Reviews tabs spanning all its repositories while keeping per-repository boards available. It also adds repository and status filters and lifts the comment box above Android navigation.

### Table Mesh 0.1.0 brings Nostr game discovery to offline board games

[Table Mesh 0.1.0](https://primal.net/e/c5c5ad0eba413e18c10e3cd2be607e550ac818a8abaf97ccbf8fa242fbaff15f) is a first Android release for playing board games across nearby phones over Bluetooth and local Wi-Fi. It includes *Mensch ärgere Dich nicht* and solo bots. A Nostr kind-7529 catalog distributes additional sandboxed game modules through Blossom, with downloaded bytes checked against their announced hashes.

The [app listing](https://zapstore.dev/apps/org.tablemesh.app) describes the Bluetooth mesh as tested in simulation and emulators, not yet at real multi-phone tables. The table session itself runs locally without an internet connection or account; Nostr does not carry its moves.

writer_model: preferred=gemini-3.1-pro, actual=openai-codex/gpt-5.6-sol, receipt=data/newsletter_workspace/writer_receipt_2026-09-16.json

GATE: PENDING REVIEW
