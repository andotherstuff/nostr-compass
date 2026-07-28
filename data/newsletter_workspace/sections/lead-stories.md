## Top Stories

### Amethyst 1.13.0 ships Nostr apps, collaboration, and new payment paths

[Amethyst 1.13.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0), the July 28 release of the Android and multiplatform Nostr client, opens NIP-5D napplets and NIP-5A nsites inside an isolated, keyless browser process. A consent-gated `window.nostr` bridge can sign and use selected capabilities through the active account, while per-site and per-account permission screens let users review or revoke those grants. Favorite apps can stay pinned in the bottom bar without sharing cookies, login state, or grants across accounts.

The same [Amethyst release](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0) adds Git repository trees, issues, and pull requests alongside Concord communities, NIP-29 relay groups, Buzz group chat, wiki pages, and RSS feeds. Those surfaces turn the release into a collaboration update, not only a social-feed refresh: a user can move between code, community, and publishing views under the same Nostr identity.

Payments and identity also widened in [version 1.13.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0). Amethyst can create and pay BOLT12 offers, starts remote-signer accounts automatically, adds Blossom fallback servers, and expands Web of Trust controls for badges, communities, and relay groups. The release notes also record a large accessibility, translation, desktop, performance, and stability pass.

### Code Call 0.2.66 keeps several remote work sessions moving from a phone

[Code Call 0.2.66](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.66), an Android remote for computer-side coding sessions, can ask a routed worker for a concise catch-up from the latest phone message. It keeps multiple sessions independent, accepts replies only from the expected sender, and keeps its inbox connected to each configured worker relay for background delivery. Encrypted [NIP-17 (Private Direct Messages)](/en/topics/nip-17/) keeps requests and replies private, while encrypted [Blossom](/en/topics/blossom/) attachments can arrive with their original file type intact. These releases let the phone maintain and catch up with multiple independently routed computer-side sessions.

### GitWorkshop coordinates maintainers and keeps repository sync independent

[GitWorkshop's July 27 signed release](https://primal.net/e/869e01f9a74d98f468a66f3b83865d198a82cc718c1db36324398b1b88a17c60) adds Android login through [NIP-55 (Android Signer Application)](/en/topics/nip-55/) to the browser-based [NIP-34 (`git` stuff)](/en/topics/nip-34/) forge. Its [source repository](https://github.com/DanConwayDev/gitworkshop) now coordinates lead maintainers recursively, preserves each maintainer's relay hints, and keeps repository synchronization independent from invitation acceptance. Cross-repository work-item references connect related work across repositories, while GRASP copies repository data to selected Git endpoints without coupling that transfer to invitation delivery.

### Mosaico 0.1.2 gives coding agents a shared Nostr coordination fabric

[Mosaico 0.1.2](https://github.com/pablof7z/mosaico/releases/tag/v0.1.2) gives coding-agent sessions in Claude Code, Codex, Goose, Hermes, OpenCode, and Grok a shared-awareness fabric over [NIP-29 (Relay-based Groups)](/en/topics/nip-29/). Sessions broadcast short status updates and can find related active work across hosts while keeping their transcripts and context separate.

Named Codex profile discovery and Goose's Top Of Mind view expose the fabric inside two more harnesses ([PR #618](https://github.com/pablof7z/mosaico/pull/618), [PR #619](https://github.com/pablof7z/mosaico/pull/619)). Hosted agents can acquire a public fabric again, and setup now requires an explicit relay choice ([PR #626](https://github.com/pablof7z/mosaico/pull/626), [PR #629](https://github.com/pablof7z/mosaico/pull/629)). Mosaico remains an awareness layer, not an agent host, orchestrator, or transcript merger.

GATE: PENDING REVIEW
