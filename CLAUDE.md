# Nostr Compass Newsletter Guidelines

## Writing Rules (CRITICAL — never violate)

These rules supersede general anti-slop guidance. Apply them BEFORE writing prose, not as a post-pass cleanup.

### Source linking is mandatory

**Every mention of a PR, release, commit, or proposal MUST include a direct link the first time it appears in prose.** No "PR #2351 closes [PR #2027]" — both PRs must be linked. No "Amethyst's PR #2968 relaxed the parser" — the PR must be a markdown link to GitHub.

Exceptions (do NOT need linking):
- Version numbers in opening summaries / section headings (e.g., `### Amethyst v1.11.0:` and the opening TLDR paragraph)
- Kind numbers referenced as protocol specifications (e.g., "kind 84 events", "kind:30023 long-form")
- Back-references within the same paragraph to a PR already linked earlier (e.g., "PR #2351, the same proposal" two sentences later)

Rule: if a reader on the published page can't click and reach the source in one hop, the link is missing. Audit every PR/release reference in your final read.

### Banned meta-frames (these phrases trigger the anti-slop scanner)

These are AI-tell phrases that announce what is about to be said instead of saying it:
- "worth flagging" / "worth noting" / "worth tracking" / "worth pointing out" / "worth highlighting"
- "one to watch" / "it bears mentioning" / "it's important to note"
- "the thing to flag here" / "the key takeaway is"

Replacement: state the claim directly. If a tradeoff is worth flagging, name the tradeoff. If something is one to watch, name the specific reason a reader should watch it.

### Banned hyperbole (release/feature superlatives)

Never use:
- "the broadest feature surface of any release this year" / "biggest release to date" / "most active week ever"
- "the first major Nostr client to X" / "the first to ship Y"
- "first-class timeline category" / "with its own surface" (redundant modifiers)
- "premier Nostr X" / "leading Nostr X"

Replacement: state the concrete change. "v1.11.0 adds NIP-52 calendar events" beats "the broadest feature surface of any release."

See `~/.claude/rules/base-antislop.md` §"Superlative claims without specifics" and §"Redundant modifier stacking" for the canonical patterns. Run `bun ~/.claude/skills/_BLOGGING/Tools/AntiPatternScanner.ts <newsletter>` before every PR push — it must return PASS.

### Newsletter section structure (CRITICAL)

Every newsletter MUST follow this section order. The boundary between sections is functional, not editorial — sort each item into the correct bucket based on what it IS, not on how prominent it feels.

