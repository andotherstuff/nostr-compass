---
title: "Nostr Compass #34"
date: 2026-08-05
publishDate: 2026-08-05
draft: false
type: newsletters
description: "Sandstr offers mock-data tours of Nostr clients, nostr-mill adds per-event signing consent, and nostrord expands relay-hosted groups. Deep dives cover relay search and portable highlights."
---

Welcome back to [Nostr Compass](https://github.com/andotherstuff/nostr-compass), your weekly guide to Nostr.

**This week:** [Sandstr](https://sandstr.app/) lets newcomers explore simulated Nostr clients without creating keys or installing an app. [nostr-mill](https://github.com/0ceanSlim/nostr-mill) adds per-event signer consent and cross-client key recovery, while [nostrord](https://github.com/nostrord/nostrord) expands relay-hosted groups, signers, moderation, uploads, and highlights. Protocol work spans Nostr event formats, wallet connections, relay discovery, napplets, Marmot, and Concord; the deep dives explain relay-assisted search and portable highlights.

## Top Stories

### nostr-mill 1.6.0 puts signing consent and account recovery in the browser

[nostr-mill 1.6.0](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) is an embeddable browser account picker and signer. It now asks for consent by event kind and shows decoded content and tags before signing, with time-limited grants and a permissions manager. The release also fixes a first-session bug that let categories configured to prompt every time sign without asking. Its optional Google onboarding can import an existing `nsec`, stores the key encrypted in the user's Drive app-data folder, supports multiple identities, and can export a [NIP-49](/en/topics/nip-49/) (encrypted private-key format) `ncryptsec`.

The [experimental relay backup](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) derives a strong recovery phrase with scrypt and HKDF, wraps the key as `ncryptsec`, verifies fetched events, and requires a relay quorum before recovery. [NIP-55](/en/topics/nip-55/) (Android signer intents) login now uses Amber's clipboard return path, and [NIP-46](/en/topics/nip-46/) (relay-mediated remote signing) connections are quiet by default. Branding controls and responsive permission screens round out the release without changing existing integrations unless an operator opts in.

### nostrord 2.5.0 gives relay groups stable, relay-specific identities

[nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) is a cross-platform client for relay-hosted communities. It now derives a [NIP-29](/en/topics/nip-29/) (relay-managed groups) identity from both group ID and host relay, scopes membership and admin badges the same way, accepts group `naddr` deep links, and synchronizes private-group threads across devices.

The [release](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) also adds a [NIP-56](/en/topics/nip-56/) (report events) moderation inbox, Amber login through NIP-55, rate-limit backoff for NIP-46 signer traffic, [NIP-84](/en/topics/nip-84/) (portable highlights) rendering with retries for unresolved references, and media uploads through Blossom or [NIP-96](/en/topics/nip-96/) (HTTP file storage). Google login now backs up the key before account creation and confirms disconnects. Thread replies gain richer content and admin deletion, while desktop keychain and mobile keyboard fixes keep those protocol features usable.

### Primal Android 3.5.25 updates remote signing and follow-list filtering

[Primal Android 3.5.25](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.25) is a mobile Nostr client with feeds, search, and remote signing. It updates its remote signer for current protocol behavior, adds a follow mute list, opens search from Explore, repairs stalled relay connections automatically, exposes request timeouts in the interface, rejects invalid follow-list entries, and refreshes fallback relay URLs. Feed prefetching, lower memory use, and a 100 MB cache ceiling reduce the cost of keeping those feeds current. Single-image notes now use the full content width, and profile controls and media preloading receive smaller interaction and ordering fixes.

### Nostur 1.30.2 expands private replies and media in direct messages

[Nostur 1.30.2](https://github.com/nostur-com/nostur-ios-public/releases/tag/527) is an Apple-platform Nostr client. It always exposes the private-reply action, adds per-conversation DM media caches with limits and clearing controls, improves name and tag completion in posts and chats, shows referenced messages in live chat, and includes the room title in chat notifications. Feed pagination and nested-reply fixes address retrieval and conversation rendering regressions.

### Chama 5.7.0 adds arbiter records and cached trade recovery

[Chama 5.7.0](https://github.com/jesuspirate/chama/releases/tag/v5.7.0) coordinates peer trades and arbitration through signed Nostr event chains. It displays an arbiter's locked amount, bond tenure, and funding outpoint; records when a backup replaced an absent arbiter; and defines dormant kind `38136` fault attestations that require both principals' signatures. An explicit repair retries incomplete relay histories against the durable device cache and republishes recovered events, while failed publishes queue for the next connection. The release also prevents cross-device duplicate arbiter-premium payments by treating the author's kind `38113` event as the payment record.

### Auditable Voting 0.1.165 restores delegated ballot delivery

[Auditable Voting 0.1.165](https://github.com/tidley/auditable-voting/releases/tag/v0.1.165) conducts verifiable ballots while separating voter credentials from ballot contents. It restores delegated blind-ballot issuance through authenticated delegation delivery and control-DM backfill, keeps blind-credential direct messages on configured private relays, and updates the audit proxy to 0.1.52.

### Sandstr lets newcomers test-drive Nostr clients with mock data

[Sandstr](https://sandstr.app/) provides interactive browser simulations of Nostr clients so a newcomer can compare their interfaces before installing one or creating a keypair. Its August 3 launch includes reference-verified reproductions of Damus, Amethyst, Primal, Snort, YakiHonne, Coracle, and Wisp, plus clearly labeled early previews of Gossip, Keychat, and Olas. Everything runs locally against mock data, so the simulations do not generate keys or connect to relays. Each simulation links onward to the real client's website and source repository, making Sandstr an onboarding and interface-comparison tool rather than another Nostr client. It shows how feeds, profiles, threads, direct messages, search, zaps, and relay controls feel without asking a first-time user to make an identity or security decision up front.


### mineracks signer pairs a browser extension with a desktop bunker

[mineracks signer](https://github.com/mineracks/mineracks-signer) provides two signing surfaces from the same project. Its browser extension implements [NIP-07](/en/topics/nip-07/) so web applications can request signatures without receiving the private key, while the desktop application exposes a [NIP-46](/en/topics/nip-46/) remote signer for clients that communicate through relays.

The project's [desktop 0.1.0 release](https://github.com/mineracks/mineracks-signer/releases/tag/desktop-v0.1.0) stores key material using NIP-49 encrypted-key encoding and keeps the decrypted key inside the Rust process rather than passing it to the interface. Each request shows the calling application and requested action, while per-application auto-approval is optional and revocable. The first desktop build supports Apple Silicon but not Intel Macs.

## Releases

### Jumble 26.8.1 adds proof-of-work controls and comment previews

[Jumble 26.8.1](https://github.com/CodyTseng/jumble/releases/tag/v26.8.1) is a web and desktop Nostr client. It remembers proof-of-work difficulty for publishing, displays verified-work badges, previews linked comments above external content, saves images from the full-screen viewer, and expands long profile biographies on demand. Reaction notifications now discard unsupported event kinds, relay disconnect notices are less noisy, default relays were refreshed, and a media-autoplay conflict was fixed.

### nostr-calendar 2.1.0 restores private-form signer binding

[nostr-calendar 2.1.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.1.0) publishes calendars, events, and form responses as Nostr data. It binds private-form submissions to the active signer, saves intentional duplicate events to relays, fixes relay fetching, parses calendar dates in local time, and adds app notifications plus an iOS client. The signer correction prevents a stale identity from producing an unusable encrypted response.

### Manent 2.0.0 adds tagging and search for saved notes

[Manent 2.0.0](https://github.com/dtonon/manent/releases/tag/v2.0.0) is a personal archive for signed Nostr notes. It adds local tags and search, letting a reader organize and retrieve saved events without modifying their signed contents.

### nosvelte 0.6.1 closes empty subscriptions after EOSE

[nosvelte 0.6.1](https://github.com/akiomik/nosvelte/releases/tag/v0.6.1) provides reactive Svelte components and hooks for relay data. Empty searches now settle at End of Stored Events, cancellation closes the underlying `REQ`, retries clear stale errors, and list hooks return their documented empty value. It also recognizes addressable events regardless of where their `d` tag appears, replaces superseded metadata and articles, deduplicates reactions by event ID, and keeps every event from a relay's first batch.

## Unreleased Changes

### NMP ties relay admission to declarations and broadens group queries

[NMP](https://github.com/pablof7z/nmp) is a TypeScript toolkit for building Nostr applications and relay-backed group interfaces. [PR #1254](https://github.com/pablof7z/nmp/pull/1254) makes relay admission follow the owner of the declaration that authorizes it, keeping the permission decision attached to signed Nostr state. [PR #1255](https://github.com/pablof7z/nmp/pull/1255) generalizes [NIP-29](/en/topics/nip-29/) relay-managed group queries instead of assuming one narrow lookup shape. Both changes are merged but have not yet appeared in a tagged release.

### Mosaico derives managed-group identity from relay records

[Mosaico](https://github.com/pablof7z/mosaico) is a Nostr client for browsing and administering relay-managed communities. [PR #758](https://github.com/pablof7z/mosaico/pull/758) derives a managed group's identity from the relay that hosts its authoritative records. [PR #757](https://github.com/pablof7z/mosaico/pull/757) observes the group's published record when resolving administration state. This keeps two similarly named groups on different relays distinct and gives clients a relay-backed source for their management metadata.

### Divine isolates slow relays during multi-relay queries

[Divine](https://github.com/divinevideo/divine-mobile) is a mobile short-video client that publishes and retrieves videos over Nostr. [PR #6673](https://github.com/divinevideo/divine-mobile/pull/6673) gives each relay query its own timeout instead of letting one stalled connection consume the timeout budget for an entire request. Results from responsive relays can therefore arrive while the slow endpoint is abandoned independently. The change improves retrieval without treating one relay as authoritative for the combined result.

### rust-nostr hardens encryption, hashes, and reconciliation

[rust-nostr](https://github.com/rust-nostr/nostr) is a Rust library and toolkit for Nostr clients, relays, and protocol implementations. [PR #1421](https://github.com/rust-nostr/nostr/pull/1421) reduces allocation in its [NIP-44](/en/topics/nip-44/) versioned-encryption path, while [PR #1423](https://github.com/rust-nostr/nostr/pull/1423) introduces typed hashes that make incompatible digest values harder to mix accidentally. [Commit 21e31c2](https://github.com/rust-nostr/nostr/commit/21e31c28da3dfadedb5fa6e58c712647f16e5f69) prevents a malformed [NIP-77](/en/topics/nip-77/) Negentropy set-reconciliation message from disconnecting the local relay. The merged work tightens both encrypted payload handling and reconciliation failure behavior before the next release.

### Zeus serializes NWC payments before charging spending budgets

[Zeus](https://github.com/ZeusLN/zeus) is a mobile Bitcoin and Lightning wallet that can expose wallet operations through Nostr Wallet Connect. [PR #4305](https://github.com/ZeusLN/zeus/pull/4305) counts pending payments against a [NIP-47](/en/topics/nip-47/) Nostr Wallet Connect budget instead of waiting for settlement. [PR #4303](https://github.com/ZeusLN/zeus/pull/4303) serializes payment handling so concurrent requests cannot race through the same authorization limit. The merged pair closes a budget-enforcement gap on the wallet's Nostr control surface.

### Nostr Components shares one relay connection attempt

[Nostr Components](https://github.com/saiy2k/nostr-components) is a reusable web-component library for adding Nostr data and interactions to applications. [PR #105](https://github.com/saiy2k/nostr-components/pull/105) lets components mounted at the same time share an in-flight relay connection attempt. Each consumer still receives the resulting connection, but concurrent mounts no longer open duplicate sockets while the first handshake is pending. The change reduces avoidable relay load in applications assembled from several independent components.

## NIP Updates and Protocol Spec Work

### Nostr event formats and discovery

[NIP PR #2430](https://github.com/nostr-protocol/nips/pull/2430) proposes sticker packs as addressable kind `30031` definitions and a user's installed packs as replaceable kind `10031`. Each sticker tag carries a shortcode, SHA-256 hash, and MIME type; the image remains on a [NIP-B7](https://github.com/nostr-protocol/nips/blob/master/B7.md) (Blossom blob storage) server. The open draft therefore standardizes pack identity and installation without placing image bytes in events.

[NIP PR #2429](https://github.com/nostr-protocol/nips/pull/2429) proposes kind `31436` addressable Gopher documents. Each event holds one UTF-8 text or menu node, and signed nodes under one pubkey form a gopherhole that any relay-backed RFC 1436 bridge can serve. The open proposal uses ordinary addressable-event storage rather than binding the publication to one Gopher hostname.

[NIP PR #2428](https://github.com/nostr-protocol/nips/pull/2428) proposes epoch-ticketed private groups. A group rotates membership credentials between epochs, and clients present the ticket for the current epoch to participate. The draft targets private chat without asking a relay to treat a permanent bearer token as lifetime membership.

[NIP PR #2425](https://github.com/nostr-protocol/nips/pull/2425), covered as a proposal last week, has now merged a URI clarification into [NIP-B0](/en/topics/nip-b0/) (addressable web bookmarks). It distinguishes omitted HTTPS prefixes from explicit URI schemes when a bookmark stores its target in the `d` tag, preventing clients from reconstructing an ambiguous destination.

### Payments and wallet connections

[NIP PR #2419](https://github.com/nostr-protocol/nips/pull/2419), covered as a proposal in the July 22 issue, has now merged a smaller [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) core. Connection URIs, encrypted relay transport, capability discovery, encryption negotiation, and common methods stay in the NIP; notifications, hold invoices, keysend, transaction history, metadata, and deep-link pairing move to a dedicated extension repository. Existing connections remain compatible while wallets can implement optional contracts independently.

[NWC PR #2](https://github.com/nostr-wallet-connect/nwc/pull/2), covered as a proposal last week, has now merged BIP-321 payment methods into that extension repository. BIP-321 provides a common Bitcoin payment URI that can carry different rails, so NWC callers can request or send a payment without adding a new core RPC for each underlying instruction type.

### Napplet host capabilities

[NAP PR #95](https://github.com/napplet/naps/pull/95) proposes catalog discovery for Nostr-distributed sandbox applications. A napplet asks its host which applications and capabilities are available, and the host returns policy-filtered metadata instead of exposing its full local environment. The contract supports launch decisions without granting execution authority during discovery.

[NAP PR #33](https://github.com/napplet/naps/pull/33) proposes shell-mediated file and blob uploads. A napplet supplies bytes and intent; the host selects a NIP-96 or Blossom rail, signs authorization, reports progress, and returns URLs, hashes, MIME data, and ready-to-attach [NIP-94](/en/topics/nip-94/) (file metadata) tags. Storage credentials and HTTP authority never enter the napplet.

### Marmot encrypted groups

[Marmot PR #410](https://github.com/marmot-protocol/marmot/pull/410) merged convergence and deferred-input rules. Clients distinguish an object that lacks a current epoch dependency from stale or invalid input, keep it eligible for refetch after resource refusal, and retry when another commit changes the decryption context. A domain-separated state commitment gives conformance tests a shared convergence oracle without adding a production wire field.

### Concord community planes

[Concord PR #14](https://github.com/concord-protocol/concord/pull/14) merged CORD-08 disappearing messages. One community metadata value sets the lifetime; chat rumors and encrypted wraps carry a [NIP-40](/en/topics/nip-40/) (event expiration) tag, while deletion events and the kind `1740` timer notice are exempt. The signed timer travels with community state, though relay deletion remains a retention request rather than a cryptographic erasure guarantee.

[Concord PR #13](https://github.com/concord-protocol/concord/pull/13) merged rotation-proof pinning into CORD-04. Each channel has one replace-entire pin list on the control plane; entries carry the original signed seal plus per-message NIP-44 expansion keys, allowing a new member to verify the author and plaintext without receiving an old epoch key. Private lists can remain sealed to a channel epoch, caps bound list size, and author deletions remove pins without forking the control-plane chain.

## NIP Deep Dive

### Search Capability (NIP-50)

[NIP-50](/en/topics/nip-50/), defined in the [primary specification](https://github.com/nostr-protocol/nips/blob/master/50.md), adds an optional search filter for relays. Ordinary Nostr filters work when a client already knows an author, event kind, identifier, or tag; NIP-50 addresses discovery when the input is a human query such as `best nostr apps`.

The [NIP-50 wire format](https://github.com/nostr-protocol/nips/blob/master/50.md#search-filter-field) adds a `search` string to a normal filter inside a `REQ` message. A request can combine that field with `kinds`, `authors`, `ids`, tag filters, and `limit`, and one REQ can carry several independent filters. A supporting relay should match primarily against event `content`, may use other fields when the event kind makes that useful, and should sort by its own relevance score before applying `limit`. That order differs from the usual newest-first event stream.

The query string can include the specification's [`key:value` extensions](https://github.com/nostr-protocol/nips/blob/master/50.md#extensions). It names `include:spam`, `domain:`, `language:`, `sentiment:`, and `nsfw:`; a relay should ignore extensions it does not implement. Clients discover declared support through the relay's [NIP-11](/en/topics/nip-11/) `supported_nips` field, but they may still send the filter elsewhere if they are prepared to reject unrelated responses.

The [NIP-50 specification](https://github.com/nostr-protocol/nips/blob/master/50.md) deliberately does not standardize tokenization, stemming, ranking, language detection, sentiment analysis, or spam classification. Two compliant relays can return different events and different ordering for the same query. That makes the relay an index and ranking provider, not a source of truth. The specification recommends querying several supporting relays, checking whether returned events satisfy the client's use case, and dropping relays whose results have poor precision.

This differs from exact [NIP-01 filtering](https://github.com/nostr-protocol/nips/blob/master/01.md). An `authors` or `#t` filter has deterministic matching semantics that a client can verify directly, while a search match may depend on an index and an opaque score. NIP-50 retains NIP-01's signed event envelope and relay transport, but accepts variation in recall and ordering to make open-ended retrieval possible.

The event below is a real search result returned by a NIP-50 search relay for a relay-discovery query, with the [seven NIP-01 event fields](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures) populated and a valid signature.

```json
{
  "id": "2943d6b43bcbf0ee4a8b4cac912111be0309607b8bb435ae40529989bea7f6c5",
  "pubkey": "3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d",
  "created_at": 1785771175,
  "kind": 1,
  "tags": [],
  "content": "I've been working on a customizable client (mostly relay feeds, but a ton of other things and subtle details too). It's called Hallway for reasons I don't remember and it's a fork of Fevela which is a fork of Jumble, but very rewritten for speed and simplicity...",
  "sig": "5b058b89dab9bd09d81bdc10eff95536125b87fbcbbc97f08d835c1272b2a3190cc3d340e42f54acb0d7e0e4b00355ab91292d0305c84a2d73b538319c0da12c"
}
```

Current clients use the same filter in different discovery surfaces. [Nostria](https://github.com/nostria-app/nostria/blob/d291c2ab091c60c36f99c90241e2fd9da1b0c4bc/src/app/services/relays/search-relay.ts) sends NIP-50 searches to dedicated search relays, [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useSearchEvents.ts) searches events through its relay pool, and [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/services/orchestration/SearchOrchestrator.ts) coordinates relay-backed searches for long-form reading. Their different result handling reflects the latitude NIP-50 leaves to relays and clients.

### Highlights (NIP-84)

[NIP-84](/en/topics/nip-84/), defined by its [primary specification](https://github.com/nostr-protocol/nips/blob/master/84.md), assigns kind `9802` to a highlight. It turns a selected passage, or a reference to non-text media, into a signed event that can move between reading, social, and annotation clients.

The [event's `content`](https://github.com/nostr-protocol/nips/blob/master/84.md#format) contains the selected text and may be empty when the source is audio, video, or another non-text medium. A highlight points to a Nostr source with an `a` tag for an addressable event or an `e` tag for an ordinary event; an `r` tag identifies a web URL. URL-producing clients should remove tracking and other non-useful query parameters before publishing so cosmetic URL variants do not fragment references to the same source.

Optional [`p` tags](https://github.com/nostr-protocol/nips/blob/master/84.md#attribution) attribute the source to one or more Nostr pubkeys. Their fourth value may identify a role such as `author` or `editor`, and a `context` tag can preserve surrounding text when the selection alone would be unclear. A quote highlight adds a `comment` tag instead of publishing a second kind `1` note: the source `r` tag receives the `source` marker, while pubkeys or URLs mentioned in the comment carry `mention`, letting renderers distinguish attribution from the user's response.

The [kind `9802` definition](https://github.com/nostr-protocol/nips/blob/master/84.md) makes a highlight a regular event rather than a replaceable one. Repeating or correcting a selection creates another signed event, and removing one relies on the normal deletion-request flow and relay retention policy. The specification does not define byte offsets, selectors, or a canonical document snapshot, so a client may be unable to relocate a passage after its web source changes. Public highlights also reveal reading interests; private annotation requires a separate encryption and sharing design.

NIP-84 differs from a [NIP-23 long-form event](https://github.com/nostr-protocol/nips/blob/master/23.md), which publishes an entire article as kind `30023`; a highlight quotes or points into material that may remain elsewhere. It also differs from a [NIP-51 bookmark set](https://github.com/nostr-protocol/nips/blob/master/51.md), which stores a replaceable collection of references. NIP-84 makes each selection independently signed, attributable, discoverable, and discussable.

The highlight below is a real kind `9802` event published from Primal's iOS client, recovered from public relays. It carries the [seven NIP-01 event fields](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures) with a valid signature, an `a` tag pointing at a [NIP-23 long-form event](https://github.com/nostr-protocol/nips/blob/master/23.md), a `p` tag attributing the article's author, and a `context` tag preserving the surrounding passage.

```json
{
  "id": "0d57c07cfdfe8ec00711e2af88a666b61fc35c167b90b02dfb5db7ffba7b794a",
  "pubkey": "07367baec8e73c076b14e47fba3b0d5c014d559d7986a7172a79a8a64419d7c2",
  "created_at": 1785797755,
  "kind": 9802,
  "tags": [
    ["context", "Quantum computers will break secp256k1 which nostr relies on for its public private key pair. This means that given an npub, a quantum computer will be able to derive your nsec, read all your encrypted data and sign events as you."],
    ["alt", "This is a highlight created in https://primal.net iOS application"],
    ["a", "30023:1ec454734dcbf6fe54901ce25c0c7c6bca5edd89443416761fadc321d38df139:nostr-quantum-preparation"],
    ["p", "1ec454734dcbf6fe54901ce25c0c7c6bca5edd89443416761fadc321d38df139", "", "mention"]
  ],
  "content": "Quantum computers will break secp256k1 which nostr relies on for its public private key pair. This means that given an npub, a quantum computer will b",
  "sig": "219f3c1e572d1a087d667dc0d3a5443c77c0db3a5d42ce4e630604901ac63d2c879a86269d81e220bb77fd48b1579adafc333075e53c6eb0a108791fdd4a1622"
}
```

The format already crosses client boundaries. [nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) added NIP-84 rendering this week, [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/components/ui/note-rendering/HighlightRenderer.ts) renders highlight events in its long-form client, and [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useCreateHighlight.ts) publishes them from selected content. Those implementations cover reading, creation, and social rendering without requiring one service to own the annotation.

---

Send a NIP-17 DM to share a project or news item through the [Nostr Compass project](https://github.com/andotherstuff/nostr-compass).
