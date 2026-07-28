# Human editorial overrides — 2026-07-29

## Mandatory include: Mosaico

User request: Track `https://github.com/pablof7z/mosaico` and include it in the current unpublished newsletter.

- Placement: Lead stories in Nostr Compass #33, not the next-week link queue.
- Tracking: Add Mosaico to `data/projects.yml` under `devtools`.
- Topic linkage: Link NIP-29 on first mention and add Mosaico to the NIP-29 topic page.
- Persistence: Preserve the item through any Stage 5 regeneration, Stage 6 review, and Stage 7 assembly.

### Verified primary-source facts

- Repository: https://github.com/pablof7z/mosaico
- Release: Mosaico v0.1.2, published July 22, 2026: https://github.com/pablof7z/mosaico/releases/tag/v0.1.2
- Product boundary from README: shared-awareness fabric for coding-agent sessions; not an orchestrator, agent host, or transcript/context merger.
- Supported harnesses: Claude Code, Codex, Goose, Hermes, OpenCode, and Grok.
- Release changes: named Codex profile discovery (PR #618), Goose Top Of Mind fabric context (PR #619), public fabric acquisition for hosted agents (PR #626), and explicit relay selection during setup (PR #629).
- Current implementation uses NIP-29 groups and NMP-backed Nostr relay I/O; the project also documents future fabric-provider seams separately.

### Approved draft copy

### Mosaico 0.1.2 gives coding agents a shared Nostr coordination fabric

[Mosaico 0.1.2](https://github.com/pablof7z/mosaico/releases/tag/v0.1.2) gives coding-agent sessions in Claude Code, Codex, Goose, Hermes, OpenCode, and Grok a shared-awareness fabric over [NIP-29 (Relay-based Groups)](/en/topics/nip-29/). Sessions broadcast short status updates and can find related active work across hosts while keeping their transcripts and context separate.

Named Codex profile discovery and Goose's Top Of Mind view expose the fabric inside two more harnesses ([PR #618](https://github.com/pablof7z/mosaico/pull/618), [PR #619](https://github.com/pablof7z/mosaico/pull/619)). Hosted agents can acquire a public fabric again, and setup now requires an explicit relay choice ([PR #626](https://github.com/pablof7z/mosaico/pull/626), [PR #629](https://github.com/pablof7z/mosaico/pull/629)). Mosaico remains an awareness layer, not an agent host, orchestrator, or transcript merger.

## Mandatory editorial corrections from human review

- Remove and permanently ban the constructions `join Shipping This Week with` and `developer-signed release expands the browser`.
- Compare every selected story with all prior newsletters, then read the latest three issues in full. Reused source URLs and repeated substance are blocking duplicates outside the explicit month-end retrospective.
- Cover the verified Amethyst 1.13.0 release from July 28 as shipped work, not as three separate in-development PR summaries. Avoid repeating the pre-release details covered in issue #32.
- Every prose paragraph must carry a repository, release, PR, commit, or other primary-source link; internal topic links alone are insufficient.
- Expand `Protocol and Spec Work` so every issue explicitly reports NIPs, BUDs, NAPs, Marmot/MIPs, Gamma Markets, and other tracked specification repositories such as Concord/CORD and NWC, including repository-linked quiet status when applicable.
- Because July 29 is the last Wednesday of the month, the final section is history, not a NIP Deep Dive. Title it `Six Years of Nostr Julys`, matching the earlier month-end naming pattern.
- Rerun July history research from primary repository history. Write at least two substantive, source-linked paragraphs for each year from 2021 through 2026 and match the denser narrative style of the January through June retrospectives.
- Keep the draft unpublished at the human-review gate; do not translate, prepare podcast assets, commit, push, or publish.
