# Stage 7 review log — Newsletter #36 (2026-08-19)

Consolidates the five reviewer artifacts for the 2026-08-19 issue. Each reviewer ran its own
checks against the assembled draft; the evidence in every gate line below is copied from the
artifact that produced it.

| Reviewer | Artifact | Result |
|---|---|---|
| LinkChecker | `review_links_2026-08-19.md` | GATE: PASS (165/165 external links HTTP 200 on 2026-08-18; 27/27 topic targets and 2/2 newsletter targets exist; 27/27 rendered backlink fragments resolve) |
| ClaimCheck | `review_claims_2026-08-19.md` | GATE: PASS (24 source audits against complete primary notes; 41/41 cited pull requests verified MERGED; 25 NIP identifiers resolved live; NIP-4e correctly framed as unmerged) |
| ProseReview | `review_prose_2026-08-19.md` | GATE: PASS (style, paragraph-link, and month-end checkers PASS; anti-slop scanner 100/100 zero violations after re-run; 0 em dashes, 0 banned intensifiers) |
| TopicAudit | `review_topics_2026-08-19.md` | GATE: PASS (production build exit 0; 27/27 topic pages carry Primary sources and a validated #36 fragment; 0 NIP-to-topic mismatches) |
| ContinuityValueCheck | `review_continuity_2026-08-19.md` | GATE: PASS (continuity checker PASS after resolving seven reused sources; three prior issues read in full; one deliberate reuse with an explicit status transition) |

## Review rounds

**Round 1** produced four failures, all of which were fixed rather than waived:

1. `check_newsletter_paragraph_links.py` reported fourteen paragraphs with no primary-source
   link, concentrated in the Citrine section and both deep dives. Specification and release
   links were added to each; the checker then passed, and a later edit reintroduced one failure
   in the Divine Mobile section which was also fixed.
2. `check_newsletter_continuity.py` reported seven reused primary-source URLs. Five became
   internal back-references to the 2026-08-12 issue, one dropped a stale proposal citation, and
   one, Concord PR #18, was rewritten to state its merge transition explicitly.
3. The anti-slop scanner returned 98/100 with two three-item-list findings in the opening
   digest. Both clauses were restructured and the scanner was re-run to 100/100.
4. `scripts/publish.ts` reported eight unresolved project names. Two were heading-parsing
   artifacts fixed by rewriting the headings so the project name leads, and the rest were
   resolved through identity research or recorded as researched-unresolved.

**Round 2** re-ran every check against the corrected draft. All five reviewers pass with no
outstanding fix-list items.

**Round 3 (2026-08-18, post-handoff)** followed owner feedback that Nail was missing. The project
was verified from source, added to the current issue through the mid-week intake path, and every
gate above was re-run afterwards: the counts in this table are the post-Round-3 figures. Two
pipeline defects were found and fixed in PR #136 rather than worked around; see
`review_human_2026-08-18T1600Z.md`.

## Identity and outreach preview

`bun scripts/publish.ts --no-inject` resolves **18 projects**, leaves **0 missing**, and records
**2 researched-unresolved** entries (Concord, Nostter). `bun run check:npubs` reports 325
entries, 0 errors, and the 2 pre-existing legacy warnings.

The eighteenth is Nail, which only resolves once `scripts/publish.ts` recognises the
`Newly Discovered` heading. That allowlist held `new projects` but not the heading the archive
actually uses, so every project introduced under it was dropped from mentions and from outreach.
Pact received no DM in #35 for exactly this reason. Fixed in PR #136.

Three projects newly bound this issue (Cambium, Bark, Toll Booth) plus nwc-kit share the
forgesworn key already verified for Bray, so they de-duplicate to a single recipient. NYM is
bound to its lead developer's key with the role recorded, not presented as a project account.
Glow, Concord, and Nostter carry documented negative research and stay untagged.

## Draft state

The draft remains `draft: true`. No merge, deployment, signing, or Nostr broadcast has occurred.

GATE: PASS (all five reviewer artifacts end in evidence-bearing PASS after two rounds; 0 outstanding fix-list items; draft remains unpublished)
