# Stage 4 selection review — Newsletter #36 (2026-08-19)

Scored against the 0-10 rubric (Nostr Relevance, User Impact, Ecosystem Breadth, Novelty), minimum 5
to include. Redundancy checked against `data/coverage_history.json` (362 projects, 35 issues) plus a
full read of #34 (2026-08-05), #35 (2026-08-12), and #33 (2026-07-29) section structures.

## Edition type

Month-end detection: `2026-08-19 + 7 days = 2026-08-26`, same calendar month. This is a **regular
edition with two NIP Deep Dives**. `Six Years of Nostr Augusts` belongs to #37.

## Deep dive rotation

Rotation source of truth: `grep -E "^## NIP Deep Dive" content/en/newsletters/*.md`. Already used
one-shot: 01, 02, 04, 07, 09, 10, 11, 13, 17, 19, 29, 34, 39, 40, 42, 43, 44, 45, 46, 47, 49, 50, 51,
52, 53, 54, 55, 56, 57, 58*, 59, 5A, 60, 62, 65, 66, 70, 72, 84, 85, 86, 89, 90, 94, 96, 99.

\* NIP-58 appears in prose in #7, #12, and #31 but has never been a Deep Dive; the rotation is on
Deep Dive headings, so it remains eligible.

Selected: **NIP-58 (Badges)** and **NIP-22 (Comments)**.

Both are merged specifications with topic pages already in the repository
(`content/en/topics/nip-58.md`, `content/en/topics/nip-22.md`). Implementation evidence, three
distinct applications each, all verifiable from this window:

- NIP-58 — Divine Mobile 1.0.20 (in-app badge minting and award), Nostter PR #2281 (profile badges),
  Amethyst (real kind 8 award recovered from relays carrying `["client","Amethyst"]`).
- NIP-22 — Divine (real kind 1111 comment recovered carrying
  `["client","Divine","31990:d95aa8fc…:divine-mobile","wss://relay.divine.video"]`), Amethyst
  (recovered kind 1111 with `["client","Amethyst"]`), nostrord PR #274 (thread posts read as forum
  posts), and the proposed NIP-9A patch format that builds directly on kind 1111.

Both dives use a real relay-recovered event, not a constructed example.

## Section allocation

### Top Stories (6)

1. **Amber 6.5.0 → 6.5.2** — score 9. A coordinated set of advisory fixes across the NIP-46 and NIP-55
   signing path plus two follow-up patches. Highest user impact of the week: everything that signs
   through Amber inherits it.
2. **Cambium 0.3.5 → 0.4.3** — score 9. Six releases adding NIP-55 website signing and repairing NIP-46
   pairing and AUTH-burst behavior against a hardware signer. Link-queue item with verified activity.
3. **Citrine 3.1.0** — score 8. A phone-hosted relay picking up NIP-29 groups, the NIP-86 management
   API, and nsite hosting in one release.
4. **Vector 0.4.2 / 0.4.3** — score 8. Concord moderation, pinned messages, cross-device list sync, and
   a cross-client review pass with Armada.
5. **Sonar alpha 13.1 → 13.3** — score 7. NIP-C7 replies land in a mesh-plus-Nostr messenger, with two
   crash follow-ups the same week.
6. **Nostria 4.1.69 → 4.1.71** — score 7. Podcast publishing over Nostr plus relay-side COUNT support.

### Tagged Releases (9)

MDK 0.9.12; Divine Mobile 1.0.20; ClipRelay 0.1.4 and 0.2.0; Bark 1.3.8/1.3.9; Bray 3.0.0 with
Toll Booth 6.0.0→6.1.2; NoorNote 1.3.4/1.3.5; the Mostro stack; NYM 3.73.520→524; Morganite 0.0.4.

Consolidated deliberately: Bray and Toll Booth share one subsection because both adopt nwc-kit in the
same 24 hours, and splitting them would separate a single story. The Mostro daemon, core library, and
mobile app share one subsection for the same reason — one envelope migration crossing three repos.

### Newly Discovered (3)

Nail, nwc-kit, and Glow. Nail was added on 2026-08-18 through the mid-week intake path after the
owner reported it missing; the discovery root cause and its fix are recorded in
`review_human_2026-08-18T1600Z.md`. Glow carries no in-window Nostr change and is written as an introduction of its
standing relay-backed wallet-label surface, per the Stage 1 resolution.

### In Development (7)

Amethyst relay auth; nostrord device pairing; nostream relay monitoring; rust-nostr; NDK
post-quantum DMs; Nostter; Zap Cooking. All are merged, unreleased PRs. No draft or open PR appears here.

