## Top Stories

### Amethyst 1.13.1 follows its Nostr apps launch with authenticated group and Blossom access

[Amethyst 1.13.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0), released July 28 for the Android and multiplatform Nostr client, opens napplets and NIP-5A nsites inside an isolated, keyless browser process. A consent-gated `window.nostr` bridge can sign and use selected capabilities through the active account, while per-site and per-account permission screens let users review or revoke those grants. Favorite apps can stay pinned in the bottom bar without sharing cookies, login state, or grants across accounts.

The same [1.13.0 release](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0) adds Git repository trees, issues, and pull requests alongside Concord communities, NIP-29 relay groups, Buzz group chat, wiki pages, and RSS feeds. Those surfaces let a user move between code, community, publishing, and social views under the same Nostr identity.

Payments and identity also widened in [version 1.13.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0). Amethyst can create and pay BOLT12 offers, starts remote-signer accounts automatically, adds Blossom fallback servers, and expands Web of Trust controls for badges, communities, and relay groups. The July 29 [1.13.1 follow-up](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.1) adds a [CORD-02 dissolution seal](https://github.com/vitorpamplona/amethyst/pull/3767), kind `9008` [group and channel deletion](https://github.com/vitorpamplona/amethyst/pull/3779), [NIP-29 host-relay authentication](https://github.com/vitorpamplona/amethyst/pull/3788), and authenticated [BUD-01 retries](https://github.com/vitorpamplona/amethyst/pull/3789) for gated Blossom downloads.

### Code Call 0.2.66 keeps several remote work sessions moving from a phone

[Code Call 0.2.66](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.66), an Android remote for computer-side coding sessions, can ask a routed worker for a concise catch-up from the latest phone message. It keeps multiple sessions independent, accepts replies only from the expected sender, and keeps its inbox connected to each configured worker relay for background delivery. Encrypted [NIP-17 (Private Direct Messages)](/en/topics/nip-17/) keeps requests and replies private, while encrypted [Blossom](/en/topics/blossom/) attachments can arrive with their original file type intact. These releases let the phone maintain and catch up with multiple independently routed computer-side sessions.

### GitWorkshop coordinates maintainers and keeps repository sync independent

[GitWorkshop's July 27 signed release](https://primal.net/e/869e01f9a74d98f468a66f3b83865d198a82cc718c1db36324398b1b88a17c60) adds Android login through [NIP-55 (Android Signer Application)](/en/topics/nip-55/) to the browser-based [NIP-34 (`git` stuff)](/en/topics/nip-34/) forge. Its [source repository](https://github.com/DanConwayDev/gitworkshop) now coordinates lead maintainers recursively, preserves each maintainer's relay hints, and keeps repository synchronization independent from invitation acceptance. Cross-repository work-item references connect related work across repositories, while GRASP copies repository data to selected Git endpoints without coupling that transfer to invitation delivery. The developer-signed [3.1.1 update](https://primal.net/e/01d0939e9960cb82f1f7aba6f1900af2c61ce384e38352221bf9d5878116ae2d) repairs Android signer intent delivery, recursive maintainer resolution, and path-preserving repository links.

### Mosaico 0.1.2 gives coding agents a shared Nostr coordination fabric

[Mosaico 0.1.2](https://github.com/pablof7z/mosaico/releases/tag/v0.1.2) gives coding-agent sessions in Claude Code, Codex, Goose, Hermes, OpenCode, and Grok a shared-awareness fabric over [NIP-29 (Relay-based Groups)](/en/topics/nip-29/). Sessions broadcast short status updates and can find related active work across hosts while keeping their transcripts and context separate.

Named Codex profile discovery and Goose's Top Of Mind view expose the fabric inside two more harnesses ([PR #618](https://github.com/pablof7z/mosaico/pull/618), [PR #619](https://github.com/pablof7z/mosaico/pull/619)). Hosted agents can acquire a public fabric again, and setup now requires an explicit relay choice ([PR #626](https://github.com/pablof7z/mosaico/pull/626), [PR #629](https://github.com/pablof7z/mosaico/pull/629)). Mosaico remains an awareness layer, not an agent host, orchestrator, or transcript merger.

### Nostrology maps relay-list concentration from published NIP-65 events

[Nostrology's relay observatory](https://dev.nostrolo.gy/relays) derives its dataset from each profile's latest [NIP-65 (Relay List Metadata)](/en/topics/nip-65/) kind `10002` event, following the [published specification](https://github.com/nostr-protocol/nips/blob/master/65.md). It separates read, write, and combined relay roles, charts how many relays each profile lists, and exposes the underlying counts in a sortable table. The current page contains 34,427 distinct relay URL values and groups 520,468 profiles at exactly one listed relay, compared with 150,657 at three and 60,710 at four.

The same [Nostrology dataset](https://dev.nostrolo.gy/relays) shows overlapping concentration around `relay.momostr.pink` at 298,859 profiles, `relay.damus.io` at 287,181, `nos.lol` at 279,468, and `relay.primal.net` at 225,336. Those counts measure published routing preferences, not availability: the raw table retains malformed URLs, local addresses, and unreachable endpoints, while the [NIP-65 specification](https://github.com/nostr-protocol/nips/blob/master/65.md) defines routing metadata and does not test relay health. The observatory makes adoption and data-quality problems visible without treating a listed relay as a live one.

GATE: PENDING REVIEW
