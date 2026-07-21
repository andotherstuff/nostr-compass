## Tagged releases

### Amber v6.3.0 groups bunker signing approvals and adds Expert List support

[Amber](https://github.com/greenart7c3/Amber) is an Android [NIP-46](/en/topics/nip-46/) remote signer. [v6.3.0](https://github.com/greenart7c3/Amber/releases/tag/v6.3.0) adds grouped multi-request approval for bunker signing so a batch of pending signature requests can be reviewed and approved together instead of one prompt at a time. The release also adds support for Expert List (kind 12022) and Expert Pack (kind 32022) events, a privacy mode that hides sensitive content on screen, and a change to fetch an account's [NIP-65](/en/topics/nip-65/) relay list before its profile metadata so signer flows start from the user's actual relay set. This follows the v6.2.x line covered in the 2026-07-08 issue.

### Nostrord v2.3.0 ships the client side of this week's NIP-29 spec work

[Nostrord](https://github.com/nostrord/nostrord) is a [NIP-29](/en/topics/nip-29/) relay-based group-chat client for Android, iOS, web, and desktop. [v2.3.0](https://github.com/nostrord/nostrord/releases/tag/v2.3.0) lands the shipped half of the NIP-29 cluster covered in this week's News section: cross-platform [NIP-51](/en/topics/nip-51/) mute lists, wired-up NIP-29 moderation actions on all UIs ([PR #188](https://github.com/nostrord/nostrord/pull/188), [PR #192](https://github.com/nostrord/nostrord/pull/192), [PR #195](https://github.com/nostrord/nostrord/pull/195)), consent-gated group invites with cross-relay detection, and Tor .onion relay support. The release follows v2.2.0's DM controls covered in #31.

### Wisp v1.2.0 adds a multi-account switcher and collapsible reply threads

[Wisp](https://github.com/barrydeen/wisp) is a Nostr client. [v1.2.0](https://github.com/barrydeen/wisp/releases/tag/v1.2.0) adds a multi-account switcher, collapsible reply threads for long conversations, stripping of tracking parameters from note links, and a wallet transaction-history view. The release follows the Wisp update covered in the 2026-07-08 issue.

### ClipRelay v0.1.2 (new project) syncs clipboards across devices over Nostr relays

[ClipRelay](https://github.com/tajava2006/cliprelay) is a newly launched app, tracked for the first time this week via its [Zapstore](https://zapstore.dev) listing. [v0.1.2](https://github.com/tajava2006/cliprelay) syncs clipboard contents across a user's devices using Nostr relays as the transport, a simple and legible Nostr-native utility. This is ClipRelay's first appearance in the newsletter.

### Sonar v0.1-alpha.11 continues the alpha line

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar), last week's lead story, cut [v0.1-alpha.11](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.11) with work on the Rust mesh link engine, BLE and mesh fixes, and relay diagnostics; an incremental follow-up to the alpha line covered in #31 rather than a new headline.

### nostr-social-graph 2.0.0 ships signed roster operations and device approval

[nostr-social-graph](https://github.com/mmalmi/nostr-social-graph) is the social-graph library in the Iris ecosystem cluster covered in this week's News section. [2.0.0](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.0) is a major version adding signed Nostr identity roster operations, device-approval flows with a canonical three-field bootstrap URI, and FIPS transport identity facets with shared Rust/TypeScript test vectors. The major-version bump signals breaking changes for consumers of the 1.x API; see the News item for how it fits with this week's nostr-pubsub and fips-ts releases from the same ecosystem.

### Amethyst lands v1.13.0 pre-release QA on napplet isolation and Concord authority

[Amethyst](https://github.com/vitorpamplona/amethyst) merged 81 PRs this week ahead of its v1.13.0 release. [PR #3650](https://github.com/vitorpamplona/amethyst/pull/3650) is a pre-release QA pass covering napplet account isolation, Concord authority fixes, and around 30 other fixes, with [PR #3653](https://github.com/vitorpamplona/amethyst/pull/3653) and [PR #3654](https://github.com/vitorpamplona/amethyst/pull/3654) continuing the same hardening line. This continues #31's coverage of Amethyst's clean-room Concord client implementation, tightening the authority and isolation behavior of that work before it ships tagged.

GATE: PASS
