---
title: 'Nostr Compass #47'
date: 2026-11-04
publishDate: 2026-11-04
draft: false
type: newsletters
---

This week [Amethyst](#amethyst) shipped inline napplets with fixes from an [embed security review](https://github.com/vitorpamplona/amethyst/pull/4710), [Napplets](#napplets---web-packages) tied applet identity to per-document ports, and [Marmot's mdk](#marmot-protocol-mdk) nightlies tightened group messaging. Elsewhere, relays, wallets, signing libraries and new apps changed, much of it in merged source that has not shipped.

## Top Stories

### Amethyst

Amethyst, the Android client, released [v1.21.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.21.0), which runs napplets inline in notes on Android 11+ and on desktop. Fixes from an [embed security review](https://github.com/vitorpamplona/amethyst/pull/4710) close a path where any napplet with relay access could read decrypted DMs. Decryption now needs a separate user grant and `nostr.signEvent` needs signer permission, while the desktop Chromium renderer remains unsandboxed. A [per-file attachment encryption change](https://github.com/vitorpamplona/amethyst/pull/4701) gives each [NIP-17](/en/topics/nip-17/) private direct message attachment a fresh AES-GCM key and nonce, where multi-file batches had reused both. The upstream risk description comes from code analysis without a reproduced exploit, and files already sent are not repaired.

### Marmot Protocol (mdk)

mdk, Marmot's MLS-based encrypted messaging kit for Nostr, published testing-only nightly prereleases, with no stable release in that line. In the 2 November nightly, [new sends wait behind older queued ones](https://github.com/marmot-protocol/mdk/pull/2849) in a group, keeping encryption generations in order for members catching up on history, though this does not guarantee against lost messages. A merged, default-off [lost-Welcome repair](https://github.com/marmot-protocol/mdk/pull/2936) follows the [Marmot heartbeat rule](https://github.com/marmot-protocol/marmot/pull/497) and resends the exact retained Welcome once the target's heartbeat shows activity at least ten minutes after the latest carrier publication. Heartbeat cadence or clock lag can delay repair by an hour or more, and completion has no upper bound. [Device linking commands](https://github.com/marmot-protocol/mdk/pull/2922) stay behind the default-off dev-device-groups feature and are off in production.

### Napplets - Web Packages

Napplets, the web packages for sandboxed Nostr applets, released [core 0.37.0](https://github.com/napplet/web/releases/tag/%40napplet/core%400.37.0), [nap 0.36.0](https://github.com/napplet/web/releases/tag/%40napplet/nap%400.36.0) and [shim 0.35.0](https://github.com/napplet/web/releases/tag/%40napplet/shim%400.35.0), which [bind applet identity to a per-document MessagePort](https://github.com/napplet/web/pull/302). The verified (dTag, artifactHash) identity is tied to the port passed in the hello from the created iframe, and all NAP traffic uses that port. A document loaded by navigation gets no grants. Shells still using Window messaging must upgrade, because there is no compatibility path. Later source [locks the preview frame to its verified document](https://github.com/napplet/web/pull/305) with frame-src 'none'.

## Tagged Releases

### Marble

Marble, a beta client built on Cosign threshold signing, can read relays as feeds in [0.12.23](https://github.com/sybenx/marble/releases/tag/v0.12.23). A relay opened by its address shows its own description and then its posts, newest first. Favorite relays are kept in a kind 10012 list and relay groups in kind 30002 sets, the same lists Jumble uses. The release also reworks reactions, with a tray of recent reactions and the user's own custom emoji.

### Sidecar

Sidecar, a browser extension for publishing notes and web highlights, can delete its wallet backup from relays in [1.16.6](https://github.com/dmnyc/sidecar/releases/tag/v1.16.6). After a confirmation, it replaces the encrypted copy with an empty one and asks relays to forget it, leaving the connected wallet in place. Relays are not guaranteed to erase the backup. Since [v1.16.5](https://github.com/dmnyc/sidecar/releases/tag/v1.16.5), Sidecar strips EXIF, XMP and IPTC metadata from JPEGs before upload, and its [upload preparation change](https://github.com/dmnyc/sidecar/pull/572) blocks any JPEG that cannot be cleaned.

### Haps

Haps publishes and installs native packages under Nostr keys. [Haps 0.1.25](https://github.com/mmalmi/haps/releases/tag/v0.1.25) ships macOS, Linux and Windows bundles with checksum-pinned htree helpers and a SHA256SUMS file covering all archives. Source for 0.1.24 [writes versioned Hashtree references](https://github.com/mmalmi/haps/commit/3dd051cefe9e506886a7f036267950282a179ee8) under the draft Hashtree specification. Haps 0.1.23 and earlier cannot read the new catalogs without a legacy transition catalog or an upgraded installer or Cargo build.

### Cosign

Cosign, the threshold-signing library behind the Marble beta, ships a partial join fix in [0.12.9](https://github.com/sybenx/cosign/releases/tag/v0.12.9): a join through a scanned inviter now needs that inviter's contribution and pieces from at least two distinct senders. Phone-to-phone joins remain unbound, so an attacker with two keys is still enough, and empty decryption parts still skip proof verification. In [0.12.8](https://github.com/sybenx/cosign/releases/tag/v0.12.8), a server that writes the member list can still choose share points with known secrets. Phones get fixes only through a Marble release.

### nostream

nostream, a TypeScript relay backed by PostgreSQL, adds [outbound peer sync](https://github.com/cameri/nostream/pull/1043) in [3.12.0](https://github.com/cameri/nostream/releases/tag/nostream%403.12.0). The worker reads each peer's [NIP-11](/en/topics/nip-11/) relay information scopes, authenticates with [NIP-42](/en/topics/nip-42/) client authentication and reconciles through [NIP-77](/en/topics/nip-77/) negentropy syncing, checking fetched events against ID, signature and scope. [Peer-specific limits](https://github.com/cameri/nostream/pull/1034) apply only after a configured peer completes AUTH. A source release does not prove any relay has deployed it.

### diVine

diVine, a short-form looping video client, published [stable Android 1.0.27](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.27) with interactive public video stickers; iOS and macOS availability is unconfirmed. A merged [below-window requery](https://github.com/divinevideo/divine-mobile/pull/10711) runs only after initial history restoration has finished, reading gift wraps, [NIP-04](/en/topics/nip-04/) deprecated encrypted DMs and deletions in pages of 100 messages per relay. It walks each relay independently, whereas the existing history drain shares one cursor and can skip a capped relay's older history. Coverage is bounded and does not recover complete history.

### Whistle

Whistle, a mobile group location-sharing and chat app, released [2.0.1](https://github.com/sjmcnamara/whistle/releases/tag/v2.0.1), its first public release on Marmot protocol v2. Existing groups cannot be carried over, so groups must be recreated and every member must update, while npub identities are kept. Scan-to-join replaces invite codes and links. In a known issue, chat messages sent offline may arrive late or not at all, which the release attributes to MarmotKit; location sharing is unaffected.

## In Development

### Quartz

Quartz, a Kotlin Multiplatform Nostr library, shipped [live subscription resume after reconnect](https://github.com/vitorpamplona/quartz/pull/82) in release 2.14.0. Each relay resumes from the newest delivered created_at, capped at the device clock, and gift-wrap filters reach back two extra days to cover backdating. Older-timestamped events a relay stored during an outage can still be missed. Merged, unreleased [count-aware negentropy windows](https://github.com/vitorpamplona/quartz/pull/85) compare an optional [NIP-45](/en/topics/nip-45/) event count with the local count and treat relay counts as untrusted.

### Buzz

Buzz merged a change that [commits kind 5 and 9005 deletions in one transaction with the target's soft delete](https://github.com/block/buzz/pull/8944), so a failure can no longer accept a deletion while the target stays live. Historic torn rows are not repaired. The mobile profile of [NIP-RS](/en/topics/nip-rs/), a Buzz draft for cross-device read state, has merged and [syncs read frontiers across devices](https://github.com/block/buzz/pull/8998). On older relays without read_state_snapshot, local reads still work and cross-device sync stops with no fallback.

### Alby Hub

Alby Hub, a self-custodial Lightning node serving [NIP-47](/en/topics/nip-47/) Nostr Wallet Connect apps, merged a [database migration fix](https://github.com/getAlby/hub/pull/2657) that keeps each table's ID counter during db_migrate or a Postgres migration. Before it, a new app could reuse a deleted app's ID and inherit its transactions and isolated balance. No tagged release or deployment containing the fix was identified. A separate [notification change](https://github.com/getAlby/hub/pull/2677) isolates per-app failures, though failed notifications are still dropped without retry.

### swift-nostr-client

swift-nostr-client, a Swift 6 Nostr library, merged a breaking change that makes [RemoteSigner run the connect handshake before its first command](https://github.com/yysskk/swift-nostr/pull/287). The new connectsAutomatically setting defaults to true, and a failed handshake means the command is not sent. Because [NIP-46](/en/topics/nip-46/) remote signing secrets are single-use, apps resuming a bunker session with a saved client key pair must set it to false, or the first command presents the spent secret. No release has been tagged.

## New Projects

### Trikey

Trikey, a pre-alpha, unaudited wallet whose phone app and guardian talk through encrypted Nostr relay messages, addresses the app freezing on open in [release 0.1.10-alpha](https://njump.me/nevent1qvzqqqr4dupzqpepqn8d9d5jc8r4qf6h7kd7ldpgrpqgdaw8wjwyrxztkjltnfy4qyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpk2jxzja4q4z8avcsc7jqenpuykke49p3z3halm0xtgmn3h6r6judumrxf). Both sides now keep a restart-surviving record of already-read wrap IDs and skip those before any signature check or decryption. Expiration hints on requests and alerts do not guarantee relay deletion, and the publisher's performance measurements were taken on a laptop.

### Pacto

Pacto, a desktop community-organizing app running legacy Marmot groups alongside NIP-17 DMs, released unsigned [v0.7.5](https://github.com/covenant-gov/pacto-app/releases/tag/v0.7.5) with one-minute editing of sent messages. Its [DM delivery fixes](https://github.com/covenant-gov/pacto-app/pull/425) fail sends immediately when the pool has no trusted relay and route typing indicators through trusted relays. Open, unmerged pull requests would add [squad events](https://github.com/covenant-gov/pacto-app/pull/488) and [encrypted squad docs](https://github.com/covenant-gov/pacto-app/pull/490).

### Mialuna

Mialuna, a media-focused Flutter Nostr client, published a [version 0.19.0 release announcement](https://njump.me/nevent1qvzqqqr4dupzqeyvpafs936l8quz5nfvskjg9wf8e3sm9q52q72wxmrvc7tdap4xqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqk6ltj5kr6mtq8mkyz9rzqxkkrhq9hsjz675e05rwgltwgreddw3npkkez) that adds deletion requests for the user's own stories when they expire. The [changelog commit](https://github.com/Lwb89dev/mialuna/commit/d0a38cb92dac724e6e7bac6ec8f94a31a378e886) records relay deletion requests and Blossom media deletion, with local-key accounts running this automatically and Amber or bunker accounts waiting until the user chooses Delete now. The APK and its device behavior have not been independently checked. Deletion requests cannot guarantee that relays or servers erase the data.

### whereAreYou

whereAreYou, an Android app sharing location within circles joined by QR code or invite link, encrypts coordinates with AES-256-GCM and sends them through public relays. A [member signing commit](https://github.com/Dzekdrix/whereAreYou/commit/82121d0f13b4d5256b2392383e74640afde3019e) stops circle-key holders from posting as another member, and every device must update. For the [Base45 identity backup](https://github.com/Dzekdrix/whereAreYou/commit/82e185967dd0115b93472b3d92a4d0393c8751bc), the author warns that anyone who photographs the QR code could guess its eight-digit code offline, by his estimate within tens of minutes of GPU time; no benchmark was published. The source carries no security endorsement.

## Protocol and Spec Work

### Buzz defines owner-authorized agent credential routes

Buzz merged a [NIP-FA](/en/topics/nip-fa/) [draft for owner-authorized agent credentials](https://github.com/block/buzz/pull/9015), defining grant, assertion and revocation routes for agents authorized through [NIP-OA](/en/topics/nip-oa/) owner attestation. A grant comes from an RFC 8693 token exchange pairing the owner's session with an agent [NIP-98](/en/topics/nip-98/) HTTP auth proof, and revocation disconnects the agent and keeps its key from re-enrolling. NIP-FA is a Buzz specification merged in source only, with no claim of production activation or interoperability.

### Post-quantum event signatures gain exact validation rules

The long-running open post-quantum signature proposal gained [exact ML-DSA-44 validation rules for Nostr events](https://github.com/nostr-protocol/nips/commit/43104cbff30ae006e907d8ee0ec15c4949d0eef6). Keys and signatures have fixed lengths, verifiers check the signature over the 32 raw event-ID digest bytes with an empty context, and no fallback algorithm is allowed. The proposed identity has no [NIP-19](/en/topics/nip-19/) bech32 encoding, and new signatures do not make [NIP-44](/en/topics/nip-44/) encrypted payloads or [NIP-59](/en/topics/nip-59/) gift wraps post-quantum safe.

### A proposed signed precondition prevents lost event replacements

An open Buzz pull request [proposes a project-local NIP-CS signed precondition](https://github.com/block/buzz/pull/8835) for replaceable and addressable events, and it is not an official NIP. The signed tag names the current head ID or `none`, and the relay checks it atomically under a coordinate lock, rejecting a stale write with a false OK or HTTP 409 and storing nothing. Untagged writes work as before, and the tag gives no compare-and-swap guarantee across relays.

## NIP Deep Dive: NIP-31 and NIP-73

Clients often meet content they do not natively understand. [NIP-31: Dealing with Unknown Event Kinds](/en/topics/nip-31/) gives an unfamiliar event kind a readable label, and [NIP-73: External Content IDs](/en/topics/nip-73/) names subjects outside Nostr, such as books or webpages. The two conventions are independent existing specifications ([NIP-31 text](https://github.com/nostr-protocol/nips/blob/master/31.md), [NIP-73 text](https://github.com/nostr-protocol/nips/blob/master/73.md)).

### NIP-31 is marked unrecommended

The current [NIP-31 text](https://github.com/nostr-protocol/nips/blob/master/31.md) opens with a warning that marks it `unrecommended` as "unnecessarily bloated," and its status line reads draft, unrecommended and optional. Events using the convention already exist on relays, so the mechanics below describe how clients read them, with no recommendation for new protocols.

### What an alt tag carries

Under the [spec](https://github.com/nostr-protocol/nips/blob/master/31.md), an author of a custom kind not meant to be read as text adds an `alt` tag with a short plaintext summary. Kind-1-centric clients are not expected to request other kinds, but users can still reference such events from notes, where a summary supplies context. A label cannot cast a vote or act on a wallet request. For richer interaction the spec points to [NIP-89: Recommended Application Handlers](/en/topics/nip-89/).

Because `alt` is a tag, the event ID and signature from [NIP-01](/en/topics/nip-01/): [Basic protocol flow description](https://github.com/nostr-protocol/nips/blob/master/01.md) cover it. A valid signature authenticates an author-controlled summary: it shows the author published the label without showing it is accurate, so misleading summaries are possible. Tags are public, so an `alt` on an event with encrypted content exposes its summary and can reveal what the content conceals. These properties come from the [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) envelope, outside NIP-31's normative text. A top-level `alt` tag is also distinct from the image-description `alt` field inside `imeta`, and renderers parse them separately.

### How two clients read alt

In noStrudel's [unknown-event card at commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx), the first `alt` tag is trimmed and becomes the main label, with an optional `Using <client>` line. A missing or blank value yields `Unknown event (kind ...)`, and up to three lines of content appear independently. The same component resolves the `client` tag through NIP-89 handler templates, showing Open when a shareable address exists and `Open in <client>` when a valid handler link resolves. Explanation and app dispatch are separate controls.

Amethyst's [UnknownEventDigest.kt at commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) prefers content it classifies as prose and falls back to `alt`. Its parser trims values and takes the first nonblank `alt`, so an event whose first `alt` is blank can be labeled differently here than in noStrudel. Both descriptions reflect source at those commits, not confirmed release behavior.

### Example: a poll with an alt label

The kind 1068 poll below was retrieved from wss://relay.damus.io, and its ID and BIP340 signature check out under [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) rules. A generic renderer can show the bilingual `alt` text, while a poll-aware client reads the `option` and `polltype` tags.

```json
{
  "kind": 1068,
  "id": "7d1df3922833b47645922de43c2edd83e928a0ad083cee592beeee2b262bb743",
  "pubkey": "5f6dc275f3f9f8752d010a110c226148a9ba3399c5b63a0f469ee93b1394a53e",
  "created_at": 1793626294,
  "tags": [
    [
      "option",
      "z25mgp",
      "Windows"
    ],
    [
      "option",
      "ncddq0",
      "macOS"
    ],
    [
      "option",
      "4wta6q",
      "Linux"
    ],
    [
      "option",
      "p9ykti",
      "UNIX or FreeBSD/NetBSD/OpenBSD"
    ],
    [
      "polltype",
      "singlechoice"
    ],
    [
      "alt",
      "Poll: Which one do you usually use?\n普段どれを使っていますか？"
    ],
    [
      "client",
      "Ditto",
      "31990:781a1527055f74c1f70230f10384609b34548f8ab6a0a6caa74025827f9fdae5:ditto"
    ]
  ],
  "content": "Which one do you usually use?\n普段どれを使っていますか？",
  "sig": "f1378a723c65e83bd3105b593f10767903bde993788cfaf625583466fca21f1ef2be945bb2ca526aa9e898c93d5f1677a2f5ceaf70cb3a59c99f97eb179658fa"
}
```

### NIP-73 subjects and families

The [NIP-73 specification](https://github.com/nostr-protocol/nips/blob/master/73.md) (draft, optional, with no unrecommended flag) puts an external subject in an `i` tag and its identifier family in a `k` tag, so clients can query one exact subject or a whole family. A book uses `["i", "isbn:9780765382030"]` with `["k", "isbn"]`, and a webpage uses its URL with `k` set to `web`. NIP-73 defines no event kind; other events carry the tags.

### Normalization and URL hints

Matching depends on identical strings, so the [spec](https://github.com/nostr-protocol/nips/blob/master/73.md) fixes a form per family: URLs normalized without a fragment, ISBNs without hyphens, geohashes lowercase, ISO 3166 codes uppercase. An optional third array element carries a URL hint for clients with no opinion on the identifier. The author chooses that hint, and it is not part of the identity. It also proves no ownership and names no canonical site.

### What a shared identifier does not prove

Under [NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md), equal identifiers join conversations and establish nothing else. A signed comment identifies its commentator, and it does not authenticate the book, site or podcast publisher or show who controls them. Aliases, edition-specific ISBNs and URLs that normalize differently can split one subject into several threads. Context matters: [NIP-22](/en/topics/nip-22/): [Comment](https://github.com/nostr-protocol/nips/blob/master/22.md) uses uppercase `I`/`K` for root scope and lowercase `i`/`k` for parent, and [NIP-39: External Identities in Profiles](/en/topics/nip-39/) uses `i` for profile identities, so not every `i` tag is a NIP-73 subject.

### NIP-73 in parser and renderer code

rust-nostr's [nip73.rs at commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) parses known prefixes into a typed `ExternalContentId` and turns an optional hint into a typed URL, emitting the third tag element only when a hint exists. Its tests keep hyphenated ISBNs: the parser strips the prefix and stores the rest without applying spec normalization, so typed parsing does not guarantee canonical strings. It separates chain IDs from the family, mapping `ethereum:100:tx:<hash>` to `ethereum:tx`. That revision has no `iso3166` country variant.

Amethyst's [DisplayExternalId.kt at commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) sends geohash and hashtag identifiers to dedicated displays. URL identifiers also get a dedicated display, while other supported types go to a generic scope chip. A URL opens the app's own thread route for that page. With previews disabled, normal rendering shows a plain link chip and requests no preview. With previews enabled, fetching a missing preview can contact the target site. Turning previews off avoids that request in normal rendering. Neither file establishes release behavior.

### Example: a comment on a webpage

This kind 1111 comment, retrieved from wss://nos.lol, places the same public Reddit thread URL in both its `I`/`K` and `i`/`k` pairs, with `web` as the family under [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) and NIP-73. Its ID and signature verify, which identifies who wrote the comment and says nothing about the linked page.

```json
{
  "kind": 1111,
  "id": "e4229e38d93fad5d612ae21c401573bf8e87f0462dc2bd653804a252f98a238a",
  "pubkey": "ce5b8496c144a9dcd4990df6e265d9b60a21cde2515f3b206dc67b1c343790a9",
  "created_at": 1793590574,
  "tags": [
    [
      "I",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "K",
      "web"
    ],
    [
      "i",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "k",
      "web"
    ],
    [
      "client",
      "LayerTake"
    ],
    [
      "L",
      "layertake"
    ],
    [
      "l",
      "pin",
      "layertake"
    ],
    [
      "anchor",
      "{\"type\":\"text\",\"exact\":\"tools and systems\",\"prefix\":\"help • 6mo ago u/TheFarSea What \",\"suffix\":\" do you use for tracking and org\"}"
    ]
  ],
  "content": "Like this. I'm making this Public but could be just for me or friends/groups.",
  "sig": "a979389480d6ca919e4ab7b1ba92e532bf281be45c5df222e17d7d4ca62ef07d52c1004c0ce88620663dfac012b306154cfd73b858225764c701c40e3d9b7dfe"
}
```
