# Continuity and selection review — Newsletter #35

Validated: 2026-08-12 UTC
Target: `content/en/newsletters/2026-08-12-newsletter.md`

The final review compared the draft with the complete English newsletter archive and re-opened the earlier PASS after the actual checker found nine repeated protocol URLs. Unchanged NAP #80/#88/#94/#95, Concord #13/#14, and NWC #2 were removed. NIPs #2378 and Concord #12 were rewritten as explicit open-to-closed transitions. NAP #91/#69/#68/#67/#62/#61/#74 were also removed after primary commit history showed no in-window branch changes despite metadata-only `updated_at` activity.

`python3 scripts/check_newsletter_continuity.py content/en/newsletters/2026-08-12-newsletter.md --history-dir content/en/newsletters` returned `PASS: repeated topics use new sources or state a material status change`.

The final-cutoff NIP-34 item uses newly opened PR #2435 rather than a previously covered destination, and the checker remained green after its addition.

The retained selection contains 6 Top Stories, 7 Tagged Releases, and 3 In Development items. Every retained project clears the score/depth threshold; every omitted candidate is accounted for in curation or the required SKIP list.

GATE: PASS (complete-archive continuity, final-cutoff interest inclusion, and exclusion audit at 2026-08-12T15:45Z)
