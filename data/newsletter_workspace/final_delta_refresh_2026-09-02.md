# Final delta refresh — 2026-09-02

Final-delta task t_c6b8a9bb. Window: 2026-09-02 14:30→17:33 UTC (mandatory
lightweight cutoff ran after the 15:30 floor; final family repair completed
17:15 UTC; final gates ran 17:28–17:33 UTC).

## Required artifacts (all present and evidence-bearing)

- `data/newsletter_workspace/prepublish_refresh_2026-09-02.md` — written by the
  14:00 refresh; ends `GATE: PASS (style/continuity/paragraph-links/
  event-examples/build/topic-backlinks all PASS on head a1e6857; ...)`.
- This file — `data/newsletter_workspace/final_delta_refresh_2026-09-02.md`.

## Broad fetch (began 14:3x UTC) and failure resolution

The broad `scripts/fetch_all.sh --since-days 8 --newsletter-date 2026-09-02`
run (log: `final_delta_fetch_log_2026-09-02.txt`) completed 7/10 families with
one skip (not month-end) and two failures, both now resolved:

1. Zapstore family failed on a jq compile error in the summary printer of
   `scripts/fetch_zapstore_releases.sh`: two single-quoted literals
   (`'new app'`, `'quiet week'`) inside the single-quoted shell string broke
   jq parsing. Fixed by rephrasing the literals without inner single quotes
   (committed in this PR). Family rerun at 17:12 UTC completed with exit 0 and a
   correct summary; fresh artifact `data/zapstore_releases/zapstore_2026-09-02.json`
   (1354 releases in window, 548 Nostr-relevant, Voca 1.1.0 among them).
2. Specification family failed with `gh api` exit 75 (transport) on
   `repos/nostr-protocol/nips/commits`. The identical call succeeded on retry;
   `scripts/fetch_spec_updates.py` rerun at 17:15 UTC completed all seven
   families (NIPs active, MIPs active, NWC active; BUD/NAP/Gamma/Concord quiet)
   and wrote `data/spec_updates/spec_updates_2026-09-03.json`.

## Mandatory final cutoff (>=15:30 UTC) findings integrated

Diffing the repaired spec artifact against the previous day's artifact found
two specification merges inside the issue window that were not yet covered:

- NIP-67 merged `"auth"` EOSE hint (nostr-protocol/nips#2371, merged
  2026-09-01T12:32Z): third hint value beside `finish`/`more`; relay must send
  the NIP-42 AUTH challenge before the EOSE carrying it. Verified via live
  commit patch (67.md and 42.md changes).
- NIP-84 merged tag-scheme update (nostr-protocol/nips#2454, merged
  2026-09-01T17:12Z): `i` tags per NIP-73 join `a`/`e`/`r` for highlight
  sources; quote-highlight rendering relaxed from MUST to SHOULD.

Both were added as a new "Nostr Implementation Possibilities" subsection in
the NIP Updates section of the assembled draft and the synchronized
`sections/nip-updates.md`/`sections/protocol-work.md` artifacts, each PR a
separate paragraph with wire-format and implementation detail per the
editorial contract. The "This week" summary and frontmatter description were
updated to match. Topic backlinks were appended to `nip-67`, `nip-84`,
`nip-42` topic pages ("Newsletter #38: NIP Updates" anchor
`#nostr-implementation-possibilities`).

Open spec PRs updated in the window (NIP-44 test-vector notes, NIP-F5 census,
NIP-100 SNIN, etc.) are proposals without merges in-window and stay excluded
per the activity rule. The two NIP-A3 commits (merged 2026-08-26/27) fall
under the earlier coverage window boundary; selection review records the
spec-family dispositions.

The repaired Zapstore artifact surfaced Voca 1.1.0 (released 2026-08-29,
after the draft's 1.0-only coverage). Its release notes (sentence-level
scroll timing, long-document smoothing, widget recovery) were verified from
the kind-30267 release content and folded into the existing Voca lead-story
paragraph; section artifact re-synchronized.

## Owner note disposition

- Voca inclusion: fulfilled (lead story, source-verified wording, npubs.yml
  and projects.yml entries with evidence links, nip-23/nip-65 topic backlinks).
- MDK v0.9.17: fulfilled by the 14:00 refresh (tagged-releases item at v0.9.17
  with PRs #1617/#1620/#1621/#1622).
- Publication hold (`publication_hold_2026-09-02.md`): conditions 1–3 satisfied
  by this run (Voca covered, draft/sections synchronized, all gates green on
  the final revision). Condition 4 (finalized English Markdown durably
  delivered to the originating Marmot group) is handled by this task's
  MARMOT_OUTCOME comment carrying the exact outbox file
  `/opt/data/blog/handoffs/deliverables/2026-09-02-newsletter.md`
  (sha256 983b3798a8e459add41d138e113bdc02dab5fadc1fbfb73b14595a9c6f777f52,
  38944 bytes, byte-identical to the committed newsletter (final commit e7c43ac)) through
  the durable outcome synchronizer; the hold stays active until durable
  attachment readback exists. This task merges nothing, deploys nothing,
  signs nothing, broadcasts nothing.

## Final gate evidence (all run on the final committed revision (e7c43ac; newsletter content identical since fbb435c))

- `check_newsletter_style.py` → PASS: no banned filler phrases or opaque anchors.
- `check_newsletter_continuity.py --history-dir content/en/newsletters`
  → PASS: repeated topics use new sources or state a material status change.
- `check_newsletter_paragraph_links.py` → PASS: every prose paragraph links to
  a repository or primary source.
- `check_newsletter_event_examples.py` → PASS: every JSON event example valid,
  no placeholder data.
- `bun run build` → PASS (Hugo production build, 5.4s).
- `check_topic_backlinks.py` on
  `public/en/newsletters/2026-09-02-newsletter/index.html` → PASS: 28 topic
  pages with Primary sources blocks, 30 rendered newsletter backlinks.
- New links verified live: nips#2371 → 200, nips#2454 → 200,
  nips/blob/master/67.md → 200, gitworkshop Voca repo page → 200.
- Sections synchronized via `scripts/sync_newsletter_sections.py` after every
  edit; assembled file and `sections/*.md` carry identical text.

## PR state

- PR #147 updated to a single amended commit
  `e7c43ac` ("Draft Nostr Compass
  Newsletter 38") directly over origin/main 2a1b5b3 via force-with-lease
  (a1e6857 → e7c43ac via two content-identical amends), resolving the earlier two-commit stack flagged by
  operator alert. Authoritative `gh` readback: commits=1, isDraft=true,
  mergeable, headRefOid matches the local push exactly.
- CI on the final head: build COMPLETED/SUCCESS at 2026-09-02T17:32:29Z
  (run 33661604758); deploy SKIPPED (expected on draft PRs).
- `draft: true` preserved in frontmatter. No merge, deploy, sign, or
  broadcast performed by this task.

GATE: PASS (10/10 fetch families resolved; late NIP-67/NIP-84 merges and Voca 1.1.0 integrated; style/continuity/paragraph-links/event-examples/build/topic-backlinks PASS on the committed revision; PR #147 one commit (e7c43ac), draft:true, CI green; hold conditions 1-3 met, condition 4 in durable delivery via this task's outcome comment)
