# Link review — Newsletter #35

Validated: 2026-08-12 UTC
Target: `content/en/newsletters/2026-08-12-newsletter.md`

- Extracted 73 distinct external destinations from the final-delta Markdown.
- A concurrent live request audit returned HTTP 2xx/3xx for all 73 destinations after the NIP-34 PR #2435 addition.
- Exact-destination duplicate scan returned zero URLs.
- `python3 scripts/check_newsletter_paragraph_links.py ...` returned `PASS: every prose paragraph links to a repository or primary source`.
- All eight internal topic links resolve to existing topic pages.

GATE: PASS (73/73 external destinations reachable at 2026-08-12T15:45Z; 0 broken, 0 unintended duplicate destinations, 0 unsourced prose paragraphs)
