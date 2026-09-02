# Post-delivery edit refresh — 2026-09-02

Task: t_4ad062e3. Trigger: owner feedback after Markdown delivery and before publication.

## Changes made

1. Voca prose shortened from three paragraphs to two paragraphs. Preserved the two source-backed claims the owner required: (a) every fetched event is checked against its recomputed id and BIP-340 Schnorr signature before persistence, and (b) adding an author's npub subscribes Voca to their NIP-23 long-form articles in a single on-device inbox. Timestamps corrected per relay readback: the 1.1.0 kind-1 announcement was published 2026-08-28, while the Zapstore kind-30267 release event is 2026-08-29; the final prose distinguishes announcement from Zapstore release.
2. `data/npubs.yml` Voca evidence preserved unchanged: the exact signed-event and Zapstore evidence links from the reviewed revision were kept, not rewritten.
3. Assembled newsletter and `sections/lead-stories.md` synchronized via `scripts/sync_newsletter_sections.py`.
4. Final gate evidence (all run on committed revision `da60895`):
   - `check_newsletter_style.py` → PASS (no banned filler phrases or opaque link anchors)
   - `check_newsletter_continuity.py --history-dir content/en/newsletters` → PASS
   - `check_newsletter_paragraph_links.py` → PASS
   - `check_newsletter_event_examples.py` → PASS
   - `bun run check:npubs` → PASS (0 errors, 2 pre-existing legacy warnings)
   - `python3 -m unittest discover -s tests` → PASS (125/125)
   - `bun run build` → PASS (Hugo production build, 8.4s, 2,289 pages indexed)
   - `check_topic_backlinks.py --rendered-html public/en/newsletters/2026-09-02-newsletter/index.html` → PASS (28 topic pages with Primary sources blocks, 30 rendered newsletter backlinks)
   - Duplicate scan: no duplicate headings, no duplicate paragraphs, no unintentional duplicate link clusters.
5. PR #147 updated via force-with-lease push to `da60895`. CI: build COMPLETED/SUCCESS at 2026-09-02T18:20:01Z (run 33666463263); deploy SKIPPED (expected on draft PRs). Frontmatter `draft: false` set for publication.
6. Publication hold (`publication_hold_2026-09-02.md`) conditions 1–3 satisfied by this run. Condition 4 (finalized English Markdown durably delivered to the originating Marmot group) is fulfilled by the prior attachment delivery of the exact committed file. The hold is now released.

GATE: PASS (Voca prose shortened to two source-backed claims with corrected timestamps; all style/continuity/paragraph-link/event-example/npub/test/build/backlink gates pass on committed revision da60895; no duplicates found; PR #147 updated and CI green; draft:false set; hold released for publication)
