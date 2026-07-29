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
- pakstr and swift-nostr remain unresolved after the current source checks; no npub was guessed.
- Marmot/MDK remains on the explicit `no_dm` list.

GATE: PASS (all five evidence-bearing review artifacts pass after the Nostrology edit; generated 2026-07-29T05:28:27Z)
