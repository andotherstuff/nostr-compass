## Tagged Releases

### Nail 0.2.0 restores Nostr-to-email subscriptions

[Nail v0.2.0](https://github.com/formstr-hq/nail/releases/tag/v0.2.0), a service that delivers Nostr messages through email workflows, adds self-healing gift-wrap subscriptions. The change is aimed at restoring Nostr-to-email delivery after subscription failures instead of leaving the bridge silently stalled.

### Nostr Mail Client 0.15.0 broadens account and relay control

[Nostr Mail Client v0.15.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.15.0) adds one-tap account switching, per-account notifications, web push, and recovery of a missing relay list from a relay, Nostr address, or `nprofile`. It also republishes profiles and relay lists to indexing relays, reconnects when network access returns, and distinguishes a device outage from unreachable mail relays. Those changes tighten account recovery and delivery across desktop, web, and Android clients.

### Linky 26.9.17 keeps recovery seeds off its server

[Linky v26.9.17](https://github.com/linky-fit/linky/releases/tag/v26.9.17), a contacts, private Nostr messaging, and Lightning/Cashu payments application, fixes a path that sent recovery seeds to Linky's server when users saved them through a password manager. The release also hardens payment-file URL handling and disables Android application backups, reducing the places where wallet and identity recovery material can escape the device.

### Calendar by Form* 2.4.0 adds Mailstr guest invitations

[Calendar by Form* v2.4.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.4.0), a Nostr calendar client, adds Mailstr guest invitations and mobile calendar fixes. The invitation path lets organizers include participants through mail-oriented coordination without requiring an existing calendar account.

### Hessible 0.1.2 speeds encrypted contact and photo sync

[Hessible 0.1.2](https://github.com/circumspace/hessible), a privacy-focused Android contacts application that stores encrypted contact data on Nostr relays, reduces synchronization overhead and mirrors encrypted contact photos across Blossom servers. The release also makes the application package smaller, while its own release guidance continues to caution users to back up keys and account for varying relay retention.

### Boris 0.12.5 bounds extraction and strengthens offline reading

[Boris v0.12.5](https://github.com/dergigi/boris/releases/tag/v0.12.5), a reading-list client built around Nostr bookmarks, follows v0.12.4 with bounded content extraction, offline caching, relay-query changes, unsafe-HTML handling, and a fix for nearly invisible text under the Paper White theme. These changes affect both content safety and the reliability of reading saved material without a live network path.

### Amethyst 1.15.2 refines media and root-scope replies

[Amethyst v1.15.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.15.2), an Android Nostr client, closes a three-release sequence with media fixes, clearer Health Connect permission handling, source-name caching, and dedicated engagement filters for NIP-22 root-scope replies. The release also includes translation and package-metadata updates.

### LibreNostr 0.5.17 routes feeds through author write relays

[LibreNostr 0.5.17](https://primal.net/e/c118efbe649823a3258a6e7663f4d8b52195adbde0481019183792eb5274afd4), a relay-first Android client, now directs feed queries to the NIP-65 write relays of followed authors and defers interaction-count queries until notes enter view. Earlier work in the same release sequence limits concurrent relay queries and closes each relay subscription as soon as that relay answers, reducing self-inflicted request rejection during refreshes.

### Voca 1.2.0 improves speech cancellation and recovery

[Voca 1.2.0](https://njump.me/nevent1qqsfcc5zel49t5zt96ufndumrzc2vzhrk7e2rnwq579gcs8yd9cn4pcflqxt3), an offline-oriented Android text-to-speech reader that can fetch and verify Nostr content, adds distinct cancellation and rendering behavior plus recovery for slow or unreliable speech engines after the 1.0 launch covered in issue #38. It also adds opt-in diagnostics sent with a fresh one-time Nostr key through a NIP-17 private message, with large reports encrypted locally before upload.

### Postr 1.1.1 adds dictation and publication recovery

[Postr 1.1.1](https://njump.me/nevent1qqszw3dsskfz3u7pqxn4r5ytslrj0e3u26et90rpy9997vtfw3qkr6g9g0f03), a focused Android kind `1` composer, adds dictation and caret-aware mention handling after the launch covered in issue #37. The preceding 1.1.0 release also improves publication recovery by retrying the same signed event after ambiguous outcomes, preventing recovery from creating a duplicate note.

### earthly 0.1.10 repairs map sanitization and authoring

[earthly v0.1.10](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.10), a collaborative Nostr map editor, materially changes map and story authoring while fixing a critical MapLibre attribution-sanitizer flaw through a MapLibre GL JS upgrade. The release also improves WebGL 2 compatibility messaging, mobile controls, geometry editing, selection, and map-presentation controls.

### Routstrd 0.4.10 tightens Nostr request routing

[Routstrd v0.4.10](https://github.com/Routstr/routstrd/releases/tag/v0.4.10) replaces a stale stored provider list with the list returned by live discovery. The preceding v0.4.9 release added manual and scheduled client refresh controls, named npubs in the CLI, and graceful daemon restarts that wait for active requests. Together, the releases make provider selection and refresh behavior more explicit for operators of the Nostr-routed service.

### Whistle 1.9.1 instruments background recovery

[Whistle 1.9.1](https://primal.net/e/bb3aae325f707b04dffd3b0b4a2d0c48022999fef7a793be3503b4c53e37eba4), an encrypted group location-sharing application built on Nostr, MLS, and Marmot Protocol, adds device-lifecycle instrumentation for iOS background recovery. Version 1.9.0 also introduces per-group sharing pauses and per-group last-event diagnostics, making a stalled group easier to distinguish from a healthy application-wide connection.

### Amber 6.6.4 closes a Tor leak and signer recovery failures

[Amber v6.6.4](https://github.com/greenart7c3/Amber/releases/tag/v6.6.4), an Android Nostr event signer, caps a three-release sequence with a Tor leak correction and fixes around signer relays and recovery. Signer users and application developers should pay particular attention to network-path assumptions and retry behavior, since signer failures can otherwise appear as client publication failures.

### nostr-wot-extension 0.7.0 encrypts wallet cache data

[nostr-wot-extension v0.7.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.7.0), a browser extension that manages Nostr identities, signs events, and initiates Lightning payments, encrypts wallet and payment cache data and strengthens vault and account isolation. It also addresses NWC and wallet behavior, payment compatibility, request approvals, account management, backup imports, relay handling, accessibility, and local event decryption.

### Lightning.Pub 0.0.41 improves publication recovery

[Lightning.Pub v0.0.41](https://github.com/shocknet/Lightning.Pub/releases/tag/v0.0.41) adds relay URL, timing, socket-state, and DNS details to Nostr publication failures. It also retries liquidity-provider startup calls, removes abandoned callbacks, and withholds invoice routing until a successful balance response proves the provider is ready. Operators now get a clearer split between relay-connectivity failures and backend-readiness failures.

### Gittr 1.0.0 advances NIP-34 collaboration

[Gittr v1.0.0](https://github.com/arbadacarbaYK/gittr/releases/tag/v1.0.0), a client for Nostr-based Git collaboration, advances NIP-34 clone-source handling, issue and discussion state, mobile usability, and interoperability. The v1.0.0 tag follows v0.3.0 and v0.3.1 from earlier this week, giving integrators a stable version marker for the release sequence.

### GitWorkshop 4.1.0 makes NIP-34 drafts recoverable

[GitWorkshop 4.1.0](https://njump.me/nevent1qqswf45vw8y5metnu8tc2fge0lr7sy8nmuk264kryrd45wqles5kfvqqrtwl3), a Nostr-native client for NIP-34 issues, pull requests, code review, and repository browsing, adds account-scoped local drafts that survive refreshes and browser restarts. It also adds bounded recovery and explicit retry controls across Git reads, relay discovery, repository state, pull-request history, uploads, and release metadata while keeping signing and payment retries manual.

### ngit-ci 0.1.1 publishes signed CI coordination

[ngit-ci 0.1.1](https://njump.me/nevent1qqs2y0p5nxkfqsrqguth3hd4wmmel4p2te8q906ex748q35ug79e6eg9hms4s), a self-hosted coordinator for the proposed NIP-C1 Nostr CI protocol, is its first release published through Nostr. It covers signed workflow coordination, container or microVM execution, logs and artifacts, encrypted repository secrets, NIP-34 maintainer authorization, and signed publication of build results.

### pakstr 0.21.1 advances Nostr application packaging

[pakstr v0.21.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.21.1) continues a five-release sequence for Nostr application packaging and app-shell behavior. NostrAppShell references point to this same pakstr release series, so the package and alias describe one shipped change.

### @elisym/cli 0.30.0 coordinates agent and delegation packages

[@elisym/cli 0.30.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/cli%400.30.0) concludes a coordinated CLI, SDK, and MCP release for Nostr-oriented agent delegation. Delegated jobs now wait for completion instead of sleeping for a fixed interval, and the application avoids paying the same delegation capability once per job. Teams using more than one package should keep CLI 0.30.0, SDK 0.36.0, and MCP 0.26.0 on the matched release line.

### Hashtree 0.2.150 advances hash-tree synchronization

[Hashtree v0.2.150](https://github.com/mmalmi/hashtree/releases/tag/v0.2.150) closes a six-release sequence with Android-safe locking for the embedded social graph. Earlier releases in the sequence keep Nostr subscriptions open briefly after an empty EOSE so delayed signed roots can arrive, select the newest valid root for the exact author and tree, and recover retained FIPS routes after transit outages. The result is more predictable mutable-root discovery and synchronization across relays, embedded clients, and intermittent network paths.

### nostr-relay 0.0.266 improves shared-database operation

[nostr-relay v0.0.266](https://github.com/mattn/nostr-relay/releases/tag/v0.0.266), a Nostr relay built on the relayer framework, advances shared-database and Redis behavior across six releases. This work is especially relevant to operators running more than one relay process against common persistence or notification infrastructure.

### fips-tcp 0.2.2 implements FIPS over TCP

[fips-tcp v0.2.2](https://github.com/mmalmi/fips-tcp/releases/tag/fips-tcp-v0.2.2) repairs missing segments after a timed-out flight as acknowledgments advance. Small writes lost during a transit outage recover together instead of waiting through a growing timeout for every segment, while the Rust and TypeScript implementations preserve identical wire bytes, retry bounds, receive-window checks, sequence wrapping, and RTT sampling.

writer_model: preferred=gemini-3.1-pro, actual=openai-codex/gpt-5.6-sol, receipt=data/newsletter_workspace/writer_receipt_2026-09-16.json

GATE: PENDING REVIEW
