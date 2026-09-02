## NIP Updates and Protocol Spec Work

### Nostr Implementation Possibilities

Two specification merges landed in the core [NIPs repository](https://github.com/nostr-protocol/nips) this week.

[NIP-67](/en/topics/nip-67/) defines hints a relay can append to an `EOSE` (end of stored events) message so a client knows whether to keep paginating. The [merged `"auth"` hint](https://github.com/nostr-protocol/nips/pull/2371) adds a third value beside `finish` and `more`: a relay may now signal that additional stored events could become visible if the user authenticates, and it must send the [NIP-42](/en/topics/nip-42/) (relay authentication) `AUTH` challenge before the `EOSE` that carries the hint. The [accompanying NIP-42 addition](https://github.com/nostr-protocol/nips/pull/2371) defines the same flow from the client side, so a client that receives an `EOSE` with `auth` already holds the challenge it needs to answer.

[NIP-84](/en/topics/nip-84/) (portable highlights, the kind `9802` events Amethyst shipped support for above) [merged a tag-scheme update](https://github.com/nostr-protocol/nips/pull/2454): highlights may now tag their source with structured `i` tags per [NIP-73](/en/topics/nip-73/) (external content identifiers) in addition to `a`/`e` tags for Nostr events and `r` tags for anything else, and quote highlights moved from a MUST to a SHOULD on rendering like a quote repost.

### Nostr Wallet Connect

A `list_transactions` response can report how many transactions match the request, not how many rows the current page returned. [Merged optional `total_count`](https://github.com/nostr-wallet-connect/nwc/pull/4) on NWC-05 (the wallet-history extension) in the [NWC extension repository](https://github.com/nostr-wallet-connect/nwc) adds that field to the response used with [NIP-47](/en/topics/nip-47/) (encrypted remote wallet control over Nostr).

The [commit that adds `total_count`](https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67) documents it as an optional integer: the total number of transactions matching the request filters.

The [commit that excludes pagination from the count](https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e) states that this total excludes pagination, so it counts all matching transactions across every page.

GATE: PENDING REVIEW
