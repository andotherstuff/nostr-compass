# Compass Newsletter → Nostr Publishing Pipeline

> **Manual invocation only.** This pipeline runs only when the operator types
> the publish command. It must not be triggered from cron, file watchers,
> hooks, slash-commands, or scheduled tasks. The script enforces this by
> checking the `COMPASS_PUBLISH_INVOCATION` environment variable and aborting
> if it is not set to `manual`.
>
> **Two safety gates.** Stage 4 (broadcast) refuses to run without
> `--really-broadcast`. Stage 5 (merge) refuses to run without `--really-merge`
> and a ledger entry showing at least one successful relay receipt. Pass both
> flags with `--stage all` to do a full publish + GitHub merge in one shot.

## What it does

Takes a prepared newsletter file (the output of `scripts/publish.ts` saved
as `/tmp/{N}publish.md`), splits it into the canonical 4 blocks, signs a
NIP-23 long-form event (kind 30023) and a top-level kind:1 digest
through an Amber bunker over NIP-46, broadcasts both events to the
configured relay set, and squash-merges the newsletter PR on GitHub so the
Hugo deploy publishes the newsletter to the website.

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
2. **SIGN** — requests a bunker signature for the kind 30023 article.
   Writes `out/{N}/event.json`. The article body is the newsletter body
   and only the body — no banner attribution or announcement prefix.
3. **ANNOUNCE-SIGN:** composes a kind:1 digest from the article's complete
   opening section (top-level, no reply tags, no hashtags) with a
   `nostr:naddr1...` reference to the article. Requests a bunker signature. Writes
   `out/{N}/announcement.json`.
4. **BROADCAST** — gated by `--really-broadcast`. Broadcasts both signed
   events to every relay in `config/relays.json`, writes per-relay
   receipts to `out/{N}/receipts.json`, and appends an entry to
   `published.json` recording which relays accepted.
5. **MERGE** — gated by `--really-merge` AND the broadcast ledger showing
   at least one ok relay. Reads the current git branch, finds the open PR
   on GitHub for that branch, verifies it is mergeable + checks-passing,
   squash-merges with `--delete-branch`. Hugo deploy fires from main and
   the newsletter goes live on the website. Writes `out/{N}/merged.flag`
   so the step is idempotent.
6. **LOG** — generates `data/newsletter_workspace/publish_log_{date}.md` from
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

The pipeline posts one line per milestone (broadcast, merged, logged, and any
halt) to the configured notification target. That target is already the
single producer for this project's outcomes, so the pipeline posts into it
instead of adding a second cron producer — AGENTS.md § "One producer owns each
recurring report".

- config: `config/notify.json` (`enabled`, `target`)
- `COMPASS_NOTIFY=0` silences a run; `COMPASS_NOTIFY_TARGET` overrides the target
- each (issue, milestone) sends at most once, tracked in `out/<n>/notified/`
- a failed send is logged to stderr and never fails the publish
- forge references are full Markdown links, per `MARMOT_MESSAGE_MARKDOWN.md`

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
| `config/notify.json` | yes | Milestone notification target and on/off switch |
| `~/.config/compass-publish/bunker.json` | NO | Bunker URI from Amber. Contains a one-time secret. Never commit. |

## Usage

```bash
# Add this to your .bashrc once:
alias compass-publish='COMPASS_PUBLISH_INVOCATION=manual bun publish/publish.ts'

# Then for a publish:
compass-publish 27                                                # dry-run: stops before broadcast
compass-publish 27 --stage all --really-broadcast --really-merge  # full publish + merge PR
compass-publish 27 --stage parse                                  # single stage
compass-publish 27 --stage sign                                   # one Amber approval
compass-publish 27 --stage announce-sign                          # one Amber approval
compass-publish 27 --stage broadcast --really-broadcast           # post to Nostr only
compass-publish 27 --stage merge --really-merge                   # merge PR only (after broadcast)
compass-publish 27 --stage log                                    # record the publication log, open its PR
compass-publish 27 --stage log --no-log-pr                        # write the log without committing
COMPASS_NOTIFY=0 compass-publish 27 --stage log                   # no milestone message
COMPASS_DIR=/path/to/worktree compass-publish 27 --stage log      # run against another working tree
```

**Both flags should be passed together for a normal publish.** Broadcasting
without merging leaves the newsletter on Nostr but invisible on the website
until the PR is merged. This is what happened with Newsletter #27 on
2026-06-17 — Nostr had the article 19 hours before the website did.

The positional argument is the newsletter number. The pipeline derives the
input file from `/tmp/{N}publish.md`.

## Safety

- The script refuses to run unless `COMPASS_PUBLISH_INVOCATION=manual`.
- The script refuses to sign unless the bunker's signing pubkey matches
  the author npub configured in `config/author.json`.
- Stage 4 (broadcast) refuses to run without `--really-broadcast`.
- Stage 5 (merge) refuses to run without `--really-merge` AND a broadcast
  ledger entry showing at least one ok relay. It also refuses to run if
  the current git branch is not `newsletter/*` or if the PR is not in a
  clean mergeable state on GitHub.
- `out/` is gitignored. Only the README, configs, and `published.json`
  are committed.

## Build status

| Stage | Status |
|-------|--------|
| 1. PARSE | shipped |
| 2. SIGN (article kind 30023) | shipped |
| 3. ANNOUNCE-SIGN (kind:1 root) | shipped |
| 4. BROADCAST | shipped; gated by `--really-broadcast` |
| 5. MERGE | shipped; gated by `--really-merge` + broadcast ledger |
