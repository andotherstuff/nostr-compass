# Newsletter #33 continuity review

Generated: 2026-07-29T14:35:31Z
Target: `content/en/newsletters/2026-07-29-newsletter.md`
History corpus: `content/en/newsletters/`

## Execution

- Ran `python3 scripts/check_newsletter_continuity.py <newsletter> --history-dir content/en/newsletters`: PASS, every repeated project cites a distinct primary source.
- Rechecked the last three prior issues in full: 2026-07-08 (#30), 2026-07-15 (#31), and 2026-07-22 (#32).
- Compared the edited draft against all earlier English issues through the continuity script.

## Late-story continuity decisions

- Bray 2.3.0 is distinct from Newsletter #31's Bray 1.34.0 story: the new sources are release 2.3.0 and PRs #75-77, covering arbitrary-event gift wrapping, relay authentication/testing, NIP-77 request behavior, and Blossom test authorization.
- Buzz Desktop 0.5.0 is explicitly framed after Newsletter #32's Armada/Buzz workspace coverage. The new source is release 0.5.0 with merged invite, relay-search, join-policy, identity-republication, and dependency-security changes.
- Amethyst's two release tags are separated, so the July 29 follow-up does not restate the July 28 source as a new change.

GATE: PASS (all-prior checker PASS; #30-#32 read in full; Bray and Buzz use distinct release/PR sources and substantive new impact, ran 2026-07-29T14:35Z)
