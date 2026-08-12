# Compass pre-publication refresh — 2026-08-12

## Run

- Start: 2026-08-12 13:03:37 UTC
- End: 2026-08-12 13:40 UTC
- Target: Newsletter #35, `2026-08-12`
- Worktree: `/opt/data/compass-worktrees/2026-08-12`
- Draft PR: https://github.com/andotherstuff/nostr-compass/pull/133 (`OPEN`, `DRAFT`, base `main`)
- Clock gate: Wednesday refresh completed before 16:00 UTC. No merge, deployment, frontmatter publication flip, signing, or relay broadcast was performed.

## Preflight and feedback

- `gh auth status`: authenticated as `Datawav` with repository access.
- `hugo version`: `v0.123.7+extended`.
- `bun --version`: `1.3.14`; `bunx --version`: `1.3.14`; `nak --version`: `v0.20.2`.
- Git refs were fetched without reset or destructive cleanup.
- PR #133 issue comments: 0; inline review comments: 0; reviews: 0. There was no GitHub feedback to accept or reject.
- Persisted outreach receipts were inspected at `/opt/data/compass/publish/out/dm-outreach-35.json` and `/opt/data/compass/publish/out/dm-outreach-35-safebox-acorn.json`: 14 unique eligible recipients have successful delivery event IDs and relay acceptance; two configured `no_dm` exclusions remain skipped.
- Configured durable relays were queried after the first receipt timestamp for inbound kind 1059 gift wraps addressed to Compass and kind 4 messages authored by the 14 recipients. Result: 0 NIP-17 wrappers and 0 NIP-04 messages. Incomplete lookup never triggered a resend; no outreach was resent.

## Source-family refresh

Command: `bash scripts/fetch_all.sh --since-days 8 --newsletter-date 2026-08-12`
Log: `logs/prepublish_refresh_2026-08-12/fetch_all.log`
Result: 9 completed, 0 failed, 1 expected skip (month-end history); all produced families reported 0-hour freshness.

| Family | Output and evidence | Result |
|---|---|---|
| Tracked GitHub projects | `data/project_updates/updates_2026-08-04_2026-08-12.json`; 119 releases, 911 merged PRs, 630 open PRs, 3,045 commits across 150 active repos | PASS |
| Direct Nostr/NIP discussions | `data/nostr_nip_discussions/discussions_2026-08-04_2026-08-12.json`; 1 NIP note | PASS |
| Nostr Recap | `data/nostr_recap/recap_2026-08-04_2026-08-12.json`; 18 events | PASS |
| Shakespeare/Soapbox apps | `data/shakespeare_apps/apps_2026-08-04_2026-08-12.json`; 61 submissions, 55 unique apps, 0 new in window | PASS |
| NIP-34 | `data/nip34_repos/nip34_2026-08-04_2026-08-12.json`; 23 tracked repos, 150 discovered repos, 0 patches, 6 issues | PASS |
| Zapstore | `data/zapstore_releases/zapstore_2026-08-12.json`; 1,092 records, 421 Nostr-relevant, 2 new apps and 419 updates | PASS |
| Candidate-only app discovery | `data/app_discovery/discovery_2026-08-12.json`; 118 candidates (116 GitHub, 2 NIP-89) | PASS |
| OpenSats / Sovereign Engineering heartbeat | `data/heartbeats/heartbeat_2026-08-04_2026-08-12.json`; SEC-08 22 archived projects, 0 tagged events; nostr-fund 1,611 events/62 repos; general-fund 3,012 events/77 repos | PASS |
| Month-end history | Target is not the final weekly issue of August | EXPECTED SKIP |
| NIP/BUD/NAP/MIP/Gamma/CORD/NWC specs | `data/spec_updates/spec_updates_2026-08-13.json` (exclusive-until filename); NIP active 7 PR/1 commit, NAP active 11/1, CORD active 5/3, NWC active 1/0; BUD, MIP, Gamma quiet | PASS |

Additional commands:

- `python3 scripts/build_coverage_history.py`: PASS, 362 projects across 35 newsletters; `data/coverage_history.json` updated.
- `bash scripts/detect_non_github_sources.sh`: PASS; `data/non_github_sources_2026-08-12.json` written and 147 NIP-34 repositories without GitHub mirrors reported.

## Final-two-day triage

Boundary: the prior fetch completed about 2026-08-11 15:31 UTC. The refresh surfaced 457 tracked-GitHub events across 56 projects, 66 Zapstore records across six apps, 49 newly active candidate-only repositories, Nostr Recap/NIP-34 items, and heartbeat/spec-window changes. Every group received an include/skip decision:

