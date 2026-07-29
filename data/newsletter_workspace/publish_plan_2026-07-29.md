# Publish plan — 2026-07-29

PR: #117 (https://github.com/andotherstuff/nostr-compass/pull/117)
Draft path: `content/en/newsletters/2026-07-29-newsletter.md`
Bunker config: `~/.config/compass-publish/bunker.json`
Compass author: `npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923`
Approved: Kanban task `t_ed0f1dbf` was explicitly promoted for publication.

## Pre-publish verification

- PR #117 is open, draft, clean, mergeable, and its build check passes.
- Review handoff and all five evidence-bearing reviewer artifacts pass.
- GitHub authentication and both bunker credential files are present.
- `bun scripts/publish.ts --no-inject` parses the issue.
- Publish preview resolves 21 project identities.
- `pakstr` and `swift-nostr` remain unresolved after repository, profile, NIP-05, relay-search, and project-site checks; no identity was guessed. Publication approval accepts omission of their inline npub mentions via the documented `--force` path.
- `bun test publish tests/publish_mentions.test.ts`: 13 pass, 0 fail.
- `bun run build`: Hugo and Pagefind pass after providing the Bun installation's `bunx` compatibility symlink on `PATH`.
- Existing pre-publication outreach receipts remain authoritative; no duplicate DMs will be sent.

## Plan

1. Set `draft: false`, commit, push, and mark PR #117 ready.
2. Squash-merge PR #117 into `main`.
3. Wait for the production GitHub Pages deployment and verify the live issue.
4. Generate canonical long-form content with absolute links and verified npub injection.
5. Sign and broadcast the kind `30023` article through the Amber bunker.
6. Sign and broadcast the kind `1` opening digest with the article `naddr`.
7. Read both event IDs back from independent configured relays.
8. Record the publish log and complete the pipeline task so translation and podcast prep are promoted.

GATE: PASS (explicit publication approval received; preflight completed 2026-07-29T12:43:07Z)
