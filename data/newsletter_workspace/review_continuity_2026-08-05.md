# ContinuityValueCheck — 2026-08-05

Draft: `content/en/newsletters/2026-08-05-newsletter.md`
History: all earlier `content/en/newsletters/*-newsletter.md` issues, including the three immediately preceding issues read during selection.

## Executed check

`python3 scripts/check_newsletter_continuity.py content/en/newsletters/2026-08-05-newsletter.md --history-dir content/en/newsletters`

Result: `PASS: repeated projects each cite a distinct primary source` (exit 0).

The first review removed reused NIP, Blossom, NAP, Marmot, NWC, and no-change sources. The retained repeated projects each describe a distinct user-facing or protocol-facing change with a distinct release, pull request, or commit URL. The two deep dives are first-time deep-dive subjects according to the all-history selection audit.

GATE: PASS (all-history continuity checker exit 0; final rerun 2026-08-05 UTC)
