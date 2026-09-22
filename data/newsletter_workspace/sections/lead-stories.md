## Top Stories

### fips2go 0.6.0 gives mesh nodes readable names

[fips2go](https://github.com/fr34aky/fips2go) is an Android client that lets selected applications reach peers and services over the FIPS encrypted mesh. [Version 0.6.0](https://github.com/fr34aky/fips2go/releases/tag/v0.6.0) adds device-local mesh names, so a user can map a long node key to a name such as `home` and connect through `home.fips` anywhere a hostname is accepted.

The [mesh-name resolver](https://github.com/fr34aky/fips2go/releases/tag/v0.6.0) applies additions, removals, and changed mappings to the next lookup without reconnecting the mesh. Names remain local to the phone and outside identity backups, which makes the feature an address book instead of a global naming system; the release also documents that only its ARM64 build received physical-device verification.

### fips-initramfs brings remote LUKS unlock into early boot

[fips-initramfs](https://github.com/jmcorgan/fips-initramfs) is a Linux initramfs package that starts a FIPS mesh node before normal boot so an operator can remotely unlock a LUKS-encrypted root through its npub-addressed node. The user-submitted [0.1.0 release](https://github.com/jmcorgan/fips-initramfs/releases/tag/v0.1.0), published September 6, packages the mesh client, SSH access, and unlock scripts for systems that need unattended or remote encrypted-root startup.

The [first release](https://github.com/jmcorgan/fips-initramfs/releases/tag/v0.1.0) documents the security tradeoffs instead of hiding them: the initramfs contains the node key, the passphrase crosses SSH over FIPS, and local console unlock remains available. This is a catch-up item from a prior user submission rather than a release from the current collection window.

### Grain 0.8.0-rc4 turns relay health into an operator dashboard

[Grain](https://github.com/0ceanSlim/grain) is a self-hosted Nostr relay with an integrated reference client and administration interface. [Version 0.8.0-rc4](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc4) adds a live vitals panel for event volume, connections, uptime, storage, memory, and writer health, plus per-kind storage charts and reorganized access, policy, and retention controls.

The [release candidate](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc4) also makes its client escalate missing-event lookups from the local relay to author outbox relays, embedded relay hints, and NIP-50 search. NIP-50 standardizes relay-side search filters, while NIP-01 defines the core event and subscription rules that include identifier and author prefix matching. Grain adds those prefix matches and configurable full-text kinds to its database, while the release-candidate label makes clear that operators should test the new dashboard and database behavior before treating it as a stable line.

### Marmot Protocol 0.10.4 makes local sends durable

[Marmot Protocol's MDK](https://github.com/marmot-protocol/mdk) is an SDK for MLS-encrypted group messaging whose transport and discovery run over Nostr. [Version 0.10.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.4) persists local sends before network completion, lowers draft and pending-message latency, prevents repeated automatic attachment downloads, and exposes retention state in chat-list previews.

The [same release](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.4) adds group creation to agent-control integrations and opt-in reaction consent for approval prompts. It also repairs a halted-wrapper edge case and bounds retry backoff during epoch backfill, continuing the post-0.10.0 reliability work without changing the requirement that generated bindings and native libraries move together.

### MintRadar makes Cashu mints easier to compare

[MintRadar](https://mintradar.org) is a privacy-focused Cashu dashboard that uses Nostr to discover mints and bind community reviews to signed identities. Its [current source](https://github.com/hroomnik007/MintRadar) adds persistent NIP-87 mint announcements, same-operator detection from NUT-06 pubkeys, shareable comparison URLs, and Nostr `naddr` deep links.

NIP-87 standardizes discovery and review events for Cashu mints, while NUT-06 defines the mint information document that exposes a mint's public keys and supported capabilities. A [signed user-submitted update](https://njump.to/nevent1qqs9hwth0rgsprqaml9xuuve2s47x08w2ltjujgwwr4zyqw0qjptecqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyqt40x2js6hcc27delgn5vqwn3qtcjn8uas3rrzmxe2hxsrvdvmmcqcyqqqqqqgyqg6ap) brought MintRadar back into the intake after it was missed in an earlier pass; the project has since accumulated substantial current-window work around those comparison and discovery paths.

### Nostr WoT Oracle 0.3.1 makes trust queries restart-safe

[Nostr WoT Oracle](https://github.com/nostr-wot/nostr-wot-oracle) is a server that ingests public follow and mute events and answers bounded web-of-trust path queries. [Versions 0.3.0 and 0.3.1](https://github.com/nostr-wot/nostr-wot-oracle/releases/tag/v0.3.1) add independently persisted public mute evidence, readiness and ingestion status, revision-bound caches, deterministic replaceable-event selection, and rollback behavior that prevents unpersisted graph changes from becoming queryable.

The [0.3.1 performance pass](https://github.com/nostr-wot/nostr-wot-oracle/releases/tag/v0.3.1) restores graph edges directly into numeric adjacency lists, coalesces superseded follow and mute events before publication, and batches distance-cache misses. These changes matter to clients that need explainable follow distance or mute evidence without silently serving a relationship graph from an older revision.

### Nostr WoT SDK 1.0.2 compresses browser graph storage

[Nostr WoT SDK](https://github.com/nostr-wot/nostr-wot-sdk) is a JavaScript toolkit for crawling, storing, and querying Nostr follow graphs in applications. [Version 1.0.2](https://github.com/nostr-wot/nostr-wot-sdk/releases/tag/nostr-wot-sdk%401.0.2) adopts a graph engine that batches up to 100 authors per relay request, stores edges with compact delta encoding, reuses compatible traversals, and exposes batch distance queries.

The [graph 0.3.0 storage migration](https://github.com/nostr-wot/nostr-wot-sdk/releases/tag/%40nostr-wot/graph%400.3.0) upgrades IndexedDB namespaces to schema 2 and cannot be reopened by older SDK versions. Applications that need rollback should use a separate namespace or clear the upgraded graph instead of assuming the earlier client can read it.

### napplet.soy publishes small sandboxed Nostr programs

[napplet.soy](https://napplet.soy) is a web playground and creator toolkit for building, publishing, playing, inspecting, and remixing small sandboxed Nostr programs called napplets. NIP-34 defines signed Nostr events for Git repository discovery and collaboration. The [soyLI 0.18.2 release](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.18.2) follows the project's September launch with signed listings, Blossom-hosted assets, Git and NIP-34 source references, and relay-discovered manifests.

The [project source](https://github.com/zeSchlausKwab/napplet-soy) keeps network and storage access behind declared capabilities instead of giving each napplet unrestricted browser authority. Its project identity remains unresolved because the canonical site and repository do not bind a project or maintainer npub, so no identity claim is attached here.

### RelayKit installs a self-hosted Nostr stack

[RelayKit](https://relayk.it) is a one-command installer for a self-hosted Nostr stack that can include relays, Blossom media, nsites, Git services, and notifications. The current project is materially broader than the browser relay-discovery client covered in April, and its [current source repository](https://github.com/samthomson/relaykit) documents the new operator-focused deployment surface.

The [installation site](https://relayk.it) presents the services as one coordinated stack instead of requiring operators to assemble each component independently. This coverage therefore treats RelayKit as a changed project direction, not as its first appearance.

### Threshold Sessions turns coding transcripts into private training data

[Threshold Sessions](https://gitworkshop.dev/npub17m2ual3pdjvhd8yc6a3m8snzjsgnmtl26hwen48ne937qgyjyshs2zgvse/relay.ngit.dev/threshold) is a command-line tool that converts AI coding sessions into normalized, redacted, and encrypted training-data epochs. Its repository supports Codex, Claude Code, Cursor, OpenCode, and pi transcripts, stores encrypted artifacts on Blossom, and publishes signed references through Nostr.

Recent [Threshold Sessions source history](https://relay.ngit.dev/npub17m2ual3pdjvhd8yc6a3m8snzjsgnmtl26hwen48ne937qgyjyshs2zgvse/threshold.git) adds timestamp randomization, provenance, extractors, and a ledger for produced epochs. The design lets a contributor preserve auditability and later data use without publishing the readable session transcript to relays.

writer_model: preferred=gemini-3.1-pro, actual=openai-codex/gpt-5.6-sol, receipt=data/newsletter_workspace/writer_receipt_2026-09-16.json

GATE: PENDING REVIEW
