# Compass Newsletter → Nostr Publishing Pipeline

> **Scheduled mutation is receipt-gated.** Wednesday publication prepares one
> exact PR/head/base/prospective-tree candidate before 16:00 UTC. Merge requires
> the scoped edition authorization, current hold version, source digest,
> feedback snapshot, review receipts, and exact-head CI. It then verifies the
> attributable production deployment before signing or broadcasting. The
> `--really-*` flags confirm execution intent; they never grant authority.

## What it does

Takes a prepared newsletter file (the output of `scripts/publish.ts` saved
as `/tmp/{N}publish.md`), splits it into the canonical 4 blocks, signs a
NIP-23 long-form event (kind 30023) and a top-level kind:1 digest
through an Amber bunker over NIP-46. It first merges the exact prepared
newsletter PR and verifies its attributable Hugo deployment and served content,
then signs and broadcasts both events to the configured relay set.

## Source format

Compass uses the prepared output of `scripts/publish.ts`, written
to `/tmp/{N}publish.md`. The file is structured as four blocks separated by
blank lines:

```
Nostr Compass #N

[21-word TL;DR]

[banner image URL — same for every newsletter]

[newsletter body, npub-injected, absolute URLs]
```

Optional 5th block (recommended): `Tags: foo, bar, baz`, comma-separated,
≤6 tags. The article kind 30023 picks them up as `t` tags. The kind:1
announcement carries no `t` tags by design.

The kind:1 text is derived mechanically from the newsletter opening. The
pipeline takes every paragraph before the first horizontal rule or H2,
removes the generic welcome line, strips markdown link wrappers while keeping
their labels and inline `nostr:npub` mentions, adds a short prose introduction,
and appends the article `nostr:naddr`. Do not write a separate announcement.

The banner image URL is pinned in `config/cover.json` to keep every
newsletter under the same brand image. The pipeline verifies the URL in
the file matches the configured one and warns on mismatch.

## Pipeline stages

1. **PARSE:** read `/tmp/{N}publish.md`, split into 4 blocks, validate
   the 21-word TL;DR, validate the banner URL, parse optional Tags line.
   Writes `out/{N}/metadata.json` and `out/{N}/article.unsigned.json`.
2. **MERGE PREPARE/COMMIT:** consumes the explicit PR number, head SHA, and base
   SHA; computes and records the prospective merge tree under the server
   current-base guard. The mutation pass requires the identical prepared tree,
   scoped edition authorization, source/feedback/review receipts, and exact-head
   CI, then merges with the expected-head precondition and verifies the result.
3. **DEPLOY:** selects the Pages run attributable to the confirmed merge SHA and
   verifies the canonical page serves the expected merged content.
4. **SIGN:** after deployment confirmation, requests an Amber bunker signature
   for the kind 30023 article and writes `out/{N}/event.json`.
5. **ANNOUNCE-SIGN:** composes the kind:1 digest with the article naddr, requests
   the second authorized signature, and writes `out/{N}/announcement.json`.
6. **BROADCAST:** gated by `--really-broadcast` and exact merge/deploy evidence.
   Broadcasts both signed events, records per-relay receipts, and independently
   recovers the exact events from the required durable relay floor.
7. **LOG:** generates `data/newsletter_workspace/publish_log_{date}.md` from
   this run's receipts, ledger, the Pages deploy for the merge commit, and a
   fresh exact-id relay readback, then opens a `chore/publish-log-{date}` PR.
   See "Publication evidence" above. `--no-log-pr` skips the commit.

Each stage reads from disk, writes to disk, and is independently
re-runnable. A crash between stages does not lose progress.

## Publication evidence: the `log` stage

The publication log used to be written by hand, and both ways of getting that
wrong happened within two issues: #36 shipped with no log, and #37's first log
named a relay-config file that does not exist (`data/compass_relays.txt`) and
reported readback from an ad-hoc probe rather than the run's own receipts.

The `log` stage derives `data/newsletter_workspace/publish_log_<date>.md` from
artifacts only:

- per-relay acceptance and rejection reasons from `out/<n>/receipts.json`
- event ids and timestamps from `published.json` and `out/<n>/*.json`
- the Pages deploy matched to the **merge commit** (a later unrelated deploy on
  `main` must not be credited to this publication), preferring the
  `push`-triggered run over a manual rerun
