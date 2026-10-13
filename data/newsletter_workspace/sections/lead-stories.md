## Top Stories

### Amethyst

[Amethyst v1.18.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.18.0) brings the Android social client's shared interface to desktop, with custom feeds, wide-window decks, opt-in locks, encrypted media and [Blossom uploads](/en/topics/blossom/). Provider scores from [NIP-85, trusted assertions](/en/topics/nip-85/), are indexed locally for requests, notifications and badges, with user-selected providers and thresholds.

Today's [v1.19.0 release](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0) adds native Wayland support and desktop video compression using separately installed FFmpeg and ffprobe. Key-storage fixes address repeated keychain prompts and Linux keyring failures. Calendar collections and RSVPs gain rendering, and the Android login interface adds [NIP-46 remote signing](/en/topics/nip-46/). Parallel opening of encrypted envelopes precedes serial indexing, while relay reconnection and feed-author relay-list handling are corrected. The [relay client honors rate-limit backoff](https://github.com/vitorpamplona/amethyst/pull/4422) before resuming subscriptions or publications.

The [trust-provider relay change](https://github.com/vitorpamplona/amethyst/pull/4437) treats provider relays from the user's kind 10040 list as own, trusted relays. Those connections use a direct route by default; Tor requires enabling the trusted-relays setting. The main client's [NIP-42 relay authentication](/en/topics/nip-42/) can disclose the user's public key to these relays.

### Amber

[Amber 6.6.9](https://github.com/greenart7c3/Amber/releases/tag/v6.6.9) fixes three security flaws in the Android Nostr signer. [Revoked permissions](https://github.com/greenart7c3/Amber/security/advisories/GHSA-8f7m-9g64-vrjw) no longer survive a cache race, and explicit rejections override fully trusted status. [Copied secrets](https://github.com/greenart7c3/Amber/security/advisories/GHSA-g62f-m6pm-jv9p) receive a system-scheduled clipboard clear after 60 seconds, including when the process is killed; contents remain readable during that interval, and newer copied text may also be cleared. Changing [“require unlocked device”](https://github.com/greenart7c3/Amber/security/advisories/GHSA-wv7c-hq2j-ppc5) preserves the old wrapping key until secret migration completes, while previously lost keys remain lost. The release repairs multi-request nostrconnect approvals and replies on the URI's specified relays. Users of 6.6.8 and earlier should update.

### Keep Android

[Keep Android v1.3.0](https://github.com/privkeyio/keep-android/releases/tag/v1.3.0), a [FROST threshold signer](/en/topics/frost/), adds on-device distributed key generation and authenticated recovery of interrupted share operations. It also handles devices without StrongBox support. With threshold signing, participating devices hold shares of the signing secret and cooperate to produce a signature; the setup and recovery steps determine which devices can participate.

[Version 1.3.1](https://github.com/privkeyio/keep-android/releases/tag/v1.3.1) prevents automatic signing from overriding remembered refusals, Ask permissions, expired approvals or failed permission reads. Expiry removes background approval while retaining denials. The [per-app policy migration](https://github.com/privkeyio/keep-android/pull/532) moves permissions into the core-owned store while preserving stricter decisions.

### Chama

[Chama v6.4.21](https://github.com/jesuspirate/chama/releases/tag/v6.4.21) [authenticates the native wallet bridge](https://github.com/jesuspirate/chama/pull/29) used by its Nostr-mediated trade application, disables production URL-based bridge redirection and validates payout amounts. It also refuses to wipe a wallet whose contents cannot be read.

[Version 6.4.22](https://github.com/jesuspirate/chama/releases/tag/v6.4.22) hardens replay against outsider events, checks successor relationships, rejects empty arbiter pools and derives refund timing from the signed LOCK time. Its consensus changes apply to CREATE events signed from November 1, 2026; the client protections apply immediately. The release notes retain caveats about listing-selected federations and dust payouts. Subsequent [signer and recovery changes](https://github.com/jesuspirate/chama/releases/tag/v6.4.23) add protected-seed readers and recoverable late locks, while [v6.4.24](https://github.com/jesuspirate/chama/releases/tag/v6.4.24) improves large trade lists.

### Zap Cooking

The recipe and social client [Zap Cooking merges safeguards for follow-list edits](https://github.com/zapcooking/frontend/pull/795) against incomplete, stale or unexpectedly shrinking reads. Follow actions share one guarded update path that preserves existing tags and content. Signer identity is checked before publication. Its [membership authorization fix](https://github.com/zapcooking/frontend/pull/802) uses the public key signing the authenticated request. A [route that exposed an administrative secret was removed](https://github.com/zapcooking/frontend/pull/801); deployment still requires secret rotation, which a merged change alone cannot establish. Later [thread and bookmark repairs](https://github.com/zapcooking/frontend/pull/833) preserve the real reply root and recover failed bookmark writes. [Recipe tag fields](https://github.com/zapcooking/frontend/pull/836) no longer send keystrokes to profile or NIP-50 search services or leave the editor with unsaved changes.

writer_model: direct-codex

GATE: PASS (source-owner content review; full publication receipts are separate)
