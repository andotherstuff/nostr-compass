---
title: 'Nostr Compass #2'
date: 2025-12-24
publishDate: 2025-12-24
draft: false
type: newsletters
---

Welcome back to Nostr Compass, your weekly guide to the Nostr protocol ecosystem.

**This week:** Three [NIP-55](/en/topics/nip-55/) signer implementations see updates: Amber adds performance caching, Aegis gains `nostrsigner:` URI support, and Primal Android joins them as a full local signer. Shopstr introduces "Zapsnags" for flash sales via zaps. Mostro adds a development fund. Four NIP updates land including Public Messages (kind 24) and group privacy improvements. NDK cache queries speed up 162x, Applesauce adds reactions and NIP-60 wallet support, and Tenex introduces RAL architecture for AI agent delegation. In our deep dive, we explain [NIP-02](/en/topics/nip-02/) (follow lists) and [NIP-10](/en/topics/nip-10/) (reply threading), foundational specs for building social timelines and conversations.

## News

**Primal Android Becomes a NIP-55 Signer** - Building on last week's [Nostr Connect support](/en/newsletters/2025-12-17-newsletter/#primal-android), Primal has implemented full local signing capabilities through eight merged pull requests. The implementation includes a complete `LocalSignerContentProvider` that exposes signing operations to other Android apps via Android's content provider interface, following the [NIP-55](/en/topics/nip-55/) specification. The architecture separates concerns cleanly: `SignerActivity` handles user-facing approval flows, `LocalSignerService` manages background operations, and a new permissions system lets users control which apps can request signatures. This makes Primal a viable alternative to Amber for Android users who want to keep their keys in one app while using others for different Nostr experiences.

