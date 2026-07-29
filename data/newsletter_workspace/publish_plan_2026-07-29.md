# Publish plan — 2026-07-29

Primary PR: #117 (merged early at 2026-07-29T12:45:34Z)
Publication-day update PR: #118 (https://github.com/andotherstuff/nostr-compass/pull/118)
Draft path: `content/en/newsletters/2026-07-29-newsletter.md`
Bunker config: `~/.config/compass-publish/bunker.json`
Compass author: `npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923`
Clock authorization: automatic publication at 16:00 UTC, provided the final refresh and all gates pass with no hold.

## Pre-publish verification

- PR #118 is open, draft, clean, mergeable, and its build check passes at commit `ca2b6f5` before the final source-evidence update.
- The 15:17 UTC final source run completed all eight source families with 0 failures and 0 stale families.
- No post-cutoff release, commit, merged PR, Nostr event, app release, heartbeat, or specification change requires a newsletter edit. NIP PR #2424 received a use-case discussion comment at 15:04 UTC; its proposal and event contract did not change. NIP PR #2419 received a concept-ACK review at 13:24 UTC; its sole specification commit remains outside the issue window.
- Review handoff and all five evidence-bearing reviewer artifacts pass.
- GitHub authentication and both mode-600 bunker credential files are present.
- `bun scripts/publish.ts --force` parses the issue and generates the canonical payload.
- Publish preview resolves 28 project identities.
- `pakstr` and `swift-nostr` remain unresolved after repository, maintainer profile, NIP-05, relay-search, and project-site checks. No identity was guessed. Their inline npub injection is omitted using the documented `--force` path; the projects and source links remain in the article.
- Targeted outreach dry-run receipts cover seven deduplicated recipients added during the publication-day refresh. The publication worker must send only these targeted plans after the 16:00 gate and must not resend the full issue campaign.
- No merge of PR #118, Amber invocation, signing, broadcast, translation, or podcast work occurred during refresh.

## Final audit hold

The user requested another complete factual and prose validation at 15:49 UTC. Publication automation was paused before 16:00. The full audit found and corrected release attribution, current-release coverage, open-versus-merged status, one live data count, two historical dates, proposal tense, source precision, prose clarity, and two final heading/body attribution mismatches. Both post-edit reviewers now pass, along with all local mechanical and production-build gates.

## Publication plan after the hold clears

1. Confirm `prepublish_refresh_2026-07-29.md` ends in evidence-bearing `GATE: PASS`, PR #118 remains clean with successful CI, and no hold exists.
2. Mark PR #118 ready and squash-merge it into `main`.
3. Wait for the production GitHub Pages deployment and verify the live issue includes the update commit.
4. Execute the two reviewed targeted outreach plans only, with `no_dm` exclusions and recipient de-duplication preserved.
5. Generate canonical long-form content with absolute links and 28 verified npub injections; omit only the two unresolved identities via `--force`.
6. Sign and broadcast the kind `30023` article through the Amber bunker.
7. Sign and broadcast the kind `1` opening digest with the article `naddr`.
8. Recover both event IDs from independent configured relays and record the publish log.
9. Complete parent task `t_ed0f1dbf` only after deployment and relay proof, promoting translation and podcast prep.

GATE: PASS (full audit and local gates passed at 2026-07-29T16:20:40Z; publication cron remains paused until the evidence commit is pushed and PR #118 CI passes)
