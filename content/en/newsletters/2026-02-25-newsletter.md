---
title: 'Nostr Compass #11'
date: 2026-02-25
publishDate: 2026-02-25
draft: false
type: newsletters
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** [White Noise v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) brings real-time messaging and Amber signer support with 160+ merged improvements. [diVine 1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) fixes video playback issues and adds Kind 22236 view events for creator analytics. [Pika](https://github.com/sledtools/pika), [Ridestr](https://github.com/variablefate/ridestr), and [Unfiltered](https://github.com/dmcarrington/unfiltered) ship updates. [FIPS](https://github.com/jmcorgan/fips) ships a working Rust implementation of Nostr-native mesh networking. Notecrumbs gets stability fixes for damus.io link previews. [ContextVM](https://contextvm.org) bridges Nostr with the Model Context Protocol. New projects include [Burrow](https://github.com/CentauriAgent/burrow) for MLS-encrypted messaging between AI agents and humans, and [Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) for browser-based vault and identity management. Deep dives cover NIP-55 Android signing and NIP-60 Cashu wallet synchronization.

## News

### Notecrumbs Stability Improvements

[Notecrumbs](https://github.com/damus-io/notecrumbs), the Nostr API and web server that powers damus.io link previews, received a series of fixes addressing reliability issues.

A [concurrency fix](https://github.com/damus-io/notecrumbs/commit/3f201f63ea49) replaced the inflight deduplication mechanism with watch channels. Two callers requesting the same note could both become fetchers, leading to a deadlock when one completed before the other subscribed to the notification. Watch channels with atomic operations ensure only one fetcher runs while others wait on the result.

[Rate limiting](https://github.com/damus-io/notecrumbs/commit/b0d0bf5a2f17) implements a two-layer defense against relay hammering. When users repeatedly access the same note, the system now debounces relay requests with a 5-minute cooldown window. This protection extends to all [NIP-19](/en/topics/nip-19/) types and profile feeds, preventing proportional spam to relays during heavy traffic.

[Performance improvements](https://github.com/damus-io/notecrumbs/commit/38670b3972b6) moved secondary data fetches to background tokio tasks. Pages now render instantly with cached data instead of blocking on sequential relay timeouts that could add up to 7.5 seconds. An upgrade to nostrdb 0.10.0 accompanied these fixes.

### ContextVM: MCP Over Nostr

[ContextVM](https://contextvm.org) is a suite of tools bridging Nostr and the [Model Context Protocol](https://modelcontextprotocol.io/) (MCP). Recent commits have introduced the new [CEP-8](https://docs.contextvm.org/spec/ceps/cep-8/) spec enabling payments, and have been pushing [SDK](https://github.com/ContextVM/sdk) improvements through February.

The SDK provides TypeScript client and server transports for MCP over Nostr. Developers can expose MCP servers across the Nostr network and clients can connect to them. Relays act like a blind message bus, just routing encrypted events blindly. Clients without native Nostr support connect through a proxy layer. The library handles relay management and cryptographic signing for event authentication. It works in both Node.js and browser environments.

[CVMI](https://github.com/ContextVM/cvmi) provides a CLI for server discovery and method invocation. [Relatr](https://github.com/ContextVM/relatr) calculates personalized trust scores from social graph distance combined with profile validation.

ContextVM positions itself as a bridge layer: existing MCP servers gain Nostr interoperability while maintaining their conventional transports.

### White Noise Documents Decentralized User Search

A [blog post from jgmontoya](https://blog.jgmontoya.com/2026/02/22/user-search.html) details how [White Noise](https://github.com/marmot-protocol/whitenoise) handles user search across the decentralized relay network.

Profile distribution creates the challenge: unlike centralized messengers with unified databases, Nostr profiles scatter across dozens of relays with no central index. White Noise solves this through a producer-consumer architecture running in parallel.

A producer process continuously expands the social graph outward from the user's follows, fetching follow lists at increasing distances and queuing discovered pubkeys for profile resolution. The consumer resolves matches through five increasingly expensive tiers: local user table (fastest), cached profiles from previous searches, connected relays, user relay lists per [NIP-65](/en/topics/nip-65/), and direct queries to user-declared relays (slowest).

Cold searches take approximately 3 seconds while warm searches from cache drop to around 10 milliseconds. For new users without established social graphs, the system injects well-connected bootstrap nodes to ensure search functionality. Group membership provides an implicit social signal alongside explicit follows.

Instrumentation proved critical for optimization, the author notes. Without metrics, improvements were guesswork.

### FIPS: Nostr-Native Mesh Networking

[FIPS](https://github.com/jmcorgan/fips) (Free Internetworking Peering System) is a working Rust implementation of a self-organizing mesh network that uses Nostr keypairs (secp256k1) as node identities. The [design documentation](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md) accompanies functional code.

The protocol addresses infrastructure independence: nodes discover each other automatically without central servers or certificate authorities. A spanning tree provides coordinate-based routing while bloom filters propagate reachability information, letting nodes make forwarding decisions with only local knowledge. Transport agnosticism means the same protocol works over UDP, Ethernet, Bluetooth, LoRa radio, or any datagram-capable medium.

Two encryption layers protect traffic. Link-layer encryption (Noise IK pattern) secures hop-by-hop communication between neighbors with mutual authentication and forward secrecy. Session-layer encryption (Noise XK pattern) provides end-to-end protection against intermediate routers, where only the destination can decrypt the payload. This mirrors how TLS protects HTTP traffic even when traversing untrusted networks.

The architecture uses a "greedy embedding" spanning tree for routing. Each node receives coordinates based on its position relative to the tree root and parent. Packets route greedily toward coordinates closer to the destination, with bloom filters advertising reachable endpoints. When greedy routing fails (local minima), nodes can fall back to tree-based paths.

The Rust implementation already includes UDP transport with bloom filter discovery. Future work targets Nostr relay integration for peer bootstrapping.

## Releases

This week brought releases across relay infrastructure and client applications, with new projects also entering the space.

### HAVEN v1.2.0

[HAVEN](https://github.com/bitvora/haven), the all-in-one personal relay bundling four relay functions with a [Blossom](/en/topics/blossom/) media server, shipped [v1.2.0](https://github.com/bitvora/haven/releases/tag/v1.2.0). This release moves beyond the RC stage [covered last week](/en/newsletters/2026-02-18-newsletter/#haven-v120-rc3).

Multi-npub support lets a single HAVEN instance serve several Nostr identities through whitelisting, with new blacklisting functionality for access control. A rewritten backup system uses portable JSONL format, with a `haven restore` command for importing notes from JSONL files. Cloud storage integration adds `--to-cloud` and `--from-cloud` flags for remote backup management.

[Web of Trust](/en/topics/web-of-trust/) improvements include configurable depth levels for trust calculations and automatic 24-hour refresh intervals with lockless optimization reducing memory overhead. User-agent configuration for relay requests and configurable Blastr timeout settings complete the release, alongside data export to compressed JSONL.

### White Noise v0.3.0

[White Noise](https://github.com/marmot-protocol/whitenoise), the [MLS](/en/topics/mls/)-based encrypted messaging app implementing the [Marmot](/en/topics/marmot/) protocol, shipped [v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) with over 160 merged improvements.

This release brings real-time messaging through streaming connections instead of polling, so messages arrive instantly. Amber support ([NIP-55](/en/topics/nip-55/)) means private keys never need to touch the app. Image sharing now works with upload progress tracking and blurhash placeholders while loading. Full-screen viewing supports pinch-to-zoom.

Group messaging received reliability improvements with chat lists showing sender names and [MLS](/en/topics/mls/) encryption ensuring forward secrecy. User search expands outward from follows up to four degrees of separation with results streaming in as found.

A breaking change resets all local data on upgrade due to Marmot protocol changes and the switch to encrypted local storage. Users should back up nsec keys before upgrading.

### diVine 1.0.5

[diVine](https://github.com/divinevideo/divine-mobile), the short-form looping video client built on restored Vine archives, shipped [1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) with extensive video playback fixes and a new decentralized analytics system.

Video playback issues dominated the fixes: phantom pause, dual audio between videos, black flash between thumbnails and first frames, and disposed player crashes are all resolved. A pooled video player now handles the Home feed for consistent playback.

Kind 22236 ephemeral view events enable creator analytics and recommendations. The system tracks traffic sources (home, discovery variants, profile, share, search) and loop counts while filtering out self-views. Local file path leaks in Nostr event imeta tags are fixed with canonical Blossom URLs constructed client-side per BUD-01 spec.

[NIP-46](/en/topics/nip-46/) remote signer improvements include parallelized relay connections and callback URL support. Android reconnects WebSocket connections on app resume after signer approval.

### Coracle 0.6.30

[Coracle](https://github.com/coracle-social/coracle), the web-based Nostr client focused on relay management and [Web of Trust](/en/topics/web-of-trust/) moderation, shipped [0.6.30](https://github.com/coracle-social/coracle/releases/tag/0.6.30) with video thumbnail support, improving media browsing in feeds.

### Nostur v1.26.0

[Nostur](https://github.com/nostur-com/nostur-ios-public), the iOS Nostr client, shipped [v1.26.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.26.0) with a new Live Streams feed section and a redesigned Settings screen. GIFs can now host on Blossom media servers, reducing reliance on centralized services. Klipy GIFs integration provides backup when Tenor becomes unavailable. Year headers in DM conversations and mention count display round out the user-facing changes.

Developer tooling and CLI apps also received updates this week.

### nak v0.18.5

[nak](https://github.com/fiatjaf/nak), fiatjaf's command-line Swiss Army knife for Nostr, shipped [v0.18.5](https://github.com/fiatjaf/nak/releases/tag/v0.18.5) with a new `nak profile` subcommand for fetching and displaying user profiles. The `git clone` command now supports [NIP-05](/en/topics/nip-05/) names in `nostr://` URIs, enabling repository cloning by human-readable identifiers.

### Pika v0.5.3

[Pika](https://github.com/sledtools/pika), the [MLS](/en/topics/mls/)-encrypted messenger for iOS, Android, and desktop built on the [Marmot](/en/topics/marmot/) protocol, shipped [v0.5.3](https://github.com/sledtools/pika/releases/tag/pikachat-v0.5.3). Recent commits add file upload and drag-and-drop media support to the desktop app, alongside Cloudflare Workers deployment fixes.

Pika uses a Rust core that owns all business logic while iOS (SwiftUI) and Android (Kotlin) act as thin UI layers rendering state snapshots. MDK (Marmot Development Kit) provides the MLS implementation. The project notes alpha status and warns against use for sensitive workloads.

### Ridestr v0.2.6

[Ridestr](https://github.com/variablefate/ridestr), the decentralized rideshare platform with Cashu payments, shipped [v0.2.6](https://github.com/variablefate/ridestr/releases/tag/v0.2.6). This release fixes TalkBack accessibility issues and resolves bugs where drivers disappeared from the nearby list when switching payment methods or where selected driver counts failed to update when drivers went offline.

The "Send to All" feature is now "Broadcast RoadFlare" with fixes for silent failures on fresh driver installs. Ridestr implements HTLC escrow for trustless ride payments and [NIP-60](/en/topics/nip-60/) wallet sync across devices.

### Unfiltered v1.0.6

[Unfiltered](https://github.com/dmcarrington/unfiltered), the Instagram-like photo-sharing app for Android, shipped [v1.0.6](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.6) with improved user search and automatic relay reconnection every 60 seconds.

Built with Kotlin and Jetpack Compose, Unfiltered uses rust-nostr bindings and Blossom-compatible servers for image hosting. Amber integration ([NIP-55](/en/topics/nip-55/)) handles secure key management. The app shows posts from followed accounts in chronological order without algorithms or ads.

Two new messaging and signing projects also launched this week.

### Burrow: MLS Messaging for AI Agents

[Burrow](https://github.com/CentauriAgent/burrow) is a messenger implementing the [Marmot](/en/topics/marmot/) protocol for MLS-encrypted communication without phone numbers or centralized servers. Both human users and AI agents can participate.

A pure Rust CLI daemon with JSONL output mode handles integration with automated systems. A Flutter cross-platform app covers Android, iOS, Linux, macOS, and Windows. Media attachments encrypt alongside messages, and WebRTC handles audio and video calls with configurable TURN servers.

Burrow layers MLS encryption on Nostr infrastructure. Identity uses Nostr keypairs (secp256k1) while MLS KeyPackages publish as kind 443 events. Messages encrypt with [NIP-44](/en/topics/nip-44/) as kind 445 events, and welcome invitations use [NIP-59](/en/topics/nip-59/) gift-wrapping.

[OpenClaw](https://openclaw.ai) integration enables AI agent participation with full tool access. Access control lists with audit logging manage contact and group permissions. This combination positions Burrow for agent-to-agent and agent-to-human messaging scenarios requiring Signal-level encryption on decentralized infrastructure.

### Nostria Signer Extension

[Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) is a Chromium-based browser extension providing vault and identity management for Nostr users.

Multiple vaults containing multiple accounts let users organize identities for different contexts. Internationalization includes RTL language support. Built with Angular and TypeScript (79.2% of the codebase), it works as both a browser extension and Progressive Web App.

Nostria Signer implements [NIP-07](/en/topics/nip-07/) for browser extension signing, enabling web-based Nostr clients to request event signatures without accessing private keys directly. Automated wallet migration handles updates distributed through the Chrome Web Store. Users can also sideload from the `dist/extension` folder.

Developers emphasize the experimental status: users must manage their own secret recovery phrases since the developers cannot restore access to lost keys.

## Project Updates

### Formstr Migrates to New Organization

[Formstr](https://github.com/formstr-hq/nostr-forms), the Google Forms alternative on Nostr, migrated its repository from `abh3po/nostr-forms` to the `formstr-hq` organization. This OpenSats grant recipient continues development at the new location.

### Notable Open PRs

Work in progress across Nostr projects:

- **Damus Outbox Model** ([PR #3602](https://github.com/damus-io/damus/pull/3602)): Implementation plan for the gossip/outbox relay model on iOS. This architectural change improves message delivery by publishing to the relays where recipients actually read.

- **Notedeck Cross-Platform Notifications** ([PR #1296](https://github.com/damus-io/notedeck/pull/1296)): Native notification system for the Damus desktop client covering Android FCM, macOS, and Linux.

- **NDK Cashu v3 Upgrade** ([PR #370](https://github.com/nostr-dev-kit/ndk/pull/370)): Updates the Nostr Development Kit's wallet integration to cashu-ts v3.

- **Zeus Cashu Offline** ([PR #3742](https://github.com/ZeusLN/zeus/pull/3742)): Offline ecash sending and receiving for the Zeus Lightning wallet.

- **Shopstr Encrypted Digital Delivery** ([PR #231](https://github.com/shopstr-eng/shopstr/pull/231)): Adds encrypted delivery for digital goods with dynamic weight support for physical items.

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged This Week:**

- **[NIP-85 Service Provider Discoverability](https://github.com/nostr-protocol/nips/pull/2223)**: The [NIP-85](/en/topics/nip-85/) spec now includes guidance on how clients discover trusted assertion providers. When a client needs [Web of Trust](/en/topics/web-of-trust/) scores or other computed metrics, it can query relays for kind 30085 announcements from providers the user already follows or trusts.

- **[NIP-29 Removes Unmanaged Groups](https://github.com/nostr-protocol/nips/pull/2229)**: The [NIP-29](/en/topics/nip-29/) group chat spec dropped support for unmanaged groups (where any member could add others). All NIP-29 groups now require relay-side management with explicit admin roles, simplifying implementations and reducing spam vectors.

- **[NIP-11 Removes Deprecated Fields](https://github.com/nostr-protocol/nips/pull/2231)**: [NIP-11](/en/topics/nip-11/) relay information documents no longer include the deprecated `software` and `version` fields. Implementations should remove these from their responses.

- **[NIP-39 Moves Identity Tags](https://github.com/nostr-protocol/nips/pull/2227)**: External identity claims ([NIP-39](/en/topics/nip-39/) `i` tags for GitHub, Twitter, etc.) moved from kind 0 profiles to dedicated kind 30382 events. This separates identity verification from profile metadata.

**AI Agent NIPs Progress:**

Four AI-focused NIPs continue active development. Since [last week's coverage](/en/newsletters/2026-02-18-newsletter/#ai-agent-nips-arrive):

- **[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220)** (updated Feb 19): Defines agent identity with kind 4199 for agent definitions and kind 4201 for prompting ("nudges"). Agents can reference [NIP-94](/en/topics/nip-94/) file metadata for extended descriptions.

- **[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)** (updated Feb 18): Standardizes conversational messaging with seven ephemeral event kinds (25800-25806) for status, streaming deltas, prompts, responses, tool calls, errors, and cancellation. Kind 31340 "AI Info" events let agents advertise supported models and capabilities.

- **[NIP-AC: DVM Agent Coordination](https://github.com/nostr-protocol/nips/pull/2228)** (opened Feb 18): Extends [NIP-90](/en/topics/nip-90/) for autonomous agent workflows. Adds heartbeats for agent discovery, job reviews for quality tracking, data escrow for result commitment, workflow chains for multi-step pipelines, and swarm bidding for competitive provider selection. A reference implementation runs at 2020117.xyz.

- **[NIP-AD: MCP Server Announcements](https://github.com/nostr-protocol/nips/pull/2221)** (opened Feb 12): Standardizes announcement of Model Context Protocol servers and skills on Nostr. Already in use on the TENEX platform.

**Other Open PRs:**

- **[NIP-144: Service Authorization Protocol](https://github.com/nostr-protocol/nips/pull/2232)**: Defines how clients prove identity and permissions to service providers on Nostr.

- **[NIP-DC: Nostr Webxdc](https://github.com/nostr-protocol/nips/pull/2230)**: alexgleason proposes integrating Webxdc (decentralized web applications) with Nostr events.

## NIP Deep Dive: NIP-55 (Android Signer Application)

[NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md) defines how Android Nostr clients request cryptographic operations from dedicated signer applications. With [White Noise v0.3.0](#white-noise-v030) and [Unfiltered v1.0.6](#unfiltered-v106) both adding Amber support this week, the Android signing protocol warrants examination.

**Communication Channels:**

NIP-55 enables inter-app signing through two mechanisms. Intents provide manual user approval with visual feedback for one-time operations. Content Resolvers enable automated signing when users grant persistent permissions, letting apps sign in the background without repeated prompts.

Communication uses the custom `nostrsigner:` URI scheme. A client initiates contact with:

```
nostrsigner:<base64-encoded-event>?type=sign_event&callbackUrl=myapp://callback
```

**Supported Operations:**

The spec defines seven cryptographic methods: event signing (`sign_event`), public key retrieval (`get_public_key`), [NIP-04](/en/topics/nip-04/) encryption/decryption, [NIP-44](/en/topics/nip-44/) encryption/decryption, and zap event decryption (`decrypt_zap_event`).

**Permission Model:**

Clients call `get_public_key` once to establish a trust relationship, receiving the signer's package name and user pubkey. The spec mandates that clients save these values and never call `get_public_key` again, preventing fingerprinting attacks.

For signing requests, users can approve once or grant "remember my choice" for background operations. If users consistently reject operations, the signer returns a "rejected" status, preventing repeated prompts.

**Implementations:**

[Amber](https://github.com/greenart7c3/amber) is the primary NIP-55 signer for Android. Clients supporting NIP-55 include [Amethyst](https://github.com/vitorpamplona/amethyst), [White Noise](#white-noise-v030), [Unfiltered](#unfiltered-v106), and others. Web applications cannot directly receive signer responses and must use callback URLs or clipboard operations.

**Relationship to Other Signing NIPs:**

NIP-55 complements [NIP-07](/en/topics/nip-07/) (browser extensions) and [NIP-46](/en/topics/nip-46/) (remote signing over relays). Where NIP-07 handles desktop browsers and NIP-46 handles cross-device signing, NIP-55 provides native Android integration with minimal latency.

## NIP Deep Dive: NIP-60 (Cashu Wallet)

[NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md) defines how [Cashu](/en/topics/cashu/) ecash wallets store state on Nostr relays, enabling cross-application wallet synchronization. With [Ridestr v0.2.6](#ridestr-v026) using NIP-60 for wallet sync across devices, the protocol deserves examination.

**Event Kinds:**

NIP-60 uses four event types. The replaceable kind 17375 stores wallet configuration including mint URLs and a dedicated private key for receiving P2PK ecash payments. Token events (kind 7375) contain unspent cryptographic proofs, while spending history (kind 7376) records transactions for user transparency. An optional kind 7374 tracks mint payment quotes.

**Wallet Architecture:**

Wallet state lives on relays, making it accessible across applications. A user's wallet event contains encrypted references to Cashu mints and a wallet-specific private key separate from the user's Nostr identity. This separation matters: the wallet key handles ecash operations while the Nostr key handles social functions.

```json
{
  "kind": 17375,
  "content": "<nip44-encrypted-wallet-config>",
  "tags": [["d", "cashu-wallet"]]
}
```

**Proof Management:**

Cashu proofs are bearer instruments. Once spent, a proof becomes invalid. NIP-60 manages this through a rollover mechanism: when spending, clients create a new token event with remaining unspent proofs and delete the original via [NIP-09](/en/topics/nip-09/). Destroyed token IDs go in a `del` field for state tracking.

Clients should periodically validate proofs against mints to detect previously-spent credentials. Multiple token events per mint are permitted, and spending history events help users track transactions even though they're optional.

**Security Model:**

All sensitive data uses [NIP-44](/en/topics/nip-44/) encryption. The wallet private key never appears in plaintext. Since relays store encrypted blobs without understanding their contents, wallet state remains private even on untrusted relays.

**Implementations:**

Wallets supporting NIP-60 include [Nutsack](https://github.com/gandlafbtc/nutsack) and [eNuts](https://github.com/cashubtc/eNuts). Clients like [Ridestr](#ridestr-v026) use NIP-60 for cross-device sync, letting users top up on desktop and spend from mobile without manual transfers.

---

That's it for this week. Building something or have news to share? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via [NIP-17](/en/topics/nip-17/) DM</a> or find us on Nostr.
