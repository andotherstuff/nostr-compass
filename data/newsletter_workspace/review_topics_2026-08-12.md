# Topic and event review — Newsletter #35

Validated: 2026-08-12 UTC
Target: `content/en/newsletters/2026-08-12-newsletter.md`

- `python3 scripts/check_newsletter_event_examples.py ...` returned `PASS: every JSON event example has valid structure and no placeholder data`.
- The kind 5 and kind 1984 examples link to their exact public-relay events and retain all seven NIP-01 event fields.
- The production build rendered all ten locale sites and Pagefind indexed 2,204 pages without error.
- `python3 scripts/check_topic_backlinks.py ... --rendered-html ...` returned `PASS: 8 topic pages have Primary sources blocks and 8 rendered newsletter backlinks`; the NIP-34 topic page records the final-cutoff proposal and links back to Newsletter #35.
- NIP-09 and NIP-56 are merged, absent from prior deep-dive rotation, and each cites at least three current implementation paths.

GATE: PASS (event integrity, deep-dive eligibility, 8/8 topic sources, and 8/8 rendered backlinks at 2026-08-12T15:45Z)
