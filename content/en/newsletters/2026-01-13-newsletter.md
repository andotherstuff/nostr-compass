---
title: 'Nostr Compass #5'
date: 2026-01-13
publishDate: 2026-01-13
draft: false
type: newsletters
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** Bitchat undergoes a professional security audit by Cure53, the same firm that audited Signal and [NIP-44](/en/topics/nip-44/), with 17+ PRs already merged fixing critical findings. [NIP-71](/en/topics/nip-71/) is merged, bringing addressable video events to the protocol. A post-quantum cryptography NIP opens discussion on future-proofing Nostr against quantum attacks. Amethyst v1.05.0 ships bookmark lists, voice notes, and an early desktop release, while Nostur v1.25.3 improves [NIP-17](/en/topics/nip-17/) DMs with reactions and replies. In library news, rust-nostr expands [NIP-62](/en/topics/nip-62/) support across SQLite and LMDB backends, and NDK fixes a subscription tracking bug.

## News

### Bitchat Completes Cure53 Security Audit

Bitchat, the iOS encrypted messenger combining Nostr with [Cashu](/en/topics/cashu/), has undergone a professional security audit by Cure53, one of the most respected security firms in the industry. Cure53 previously audited Signal, Mullvad VPN, and notably the [NIP-44](/en/topics/nip-44/) encryption specification that underpins modern Nostr private messaging.

The audit found 12+ security issues (BCH-01-002 through BCH-01-013). The Bitchat team responded with 17+ pull requests. Key fixes include:

