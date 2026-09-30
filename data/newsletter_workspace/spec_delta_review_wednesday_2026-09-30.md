# Wednesday specification delta review

These are explicit editorial dispositions for three newly retained current-pass specification sources. Primary PR metadata is bound to the finalized specs artifact; detailed discussion and implementation findings are supplied by the owning specification reviewer. None is claimed adopted, merged, or deployed.

Axes: Nostr significance, user/operator impact, novelty, evidence maturity, explanatory value.

## PR 2490: README ordering — SKIP
The September 30 PR moves the NIP-A3 README entry into list order. It supplies no new wire format, deployed behavior or substantive Nostr capability. Score 1/10: direct proposed documentation edit, no material protocol delta.
Primary: https://github.com/nostr-protocol/nips/pull/2490
Scores: {'nostr_significance': 0, 'user_operator_impact': 0, 'novelty': 0, 'evidence_maturity': 1, 'explanatory_value': 0}

## PR 1985: Preferred relay list proposal — SKIP
The proposal was opened July 23, 2025. Current-window activity merges master into the existing proposal; no newly verified proposal or implementation milestone is established. Score 2/10: readable source proposal but no material in-window novelty.
Primary: https://github.com/nostr-protocol/nips/pull/1985
Scores: {'nostr_significance': 0, 'user_operator_impact': 0, 'novelty': 0, 'evidence_maturity': 1, 'explanatory_value': 1}

## PR 2489: Hidden replies set proposal — INCLUDE
New September 29 NIP-51 proposal introduces a hidden replies set using kind 30027. Discussion leaves format details unresolved. The author claims a Nostrich implementation; review of 594 public source files did not verify kind 30027 support in that inspected source. This does not establish that no implementation exists. Score 8/10: reviewable new Nostr proposal milestone (significance2, impact1, novelty2, maturity1, explanatory2). The actual specification draft supplies primary evidence independently of its unverified implementation claim.
Primary: https://github.com/nostr-protocol/nips/pull/2489
Scores: {'nostr_significance': 2, 'user_operator_impact': 1, 'novelty': 2, 'evidence_maturity': 1, 'explanatory_value': 2}

## Detailed primary reviewer evidence
Actual saved report: `/opt/data/tmp/compass_specs_late_20260930/decisions.md` at `918c737399d32e5edddb7baaaf35f73db022b2d80758a4cf64199d4e4651b7f6`.
# Late specification decisions: September 30, 2026

## Result

PR2489 meets the issue's 8/10 inclusion threshold as a reviewable proposal milestone. PR2490 and PR1985 remain below threshold. These decisions follow full proposal diffs, live PR state, commit history, primary README, and a fixed public implementation snapshot. No article or ledger was edited.

