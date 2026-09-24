## In Development

### 0xchat merges fixes for signing, message-authentication, and redirect flaws

[0xchat's merged security PR](https://github.com/0xchat-app/0xchat-app-main/pull/92) addresses four audit findings in its Nostr and Cashu application code. It limits Cashu P2PK witness signing to keys actually authorized by a lock, rejects unsealed gift-wrap contents except MLS Welcome events, accepts infrastructure host-map configuration only from the trusted server key, and requires consent before an embedded web page can call NIP-07 signing or read relay settings.

The [PR's test record](https://github.com/0xchat-app/0xchat-app-main/pull/92) reports static analysis and runtime checks for the gift-wrap path. This is source-level progress, not a claim that an updated app has been released or independently tested on a device.

### nos2x-fox closes a PIN exposure path

[nos2x-fox](https://github.com/diegogurpegui/nos2x-fox) is a Firefox extension that offers Nostr signing to websites. A [merged access-control fix](https://github.com/diegogurpegui/nos2x-fox/pull/69) stops a website from asking the extension background for the cached PIN that derives its private-key encryption key. The page bridge now forwards only allowed request types, and the background rejects privileged requests unless they originate from an extension page.

A separate [merged injection change](https://github.com/diegogurpegui/nos2x-fox/pull/67) makes the NIP-07 `window.nostr` interface appear at document start and removes a web-accessible script URL that exposed a stable extension identifier. It raises the Firefox minimum to version 128. Both fixes are merged source work; a new extension-store release has not been verified.

### nostream publishes relay health events

[nostream](https://github.com/cameri/nostream) is a Nostr relay implementation that also runs a relay monitor. Its [merged NIP-66 work](https://github.com/cameri/nostream/pull/741) publishes signed relay-discovery and monitor-announcement events after a probe, giving other clients a way to find the monitor's measurements through Nostr. [NIP-66](/en/topics/nip-66/) defines relay-discovery and monitor events so relay status can be shared in a common format.

The relay also [merged an opt-in trust-distance rule for adaptive proof of work](https://github.com/cameri/nostream/pull/779): an operator can lower the posting difficulty for keys near its web-of-trust graph while unknown keys retain the full requirement. No threshold is configured by default, so existing relays keep their previous admission behavior.

### nostter ties remote signing to the active session

[nostter](https://github.com/SnowCait/nostter) is a web Nostr client for reading and publishing through relays. Its [NIP-46 connection lifecycle](https://github.com/SnowCait/nostter/pull/2518) now belongs to the authenticated session's signer, so a failed login or session reset can dispose of the remote connection instead of leaving a module-global signer behind. [NIP-46](/en/topics/nip-46/) lets a client ask a separate signer to approve cryptographic operations over Nostr.

The client also [accepts images from the operating system's share menu](https://github.com/SnowCait/nostter/pull/2510), passing them to its normal composer and upload path. That makes sharing a photo into a Nostr post possible without first saving and selecting it inside the client.

### Zap Cooking publishes image descriptions and blocks secret-key searches

[Zap Cooking](https://github.com/zapcooking/frontend) is a Nostr recipe and long-form publishing site. Its [NIP-92 image-description work](https://github.com/zapcooking/frontend/pull/746) lets authors write alternative text for images in notes, replies, recipes, articles, and products, then carries that text in `imeta` tags that other clients can render. [NIP-92](/en/topics/nip-92/) standardizes media metadata attached to Nostr events, including image descriptions.

The site's [search fix](https://github.com/zapcooking/frontend/pull/744) now opens pasted `nostr:` identifiers directly and rejects secret-key input before it becomes a relay search. That matters because NIP-50 sends search terms to relays; accidentally pasting an `nsec` into the old search field could disclose the private key to those relays. [NIP-50](/en/topics/nip-50/) defines relay-side search filters for Nostr content.

### Divine Mobile reconnects idle relay subscriptions

[Divine Mobile](https://github.com/divinevideo/divine-mobile) is a short-video client that publishes and reads Nostr events. A [merged relay fix](https://github.com/divinevideo/divine-mobile/pull/9246) reconnects after an idle timeout or remote closure, including subscriptions that only receive data and never send another request to trigger recovery. That restores a path used by direct-message inboxes and moderation labels after a connection drops.

A separate [profile-verification fix](https://github.com/divinevideo/divine-mobile/pull/9293) waits for all queried relays before concluding that a profile has no linked accounts. The previous early empty answer could hide a valid identity event from a slower relay, so users see valid identity events from slower relays on a first profile view.

### Conduit uploads product images through Blossom

[Conduit](https://github.com/Conduit-BTC/conduit-mono) is a Nostr-based marketplace with merchant publishing tools. Its [merged image-upload work](https://github.com/Conduit-BTC/conduit-mono/pull/503) lets merchants add product images from desktop or mobile through a configured Blossom server while keeping product publication separately signed. Blossom is a media-storage protocol that uses Nostr identities to authorize uploads and let applications retrieve files.

The [upload path](https://github.com/Conduit-BTC/conduit-mono/pull/503) authorizes only the prepared image hash and selected server with a short-lived signed event, then checks the returned result. That gives a merchant an in-app media workflow without silently changing the signed server preference that governs where images go.

### Buzz adds authenticated relay moderation controls

[Buzz](https://github.com/block/buzz) includes a Nostr relay and community administration tools. Its [merged relay-admin routes](https://github.com/block/buzz/pull/7302) let authorized operators list active bans and timeouts and lift them through a signed HTTP request. [NIP-98](/en/topics/nip-98/) defines Nostr-event authorization for HTTP calls, allowing the relay to verify who made the administrative request.

The [unban and untimeout operations](https://github.com/block/buzz/pull/7302) write their audit record in the same database transaction as the restriction change. Operators can therefore inspect and reverse a live moderation decision without a successful reversal losing its audit trail.

### ContextVM SDK shortens publish waits and repairs streams

[ContextVM SDK](https://github.com/ContextVM/sdk) is a TypeScript toolkit for applications that exchange signed requests and streams over Nostr relays. Its [relay-pool change](https://github.com/ContextVM/sdk/pull/100) sends an event to every connected relay but, by default, finishes the caller's wait after the first positive acknowledgement; applications that need all acknowledgements can still request that mode. One slow relay no longer determines the normal publish wait.

The SDK also [repaired per-sender stream sequencing](https://github.com/ContextVM/sdk/pull/95) so client-started streams no longer reuse a sequence number for an accept and a control frame. The PR notes that tool-side consumption of those streamed chunks remains unwired, so this is a transport milestone, not a claim that every streaming application path is complete.

### Mostro preserves an order's original creation time

[Mostro](https://github.com/MostroP2P/mostro) is a peer-to-peer Bitcoin exchange coordinator that publishes orders over Nostr. Its [merged kind `38383` change](https://github.com/MostroP2P/mostro/pull/971) adds a stable `created_at` tag from the order record, allowing clients to sort or age an order by when it was opened instead of by its latest status revision. [NIP-69](/en/topics/nip-69/) defines the Nostr order format used by interoperable trading clients.

This is the implementation counterpart to the [proposed NIP-69 clarification](https://github.com/nostr-protocol/nips/pull/2476) below. Older clients can ignore the additive tag, while clients that read it can avoid making a returned or repaired order look newly created.

### Amethyst implements DECK-0003 objects and encrypted bag search

[Amethyst's merged DECK-0003 work](https://github.com/vitorpamplona/amethyst/pull/4186) reads and renders Simple Nostr Objects, a JSON 3D-mesh format carried in Nostr events. It supports kind `11333` avatars, kind `3330` shards, and opening encrypted kind `33330` region bags from a location hint. CLI commands parse and verify objects or calculate the bounded search needed to open a bag. The PR reports 15 passing conformance sections against reference implementations.

The [bag-search implementation](https://github.com/vitorpamplona/amethyst/pull/4186) is still a development milestone, not a device-verified release. Its card compiles and its state machine has unit tests, but it has not been exercised on a phone; the reachable real bags checked by the maintainer lack the hint needed to offer a search button. A synthetic bag is needed to exercise that user path.

### Amethyst broadens MLS interoperability and repairs desktop group rendering

[Amethyst's Quartz library](https://github.com/vitorpamplona/amethyst/pull/4187) now lets callers choose an MLS group ID and omit Marmot-only required capabilities when interoperating with other MLS stacks. Separate merged changes allow [extensions supported by every group member](https://github.com/vitorpamplona/amethyst/pull/4182), carry [authenticated application-message data](https://github.com/vitorpamplona/amethyst/pull/4184), and set an optional [key-package lifetime](https://github.com/vitorpamplona/amethyst/pull/4188). The Marmot defaults remain unchanged; these are shared-library capabilities, not a claim that every client UI exposes them.

A later [desktop render fix](https://github.com/vitorpamplona/amethyst/pull/4189) uses shared dialogs and prevents blank group messages after the display-layer split. These merged PRs are development progress, not a tagged Amethyst release.

### nostter gates signing and private reads on real capabilities

Continuing the session-owned NIP-46 work above, [nostter's merged signer migration](https://github.com/SnowCait/nostter/pull/2570) checks for an actual signer before offering write actions instead of treating every logged-in session as writable. [Private bookmarks](https://github.com/SnowCait/nostter/pull/2574) now require NIP-04 or NIP-44 decryption capability, and [remote-signer settings](https://github.com/SnowCait/nostter/pull/2576) require NIP-44 support. A read-only or anonymous account can still use non-writing profile actions.

The [npub display change](https://github.com/SnowCait/nostter/pull/2577) and subsequent authentication-state refactors continue that same migration. These are merged application changes, but no new tagged release is claimed here.

### Pensieve makes archive reconciliation bounded and durable

[Pensieve's archive receipt work](https://github.com/andotherstuff/pensieve/pull/48) waits for actual durable event markers before declaring a reconciliation attempt complete, retaining unresolved IDs across recovery. The [sealing change](https://github.com/andotherstuff/pensieve/pull/49) separates periodic archive durability from optional Parquet publication, and the [bounded inventory](https://github.com/andotherstuff/pensieve/pull/50) scans sealed segments with explicit limits and a persisted cursor.

These are [merged library increments](https://github.com/andotherstuff/pensieve/pull/50), not an enabled relay repair worker: runtime scheduling, peer-authenticated IPC, deployment, and production canary remain separate gates.

### MDK reduces repeated replay work for parked encrypted messages

[MDK's merged replay fix](https://github.com/marmot-protocol/mdk/pull/2007) addresses work repeated after a publish confirmation, publish failure, or group join when messages remain parked because they cannot yet be decrypted. The previous path classified each row's lineage again and rewound group state for each row and retained anchor. The new deferred-sweep ingest path skips redundant classification and shares a group-scoped cache of historical contexts, invalidating it when canonical state changes.

The [PR's regression tests](https://github.com/marmot-protocol/mdk/pull/2007) compare the one-row and eight-row parked-message cases. Its engine suite reports 681 passing tests and five skipped. This is merged library work after MDK 0.10.4, not part of that tagged release or a measured end-user latency claim.

GATE: PENDING REVIEW
