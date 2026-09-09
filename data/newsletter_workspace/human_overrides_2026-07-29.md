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

## Mandatory include: Nostrology relay observatory

User request: Research `https://dev.nostrolo.gy/relays` and add it to the current unpublished newsletter.

- Placement: Top Stories in Nostr Compass #33, not the next-week link queue.
- Topic linkage: Link NIP-65 on first mention, add the observatory to the NIP-65 topic page, and add the Newsletter #33 backlink.
- Persistence: Preserve the item through any Stage 5 regeneration, Stage 6 review, and Stage 7 assembly.

### Verified primary-source facts

- The page identifies itself as a Nostr ecosystem observatory for NIP-65 relay-list adoption.
- It derives the dataset from each profile's latest kind `10002` event and separates read, write, read-only, write-only, and combined roles.
- The fetched page contained 34,427 distinct relay URL values.
- Its distribution data grouped 520,468 profiles at exactly one listed relay, 150,657 at three, and 60,710 at four.
- The four largest overlapping counts were `relay.momostr.pink` at 298,859 profiles, `relay.damus.io` at 287,181, `nos.lol` at 279,468, and `relay.primal.net` at 225,336.
- The raw values include malformed URLs, local addresses, and unreachable endpoints, so the page measures published preferences and does not provide NIP-66-style liveness data.
- Both `https://dev.nostrolo.gy/relays` and the NIP-65 specification returned HTTP 200 during verification.
- Resolve both new-project and maintainer identities before pre-publication outreach. For Nostrology, the project source attribution, Sovereign Engineering interview, relay-backed kind `0` profile, and `_@whisperhash.com` NIP-05 all resolve to WhisperHash's `npub1t6m495kynns7xjmgz8yt6krrw4r8tac0mvr3f25f9r35ke72ap3su4qycp`; no distinct project npub was found, so the shared pubkey must receive one deduplicated DM.
- **Superseded 2026-09-01:** Whenever a genuinely new project enters an unpublished draft, update the review PR and send only the standard GitHub-review DM to the verified project and maintainer identities after a targeted dry run. Honor `no_dm`, never guess an identity, and verify event IDs plus relay acceptances. Podcast outreach is separate, post-publication, and disabled pending approval of the new setup and message.

## Mandatory publication-day refresh additions

Primary-source verification after the first refresh pass found two in-window releases that must survive any resumed Stage 5 or Stage 6 run:

- [Bray 2.3.0](https://github.com/forgesworn/bray/releases/tag/v2.3.0), with merged [PR #75](https://github.com/forgesworn/bray/pull/75), [PR #76](https://github.com/forgesworn/bray/pull/76), and [PR #77](https://github.com/forgesworn/bray/pull/77). The bounded story is arbitrary-event NIP-59 wrapping through NIP-46, NIP-42 test-relay authentication, NIP-77 request ergonomics, and an authorized in-memory Blossom test endpoint. The release is distinct from Newsletter #31's Bray 1.34.0 coverage. Bray's repository links `forgesworn.dev`; its primary NIP-05 document maps `_` and `darren` to the same verified key, so the project and maintainer aliases share one de-duplicated outreach recipient.
- [Buzz Desktop 0.5.0](https://github.com/block/buzz/releases/tag/v0.5.0), with use-limited invites, structured relay search filters, native join-policy retrieval, persona-rename identity republishing, and a NIP-44 security dependency update. Frame it as continuity from Newsletter #32's Armada/Buzz coverage. `Buzz` and `block` share the existing verified project key and must produce one de-duplicated targeted outreach recipient.

Also preserve the source-attribution corrections from the publication-day audit: Amethyst 1.13.0 owns the broad app, browser, Git, payment, and identity feature set; Amethyst 1.13.1 owns only its July 29 follow-up changes. The intro remains a feature digest with no version, PR, event-kind, or incidental NIP numbers.
