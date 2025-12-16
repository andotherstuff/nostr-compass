---
title: 'Nostr Compass #1'
date: 2025-12-17
publishDate: 2025-12-15
draft: false
type: newsletters
---

Welcome to Nostr Compass, a weekly newsletter dedicated to the Nostr protocol ecosystem. Our mission is to keep developers, relay operators, and builders informed about important developments across the network. We document protocol evolution with technical accuracy, neutrality, and depth, covering everything from NIP proposals to client releases to implementation best practices.

Nostr Compass is inspired by [Bitcoin Optech](https://bitcoinops.org/), whose years of dedicated work advancing Bitcoin technical knowledge set the standard for protocol-focused newsletters. We're grateful for their example and hope to bring the same rigor to the Nostr ecosystem.

This inaugural issue establishes our weekly format. Each Wednesday we'll bring you NIP updates, release notes, development highlights, and technical guidance. Whether you're building a client, running a relay, or contributing to the protocol, Nostr Compass aims to be your reliable source for what's happening across the ecosystem.

## What is Nostr?

*Since this is our first issue, we're starting with a primer on how Nostr works. Regular readers can [skip ahead](#news--updates).*

Nostr (Notes and Other Stuff Transmitted by Relays) is a decentralized protocol for social networking and messaging. Unlike traditional platforms, Nostr has no central server, no company controlling it, and no single point of failure. Users own their identity through cryptographic keypairs, and content flows through independent relay servers that anyone can run.

**How it works:** Users generate a keypair (a private key called nsec and public key called npub). The private key signs messages called "events," and the public key serves as your identity. Events are sent to relays, which store and forward them to other users. Because you control your keys, you can switch between clients or relays without losing your identity or followers.

**Why it matters:** Nostr provides censorship resistance through relay diversity (if one relay bans you, others can still serve your content), portability (your identity works across any Nostr app), and interoperability (all Nostr clients speak the same protocol). There's no algorithm deciding what you see, no ads, and no data harvesting.

**The ecosystem today:** Nostr supports microblogging (like Twitter/X), long-form content (like Medium), direct messages, marketplaces, livestreaming, and more. Clients include Damus (iOS), Amethyst (Android), Primal, Coracle, and dozens of others. Lightning Network integration enables instant payments through "zaps." The protocol continues to evolve through NIPs (Nostr Implementation Possibilities), community-driven specifications that extend functionality.

## News & Updates

**NIP-BE Merged: Bluetooth Low Energy Support** - A significant new capability landed in the protocol. [NIP-BE](https://github.com/nostr-protocol/nips/blob/master/BE.md) specifies how Nostr applications can communicate and synchronize over Bluetooth Low Energy. This enables offline-capable apps to sync data across nearby devices without internet connectivity. The spec adapts WebSocket relay patterns to BLE's constraints, using DEFLATE compression and chunked messaging to handle BLE's small MTU sizes (20-256 bytes). Devices negotiate roles based on UUID comparison, with the higher UUID becoming the GATT server.

**MIP-05: Privacy-Preserving Push Notifications** - The Marmot Protocol published [MIP-05](https://github.com/marmot-protocol/marmot/pull/18), a specification for push notifications that maintain privacy. Traditional push systems require servers to know device tokens and user identities; MIP-05 solves this by encrypting device tokens with ECDH+HKDF and ChaCha20-Poly1305, using ephemeral keys to prevent correlation. A three-event gossip protocol (kinds 447-449) synchronizes encrypted tokens across group members, and notifications use NIP-59 gift wrapping with decoy tokens to hide group sizes. This enables WhiteNoise and other Marmot clients to deliver timely notifications without compromising user privacy.

**Blossom BUD-10: New URI Scheme** - The Blossom media protocol is getting a custom URI scheme via [PR #84](https://github.com/hzrd149/blossom/pull/84). The new `blossom:<sha256>.ext` format embeds file hash, extension, size, multiple server hints, and author pubkeys for BUD-03 server discovery. This makes blob links more resilient than static HTTP URLs by enabling automatic fallback across servers.

**Shopstr Marketplace Updates** - The Nostr-native marketplace [implemented Nostr Wallet Connect](https://github.com/shopstr-eng/shopstr/pull/202) (NIP-47) for payments, [added listing expiration](https://github.com/shopstr-eng/shopstr/pull/203) using NIP-40, and introduced [discount codes](https://github.com/shopstr-eng/shopstr/pull/210) for sellers.

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**New NIPs:**
- **NIP-BE** - Bluetooth Low Energy messaging and device synchronization ([#1979](https://github.com/nostr-protocol/nips/pull/1979))

**Significant Changes:**
- **NIP-69** - Added order expiration support for P2P trading with `expires_at` and `expiration` tags ([#2118](https://github.com/nostr-protocol/nips/pull/2118))
- **NIP-59** - Gift wrap events can now be deleted via NIP-09/NIP-62 requests ([#2131](https://github.com/nostr-protocol/nips/pull/2131))
- **NIP-51** - Removed hashtag and URL tags from generic bookmarks; hashtags now use kind 30015 ([#2133](https://github.com/nostr-protocol/nips/pull/2133))
- **NIP-18** - Improved generic reposts for replaceable events with `a` tag support ([#2132](https://github.com/nostr-protocol/nips/pull/2132))
- **NIP-17** - Refined wording and added kind 7 reaction support to DMs ([#2098](https://github.com/nostr-protocol/nips/pull/2098))
- **NIP-11** - Added `self` field for relay public key identification ([#1764](https://github.com/nostr-protocol/nips/pull/1764))

## NIP Deep Dive: NIP-01 and NIP-19

For this inaugural issue, we cover two foundational NIPs that every Nostr developer should understand.

### NIP-01: Basic Protocol

[NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) defines the core protocol. Everything in Nostr builds on this specification.

**Events** are the only object type. Each event contains:
- `id`: SHA256 hash of the serialized event (the event's unique identifier)
- `pubkey`: The creator's public key (32-byte hex, secp256k1)
- `created_at`: Unix timestamp
- `kind`: Integer categorizing the event type
- `tags`: Array of arrays for metadata
- `content`: The payload (interpretation depends on kind)
- `sig`: Schnorr signature proving the pubkey created this event

**Kinds** determine how relays store events:
- Regular events (1, 2, 4-44, 1000-9999): Stored normally, all versions kept
- Replaceable events (0, 3, 10000-19999): Only the latest per pubkey is kept
- Ephemeral events (20000-29999): Not stored, just forwarded to subscribers
- Addressable events (30000-39999): Latest per pubkey + kind + `d` tag combination

Kind 0 is user metadata (profile), kind 1 is a text note (the basic post), kind 3 is the follow list.

**Kind 1: Text Notes** are the heart of social Nostr. A kind 1 event is a short-form post, similar to a tweet. The `content` field contains the message text (plaintext, though clients often render markdown). Tags enable replies, mentions, and references:

```json
{
  "kind": 1,
  "content": "Hello Nostr! Check out @jb55's work on Damus.",
  "tags": [
    ["e", "<replied-to-event-id>", "wss://relay.example.com", "reply"],
    ["p", "<jb55-pubkey>"]
  ]
}
```

The `e` tag with "reply" marker indicates this is a reply (see NIP-10 for threading conventions). The `p` tag mentions a user, enabling clients to notify them and render their name instead of the raw pubkey. Clients fetch the mentioned user's kind 0 event to get their display name and picture.

To build a timeline, a client subscribes to kind 1 events from followed pubkeys: `["REQ", "feed", {"kinds": [1], "authors": ["<pubkey1>", "<pubkey2>", ...], "limit": 50}]`. The relay returns matching notes, and the client renders them chronologically.

**Addressable events** (30000-39999) work like replaceable events but use a `d` tag as an additional identifier. The relay keeps only the latest version of each pubkey + kind + d-tag combination. This enables editable articles, product listings, or any case where you need multiple replaceable items per user.

**Tags** are arrays where the first element is the tag name. Standard single-letter tags (`e`, `p`, `a`, `d`, `t`) are indexed by relays for efficient querying. For example, `["e", "<event-id>"]` references another event, `["p", "<pubkey>"]` references a user.

**Client-Relay Communication** uses WebSocket connections with JSON arrays as messages. The first element identifies the message type.

From client to relay:
- `["EVENT", <event>]` - Publish an event to the relay
- `["REQ", <sub-id>, <filter>, ...]` - Subscribe to events matching the filter(s)
- `["CLOSE", <sub-id>]` - End a subscription

From relay to client:
- `["EVENT", <sub-id>, <event>]` - Delivers an event matching your subscription
- `["EOSE", <sub-id>]` - "End of stored events" - the relay has sent all historical matches and will now only send new events as they arrive
- `["OK", <event-id>, <true|false>, <message>]` - Acknowledges whether an event was accepted or rejected (and why)
- `["NOTICE", <message>]` - Human-readable message from the relay

The subscription flow: client sends `REQ` with a subscription ID and filter, relay responds with matching `EVENT` messages, then sends `EOSE` to signal it's caught up on history. After `EOSE`, any new `EVENT` messages are real-time. Client sends `CLOSE` when done.

**Filters** specify which events to retrieve. A filter object can include: `ids` (event IDs), `authors` (pubkeys), `kinds` (event types), `#e`/`#p`/`#t` (tag values), `since`/`until` (timestamps), and `limit` (max results). All conditions within one filter use AND logic. You can include multiple filters in a `REQ`, and they combine with OR logic - useful for fetching different event types in one subscription.

### NIP-19: Bech32-Encoded Identifiers

[NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md) defines the human-friendly formats you see everywhere in Nostr: npub, nsec, note, and more. These aren't used in the protocol itself (which uses hex), but they're essential for sharing and display.

**Why bech32?** Raw hex keys are error-prone to copy and hard to distinguish visually. Bech32 encoding adds a human-readable prefix and checksum. You can immediately tell an `npub` (public key) from an `nsec` (private key) or `note` (event ID).

**Basic formats** encode raw 32-byte values:
- `npub` - Public key (your identity, safe to share)
- `nsec` - Private key (keep secret, used for signing)
- `note` - Event ID (references a specific event)

Example: The hex pubkey `3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d` becomes `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

**Shareable identifiers** include metadata using TLV (Type-Length-Value) encoding:
- `nprofile` - Profile with relay hints (helps clients find the user)
- `nevent` - Event with relay hints, author pubkey, and kind
- `naddr` - Addressable event reference (pubkey + kind + d-tag + relays)

These solve a key problem: if someone shares a note ID, how do you know which relay has it? An `nevent` bundles the event ID with suggested relays, making sharing more reliable.

**Important:** Never use bech32 formats in the protocol itself. Events, relay messages, and NIP-05 responses must use hex. Bech32 is purely for human interfaces: display, copy/paste, QR codes, and URLs.

## Releases

**Amber v4.0.3** - The Android signer app received a significant update with revamped encryption/decryption UI that better distinguishes between plain text, events, and tag arrays. Also added account export/import, per-account relay handling, bunker ping support, and crash reporting. [Release](https://github.com/greenart7c3/amber/releases/tag/v4.0.3)

**Coracle 0.6.28** - Bug fix release for the web client. Fixed topic feeds, image handling when imgproxy is disabled, and linkification of non-link highlight sources. [Release](https://github.com/coracle-social/coracle/releases/tag/0.6.28)

**Flotilla v1.3.0** - The Discord-like communities client added optional badges and sounds for notifications, improved link rendering, QR code scanning for invite links, and streamlined wallet setup. Also restored Blossom feature detection for spaces, enhanced light theme, and fixed duplicate DMs. [Release](https://github.com/coracle-social/flotilla/releases/tag/1.3.0)

**nak v0.17.2** - The command-line Nostr tool added a new `nip` command for quick NIP reference lookup, plus fixes for git repository handling and stdin event processing. [Release](https://github.com/fiatjaf/nak/releases/tag/v0.17.2)

**WhiteNoise v0.2.1** - Major release for the MLS-based encrypted messaging app adding image sharing via Blossom, background sync, push notifications, 8-language localization, and group member management. [Release](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Amethyst v1.04.2** - Feature release introducing follow lists/packs, new timeline filters, image gallery, and H.265 video compression (50% smaller files). Completed Kotlin Multiplatform migration. [Release](https://github.com/vitorpamplona/amethyst/releases/tag/v1.04.2)

**Mostro v0.15.5** - P2P trading bot update with NIP-69 order expiration support and improved trade history responses. [Release](https://github.com/MostroP2P/mostro/releases/tag/v0.15.5)

## Client Development

### Damus (iOS)

Stability focus with crash and UI fixes: [cursor jumping fix](https://github.com/damus-io/damus/pull/3377) for the compose view, [NostrDB interface redesign](https://github.com/damus-io/damus/pull/3366) using Swift's `~Copyable` types for transaction safety, [thread UI stability](https://github.com/damus-io/damus/pull/3341) fixing action bar reinstantiation, [mute list freeze](https://github.com/damus-io/damus/pull/3346) from AttributeGraph cycles, and [profile crash](https://github.com/damus-io/damus/pull/3334) from cross-thread transaction cleanup. Also added [AGENTS.md](https://github.com/damus-io/damus/pull/3293) guidelines for AI coding agents.

### Notedeck (Desktop/Mobile)

[Secure key storage](https://github.com/damus-io/notedeck/pull/1191) moves nsec to OS secure store with automatic migration. [Future note filtering](https://github.com/damus-io/notedeck/pull/1201) hides events dated 24+ hours ahead (anti-spam). [nevent copying](https://github.com/damus-io/notedeck/pull/1183) now includes relay hints. Also: [profile column quick-add](https://github.com/damus-io/notedeck/pull/1212), [keyboard navigation](https://github.com/damus-io/notedeck/pull/1208), [media loading optimization](https://github.com/damus-io/notedeck/pull/1210).

### Amethyst (Android)

[NIP-46 remote signing](https://github.com/vitorpamplona/amethyst/pull/1555) support for Nostr Connect. [Bookmark organization](https://github.com/vitorpamplona/amethyst/pull/1586) with public/private list management. [strfry compatibility](https://github.com/vitorpamplona/amethyst/pull/1596) fix for relay info parsing edge cases.

### Primal (Android)

[Nostr Connect deep links](https://github.com/PrimalHQ/primal-android-app/pull/788) for `nostrconnect://` URLs. [Remote login](https://github.com/PrimalHQ/primal-android-app/pull/787) via QR scan for bunker connections. [Connection race condition fix](https://github.com/PrimalHQ/primal-android-app/pull/783).

### WhiteNoise (Encrypted Messaging)

[App data retention fix](https://github.com/marmot-protocol/whitenoise/pull/890) disables Android auto-backup for privacy. [Chat scroll behavior](https://github.com/marmot-protocol/whitenoise/pull/861) preserves position when reading history.

### Zeus (Lightning Wallet)

[NWC parallel payments](https://github.com/ZeusLN/zeus/pull/3407) for improved batch zap throughput.

## Developer Best Practices

**Validate Auth Events Defensively** - go-nostr fixed a [panic in NIP-42 validation](https://github.com/nbd-wtf/go-nostr/pull/182) when the relay tag was missing. Always check for required tags before accessing them, even in auth flows where you expect well-formed events.

**Rate Limit by Authentication State** - khatru added [NIP-42 based rate limiting](https://github.com/fiatjaf/khatru/pull/57), allowing relays to apply different limits for authenticated vs anonymous connections. Consider tiered limits based on auth status rather than blanket restrictions.

**Use Cursor Pagination for Lists** - Blossom [replaced date-based pagination](https://github.com/hzrd149/blossom/pull/65) with cursor-based pagination on the `/list` endpoint. Date-based pagination breaks when items share timestamps; cursors provide reliable iteration.

**Schema Validation for Event Types** - The [nostrability/schemata](https://github.com/nostrability/schemata) project provides JSON schemas for validating NIP-compliant events. Consider integrating schema validation in development to catch malformed events before they reach relays.

---

That's it for this week. Building something? Have news to share? Want us to cover your project? Reach out at [info@nostrcompass.org](mailto:info@nostrcompass.org) or find us on Nostr.

