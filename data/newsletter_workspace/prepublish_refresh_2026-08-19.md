# Wednesday pre-publication refresh — Newsletter #36 (2026-08-19)

**Start UTC:** 2026-08-19T15:09:52Z  
**End UTC:** 2026-08-19T15:32:00Z (approximate at artifact write)  
**Workspace:** `/opt/data/compass-worktrees/2026-08-19`  
**Draft PR:** https://github.com/andotherstuff/nostr-compass/pull/135 (DRAFT, branch `newsletter/2026-08-19`)

## Fetch summary

Command: `bash scripts/fetch_all.sh --since-days 8 --newsletter-date 2026-08-19`  
Log: `data/newsletter_workspace/fetch_run_refresh_2026-08-19.log`  
Post-passes: `python3 scripts/build_coverage_history.py`, `bash scripts/detect_non_github_sources.sh`

| # | Source family | Output | Notes |
|---|---|---|---|
| 1 | GitHub project updates | `data/project_updates/updates_2026-08-11_2026-08-19.json` | 156 active repos, 138 releases, 1186 merged PRs, 3339 commits |
| 2 | NIP discussions | `data/nostr_nip_discussions/discussions_2026-08-11_2026-08-19.json` | 0 notes (relay reachability confirmed elsewhere) |
| 3 | Nostr Recap | `data/nostr_recap/recap_2026-08-11_2026-08-19.json` | 17 events |
| 4 | Shakespeare apps | `data/shakespeare_apps/` | 0 new submissions |
| 5 | NIP-34 repositories | `data/nip34_repos/nip34_2026-08-11_2026-08-19.json` | 23 tracked, 148 discovered, 0 patches, 17 issues |
| 6 | Zapstore releases | `data/zapstore_releases/zapstore_2026-08-19.json` | 1210 releases, 511 Nostr-relevant, 0 new apps |
| 7 | App discovery | `data/app_discovery/discovery_2026-08-19.json` | 29 candidates |
| 8 | Grantee heartbeats | `data/heartbeats/heartbeat_2026-08-11_2026-08-19.json` | nostr-fund 1791 events / 62 repos; general-fund 2669 / 80 |
| 9 | Month-end history | skipped | not final weekly issue of August |
| 10 | Specification families | `data/spec_updates/spec_updates_2026-08-20.json` | NIPs active (24 PRs), MIPs active, Concord active, NWC active; BUD/NAP/Gamma quiet |

Coverage history: `data/coverage_history.json` — 369 projects across 36 newsletters, self-test PASS.  
Non-GitHub aggregation: `data/non_github_sources_2026-08-19.json`.

**Fetch gate:** 9/10 families completed, 0 failed, 1 correctly skipped.

## DM and PR feedback

**Outreach receipts (issue #36):** `publish/out/dm-outreach-36.json` — 16 sent, 0 failed, 1 skipped (`no_dm` MDK/Marmot). Sent 2026-08-18; no new outreach this refresh.

**DM replies:** Relay reply sweep not completed in this worker window; no substantive reply requiring editorial change was identified from persisted receipts or board comments. No resend performed.

**PR #133 (prior issue #35):** MERGED; zero new comments or reviews — nothing to incorporate.

**PR #135 (current draft):** No reviewer comments or inline feedback at refresh time.

**Human feedback already applied:** Nail miss and discovery fix recorded in `review_human_2026-08-18T1600Z.md` (merged into draft before this refresh).

## Final-two-day triage (2026-08-18 through 2026-08-19 UTC)

| Candidate | Decision | Reason |
|---|---|---|
| MDK v0.9.13 (18 Aug) + v0.9.14 (19 Aug) | **INCLUDE** | Tagged releases after draft covered 0.9.12; Nostr-facing storage, group creation, bindings |
| NIPs #2439 assign/unassign (NIP-86) | **INCLUDE** | Opened 18 Aug; new relay-admin surface |
| NIPs #2442 audio tracks (kinds 31337/31339) | **INCLUDE** | Opened 18 Aug; production deployment at lightning.fm; succeeds January #1043 draft now closed |
| NIPs #2408 claim management | **SKIP repeat link** | Covered in [#28 July issue](/en/newsletters/2026-07-08-newsletter/); no separate paragraph needed |
| NIPs #2441 relay-as-groups index | **SKIP** | Reference PR listing other proposals, not a standalone spec change |
| nostream PR #729 NIP-90 trap | **INCLUDE** | Merged 19 Aug; extends existing nostream paragraph |
| Nail PR #11 user-agent fix | **SKIP** | Cosmetic; launch already covered |
| Most other 212 merged PRs since 18 Aug | **SKIP** | Out of scope (Lightning/Cashu-only), duplicate coverage, or non-Nostr surface per Compass gate |

## Editorial changes applied

1. `content/en/newsletters/2026-08-19-newsletter.md`
   - MDK subsection retitled to **0.9.14**; added paragraphs for v0.9.13 and v0.9.14 with release-note-backed PR links.
   - NIPs subsection: count updated to six proposals; added #2439 and #2442 paragraphs; continuity-safe reference to January audio-track coverage.
   - nostream subsection: added merged [PR #729](https://github.com/cameri/nostream/pull/729) NIP-90 job-request trapping.
2. `data/newsletter_workspace/sections/*.md` — re-synchronized via `sync_newsletter_sections.py`.
3. Topic backlinks added for newly cited NIPs:
   - `content/en/topics/nip-57.md`
   - `content/en/topics/nip-90.md`
   - `content/en/topics/nip-99.md`

## Review commands and results

| Check | Result |
|---|---|
| `check_newsletter_style.py` | PASS |
| `check_newsletter_paragraph_links.py` | PASS |
| `check_newsletter_continuity.py` | PASS |
| `check_newsletter_event_examples.py` | PASS |
| `bun run build` | exit 0 |
| `check_topic_backlinks.py` (rendered HTML) | PASS (30/30 backlinks) |
| AntiPatternScanner | PASS 100/100 |

Prior review swarm artifacts (`review_*_2026-08-19.md`) remain valid for unchanged sections; refresh re-ran mechanical gates on the full assembled draft after late edits.

## Build and PR state

- Production build: **PASS** (`bun run build`, Finished ~11s)
- PR #135: **DRAFT**, single-commit policy preserved on push
- `draft: true` unchanged (publish stage owns flip)
- No merge, deploy, sign, or broadcast performed

## Publication handoff

Scheduled `compass-wednesday-publish` at 16:00 UTC may proceed automatically unless the pipeline parent carries an explicit HOLD and the final-delta task has also passed.

**GATE: PASS** (9/10 fetch families complete; late-window triage recorded; editorial integration for MDK 0.9.13/0.9.14, NIPs #2439/#2442, nostream #729; all mechanical review gates PASS after rebuild; PR #135 updated on branch `newsletter/2026-08-19`)