**Noise Protocol DH Secret Clearing** - [PR #928](https://github.com/permissionlesstech/bitchat/pull/928) fixes six locations where Diffie-Hellman shared secrets were not being zeroed after key agreement, restoring forward secrecy guarantees. When secrets persist in memory longer than necessary, a memory dump or cold boot attack could compromise past communications.

**Signature Verification** - Multiple PRs harden cryptographic verification paths, ensuring message authenticity checks cannot be bypassed through malformed inputs.

**Thread Safety** - [PR #929](https://github.com/permissionlesstech/bitchat/pull/929) adds barrier synchronization to read receipt queues in NostrTransport, preventing race conditions that could cause data corruption or crashes under high message volumes.

**Memory Safety** - [PR #920](https://github.com/permissionlesstech/bitchat/pull/920) optimizes the message deduplicator for better performance with high message throughput while avoiding memory exhaustion.

**Input Validation** - [PR #919](https://github.com/permissionlesstech/bitchat/pull/919) hardens hex string parsing to prevent crashes from malformed input, a common attack vector for denial-of-service.

Bitchat handles [Cashu](/en/topics/cashu/) ecash, making professional security review essential. The audit follows last year's [Marmot](/en/topics/marmot/) Protocol audit and the NIP-44 audit that verified the encryption layer.

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-71](/en/topics/nip-71/)** - Addressable Video Events ([#1669](https://github.com/nostr-protocol/nips/pull/1669)) introduces kinds 34235 (horizontal video) and 34236 (vertical video) as addressable events. A required `d` tag provides unique identifiers, so video metadata can be updated without republishing the entire event. An optional `origin` tag tracks import sources. Already implemented in Amethyst and nostrvine.

**Open PRs:**

- **Post-Quantum Cryptography** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) proposes adding quantum-resistant cryptographic algorithms to Nostr. The spec introduces ML-DSA-44 and Falcon-512 for digital signatures, targeting "super-high value events" like applications and authorities rather than individual users. While [NIP-44](/en/topics/nip-44/)'s symmetric encryption (ChaCha20) is quantum-resistant, its key exchange uses secp256k1 ECDH which is vulnerable to Shor's algorithm. The proposal includes ML-KEM for key agreement to address this gap. This is an early-stage proposal opening discussion on crypto-agility for Nostr's long-term security.
- **BOLT12 for NIP-47** - After 137 comments and extensive discussion, the community decided that BOLT12 offers deserve their own specification rather than extending [NIP-47](/en/topics/nip-47/). BOLT12 offers provide significant upgrades over BOLT11 invoices including reusability, better privacy through blinded paths, and optional payer information. The new NIP will define methods like `make_offer`, `pay_offer`, and `list_offers` for Nostr Wallet Connect implementations.
- **Audio Track NIP** - [PR #1043](https://github.com/nostr-protocol/nips/pull/1043) proposes kinds 32100 for music tracks and 32101 for podcast episodes, giving audio content the same first-class treatment that NIP-71 provides for video. Currently, audio platforms like Wavlake, Zapstr, and Stemstr each use proprietary event formats, fragmenting the ecosystem. A common standard would enable interoperability so users could discover and play audio from any compatible client.
- **NIP-A3 Universal Payment Targets** - [PR #2119](https://github.com/nostr-protocol/nips/pull/2119) proposes kind 10133 events using RFC-8905 `payto:` URIs to expose payment options across multiple networks. Rather than creating separate event kinds for Bitcoin, Lightning, [Cashu](/en/topics/cashu/), or traditional payment rails, this abstraction lets clients parse standardized tags and invoke native payment handlers. The approach is future-proof since new payment methods just need a `payto:` URI scheme.

## NIP Deep Dive: NIP-51 and NIP-65

This week we cover two NIPs that store user preferences: NIP-51 for organizing content, and NIP-65 for organizing relay connections. Both use replaceable events, meaning each new publication overwrites the previous version.

### [NIP-51](/en/topics/nip-51/): Lists

[NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md) defines multiple list types for organizing references to events, users, hashtags, and other content. Amethyst v1.05.0 adds bookmark support, making this a good time to understand how lists work.

The spec defines several list kinds, each serving a different purpose. Kind 10000 is your mute list for hiding users, threads, or words. Kind 10001 pins events to feature on your profile. Kind 30003 stores bookmarks, which is what Amethyst now supports. Other kinds handle follow sets (30000), curated article collections (30004), hashtag interests (30015), and custom emoji sets (30030).

Lists reference content through tags. A bookmark list uses `e` tags for specific events and `a` tags for addressable content like articles:

```json
{
  "id": "ae3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 30003,
  "tags": [
    ["d", "saved-articles"],
    ["e", "abc123def456...", "wss://relay.example"],
    ["a", "30023:author-pubkey:article-id", "wss://relay.example"]
  ],
  "content": "<encrypted-private-bookmarks>",
  "sig": "908a15e46fb4d8675bab026fc230a0e3542bfade63da02d542fb78b2a8513fcd0092619a2c8c1221e581946e0191f2af505dfdf8657a414dbca329186f009262"
}
```

The `d` tag provides a unique identifier, so you can maintain multiple bookmark sets like "saved-articles", "read-later", or "favorites" under the same kind.

Lists support both public and private items. Public items appear in the tags array, visible to anyone who fetches the event. Private items go in the `content` field, encrypted using [NIP-44](/en/topics/nip-44/) to yourself. This dual structure lets you keep public bookmarks while attaching private notes, or maintain a mute list without revealing who you've muted. To encrypt to yourself, use NIP-44 with your own pubkey as recipient.

The 10000-series kinds are replaceable, meaning relays keep only one event per pubkey. The 30000-series are parameterized replaceable, allowing one event per pubkey and `d` tag combination. In both cases, updating a list means publishing a complete replacement; you cannot send incremental changes. Clients should preserve unknown tags when modifying lists to avoid overwriting data added by other applications.

### [NIP-65](/en/topics/nip-65/): Relay List Metadata

[NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) defines kind 10002 events that advertise which relays a user prefers for reading and writing. This helps other users and clients find your content.

```json
{
  "id": "bd2217a96b5835b59f9a6a42d8d8a36f8c9b7d4e5f0a1b2c3d4e5f6a7b8c9d0e1",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "f1c2d3e4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2"
}
```

Each `r` tag contains a relay URL and an optional marker. A `write` marker designates your outbox: relays where you publish your content. A `read` marker designates your inbox: relays where you check for mentions, replies, and tags. Omitting the marker indicates both.

When Alice wants to find Bob's posts, her client fetches Bob's kind 10002, extracts his write relays (his outbox), and subscribes there. When Alice replies to Bob, her client publishes to his read relays (his inbox) so he'll see the mention. This relay-aware routing is the "outbox model," and it distributes users across many relays rather than concentrating everyone on a few central servers.

NIP-65 handles public content routing, but private messages use a separate list. [NIP-17](/en/topics/nip-17/) defines kind 10050 for DM inbox relays, using `relay` tags instead of `r` tags. When sending someone a private message, clients look for the recipient's kind 10050 event and publish the encrypted gift-wrapped message there. This separation keeps DM routing distinct from public content routing, and lets users specify different relays for private versus public communication.

The outbox model improves censorship resistance since no single relay needs to store or serve everyone's content. Clients maintain connections to relays listed in their followed users' NIP-65 events, dynamically connecting to new relays as they discover new accounts. NIP-65 complements the relay hints found in other NIPs. When you tag someone with `["p", "pubkey", "wss://hint.relay"]`, the hint tells clients where to look for that specific reference. NIP-65 provides the authoritative, user-controlled list, while hints offer shortcuts embedded in individual events.

For best results, keep your relay list current since stale entries make you harder to find. The spec recommends two to four relays per category. Listing too many relays burdens every client that wants to fetch your content, slowing down their experience and increasing network load. Clients cache NIP-65 events and refresh them periodically to stay current as users update their preferences.

## Releases

**Amethyst v1.05.0** - The popular Android client [ships a major update](https://github.com/vitorpamplona/amethyst/releases) with several headline features. [NIP-51](/en/topics/nip-51/) kind 30003 bookmark lists let users save posts for later reference, syncing across compatible clients. Voice notes now work in DMs and regular posts with waveform visualization, media server selection, and upload progress indicators. [Web of Trust](/en/topics/web-of-trust/) scores are now visible in the interface, helping users understand how the algorithm evaluates accounts relative to their social graph. The [Quartz](/en/topics/quartz/) database migration improves query performance as part of the OpenSats-funded Kotlin Multiplatform work. An early desktop release brings Amethyst to Windows, macOS, and Linux via Compose Multiplatform, sharing the same codebase as the Android app. New user onboarding flows smooth the experience for first-time Nostr users.

**Nostur v1.25.3** - The iOS and macOS client [focuses on private messaging](https://github.com/nostur-com/nostur-ios-public/releases) with [NIP-17](/en/topics/nip-17/) improvements. DM conversations now support reactions and replies, bringing the interactivity of public posts into encrypted messages. The conversation view has been reworked with better threading so multi-message exchanges are easier to follow, and timestamps show "time ago" in the DM list for quick scanning. Desktop users get multi-column layouts for viewing multiple feeds or conversations side by side. [NIP-46](/en/topics/nip-46/) remote signer support allows users to keep their private keys in dedicated signer apps like Amber or nsec.app. Additional fixes restore DM functionality on iOS 15 and iOS 16, resolve notification delays, and add the ability to configure which relays receive published DMs.

## Notable code and documentation changes

*These are open pull requests and early-stage work, perfect for getting feedback before they merge. If something catches your eye, consider reviewing or commenting!*

### Citrine (Android Relay)

[PR #89](https://github.com/greenart7c3/Citrine/pull/89) fixes a SQL injection vulnerability in the Android personal relay app. The issue allowed malformed event data to execute arbitrary database queries, a serious flaw for any app that stores and processes untrusted input. The fix properly sanitizes all database operations using parameterized queries. No release has been tagged yet, so users will need to wait for the next version or build from source. [PR #90](https://github.com/greenart7c3/Citrine/pull/90) optimizes ContentProvider query performance with database-level filtering and pagination, reducing latency when external apps like Amethyst access Citrine's event database through Android's inter-process communication layer.

### rust-nostr (Library)

[NIP-62](/en/topics/nip-62/) (Vanish Requests) support is expanding across rust-nostr's database backends. [PR #1180](https://github.com/rust-nostr/nostr/pull/1180), merged two weeks ago, added NIP-62 support to SQLite, handling `ALL_RELAYS` vanish requests since the database layer doesn't know specific relay URLs. [PR #1210](https://github.com/rust-nostr/nostr/pull/1210) extends this to the LMDB backend, ensuring vanish requests are persisted to disk and survive relay restarts. An IndexedDB implementation for browser environments is also in progress. Together, these changes give developers consistent NIP-62 support across SQLite, LMDB, and soon browser storage.

### NDK (Nostr Development Kit)

[PR #375](https://github.com/nostr-dev-kit/ndk/pull/375) fixes a bug in the seenEvents tracking system. The issue caused certain subscription patterns to incorrectly mark events as already seen, leading to missed content when users opened new subscriptions or reconnected to relays. The fix ensures events are tracked accurately across subscription lifecycles, which is particularly important for applications that dynamically subscribe and unsubscribe based on user navigation. NDK bumped to beta.70 with this fix included.

### Damus (iOS)

[PR #3515](https://github.com/damus-io/damus/pull/3515) fixes a startup crash affecting iOS 17 users. The issue stemmed from an arithmetic overflow in `NdbUseLock`, a fallback class used because Swift Mutexes aren't available on iOS 17. The fix replaces the previous synchronization approach with `NSLock`, which is available on iOS 17 and handles the remaining race conditions properly. iOS 18+ users weren't affected since they have access to the native Swift Mutex implementation.

Separately, a batch of longform article improvements landed via [PR #3509](https://github.com/damus-io/damus/pull/3509). Reading progress bars track your position through articles, estimated read times appear on previews, and sepia mode with adjustable line height settings provide more comfortable reading. Focus mode auto-hides the navigation chrome when scrolling down and restores it on tap, reducing visual clutter for distraction-free reading. Several fixes address image display in markdown content and ensure articles open at the top rather than midway through.

### Zap.stream (Live Streaming)

YouTube and Kick chat integration bridges messages from external streaming platforms into Nostr. Streamers who multicast to YouTube, Kick, and Zap.stream can now see all chat messages in a unified view, with messages from each platform appearing alongside native Nostr comments. This removes a major friction point for creators who want to use Nostr for streaming but can't abandon audiences on established platforms. The integration displays which platform each message originated from and handles the authentication flow for connecting external accounts.

### Chachi (NIP-29 Groups)

The [NIP-29](/en/topics/nip-29/) group chat client shipped six merged PRs this week. A security update addresses [CVE-2026-22029](https://github.com/purrgrammer/chachi/pull/89), an XSS vulnerability in react-router that could enable open redirect attacks; the fix updates to react-router-dom 6.30.0. [PR #92](https://github.com/purrgrammer/chachi/pull/92) adds paginated message loading for group chats, so long conversations load incrementally rather than all at once. [PR #91](https://github.com/purrgrammer/chachi/pull/91) fixes several NIP-29 bugs including a race condition that caused blank group names on initial load and undefined participant lists that crashed member views. Translation coverage now spans all 31 supported locales with 1060 keys each.

### 0xchat (Messaging)

The Telegram-style messaging client improved [NIP-55](/en/topics/nip-55/) compliance by properly saving signer package names when using external signing apps, fixing issues where the app would lose track of which signer to use after restarts. NIP-17 reply handling now correctly includes the `e` tag for threading, ensuring replies appear in the right conversation context across clients. Performance optimizations address scroll lag in message lists, a common pain point when loading long chat histories. Draft auto-save prevents message loss if you navigate away mid-composition, and file storage options now include default FileDropServer and BlossomServer endpoints.

### Primal (iOS)

[NIP-46](/en/topics/nip-46/) remote signer support lands on iOS via [PR #184](https://github.com/PrimalHQ/primal-ios-app/pull/184), completing the cross-platform rollout that started with Android several weeks ago. Users can now keep their private keys in dedicated bunker services like nsec.app or self-hosted nsecBunker instances, connecting over Nostr relays to sign events without exposing keys to the client app. This separation improves security posture for users who want to use Primal's features while maintaining stricter key management practices. The implementation includes QR code scanning for bunker connection URIs and handles the NIP-46 request/response flow over encrypted relay messages.

---

That's it for this week. Building something? Have news to share? Want us to cover your project? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via NIP-17 DM</a> or find us on Nostr.