1. **Top stories** — multi-PR releases of major projects, architecturally significant new projects, or coordinated multi-repo work that needs flagship treatment.
2. **Releases** — every version-tagged release that didn't qualify for Top stories. One subsection per project, named `### Project vX.Y.Z: short description`. If a release qualifies for Top stories, it does NOT also appear here.
3. **Unreleased changes** — merged PRs that have NOT been bundled into a versioned release. Once these features ship in a release, they move to that release's writeup in a future newsletter. NEVER include unmerged or draft PRs here.
4. **NIP updates and protocol spec work** — every proposal opened against `nostr-protocol/nips`, plus any `kind:30023` long-form NIP proposal circulated this week. This includes PRs from project teams (e.g. Formstr's calendar stack) as well as individual NIP proposals (e.g. Payment Targets, Silent Payments). Each PR or proposal must explain the event kind, tag structure, wire-protocol behavior, and the problem the proposal solves. NIP work from projects always goes here, NEVER in Top stories or Releases, regardless of how flagship the originating project is.
5. **NIP Deep Dives OR History section** — see the month-end rule below.

NEVER add a "Closing notes" or "Closing thoughts" section. The newsletter ends with the deep dives or the history section. Forward-looking commentary belongs inside the relevant section as a single concrete sentence, not in a meta-summary at the end.

### NIP-34 hosting is delivery, not subject matter (CRITICAL — scope rule)

**A repository being hosted via NIP-34 git-over-Nostr does NOT make its subject matter Nostr news.** NIP-34 is the transport for the source code; the project's substance determines coverage.

Out of scope, even with heavy patch volume on `relay.ngit.dev` or a GRASP server:
- CoinJoin coordinators and clients (joinmarket-ng, Whirlpool clones, PayJoin tooling)
- On-chain mixers, Bitcoin Core forks, hardware-wallet firmware
- Pure Lightning/Bitcoin tooling without a Nostr surface
- Tor/I2P relay binaries, generic network infrastructure

In scope:
- NIP-34 tooling itself (ngit, GitWorkshop, ngit-indexer, GRASP servers, gitstr, nostr-git, schemata)
- Any project whose own runtime functionality runs on Nostr

The NIP-34 tracker (`data/nip34_tracked.yml`) MUST only track repositories whose subject matter is itself Nostr-relevant. NIP-34 repos for Bitcoin-only tools are visible in the discovery output but never promoted into `nip34_tracked.yml` and never written into newsletter prose. If a NIP-34 repo's project description names a Bitcoin-only protocol (CoinJoin, PayJoin, BIP-352 silent payments outside a Nostr context, etc.) and the project does not also implement a Nostr surface, the repo fails this gate.

### NIP-34 fetcher access (CRITICAL — wrong-key bug)

`data/nip34_repos/nip34_*.json` stores per-repo activity as `tracked[].activity.patches` and `tracked[].activity.issues`, NOT `tracked[].patches`. The `summary.total_patches_in_period` field is the authoritative count. To enumerate repos with activity:

```bash
jq '[.tracked[] | select(.activity.patches_in_period > 0 or .activity.issues_in_period > 0) | {name: .repo.name, web: .repo.web_urls[0], patches: .activity.patches_in_period, issues: .activity.issues_in_period}]' data/nip34_repos/nip34_*.json
```

NEVER write "the NIP-34 tracker was quiet this week" without first running that exact query AND inspecting the `summary` field. Empty `tracked[].patches` does not mean no activity — it means the field is at the wrong path.

### Month-end history rule (CRITICAL — check BEFORE selecting deep dives)

The LAST newsletter of each calendar month replaces the two NIP deep dives with a comprehensive historical retrospective titled `## N Years of Nostr [Month]s` covering that month's milestones since November 2020.

**Detection (run before drafting):** if the next Wednesday after this newsletter's date falls in a different calendar month, this is the last newsletter of the month — DO HISTORY, NOT DEEP DIVES.

```bash
# Compute next Wednesday after the newsletter date YYYY-MM-DD:
date -d "$(date -d "YYYY-MM-DD +7 days" +%Y-%m-%d)" +"%Y-%m"
# Compare to newsletter's month. If different → month-end → history section.
```

**History section requirements:**
- One subsection per year (e.g. `### May 2021`, `### May 2022`, ... up through the current year)
- Each year covers the most important events in that month: protocol milestones (NIP proposals/merges), client launches, key project releases, ecosystem-defining events, controversies
- Source every claim — link to the actual NIP PR, release tag, blog post, or Nostr event
- The retrospective REPLACES both NIP Deep Dive sections; do NOT include either

**History completed (do not repeat, do not re-summarize):**
- #3 (2025-12-31): "December Recap: Five Years of Nostr Decembers"
- #7 (2026-01-28): "Five Years of Nostr Januaries"
- #12 (2026-03-04): "Five Years of Nostr Februaries" (catch-up; #11 missed the rule and shipped deep dives instead)
- #15 (2026-03-25): "Five Years of Nostr Marches"
- #20 (2026-04-29): "Six Nostr Aprils"
- #24 (2026-05-28): "Six Years of Nostr Mays"

Common mistakes the structure prevents:
- Skipping the month-end history rule and shipping deep dives instead (this happened in #11)
- Putting NIP proposals in Top stories because they came from a flagship team
- Mixing released and unreleased work in the same section
- Using "Shipping this week" or "In Development" as section headings (boundary is unclear)
- Splitting a single project across multiple sections (consolidate under the one section where it belongs)

## PR Management for Newsletters

When working on newsletter updates:

1. **ALWAYS check for existing PR first** - Newsletter branches typically have an open PR already
2. **Update existing PR** - Force push changes to the existing newsletter branch
3. **Never create duplicate PRs** - One PR per newsletter issue

### Workflow
```bash
# Check for existing PR
gh pr list --head newsletter/YYYY-MM-DD

# If PR exists, update it
git checkout newsletter/YYYY-MM-DD
# Make changes
git add .
git commit --amend
git push --force

# If no PR exists (rare), create one
gh pr create --title "Newsletter #X (YYYY-MM-DD)" ...
```

## Common Newsletter Fixes

- Link updates (njump to GitHub releases, broken URLs)
- Typo corrections
- Content accuracy updates
- Translation synchronization

## Publishing to Nostr

**NEVER ask for an nsec. NEVER use `nak` directly. Always use the pipeline.**

```bash
# Full pipeline (all stages)
COMPASS_PUBLISH_INVOCATION=manual bun ~/compass/publish/publish.ts <N> --stage all --really-broadcast

# Individual stages (run in order)
COMPASS_PUBLISH_INVOCATION=manual bun ~/compass/publish/publish.ts <N> --stage parse
COMPASS_PUBLISH_INVOCATION=manual bun ~/compass/publish/publish.ts <N> --stage sign
COMPASS_PUBLISH_INVOCATION=manual bun ~/compass/publish/publish.ts <N> --stage announce-sign
COMPASS_PUBLISH_INVOCATION=manual bun ~/compass/publish/publish.ts <N> --stage broadcast --really-broadcast

# Or use the wrapper (same thing, shorter)
compass-publish <N>
compass-publish <N> --stage sign
```

**Config:**
- Bunker URI: `~/.config/compass-publish/bunker.json`
- Client key: `~/.config/compass-publish/client_key` (never rotate)
- Author: see `publish/config/author.json`
- Relays: see `publish/config/relays.json`
- Input file: `/tmp/<N>publish.md` (5 blocks: title, 21-word TLDR, banner URL, announcement, body)

**Before publishing:** check `publish/published.json` — if the issue is already there, do not publish again.

**Stale lockfile:** if a run aborts, remove `publish/out/<N>/.lock` before retrying.

**Expected relay rejections (not failures):**
- `wss://relay.nsec.app` — only accepts bunker traffic (kind 24133/24135)
- `wss://relay.towardsliberty.com` — whitelist-restricted

**Sign timeouts → read the error, do NOT immediately rotate the URI.** The pipeline holds a persistent NIP-46 session (one connect per run, every sign is ~350 ms after). Same bunker URI works forever after first pairing. Full writeup: `~/compass/publish/BUNKER.md` (protocol, Amber persistence proof, benchmarks).

**Cross-project bunker identity registry:** `~/.config/BUNKER_IDENTITIES.md` — compass uses its own identity (`npub1wav4fae...` / `775954f7...`), separate from blog and towardsliberty.

Full docs: `~/.config/meridian/profiles/alt/projects/-home-vibe-compass/memory/feedback_publishing_bunker.md`