# Nostr Compass pre-publication refresh, 2026-07-29

Start UTC: 2026-07-29T13:05:27Z
End UTC: 2026-07-29T15:36:55Z
Target: `content/en/newsletters/2026-07-29-newsletter.md`
Mode: publication-day incident-recovery update

## Preconditions and incident state

- Wednesday/date gate: PASS, target `2026-07-29`.
- GitHub authentication, Hugo 0.123.7 extended, Bun 1.3.14, Bunx 1.3.14, and nak 0.18.3 passed preflight.
- Git refs were fetched without resetting, cleaning, deleting, or rewriting worktree data.
- Original PR [#117](https://github.com/andotherstuff/nostr-compass/pull/117) merged early at 2026-07-29T12:45:34Z as commit `4fd0ebedc662760c3d3d128f0315810b54d4dc6a`.
- Recovery branch: `newsletter/2026-07-29-update`, created from `origin/main` without history rewriting or force-push.
- Draft recovery PR: [#118](https://github.com/andotherstuff/nostr-compass/pull/118), OPEN, DRAFT, CLEAN at 2026-07-29T14:12:36Z.
- This job did not merge, mark ready, deploy intentionally, change draft state, invoke Amber, sign or broadcast a Nostr event, or complete the Kanban parent.

## Source-family refresh evidence

The aggregate `scripts/fetch_all.sh --since-days 8` run started at 13:05:27Z and exceeded the 600-second wrapper while NIP-34 was still running. Completed early families were retained. NIP-34, Zapstore, heartbeats, and the specification sweep were rerun individually; all retries exited 0. `scripts/build_coverage_history.py` and `scripts/detect_non_github_sources.sh` also exited 0. No more than one subfamily was empty: Gamma recorded no specification activity, and the remaining families returned fresh data.

1. **Tracked GitHub repositories**
   - Output: `data/project_updates/updates_2026-07-21_2026-07-29.json`
   - Generated: 2026-07-29T13:06:46.693171Z
   - Counts: 150 active repositories; 189 releases; 1,092 merged PRs; 693 open PRs; 4,011 commits.
   - Log: `logs/prepublish_refresh_2026-07-29/fetch_all.log`
2. **Direct Nostr/NIP discussions**
   - Output: `data/nostr_nip_discussions/discussions_2026-07-21_2026-07-29.json`
   - Generated: 2026-07-29T13:08:02Z
   - Counts: 2 NIP documents; 0 direct notes; 0 community records.
   - Log: `logs/prepublish_refresh_2026-07-29/fetch_all.log`
3. **Nostr Recap**
   - Output: `data/nostr_recap/recap_2026-07-21_2026-07-29.json`
   - Generated: 2026-07-29T13:08:27Z
   - Count: 17 events.
   - Log: `logs/prepublish_refresh_2026-07-29/fetch_all.log`
4. **Shakespeare/Soapbox apps**
   - Output: `data/shakespeare_apps/apps_2026-07-21_2026-07-29.json`
   - Generated: 2026-07-29T13:08:38Z
   - Counts: 61 submissions; 55 unique apps; 0 new in the issue window.
   - Log: `logs/prepublish_refresh_2026-07-29/fetch_all.log`
5. **NIP-34 repositories**
   - Output: `data/nip34_repos/nip34_2026-07-21_2026-07-29.json`
   - Generated: 2026-07-29T13:26:09Z
   - Counts: 23 tracked repositories; 183 discovered announcements; 0 in-window patches; 58 in-window issues.
   - Retry log: `logs/prepublish_refresh_2026-07-29/nip34_retry1.log`, exit 0.
6. **Zapstore developer-signed releases**
   - Output: `data/zapstore_releases/zapstore_2026-07-29.json`
   - Generated: 2026-07-29T13:19:25Z
   - Counts: 857 releases; 551 Nostr-relevant; 454 strong matches; 2 new apps; 549 updates; 38 tracked; 513 candidates.
   - Retry log: `logs/prepublish_refresh_2026-07-29/zapstore_retry1.log`, exit 0.
7. **OpenSats and Sovereign Engineering heartbeats**
   - Output: `data/heartbeats/heartbeat_2026-07-21_2026-07-29.json`
   - Generated: 2026-07-29T12:52:28.367Z
   - Counts: OpenSats Nostr Fund 255 repositories / 1,903 events; General Fund 209 repositories / 2,718 events; Sovereign Engineering cohort SEC-08, 22 archive projects, 5 relay events, current relay project tag FIPS.
   - Retry log: `logs/prepublish_refresh_2026-07-29/heartbeats_retry1.log`, exit 0.
8. **Specification families**
   - Output: `data/spec_updates/spec_updates_2026-07-30.json`; filename uses the exclusive `until=2026-07-30T00:00:00Z` boundary, while the generated data belongs to the July 29 refresh.
   - Generated: 2026-07-29T13:16:17.448389Z
   - Counts: NIPs 15 PRs / 3 commits; BUDs 1 / 0; NAPs 9 / 3; MIPs 2 / 3; Gamma 0 / 0; CORD 1 / 0; NWC 1 / 0.
   - Retry log: `logs/prepublish_refresh_2026-07-29/spec_updates_retry1.log`, exit 0.

Coverage and aggregation:

- `python3 scripts/build_coverage_history.py`: PASS, log `logs/prepublish_refresh_2026-07-29/coverage_history.log`.
- `bash scripts/detect_non_github_sources.sh`: PASS, log `logs/prepublish_refresh_2026-07-29/non_github_sources.log`.

## Late triage and editorial decisions

Publication-day comparison used cutoff `2026-07-28T14:08:55.638055Z`, the prior triage/selection artifacts, synchronized sections, topic pages, and every earlier English issue. The project feed contained 695 post-cutoff rows; routine commits, release churn, cumulative release notes, Bitcoin-only activity, NIP-34 hosting noise, and changes without distinct user/protocol impact were excluded.

Included or updated after primary-source verification:

- Amethyst 1.13.0 and 1.13.1, with the broad feature set attributed to 1.13.0 and only the July 29 follow-up attributed to 1.13.1.
- GitWorkshop developer-signed 3.1.1 Android signer repair.
- Kairos signed 0.1.0 launch and 0.1.1 reminders/local Astraea instruction.
- Shosho 1.0.0 marketplace and live-streaming update.
- NoorNote 1.3.1 with 1.3.0 claims separated by release.
- MDK 0.9.10 and merged PRs #1157, #1159, and #1167.
- Ditto 2.34.2 status cards and zap-comment display.
- Keep merged, untagged PRs #451 through #455.
- Routstrd merged, untagged PR #56.
- Mill's merged but unreleased cloud-account key-backup draft, explicitly labeled provisional.
- Bray 2.3.0 and merged PRs #75-77, covering arbitrary-event gift wrapping through NIP-46, NIP-42 relay tests, NIP-77 request behavior, and an authorized Blossom test endpoint.
- Buzz Desktop 0.5.0 and merged PRs #3141, #2871, #2862, and #2607, framed as a distinct follow-up to Newsletter #32's Armada/Buzz workspace coverage.

No further material item passed the late gate from Nostr Recap, Shakespeare, NIP-34, heartbeats, or the remaining specification and Zapstore candidates. The current issue already contained the week's material NIP, BUD, NAP, MIP, CORD, and NWC changes; Gamma had no public change.

## Files changed for the update PR

Editorial and evidence files:

- `content/en/newsletters/2026-07-29-newsletter.md`
- `content/en/topics/nip-09.md`
- `content/en/topics/nip-49.md`
- `data/newsletter_workspace/review_log_2026-07-29.md`
- `data/newsletter_workspace/review_{links,claims,prose,topics,continuity}_2026-07-29.md`
- `data/newsletter_workspace/human_overrides_2026-07-29.md`
- `data/newsletter_workspace/sections/{lead-stories,tagged-releases,unreleased-changes,protocol-work,nip-updates,history}.md`
- `data/npubs.yml`
- `data/newsletter_workspace/outreach_refresh_2026-07-29.md`
- `data/newsletter_workspace/prepublish_refresh_2026-07-29.md`
- `data/newsletter_workspace/incident_2026-07-29_early_merge.md`
- `data/heartbeats/heartbeat_2026-07-21_2026-07-29.json`
- `data/spec_updates/spec_updates_2026-07-30.json`

Ignored runtime evidence is preserved under `logs/prepublish_refresh_2026-07-29/` and `publish/out/`; these paths are excluded from Git by repository policy.

Outreach extraction fix and regression coverage:

- `scripts/publish.ts`
- `tests/publish_mentions.test.ts`

Local ignored runtime adaptation:

- `publish/dm-outreach.ts` now resolves the Compass root from `COMPASS_DIR` or its own directory instead of the removed `/home/vibe/compass` path. The `publish/` directory is intentionally gitignored, so this local operational fix is not part of PR #118.

Unrelated tracked/untracked files were preserved and not staged.

## Five review gates

1. **Links, PASS at 2026-07-29T14:35:31Z.** Content-bearing checks passed for 124/124 unique external URLs; all 40 internal references covering 25 unique targets resolve.
2. **Claims, PASS at 2026-07-29T14:35:31Z.** Live APIs verified 34/34 NIP files and 52/52 PR records, comprising 43 merged and 9 open PRs. Amethyst, Kairos, Bray, Buzz, NoorNote, and Mill attribution was checked against primary release, repository, signed Zapstore, and relay evidence.
3. **Prose/style/history, PASS at 2026-07-29T14:35:31Z.** Shaka scored 100/100 on 4,675 words; `check_newsletter_style.py`, `check_newsletter_paragraph_links.py`, and `check_month_end_history.py` passed; the opening digest has no visible version, PR, event-kind, or incidental NIP identifiers.
4. **Rendered topics/backlinks, PASS at 2026-07-29T14:35:31Z.** `check_topic_backlinks.py` verified 25 topic pages with Primary sources blocks and 34 rendered backlinks after repairing the Kairos/NIP-09 heading anchor.
5. **Continuity, PASS at 2026-07-29T14:35:31Z.** `check_newsletter_continuity.py` passed across all prior English issues; the three immediate predecessors were read in full, and Bray/Buzz use distinct release/PR sources with substantive new impact.

Final mechanical commands:

```text
python3 scripts/check_newsletter_style.py content/en/newsletters/2026-07-29-newsletter.md
PASS: no banned Compass filler phrases

python3 scripts/check_newsletter_paragraph_links.py content/en/newsletters/2026-07-29-newsletter.md
PASS: every prose paragraph links to a repository or primary source

python3 scripts/check_month_end_history.py content/en/newsletters/2026-07-29-newsletter.md
PASS: month-end history title, years, depth, and source links are valid

python3 scripts/check_newsletter_continuity.py content/en/newsletters/2026-07-29-newsletter.md --history-dir content/en/newsletters
PASS: repeated projects each cite a distinct primary source

python3 scripts/check_topic_backlinks.py content/en/newsletters/2026-07-29-newsletter.md --rendered-html public/en/newsletters/2026-07-29-newsletter/index.html
PASS: 25 topic pages have Primary sources blocks and 34 rendered newsletter backlinks

bun test tests/publish_mentions.test.ts
4 pass, 0 fail

git diff --check
PASS
```

## Build and outreach

- `npm run build`: PASS again at 2026-07-29T15:36Z. Hugo built all ten languages; Pagefind indexed 2,170 pages and 166,752 words.
- Targeted outreach dry runs: PASS. Seven unique NIP-17 recipients were planned: the original Kairos/LWB, Mill/0ceanSlim, Routstrd, Shosho, and Keep/wksantiago group, plus de-duplicated Bray/Darren and Buzz Desktop/Block recipients. Receipt: `data/newsletter_workspace/outreach_refresh_2026-07-29.md` and ignored plan JSON files under `publish/out/`.
- No real outreach DM was signed or sent because this refresh job may not invoke Amber. The 16:00 publication worker must review the targeted plan, avoid resending the full issue campaign, and perform any approved targeted send before publication.

## Final 15:17 UTC update run

The user-requested final aggregate refresh ran from 15:17 through 15:34 UTC. `scripts/fetch_all.sh --since-days 8` completed **8/8 source families, 0 failed, 0 skipped**, and reported every family 0 hours old. Coverage-history and non-GitHub aggregation then exited 0.

- GitHub projects: 150 active repositories, 189 releases, 1,092 merged PRs, 693 open PRs, and 4,011 commits. No release, merged PR, or commit occurred after the previous 14:51 cutoff.
- Direct Nostr/NIP discussions: 2 NIP documents, 0 direct notes, 0 community records; no post-cutoff event.
- Nostr Recap: 17 events; no post-cutoff event.
- Shakespeare apps: 61 submissions, 55 unique apps, 0 new in-window apps.
- NIP-34: 23 tracked and 184 discovered repositories, 0 in-window patches, 58 in-window issues. One new `microfips-upstream` kind 30617 announcement appeared at 14:44:59 UTC, with an empty description and no patch or issue evidence. NIP-34 hosting alone does not establish newsletter scope, and the current FIPS section already covers its substantive primary-source changes, so no prose was added.
- Zapstore: fresh eight-day relay result completed. No post-cutoff signed release passed the editorial gate. Same-day re-fetches mutate the persistent publisher-seen baseline, so the second run's `new_apps` field is not used to retract the earlier verified launch decisions.
- Heartbeats: OpenSats and Sovereign Engineering completed with the same FIPS project tag and no post-cutoff event.
- Specifications: NIPs now list 16 active PRs. PR #2424 received a use-case discussion comment at 15:04 UTC but its kind 10045 proposal did not change and is already covered. PR #2419 entered the fresh snapshot because of a 13:24 concept-ACK review; its sole specification commit predates the issue window. No newsletter text changed.

Final validation passed: style, paragraph links, month-end history, continuity, 3 topic-backlink unit tests, 14 publish tests, production build, 25-topic/34-backlink validation against minified HTML, canonical publish payload generation with `--force`, and `git diff --check`.

## Git and publication gate

Final parent verification against the minified production build found that `check_topic_backlinks.py` accepted only quoted HTML `id` attributes, while Hugo emits unquoted IDs under minification. A regression test reproduced the false stale-fragment failures before the implementation changed. The checker now accepts quoted and unquoted IDs; all three unit tests pass, and the checker validates 25 topic pages with 34 backlinks directly against `public/en/newsletters/2026-07-29-newsletter/index.html`. The second GitHub refresh contained zero project releases, merged PRs, or commits after the original refresh cutoff once timestamps were normalized to UTC.

```text
python3 -m unittest tests.test_check_topic_backlinks -v
3 tests, PASS

python3 scripts/check_topic_backlinks.py content/en/newsletters/2026-07-29-newsletter.md --rendered-html public/en/newsletters/2026-07-29-newsletter/index.html
PASS: 25 topic pages have Primary sources blocks and 34 rendered newsletter backlinks
```

- First update commit: `9d3d365` (`Refresh Newsletter #33 for publication day`), pushed without force to `origin/newsletter/2026-07-29-update`.
- Draft update PR: https://github.com/andotherstuff/nostr-compass/pull/118, OPEN/DRAFT/CLEAN.
- Parent Kanban task: `t_ed0f1dbf`, remains `blocked`.
- Translation task `t_d6185011` and podcast task `t_dec07541` remain `todo`.
- No publication action occurred. The recovery PR remains parked for the 16:00 UTC publication gate.

GATE: PASS (final 15:17 UTC run completed 8/8 source families with 0 failures; no material post-cutoff change required prose edits; all mechanical, publish-payload, production-build, and CI gates pass; PR #118 remains the publication target; ended 2026-07-29T15:36:55Z)
