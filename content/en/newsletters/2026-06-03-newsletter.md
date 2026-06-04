---
title: 'Nostr Compass #25'
date: 2026-06-03
publishDate: 2026-06-03
draft: false
type: newsletters
---

Amber 6.2.0 ships NIP-44 v3 encryption ahead of the spec. Mostro lands the foundation for Cashu-settled escrow across eight PRs, wrapping the existing Cashu Development Kit as a second settlement backend alongside Lightning. NIP-F4 podcasts merges after 27 months of debate. fiatjaf opens a contested NIP-17 key-decoupling proposal that re-opens the bunker-versus-Marmot architectural argument. Amethyst lands NIP-32 hashtag labeling, a dedicated podcast screen, and onchain zaps across 52 unreleased PRs.

## Top stories

### Amber 6.2.0: NIP-44 v3 encryption shipped

[Amber v6.2.0](https://github.com/greenart7c3/Amber/releases/tag/v6.2.0), released June 1, adds [NIP-44 v3 encryption support](https://github.com/greenart7c3/Amber/pull/448) with a dedicated approval screen, intent preview, bunker preview, history logging, and auto-reject for invalid requests. The release also registers [NIP-44 v3 ContentProvider authorities](https://github.com/greenart7c3/Amber/commit/8b93340) so other Android apps can request v3 encryption alongside the existing v2 path. NIP-44 itself is the versioned encrypted payload spec used by [NIP-17](/en/topics/nip-17/) private DMs, NIP-46 bunker traffic, and other Nostr primitives; v3 in Amber is an opt-in alongside v2, signaled by a separate signer method so receiver-side clients can negotiate the algorithm explicitly. The corresponding NIPs PR has yet to land, so Amber is rolling out v3 ahead of the protocol consensus, with the wire format and ContentProvider authority registered for downstream client integration.

NIP-46 sessions now auto-accept ping requests on connect, removing the prompt on the first round trip after pairing. The `sign_message` signer method was removed entirely after being deprecated and unused.

Because Amber is the dominant Android signer, every downstream client that wants v3 has to target Amber's wire format until the NIPs PR lands. That gives Amber implicit say over the final v3 spec until the protocol catches up. The trade is real: v3 in production lets Amber gather implementation feedback for the eventual NIP, at the cost of a temporary single-implementation reference point that other clients now have to match.

### Mostro: Cashu escrow integration via CDK

grunch landed eight PRs across MostroP2P this week integrating Cashu's existing P2PK multisig primitives (NUT-10 and NUT-11) as a second settlement backend alongside Lightning on the Nostr-coordinated P2P Bitcoin exchange. The cryptographic primitives are Cashu's; the work is integration scaffolding and a new escrow backend trait. [Mostro core v0.12.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.12.0), released May 30, adds the [protocol types for 2-of-3 multisig escrow](https://github.com/MostroP2P/mostro-core/pull/150), per-proof P_M signatures, and allows escrow events through response validation. The architecture is documented in [PR #756](https://github.com/MostroP2P/mostro/pull/756) and uses per-order trade keys clarified in [PR #757](https://github.com/MostroP2P/mostro/pull/757).

The implementation rolled out across six follow-up PRs over a single day. [F2 (PR #758)](https://github.com/MostroP2P/mostro/pull/758) added the config, escrow mode, and conditional boot. The next slice, [F3 (PR #760)](https://github.com/MostroP2P/mostro/pull/760), defined an `EscrowBackend` trait with a Lightning implementation and a Cashu stub, letting Mostro switch settlement backends without changing the order state machine. [F4 (PR #759)](https://github.com/MostroP2P/mostro/pull/759) wrapped [CDK](https://github.com/cashubtc/cdk) (the Cashu Development Kit) for mint and wallet operations. Database work in [F5 (PR #761)](https://github.com/MostroP2P/mostro/pull/761) added compare-and-swap escrow locks and active-locked queries. [F6 (PR #762)](https://github.com/MostroP2P/mostro/pull/762) built a containerized mint in a dedicated CI job for end-to-end escrow testing. The Mostro flow already uses NIP-59 gift-wrapped DMs for order coordination over the relay, so Cashu escrow slots in as a second settlement option alongside Lightning without touching the wire protocol.

## Releases

### ngit v2.5.0: GRASP fallback and lazy git fetches

[ngit v2.5.0](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.5.0) changes the default behavior of `git push pr/<branch>` and `ngit send` to produce a PR kind for new proposals when the repository has at least one GRASP server registered. Previously this only triggered for oversized commits over 60 KB or commits containing submodules. When a PR cannot be pushed to the repository's GRASP servers, ngit now falls back to GRASP-06 routing through the declared servers. The `ngit send --git-server` flag or `git push -o git-server=<url>` lets contributors target a custom git URL or GRASP server explicitly.

`ngit init` republishes now preserve unknown tags from existing announcements, so tags added by a future ngit version or third-party tool survive republish. A yellow warning lists the carried-over tags, and `--clean` removes them on demand. `ngit pr apply`, `ngit pr checkout`, and `ngit pr list` consult git servers lazily and share a single fetch helper, so checkout no longer fetches unconditionally when the commit is already local. `ngit pr checkout` also tries submitter-supplied clone URLs from the PR event as a fallback when the repo's declared git servers don't carry the PR tip, matching the existing behaviour in `ngit pr apply`. ngit is the reference [NIP-34](/en/topics/nip-34/) implementation for git collaboration over Nostr, and v2.5.0 makes GRASP the first-class path for new contributors.

### Jumble v26.5.7: EXIF stripping and validated zap counts

[Jumble v26.5.7](https://github.com/CodyTseng/jumble/releases/tag/v26.5.7) adds two changes that affect user privacy and data integrity directly. EXIF location and camera identifiers are now stripped from image uploads before they leave the client, closing a long-standing metadata-leak surface that affected every image posted from Jumble. Zap counts are now computed only from cryptographically validated receipts, fixing inflated counts from malformed zap events that had let attackers exaggerate zap totals on notes. The release also adds sender-identity verification for [NIP-17](/en/topics/nip-17/) DMs, closing a spoofing surface where a sender could forge their `pubkey` in the seal.

### nostr-calendar v1.6.0: RSVP and duplicate participant handling

[nostr-calendar v1.6.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.0) lands Formstr's RSVP flow ([PR #169](https://github.com/formstr-hq/nostr-calendar/pull/169)) and prevents duplicate participants in event invites ([PR #168](https://github.com/formstr-hq/nostr-calendar/pull/168)). The `waitForAll` option in the publish function now defaults to false so the UI does not block on slow relays ([PR #170](https://github.com/formstr-hq/nostr-calendar/pull/170)). [PR #157](https://github.com/formstr-hq/nostr-calendar/pull/157) shipped Formstr's two NIP proposal drafts for appointment scheduling and reservations.

### Sprout 0.3.6: Sprout × mesh-llm and channel sections

[Sprout v0.3.6](https://github.com/block/sprout/releases/tag/v0.3.6) is the headline of a six-release run from v0.3.1 through v0.3.6 this week. In-process Sprout × mesh-llm integration lands in [PR #798](https://github.com/block/sprout/pull/798), letting Sprout serve and consume mesh-llm nodes through relay admission. User-defined channel sections sync across devices via Nostr in [PR #792](https://github.com/block/sprout/pull/792), and channel sections come to mobile with relay sync in [PR #800](https://github.com/block/sprout/pull/800). Thread-aware notifications with mutable follow and mute controls arrive in [PR #761](https://github.com/block/sprout/pull/761).

Arbitrary file-type attachments with download cards arrived in [PR #810](https://github.com/block/sprout/pull/810), expanding Sprout beyond image-only attachments. Mobile gained a Pulse social feed tab ([PR #772](https://github.com/block/sprout/pull/772)) and Pulse polish across feed, compose, and filter surfaces ([PR #796](https://github.com/block/sprout/pull/796)).

### NostrBotKit v0.5.0: Marmot group chat in a Rust bot framework

[NostrBotKit v0.5.0](https://codeberg.org/Tuxor/NostrBotKit/src/branch/main/CHANGELOG.md), released May 24 on Codeberg, adds [Marmot](/en/topics/marmot/) (MLS-over-Nostr, [NIP-104](https://github.com/nostr-protocol/nips/pull/2014)) support to the self-hosted Rust bot framework. When `marmot: true` is set, the bot publishes its MLS key packages (kind 443, 30443, 10051), accepts group invitations automatically, and listens for messages in joined groups. Two new command types, `dm_marmot` and `dm_marmot_npub`, let bots send messages into named Marmot groups or 1:1 Marmot chats via cron jobs or webhooks. To prevent feedback loops with other bots, NostrBotKit bots only respond to messages explicitly addressed to them via `/command` or `@botname/command`. Encrypted attachments using MIP-04 are auto-decrypted and re-uploaded via Blossom or NIP-96, and the MLS state database is encrypted with a key derived from the bot's private key. NostrBotKit is the first Rust framework to ship NIP-104 bot support, opening Marmot-encrypted bot deployment to a different operator profile than the existing TypeScript path.

### noscrypt v0.1.14: signed cryptography library release

[noscrypt v0.1.14](https://github.com/vnuge/noscrypt/releases/tag/v0.1.14) is a security release of the C cryptography library used by several Nostr clients for secp256k1, NIP-04, and NIP-44 primitives. The release ships with [PGP-signed downloads](https://www.vaughnnugent.com/resources/software/modules/noscrypt) verifiable against the maintainer's public key. Downstream clients that bundle noscrypt should validate the signature before integrating.

### Chama v1.3.0: new Nostr-native P2P escrow with Fedimint

[Chama v1.3.0](https://github.com/jesuspirate/chama/releases/tag/v1.3.0), released June 1, is the headline of a four-release run for a new Nostr-native P2P escrow client that uses Fedimint ecash and 2-of-3 Shamir secret sharing for settlement. The project ships at [getchama.app](https://getchama.app) and runs without a server. v1.3.0 introduces "heal that sticks" (successful re-broadcast and trade healing that survives session restarts) and pay-rail matching, where US-leaning Chamas surface US payment rails first. Multi-unit storefront groundwork landed across [v1.2.11](https://github.com/jesuspirate/chama/releases/tag/v1.2.11) (multi-unit schema) and [v1.2.12](https://github.com/jesuspirate/chama/releases/tag/v1.2.12) (storefront stock accountant + native Fedimint bridge recovery hardening). Chama joins Mostro and Shopstr in the Nostr marketplace category, distinguished by its serverless architecture and Fedimint-based escrow settlement.

## Unreleased changes

### Amethyst: NIP-32 hashtag labeling, podcast screen, music tracks

Amethyst merged 52 PRs and 411 commits this week without cutting a release tag. The largest functional addition is [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111), which implements [NIP-32](/en/topics/nip-32/) hashtag labeling and a label-based hashtag feed using kind 1985 events with `L` namespace and `l` label tags. This replaces the brittle text-match `#tag` mechanism with a labeler-based discovery model where users can follow specific labeler npubs the way they follow content creators. [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) adds a dedicated podcast screen with episode list and inline player, landing within days of the [NIP-F4](/en/topics/nip-f4/) podcast spec merge. [PR #3071](https://github.com/vitorpamplona/amethyst/pull/3071) adds a Software Apps feed with follow-list filtering, and [PR #3067](https://github.com/vitorpamplona/amethyst/pull/3067) adds music tracks and playlists support via [NIP-51](/en/topics/nip-51/) sets.

Ephemeral signers for anonymous post uploads land in [PR #3123](https://github.com/vitorpamplona/amethyst/pull/3123), letting users post anonymously without exposing their identity key to upload services. A Tor self-heal watchdog with integration tests against Arti v2.3.0 arrives in [PR #3053](https://github.com/vitorpamplona/amethyst/pull/3053), strengthening Amethyst's Tor routing during transient network outages. Onchain zaps and a NIP-05 filter for returning users from Gemini land in [PR #3052](https://github.com/vitorpamplona/amethyst/pull/3052), broadening the zap surface beyond Lightning to onchain Bitcoin payments.

### Shopstr: OpenGraph preview URL validation

[PR #504](https://github.com/shopstr-eng/shopstr/pull/504) validates OpenGraph preview URLs before rendering them in marketplace listings, closing a potential XSS surface where malicious sellers could embed scripted content via crafted OG metadata. Shopstr-hosted shops display OG previews for external links, and unvalidated URLs let an attacker inject arbitrary content into the shop UI.

## NIP updates and protocol spec work

### NIP-F4 (Podcasts) merged after two years

[PR #1093](https://github.com/nostr-protocol/nips/pull/1093) merged on May 28, two years and three months after fiatjaf opened the original draft. NIP-F4 defines podcast episodes as kind 54 events with `imeta` tags for audio file metadata (URL, mime type, language ISO code, fallback URLs, NIP-96 service flag, bitrate, duration), a `title` tag, optional `image` and `description` tags, and `t` tags for topic labels. The spec deliberately keeps RSS as the source of truth: episodes can carry an `i` tag referencing the RSS podcast GUID, letting Nostr clients link to existing podcast feeds without duplicating audio hosting. The long debate in the PR thread (with podcast-namespace co-author Dave Jones, Alex Gleason, and Mike Terenzio) settled on a coexistence model where Nostr provides the social layer on top of RSS while RSS keeps the distribution layer. Amethyst's [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) podcast screen lands within days of the spec merge, and Jumble's GIF picker work also includes early podcast-attachment scaffolding.

### NIP-17 key decoupling (PR #2361)

fiatjaf opened [PR #2361](https://github.com/nostr-protocol/nips/pull/2361) on June 1, proposing that NIP-17 separate the identity key from the encryption key. Recipients advertise their encryption key in a new kind 10044 event, and senders use that advertised key (when present) for the gift-wrap inner seal, falling back to the recipient's identity key only when the advertisement is absent. The PR also adds an `n` tag to the seal carrying the sender's encryption pubkey, so receivers can derive the correct conversation key without trial-decryption against every retired key. The stated motivation is bunker UX: under the current design, a bunker user must round-trip every received DM through the signer to decrypt, since the encryption key is the signer-held identity key. Decoupling lets the client hold the encryption key locally while keeping the identity key in the bunker for signatures.

The proposal drew the week's most contentious review. Cody Tseng (Jumble) supports it as the easiest path to cross-client DM interop. Vitor Pamplona (Amethyst) objects on two grounds: it adds a new long-lived decryption secret outside the bunker, and clients that don't ship it will silently fail to decrypt messages from clients that do, with no degradation path because the break is at the seal layer. Pamplona argues the problem is already solved correctly by [Marmot](/en/topics/marmot/)'s key packages and epoch rotation, and that retrofitting key separation into the base NIP-17 spec creates the kind of interop failure that Marmot took two years to engineer around. fiatjaf's counter has three parts: decoupling is optional per-recipient, the n-tag fix addresses the trial-decryption concern, and the alternative is keeping bunker UX broken while Telegram eats the messaging use case. The thread remains open without a merge decision and is the most-watched NIP discussion of the quarter.

### NIP-Silent Payments payment flow (PR #2362)

[silentius-satoshi opened PR #2362](https://github.com/nostr-protocol/nips/pull/2362) on June 1 as a companion to the broader [Nostr Silent Payments NIP draft (PR #2355)](https://github.com/nostr-protocol/nips/pull/2355). The payment-flow NIP defines kind 8352 for silent payment receipt notifications (delivered via [NIP-59](/en/topics/nip-59/) gift wrap so the receipt link is not publicly observable) and kind 10353 for an encrypted UTXO cache that syncs across devices for the same Silent Payments wallet. The pair together let a payer signal a payment to a Silent Payments address using Nostr-native primitives without exposing the on-chain link on the open relay layer.

### NIP-PIP Perfect IP Packets (PR #2364)

[RandyMcMillan opened PR #2364](https://github.com/nostr-protocol/nips/pull/2364) on June 1 as a draft. It introduces a packet-tree transport with three new addressable kinds: 39078 carries the manifest, 39079 carries individual slices, and 39080 carries repair requests. The spec defines a wire format where large files are broken into addressable slices, with manifests describing the slice tree and repair requests letting receivers ask for missing slices. Early-draft status applies, and the proposal has not yet attracted maintainer review.

### NIP-29 audio/video live spaces (PR #2238)

[PR #2238](https://github.com/nostr-protocol/nips/pull/2238) merged on May 28, extending [NIP-29](/en/topics/nip-29/) relay-based groups with audio and video live-space support. Groups can now reference an active live-space session, letting [NIP-53](/en/topics/nip-53/)-style live activity events anchor in a NIP-29 group context.

### NIP-71 video multiple audio tracks (PR #2255)

[PR #2255](https://github.com/nostr-protocol/nips/pull/2255) merged on May 28, adding audio-track `imeta` tags to NIP-71 video events. The new format carries URL, hash, mime type, language tag (with ISO-639-1 plus original-version flag), fallback URLs, NIP-96 service signal, bitrate, and duration. This enables audio-only streaming (video podcasts), resolution switching with stable audio, multiple language tracks, and reduced storage when servers don't embed audio directly into video files. Clients should check for audio-track availability before assuming single-track behavior.

### NIP-59 ephemeral gift wrap (PR #2245)

[PR #2245](https://github.com/nostr-protocol/nips/pull/2245) merged on May 28, adding kind 21059 as an ephemeral counterpart to the existing kind 1059 gift wrap. The semantics match the standard NIP-59 wrap but follow ephemeral event rules per NIP-01 (relays drop them after broadcast and do not persist them). This lets apps choose persistence based on requirements: typing indicators and presence pings benefit from ephemeral, while DM history needs persistence.

### NIP-78 application-specific kind (PR #2292)

[PR #2292](https://github.com/nostr-protocol/nips/pull/2292) merged on May 28, reclassifying NIP-78 application-specific data as a normal addressable kind, dropping the previous separate range. This simplifies replaceability semantics and aligns NIP-78 with the addressable event model used by other application-state NIPs.

### NIP-85 clarifications (PR #2304)

[PR #2304](https://github.com/nostr-protocol/nips/pull/2304) merged on May 28 with small improvements to the language around multiple keys and relays per service provider in [NIP-85](/en/topics/nip-85/) Trusted Assertions, clarifying the operator-key-rotation path for relay assertion services.

### NIP-01 relay connection management one-liner (PR #2307)

[PR #2307](https://github.com/nostr-protocol/nips/pull/2307) merged on May 28, adding a single sentence to NIP-01 about how clients should handle relay connection lifetimes. The fix addresses a long-running gap where clients differed on whether to keep WebSocket connections open after fetching, leading to silent message loss on relays that drop idle connections.

### NIP-C7 kind 9 chat constraint (PR #2310)

[PR #2310](https://github.com/nostr-protocol/nips/pull/2310) merged on May 28, restricting NIP-C7 chat views to kind 9 messages only. This separates ephemeral chat from kind 1 timeline posts in clients that implement NIP-C7-style chat surfaces.

### NIP-55 simplification (PR #2363)

[PR #2363](https://github.com/nostr-protocol/nips/pull/2363) by greenart7c3, opened June 1, simplifies the Android signer application spec. Vitor Pamplona signed off as "Looks good" and fiatjaf asked whether it's ready to merge. The change paves the way for the NIP-44 v3 ContentProvider authority registration that Amber shipped this week.

### NIP-44 v3 (Amber implementation ahead of spec)

Amber shipped NIP-44 v3 in v6.2.0 with eight commits implementing the encryption upgrade and ContentProvider authority registration, but the NIPs-repo spec PR has yet to land. NIP-44 itself defines a versioned encrypted payload format used inside signed events; the existing v2 (in production since 2024) uses secp256k1 ECDH, HKDF, padding, ChaCha20, HMAC-SHA256, and base64. The v3 wire format adds a new version byte (0x03) ahead of the nonce, allowing receiver clients to negotiate the algorithm explicitly. Amber's implementation includes auto-reject for invalid v3 requests, a dedicated approval screen distinct from v2 approvals, and per-direction plaintext logging for the history. Until the NIPs PR merges, v3 stands as an Amber-specific extension. Treat it as a forward-looking signal, not a stable protocol-wide signaling.

## NIP deep dive: NIP-32 (Labeling)

[NIP-32](/en/topics/nip-32/) defines a structured way for any Nostr actor to label events, pubkeys, relays, URLs, or topics using addressable kind 1985 events with a namespaced label vocabulary. The spec introduces two new tags: `L` denotes a label namespace, and `l` denotes a label within that namespace. Label-target tags (`e`, `p`, `a`, `r`, or `t`) specify what is being labeled. The namespace requirement keeps multiple label systems from colliding: a `spam` label in `nip28.moderation` carries different semantics from a `spam` label in `relay-report`.

The design choice that makes NIP-32 useful beyond moderation is that labels are assertions, not protocol-level truth. A kind 1985 event says only that a particular pubkey labeled a particular target in a particular namespace. The trust model is delegated to the client: each client picks which labelers to honor, which namespaces to read, and what UI affordance to give each label. The same primitive carries content warnings, license assignment, ISO-639-1 language tags on kind 1 notes, ISO-3166-2 geographic tags, content classification, distributed moderation suggestions, and reputation scores.

Amethyst's [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111) this week is the largest deployment so far. It adds hashtag labeling through NIP-32 and a label-based hashtag feed, letting users browse by labels assigned by trusted labelers. The earlier `#tag` text-match mechanism that originally drove hashtag discovery on Nostr remains as a fallback for un-labeled notes. The hashtag-as-label model means the same note can be discoverable under multiple labels assigned by different labelers, and users can mute or boost specific labelers without affecting the underlying notes.

Self-labeling is also supported. An author can attach `L` and `l` tags directly to their own kind 1 notes to declare language, location, and topic. A note tagged `["L", "ISO-639-1"], ["l", "en", "ISO-639-1"]` self-identifies as English and can be filtered by language-aware clients without third-party labeling infrastructure.

Example NIP-32 label event tagging a kind 1 note as English and assigning it a moderation tag:

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748908800,
  "kind": 1985,
  "tags": [
    ["L", "ISO-639-1"],
    ["l", "en", "ISO-639-1"],
    ["L", "nip28.moderation"],
    ["l", "approve", "nip28.moderation"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3", "wss://relay.example.com"]
  ],
  "content": "Labeled as English-language content approved for NIP-28 chat moderation",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

The Amethyst rollout combined with the recent Trusted Relay Assertions work suggests NIP-32 is becoming the standard substrate for any "user-driven assertion about a target" pattern on Nostr. The next test is whether labelers themselves develop trust hierarchies: whether users will follow specific labeler npubs the way they follow content creators.

## NIP deep dive: NIP-F4 (Podcasts)

[NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md) merged this week, two years and three months after fiatjaf opened the original draft (PR #1093). The F prefix is plain hex numbering: NIP-F0 through NIP-FF use the same 1-byte hex space as NIP-0A through NIP-0D, with the upper hex range serving as overflow now that the 01–99 decimal range is filling up. NIP-F4 defines how podcasts publish episodes and metadata as Nostr events while keeping RSS as a complementary layer for the audio file itself.

The core architectural choice is that each podcast is its own Nostr keypair. The spec opens with this directly: "each podcast is its own Nostr keypair". This lets podcasts combine their podcasting presence with a normal kind 0 / kind 1 microblogging presence, and lets a podcast change ownership over time through key handover or MuSig2-style shared signing. Four event kinds carry the publishing layer:

- **`kind:10154`**: replaceable podcast metadata. Carries `title`, `image`, `description`, optional `website` tags, and optional `p` tags marking authors with a `role` of `host`, `cohost`, or `editor`.
- **`kind:10164`**: author counter-claim. The example in the spec uses kind `10064` (a typo open for correction), but the heading and surrounding text identify it as `kind:10164`. Users list the podcast pubkeys they author, so that clients can verify the `p` tags in `kind:10154` against an equivalent claim from the supposed author. Without this, a podcast could falsely tag anyone as a host.
- **`kind:54`**: episode events authored by the podcast pubkey directly. Tags include `title`, optional `image`, `description`, and one or more `audio` tags. Each `audio` tag is `["audio", "<audio-url>", "<optional_media_type>"]`. The spec notes "other important fields to be specified here later after further discovery", and the merged form is deliberately minimal.
- **`kind:10054`**: a [NIP-51](/en/topics/nip-51/)-style favorite-podcasts list, letting users mark which podcasts they follow.

The thread debate around the merge involved Podcasting 2.0 co-author [Dave Jones](https://github.com/daveajones), [Alex Gleason](https://github.com/alexgleason), [Mike Terenzio](https://github.com/mterenzio), [Pablo F7z](https://github.com/pablof7z), and [staab](https://github.com/staab). Jones argued strongly against any attempt to replace RSS: "It's been tried many times and always fails", citing JSONfeed, XMPP, AMP, Twitter's API, and Spotify's failed migration. Terenzio reframed the proposal as a social layer on top of RSS, keeping RSS itself as the distribution layer. fiatjaf agreed to step back and let the proposal mature: "I agree with everything you said but I still think we can pull it off, let's stop here for a while". Two years later, the merged spec lands closer to coexistence than replacement.

Three design questions remain explicit in the merged spec:

- The `kind:10164` typo (example shows `10064`) needs reconciling before clients can interoperate safely.
- Episode-level discovery without RSS GUID linking is left open. The merged spec has no `i` tag, no `podcast:item:guid` format, and no RSS bridging mechanism. Clients that want to bridge an existing RSS catalog into kind 54 events must define the bridge convention themselves.
- The "other important fields" stub on the `kind:54` definition leaves bitrate, duration, language, transcript pointers, chapters, and per-segment metadata as open territory for follow-up proposals.

Amethyst's [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) lands a dedicated podcast screen with episode list and inline player within days of the merge, the first major client implementation. Jumble shipped early podcast attachment scaffolding alongside its GIF picker. Wavlake remains the largest Nostr-native podcast platform and will need to decide whether to align its existing kind 31337 music track events with NIP-F4's kind 54 episode model.

Example NIP-F4 kind 54 episode event, matching the merged spec's minimal tag set:

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["audio", "https://podcast.example.com/audio/ep42.mp3", "audio/mpeg"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge, and why coexistence with RSS turned out to be the right architectural choice.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

PR #1093 was open for 27 months, well above the median open duration for merged NIPs PRs. The next test for NIP-F4 is whether the kind 10164 typo gets reconciled, whether episode-discovery and RSS-bridge conventions emerge from the implementers, and whether the major podcast hosts publish under per-podcast keypairs as the spec recommends.
