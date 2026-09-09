## In Development

### Zap Cooking renders NIP-27 references with relay hints

[The September 4 merge](https://github.com/zapcooking/frontend/pull/665) makes [Zap Cooking](https://github.com/zapcooking/frontend) render `nostr:npub` and `nostr:nprofile` references in articles, recipes, editor previews, and print views. Invalid identifiers remain text, resolution is non-blocking, and the editor previews the Markdown that will be signed. When relay information exists, a bare `npub` becomes an `nprofile` with outbox relays and a matching `p` tag.

The same week fixed [author-scoped kind `30023` reads](https://github.com/zapcooking/frontend/commit/6a379c680727bb49074a4ff85f070b404dba97a7), added [verified NIP-50 search relays](https://github.com/zapcooking/frontend/commit/1802e8d7e95ed482209d09e03c834c2d9adfc1ea) with deduplication and stale-query guards, and repaired [NIP-47 wallet calls](https://github.com/zapcooking/frontend/pull/705) after dependency changes broke balances and history.

### Conduit reconciles signed relay and Blossom preferences

[Conduit](https://github.com/Conduit-BTC/conduit-mono) merged [Blossom preference editing](https://github.com/Conduit-BTC/conduit-mono/pull/374) on September 2 and [signed preference reconciliation](https://github.com/Conduit-BTC/conduit-mono/pull/397) on September 7. Market and Merchant retain the latest valid kind `10002` relay list and kind `10050` inbox declaration, preserve a usable signed list when a newer event is malformed, distinguish an explicit empty list from an unavailable lookup, and do not replace failed declared relays with code defaults.

The [kind `10063` editor](https://github.com/Conduit-BTC/conduit-mono/pull/374) lets a user load, reorder, review, externally sign, publish, and read back an ordered HTTPS media-server list without contacting those servers or inserting an undeclared default.

### NIP-A3 payment targets reach three clients

From September 1–3, [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041), [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851), and [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) implemented NIP-A3 kind `10133` payment targets. Amethyst offers an opt-in handoff only when a compatible target exists and does not turn it into a zap; Grimoire uses a fixed registry before building wallet URIs; Pollerama validates Monero addresses and fetches the author's relay list before querying targets. Each client still needs an allowed payment method, a relay route, and an accurate display.

### Ditto expands Blossom fallback and live embeds

[Ditto](https://github.com/soapbox-pub/ditto) merged [broad Blossom fallback and mirroring](https://github.com/soapbox-pub/ditto/commit/1e35a0705c28f706eb40d1f99aedef3105cf6f07) on September 6. Avatars, badges, banners, community images, custom emoji, and application icons now try declared servers with the same blob hash; mirror uploads use a standard BUD-11 authorization token. A [September 4 change](https://github.com/soapbox-pub/ditto/commit/e2a29004a65122470179c83d6ded8336a5c10dfa) added compact `kind:30311` live-stream embeds.

writer_model: claude-opus-5 (bounded first-party fallback candidate; wrapper run `7dee2ec3-0440-4980-a0a5-9dd9ce854a4c`)

GATE: PENDING REVIEW