| Candidate group | Decision | Primary evidence and reason |
|---|---|---|
| Nostria 4.1.67 | INCLUDE | https://github.com/nostria-app/nostria/releases/tag/v4.1.67 and the full 58-commit diff from 4.1.53. Updated the draft for encrypted-community dissolution, media, attachments, threaded chat, and billing. |
| Mostro 0.18.1 | INCLUDE | https://github.com/MostroP2P/mostro/releases/tag/v0.18.1 and its 26-commit diff. Added the Cashu escrow foundation, trusted-Nostr price provider, first-contact PoW advertisement, sender validation, key/URL/payout hardening, and restart recovery. |
| Buzz Desktop 0.5.10 | INCLUDE | https://github.com/block/buzz/releases/tag/v0.5.10. Expanded the existing Buzz item with reply threading, searchable membership, upload visibility, multi-image ordering, and mobile community lifecycle parity. |
| BitBlik 0.10.0 | SKIP | https://github.com/bit-blik/bitblik/releases/tag/v0.10.0. Full notes center on fiat rails, translations, NFC import, and payout UI, without a material Nostr-facing change. |
| RSSNotes 0.1.0, Stash Bookmark, Earthly | SKIP | https://github.com/trinidz/rssnotes/releases/tag/v0.1.0 and corresponding Nostr Recap records. Potentially relevant, but too late for complete identity, release-diff, continuity, and recipient verification before the refresh gate; preserve for next intake rather than publish underverified claims. |
| gittr/gittr-mcp; Indexstr/SIP/Crawlstr/Presearchstr; Relay Hands; iris-chat-rs; eventstore search; Mosaico/NMP | SKIP | Signed NIP-34 announcements in `nip34_2026-08-04_2026-08-12.json`. They are substantive candidates, but repository ownership, full implementation state, continuity, and outreach identities could not all be verified to publication standard in the remaining refresh window. |
| Divine Mobile 1.0.19, Amber 6.4.0, Mostro Core 0.14.2, existing MDK/LaWallet/Bray/ClipRelay items | RETAIN / NO DUPLICATE | Their refreshed events duplicate already reviewed Newsletter #35 sections or add maintenance after the selected release. Existing coverage remains the complete verified story. |
| Remaining 56-project GitHub activity | SKIP AS INDIVIDUAL ITEMS | Audited project-level. Most activity was unreleased maintenance, dependency/CI/docs/test work, already represented by the selected release, or below the weekly editorial threshold. No additional independently complete release story survived verification. |
| Remaining six-app Zapstore delta | SKIP AS INDIVIDUAL ITEMS | Release records either corroborated tracked GitHub candidates above, were repeated app versions, or lacked a complete primary-source release delta. |
| 49 app-discovery additions | SKIP / QUEUE FOR VERIFICATION | Candidate-only output intentionally requires ownership and behavior verification before tracking. No candidate had independently verified final-two-day release evidence; strongest future checks include notary, plaza, wisp, ephemeral-relay, blossom-rs, nostr-relay, nula, xray, FSociety, and blocktv. |
| Direct Nostr discussion | SKIP | Artifact is identical to the prior fetch; no late discussion surfaced. |
| Shakespeare/Soapbox | SKIP | No new app in the issue window. |
| Heartbeats | SKIP AS LATE STORIES | Refreshed OpenSats/SovEng data found no new final-two-day cohort or tagged-event story beyond material already triaged. |
| Spec families | SKIP AS LATE STORIES | Comparing the August 12 and exclusive-until-August-13 artifacts found no newly added/changed PR or commit. Lower counts are window expiry, not new development. |

## Editorial changes

- Upgraded the Nostria Top Story from 4.1.53 to 4.1.67 with full release-diff coverage.
- Added Mostro 0.18.1 to Tagged Releases with complete substantive Nostr/security changes.
- Expanded the existing Buzz development story with verified 0.5.10 changes rather than creating a duplicate item.
- Replaced a Safebox documentation URL that began returning 404 during live review with the current project-controlled recovery guide.
- Added Newsletter #35 to the NIP-59 topic backlink list because the late Mostro paragraph introduced a NIP-59 link.
- Synchronized assembled Markdown and section sources with `python3 scripts/sync_newsletter_sections.py`.

Intended changed files:

- `content/en/newsletters/2026-08-12-newsletter.md`
- `content/en/topics/nip-59.md`
- `data/newsletter_workspace/sections/{lead-stories,top-stories,tagged-releases,unreleased-changes,protocol-work,nip-updates,nip-deep-dive}.md`
- `data/newsletter_workspace/review_{claims,links,prose,topics,continuity}_2026-08-12.md`
- `data/newsletter_workspace/review_log_2026-08-12.md`
- `data/newsletter_workspace/prepublish_refresh_2026-08-12.md`
- `data/heartbeats/heartbeat_2026-08-04_2026-08-12.json`
- `data/spec_updates/spec_updates_2026-08-13.json`

## Five review gates and build

1. Links: 72/72 distinct external destinations returned HTTP 2xx/3xx after the Safebox repair; zero broken links. Paragraph-link checker passed.
2. Claims: complete release notes/tag diffs for Nostria, Mostro, Buzz, and BitBlik were checked; all retained claims have primary evidence; BitBlik was excluded.
3. Prose/style: the complete assembled newsletter was read front to back. Continuity, banned-phrase/style, paragraph-link, and event-example scripts all passed. No duplicated late section was introduced.
4. Topics: production-rendered topic checker passed with 8 topic pages carrying Primary sources blocks and 8 rendered Newsletter #35 backlinks.
5. Continuity: `check_newsletter_continuity.py` passed against the complete English archive; repeated topics use new sources or explicitly state a material status change.

Commands and results:

- `python3 scripts/check_newsletter_continuity.py ...`: PASS.
- `python3 scripts/check_newsletter_style.py ...`: PASS.
- `python3 scripts/check_newsletter_paragraph_links.py ...`: PASS.
- `python3 scripts/check_newsletter_event_examples.py ...`: PASS.
- `python3 scripts/check_topic_backlinks.py ... --rendered-html public/en/newsletters/2026-08-12-newsletter/index.html`: PASS (8/8).
- Live external URL audit: PASS (72/72).
- `bun run build`: PASS; Pagefind indexed 2,204 pages in 10 languages.
- `git diff --check`: PASS.

## Handoff

The refresh passed and PR #133 remains a draft publication PR. This worker will normalize it to the required single commit and force-with-lease update it. Publication remains scheduled for 16:00 UTC unless the owner sends an explicit hold or a later publication verification gate fails.

GATE: PASS (10/10 source families accounted for with 9 fresh outputs and 1 expected month-end skip; final-two-day triage recorded; PR/DM feedback checked; 72/72 live links; all five review gates and production build passed; no publication action performed)
