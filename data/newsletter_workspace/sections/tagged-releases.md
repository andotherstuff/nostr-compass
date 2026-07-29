## Tagged Releases

### Mafrend v1.0 previews place-based Nostr chat on Android

[Mafrend v1.0](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.0) is the first public Android alpha of a planned place-based Nostr chat app. Its [project page](https://mafrend.com) labels the feature set as still in active development and describes each map location as a dedicated chat room for conversations around a place. A public release repository carries the installable Zapstore package while the main app remains private.

### Hanami 0.1.0 gives Blossom servers a signer-mediated Android path

[Hanami 0.1.0](https://github.com/Letdown2491/hanami-android/releases/tag/v0.1.0), an Android companion for [Blossom](/en/topics/blossom/) servers, lets people sign in, upload, and download from a phone. The app uses [NIP-55 (Android Signer Application)](/en/topics/nip-55/) for approval-mediated signing and a native [NIP-98 (HTTP Auth)](/en/topics/nip-98/) handshake for the server session. Its web shell and signing bridge are locked to the chosen server origin, keeping credentials with the signer while the server's existing web interface supplies the application experience. The first public release requires Android 8 or later, a reachable Hanami server, and a compatible signer app.

### Cordn launches its Nostr-identity group chat on Android

Cordn, a private group-messaging client, now gives Android users Nostr identity onboarding, profile links through [NIP-05 (Mapping Nostr Keys to DNS-Based Internet Identifiers)](/en/topics/nip-05/), and verified links that open Cordn destinations in the app. The [0.2.1 release published July 24](https://github.com/Cordn-msg/cordn-web/releases/tag/v0.2.1) introduces that native line alongside the existing web client. Messages use [MLS](/en/topics/mls/), a group-encryption protocol, with coordinator-assisted delivery, so groups retain ordered encrypted conversations without requiring an email address or phone number.

### Nostur 1.30.1 tightens sharing, threads, and duplicate-post protection

[Nostur 1.30.1](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.30.1), a Nostr client for iPhone, iPad, and Mac, lets people work through nested reply threads without the expansion and collapse failures that disrupted the new layout. It also prevents the same draft from publishing twice, including when media-upload callbacks repeat. The release follows [1.30.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.30.0), which added disappearing direct messages and a share-sheet route for sending media into Nostr, so the app now pairs new messaging and publishing paths with fixes to their everyday thread and posting flows.

### Formstr Drive 0.0.2 pairs Nostr file metadata with Blossom blobs

[Formstr Drive 0.0.2](https://github.com/formstr-hq/formstr-drive/releases/tag/v0.0.2), a Nostr-native file manager, gives users in-app previews and the option to open office documents in Nostr Docs. Underneath, it adds chunked [Blossom](/en/topics/blossom/) storage, the blob-server layer for Nostr media, plus deletion that removes the remote blob when a user removes a file. A local relay keeps the app's Nostr metadata close at hand while Blossom holds the file data, separating file organization from the large bytes themselves.

### NoorNote 1.3.0

[NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0), a Nostr client for web, desktop, and Android, now renders [NIP-53 (live activities)](/en/topics/nip-53/) as live cards across timelines, reposts, bookmarks, and notifications, so a stream stays recognizable wherever its event appears. Image posts can tag people through [NIP-68 (Picture-first feeds)](/en/topics/nip-68/), while a [NIP-78 (application-data)](/en/topics/nip-78/) soft mute suppresses a person's notification activity without removing their posts from the feed. The release also shows which relays have seen a note, giving readers a direct view of its relay distribution.

### algia 0.0.133

[algia 0.0.133](https://github.com/mattn/algia/releases/tag/v0.0.133), a Go command-line client for Nostr, follows [0.0.132](https://github.com/mattn/algia/releases/tag/v0.0.132), which added [NIP-29 (Relay-based Groups)](/en/topics/nip-29/) listing, timelines, posting, reactions, deletions, and join and leave flows. The same release added [NIP-42 (Authentication of clients to relays)](/en/topics/nip-42/) pre-authentication for relays configured to require it. Version 0.0.133 then added local-image uploads to regular, channel, and group posting commands, attaching the resulting URLs and [NIP-92 (Media Attachments)](/en/topics/nip-92/) tags to each event. Image-only posts work as well, and group posts target the group's relay media store by default while other posts use configured file servers.

### swift-nostr 0.7.0

For Swift applications, [swift-nostr 0.7.0](https://github.com/yysskk/swift-nostr/releases/tag/0.7.0), a Nostr library for Apple platforms, lets one [NIP-46 remote signer](/en/topics/nip-46/) drive every client feature through its signing abstraction. The release adds [NIP-98 (HTTP Auth)](/en/topics/nip-98/) and [NIP-29 (Relay-based Groups)](/en/topics/nip-29/) support, including group joining, posting, and moderation flows. It also validates [NIP-44 (Encrypted Payloads, Versioned)](/en/topics/nip-44/) padding against the official vectors, rejecting payloads that carry a valid MAC over noncanonical padding.

### lawallet-nwc 2.0.0

[LaWallet NWC 2.0.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.0.0), a Nostr-connected wallet and [NIP-47 (Nostr Wallet Connect)](/en/topics/nip-47/) service, adds passkey login that derives the Nostr signing key in the browser with the WebAuthn PRF extension. The server never receives that secret, and the same passkey can recover the same key on another synced device. Accounts can now link and merge multiple Nostr pubkeys, while the optional listener service relays wallet-connect events and retries webhook delivery after an unreachable endpoint.

### MDK 0.9.9

[MDK 0.9.9](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.9), the Rust implementation of the [Marmot protocol](/en/topics/marmot/), now preserves a user's manual order for pinned chats, so an intentional chat layout survives later updates. It also adds terminal group disbanding for encrypted groups that have reached their end of life. Agent integrations receive richer inbound context, including reply and ambient group information, so they can respond with the surrounding conversation state available.

### pakstr 0.3.1

[pakstr 0.3.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.3.1) lets web teams packaging a Nostr client for Android supply runtime configuration and an API proxy without rebuilding the app shell. Its [same-day release series](https://git.nostrdev.com/stuff/pakstr/releases) added an Amber signer bridge, [NIP-44 (encrypted payloads)](/en/topics/nip-44/) encryption and decryption, and corrected Android permission injection before the 0.3.x runtime-configuration work. The scaffold keeps bundled web assets local while deployment-specific settings arrive at runtime, and the proxy gives the wrapped app a controlled route for API requests alongside its ordinary relay connections.

### Ditto 2.34.1

[Ditto 2.34.1](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.34.1), a customizable Nostr social client, now places a globe button on a profile when its owner has published a [NIP-5A (website manifest)](/en/topics/nip-5a/) root site. Selecting it opens that site's content inside Ditto, so readers can visit a profile owner's published site without leaving the feed. The button appears only when the root-site event includes published paths to serve.

### Earthly 0.0.9

[Earthly 0.0.9](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.0.9), a collaborative map editor built on Nostr, now keeps likes visible when a map entity drawer closes, reopens, or refreshes. Its [NIP-57 (Lightning zaps)](/en/topics/nip-57/) flow sends valid zap-request JSON so Lightning providers can publish verified receipts to publicly reachable relays, including during local development. Generated invoices remain visible across entity-surface changes, and the app shows confirmation after a verified receipt arrives.

GATE: PASS (Stage 7 revised-draft review: all five evidence-bearing gates pass 2026-07-29T05:28:27Z)
