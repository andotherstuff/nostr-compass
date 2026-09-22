## Tagged Releases

### Nostr Mail Client 0.16.0 adds per-recipient delivery choices

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client) is a web, desktop, and Android mail client that exchanges messages through Nostr relays while supporting conventional email delivery. [Version 0.16.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.16.0) lets a sender choose SMTP or Nostr delivery for each recipient and strips location, capture time, and device metadata from photos and videos before upload.

The [release](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.16.0) also requires every account to establish a relay list, keeps at least one relay configured, and adds safer permanent deletion from trash. Those changes make routing and attachment privacy explicit at the point where a mixed email/Nostr message leaves the device.

### Amber 6.6.5 separates backup encryption from app permissions

[Amber](https://github.com/greenart7c3/Amber) is an Android signer that keeps Nostr private keys outside the applications requesting signatures or encryption. NIP-44 standardizes encrypted payloads between Nostr keys, while NIP-46 lets an application request signing and encryption from a remote signer over relays. [Version 6.6.5](https://github.com/greenart7c3/Amber/releases/tag/v6.6.5) encrypts application backups with a dedicated key derived from the account key, preventing an application with remembered NIP-44 decryption permission from reading backup payloads that contain local keys or per-app NIP-46 secrets.

The [migration path](https://github.com/greenart7c3/Amber/releases/tag/v6.6.5) can still restore older identity-encrypted backups until the next publish replaces them, and the release fixes a restore prompt that disappeared after logout when backup publishing was disabled. Users receive both a tighter permission boundary and a recovery path for existing backups.

### Amethyst 1.16.0 expands video, calendars, and geocaching

[Amethyst](https://github.com/vitorpamplona/amethyst) is a feature-rich Android Nostr client with social, media, wallet, and signer integrations. NIP-71 standardizes video events, NIP-51 defines user-curated lists, NIP-CC defines geocache records, and NIP-52 defines calendar events and responses. [Version 1.16.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.16.0) adds interoperability across those four event families and attaches relay hints to calendar responses.

The [release series](https://github.com/vitorpamplona/amethyst/releases/tag/v1.16.0) also adds BOLT12 offers with BOLT11 fallback, improves notification replies and deep links, and keeps QR key material off screen and out of logs. That mix broadens the event types users can act on while tightening sensitive scanner behavior.

### Alby Extension 3.15.0 hardens website-initiated requests

[Alby Extension](https://github.com/getAlby/lightning-browser-extension) is a browser wallet and Nostr signer that grants websites scoped Lightning and signing capabilities. [Version 3.15.0](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.15.0) blocks website-supplied LNURLs from local or private network addresses, requires cross-host LNURL-auth confirmation, and removes remembered approval for raw Schnorr-signing methods.

The [security release](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.15.0) also debits allowance budgets before sending concurrent payments and removes the generic WebLN request method. Integrators must use dedicated WebLN methods, while users gain clearer boundaries around network targets, authentication hosts, and site spending limits.

### LaWallet NWC 2.7.1 unifies zap receipts across wallets

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) is an open-source Lightning wallet service that exposes accounts to applications through Nostr Wallet Connect. NIP-57 standardizes signed Lightning zap requests and settlement receipts for Nostr profiles and events. [Version 2.7.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.7.0) decouples that receipt publication from wallet-specific settlement paths so every supported NWC wallet can emit zap receipts, then [2.7.1](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.7.1) brings receive and activity screens onto the same receipt flow as sends.

The [2.7.1 package](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.7.1) also aligns StartOS storage and backup layout between sideload and community packages. Operators upgrading the first 2.7.0 sideload need the corrected package before relying on the database volume transition.

### NoorNote 1.6.1 adds encrypted calendars

[NoorNote](https://github.com/77elements/noornote) is a Nostr notes application with optional productivity modules and local reminders. [Version 1.6.0](https://github.com/77elements/noornote/releases/tag/v1.6.0) adds public and encrypted calendar events, month, week, and list views, Android reminders, and interactive timeline cards for shared events.

[Version 1.6.1](https://github.com/77elements/noornote/releases/tag/v1.6.1) reorganizes addons into a per-account dashboard and fixes URLs containing `naddr` or `npub` identifiers being misread as cards or mentions. The release turns calendar data into a usable Nostr workflow while repairing identifier parsing in ordinary notes.

### Citrine 3.2.0 bounds relay-aggregator memory

[Citrine](https://github.com/greenart7c3/Citrine) is an Android Nostr relay that gives other applications a local event store and relay interface. [Version 3.2.0](https://github.com/greenart7c3/Citrine/releases/tag/v3.2.0) streams matching events in batches, caps aggregator fan-out at 200 relays, and bounds caches to prevent large queries from exhausting memory.

The [release](https://github.com/greenart7c3/Citrine/releases/tag/v3.2.0) also exposes out-of-memory failures in the in-app log and lets operators hide the event graph. A phone acting as both relay and aggregator now fails more visibly and holds a defined memory boundary.

### Wisp 1.2.5 routes threads through inbox relays

[Wisp](https://github.com/barrydeen/wisp) is a privacy-oriented Nostr client with built-in Cashu and Lightning wallet support. NIP-22 defines generic kind `1111` comments that can reply to many kinds of Nostr content. [Version 1.2.4](https://github.com/barrydeen/wisp/releases/tag/v1.2.4) sends thread and notification reads only to inbox relays, treats those comments as replies, and lets users withdraw their full wallet balance on chain.

[Version 1.2.5](https://github.com/barrydeen/wisp/releases/tag/v1.2.5) packages the follow-up release after those changes. Inbox-only routing reduces unnecessary relay exposure while the comment handling keeps NIP-22 conversations visible in threads, counts, and notifications.

### nostr-wot-extension 0.8.0 restores opt-in graph queries

[nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension) is a browser signer and identity extension with wallet payments and local web-of-trust analysis. [Version 0.8.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.0) restores its experimental web-of-trust API as a menu-only opt-in with local, remote, and hybrid query modes, scalable graph synchronization, mute-aware scoring, and per-account storage controls.

The [release](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.0) also requires confirmation before replacing a known follow list with zero or one contact, even when a saved permission or remote signer is present. That guard uses verified relay, signed-event, and synchronized graph history to make destructive follow-list changes harder to approve silently.

### pakstr 0.24.0 expands its Android Nostr runtime

[pakstr](https://git.nostrdev.com/stuff/pakstr) is a packaging system and application shell for distributing web applications with native Nostr capabilities. NIP-46 defines remote-signer sessions, NIP-98 defines signed HTTP authentication, and NIP-55 lets Android applications request signatures from an external signer. [Versions 0.21.0 through 0.24.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.24.0) add production bunker pairing, proxied authenticated requests, external signing through a bunker, a persistent Android API endpoint, and Zapstore icons.

The [release sequence](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.24.0) also repairs invalid-relay cleanup and Amber pairing. NostrAppShell entries point to the same package series, so they are one implementation and are covered here once.

### Nail 0.2.2 makes mail attachments fail soft

[Nail](https://github.com/formstr-hq/nail) is a bridge and application that carries Nostr messages into email workflows. [Version 0.2.2](https://github.com/formstr-hq/nail/releases/tag/v0.2.2) retries a message without attachments when a relay refuses the attachment payload, adds a size ceiling to prevent bridge restarts, and changes the default bridge relay.

The [application update](https://github.com/formstr-hq/nail/releases/tag/v0.2.2) also restores link opening and opt-in image viewing. Delivery can now degrade to the message body instead of losing the entire email when its attachment path fails.

### Mostro CLI 0.16.2 removes its legacy chat transport

[Mostro CLI](https://github.com/MostroP2P/mostro-cli) is a terminal client for coordinating peer-to-peer Bitcoin trades through Mostro's Nostr protocol. [Version 0.16.2](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.2) removes the version-one gift-wrap dual-read and dual-write path, migrates peer chat to the current envelope, and lets a trader reach the solver through dispute chat.

The [release](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.2) also adds an operator command for cancelling pending orders. Deployments should update client and coordinator expectations together because the old chat transport is no longer a fallback.

### Dart NDK dev.5 adds signed app-update releases

[Dart NDK](https://github.com/relaystr/ndk) is a Dart client library for relay connections, signing, caching, wallet operations, and Nostr application state. NIP-82 standardizes signed application-release metadata and downloadable artifacts. [Version 0.10.0-dev.5](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.5) adds those application-update events, while the preceding development release makes Cashu quote recovery resumable and lets a broadcast declare the identity to which it may be attributed.

The [development series](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.5) also avoids anonymous connections when a broadcast requires authentication and stops waking relays for deliveries parked on a missing identity. The prerelease label still signals migration risk for applications adopting the new broadcast and wallet behavior.

### BitBlik 0.11.0 brings disputes into the app

[BitBlik](https://github.com/bit-blik/bitblik) is a mobile peer-to-peer Bitcoin trading client that coordinates orders and chat over Nostr. [Version 0.11.0](https://github.com/bit-blik/bitblik/releases/tag/v0.11.0) adds coordinator dispute chat, BOLT12 payouts where supported, Android self-updates sourced from NIP-82 release events, and wallet backup and recovery fixes.

The [release](https://github.com/bit-blik/bitblik/releases/tag/v0.11.0) also handles refunds after dispute rulings and preserves wallet state during Neko recovery. Traders can now remain inside the client for the dispute conversation instead of switching to a separate coordinator channel.

writer_model: preferred=gemini-3.1-pro, actual=openai-codex/gpt-5.6-sol, receipt=data/newsletter_workspace/writer_receipt_2026-09-16.json

GATE: PENDING REVIEW
