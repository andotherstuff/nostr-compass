## Top Stories

### nostream expands relay-side DVM routing and authenticated operation

After [August 19's job-ingestion work](/en/newsletters/2026-08-19-newsletter/#nostream-adds-a-relay-monitor-and-mints-invite-codes), [nostream](https://github.com/cameri/nostream), a TypeScript relay implementation, [stores and serves NIP-89 application handler events](https://github.com/cameri/nostream/pull/737). [NIP-89](/en/topics/nip-89/) (application handler discovery) uses kind `31989` recommendations and kind `31990` handler information, both already in the parameterized-replaceable range, so a client can query those kinds and receive a replacement when a `d` tag collides. The relay does not publish handler information for its own workers.

Pending [NIP-90](/en/topics/nip-90/) (data vending machine) jobs now [reach a worker process and return as result events](https://github.com/cameri/nostream/pull/734). On success the relay signs a kind 6000-6999 result with its own key. A timeout or worker crash marks the job failed instead of leaving it submitted.

Authenticated sessions and admin HTTP calls sit on different boundaries. [NIP-42](/en/topics/nip-42/) (client authentication to relays) [tracks the authenticated pubkey per socket](https://github.com/cameri/nostream/pull/716), can require AUTH before clients publish events, and advertises that requirement in the [NIP-11](/en/topics/nip-11/) (relay information) document, with both controls off by default. Separately, [admin API routes can accept NIP-98 signed HTTP authorization](https://github.com/cameri/nostream/pull/730). [NIP-98](/en/topics/nip-98/) (HTTP authentication with signed events) stays off until an operator enables it and names the allowed pubkeys.

### NDK for Dart fixes negentropy, multi-relay request lifetimes, and signature verification

A [NIP-77](/en/topics/nip-77/) (negentropy set-reconciliation) run in [NDK](https://github.com/relaystr/ndk), a Dart development kit for Nostr, returned the wrong have and need sets without erroring, because the codec did not speak [negentropy](/en/topics/negentropy/) protocol v1. The [v1 encoding fix](https://github.com/relaystr/ndk/pull/722) now returns the ids the relay actually has and the ids it still needs.

Identical filters sent to different relays [were collapsing into one request](https://github.com/relaystr/ndk/pull/705). Requests with the same filter now stay distinct when they target different relays or have different lifetimes, so a short query cannot mix another relay's events into the result or leave a live subscription stalled.

The same kit [verifies a signature once and keeps that result](https://github.com/relaystr/ndk/pull/726). A later duplicate delivery no longer spends another check or overwrites the stored verified event.

### Divine Mobile makes wrapped direct-message deletion and signing deterministic

Wrapped [NIP-09](/en/topics/nip-09/) (event deletion request) kind `5` events that targeted a message never applied in [Divine Mobile](https://github.com/divinevideo/divine-mobile), a mobile short-video client that publishes through Nostr. The client [now resolves each deletion against the named message](https://github.com/divinevideo/divine-mobile/pull/8174) instead of treating anything that is not a reaction as already processed. A second [delete-for-everyone request while the first was still in flight](https://github.com/divinevideo/divine-mobile/pull/8164) used to vanish with no error and no kind `5` on the wire; concurrent deletes now each publish.

Divine also tagged [1.0.22](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.22). After that tag, sending the same 1:1 [NIP-17](/en/topics/nip-17/) (gift-wrapped private DMs) text twice in one second [built one rumor id](https://github.com/divinevideo/divine-mobile/pull/8163), so the second send disappeared; each send now carries a token inside the [NIP-59](/en/topics/nip-59/) (gift wrap) rumor so the ids differ.

A caller that had already signed a kind `4` or kind `5` event [kept that signature](https://github.com/divinevideo/divine-mobile/pull/8173), instead of having a client tag appended afterward, which changed the id and made relays reject the event as invalid.

### Conduit Relay hardens its NIP-42 protected inbox

Kind `1059` gift wraps are stored for one recipient. [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay), a Go relay that keeps those wraps in a recipient-protected inbox, [defaults to enforce mode](https://github.com/Conduit-BTC/conduit-relay/pull/8): a kind `1059` query must present [NIP-42](/en/topics/nip-42/) authentication as that recipient, or the relay rejects the request. Mixed-kind filters, wildcards, counts, and [negentropy](/en/topics/negentropy/) over those wraps are `restricted`, so another AUTH cannot turn them into a dump of someone else's inbox.

The same [protected-inbox merge](https://github.com/Conduit-BTC/conduit-relay/pull/8) requires a canonical event id on the transmitted AUTH event and accepts an otherwise-valid NIP-42 event whether or not `content` is empty. Challenge-only still offers AUTH without blocking the read; disabled admits freely. The library default is enforce.

### Amethyst ships NIP-84 highlights and fixes two relay-facing failure paths

Following last week's [Blossom authorization work](/en/newsletters/2026-08-26-newsletter/#amethyst-moves-blossom-authorization-off-image-loading-threads), [Amethyst](https://github.com/vitorpamplona/amethyst), an Android Nostr client, ships [v1.14.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0) with [NIP-84](/en/topics/nip-84/) (portable highlights). A selected passage becomes a kind `9802` event from the composer, a highlights feed, or a share into the app.

After that tag, [trusted lists](https://github.com/vitorpamplona/amethyst/pull/3983) in kinds `30392` through `30395` are [NIP-50](/en/topics/nip-50/) (full-text search) indexed by title only, so a list named in prose can be found without indexing member hex ids. Wallet refusals that arrived over [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) [now show their error instead of looking like a tap that did nothing](https://github.com/vitorpamplona/amethyst/pull/3987), including `QUOTA_EXCEEDED` and `RESTRICTED`, plus a timeout when the wallet never answers.

### Mostro validates signed orders before expensive work and preserves order audit events

After [v0.18.1's Cashu escrow foundation](/en/newsletters/2026-08-12-newsletter/#mostro-0181-starts-a-cashu-escrow-path-and-hardens-the-daemon), [Mostro](https://github.com/MostroP2P/mostro), a peer-to-peer exchange daemon that coordinates orders over Nostr, tagged [v0.18.5](https://github.com/MostroP2P/mostro/releases/tag/v0.18.5), which defaults transport to [NIP-44](/en/topics/nip-44/) (payload encryption) and keeps gift wrap as an explicit opt-in.

After that tag, a [signature check now runs before the spam gate](https://github.com/MostroP2P/mostro/pull/892). An event id does not commit to `sig`, so a copy of a victim's kind `14` with a broken signature could occupy the replay slot and silently drop the genuine message; the daemon verifies first and drops an invalid wrap instead of warning and continuing.

Fee-audit events of kind `8383` were carrying a [NIP-40](/en/topics/nip-40/) (expiration timestamp) of 15 days. They now [keep a one-year expiration](https://github.com/MostroP2P/mostro/pull/924), matching their role as a public payment record. On a Cashu-enabled node, taking an order [asks the seller over Nostr to lock a 2-of-3 escrow](https://github.com/MostroP2P/mostro/pull/830) and publishes the waiting order event, rather than creating a Lightning hold invoice. That completes the request path; it does not by itself close every escrow or marketplace-abuse case.

### Napstr publishes audio catalogues on Nostr and transfers files over Tor

[Napstr](https://github.com/lnbits/napstr) is a desktop audio-sharing client that publishes searchable catalogues and live seeders on Nostr, then transfers the files through a bundled Tor process with no direct-IP fallback. [Version 0.2.0](https://github.com/lnbits/napstr/releases/tag/v0.2.0) keeps profiles and catalogue metadata public, and it keeps requests, transfer credentials, file contents, and peer IP addresses off the relays.

Discovery uses two addressable event kinds in the [Napstr repository](https://github.com/lnbits/napstr). Kind `30421` catalogue entries name a file by its SHA-256 digest, public basename, size, and audio format, and an author withdraws a file by replacing that coordinate with a deleted marker. Kind `30422` availability heartbeats expire after ten minutes and list the file IDs the author is prepared to seed, so a catalogue row is live only while an unexpired heartbeat still contains that digest.

Public conversation uses [NIP-C7](/en/topics/nip-c7/) (kind 9 chat messages) instead of a relay-owned group. The [Napstr repository](https://github.com/lnbits/napstr) defines a shared public room plus a per-track discussion keyed to the file digest. Those messages are signed and public. They do not carry onion addresses, transfer credentials, or file bytes.

A download starts as a [NIP-17](/en/topics/nip-17/) (gift-wrapped private DMs) negotiation. The [Napstr repository](https://github.com/lnbits/napstr) wraps a request, an offer, or a refusal inside a kind `14` rumor, so relays do not see the temporary v3 onion hostname or the one-use capability that an accepted offer returns. The bundled Tor path then moves the bytes over that onion, verifies the complete SHA-256 digest, and re-validates the audio before the file becomes playable.

The [v0.1.7 to v0.2.0 comparison](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) adds audiobook collections and Napstrfy, an optional Android companion. Kind `30423` manifests list ordered chapters that remain ordinary catalogue files, so a client that ignores the collection can still fetch each chapter. Napstr creates a non-destructive local Audiobooks folder for that purpose. Napstrfy pairs to a running desktop with a one-use QR code, then searches and requests downloads through that desktop's existing Nostr and Tor services without receiving the desktop secret key.

The same [comparison](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) times out a companion handshake that does not complete. A seeder copies and hashes the shared file before it serves bytes, writes incoming data into a private temporary file, confines audiobook destinations to a real child of the Napstr folder, and aborts if that destination changes during the transfer.

writer_model: Cursor Grok 4.6

GATE: PASS (Stage 7 ClaimCheck, LinkChecker, ProseReview, TopicAudit, and ContinuityReview all pass; source synchronized 2026-08-26 UTC)
