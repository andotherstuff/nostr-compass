# Newsletter #33 topic and rendered-backlink review

Generated: 2026-07-29T14:35:31Z
Target: `content/en/newsletters/2026-07-29-newsletter.md`

## Execution

1. Removed `/tmp/compass-review-public`.
2. Ran `hugo --buildDrafts --buildFuture --destination /tmp/compass-review-public`.
3. Confirmed the rendered issue exists at `/tmp/compass-review-public/en/newsletters/2026-07-29-newsletter/index.html`.
4. Ran `python3 scripts/check_topic_backlinks.py <newsletter> --rendered-html <rendered issue>`.

The audit initially detected the Kairos heading change as a stale NIP-09 backlink. `content/en/topics/nip-09.md` now uses the rendered `local-astraea-instruction` anchor, and the complete rerun passed.

GATE: PASS (25 referenced topic pages contain Primary sources blocks and 34 rendered Newsletter #33 backlinks resolve, ran 2026-07-29T14:35Z)
