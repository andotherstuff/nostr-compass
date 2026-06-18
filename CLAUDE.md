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

### Brief description on first NIP mention (CRITICAL)

**Every NIP mentioned in the newsletter MUST carry a brief description on its first appearance.** The description is one short clause or noun phrase that tells a reader unfamiliar with the protocol what the NIP defines. Subsequent mentions of the same NIP do not need re-description.

Two acceptable shapes:
- **Parenthetical**: `[NIP-17](/en/topics/nip-17/) (gift-wrapped private DMs)`
- **Inline-via-context**: `[NIP-77](/en/topics/nip-77/) Negentropy support for set-reconciliation syncs` (the surrounding sentence already states the spec's purpose)

If neither shape fits without distorting the sentence, prefer the parenthetical. Description length: one short clause or noun phrase, ideally fewer than 10 words. Do NOT re-describe within the dedicated deep-dive sections — those explain the spec in full.

Verify before commit: scan every `NIP-XX` token; for each token's first appearance, the same paragraph (or the prior clause in the same sentence) must explain what the NIP does. If not, add a parenthetical.

### Topic page link targets must match the NIP being linked (CRITICAL)

**A `[NIP-XX](/en/topics/nip-YY/)` link where XX != YY is always a bug.** This has happened before with `[NIP-44](/en/topics/nip-17/)` (NIP-44 is the encryption spec; NIP-17 is the private-DMs spec). Both deserve their own topic page links.

Audit before commit:

```bash
grep -oE '\[NIP-[A-Z0-9]+\]\(/en/topics/nip-[a-z0-9]+/\)' content/en/newsletters/<file>.md | awk -F'[][()/]' '{print $2, "->", $9}' | awk '$1 != $2 {print "MISMATCH:", $0}'
```

The audit must return no MISMATCH lines.

### NIP Deep Dive structure (CRITICAL — spec first, news last)

**A deep dive is a spec explainer, not a release recap.** ~80% of the prose must explain how the spec works, what problem it solves, and the design tradeoffs. ~20% (at most) is a closing pointer to current-week implementations.

Mandatory structure for every deep dive:
1. **Opening paragraph** — what the spec defines in one sentence, plus the core problem it solves
2. **Mechanics** — wire format, event kinds, tags, message exchange, encryption layer (whichever apply). Use precise field names, kind numbers, and concrete byte/structure detail.
3. **Design tradeoffs** — what was rejected, what was made optional, what the spec deliberately punts on, the trust model
4. **Comparison to adjacent specs** — when relevant, contrast with the closest NIP that solves a related problem (NIP-57 vs NIP-61, NIP-34 vs traditional git, NIP-46 vs NIP-55)
5. **Example event** — a full JSON example with all 7 NIP-01 fields (id, pubkey, created_at, kind, tags, content, sig)
6. **Implementation pointer** — ONE short paragraph linking to this week's substantive implementation, no longer than three sentences

What a deep dive is NOT:
- A list of this week's PRs by implementation project
- A round-up of "Amber/Clave/Nostur all shipped X"
- An update on protocol-PR status (that's the NIP updates section's job)
- A history of the proposal's open/merge timeline beyond one sentence

Anti-pattern caught in #27 first draft (now fixed): the original NIP-46 deep dive devoted entire paragraphs to "this week's PR #2373 logout method, Amber shipped it, Clave shipped it, Nostur shipped it" — that belongs in the lead and the NIP updates section, NOT in the deep dive. The same draft devoted only one paragraph each to the bunker/nostrconnect pairing flow, with no concrete byte-level detail.

When picking which NIPs to deep dive each week, check the rotation table in MEMORY.md (`grep -E "^## NIP Deep Dive" content/en/newsletters/*.md` is the authoritative source). NEVER deep dive a NIP that has been covered before; the rotation is one-shot.

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

### Per-PR Nostr-surface gate (CRITICAL — applies to EVERY project)

**Compass is a Nostr newsletter. Every PR, release item, or feature mentioned MUST touch a Nostr surface.** A project being broadly Nostr-aware (e.g. Zeus has NWC, Alby Extension has NIP-07) does NOT make every change in that project newsletter material. Each item is gated individually.

**Nostr surfaces (in scope):**
- Event publishing / signing / verifying (any kind)
- NIP implementations (any NIP, including NWC NIP-47, signers NIP-07/NIP-46/NIP-55, zaps NIP-57, nutzaps NIP-61, Cashu wallets NIP-60, etc.)
- Nostr-as-transport (NIP-34 hosting tooling, NIP-17 DMs, NIP-29 groups, NIP-59 gift wrap)
- Relay implementations and relay-protocol changes
- Nostr-key-derived primitives (CLINK noffers, NIP-07 signed payloads)
- Cryptographic libraries used by the Nostr signer/encryption path (noble/scure, secp256k1, NIP-44 ciphers) — only when bumping affects the wire format or signer behavior

**Out of scope (cut every time), even for Nostr-aware projects:**
- Lightning-only changes: LDK pathfinding, payment retry timeouts, Bolt11/Bolt12 mechanics, channel management, pathfinding heuristics, LNURL flows that don't touch a Nostr event
- Cashu-only changes: token decoding/redemption, keyset rotation, mint input/output limits, CDK Bolt12 quote recovery, melt recovery, Cashu wallet UX — unless the change touches kind 17375 (wallet), kind 7375 (token), kind 9321 (nutzap), kind 10019 (mint announcement), or another Nostr surface
- Bitcoin-only changes: on-chain wallet UX, signing flows, hardware wallet integration, coin control, fee estimation
- Generic UX/UI polish: animated keypads, QR scanner improvements (unless they scan Nostr payloads specifically), settings page redesigns, icon updates, theme tweaks
- Dependency bumps that don't change protocol behavior (security patches for `uuid`, `axios`, `postcss`, `webpack-dev-server`; ESLint config migrations; build-tool updates)
- Connector removals (LaWallet/Kollider/Citadel-style cleanup) — these are Lightning-wallet integrations, not Nostr; mention only if it ALSO drops a Nostr surface
- URL parsing / deep-link handling that doesn't decode `nostr:` URIs

**Examples of correct gating:**
- ✅ Zeus CLINK noffers (CLINK is a Nostr-key payment primitive) — KEEP
- ✅ Zeus queue-less NWC on iOS (NIP-47 surface) — KEEP
- ✅ Zeus Nostr Zap opt-out (controls kind 9735 receipts) — KEEP
- ❌ Zeus Cashu multi-mint sends — CUT (Cashu payment mechanics, no Nostr surface)
- ❌ Zeus LDK pathfinding improvements — CUT (Lightning-only)
- ❌ Zeus animated keypad / stealth QR scanner — CUT (UX polish)
- ❌ CDK token decoding for inactive keysets — CUT (Cashu-only)
- ❌ CDK CLN Bolt12 quote recovery — CUT (Lightning-only)
- ✅ Alby Extension @noble/@scure crypto migration — KEEP (touches NIP-07 signer / NIP-44 wire format)
- ❌ Alby Extension Boltz/SideShift Send-to-BTC swap flow — CUT (on-chain swap, no Nostr surface)
- ❌ Alby Extension dependency bumps (React, axios, etc.) — CUT
- ✅ Alby Hub stops retrying NIP-47 info publish for deleted apps (kind 13194 surface) — KEEP
- ❌ Alby Hub Just-in-Time channels / Cards page / Ark backend — CUT (already correctly gated as "outside Compass scope")

**Procedure when drafting any release writeup:**
1. List the release's full changelog
2. For each item, ask: "What Nostr event kind, NIP, or wire-format surface does this touch?"
3. If the answer is "none" — CUT the item
4. If the entire release has no Nostr surface — DROP the entire entry (e.g. CDK v0.17.1 in this week's audit)
5. Never use phrases like "the non-Nostr surface is large" to justify covering non-Nostr content alongside Nostr content — split the prose so only the Nostr surface appears

This rule applies retroactively: when auditing a draft, every Lightning/Cashu/Bitcoin-only line is a defect, not a stylistic choice.

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