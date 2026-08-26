# Pre-publication refresh — 2026-08-26

Start: 2026-08-26 16:32 UTC (incident recovery after the 14:00 task was left scheduled)
End: 2026-08-26 16:53 UTC
PR: https://github.com/andotherstuff/nostr-compass/pull/139

## Source refresh

- Tracked GitHub/Gitea projects: `data/project_updates/updates_2026-08-18_2026-08-26.json`; 721 repositories fetched, 150 active.
- Direct Nostr/NIP discussions: `data/nostr_nip_discussions/discussions_2026-08-18_2026-08-26.json`; seven relays queried, no qualifying events.
- Nostr Recap: `data/nostr_recap/recap_2026-08-18_2026-08-26.json`; 21 unique events.
- Shakespeare apps: `data/shakespeare_apps/apps_2026-08-18_2026-08-26.json`; 61 submissions, 55 unique apps, no new in-window app.
- NIP-34: `data/nip34_repos/nip34_2026-08-18_2026-08-26.json`; 23 tracked repositories, 104 discovery candidates, 45 in-window issues.
- Zapstore: `data/zapstore_releases/zapstore_2026-08-26.json`; 1,313 self-signed releases after filtering, 622 Nostr-relevant candidates.
- Untracked apps: `data/app_discovery/discovery_2026-08-26.json`; 14 candidates.
- OpenSats/Sovereign Engineering: `data/heartbeats/heartbeat_2026-08-18_2026-08-26.json`; OpenSats and SEC feeds completed.
- Month-end history: `data/history_research/2026-08-candidates.json`; first call hit 84 source-window errors, bounded retry completed with 2,247 candidates and zero errors.
- Specification families: `data/spec_updates/spec_updates_2026-08-27.json`; first call hit the GitHub quota guard, bounded retry after its reset completed all seven families.

## Late decisions and integration

- Included Haven's merged NIP-86 administration console, notes browser, metrics dashboard, and LMDB event-count fix from primary PR evidence.
- Included Amethyst's merged nonblocking Blossom read-authorization flow and BUD-11 token correction from primary PR evidence.
- Included the newly opened NIP-32 BCP-47 `lang` namespace proposal, clearly labeled unmerged.
- Excluded late maintenance-only changes (screenshots, release-pipeline repair, version bump, login-state reset, generated release notes, C# interop, and Buzz UI/runtime refactors) for insufficient reader impact.
- Excluded Buzz paired prompt-tag framing and an open MDK refused-ingest fix because both are implementation-stage changes without a shipped user-facing transition at cutoff.
- Updated the assembled issue and synchronized `unreleased-changes.md` and `nip-updates.md`. The history source stayed synchronized after scanner corrections.

## Verification

- 80 Python `unittest` tests: PASS.
- 22 Bun tests: PASS.
- Newsletter style, paragraph-link, event-example, and complete-history continuity checks: PASS.
- Shaka: 91/100 PASS; zero cardinal sins, banned words, banned constructions, AI tells, dash violations, or hedging findings.
- `check_npubs.ts`: 329 entries, 169 valid unique pubkeys, zero errors; two legacy warnings.
- `git diff --check`: PASS.
- Production Hugo/Pagefind build: PASS after the last editorial edit.

GATE: PASS — every source family completed after bounded retries, material late findings were integrated into synchronized editorial sources, and all final checks passed.
