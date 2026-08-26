## Unreleased Changes

### Shopstr keeps remote-signer and wallet secrets out of browser storage

[Shopstr](https://github.com/shopstr-eng/shopstr) is a web marketplace for [NIP-99](/en/topics/nip-99/) classified listings. After [last month's payment-integrity work](/en/newsletters/2026-07-22-newsletter/#shopstr-binds-payment-validation-to-signed-receipts-and-server-side-prices), it [stops writing serialized bunker signer secrets to `localStorage`](https://github.com/shopstr-eng/shopstr/pull/437). A [NIP-46](/en/topics/nip-46/) (remote signing) bunker payload had included the live `bunker://` URL and the generated app private key, so any script in the Shopstr origin could resume the remote-signing session. Bunker data now stays in runtime memory for the current session, leftover bunker payloads are removed when they are found, and non-bunker signer types keep their previous storage behavior.

The matching [NWC change](https://github.com/shopstr-eng/shopstr/pull/436) does the same for [NIP-47](/en/topics/nip-47/) (wallet-connect) credentials. Shopstr had stored the full `nostr+walletconnect://` string, including the secret used for wallet actions, as ordinary browser data and reused it at checkout. Connection strings and wallet metadata now stay in memory, and older stored copies are deleted when local data is read. Scripts that already run in the Shopstr origin during an active session can still see those in-memory values.

### Routstr verifies relay-sourced provider discovery

A single malicious relay could previously decide which inference providers a Routstr client trusted. [Routstr SDK](https://github.com/Routstr/routstr-sdk) is the TypeScript library behind Routstr, a marketplace that discovers AI providers on Nostr and pays them with Cashu. [This week's discovery fix](https://github.com/Routstr/routstr-sdk/pull/47) verifies every relay-delivered provider announcement, model list, and review (kinds 38421, 38423, and 38425) before any consumer sees it, so a review that names a trusted pubkey but carries a garbage signature no longer enters ranking.

[Far-future timestamps](https://github.com/Routstr/routstr-sdk/pull/47) are dropped before "latest review" selection. Events more than fifteen minutes ahead of the local clock are removed on the live path and when reading the persistent store, which stops a forged `created_at` from outranking validly signed reviews across restarts. If trusted reviews are unavailable, the review gate fails closed and excludes unreviewed providers from payment ranking until reviews arrive. Operators can still force-enable a provider by hand.

### nostr-tools binds gift-wrap rumors to their seals

Unwrapping a [NIP-59](/en/topics/nip-59/) (gift wrap) event used to decrypt the wrap, decrypt the seal, and return the inner rumor without checking who the seal came from. [nostr-tools](https://github.com/nbd-wtf/nostr-tools) is a JavaScript library of Nostr protocol helpers. [This week's unwrap fix](https://github.com/nbd-wtf/nostr-tools/pull/545) requires the wrap to be kind 1059, the seal to be kind 13 with a valid signature, and the rumor's `pubkey` to equal the seal's `pubkey`. Decrypting the seal already proves control of `seal.pubkey`. Without the last check, anyone could seal a rumor that named someone else as author and have a client attribute the message to that victim.

[NIP-17](/en/topics/nip-17/) (gift-wrapped private DMs) uses the same unwrap path, so the bind applies to private DMs. [Batch unwrap](https://github.com/nbd-wtf/nostr-tools/pull/545) now skips a wrap that fails those checks instead of throwing, because gift wraps are unsolicited and one hostile event would otherwise discard the rest of a relay query.

### Haven adds signed relay administration and a local notes browser

[Haven](https://github.com/barrydeen/haven) is a self-hosted Nostr relay and Blossom media server. Its newly merged [administration console](https://github.com/barrydeen/haven/pull/135) exposes NIP-86 management calls on each relay endpoint, with every request authenticated by a NIP-98 event from the configured owner. Operators can manage bans, allowlists, kind rules, relay names, and stored media without giving the relay a signing key. A read-only notes browser keeps encrypted kinds opaque and loads remote media only after a click, avoiding an automatic request that would reveal the operator's IP address to an outside host.

The same [Haven change](https://github.com/barrydeen/haven/pull/135) adds persistent traffic charts and fixes a default-LMDB failure in which counting stored events could loop forever, pin a CPU core, and block later statistics calls. Haven now uses the backend counter where it terminates and a bounded event walk otherwise. The project added its first 23 tests around event paging, deletion, metrics persistence, owner checks, and URL-bound request signatures.

### Amethyst moves Blossom authorization off image-loading threads

[Amethyst](https://github.com/vitorpamplona/amethyst), an Android Nostr client, [stops waiting for Blossom read authorization on OkHttp dispatcher threads](https://github.com/vitorpamplona/amethyst/pull/3991). The interceptor now starts signing away from the network thread, while the image fetcher awaits one shared signature per host and retries the protected blob request. A burst of gated images therefore no longer occupies every per-host connection slot while a signer responds.

The same [Amethyst patch](https://github.com/vitorpamplona/amethyst/pull/3991) brings the token encoding into line with BUD-11: Base64url without padding, `server` scope, and no blob-specific `x` tag, allowing one token to cover multiple blobs on the same host. New concurrency tests exercise caching, expiry, signed retries, and sixteen simultaneous callers sharing one signature.

GATE: PENDING REVIEW