- a fresh exact-id readback against every durable relay that accepted, with the
  write-only NIP-66 blaster excluded from readback evidence
- the pre-publication gate files, reported as they read rather than asserted

It ends in a `GATE:` line. `GATE: FAIL` means nothing accepted the events or
nothing serves them back — the issue is not safely published. Do not hand-edit
the log to make it pass. `--no-log-pr` writes the log without committing.

The stage is idempotent: re-running reuses the existing
`chore/publish-log-<date>` PR rather than opening another. It also archives the
signed events to `data/newsletter_workspace/published/<date>_{30023,1}.json`.

## Milestone notifications

Repository publication and translation code never sends user-facing milestone
messages. The host-owned durable outbox/reconciler is the sole notification
producer. It observes committed workflow state and owns logical identities,
retries, routing, connector acknowledgement, and delivery readback. This keeps
publication side effects independent from message transport and prevents a
repository retry from creating duplicate chat output.

## Paths

Every path is resolved from the module location (`import.meta.dir`), never from
the working directory or a hardcoded home. The pipeline therefore behaves the
same however it is invoked. `COMPASS_DIR` overrides the repo root when the
working tree lives somewhere else, such as a per-issue worktree.

## Configuration

| File | Committed | Purpose |
|------|-----------|---------|
| `config/relays.json` | yes | Relay set for broadcast |
| `config/author.json` | yes | Author npub + hex pubkey |
| `config/cover.json` | yes | Pinned banner image URL (verified per publish) |
| `~/.config/compass-publish/bunker.json` | NO | Bunker URI from Amber. Contains a one-time secret. Never commit. |

## Usage

```bash
# Add this to your .bashrc once:
alias compass-publish='bun publish/publish.ts'

# Then for a publish:
compass-publish 27 --dry-run                                      # zero-mutation preview
compass-publish 27 --stage merge --pr-number 123 --head-sha <sha> --base-sha <sha> --page-url <url>
compass-publish 27 --stage merge --really-merge                   # only after the identical prepared candidate passes
compass-publish 27 --stage deploy                                 # verify attributable production deployment
compass-publish 27 --stage parse                                  # single stage
compass-publish 27 --stage sign                                   # one Amber approval
compass-publish 27 --stage announce-sign                          # one Amber approval
compass-publish 27 --stage broadcast --really-broadcast           # only after exact deploy verification
compass-publish 27 --stage log                                    # record the publication log, open its PR
compass-publish 27 --stage log --no-log-pr                        # write the log without committing
COMPASS_DIR=/path/to/worktree compass-publish 27 --stage log      # run against another working tree
```

The normal scheduled flow prepares the exact merge candidate before 16:00, then
runs merge, deploy verification, signing, broadcast, relay recovery, and log as
separate restart-safe effects. Never broadcast first and never infer the PR from
the checkout's current branch.

The positional argument is the newsletter number. The pipeline derives the
input file from `/tmp/{N}publish.md`.

## Safety

- The script refuses to sign unless the bunker's signing pubkey matches
  the author npub configured in `config/author.json`.
- Merge requires a previously prepared identical PR/head/base/prospective-tree
  candidate plus scoped authorization and current source, feedback, review, hold,
  and exact-head CI evidence.
- Signing and broadcast require confirmed exact merge and deployment evidence.
- Broadcast refuses to run without `--really-broadcast`; merge refuses to mutate
  without `--really-merge`. These switches never substitute for authority.
- `out/` is gitignored. Only the README, configs, and `published.json`
  are committed.

## Build status

| Stage | Status |
|-------|--------|
| 1. PARSE | shipped |
| 2. MERGE | shipped; exact prepared identity + authorization/evidence gated |
| 3. DEPLOY | shipped; attributable merge SHA and served-content verification |
| 4. SIGN (article kind 30023) | shipped; post-deploy only |
| 5. ANNOUNCE-SIGN (kind:1 root) | shipped; post-deploy only |
| 6. BROADCAST | shipped; gated by `--really-broadcast` + merge/deploy evidence |
| 7. LOG | shipped; acceptance and independent relay recovery evidence |
