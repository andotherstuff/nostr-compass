## Tagged releases

### Amber v6.3.0 groups bunker signing approvals and adds Expert List support

[Amber](https://github.com/greenart7c3/Amber) is an Android [NIP-46](/en/topics/nip-46/) remote signer. [v6.3.0](https://github.com/greenart7c3/Amber/releases/tag/v6.3.0) adds grouped multi-request approval for bunker signing so a batch of pending signature requests can be reviewed and approved together instead of one prompt at a time. The release also adds support for Expert List (kind 12022) and Expert Pack (kind 32022) events, a privacy mode that hides sensitive content on screen, and a change to fetch an account's [NIP-65](/en/topics/nip-65/) relay list before its profile metadata so signer flows start from the user's actual relay set. This follows the v6.2.x line covered in the 2026-07-08 issue.

### Nostrord v2.3.0 ships the client side of this week's NIP-29 spec work

[Nostrord v2.3.0](https://github.com/nostrord/nostrord/releases/tag/v2.3.0) is the shipped half of the NIP-29 cluster covered in this week's News section, and adds [PR #192](https://github.com/nostrord/nostrord/pull/192) (moderation wiring) beyond what the lead story lists. The release follows v2.2.0's DM controls covered in #31.

### Wisp v1.2.0 adds a multi-account switcher and collapsible reply threads

[Wisp](https://github.com/barrydeen/wisp) is a Nostr client. [v1.2.0](https://github.com/barrydeen/wisp/releases/tag/v1.2.0) adds a multi-account switcher, collapsible reply threads for long conversations, stripping of tracking parameters from note links, and a wallet transaction-history view. The release follows the Wisp update covered in the 2026-07-08 issue.

### ClipRelay v0.1.2 (new project) syncs clipboards across devices over Nostr relays

[ClipRelay](https://github.com/tajava2006/cliprelay) is a newly launched app, tracked for the first time this week via its [Zapstore](https://zapstore.dev) listing. [v0.1.2](https://github.com/tajava2006/cliprelay) syncs clipboard contents across a user's devices using Nostr relays as the transport, a simple and legible Nostr-native utility. This is ClipRelay's first appearance in the newsletter.

### Sonar v0.1-alpha.11 continues the alpha line

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar), last week's lead story, cut [v0.1-alpha.11](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.11) with work on the Rust mesh link engine, BLE and mesh fixes, and relay diagnostics; an incremental follow-up to the alpha line covered in #31 rather than a new headline.

### nostr-social-graph 2.0.0 and the rest of the week's smaller launches

[nostr-social-graph 2.0.0](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.0), the Iris-ecosystem social-graph library from this week's News section, is a major-version bump adding signed Nostr identity roster operations, device-approval flows with a canonical three-field bootstrap URI, and FIPS transport identity facets with shared Rust/TypeScript test vectors. Breaking changes for 1.x consumers. Beyond the cluster, three smaller launches deserve one line each: [noscall v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release), the Nostr calling app, migrated its push notifications to UnifiedPush, keeping call signaling off Google's push infrastructure; [nostr-vpn v4.1.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.1.1), a mesh VPN that uses Nostr for signaling, launched on Zapstore; and two new apps debuted there as well: StableKraft, a Nostr-plus-Lightning music and podcast aggregator, and Hakari, an encrypted Nostr backup for a weight logger.

### Amethyst lands v1.13.0 pre-release QA on napplet isolation and Concord authority

[Amethyst](https://github.com/vitorpamplona/amethyst) merged 81 PRs this week ahead of its v1.13.0 release. [PR #3650](https://github.com/vitorpamplona/amethyst/pull/3650) is a pre-release QA pass covering napplet account isolation, Concord authority fixes, and around 30 other fixes, with [PR #3653](https://github.com/vitorpamplona/amethyst/pull/3653) and [PR #3654](https://github.com/vitorpamplona/amethyst/pull/3654) continuing the same hardening line. This continues #31's coverage of Amethyst's clean-room Concord client implementation, tightening the authority and isolation behavior of that work before it ships tagged.

GATE: PASS
