## In Development

### Keep adds kind-scoped NIP-44 v3 signing and tightens approval policy

Keep merged five Android signer changes that carry [NIP-44 (Encrypted Payloads)](/en/topics/nip-44/) v3 encrypt and decrypt requests through both [NIP-55 (Android Signer Application)](/en/topics/nip-55/) transports and its [NIP-46 (Nostr Connect)](/en/topics/nip-46/) bunker. [PRs #451](https://github.com/privkeyio/keep-android/pull/451), [#452](https://github.com/privkeyio/keep-android/pull/452), and [#453](https://github.com/privkeyio/keep-android/pull/453) keep v3 grants separate from v2, scope them by event kind, reject missing or invalid kinds, and preserve approval requests opened from notifications. [PRs #454](https://github.com/privkeyio/keep-android/pull/454) and [#455](https://github.com/privkeyio/keep-android/pull/455) stop treating the Basic signing policy as Auto and move the global selection into the core-owned encrypted store. The Keep maintainers merged all five changes after the latest tagged Android release.

### Routstrd changes its default network bind after an unauthenticated exposure

Routstrd [PR #56](https://github.com/Routstr/routstrd/pull/56) changes the local Nostr inference router's default bind address from all network interfaces to `127.0.0.1`. The former default exposed unauthenticated wallet balance, history, unlock, send, refund, API-key, provider, client, usage, and daemon-stop endpoints to any host that could reach the port. Operators can still configure a non-local bind explicitly, but the merged change makes a fresh deployment local-only by default and has not yet appeared in a tagged release.

### Imwald Android clarifies offline publishing status

Imwald Android, an Android Nostr client, now treats acknowledgement from a local relay as a completed publish only when every configured target is local. Its [offline-publishing and outbox fix](https://git.imwald.eu/silberengel/imwald-android/commit/f4de9f61df35110c77d2e5f99d764c0df176962b) keeps remote delivery pending when a local relay has accepted the event but configured remote relays have not, so the publish report distinguishes device-local storage from relay delivery.

### FIPS opens an OpenWrt access layer and starts a FreeBSD port

The Free Internetworking Peering System now lets an OpenWrt router expose an open `!FIPS` access network through [merged PR #126](https://github.com/jmcorgan/fips/pull/126). The parallel [FreeBSD PR #129](https://github.com/jmcorgan/fips/pull/129) ports the daemon, TUN data path, `.fips` name resolution, service management, and native package build. Together, the changes widen the paths into the encrypted peer-to-peer network from dedicated routers to another general-purpose operating system.

A July 26 [FIPS project update](https://primal.net/e/d0afe733f75e909341ab7f39834883968df097472238a474df3a3346c5d38f51) reported more than 300 nodes on its public UDP overlay and a broader mesh approaching 2,000 nodes. The [FIPS repository](https://github.com/jmcorgan/fips) spent the same week hardening concurrent network tests, rekey continuity, hop-limit behavior, firewall checks, and NAT-lab isolation. Those changes give operators reproducible behavior checks as the network grows.

### Zap Cooking schedules posts and binds scanner requests

Zap Cooking, a Nostr recipe-sharing and meal-planning app, can now retain a scheduled post in encrypted storage and publish it when due through a periodic relay sweep ([PR #566](https://github.com/zapcooking/frontend/pull/566), [PR #569](https://github.com/zapcooking/frontend/pull/569)). That gives users a scheduled-publishing path without leaving unsigned post content exposed in the scheduler's database.

Its fridge scanner now authenticates the exact request body with [NIP-98](/en/topics/nip-98/) HTTP authentication, so membership checks rely on the key that signed the scan request instead of a pubkey supplied in its body ([PR #599](https://github.com/zapcooking/frontend/pull/599)).

### Citrine turns an Android device into a manageable relay

Citrine, an Android-hosted Nostr relay, can now send events it has stored to external relays, giving an operator a way to rebroadcast local history ([PR #179](https://github.com/greenart7c3/Citrine/pull/179)). It also adds [NIP-86 (Relay Management API)](/en/topics/nip-86/) commands so compatible clients can administer the relay ([PR #150](https://github.com/greenart7c3/Citrine/pull/150)).

Group operators can administer [NIP-29](/en/topics/nip-29/) relay-based groups through Amber signing in [PR #178](https://github.com/greenart7c3/Citrine/pull/178), while [PR #174](https://github.com/greenart7c3/Citrine/pull/174) keeps Tor-backed relay configuration and lifecycle state aligned through restarts.

### Wired recovers complete conversations in the browser

Wired, a browser-based Nostr client, now follows feed roots, replies, and referenced events to completion instead of stopping at fixed breadth or result limits ([PR #148](https://github.com/smolgrrr/Wired/pull/148), [PR #147](https://github.com/smolgrrr/Wired/pull/147), [PR #146](https://github.com/smolgrrr/Wired/pull/146)). Users can therefore recover deeper threads and feed context when the relevant events are available from their relays.

The browser also preserves relay hints on referenced events and uses them only for still-missing context, restoring conversations that configured relays do not carry ([PR #145](https://github.com/smolgrrr/Wired/pull/145), [PR #144](https://github.com/smolgrrr/Wired/pull/144)). Incomplete retrieval is kept distinct from a completed snapshot, so a partial response does not overwrite the prior cached view.

GATE: PASS (prepublish refresh: five review gates PASS at 2026-07-29T14:00:03Z; 113/113 external URLs 200, claims/style/topics/continuity verified)
