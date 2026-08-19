# Review: ContinuityValueCheck — Newsletter #36 (2026-08-19)

## Mechanical gate

```
python3 scripts/check_newsletter_continuity.py \
  content/en/newsletters/2026-08-19-newsletter.md \
  --history-dir content/en/newsletters
  PASS: repeated topics use new sources or state a material status change
```

The first run of this checker returned seven failures, all reused primary-source URLs:
Amber v6.4.0, Nostria v4.1.67, Divine Mobile 1.0.19, NoorNote v1.3.2, ClipRelay v0.1.3,
NIPs PR #1647, and Concord PR #18 (twice). Each was resolved rather than suppressed:

- The five release back-references now link to the corresponding section of the
  2026-08-12 issue instead of re-citing the release URL, which is the documented
  back-reference form.
- NIP-4e's proposal URL was cited in the 2026-07-15 issue and its status has not changed, so
  the paragraph now points at that earlier coverage and names the proposal without re-citing
  the pull request.
- Concord PR #18 is retained deliberately as the one permitted reuse, because it is a real
  status transition. The paragraph states the earlier coverage and the change explicitly:
  "covered previously in last week's issue as an open proposal, has now merged on 15 August."
  The second occurrence, in the Vector section, was rewritten to link the Concord repository.

## Manual read of the three previous issues

#35 (2026-08-12), #34 (2026-08-05), and #33 (2026-07-29) were read in full. Findings:

- No project appears in #36 on the same release, pull request, commit, or signed-event URL
  used in any of those issues.
- Eighteen already-covered items from the shared fetch window were dropped before drafting;
  they are enumerated in `triage_2026-08-19.md`.
- Every repeated project carries both a distinct source and a distinct user-facing or
  protocol-facing change, tabulated in `selection_review_2026-08-19.md`. Spot checks: Amber
  moves from grouped-permission presentation to what the signer will authorize at all; Nostria
  moves from community administration to podcast publishing and relay counting; ClipRelay moves
  from reconnection to credential handling and pairing; Mostro moves from the encrypted chat
  envelope change to the rumor-identifier defect inside gift wrap.
- No version-only entry and no "incremental follow-up" pointer reached a section. Jumble
  v26.8.2 was cut precisely because its distinct change could not be stated beyond reliability.

## Full-archive check

`data/coverage_history.json` was rebuilt this run (362 projects across 35 newsletters) and
consulted for every selected project. Sonar was last covered in #22, NYM in #29, Morganite in
#26, and Cambium only as a project note in #31, so none of those are near-duplicates.

GATE: PASS (continuity checker PASS after resolving seven reused sources; three prior issues read in full; one deliberate reuse, Concord PR #18, carries an explicit merged-status transition; 18 already-covered items dropped pre-draft)
