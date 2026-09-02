# Post-delivery edit refresh — 2026-09-02

Task: t_4ad062e3. Trigger: owner feedback after Markdown delivery and before publication.

## Changes made

1. Voca prose shortened from three paragraphs to two paragraphs. Preserved the two source-backed claims the owner required: (a) every fetched event is checked against its recomputed id and BIP-340 Schnorr signature before persistence, and (b) adding an author's npub subscribes Voca to their NIP-23 long-form articles in a single on-device inbox. Timestamps corrected per relay readback: the 1.1.0 kind-1 announcement was published 2026-08-28, while the Zapstore kind-30267 release event is 2026-08-29; the final prose distinguishes announcement from Zapstore release.
2. Final publication preflight rejected two non-HTTP annotations in Voca's `data/npubs.yml` evidence. They were normalized to the exact GitWorkshop repository page and an `njump.me/nevent` link for Zapstore application event `5bb516cb29571ee0db367a4cc2cd8e3a73cafd92b15560baaf5f0e2b17475ad7`; source specificity was preserved.
3. Assembled newsletter and `sections/lead-stories.md` synchronized via `scripts/sync_newsletter_sections.py`.
4. Final editorial gate evidence (run on committed revision `da60895`; publication proof is consolidated in `publish_log_2026-09-02.md`):
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

GATE: PASS (Voca prose shortened to two source-backed claims with corrected timestamps; style/continuity/paragraph-link/event-example/test/build/backlink gates passed on revision da60895; the npub validator passed after evidence URL normalization; no duplicates found; publication proof is authoritative in publish_log_2026-09-02.md)
