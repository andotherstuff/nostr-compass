# Stage 0 pre-flight — Newsletter #36 (2026-08-19)

Run started 2026-08-18T14:20Z. Executed manually from the Hermes workspace because the
`compass-tuesday-intake` cron and every downstream Compass job are paused: the OpenRouter
writing lanes (`moonshotai/kimi-k3`, `google/gemini-3.1-pro-preview`) return HTTP 402
`Insufficient credits` (see `/opt/data/KIMI_OPENROUTER_PAUSE.md`, 2026-08-17). No agent
worker could claim the pipeline task, so the stages below were driven directly.

## Repository

- Repo: `andotherstuff/nostr-compass`
- Shared checkout `/opt/data/compass` left untouched (no fetch/switch/reset/clean/stash).
- Isolated weekly worktree: `/opt/data/compass-worktrees/2026-08-19`, created by
  `python3 /opt/data/scripts/compass_weekly_workspace.py 2026-08-19`
  (`{"base": "origin/main", "branch": "newsletter/2026-08-19", "created": true, "queue_copied": true, "shared_checkout_preserved": true}`).
- Branch: `newsletter/2026-08-19`
- Base: `origin/main` at `06046df` ("Add Newsletter #35 publication log (#134)")
- Working tree: clean apart from the Stage 1 intake edit to `data/projects.yml` and the
  workspace-local `link_queue.md` copy plus this run's fetch log.

## Environment

- `gh` 2.96.0, authenticated as `Datawav` (scopes: gist, project, read:org, repo, workflow)
- `hugo` v0.123.7+extended
- `bun` 1.3.14
- Python 3.13.5

## Previous issue and publication proof

Last published English issue: **Nostr Compass #35**, `content/en/newsletters/2026-08-12-newsletter.md`.

Publication proof required before starting a new issue is present and evidence-bearing:

- `data/newsletter_workspace/publish_log_2026-08-12.md` ends with
  `GATE: PASS (PR #133 merged; GitHub Pages deploy passed; canonical page HTTP 200 with issue title; kind 30023 and kind 1 received 12/12 broadcast acceptances and exact-ID independent readback from 11/11 durable relays)`.
- PR [#133](https://github.com/andotherstuff/nostr-compass/pull/133) squash-merged 2026-08-12T16:06:39Z; Pages deploy run 31615932627 succeeded.
- Kind 30023 `cc64af74394bbce58fee0ad28e5b1cf2476afd10ab8e0a314eaac44a526a3bb9` and
  kind 1 `177a8fd90fed7105b3e2d486b307ce3eea098128541b0ffbda474ca2a17ec4da` independently
  recovered from 11 durable relays.

`draft: false` is set on the #35 file and the canonical page is live. The link queue may
therefore be consumed for this issue.

## Open pull requests

`gh pr list --state open` returns an empty list. No newsletter or translation PR is open,
so `newsletter/2026-08-19` starts from a clean base and Stage 8 will open a new draft PR
rather than force-pushing an existing one.

## Target

- Target publish date: **2026-08-19** (`date -u -d "next Wednesday" +%F`)
- Issue number: **#36** (derived from #35's frontmatter title `Nostr Compass #35`)

## Month-end detection

```
2026-08-19 + 7 days = 2026-08-26  → 2026-08 == 2026-08
```

The next weekly slot stays inside August, so this is **not** the final weekly issue of the
month. #36 carries two NIP Deep Dives; the `Six Years of Nostr Augusts` retrospective
belongs to #37 (2026-08-26).

GATE: PASS (worktree on `newsletter/2026-08-19` at `06046df`; #35 publication proof verified; zero open PRs; target 2026-08-19 / issue #36; month-end check returns deep-dive mode)
