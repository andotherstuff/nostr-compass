# Newsletter #33 consolidated review log

Generated: 2026-07-29T05:28:27Z
Target: `content/en/newsletters/2026-07-29-newsletter.md`
State: unpublished (`draft: true`)

## Editorial gates

- PASS: LinkCheck resolved all 90 external URLs and verified the rendered topic backlinks.
- PASS: ClaimCheck reproduced every Nostrology number from the live page and retained the prior PR, NIP, release, commit, and relay-event checks.
- PASS: ProseStyle scored 100/100 with zero violations; every prose paragraph carries a repository or primary-source link.
- PASS: TopicCoverage updated NIP-65 and resolved 30 rendered backlinks across 21 referenced topic pages.
- PASS: Continuity found no duplicate Nostrology coverage and confirmed the NIP-65 item adds a distinct source and current adoption evidence.
- PASS: Amethyst 1.13.0, Mosaico 0.1.2, the seven-family specification sweep, Sovereign Engineering discovery, and `Six Years of Nostr Julys` remain intact.

## Mechanical evidence

- PASS: `scripts/check_newsletter_style.py`.
- PASS: `scripts/check_newsletter_paragraph_links.py`.
- PASS: `scripts/check_month_end_history.py`.
- PASS: `scripts/check_newsletter_continuity.py --history-dir content/en/newsletters`.
- PASS: Hugo draft/future render and `scripts/check_topic_backlinks.py`.
- PASS: Bun production build and Pagefind indexing.
- PASS: `git diff --check`.

## Outreach readiness

- Publish preview resolves 21 project identities.
- Nostrology resolves to WhisperHash through source attribution, a Sovereign Engineering interview, a relay-backed kind `0` profile, and `_@whisperhash.com` NIP-05. No separate project npub was found, so project and maintainer aliases share one deduplicated recipient.
- After PR #117 was updated, the targeted dry run selected that one shared recipient. The real NIP-17 send produced event `4ebb50feb1c5c72cbc322b9fc2ad1cd15ff91394a1b229173f176e5acd8d6f5a`, accepted by 4 of 9 relays. Independent readback found the exact event on `wss://nos.lol`, `wss://relay.primal.net`, and `wss://relay.snort.social`.
- pakstr and swift-nostr remain unresolved after the current source checks; no npub was guessed.
- Marmot/MDK remains on the explicit `no_dm` list.

GATE: PASS (all five evidence-bearing review artifacts pass after the Nostrology edit; generated 2026-07-29T05:28:27Z)

## Publication-day refresh review

Reviewed: 2026-07-29T13:46:49Z through 2026-07-29T14:00:03Z
State: incident-recovery update after PR #117 merged early; no merge, deployment, signing, broadcast, or Kanban completion performed by the refresh job.

- PASS: LinkCheck performed content-bearing GETs for 113 unique external URLs, with 113 HTTP 200 responses; 23 internal content paths, 44 PR URLs, 21 release URLs, 23 directly version-labelled URLs, and 35 distinct live NIP identifiers passed.
- PASS: ClaimCheck live-verified the late Amethyst, GitWorkshop, Kairos, Shosho, NoorNote, MDK, Ditto, Keep, Routstrd, and Mill claims, including merged versus untagged wording and the corrected local Kairos-to-Astraea handoff.
- PASS: ProseStyle ran all three required scripts, found zero banned phrases, em dashes, prohibited comparison structures, rhetorical questions, or passive-voice violations, and retained all six month-end history years.
- PASS: TopicCoverage rendered the issue and verified 23 topic pages with Primary sources blocks and 32 backlinks, including exact NIP-09 and NIP-49 anchors.
- PASS: Continuity compared the issue against all 32 prior English issues, read the three immediate predecessors in full, and verified distinct primary sources and substantive impact for 16 repeated project headers.
- PASS: `npm run build` completed the Hugo production build and Pagefind indexed 2,170 pages across 10 languages at 2026-07-29T14:01Z.
- PASS: `git diff --check` and `bun test publish/outreach-scope.test.ts` completed with zero failures.

GATE: PASS (five evidence-bearing publication-day review gates plus production build passed; final verification 2026-07-29T14:00:03Z)
