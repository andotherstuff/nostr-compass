## Tagged releases

### n_cord v1.1 adds NSEC Bunker support

[n_cord](https://github.com/0n4t3/n_cord) is a Nostr-powered chat client inspired by Discord and IRC. [v1.1](https://github.com/0n4t3/n_cord/releases/tag/v1.1) adds [NIP-46](/en/topics/nip-46/) NSEC Bunker support alongside a reply-handling bug fix, a real signer-interoperability addition rather than routine maintenance.

### cdk v0.17.3 adds NIP-47 wallet-service support across cdk, cdk-nwc, and cdk-ffi

[cdk](https://github.com/cashubtc/cdk) is a Cashu development kit; this release is Bitcoin/Lightning-only in most respects, but [v0.17.3](https://github.com/cashubtc/cdk/releases/tag/v0.17.3) adds [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) service support with a dedicated NWC service crate, wallet integration, FFI bindings for `cdk-ffi`, and end-to-end test coverage, giving Cashu wallets built on cdk a standard Nostr Wallet Connect surface.

### Coop Mobile v0.2.4 improves Nostr Connect and adds ncryptsec1 import

[Coop Mobile](https://git.reya.su/reya/coop-mobile) is a [NIP-17](/en/topics/nip-17/) private-messaging client for mobile platforms. [v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4) improves its [NIP-46](/en/topics/nip-46/) Nostr Connect flow, fixes a loading indicator that stuck permanently on some connections, and adds import support for the [NIP-49](/en/topics/nip-49/) `ncryptsec1` encrypted key format alongside a redesigned identity-import screen.

### Nmail v0.14.0 ships on macOS with scheduled send and push notifications

[Nmail](https://github.com/nogringo/nostr-mail-client) is a mail client built on Nostr; [v0.14.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.14.0) brings the app to macOS, adds scheduled send with a dedicated Scheduled mailbox for queued messages, and adds push notifications. The release also switches address-book Nostr identifier resolution to NDK's [NIP-05](/en/topics/nip-05/) resolver in place of a bespoke implementation.

### Nostrord v2.2.0 adds a DM master toggle and richer direct messages

[Nostrord](https://github.com/nostrord/nostrord) is a [NIP-29](/en/topics/nip-29/) relay-based group-chat client for Android, iOS, web, and desktop. [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) adds a master toggle to disable all direct-message features at once ([PR #175](https://github.com/nostrord/nostrord/pull/175)) and ships "richer direct messages" ([PR #186](https://github.com/nostrord/nostrord/pull/186)), continuing from #30's coverage of the release folding the relay pool and detecting zombie WebSockets.

### Nostr WoT 0.3.86 hardens key backups and signing prompts

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension) is a browser extension pairing a Nostr identity with a Lightning wallet. [v0.3.86](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.3.86) moves encrypted-key backups to the standard [NIP-49](/en/topics/nip-49/) format, makes signing prompts show the full event and all tags instead of a summary, verifies relay data against its signature, and stops exposing the active identity when switching accounts. The extension also drops the unused `scripting` browser permission.

### Keep Android v1.1.8 adds first-run FROST onboarding

[Keep](https://github.com/privkeyio/keep-android) is an Android signer built on threshold FROST key shares. [v1.1.8](https://github.com/privkeyio/keep-android/releases/tag/v1.1.8) adds a first-run flow that explains FROST key shares and lets a new user pick a signing policy of Manual, Basic, or Auto before the first signature request arrives, shipping the tagged form of the onboarding work #30 covered as unreleased.

### Noscall v0.6.0 adds a Cashu wallet and relay-based push notifications

[Noscall](https://github.com/sanah9/noscall) is a secure audio- and video-calling app built on Nostr. [v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release) adds an account-scoped Cashu wallet with multi-mint balances, ecash send and receive, and Lightning pay and receive with quote persistence. The release also migrates Android push notifications off Firebase Cloud Messaging to a Nostr-relay-based delivery path through UnifiedPush, and improves iOS VoIP and APNs push reliability during login retries.

### Kubo ships tablet mode and group-chat photos

[Kubo](https://github.com/JeroenOnNostr/kubo) is a child-safe Nostr video platform with Web-of-Trust feed curation, not covered since 2026-06-24. [kubo-v2026.07.05](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v2026.07.05) adds an opt-in tablet grid layout for the child feed and support for attaching photos to group-chat messages, plus fixes for the sign-up button hiding behind the on-screen keyboard on Android.

### Nostr Codex Phone v0.2.9 adds git/diff/read-file helper requests

[Nostr Codex Phone](https://github.com/tidley/nostr-codex-phone) is a mobile control surface for a local coding-assistant worker communicating over encrypted Nostr DMs, which launched in #29. [v0.2.9](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.9) adds mobile OpenCode tool actions including git, diff, read-file, status, and history helper requests, session pin and search improvements, and a task-stop control, alongside an encrypted [Blossom](/en/topics/blossom/) upload wrapper that shipped in the preceding v0.2.8.

### GitWorkshop v3.0.3 fixes newly announced refs in the repo explorer

[GitWorkshop](https://github.com/DanConwayDev/gitworkshop) is a git-over-Nostr web UI for browsing and reviewing NIP-34 repositories. [v3.0.3](https://github.com/DanConwayDev/gitworkshop/releases/tag/v3.0.3) fixes the branches, tags, commits, and code-browsing views failing to resolve a ref that a repo announces after the explorer has already loaded it, alongside CI workflow-timing cleanup, confirmed directly against the tag and commit history.

### Bitcoin-Safe reaches Flathub, spotlighting its Nostr Sync & Chat plugin

[Bitcoin-Safe](https://bitcoin-safe.org) is a self-custody Bitcoin wallet built around hardware-signer workflows. The project [shipped a Flathub package](https://flathub.org/apps/org.bitcoin_safe.BitcoinSafe) this week, its first listing in a mainstream Linux app store. The Flathub release puts Bitcoin-Safe's Sync & Chat plugin in front of a wider audience: the plugin uses [NIP-17](/en/topics/nip-17/) direct messages, via the project's own [bitcoin-nostr-chat](https://github.com/andreasgriffin/bitcoin-nostr-chat) library, to synchronize wallet labels between a user's devices and to send and receive PSBTs for remote multisig co-signing between trusted participants. The Nostr layer itself shipped earlier, in [2.0.0](https://github.com/andreasgriffin/bitcoin-safe/releases/tag/2.0.0) (2026-06-29), which redesigned transaction signing around a "Share via Chat & Sync" connection type alongside QR, USB, and Bluetooth; this week's news is the Flathub reach rather than new protocol work. Whether the project eventually moves this messaging layer onto [Marmot](/en/topics/marmot/) (MLS-over-Nostr) instead of individually-wrapped NIP-17 DMs is worth watching as group-signing setups grow past two or three participants.