### Protocol and Spec Work

NIPs #2436, #2437, #2438; Marmot MIP #416; Concord #18 merged plus #22 and #23 opened. BUDs, NAPs,
and Gamma Markets are `quiet` in `spec_updates_2026-08-19.json` and are therefore absent from the
prose rather than present as quiet-status filler.

## Repeated-project justification (mandatory)

Every project below appeared in an earlier issue. Each entry records the distinct primary source and
the distinct user-facing or protocol-facing change; none reuses a release, PR, commit, or event URL
already cited in the archive.

| Project | Last covered | Distinct source this week | Distinct change |
|---|---|---|---|
| Amber | #35, v6.4.0 | releases v6.5.0/v6.5.1/v6.5.2 | advisory fixes to relay-auth scoping, NIP-46 replay windows, secret storage at rest |
| Cambium | #31, project note | releases v0.3.5 → v0.4.3 | NIP-55 website signing and NIP-46 pairing/AUTH admission |
| Citrine | #33 | release v3.1.0 | NIP-29 groups, NIP-86 API, nsite hosting |
| Vector | #31, v0.4.0/v0.4.1 | releases v0.4.2/v0.4.3 | Concord moderation queueing, pinned messages, synced lists |
| Sonar | #22 | releases v0.1-alpha.13.1 → 13.3 | NIP-C7 replies |
| Nostria | #35, v4.1.67 | releases v4.1.69 → v4.1.71 | NIP-45 COUNT and podcast publishing |
| MDK | #35, v0.9.11 | release v0.9.12 | fork-anchor fail-closed, atomic leave proposals, cross-adapter convergence |
| Divine Mobile | #35, 1.0.19 | release 1.0.20 | in-app NIP-58 badge minting |
| ClipRelay | #35, v0.1.3 | releases v0.1.4 and v0.2.0 | sensitive-clipboard retention, `nostrconnect://` QR login |
| NoorNote | #35, v1.3.2 | releases v1.3.4/v1.3.5 | Armada/Concord community invites |
| Mostro | #35, v0.18.1 and core v0.14.2 | v0.18.2/v0.18.4, core v0.14.3 → v0.14.5, mobile v1.3.1/v1.3.2 | rumor-id serialization inside the gift wrap, dispute-chat migration to kind 14 |
| NYM | #29 | releases v3.73.520 → v3.73.524 | encrypted group chat refinements and encrypted SQLite |
| Morganite | #26 | release v0.0.4 | single-pass blob hash verification |
| Amethyst | #35, Concord invites | PRs #3899/#3905/#3906/#3931/#3937 | NIP-42 auth decision flow |
| rust-nostr | #34, hardening batch | PRs #1444/#1445/#1450 | gift wrap rumor ids, protected-event reposts, NIP-47 tolerance |
| Concord | #35, PR #18 open | PR #18 merged 2026-08-15, PRs #22/#23 opened | status transition from proposed to merged, then two follow-ups |

Concord PR #18 is the only reused source URL in the issue. It is retained because the paragraph states
the earlier coverage and the merge transition explicitly, which is the one permitted exception.

## Excluded, with reasons

CDK, Zeus, Alby Hub, Alby Go, Brezn, Astraea, nostr-codex-phone, mesh-llm, Jumble, Buzz desktop,
fips-ts/hashtree, and the whole Zapstore new-app bucket are excluded for the reasons recorded in
`triage_2026-08-19.md`. Chama, Earthly, NostrAppShell, and Obelisk stay MAYBE and are not written.

## Validation rounds

- **Round 0 (dedup)** — applied the 2026-08-12T15:30Z cutoff across the release set and dropped 18
  already-covered items. Recorded in Triage.
- **Round 1 (completeness)** — walked both the release list and the ≥5-merged-PR list (33 projects) and
  enumerated NIP PRs directly through `gh pr list -R nostr-protocol/nips`, which found zero merges and
  eleven touched proposals in the window. The relay-side NIP discussion scrape returned zero, so the
  `gh` enumeration is the load-bearing source for spec activity this week.
- **Round 2 (topic pages + month-end)** — `nip-22.md`, `nip-27.md`, `nip-58.md`, `nip-98.md` all exist.
  The two dive pages need `Mentioned in` entries for #36. Month-end check re-run: deep dives, not history.

GATE: PASS (6 Top Stories, 9 Tagged Releases, 3 Newly Discovered, 7 In Development, 3 spec families with in-window change, 2 rotation-eligible deep dives with three verified implementations each; every repeated project carries a distinct source and a distinct change)
