# Selection Validation — 2026-08-12

Stage: 4 Selection
Review model: four independent selection reviews, run as separate isolated agent turns
Current status: four reviews complete; all findings resolved

## Reviewer 1 — continuity, scoring, and allocation

Initial verdict: FAIL.

Findings:

1. Unchanged NIP PR URLs #2430, #2429, #2428, #2421, and #2303 were already explained in prior issues.
2. Standing protocol-family repository links were incorrectly included in a global “zero URL reuse” claim.
3. nostrord releases were scored 4/12 in curation but selected at 7/12 and duplicated across Releases and In Development.
4. nostr-wot-extension and Cliprelay were incorrectly described as first archive mentions.

Applied deltas:

- Removed unchanged repeated NIP PRs from the selected issue. Retained only genuinely new proposals/status transitions, including the explicit closed-unmerged transition for #2378.
- Limited the zero-reuse claim to selected project release/PR sources and documented the mandatory status-sweep exemption.
- Removed nostrord’s release aggregate and selected it once under the repository-required In Development section through merged PR #250.
- Corrected prior-coverage notes for nostr-wot-extension (#31) and Cliprelay (#32).

Resolution: PASS after revision.

## Final interest, continuity, and duplicate-link audit

Initial verdict: FAIL.

The final mechanical rerun found that the earlier PASS was inaccurate: nine repeated protocol URLs failed the all-history continuity checker, the paragraph-source checker found ten unsupported prose blocks, and exact URL extraction found three repeated destinations. Primary-source inspection then showed that seven NAP proposals had no commits in the issue window, four more NAP proposals repeated prior coverage, NWC PR #2 had already been covered after merging, and Concord PRs #13/#14 repeated last week's merged work.

Applied deltas:

- Removed the entire metadata-only NAP proposal list, the repeated NWC paragraph, and repeated Concord #13/#14 paragraphs.
- Retained NIPs #2378 and Concord #12 only as explicit open-to-closed status transitions, and retained Concord #15 as genuinely new merged work.
- Added distinct primary-source links to every factual prose paragraph.
- Removed every unintended duplicate destination while preserving the opening site link and closing project link as different destinations.
- Kept the canonical H2 order required by NewsletterAgent: Top Stories, Tagged Releases, In Development, Protocol and Spec Work, and NIP Deep Dive.

Resolution: PASS after the corrected draft passed the actual continuity, paragraph-source, style, event, duplicate-destination, topic-backlink, link-reachability, build, and whitespace gates.

## Reviewer 2 — protocol, rotation, topics, and discovery

Initial verdict: FAIL.

Findings:

1. NIP-32 was already deep-dived under a lowercase heading in #26; the case-sensitive rotation scan missed it.
2. One Divine implementation did not meet the rule requiring three independent implementation sources per deep-dive NIP.
3. Concord’s existing topic page was missed.
4. The validation artifact did not yet exist.

Applied deltas:

- Re-ran rotation with case-insensitive headings and rejected previously used NIP-32 and NIP-78.
- Selected merged NIP-09 and NIP-56, neither previously deep-dived.
- Added four current implementation pointers for NIP-09 (Divine, strfry, Amethyst, nostrord) and four for NIP-56 (Divine, Conduit, nostrord, Amethyst).
- Corrected the topic audit to use `content/en/topics/concord-protocol.md`.
- Created this durable validation artifact.

Resolution: PASS after revision.

## Reviewer 3 — scope and section boundaries

Initial verdict: FAIL.

Findings:

1. `New Projects` is not an allowed standalone H2 under the repository’s critical section structure.
2. Selected angles included non-Nostr features: Divine captions/clip provenance, Nostria clip/profile editing, LaWallet weighted receive routing, and Bray build reproducibility.
3. The selected-structure NIP counts did not match the final filtered set.

Applied deltas:

- Moved Safebox Acorn into Top Stories and updated the final count from 5 to 6.
- Removed the non-Nostr feature lines while preserving the event-, relay-, signer-, and protocol-facing changes.
- Corrected the structure to 3 selected open NIP PRs, 2 closed-unmerged transitions, and 1 merged documentation commit.

Resolution: PASS after revision.

## Reviewer 4 — terminal gate and adversarial recheck

Initial verdict: FAIL, limited to gate evidence and count wording.

Findings:

1. This artifact still carried PENDING placeholders while Selection already claimed PASS.
2. The durable spec artifact contains 10 PR records: 8 open and 2 closed. Final Selection retains 5 PRs: 3 open and 2 closed-unmerged transitions.

Applied deltas:

- Recorded all four reviews and resolutions here.
- Distinguished the direct open-PR query (nine results) from the durable spec sweep (10 records: eight open, two closed) and the continuity-filtered selection (five PRs: three open, two closed).
- Ran the mechanical checks below before synchronizing both terminal gates.

Resolution: PASS after revision.

## Mechanical checks

```text
CHECK continuity: selected release/PR URLs=27 archive_hits=1 unallowed=0
allowed_transition_hits: https://github.com/nostr-protocol/nips/pull/2378
CHECK rotation: headings=44 nip09_prior=False nip56_prior=False
CHECK count Top Stories: 6
CHECK count Tagged Releases: 7
CHECK count In Development: 3
CHECK spec families: 7
CHECK published active families: NIPs and Concord
CHECK duplicate URL destinations: 0
CHECK terminal gate: GATE: PASS — 6 Top Stories, 7 Tagged Releases, 3 In Development items, substantive NIP and Concord activity, and 2 non-rotated merged NIP deep dives
```

- Continuity: the one archive hit is PR #2378, explicitly allowed only because its state changed from open to closed-unmerged on 2026-08-09. No other selected release/PR URL appears in the archive.
- Rotation: case-insensitive scan includes lowercase historical headings and confirms no prior NIP-09 or NIP-56 deep dive.
- Implementation: NIP-09 and NIP-56 each have at least three independent current implementation links in Selection.
- Discovery: five candidates were checked and none met canonical ownership/current-release requirements.
- Topic audit: existing NIP-09, NIP-56, Marmot, and Concord pages are recorded; missing project pages are queued.
- Integrity: `git diff --check` returned no output for all three Stage 4 artifacts.

GATE: PASS — independent selection reviews plus the final interest/continuity audit are complete; every critical finding is resolved with mechanical evidence
