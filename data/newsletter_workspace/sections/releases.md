## Tagged Releases

### nostr-relay 0.0.251 through 0.0.260 adds proof-of-work checks, union counting, and operator metrics

[nostr-relay](https://github.com/mattn/nostr-relay) is a relay written in Go that stores events in SQLite, PostgreSQL, or MySQL. The sequence from [0.0.251](https://github.com/mattn/nostr-relay/releases/tag/v0.0.251) to [0.0.260](https://github.com/mattn/nostr-relay/releases/tag/v0.0.260) validates [NIP-13](/en/topics/nip-13/) (proof of work) difficulty on incoming events, so an operator can require submitters to spend work before a write is accepted, and it corrects [NIP-45](/en/topics/nip-45/) (event counting) so a `COUNT` across several filters reports the union of matching events instead of a sum that double-counts.

The [same release sequence](https://github.com/mattn/nostr-relay/releases/tag/v0.0.260) now advertises the NIPs the relay supports in its relay-information document, which lets clients decide what to attempt before they try it, and exposes Go runtime metrics plus an endpoint that returns free memory to the operating system. That last pair gives operators both a view of allocation behavior and a way to hand reclaimed memory back to the host without restarting the relay.

### Jumble 26.9.2 shows favorite relay lists and stops queries stalling on dead sockets

Opening a profile in [Jumble](https://github.com/CodyTseng/jumble), a web client built around browsing relay feeds, now shows the relays that account marks as favorites. [Version 26.9.2](https://github.com/CodyTseng/jumble/releases/tag/v26.9.2) reads and displays `kind:10012` favorite relay lists, which turns another user's relay preferences into a place to browse instead of a value hidden in their event history.

The [same release](https://github.com/CodyTseng/jumble/releases/tag/v26.9.2) fixes a failure mode that looked like an empty feed. Queries issued against a relay whose socket connection failed were left pending, so the interface kept waiting on a request that could never be answered; those queries are now resolved when the connection fails, and the surrounding view can move on or retry.

### NoorNote 1.5.0 through 1.5.2 tracks unread bookmarks and adds undo to reactions

[NoorNote](https://github.com/77elements/noornote) is a Nostr client for notes, messages, and long-form articles on web, desktop, and Android. [Version 1.5.0](https://github.com/77elements/noornote/releases/tag/v1.5.0) makes bookmarks a reading queue: saved items carry unread state, and that state can be synchronized between devices through optional encrypted sync, so a note bookmarked on a phone is still marked unread on a desktop.

Reactions became reversible in the same line. Likes and reposts can now be undone from the interface, which matters because both are published events and an accidental one is otherwise visible to everyone who reads the author's feed. [Version 1.5.1](https://github.com/77elements/noornote/releases/tag/v1.5.1) and [version 1.5.2](https://github.com/77elements/noornote/releases/tag/v1.5.2) extend live zap and like updates to long-form articles, so an article page updates as the reactions arrive, and add a clean unlock card for gated premium notes, so a reader sees what the note requires before the content appears.

### Chama 6.2.0 through 6.3.3 separates wallet storage and recovers from stalled sockets

[Chama](https://github.com/jesuspirate/chama) is a Nostr-native peer-to-peer escrow client that holds funds in Fedimint ecash. [Version 6.2.0](https://github.com/jesuspirate/chama/releases/tag/v6.2.0) separates wallet storage by federation and by identity, so two identities or two federations on one device no longer share a single store, and a returning session recovers correctly instead of resuming against the wrong state.

Mobile publishing is the other repair. Through [version 6.3.3](https://github.com/jesuspirate/chama/releases/tag/v6.3.3), a phone that resumes with a socket the operating system has already abandoned cycles its relay connection pool and resends the same signed event once, so a trade action taken after the screen wakes reaches relays instead of silently failing. Resending the identical signed event, and only once, keeps the retry from turning one trade action into two records.

### Mostro Mobile 1.4.1 and 1.4.2 keep range orders and chats alive across restarts

[Mostro Mobile](https://github.com/MostroP2P/mobile) is the mobile client for the Mostro peer-to-peer exchange, which coordinates orders and trade chat over Nostr. [Version 1.4.1](https://github.com/MostroP2P/mobile/releases/tag/v1.4.1) persists the pending child sessions of a range order across process isolates and app restarts, so a partially filled range order survives the app being backgrounded or killed, and it reissues open relay subscriptions after a reconnection so the trade keeps receiving events.

Trade chat received two fixes in [version 1.4.2](https://github.com/MostroP2P/mobile/releases/tag/v1.4.2). Duplicate chat rooms for the same counterparty are repaired, which removes the case where two threads held halves of one conversation, and tapping a chat notification now opens the conversation directly instead of dropping the user at a list to find it again.

### Dart NDK 0.9.2 and 0.9.3 add DM relay discovery and NIP-17 file messages

[Dart NDK](https://github.com/relaystr/ndk) is the Nostr development kit for Dart and Flutter applications. [Version 0.9.2](https://github.com/relaystr/ndk/releases/tag/v0.9.2) gives applications APIs to discover a recipient's direct-message relays and publish to them, which is the lookup step a client must perform before a private message can arrive where the recipient reads it. It also separates legacy [NIP-04](/en/topics/nip-04/) (deprecated encrypted direct messages) into explicit calls, so an application chooses that older format deliberately, and adds [NIP-17](/en/topics/nip-17/) (private direct messages) file messages for sending attachments through the modern path.

[Version 0.9.3](https://github.com/relaystr/ndk/releases/tag/v0.9.3) extends the wallet and query surfaces. Hold-invoice timeouts and a `max_fee` limit arrive for Nostr Wallet Connect calls, per-relay pagination lets a client page each relay on its own cursor instead of assuming one shared position, and the wallet command-line tool is isolated from unrelated pending deliveries and from remote signers, so a wallet operation no longer waits behind traffic it does not own.

### nostr-social-graph 2.0.1 coalesces follow-distance work without changing its format

[nostr-social-graph](https://github.com/mmalmi/nostr-social-graph) is a TypeScript library that builds and queries social graphs from Nostr follow events. [Version 2.0.1](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.1) coalesces overlapping follow-distance calculations so concurrent requests share one pass, and it removes temporary byte arrays from binary loading, which lowers the allocation cost of reading a serialized graph.

Neither change in [the release](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.1) touches the public API or the binary format, so an application upgrades without migrating stored graphs or editing call sites. The project's local benchmark reports 21 simultaneous recalculations over the bundled 24,489-user graph falling from 799.3 ms to 33.6 ms; these are library measurements, not end-to-end relay latency.

### better-auth-nostr 0.3.0 hardens sign-in nonces and links keys to existing accounts

[better-auth-nostr](https://github.com/leon-wbr/better-auth-nostr) adds Nostr key sign-in to applications built on the Better Auth authentication library. [Version 0.3.0](https://github.com/leon-wbr/better-auth-nostr/releases/tag/v0.3.0) hardens how the login nonce is issued and consumed, which is the value that binds a signature to one specific sign-in attempt and prevents a captured signature from being replayed.

The release also adds public-key linking, so an account created another way can attach a Nostr key and sign in with it afterward, and it ships a usable React example that runs the whole sign-in flow end to end. A developer integrating the plugin can therefore compare their nonce and callback handling against working code instead of inferring it. Both pieces landed through [the merged authentication-flow work](https://github.com/leon-wbr/better-auth-nostr/pull/9).

writer_model: claude-opus-5 (bounded first-party fallback candidate; wrapper run `7dee2ec3-0440-4980-a0a5-9dd9ce854a4c`)
GATE: PASS (8/8 approved release groups present; style and paragraph-link checks passed; every linked release resolved 2026-09-09)