**Shopstr Zapsnags: Flash Sales via Lightning** - The Nostr-native marketplace introduced ["Zapsnags"](https://github.com/shopstr-eng/shopstr/pull/211), a flash sale feature that lets buyers purchase items directly from their social feed with a single zap. The implementation filters kind 1 notes tagged with `#shopstr-zapsnag` and renders them as product cards with a "Zap to Buy" button instead of the standard cart flow. When a buyer zaps, the system generates a payment request using [NIP-57](/en/topics/nip-57/), polls for the kind 9735 zap receipt to confirm payment, then encrypts shipping information using [NIP-17](/en/topics/nip-17/) gift wrapping before sending it privately to the seller. The feature stores buyer details locally for repeat purchases and includes a merchant dashboard for creating flash sale listings. It's a clever combination of social, payment, and privacy primitives that demonstrates how Nostr's composable design enables novel commerce patterns.

**Mostro Introduces Development Fund** - The [NIP-69](/en/topics/nip-69/) P2P Bitcoin trading bot [implemented configurable development fees](https://github.com/MostroP2P/mostro/pull/555) to support sustainable maintenance. Operators can set `dev_fee_percentage` between 10-100% of the Mostro trading fee (defaulting to 30%), which automatically routes to a development fund on each successful trade. The implementation adds three database columns (`dev_fee`, `dev_fee_paid`, `dev_fee_payment_hash`) to track contributions and validates the percentage at daemon startup. Technical documentation in [`docs/DEV_FEE.md`](https://github.com/MostroP2P/mostro/blob/main/docs/DEV_FEE.md) explains the system. This opt-in model lets operators support ongoing development while maintaining full transparency about fee allocation.

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**New NIPs:**
- **[NIP-A4](/en/topics/nip-a4/) (Public Messages, kind 24)** - A new kind for notification-screen messages designed for broad client support ([#1988](https://github.com/nostr-protocol/nips/pull/1988)). Unlike threaded conversations, these messages have no concept of chat history or message chains. They use `q` tags (quotations) rather than `e` tags to avoid threading complications, making them ideal for simple public notifications that appear in a recipient's notification feed without creating conversation state.

**Significant Changes:**
- **[NIP-29](/en/topics/nip-29/)** - Major clarification of group semantics ([#2106](https://github.com/nostr-protocol/nips/pull/2106)). The `closed` tag now means "unable to write" (read-only for non-members), decoupled from join mechanics. A new `hidden` tag prevents relays from serving metadata or member events to non-members, enabling truly private groups that are undiscoverable without out-of-band invitation. The `private` tag controls message visibility while still allowing public metadata for discovery.
- **[NIP-51](/en/topics/nip-51/)** - Added kind 30006 for curated picture sets ([#2170](https://github.com/nostr-protocol/nips/pull/2170)), following the pattern of 30004 (articles) and 30005 (videos). Already implemented in Nostria.
- **[NIP-55](/en/topics/nip-55/)** - Clarified connection initiation for Android signers ([#2166](https://github.com/nostr-protocol/nips/pull/2166)). Developers implementing multi-user sessions were misusing `get_public_key` by calling it from background processes. The updated spec recommends calling it only once during initial connection, preventing a common implementation footgun.

## NIP Deep Dive: NIP-02 and NIP-10

This week we cover two NIPs essential for social functionality: how clients know who you follow and how conversations are threaded.

### [NIP-02](/en/topics/nip-02/): Follow List

[NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md) defines kind 3 events, which store your follow list. This simple mechanism powers the social graph that makes timelines possible.

**Structure:** A kind 3 event contains `p` tags listing followed pubkeys:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Each `p` tag has four positions: the tag name, the followed pubkey (hex), an optional relay URL hint, and an optional "petname" (a local nickname). The relay hint tells other clients where to find that user's events. The petname lets you assign memorable names to contacts without relying on their self-declared display names.

**Replaceable behavior:** Kind 3 falls in the replaceable range (0, 3, 10000-19999), so relays keep only the latest version per pubkey. When you follow someone new, your client publishes a complete new kind 3 containing all your follows plus the new one. This means follow lists must be complete each time; you can't publish incremental updates.

**Building timelines:** To construct a home feed, clients fetch the user's kind 3, extract all `p` tag pubkeys, then subscribe to kind 1 events from those authors:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

The relay returns matching notes, and the client renders them. The relay hints in kind 3 help clients know which relays to query for each followed user.

**Petnames and identity:** The petname field enables a decentralized naming scheme. Rather than trusting whatever name a user claims in their profile, you can assign your own label. A client might display "alice (My Sister)" where "alice" comes from her kind 0 profile and "My Sister" is your petname. This provides context that global usernames cannot.

**Practical considerations:** Because kind 3 events are replaceable and must be complete, clients should preserve unknown tags when updating. If another client added tags your client doesn't understand, blindly overwriting would lose that data. Append new follows rather than rebuilding from scratch.

### [NIP-10](/en/topics/nip-10/): Text Note Threading

[NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md) specifies how kind 1 notes reference each other to form reply threads. Understanding this is essential for building conversation views.

**The problem:** When someone replies to a note, clients need to know: What is this a reply to? What's the root of the conversation? Who should be notified? NIP-10 answers these questions through `e` tags (event references) and `p` tags (pubkey mentions).

**Marked tags (preferred):** Modern clients use explicit markers in `e` tags:

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "Great point! I agree.",
  "sig": "b7d3f..."
}
```

The `root` marker points to the original note that started the thread. The `reply` marker points to the specific note being answered. If replying directly to the root, use only `root` (no `reply` tag needed). The distinction matters for rendering: the `reply` determines indentation in a thread view, while `root` groups all replies together.

**Threading rules:**
- Direct reply to root: One `e` tag with `root` marker
- Reply to a reply: Two `e` tags, one `root` and one `reply`
- The `root` stays constant throughout the thread; `reply` changes based on what you're responding to

**Pubkey tags for notifications:** Include `p` tags for everyone who should be notified. At minimum, tag the author of the note you're replying to. Convention is to also include all `p` tags from the parent event (so everyone in the conversation stays in the loop), plus any users you @mention in your content.

**Relay hints:** The third position in `e` and `p` tags can contain a relay URL where that event or user's content might be found. This helps clients fetch the referenced content even if they're not connected to the original relay.

**Deprecated positional tags:** Early Nostr implementations inferred meaning from tag position rather than markers: first `e` tag was root, last was reply, middle ones were mentions. This approach is deprecated because it creates ambiguity. If you see `e` tags without markers, they're likely from older clients. Modern implementations should always use explicit markers.

**Building thread views:** To display a thread, fetch the root event, then query for all events with an `e` tag referencing that root:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Sort results by `created_at` and use `reply` markers to build the tree structure. Events whose `reply` points to the root are top-level replies; events whose `reply` points to another reply are nested responses.

## Releases

**Zeus v0.12.0** - Building on last week's [NWC parallel payments support](/en/newsletters/2025-12-17-newsletter/#zeus), the Lightning wallet's [major release](https://github.com/ZeusLN/zeus/releases/tag/v0.12.0) ships a complete [NIP-47](/en/topics/nip-47/) Nostr Wallet Connect service with custom relay support and budget tracking. A [budget reload fix](https://github.com/ZeusLN/zeus/pull/3455) ensures connections use current limits. [Lightning address copying](https://github.com/ZeusLN/zeus/pull/3460) no longer includes the `lightning:` prefix, fixing paste issues in Nostr profile fields.

**Amber v4.0.6** - The Android [NIP-55](/en/topics/nip-55/) signer [adds performance caching](https://github.com/greenart7c3/Amber/releases/tag/v4.0.6) to signing operations and improves error handling when decrypting malformed content. Connection reliability improved with retry logic for relay connect events, and several crash fixes address edge cases around invalid `nostrconnect://` URIs and permission screen interactions.

**nak v0.17.3** - The command-line Nostr tool's [latest release](https://github.com/fiatjaf/nak/releases/tag/v0.17.3) restricts LMDB builds to Linux, fixing cross-platform compilation issues.

**Aegis v0.3.4** - The cross-platform Nostr signer [adds support](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.4) for the `nostrsigner:` URI scheme defined in [NIP-55](/en/topics/nip-55/), matching Amber's connection flow. Local relay data can now be imported and exported for backup, and the release includes bug fixes for relay socket errors and UI improvements to the local relay interface.

## Notable code and documentation changes

*These are open pull requests and early-stage work, perfect for getting feedback before they merge. If something catches your eye, consider reviewing or commenting!*

### Damus (iOS)

[Mute list persistence](https://github.com/damus-io/damus/pull/3469) fixes an issue where mute lists were wiped on cold start. The fix adds guards to prevent accidental overwrites during app initialization. [Profile stream timing](https://github.com/damus-io/damus/pull/3457) eliminates a ~1 second delay before cached profiles appeared. Previously, views waited for subscription tasks to restart; now `streamProfile()` immediately yields cached data from NostrDB, removing the window where abbreviated pubkeys and placeholder images showed.

### White Noise (Encrypted Messaging)

[Real-time message streaming](https://github.com/marmot-protocol/whitenoise/pull/919) replaces the previous polling mechanism with a stream-based architecture. The new `ChatStreamNotifier` consumes the Rust SDK's message stream directly, maintaining chronological order and handling incremental updates efficiently. Testing showed significant improvement in responsiveness. A [chat list API](https://github.com/marmot-protocol/whitenoise/pull/921) adds `get_chat_list` for retrieving conversation summaries, and a [stable sort fix](https://github.com/marmot-protocol/whitenoise/pull/905) prevents message reordering loops by using `createdAt` with message ID as tiebreaker.

### NDK (Library)

Two pull requests delivered dramatic cache performance improvements. [PR #371](https://github.com/nostr-dev-kit/ndk/pull/371) fixed a bug where events read from SQLite cache were immediately written back, causing 100% duplicate writes on app boot. The fix adds a `fromCache` guard and implements O(1) duplicate checking via an in-memory Set. For small result sets (<100 events), direct JSON transfer replaces binary encoding overhead. [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372) removed unnecessary `seenEvent` calls for cached events. The LRU cache lookup cost 0.24-0.64ms per event; for 5,700 cached events, this added ~1.4 seconds of overhead. Result: cache queries dropped from ~3,690ms to ~22ms (162x faster).

### rust-nostr (Library)

[Multi-filter REQ support](https://github.com/rust-nostr/nostr/pull/1176) was restored after being removed in a previous refactor. The SDK again accepts `Vec<Filter>` for subscription requests, enabling efficient queries that combine multiple filter conditions with OR logic. [Relay provenance](https://github.com/rust-nostr/nostr/pull/1156) was added to `stream_events*` methods, so each streamed event now includes the `RelayUrl` it came from and a `Result` indicating success or failure, useful for tracking relay reliability and debugging connection issues. A [security fix](https://github.com/rust-nostr/nostr/pull/1179) removed the `url-fork` dependency following RUSTSEC-2024-0421, eliminating a known vulnerability.

### Applesauce (Library)

The TypeScript library powering [noStrudel](https://github.com/hzrd149/nostrudel) saw significant development this week. New models include a [reactions system](https://github.com/hzrd149/applesauce) and user groups casting. Wallet functionality expanded with NIP-60 support, a send tab, and improved token recovery tools. A new `user.directMessageRelays$` property exposes DM relay configuration. All actions were refactored to use async interfaces (removing async generators), and bug fixes addressed encrypted content restoration and time-based event filter edge cases.

### Tenex (AI Agents)

The [multi-agent coordination system](https://github.com/tenex-chat/tenex) built on Nostr introduced RAL (Request-Action-Lifecycle) architecture in [five merged PRs](https://github.com/pablof7z/tenex/pull/38). RAL enables agents to pause when delegating tasks and resume when results arrive, with conversation-scoped state persistence. Delegation tools (`delegate`, `ask`, `delegate_followup`, `delegate_external`) now publish Nostr events and return stop signals instead of blocking. The refactor includes AI SDK v6 migration, VCR testing infrastructure for deterministic LLM interaction recording, and multimodal image support.

---

That's it for this week. Building something? Have news to share? Want us to cover your project? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via NIP-17 DM</a> or find us on Nostr.
