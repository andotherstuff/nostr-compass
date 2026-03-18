---
title: 'Nostr Compass #14'
date: 2026-03-18
publishDate: 2026-03-18
draft: false
type: newsletters
description: 'Amethyst expands Nostr Wallet Connect, and Notedeck moves software release discovery onto Nostr.'
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** [Amethyst](https://github.com/vitorpamplona/amethyst) lands full [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) method support, [Alby Hub](https://github.com/getAlby/hub) adds multiple relay support in [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6), [Amber](https://github.com/greenart7c3/Amber) ships [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3) with built-in Tor and finer signer permissions, and [Zeus](https://github.com/ZeusLN/zeus) removes a risky NWC keysend path in [PR #3835](https://github.com/ZeusLN/zeus/pull/3835). [Notedeck](https://github.com/damus-io/notedeck) ships a signed updater in [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) that discovers releases through [NIP-94](/en/topics/nip-94/) (File Metadata) events, while [Damus](https://github.com/damus-io/damus) fixes stale [NIP-65](/en/topics/nip-65/) (Relay List Metadata) state, [Nostrability Outbox](https://github.com/nostrability/outbox) revises its benchmark results with corrected data, and [Primal iOS](https://github.com/PrimalHQ/primal-ios-app) tests direct relay subscriptions for DMs. [Primal Android](https://github.com/PrimalHQ/primal-android-app) ships [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7), [Route96](https://github.com/v0l/route96) ships [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0), [OpenChat](https://github.com/DavidGershony/openChat) keeps tightening Marmot interoperability in [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11), [Pika](https://github.com/sledtools/pika) consolidates its runtime in [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1), and [Nostria](https://github.com/nostria-app/nostria) adds [NIP-85](/en/topics/nip-85/) (Trusted Assertions) Web of Trust filtering. The NIPs repository merges [NIP-54](/en/topics/nip-54/) (Wiki) Djot markup and a 5000-character input cap for [NIP-19](/en/topics/nip-19/) (Bech32-Encoded Entities), and this issue digs into [NIP-94](/en/topics/nip-94/) (File Metadata) and what the [NIP-54](/en/topics/nip-54/) Djot switch changes for implementers.

## News

### Wallet Connect support broadens, and wallet clients tighten failure paths

[Amethyst](https://github.com/vitorpamplona/amethyst), the Android client maintained by vitorpamplona, merged [PR #1828](https://github.com/vitorpamplona/amethyst/pull/1828), which brings its [NIP-47](/en/topics/nip-47/) implementation close to full protocol coverage. The patch adds `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, `get_info`, hold invoice methods, keysend support with TLV records, capability discovery via kind `13194`, and notification events on kind `23197` with [NIP-44](/en/topics/nip-44/) (Encrypted Payloads). That gives the client a much wider NWC surface without leaning on app-specific extensions.

The surrounding wallet stack moved in the same direction. [Alby Hub](https://github.com/getAlby/hub), the self-custodial Lightning node and wallet service behind many NWC deployments, shipped [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6) with multiple relay support and simpler connection and swap flows. [Zeus](https://github.com/ZeusLN/zeus), the mobile Lightning wallet, merged [PR #3835](https://github.com/ZeusLN/zeus/pull/3835) removing NWC keysend support after identifying a silent fund-drain path in that flow, while also fixing pending-event and Cashu activity handling. Wallet connectivity on Nostr is getting broader, and implementers are removing flows that are hard to secure.

### Notedeck moves release discovery onto Nostr

[Following last week's Notedeck coverage](/en/newsletters/2026-03-11-newsletter/), [Notedeck](https://github.com/damus-io/notedeck), the native desktop client from the Damus team, shipped [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) after merging [PR #1326](https://github.com/damus-io/notedeck/pull/1326). The new updater subscribes to signed kind `1063` release events, matches the local platform, downloads the referenced binary, and verifies its SHA256 hash before install. Release metadata no longer has to come from the GitHub API or a project website. A trusted release pubkey and a relay connection are enough.

The same patch adds a `notedeck-release` CLI that publishes those events from GitHub release artifacts, which means the release pipeline now has a Nostr-native publishing path as well as a Nostr-native discovery path. It also puts the Damus and Notedeck updater model much closer to Zapstore's relay-published signed release flow: Zapstore's `zsp` tooling already handles software assets as kind `1063` or `3063` events, so this path is not locked to one client or one publisher. The rest of the release candidate is practical desktop work, follows columns, profile "View As User," [NIP-59](/en/topics/nip-59/) (Gift Wrap) support, real-time note stats, and [NIP-11](/en/topics/nip-11/) (Relay Information Document) limitation handling, but the updater is the part likely to outlive this one release cycle.

### Relay state is moving closer to runtime behavior

[Damus](https://github.com/damus-io/damus) merged [PR #3665](https://github.com/damus-io/damus/pull/3665), replacing a stale stored relay-list event ID with a direct database query for the latest kind `10002` event. When the old value went stale, relay add and remove operations could fall back to bootstrap or year-old lists, which made some relay changes appear to succeed while leaving the active state unchanged. [PR #3690](https://github.com/damus-io/damus/pull/3690) fixes a second failure path by deleting stale `lock.mdb` state during LMDB compaction so the app does not crash with `SIGBUS` on the next launch.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) opened [PR #194](https://github.com/PrimalHQ/primal-ios-app/pull/194), which subscribes directly to a chat partner's [NIP-04](/en/topics/nip-04/) (Encrypted Direct Messages) write relays while a conversation is open, keeping the cache server as fallback. [Nostur](https://github.com/nostur-com/nostur-ios-public) opened [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53), which combines randomized relay scoring, [NIP-66](/en/topics/nip-66/) liveness filtering from nostr.watch, and Thompson sampling to change relay selection from a fixed heuristic into a learned policy. Clients have long treated relay choice as setup data. More apps now treat it as live state that needs measurement and repair logic.

## Releases

### Primal Android 3.0.7

[Primal Android](https://github.com/PrimalHQ/primal-android-app), the Android client from Primal, shipped [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7) with a new poll and wallet cycle. [PR #945](https://github.com/PrimalHQ/primal-android-app/pull/945) adds zap-based poll voting, [PR #948](https://github.com/PrimalHQ/primal-android-app/pull/948) paginates vote loading so larger polls stay usable, and [PR #965](https://github.com/PrimalHQ/primal-android-app/pull/965) fetches zap receipts for all transactions. The same release also tags supported events with [NIP-89](/en/topics/nip-89/) (Recommended Application Handlers) client metadata in [PR #968](https://github.com/PrimalHQ/primal-android-app/pull/968), which helps downstream clients attribute event origins more cleanly.

### Amber v4.1.3

[Following last week's Amber coverage](/en/newsletters/2026-03-11-newsletter/), [Amber](https://github.com/greenart7c3/Amber), the Android signer app for [NIP-55](/en/topics/nip-55/) flows, shipped [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3). The release builds on its recent [NIP-42](/en/topics/nip-42/) relay-auth work with more operational hardening: [PR #327](https://github.com/greenart7c3/Amber/pull/327) adds built-in Tor alongside Orbot support, [PR #324](https://github.com/greenart7c3/Amber/pull/324) replaces coarse NIP-based encryption permissions with content-type-specific rules, and [PR #336](https://github.com/greenart7c3/Amber/pull/336) removes network permissions from the offline flavor while [PR #335](https://github.com/greenart7c3/Amber/pull/335) adds CI checks to keep it that way. [PR #322](https://github.com/greenart7c3/Amber/pull/322) also moves PIN storage into encrypted DataStore.

This release tightens the signer boundary itself. That is useful for any Android flow that hands real keys or relay-auth decisions to Amber, because the hard part is not only what the signer can do. It is also how narrowly it can be scoped.

### Route96 v0.6.0

[Following last week's Route96 coverage](/en/newsletters/2026-03-11-newsletter/), [Route96](https://github.com/v0l/route96), the media server that supports Blossom and [NIP-96](/en/topics/nip-96/) (HTTP File Storage), released [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0). The release moves configuration and whitelist state into the database with hot reload and adds retention policies for cold or aging files. It also adds a richer `GET /user/files` endpoint plus file-stat tracking for downloads and egress, which gives operators more visibility into how their storage server is being used.

### OpenChat v0.1.0-alpha.11

[Following last week's OpenChat coverage](/en/newsletters/2026-03-11-newsletter/), [OpenChat](https://github.com/DavidGershony/openChat), the Avalonia-based chat client built on the Marmot stack, shipped [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11) after a week of fast protocol work. [Commit c33895d](https://github.com/DavidGershony/openChat/commit/c33895d6b1a198f01b9b01a7be974bdce033fb9c) wraps Welcome events in [NIP-59](/en/topics/nip-59/) gift wrap and removes old MIP-00 tag-normalization shims, [commit 2738ff4](https://github.com/DavidGershony/openChat/commit/2738ff428154f60f50debb8f2a53662d427b28f1) completes the MIP-02 compliance audit, and [commit 8e470cf](https://github.com/DavidGershony/openChat/commit/8e470cf7945bced010168c8229d73d67db638b9f) does the same for MIP-03 group message encryption. [Commit 129ca37](https://github.com/DavidGershony/openChat/commit/129ca37e264efaa2d1a8b04fe95cd72e5e212547) also consolidates NIP-44 handling onto the shared marmot-cs implementation, reducing the risk of client-side crypto drift.

### nak v0.19.0 and v0.19.1

[nak](https://github.com/fiatjaf/nak), fiatjaf's command-line Nostr toolkit, shipped [v0.19.0](https://github.com/fiatjaf/nak/releases/tag/v0.19.0) and [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1). The 0.19 series adds a group-forum UI in [commit 5f4efdb](https://github.com/fiatjaf/nak/commit/5f4efdbc69a36fc80ea3f97b2cdee1db6a7c5b47), switches group metadata edits to a full replace flow in [commit da0b753](https://github.com/fiatjaf/nak/commit/da0b75337198010687aceb6a07bbae67407faee3), and replaces the older `no-text` handling with `supported_kinds` in [commit bef67d3](https://github.com/fiatjaf/nak/commit/bef67d35d259e0450debf0fd870e1a937a2406bf). For group implementers, that keeps the CLI aligned with the direction group specs and clients are moving.

## Project Updates

### Amethyst

[Following last week's Amethyst coverage](/en/newsletters/2026-03-11-newsletter/), [Amethyst](https://github.com/vitorpamplona/amethyst), the Android client with one of the broadest protocol surfaces in Nostr, kept building on its wallet and relay work after the NIP-47 patch. [PR #1853](https://github.com/vitorpamplona/amethyst/pull/1853) adds [NIP-45](/en/topics/nip-45/) (Event Counting) COUNT queries across relay management screens, so users can see how many events each relay actually holds for home feed, notifications, DMs, and index data. [PR #1849](https://github.com/vitorpamplona/amethyst/pull/1849) adds encrypted file uploads for [NIP-17](/en/topics/nip-17/) (Private Direct Messages) chats, with a retry path for unencrypted uploads when a storage host rejects the encrypted version.

[PR #1791](https://github.com/vitorpamplona/amethyst/pull/1791) also brings full [NIP-46](/en/topics/nip-46/) (Nostr Connect) desktop bunker login with a heartbeat indicator, which matters because remote signing failures often feel like random UI breakage from the user's side. The client shows whether the signer is alive and how recently it answered, while also making it obvious when the current session uses a bunker.

### Nostria

[Nostria](https://github.com/nostria-app/nostria), the multi-platform client built around a local-first stack, merged [PR #561](https://github.com/nostria-app/nostria/pull/561) adding Web of Trust filtering for feeds and thread replies. The feature uses the existing trust-service rank data and exposes it as both a feed filter and a reply filter, hiding authors whose rank does not clear the threshold while preserving thread structure when trusted descendants are present. That gives users a middle layer between "show everyone" and hardcoded list-based curation.

The same week also brought [PR #563](https://github.com/nostria-app/nostria/pull/563), which adds content filtering and repost support to the summary page. Outside the tracked PR list, Nostria has also been filling in more of its power-user surface. It now supports the latest Brainstorm Web of Trust service with in-app signup, along with send and receive money flows in DMs using NWC and BOLT-11 invoices. It also adds Nostr-native GIF handling through the emoji NIP and a stronger RSS import path for musicians that can pick up existing Lightning splits from podcast feeds. Nostria is treating ranking, media, payments, and publishing as one connected app surface.

### Nostur

[Nostur](https://github.com/nostur-com/nostur-ios-public), the iOS client maintained by nostur-com, opened [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53) to change outbox routing from a fixed plan into a scored policy. The patch adds randomized relay scoring, [NIP-66](/en/topics/nip-66/) relay liveness filtering with a cached nostr.watch feed, and Thompson sampling so relay success and failure data changes future selections. The design keeps a safety valve when too many relays would be filtered out and preserves `.onion` relays. This is one of the clearest current examples of a client treating relay selection as an adaptive system.

### Nostrability Outbox

[Following the earlier Outbox benchmark report](/en/newsletters/2026-03-04-newsletter/), [Nostrability Outbox](https://github.com/nostrability/outbox), the benchmark and analysis project focused on [NIP-65](/en/topics/nip-65/) and [NIP-66](/en/topics/nip-66/) client routing, spent the week tightening its own claims. [PR #35](https://github.com/nostrability/outbox/pull/35) replaces inflated Thompson-sampling results with a full re-benchmark across 1,511 runs and recommends the `CG3` variant for NDK-style routing. [PR #43](https://github.com/nostrability/outbox/pull/43) adds decay and use-case comparisons, fixes a `0 follows` cache-poisoning bug, then re-runs the Telluride dataset after pinning cache TTLs.

That is not product work in the usual sense, but it matters for client authors because the project's numbers are now sharper and less flattering in the places where they had previously overclaimed. The corrected result is still useful. Randomized selection keeps beating purely deterministic routing in the cases Outbox cares about, Thompson-style learning can materially improve coverage when clients persist useful relay history, and [NIP-66](/en/topics/nip-66/) liveness filtering cuts wasted time on dead relays. The work is also turning into concrete implementation proposals, including [NDK #387](https://github.com/nostr-dev-kit/ndk/pull/387), [Nostur #53](https://github.com/nostur-com/nostur-ios-public/pull/53), [Amethyst #1833](https://github.com/vitorpamplona/amethyst/pull/1833), [rust-nostr #1282](https://github.com/rust-nostr/nostr/pull/1282), [welshman #53](https://github.com/coracle-social/welshman/pull/53), and [applesauce #54](https://github.com/hzrd149/applesauce/pull/54) plus [applesauce #55](https://github.com/hzrd149/applesauce/pull/55).

### White Noise backend

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), the Rust backend used by White Noise and other Marmot tooling, merged two boundary-hardening patches around Blossom media handling. [PR #637](https://github.com/marmot-protocol/whitenoise-rs/pull/637) enforces HTTPS on Blossom URLs and adds an upload timeout, while [PR #642](https://github.com/marmot-protocol/whitenoise-rs/pull/642) caps blob downloads at `100 MiB` to block oversized media pulls from turning into a denial-of-service path. For private messaging software, media URLs are one of the sharpest interfaces between encrypted application logic and untrusted network infrastructure. This week the team tightened that edge.

### rust-nostr

[rust-nostr](https://github.com/rust-nostr/nostr), the Rust protocol library, merged [PR #1280](https://github.com/rust-nostr/nostr/pull/1280) adding convenience constructors for `LocalRelayBuilderNip42`. The new read and write helpers give embedded relay and test setups a clearer way to turn [NIP-42](/en/topics/nip-42/) auth policy into code. This is a small library patch, but it matters for teams building local or app-bundled relays that need auth turned on without repeating boilerplate every time.

### Pika

[Following earlier Pika coverage](/en/newsletters/2026-03-04-newsletter/), [Pika](https://github.com/sledtools/pika), the Marmot-based messaging app, shipped [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1) and [pikachat-v1.1.1](https://github.com/sledtools/pika/releases/tag/pikachat-v1.1.1) with a release cycle focused on runtime convergence. [PR #542](https://github.com/sledtools/pika/pull/542) introduces a shared Marmot runtime facade for the CLI and sidecar, with the app host moving onto the same surface. [PR #556](https://github.com/sledtools/pika/pull/556) tightens OpenClaw agent lifecycle and provisioning state, while [PR #600](https://github.com/sledtools/pika/pull/600) adds restore-from-backup and stricter recovery safety for managed environments.

The direct user-facing surface here is smaller than in the last Pika writeup, but the architectural change is meaningful. Pulling group, media, call, and session logic behind one shared runtime reduces the chance that the app and daemon drift apart as the Marmot stack grows.

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-54](/en/topics/nip-54/) (Wiki): Switch from Asciidoc to Djot** ([PR #2242](https://github.com/nostr-protocol/nips/pull/2242)): Wiki content on kind `30818` now uses Djot as the canonical markup format. The merged text adds explicit wikilink behavior, merge-request examples for kind `818`, redirect examples for kind `30819`, and non-Latin normalization examples for `d` tags. That gives implementers a cleaner parsing target than Asciidoc and removes one more spec path that depended on a Ruby-centered toolchain.

- **[NIP-19](/en/topics/nip-19/) (Bech32-Encoded Entities): Add input limit** ([PR #2264](https://github.com/nostr-protocol/nips/pull/2264)): The spec now recommends capping Bech32-encoded entity strings at 5000 characters. This is a small change with real parser value, because NIP-19 strings now appear in QR flows, deep links, share sheets, and user-pasted input across many clients.

**Open PRs and Discussions:**

- **Nostr Key File for [NIP-49](/en/topics/nip-49/) (Private Key Encryption)** ([PR #2269](https://github.com/nostr-protocol/nips/pull/2269)): Proposes a `.nostrkey` file format for password-encrypted key export and import. If merged, it would give clients a more normal file-based backup path than copying raw `ncryptsec` strings around.

- **Membership state consistency for [NIP-43](/en/topics/nip-43/) (Relay Access Metadata and Requests)** ([PR #2267](https://github.com/nostr-protocol/nips/pull/2267)): Adds a section clarifying that relays should maintain one authoritative membership state per pubkey. That would simplify group-client logic around membership changes and replayed history.

- **Deletion guidance for [NIP-17](/en/topics/nip-17/) (Private Direct Messages)** ([PR #2260](https://github.com/nostr-protocol/nips/pull/2260)): Proposes a concrete path for editing and deleting private messages through gift-wrapped delete events. The work is still open, but client authors need an answer here if NIP-17 is going to replace older DM flows fully.

- **Share-intent URI for [NIP-222](/en/topics/nip-222/)** ([PR #2266](https://github.com/nostr-protocol/nips/pull/2266)): The draft would standardize how mobile and desktop apps hand shared content into a Nostr client. That is one of the roughest interop edges in current app-to-app flows.

## NIP Deep Dive: NIP-94 (File Metadata)

[NIP-94](/en/topics/nip-94/) defines kind `1063` as a first-class metadata event for a file. The [specification](https://github.com/nostr-protocol/nips/blob/master/94.md) gives the event its own human-readable `content` plus machine-readable tags for download URL, MIME type, hashes, dimensions, previews, fallbacks, and storage service hints. That matters because the file becomes queryable on relays as its own object. A client does not have to scrape metadata out of surrounding content to understand what the file is.

```json
{
  "id": "6a92ef8d7c3a1b5d4e8f9a0b1c2d3e4f567890abcdef1234567890abcdef1234",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1742342400,
  "kind": 1063,
  "tags": [
    ["url", "https://downloads.example.org/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["m", "application/gzip"],
    ["x", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["ox", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["size", "48392011"],
    ["dim", "0x0"],
    ["magnet", "magnet:?xt=urn:btih:00112233445566778899aabbccddeeff00112233"],
    ["i", "00112233445566778899aabbccddeeff00112233"],
    ["blurhash", "LEHV6nWB2yk8pyo0adR*.7kCMdnj"],
    ["thumb", "https://downloads.example.org/notedeck/v0.8.0-rc2/thumb.png", "bbccddeeff00112233445566778899aabbccddeeff0011223344556677889900"],
    ["image", "https://downloads.example.org/notedeck/v0.8.0-rc2/screenshot.png", "ccddeeff00112233445566778899aabbccddeeff001122334455667788990011"],
    ["summary", "Signed macOS release artifact for Notedeck v0.8.0-rc2"],
    ["alt", "Notedeck desktop release archive"],
    ["fallback", "https://mirror.example.net/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["service", "nip96"]
  ],
  "content": "Notedeck macOS universal build",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

The tags do more work than they first appear to do. `x` identifies the served file, while `ox` identifies the original file before any server-side transformation. The preview tags let clients build browseable file indexes without downloading the full asset, and `summary` can carry a short excerpt beside them. `fallback` gives a second source when the main URL fails, and `service` hints at the storage protocol behind the file, such as [NIP-96](/en/topics/nip-96/) or another host. NIP-94 therefore sits below social posting and above raw storage. It describes the file, not the conversation around the file.

That is why this week's Notedeck updater is interesting. [PR #1326](https://github.com/damus-io/notedeck/pull/1326) uses signed kind `1063` events for software release discovery, then verifies the downloaded binary against the published SHA256. The same event shape can describe a software artifact or a media upload. NIP-94 is old enough to be stable, but it still has room to grow because more projects are treating metadata events as a transport for machines, not only as decoration for people.

## NIP Deep Dive: NIP-54 (Wiki)

[NIP-54](/en/topics/nip-54/) defines kind `30818` as a wiki article event. The [specification](https://github.com/nostr-protocol/nips/blob/master/54.md) treats the `d` tag as the normalized article topic and lets many authors publish entries for the same subject. The article body lives in `content`, while tags handle normalized identity, display title, summaries, and references to earlier versions. That means NIP-54 is not only a content format. It is also a retrieval and ranking problem, because each client still has to decide which article version to show.

```json
{
  "id": "8c94e5d1f2a300112233445566778899aabbccddeeff00112233445566778899",
  "pubkey": "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff",
  "created_at": 1742342400,
  "kind": 30818,
  "tags": [
    ["d", "nostr-wiki"],
    ["title", "Nostr Wiki"],
    ["summary", "Djot-formatted reference article about Nostr wiki events"],
    ["a", "30818:11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff:nostr-wiki", "wss://relay.example.org", "fork"],
    ["e", "11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff", "wss://relay.example.org", "fork"]
  ],
  "content": "Nostr is a [protocol][] for carrying events across relays.\n\n[protocol]: nostr:nevent1example",
  "sig": "33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889900112233cc44dd55ee66ff77889900aabbccddeeff00112233445566778899001122"
}
```

The merge this week changes the canonical markup from Asciidoc to Djot in [PR #2242](https://github.com/nostr-protocol/nips/pull/2242). That matters for implementers because Djot has a tighter standalone spec and simpler parser story across languages. The merged text also clarifies how reference-style wikilinks resolve, how merge requests use kind `818`, how redirects use kind `30819`, and how `d` tag normalization should behave for non-Latin scripts. Those are the parts that make two independent clients agree on what article a link points to.

NIP-54 also sits in an unusual place in the protocol. A wiki client needs content rendering, but it also needs ranking policy. Reactions, relay lists, contact lists, and explicit deference signals all feed into which article wins for a given topic. The Djot switch does not solve that ranking problem, but it does remove one of the parser ambiguities that sat underneath it. That is why the merge matters now: the change is less about nicer prose formatting and more about making multi-client wiki behavior easier to implement consistently.

Building something, or want us to cover it? Reach out via [NIP-17](/en/topics/nip-17/) DM on Nostr at `npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923`.
