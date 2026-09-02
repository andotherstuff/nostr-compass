# Pre-publication refresh — Newsletter #38 (2026-09-02)

Recorded: 2026-09-02T17:49Z. This is the final evidence-bearing verifier
refresh. It supersedes the provisional 16:49 UTC readback, which described the
then-current two-commit remote branch. No publication side effect occurred
during this refresh.

## Authoritative final state

- Draft PR: https://github.com/andotherstuff/nostr-compass/pull/147
- Newsletter-content head before this evidence-only amend:
  `ed86b05c2e2ee2b56fc9a39d74b2e262ffce3b8a`. The authoritative final PR
  head is read back after the amend and recorded on the durable verifier task;
  it cannot be embedded inside the commit whose hash it determines.
- PR readback: OPEN, `draft: true`, MERGEABLE, exactly one commit.
- Required CI on that exact head: `build` COMPLETED/SUCCESS; `deploy`
  COMPLETED/SKIPPED as expected for a draft.
- The finalized English Markdown is byte-identical to the preflighted Marmot
  attachment: SHA-256
  `983b3798a8e459add41d138e113bdc02dab5fadc1fbfb73b14595a9c6f777f52`,
  38,944 bytes.

## Source and editorial reconciliation

- All ten source families were resolved. The transient spec-family `gh` exit
  75 was retried successfully, producing
  `data/spec_updates/spec_updates_2026-09-03.json`. The Zapstore relay crawl
  completed successfully after correcting the summary renderer, producing
  1,354 releases and 548 Nostr-relevant candidates.
- Required late findings are integrated: Voca's verified Nostr relay fetching,
  event-id/signature validation, event reading, npub-to-kind-30023 queue
  subscription, and the 1.1.0 follow-up; MDK v0.9.17; merged NIP-67 `auth`
  hints; and the merged NIP-84 tag-scheme update.
- Assembled newsletter, section artifacts, selection/triage evidence, project
  tracking, and affected topic backlinks are synchronized.
- Release-digest triage reports zero untriaged high-signal releases.

## Exact-final gates

All were rerun after the last newsletter edit and passed:

- style / anti-slop
- continuity against prior English issues
- prose paragraph primary-source links
- event-example validation
- release-digest triage coverage
- production `bun run build`
- rendered topic backlinks: 28 topic pages and 30 backlinks
- live validation of the newly added NIP and Voca links

## Explicit hold disposition

All four conditions in `publication_hold_2026-09-02.md` are satisfied. The
canonical Compass Marmot group received the exact finalized English Markdown
under digest-idempotent delivery. Canonical message id:
`e73c81238643dea226819310cf7f071efa7a8186705a201ed6cdeef9b0515cde`.
Timeline readback proved the exact caption, `attachments_truncated=false`, and
exactly one attachment named `2026-09-02-newsletter.md`.

No merge, deploy, signing, Nostr event creation, or relay broadcast occurred
during this verifier refresh.

GATE: PASS (newsletter content unchanged since ed86b05c; authoritative post-amend PR readback must remain OPEN/draft/mergeable with exactly one commit and green CI; all editorial/build/triage/topic gates green; exact finalized Markdown durably confirmed in canonical Compass Marmot message e73c8123)