| Candidate | Decision | Score | Concrete reason |
|---|---|---:|---|
| [NIPs PR2490](https://github.com/nostr-protocol/nips/pull/2490) | Skip | 1/10 | Moves the existing NIP-A3 README entry into text order. The full diff changes no specification or behavior. |
| [NIPs PR1985](https://github.com/nostr-protocol/nips/pull/1985) | Skip | 2/10 | An open proposal from July 2025. September 29's new commit merges master into the existing branch. The latest non-merge proposal edit dates to August 2025; recent activity does not establish new functionality or adoption this week. |
| [NIPs PR2489](https://github.com/nostr-protocol/nips/pull/2489) | Include | 8/10 | A genuinely new, reviewable thread-moderation proposal with concrete relay semantics and explanatory value. Scope as an open proposal, attribute the implementation claim, and preserve the unresolved design discussion. |

## PR2489: novelty and exact state

The proposal was created September 29 at 18:46:20 UTC and remains OPEN at head `ace81d7e534c82a63f7f49e96330370f7b654ee7`. It proposes one addressable kind-30027 event per thread, using the root ID as the `d` tag and public `e` tags to identify replies. Only a set signed by the root's author applies. Listed replies and their descendants are hidden behind a disclosure; listing the root hides other authors' replies and asks clients to disable their composer. It does not prevent anybody publishing a reply to a relay.

The first commit used a single replaceable kind-10022 list. In-window feedback raised contention across clients/devices; the next commit changed the design to per-thread sets. The latest public response still suggests random `d` values or a separate/NIP-22 design, so the current root-ID format is not an agreed interoperability surface.

The author explicitly states **“Implemented in Nostrich.”** This claim remains part of the evidence. The investigation does not establish that no implementation exists.

## Public Nostrich implementation check

The live repository is [nostrichOS/nostrich-client](https://github.com/nostrichOS/nostrich-client). Its only published branch is `main`, at `d693ab84544beb810e75577080c679e735fe26d5`, committed September 24 at 03:00:54 UTC. The branch list and PR list were both exhausted; the repository has no public pull requests. The fixed-head source archive is 1,301,210 bytes. All 594 TypeScript, TSX, Markdown, and JSON files were retained and hashed, including the primary README.

Source searches for `30027`, `10022`, author hidden-reply sets, reply closure, and comparable semantics did not identify the proposed protocol in that public snapshot. Named runtime paths were then read rather than relying solely on text search:

- [`apps/web/lib/thread.ts`](https://github.com/nostrichOS/nostrich-client/blob/d693ab84544beb810e75577080c679e735fe26d5/apps/web/lib/thread.ts) queries short-note and NIP-22 comment kinds, collects thread ancestry/replies, and exposes them to the UI. Its thread queries do not load root-author kind-30027 sets.
- [`ThreadScreen.tsx`](https://github.com/nostrichOS/nostrich-client/blob/d693ab84544beb810e75577080c679e735fe26d5/apps/web/components/ThreadScreen.tsx) folds advertising, low-signal profiles, and the reader's own muted content. Its “hidden replies” disclosure is therefore reader filtering in this snapshot, not proof of the proposed root-author moderation protocol. It renders the reply composer without the proposed root-set closure gate.
- `ReplyComposer.tsx` signs and publishes NIP-10 replies/NIP-22 comments. `user-lists.ts` stores the reader's own mutes and filters. `signer-perms.ts` lists published kind permissions without kind 30027. These findings support the bounded verification result and do not rule out an unpublished implementation or different deployment.

The policy admits reviewable proposal milestones. Score axes: Nostr significance 2, user/operator impact 1 (prospective), novelty 2, evidence maturity 1 (reviewable open proposal; implementation claim not publicly established), explanatory value 2. Total 8/10, no zero axis. Include a short proposal paragraph; the public implementation verification limit constrains its claims. The earlier provisional 7/10 score underweighted explanatory value and is superseded by this policy-based axis assessment.

## PR1985: established historical implementation, no fresh milestone

The proposal adds preferred Indexer, Proxy, Broadcast, and Trusted relay lists, kinds 10086–10089. The author reported Amethyst support in August 2025, and another participant described upcoming applesauce/noStrudel support in May 2026. Those historical implementation claims should not be erased or called unimplemented. The September 29 merge of master supplies no new implementation milestone for the newsletter window. The PR remains OPEN at `f4635984e8c2e091dc12189ed9ed212ec0d4fce8`.

## Evidence files

`exact_raw.json` retains full live PR bodies, commit histories, review discussion, Nostrich README, and default head. `branches_raw.json` retains exhausted public branch/PR connections. `pr2489.diff`, `pr1985.diff`, and `pr2490.diff` retain the complete proposal diffs. `nostrich_source_manifest.json` hashes all retained text files. `final_state_raw.json` and `final_state_receipt.json` provide the final exact live state and query timestamps. `decisions.json` records machine-readable dispositions and evidence hashes.

## Proposed paragraph for PR2489

### A NIP-51 proposal gives thread authors public reply controls

An [open NIP-51 proposal](https://github.com/nostr-protocol/nips/pull/2489) would let a thread's author publish a public hidden-replies set that cooperating clients display behind a toggle. It uses one addressable kind-30027 event per thread, with the root ID as its `d` tag and `e` tags naming replies; only a set signed by the root's author applies. Listing the root asks clients to hide other authors' replies and stop offering a reply composer, while replies can still be published on relays. The per-thread format limits editing collisions to the same conversation. The author reports an implementation in Nostrich, but public-source inspection did not establish it; the proposal remains unmerged, with its set format still under discussion.
