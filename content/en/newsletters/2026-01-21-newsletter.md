---
title: 'Nostr Compass #6'
date: 2026-01-21
publishDate: 2026-01-21
draft: false
type: newsletters
---

Welcome back to Nostr Compass, your weekly guide to Nostr.

**This week:** Bitchat replaces C Tor with the Rust Arti implementation for better reliability and performance. nostrdb-rs gains streaming fold queries that enable zero-allocation database operations. Listr receives a major refactor with NDK 3 beta migration and AI-assisted maintenance after a year of dormancy. Zeus ships 17 merged PRs focused on [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect for remote Lightning control) fixes and [Cashu](/en/topics/cashu/) improvements, while Primal Android adds wallet backup flows and [NIP-92](/en/topics/nip-92/) (media dimensions for proper aspect ratios) support. A new draft NIP proposes [Trusted Relay Assertions](/en/topics/trusted-relay-assertions/) for standardized relay trust scoring.

## News

### Bitchat Moves to Rust Arti for Tor Support

Bitchat has migrated from C Tor to [Arti](https://gitlab.torproject.org/tpo/core/arti), the Rust implementation of the Tor protocol. [PR #958](https://github.com/permissionlesstech/bitchat/pull/958) removes the C Tor dependency and integrates Arti, bringing memory safety guarantees and improved reliability. The change eliminates dormant wake attempts that caused foreground service restarts, a longstanding issue with the C implementation.

**What this means for users:** More stable encrypted messaging with fewer disconnections, especially on mobile devices. The Rust implementation reduces crash risks and battery drain from constant reconnection attempts.

Arti is a ground-up rewrite of Tor in Rust, developed by the Tor Project to provide better security through memory safety and easier integration into applications. For Bitchat, the memory safety properties reduce attack surface when handling encrypted messages and relay connections. The migration follows the team's recent [Cure53 security audit](/en/newsletters/2026-01-13-newsletter/#bitchat-completes-cure53-security-audit) (covered in Newsletter #5), continuing their security improvements.

The PR also introduces comprehensive test coverage for ChatViewModel and BLEService, removes dead code, and stabilizes the test suite. Bluetooth Low Energy mesh reliability improvements accompany the Tor changes, addressing large transfer failures. Together, these changes improve Bitchat's resilience for offline mesh networking scenarios where Tor provides internet connectivity alongside local BLE communication.


### Listr Revitalized with AI-Powered Maintenance

JeffG announced a major refactor of [Listr](https://github.com/erskingardner/listr), the Nostr list management application available at [listr.lol](https://listr.lol), after the project had been dormant for over a year. Using AI assistance, he completed a comprehensive upgrade including migration to [NDK](https://github.com/nostr-dev-kit/ndk) 3 beta, updates to latest versions of Svelte and Vite, and all dependencies brought current. The refactor adds first-class support for following packs, implements pagination for lists exceeding 50 items, and fixes numerous bugs that had accumulated during the dormant period.

**What this means for users:** Listr is back online with improved performance and new features for managing follow lists, content collections, and topic curation. The pagination fix makes large lists actually usable.

JeffG noted that without AI assistance, this maintenance work would likely never have happened, preventing the project from becoming abandoned. Listr enables content curation on Nostr, allowing users to create, manage, and share lists of profiles, topics, and resources. The upgrade keeps the application compatible with current Nostr standards and client expectations as list management becomes more central to content discovery on the protocol.


## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-29](/en/topics/nip-29/)** (Relay-based groups) - Relay Key Clarification ([#2190](https://github.com/nostr-protocol/nips/pull/2190) - merged) clarifies that the relay key is the relay URL itself, not a pubkey. The spec now explicitly states "The relay key is the relay's WebSocket URL (e.g., wss://groups.example.com)" to avoid confusion. This affects how clients identify which relay hosts a given group, ensuring groups are properly attributed to their hosting relays.

**Open PRs and Discussions:**

- **Trusted Relay Assertions** - A draft NIP proposes standardizing relay trust scoring through kind 30385 events containing trust scores (0-100) computed from [NIP-66](/en/topics/nip-66/) (relay discovery and monitoring) metrics, operator reputation, and user reports. The specification divides trust into reliability (uptime, latency), quality (TLS, documentation, operator verification), and accessibility (jurisdiction, barriers, surveillance risk) components. Operator verification includes cryptographic signatures via [NIP-11](/en/topics/nip-11/) (relay information documents), DNS TXT records, and .well-known files. Users declare trusted assertion providers via kind 10385 events, enabling clients to query multiple providers for diverse perspectives. The proposal complements [NIP-66](/en/topics/nip-66/) discovery with evaluation, helping [NIP-46](/en/topics/nip-46/) (remote signing/Nostr Connect) assess relay trustworthiness in connection URIs.

- **Post-Quantum Cryptography** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) (open) continues evolving since [Newsletter #5](/en/newsletters/2026-01-13-newsletter/#nip-updates) introduced the proposal for quantum-resistant algorithms. This week's discussion focused on implementation details for crypto-agility: how clients handle dual signatures during migration, backward compatibility for older clients, and performance implications of larger quantum-resistant signatures. Contributors debated whether to mandate ML-DSA-44 only or support multiple algorithms (ML-DSA-44, Falcon-512, Dilithium) for flexibility. The consensus leans toward a phased approach: optional quantum signatures initially, becoming mandatory only after widespread client support and real quantum threat emergence.


## NIP Deep Dive: NIP-11 and NIP-66

This week we examine two NIPs that work together to enable relay discovery and evaluation: NIP-11 defines how relays describe themselves, and NIP-66 standardizes how we measure relay behavior. Together they form the foundation for relay trust evaluation systems.

### [NIP-11](/en/topics/nip-11/): Relay Information Document

[NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md) defines a JSON document that relays serve over HTTP to describe their capabilities, policies, and operator information. When a client connects to `wss://relay.example.com`, it can fetch `https://relay.example.com` (replacing `wss://` with `https://`) to retrieve the relay's information document.

The document uses standard HTTP content negotiation with the `Accept: application/nostr+json` header. This allows relays to serve their normal website to browsers while providing machine-readable metadata to Nostr clients. The response includes relay software name and version, operator contact information (pubkey, email, alternative contact), supported NIPs, and operational parameters like payment requirements or content restrictions.

Importantly, basic NIP-11 documents are unsigned JSON served over HTTPS, relying solely on TLS certificates for authenticity. This means anyone controlling the relay's web server can modify the document, making operator claims unverifiable. The Trusted Relay Assertions proposal addresses this gap by introducing signed attestations through a relay's `self` pubkey field, enabling cryptographic proof of operator identity similar to how relays use signed events for authentication mechanisms.

```json
{
  "name": "relay.example.com",
  "description": "A general-purpose public relay",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "contact": "admin@example.com",
  "supported_nips": [1, 2, 4, 9, 11, 12, 16, 20, 22],
  "software": "git+https://github.com/relay/relay.git",
  "version": "1.2.3",
  "limitation": {
    "max_message_length": 16384,
    "max_subscriptions": 20,
    "max_filters": 100,
    "max_limit": 5000,
    "max_subid_length": 100,
    "min_prefix": 4,
    "max_event_tags": 2000,
    "max_content_length": 8196,
    "min_pow_difficulty": 0,
    "auth_required": false,
    "payment_required": false
  },
  "payments_url": "https://relay.example.com/payments",
  "fees": {
    "admission": [{"amount": 5000, "unit": "msats"}],
    "subscription": [{"amount": 1000, "unit": "msats", "period": 2592000}],
    "publication": []
  }
}
```

The `limitation` object tells clients what constraints the relay enforces. `max_message_length` limits WebSocket frame size, `max_subscriptions` caps concurrent REQ subscriptions per connection, `max_filters` limits filters per REQ, and `max_limit` constrains how many events a single filter can request. These parameters help clients adapt their behavior to relay capabilities, avoiding disconnections from exceeding limits.

Payment information appears in `fees` and `payments_url`. Relays can charge for admission (one-time access), subscription (recurring access), or publication (per-event fees). The `payments_url` points to details about payment methods, typically Lightning invoices or ecash mints. Paid relays use these fields to communicate pricing before clients attempt authentication.

The `supported_nips` array lets clients discover relay capabilities. If a relay lists [NIP-50](/en/topics/nip-50/), clients know they can send full-text search queries. If [NIP-42](/en/topics/nip-42/) appears, clients should expect authentication challenges. This declarative capability advertisement enables progressive enhancement: clients can use advanced features where available while gracefully degrading on relays with limited support.

Operator information builds accountability. The `pubkey` field identifies the relay operator on Nostr, enabling direct communication via [NIP-17](/en/topics/nip-17/) DMs or public mentions. The `contact` email provides an off-protocol fallback. Together, these fields help users reach operators for abuse reports, access requests, or technical issues.

[NIP-11](/en/topics/nip-11/) documents are self-reported: relays describe what they claim to support, not necessarily what they actually do. This is where NIP-66 becomes important.

### [NIP-66](/en/topics/nip-66/): Relay Discovery and Liveness Monitoring

[NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) standardizes publishing relay monitoring data to Nostr. Monitor services continuously test relays for availability, latency, protocol compliance, and supported NIPs. They publish results as kind 30166 events, providing real-time relay status independent of relay self-reporting.

Monitors check relay availability by connecting and sending test subscriptions. Latency measurements track connection time, subscription response time, and event propagation delay. Protocol compliance testing verifies relay behavior matches specifications, catching implementation bugs or intentional deviations. NIP support verification goes beyond [NIP-11](/en/topics/nip-11/) claims by actually testing whether advertised features work correctly.

```json
{
  "id": "a34b5c7d89e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7",
  "pubkey": "4e2d0bc6f8e7c3a5b9f1d2e3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4",
  "created_at": 1736784000,
  "kind": 30166,
  "tags": [
    ["d", "wss://relay.example.com"],
    ["rtt", "open", "143", "1736784000"],
    ["rtt", "read", "89", "1736784000"],
    ["rtt", "write", "92", "1736784000"],
    ["nips", "1", "2", "4", "9", "11", "12"],
    ["geo", "US", "United States", "New York"],
    ["other", "network", "clearnet"],
    ["other", "payment_required", "false"],
    ["other", "auth_required", "false"]
  ],
  "content": "{\"last_check\": 1736784000, \"checks\": 8760}",
  "sig": "8b9c4d5e6a7f8b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b"
}
```

The `d` tag contains the relay URL, making this a parameterized replaceable event. Each monitor publishes one event per relay, updated as measurements change. Multiple monitors can track the same relay, providing redundancy and cross-validation. Clients query multiple monitor pubkeys to get diverse perspectives on relay health.

Round-trip time (rtt) tags measure latency for different operations. `rtt open` tracks WebSocket connection establishment, `rtt read` measures subscription response time, and `rtt write` tests event publication speed. All values are in milliseconds. Clients use these metrics to prefer low-latency relays for time-sensitive operations or deprioritize slow relays.

The `nips` tag lists actually verified NIP support, not just claimed support. Monitors test each NIP by exercising its functionality. If a relay claims [NIP-50](/en/topics/nip-50/) search in its [NIP-11](/en/topics/nip-11/) document but search queries fail, monitors will omit NIP-50 from the verified list. This provides ground truth about relay capabilities.

Geographic information helps clients select nearby relays for better latency and censorship resistance. The `geo` tag contains country code, country name, and region. The `network` tag distinguishes clearnet relays from Tor hidden services or I2P endpoints. Together, these tags enable geographic diversity: clients can connect to relays in multiple jurisdictions to resist regional censorship.

Monitor data powers relay selectors in clients, explorer websites, and the Trusted Relay Assertions proposal. By combining self-reported [NIP-11](/en/topics/nip-11/) documents with measured [NIP-66](/en/topics/nip-66/) data and computed trust assertions, the ecosystem moves toward informed relay selection rather than relying on hardcoded defaults or word-of-mouth recommendations.

## Releases

### 0xchat v1.5.3 - Enhanced Messaging Features

[0xchat v1.5.3](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.3-release) brings significant improvements to the Telegram-style Nostr messaging client. The release addresses [NIP-55](/en/topics/nip-55/) (Android signer application) compliance issues that were preventing proper event signing through external signers like Amber. Full compliance means 0xchat now correctly delegates signing operations, improving security by keeping private keys isolated.

The update integrates both FileDropServer and BlossomServer as default media storage options, giving users redundancy for file uploads. [Blossom](https://github.com/hzrd149/blossom) provides content-addressed storage where files are referenced by their SHA-256 hashes, ensuring integrity and enabling deduplication across the network. Automatic draft saving for Moments prevents data loss when composing long-form content, addressing user complaints about lost posts during app switches or connectivity interruptions.

[Cashu](/en/topics/cashu/) wallet integration receives polish with automatic proof filtering that removes spent tokens from the wallet view. This solves the confusing UX where users saw invalid proofs alongside valid ecash, making balance calculations unreliable. The filtering happens client-side, maintaining privacy while improving the payment experience for peer-to-peer transactions within chats.

### Amber v4.1.0 Pre-releases - UI Overhaul

[Amber v4.1.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre1) through [v4.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre3) introduce a redesigned interface for the popular Android event signer. The login screen now clearly displays which application is requesting signature permissions, addressing user confusion about authorization flows. The new events screen provides detailed inspection of what data applications want to sign, allowing users to make informed security decisions before approving operations.

Permission management receives significant attention with a revamped interface showing exactly what capabilities each connected application has been granted. Users can revoke specific permissions without disconnecting entirely, enabling fine-grained control over signing delegation. The refactored relay counters using the updated quartz library provide real-time statistics on event throughput and relay performance. [NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) (Nostr Connect) bunker connections now surface detailed error messages when connections fail, replacing cryptic timeout errors with actionable diagnostics.

## Notable code and documentation changes

*These are merged pull requests and early-stage developments worth tracking. Some are experimental features that may evolve before release.*

### Zeus (Lightning Wallet with Nostr Wallet Connect)

Zeus merged 17 pull requests this week, strengthening its position as a leading [NIP-47](/en/topics/nip-47/) Nostr Wallet Connect implementation. The most significant fixes address data consistency and protocol compliance issues that were causing interoperability problems with Nostr clients.

**Transaction History Fix** - [PR #3542](https://github.com/ZeusLN/zeus/pull/3542) resolves a critical bug where NWC transaction lists displayed incorrect or duplicate entries. The issue occurred when Zeus cached transaction data without properly handling event updates, causing users to see phantom transactions or missing payments. The fix implements proper event deduplication and cache invalidation, ensuring transaction history accurately reflects Lightning node state.

**Protocol Compliance** - [PR #3548](https://github.com/ZeusLN/zeus/pull/3548) addresses incomplete `getInfo` responses that broke compatibility with clients expecting full NIP-47 compliance. Some Nostr clients crashed when receiving partial responses missing fields like `block_height` or `network`. The PR ensures all required fields return with sensible defaults even when the underlying Lightning implementation doesn't provide them, improving Zeus's compatibility across the ecosystem.

**Connection Resilience** - [PR #3543](https://github.com/ZeusLN/zeus/pull/3543) implements timeout notifications for stalled Nostr connections. Previously, users waited indefinitely when relay connections dropped silently. Now Zeus displays clear timeout messages after 30 seconds of inactivity, letting users retry or switch relays. [PR #3541](https://github.com/ZeusLN/zeus/pull/3541) adds backend validation to prevent NWC activation on incompatible Lightning implementations, catching configuration errors before they cause runtime crashes.

**[Cashu](/en/topics/cashu/) Race Condition** - [PR #3531](https://github.com/ZeusLN/zeus/pull/3531) fixes a concurrency bug in [Cashu](/en/topics/cashu/) token management where simultaneous mint operations could corrupt the token database. The race condition occurred when multiple threads updated token counts without proper locking, occasionally resulting in incorrect balances. The fix adds mutex protection around critical sections, ensuring atomic updates to token state.

### Primal Android (Client)

Primal Android shipped 12 merged PRs with significant improvements to wallet security and media handling. The wallet backup implementation addresses one of the most requested features, while NIP-92 support improves the visual experience across the application.

**Wallet Backup System** - A four-PR series ([#844](https://github.com/PrimalHQ/primal-android-app/pull/844), [#845](https://github.com/PrimalHQ/primal-android-app/pull/845), [#846](https://github.com/PrimalHQ/primal-android-app/pull/846), [#848](https://github.com/PrimalHQ/primal-android-app/pull/848)) implements comprehensive seed phrase backup functionality. Users can now export their 12-word mnemonic through a secure flow that prevents screenshots, displays backup status in the wallet dashboard, and guides existing users through migration. The implementation follows BIP-39 standards and includes validation to prevent users from losing funds due to incorrect phrase recording.

**Media Dimensions (NIP-92)** - [PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) implements [NIP-92](/en/topics/nip-92/) support for proper image and video aspect ratios. Without dimension metadata, clients must download images to determine their size, causing layout jumps as content loads. NIP-92 adds `dim` tags (like `["dim", "1920x1080"]`) to file metadata events, allowing Primal to reserve correct space before downloading media. This eliminates jarring reflows in image galleries and improves perceived performance.

**Remote Signer Reliability** - [PR #841](https://github.com/PrimalHQ/primal-android-app/pull/841) fixes [NIP-46](/en/topics/nip-46/) connection issues where missing `wss://` prefixes caused silent failures. The PR validates relay URIs during bunker connection setup, adding the protocol prefix automatically when users paste bare domains. [PR #843](https://github.com/PrimalHQ/primal-android-app/pull/843) addresses a threading bug where poor network conditions caused replies to post as root notes, breaking conversation flow. The fix ensures parent event IDs persist through network interruptions.

### Marmot Protocol: White Noise (Encrypted Group Chat Library)

White Noise, the Rust library powering [Marmot](/en/topics/marmot/) Protocol's encrypted group chats, merged six PRs improving user experience and security. The changes bring Marmot closer to feature parity with mainstream messaging applications while maintaining its privacy-first architecture.

**Read Receipts** - [PR #433](https://github.com/marmot-protocol/whitenoise-rs/pull/433) and [#436](https://github.com/marmot-protocol/whitenoise-rs/pull/436) implement message read tracking for group conversations. The system stores read positions per user per group within a single device, enabling unread count badges. The implementation uses monotonic timestamps to track the last read message position for each conversation. This foundational feature enables UI indicators showing unread message counts per conversation.

**Conversation Pinning** - [PR #442](https://github.com/marmot-protocol/whitenoise-rs/pull/442) adds persistent conversation pinning through a `pin_order` field in the `accounts_groups` junction table that links accounts to groups. Pinned conversations maintain their position at the top of chat lists regardless of message activity, matching user expectations from Signal and WhatsApp. The implementation uses integer ordering to allow unlimited pins with deterministic sorting.

**Deterministic Commit Resolution (MIP-03)** - [PR #152](https://github.com/marmot-protocol/mdk/pull/152) (open) implements Marmot Improvement Proposal 03, solving the critical problem of commit race conditions in distributed group chats. When multiple members submit group state changes (adding/removing members, changing permissions) simultaneously, clients could diverge on commit ordering, fragmenting the group into incompatible states. MIP-03 introduces epoch snapshots and a deterministic winner selection: the commit with the earliest `created_at` timestamp wins, with lexicographic event ID as tiebreaker. This allows all clients to converge on the same state through rollback and replay, maintaining group coherence even during network partitions.

**Security Hardening** - [PR #443](https://github.com/marmot-protocol/whitenoise-rs/pull/443) prevents unnecessary copying of cryptographic secrets by using references in `resolve_group_image_path`. This reduces the window for memory attacks where secrets could be recovered from freed heap allocations. [PR #438](https://github.com/marmot-protocol/whitenoise-rs/pull/438) enables SQLCipher database encryption through keyring parameters, protecting message history at rest. The keyring integration allows secure key storage in platform keychains rather than configuration files.

### nostrdb-rs (Database Library) - Open PR

**Streaming Queries Implementation** - [PR #58](https://github.com/damus-io/nostrdb-rs/pull/58) (open) proposes streaming fold queries to enable zero-allocation database operations. The implementation adds `fold`, `try_fold`, `count`, `any`, `all`, and `find_map` methods that would process database results one at a time without materializing entire result sets into vectors. This approach would reduce memory consumption and enable early termination for common query patterns.

The technical implementation exposes low-level query result callbacks (`ndb_query_visit`) as stateful Rust visitors that map `ControlFlow` variants to C visitor actions. Once merged, application code will read like iterator logic while running close to the database layer. For example, counting matching notes would stream through results rather than collecting them, and `find_map` would return the first useful result without processing remaining rows.

nostrdb powers Damus and Notedeck, both iOS/macOS and desktop clients respectively. The streaming queries would enable efficient patterns like pagination, conditional filtering, and existence checks. The PR changes 3 files with +756 additions and -32 deletions, a substantial refactoring of the query layer. Users of nostrdb-rs-based applications would see reduced memory usage when browsing large timelines or searching through extensive event databases.

### nak (CLI Tool)

nak, fiatjaf's command-line Nostr tool, merged six PRs focused on build system improvements and new functionality. [PR #91](https://github.com/fiatjaf/nak/pull/91) implements a Blossom mirror feature, letting nak serve as a mirror for Blossom media servers. [Blossom](/en/topics/blossom/) is a content-addressed media storage protocol that works alongside Nostr events.

The remaining PRs address build system compatibility across Windows, macOS, and Linux platforms, enabling FUSE filesystem support for mounting Nostr events as local directories.

### Damus (iOS Client) - Open PRs

Damus has 11 open PRs exploring significant architectural improvements. While these haven't merged yet, they signal important directions for iOS Nostr client development, particularly around privacy, synchronization efficiency, and mobile data optimization.

**Tor Integration** - [PR #3535](https://github.com/damus-io/damus/pull/3535) embeds the Arti Tor client directly into Damus, enabling anonymous relay connections without external dependencies. Unlike Orbot or Tor Browser approaches, embedding Arti provides seamless integration with iOS sandboxing and background execution limits. The Rust implementation brings memory safety to network anonymization, reducing attack surface compared to C Tor. Users could toggle Tor mode per-relay or globally, with the client handling circuit management transparently.

**Negentropy Sync Protocol** - [PR #3536](https://github.com/damus-io/damus/pull/3536) implements Negentropy, a set reconciliation protocol that radically improves synchronization efficiency. Instead of downloading all events since last connection, Negentropy exchanges compact fingerprints (Merkle trees) to identify exactly which events differ between client and relay. For users following hundreds of pubkeys, this reduces sync bandwidth from megabytes to kilobytes. The implementation integrates with RelayPool and SubscriptionManager, enabling automatic efficient sync across all connected relays.

**Low Data Mode** - [PR #3549](https://github.com/damus-io/damus/pull/3549) adds cellular data conservation features responding to user feedback about bandwidth consumption. The mode disables image auto-loading, video prefetching, and reduces subscription limits. Users on metered connections can browse text content without fear of exceeding data caps. The implementation respects iOS low data mode settings and provides granular controls for different media types.

**Database Optimizations** - [PR #3548](https://github.com/damus-io/damus/pull/3548) reworks nostrdb snapshot storage for faster queries and reduced disk usage. The optimization changes how database snapshots persist to disk, improving both read performance and write amplification. This addresses battery drain complaints from users with large event databases.

---

That's it for this week. Building something? Have news to share? Want us to cover your project? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via NIP-17 DM</a> or find us on Nostr.
