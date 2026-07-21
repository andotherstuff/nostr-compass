## Tagged releases


### Amber v6.3.0 groups bunker signing approvals and adds Expert List support

[Amber](https://github.com/greenart7c3/Amber) is an Android [NIP-46](/en/topics/nip-46/) remote signer. [v6.3.0](https://github.com/greenart7c3/Amber/releases/tag/v6.3.0) adds grouped multi-request approval for bunker signing so a batch of pending signature requests can be reviewed and approved together instead of one prompt at a time. The release also adds support for Expert List (kind 12022) and Expert Pack (kind 32022) events, a privacy mode that hides sensitive content on screen, and a change to fetch an account's [NIP-65](/en/topics/nip-65/) relay list before its profile metadata so signer flows start from the user's actual relay set. This follows the v6.2.x line covered in the 2026-07-08 issue.

### Nostrord v2.2.0 follow-up

With [v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays) leading this week's News section, the tagged-release slot notes only what the lead does not: v2.3.0 follows v2.2.0's DM controls covered in #31, making this the client's second consecutive weekly release.

### Wisp v1.2.0 adds a multi-account switcher and collapsible reply threads

[Wisp](https://github.com/barrydeen/wisp) is a privacy-oriented Nostr client with built-in wallet support. [v1.2.0](https://github.com/barrydeen/wisp/releases/tag/v1.2.0) adds a multi-account switcher for moving between profiles without re-login, collapsible reply threads for long conversations, stripping of tracking parameters from note links before they open, and a wallet transaction-history view. The release follows the Wisp update covered in the 2026-07-08 issue.

### ClipRelay v0.1.2 (new project) syncs clipboards across devices over Nostr relays

[ClipRelay](https://github.com/tajava2006/cliprelay) is a newly launched cross-platform app (Android, macOS, Windows, Linux) that syncs your clipboard across your own devices: copy on one machine, paste on another. All traffic moves through Nostr relays as [NIP-44](/en/topics/nip-44/) encrypted events addressed to yourself, so there is no server to run and no account to create; the private key stays outside the app. [v0.1.2](https://github.com/tajava2006/cliprelay/releases) fixes a subtle sync failure where a machine waking from sleep kept publishing but silently stopped receiving, and tightens the relay-status indicators that previously reported dead subscriptions as healthy. This is ClipRelay's first appearance in the newsletter.

### Sonar v0.1-alpha.11 continues the alpha line

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar), last week's lead story, cut [v0.1-alpha.11](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.11) with work on the Rust mesh link engine, BLE and mesh fixes, and relay diagnostics; an incremental follow-up to the alpha line covered in #31.

### The week's smaller launches

Three smaller releases deserve one line each: [noscall v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release), the Nostr calling app, migrated its push notifications to UnifiedPush, keeping call signaling off Google's push infrastructure; [nostr-vpn v4.1.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.1.1), a mesh VPN that uses Nostr for signaling, shipped an update on Zapstore; and two new apps debuted there as well: StableKraft, a Nostr-plus-Lightning music and podcast aggregator, and Hakari, an encrypted Nostr backup for a weight logger.

### Amethyst lands v1.13.0 pre-release QA on napplet isolation and Concord authority

[Amethyst](https://github.com/vitorpamplona/amethyst) merged 81 PRs this week ahead of its v1.13.0 release. [PR #3650](https://github.com/vitorpamplona/amethyst/pull/3650) is a pre-release QA pass covering napplet account isolation, Concord authority fixes, and around 30 other fixes, with further v1.13.0 prep PRs landing through 07-21. This continues #31's coverage of Amethyst's clean-room Concord client implementation, tightening the authority and isolation behavior of that work before it ships tagged.


GATE: PASS
