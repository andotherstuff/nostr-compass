## Releases

### Jumble 26.8.1 adds proof-of-work controls and comment previews

[Jumble 26.8.1](https://github.com/CodyTseng/jumble/releases/tag/v26.8.1) is a web and desktop Nostr client. It remembers proof-of-work difficulty for publishing, displays verified-work badges, and previews linked comments above external content. Reaction notifications now discard unsupported event kinds, relay disconnect notices are less noisy, default relays were refreshed, and a media-autoplay conflict was fixed.

### nostr-calendar 2.1.0 restores private-form signer binding

[nostr-calendar 2.1.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.1.0) publishes calendars, events, and form responses as Nostr data. It binds private-form submissions to the active signer, saves intentional duplicate events to relays, fixes relay fetching, parses calendar dates in local time, and adds app notifications plus an iOS client. The signer correction prevents a stale identity from producing an unusable encrypted response.

### Manent 2.0.0 adds tagging and search for saved notes

[Manent 2.0.0](https://github.com/dtonon/manent/releases/tag/v2.0.0) is a personal archive for signed Nostr notes. It adds local tags and search, letting a reader organize and retrieve saved events without modifying their signed contents.

### nosvelte 0.6.1 closes empty subscriptions after EOSE

[nosvelte 0.6.1](https://github.com/akiomik/nosvelte/releases/tag/v0.6.1) provides reactive Svelte components and hooks for relay data. Empty searches now settle at End of Stored Events, cancellation closes the underlying `REQ`, retries clear stale errors, and list hooks return their documented empty value. It also recognizes addressable events regardless of where their `d` tag appears, replaces superseded metadata and articles, deduplicates reactions by event ID, and keeps every event from a relay's first batch.

GATE: PASS
