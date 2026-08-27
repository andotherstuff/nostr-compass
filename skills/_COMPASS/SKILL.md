# _COMPASS Skill

**Nostr Compass AI Infrastructure** — orchestrated weekly newsletter generation, validation, publication, and translation for the Nostr protocol ecosystem.

Repository: `andotherstuff/nostr-compass` on GitHub. Site: https://nostrcompass.org.

## Overview

The skill is a multi-agent pipeline kicked off each Tuesday: pre-flight checks, intake of user-submitted project links, parallel data fetch, triage, selection, drafting, multi-round adversarial review, draft-PR handoff, and verified outreach. Wednesday automation then reruns every source family at 14:00 UTC and, only after that refresh passes, merges/deploys/signs/broadcasts at 16:00 UTC before releasing translation and podcast prep.

Quality > time. The review loop is uncapped; each iteration must produce concrete fix lists. A draft handed to the user has passed link integrity, claim verification, prose review, and topic-page audit.

## Workflow Entry Point

### `/newsletter <links + notes>` — Tuesday-morning kickoff

The user pastes a freeform message containing project URLs and editorial notes. Example:

```
/newsletter
Big week. Cover:
- Amethyst v1.13 https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0
- new project Nostrcrumb https://github.com/foo/nostrcrumb
- NIP-77 PR https://github.com/nostr-protocol/nips/pull/2400
Skip the docs renames.
```

The OrchestratorAgent takes over and runs the full pipeline. See `agents/OrchestratorAgent.md` for the stage-by-stage contract.

The pipeline parks at the review handoff with a draft PR open. The user can review, share it for outside feedback, and run `/newsletter-fix "<feedback>"` before the 16:00 UTC publication window.

At 14:00 UTC Wednesday the refresh cron reruns GitHub, direct Nostr, NIP-34, Zapstore, heartbeat, and spec-family sources and updates the PR without publishing. At 16:00 UTC the PublishAgent automatically merges, verifies deployment, signs/broadcasts kind 30023 and kind 1, verifies both events, then releases translation and podcast prep. Manual early publication requires an explicit user clock override.

## Installation State

This skill replaces the legacy `.opencode/command/newsletter.md` workflow. The OrchestratorAgent is the single entry point. Legacy `.opencode/` skill files are kept for backward compatibility with tools that read them but are no longer the source of truth for the workflow.

**Paths and host wiring:**

Paths are written as variables so the workflow does not assume one machine.

| Variable | Meaning | Typical value |
|---|---|---|
| `$COMPASS_DIR` | The shared repository checkout | `/srv/compass` |
| `$COMPASS_WORKTREE_ROOT` | Where per-issue worktrees are created | `/srv/compass-worktrees` |
| `$COMPASS_OPS_DIR` | Operator scripts: dispatchers, workspace resolver, task bodies | `/srv/ops/scripts` |
| `$COMPASS_STATE_DIR` | Discovery baselines, outside every worktree | `/srv/compass-state` |

Scheduling, work-queue, and notification integration is specific to the install
and is deliberately absent from this repository. When an install provides one,
its values and commands live in `skills/_COMPASS/LOCAL_OPS.md`, which is
gitignored. Read it if present; the workflow below does not otherwise depend on
any particular scheduler or messaging transport.

**File Structure:**
```
$COMPASS_DIR/
├── skills/
│   └── _COMPASS/           # Shaka skill (this file)
├── .opencode/              # Legacy OpenCode structure (preserved)
│   ├── command/            # Command files for OpenCode
│   └── skills/             # OpenCode skills
├── content/
│   ├── en/                 # English (primary)
│   ├── de/, es/, fr/, it/, ja/, ko/, nl/, pt/, zh/  # Translations
├── data/
│   ├── projects.yml        # 440+ tracked projects
│   ├── project_updates/    # GitHub activity JSON
│   ├── app_discovery/      # Candidate-only GitHub + NIP-89 + Zapstore-listing discovery
│   ├── nostr_nip_discussions/  # NIP discussions from Nostr
│   ├── nip34_repos/        # NIP-34 git-over-nostr repo tracking
│   ├── nip34_tracked.yml   # Known NIP-34 repos to monitor
│   ├── shakespeare_apps/   # Soapbox MiniApps submissions
│   └── non_github_updates.yml  # Manual updates for Codeberg/Sourcehut
├── scripts/
│   ├── fetch_all.sh                     # Master orchestrator (all fetchers)
│   ├── fetch_project_updates.py         # GitHub data fetcher
│   ├── fetch_nostr_nip_discussions.sh   # NIP discussion scraper
│   ├── fetch_nip34_repos.sh             # NIP-34 repo tracker + discoverer
│   ├── fetch_shakespeare_apps.sh        # Soapbox MiniApps
│   ├── fetch_zapstore_releases.sh       # Zapstore developer-signed app releases
│   ├── fetch_app_discovery.py            # Signature-verified untracked app candidates
│   ├── detect_non_github_sources.sh     # Aggregates non-GitHub repos (Codeberg/Sourcehut/NIP-34/Zapstore)
│   ├── build_coverage_history.py        # Builds coverage_history.json from past newsletters
│   └── nostr_common.sh                  # Shared functions
└── data/newsletter_workspace/           # Working artifacts for the next newsletter
    ├── triage_YYYY-MM-DD.md             # Source-pointer triage (greenlist/skip verdicts)
    ├── selection_review_YYYY-MM-DD.md   # Curated section selection awaiting user approval
    └── sections/                        # Per-section drafts (one file per section)
```

## Workspace + Coverage Artifacts (CRITICAL)

The newsletter flow now stages everything through `data/newsletter_workspace/` before prose is written, and consults `data/coverage_history.json` for redundancy checks. **Every fresh `/newsletter` session MUST:**

1. Check `data/newsletter_workspace/selection_review_<latest>.md` — if it exists for the upcoming Wednesday, this is the staging artifact and the user has either approved or is reviewing it. Do NOT overwrite without confirmation.
2. Check `data/newsletter_workspace/triage_<latest>.md` — if present, the user has triaged candidate new sources; honour those verdicts.
3. Consult `data/coverage_history.json` (regenerate with `python3 scripts/build_coverage_history.py` if older than the most recent newsletter) instead of grepping past markdown for redundancy checks.
4. Consult `data/non_github_sources_<latest>.json` (regenerate with `bash scripts/detect_non_github_sources.sh`) for Codeberg, Sourcehut, NIP-34, and Zapstore-signed non-GitHub sources.
5. Drafts go into `data/newsletter_workspace/sections/` one file per section. Only assemble into `content/en/newsletters/YYYY-MM-DD-newsletter.md` after the user signs off on the selection-review and the section drafts.
6. The pipeline is human-initiated via the `/newsletter <links + notes>` command. The OrchestratorAgent reads existing workspace files and resumes a partial run, so re-invoking with the same date is safe.
7. Read pre-enriched `Prep (verified YYYY-MM-DD):` blocks in `link_queue.md` and revalidate only stale or conflicting fields. Canonical repo, tracked-project relationship, and verified project/maintainer npub discovery should happen when the link arrives, not be deferred to Tuesday.

## Intro paragraph rule (CRITICAL)

The **"This week:" intro paragraph** is a feature digest, not a release manifest. It exists so a reader can scan five seconds of bold project names and one-clause feature descriptions to decide what to click into.

**Intro paragraph forbidden:**
- Version numbers (`v1.12.0`, `v6.2.2`, `0.6.34`, etc.)
- Event kind numbers (`kind 30617`, `kind 1111`, `kind 38383`, etc.)
- PR numbers (`PR #2381`, `#2378`, etc.)
- NIP numbers UNLESS the NIP is the actual subject of the paragraph (e.g. "[NIP-99 picks up an on-graph checkout-and-escrow proposal](...)")
- Long technical specifications (RPC numbers, tag formats, etc.)

**Intro paragraph required:**
- Project name as the linked anchor for its section
- One-clause description of WHAT FEATURE WAS RELEASED (not which version released it)
- Cause-and-effect when appropriate ("Sprout rebranded to Buzz and started publishing personas, teams, and managed-agent records as Nostr relay events")
- Continuity framing for ongoing stories ("Amethyst follows up last week's wallets-podcasts-workouts launch with Health Connect Workouts, Road Events, collapsable replies...")

**Why:** Past intros buried features under version-number scaffolding ("Amethyst v1.12.0 ships 170+ PRs adding NIP-60 Cashu wallets, NIP-61 nutzaps, NIP-82 software-app feeds..."). The reader's question is "what changed?", not "which release number contains the change?". Version numbers belong in the section body where the user has chosen to read details. Kind numbers belong in protocol-spec paragraphs and topic pages.

This rule applies to the intro paragraph ONLY. Section bodies still cite versions, kinds, and PRs in full because section bodies are the depth surface.

## Scope Rule (CRITICAL — non-negotiable)

**The newsletter is exclusively about Nostr.** Bitcoin-only and Lightning-only news items are excluded. Bitcoin/Lightning projects (Cashu wallets, joinmarket-ng, Bitcoin Core forks, hardware-wallet firmware, on-chain mixers, NFC payment apps, BTC price alerts, BTC meetup announcers, etc.) are mentioned ONLY when they ship *meaningful Nostr progress* in the week being covered (NIP-46 NWC support added, kind:1 publishing surface, Marmot integration, etc.).

When in doubt, ask: "Could a reader who doesn't care about Bitcoin/Lightning enjoy this paragraph?" If no, cut it. Same rule that killed joinmarket-ng coverage (NIP-34 hosting != Nostr subject) and pure Cashu wallet PRs (NUT-XX work != Nostr surface).

## Validation Discipline — Three-Round Adversarial Pass (CRITICAL)

After the initial selection-review is written and BEFORE asking for user approval, run at minimum ONE validation pass. For launch-heavy weeks (multiple new projects + multiple NIP merges), run all three rounds with parallel agents.

### Round 0 (mandatory, FIRST) — Previous-newsletter dedup gate

**Every newsletter builds on the previous one. Coverage is additive, never duplicative.** Before any selection or prose work, identify what the previous newsletter already covered so this week's draft frames continuity instead of re-introducing the same releases:

```bash
PREV=$(ls -t content/en/newsletters/*-newsletter.md | sed -n '2p')
PREV_DATE=$(basename "$PREV" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')
echo "Previous newsletter: $PREV (publishDate $PREV_DATE)"

# Extract previously-covered items
grep -oE 'PR #[0-9]+' "$PREV" | sort -u > /tmp/prev_prs.txt
grep -oE 'v[0-9]+\.[0-9]+\.[0-9]+[a-z0-9.-]*' "$PREV" | sort -u > /tmp/prev_versions.txt
grep -oE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' "$PREV" | sed 's/\.git$//' | sort -u > /tmp/prev_repos.txt

# For every release in this week's fetch, flag any with published_at <= previous newsletter's date
UPDATES=$(ls -t data/project_updates/updates_*.json | head -1)
jq -r --arg cutoff "${PREV_DATE}T00:00:00Z" '
  .projects | to_entries[]
  | .key as $proj
  | .value.releases[]?
  | select(.published_at <= $cutoff)
  | "ALREADY-COVERED-CANDIDATE: \($proj) \(.name // .tag) (published \(.published_at))"
' "$UPDATES"
```

**Decision tree for every release / PR in this week's fetch:**

1. **Release `published_at` BEFORE previous newsletter's date?** → Already covered. Either drop entirely, or write a one-sentence back-reference: "following [last week's v1.12.0 launch](/en/newsletters/PREV-DATE-newsletter/#section)". Never re-introduce.
2. **Previous newsletter cites this PR number?** → Already covered. Cross-link, do not re-write.
3. **Project covered in previous newsletter but with NEW activity this week?** → Cover the new activity in continuity framing: "after last week's…", "the v1.12.0 launch now has six patch follow-ups…"
4. **Brand new project / brand new release window** → Cover fresh.

The dedup gate runs BEFORE Round 1. If skipped, the rest of the validation cascades on contaminated input.

### Round 1 (mandatory) — Completeness sweep

Enumerate BOTH releases AND high-PR-count projects from `data/project_updates/updates_*.json`:

```bash
UPDATES=$(ls -t data/project_updates/updates_*.json | head -1)
# Releases this week
jq -r '.projects | to_entries[] | select(.value.releases | length > 0) | "\(.value.releases | length)\t\(.key)"' "$UPDATES" | sort -rn
# Projects with >=5 merged PRs (often shipping substantive work without a release tag)
jq -r '.projects | to_entries[] | select(.value.merged_prs | length >= 5) | "\(.value.merged_prs | length)\t\(.key)"' "$UPDATES" | sort -rn
```

A 0-release / 15-PR week is NOT a slow week. Sample release notes AND merged-PR titles for every project before scoring. Selection-review is incomplete until both lists are walked.

Also enumerate NIP PRs DIRECTLY via gh CLI (the relay scrape is unreliable for spec activity):

```bash
gh pr list -R nostr-protocol/nips --state merged --search "merged:>=$(date -u -d '7 days ago' +%Y-%m-%d)" --limit 30 --json number,title,mergedAt,author
gh pr list -R nostr-protocol/nips --state open    --search "updated:>=$(date -u -d '7 days ago' +%Y-%m-%d)" --limit 30 --json number,title,updatedAt,author
```

Filter Bitcoin-only / Silent Payments / DLC items per scope rule. For each merged PR, check whether the PR author also maintains a tracked project (that's a hub-link opportunity: spec ↔ shipping implementation).

### Round 2 (mandatory) — Topic-page audit + month-end check

For every NIP, protocol, and project that will be referenced in the issue, verify the topic page exists, list pages that need updates, and queue creation of missing pages BEFORE drafting. Topic-page work is part of newsletter drafting, not an afterthought.

Month-end check: if next Wednesday after this issue's date falls in a different calendar month, this is the last newsletter of the month. The two NIP deep dives are REPLACED by a "N Years of Nostr [Month]s" retrospective.

### Write findings to validation log

`data/newsletter_workspace/validation_log_YYYY-MM-DD.md` documents R1+R2+R3 deltas. Update the selection-review with an addendum reflecting all findings. Only THEN ask user for approval.

## Data-quality discipline (lessons from #28's 3-round validation)

These are observed failure modes that recur. Apply automatically:

1. **Monorepo npm-version churn:** if a single repo has >=10 releases in one week and tag names match `@scope/package@x.y.z`, collapse to ONE story. Cite the version range, not each tag. Example: napplet/web shipped 51 sub-package version tags in a single launch week.
2. **GitHub repo renames silently double-count:** if `projects.yml` contains both an old name and the canonical name (GitHub auto-redirects API requests), the fetcher pulls the same repo twice. Recovery: collapse to the canonical name, remove the duplicate entry. Record each known rename beside the canonical entry in `data/projects.yml`.

   **Rebrand vs. launch detection:** When a repo appears with a new name in the fetch, do NOT assume it is a new project. Always check:
   - Does `git log --follow` on the repo show inherited history from the previous name?
   - Does `gh api repos/<old-name>` redirect to the new name?
   - Has the previous-name slug been covered in past newsletters (`grep -l "<old-name>" content/en/newsletters/*.md`)?
   - Does the README explicitly frame this as a rebrand vs. as a launch?

   If any of these point to "rebrand," frame the section as continuity ("`<old-name>` was renamed to `<new-name>` this week") and link past coverage. Never re-introduce a rebranded project as if it were new. The Sprout → Buzz rename was caught only AFTER drafting #28's lead story as a launch; do the rebrand check during selection-review.
4. **Zapstore relevance gate scores against `app_name` + `app_summary` + `app_content`, not the project's GitHub README.** Projects whose Nostr surface is only in the repo (e.g. BitBlik) can score `nostr_relevant: false`. Manual triage must inspect the underlying repo and override when primary evidence establishes the Nostr surface.

## Project Category Placement (automatic — do not ask)

When adding a new project to `data/projects.yml`, place it in the existing top-level category that fits best. Do NOT invent new top-level categories without explicit user direction. Mapping:

| Project shape | Category |
|---------------|----------|
| Social feed / microblog / kind:1 client | `social_clients` |
| Long-form / NIP-23 / blog client | `longform_clients` |
| NIP-17 DM / Marmot messenger / encrypted chat / location-sharing on Marmot | `messaging_clients` |
| Video / audio / image / live-stream client | `media_clients` |
| Marketplace, commerce spec, NIP-99 implementation, P2P exchange order book | `marketplaces` |
| Bitcoin shop, gift card, top-up, prepaid card | `shops` |
| Developer tooling, CLI, debugger, builder, IDE, agentic-coding bridge, P2P fiat↔Lightning protocol with Nostr transport | `devtools` |
| Remote signer, NIP-46 bunker, hardware signer, FROST | `signers` |
| Relay implementation, relay extension, scope-N relay layer | `relays` |
| NDK, nostr-tools, SDK, schema, language library | `libraries` |
| LN wallet with Nostr, NWC client, Cashu wallet with Nostr surface | `wallets` |
| Protocol specification, runtime, browser, applet framework, agent workspace relay, MLS coordinator | `protocols` |
| Doesn't fit above | `other` |

Sub-rule for `protocols`: a project belongs here when it defines or implements a Nostr-shaped protocol surface that is itself the subject (Marmot, Blossom, Napplets, NAPs, Buzz workspace-as-relay, Cordn coordinator). When it primarily *consumes* an existing protocol, it goes in the consumer category instead.

When ambiguous, prefer the category where similar shipped projects live. Append entries to the *end* of the chosen category list; do not reorder existing entries. Use the same indentation (two spaces) and field order as neighbouring entries (`name`, `description`, `repo`, optional `website`, `maintainer`, `status`, `priority`, `notes`).

## Newsletter #34 permanent editorial gates

Every selection, review swarm, feedback resume, and Wednesday refresh must
enforce these gates before handoff:

- Compare the assembled issue with the complete English archive using
  `scripts/check_newsletter_continuity.py --history-dir`. The gate covers exact
  release, PR, and commit URLs anywhere in the draft, including items nested
  under generic protocol-family headings. Reuse is permitted only when the same
  paragraph explicitly describes a material status transition.
- Audit every included tagged release against the complete primary release
  notes and tag diff. `review_claims_<date>.md` must enumerate the checked
  source and confirm that every substantive user-facing and protocol change is
  represented; release-title summaries are insufficient.
- Briefly explain what every project does on its first mention in each section,
  and explain every NIP in human terms rather than leaving a bare identifier.
- Include only spec items with verified in-window activity. Group by protocol
  family, give each changed PR/commit/spec item its own paragraph, and explain
  technical behavior, trust/security impact, and maturity in useful detail.
- Select Deep Dives only from merged NIPs with current implementation evidence.
  Each dive must cite the canonical specification and at least three distinct
  clients or applications that implement or use it.
- Reader-facing prose must never mention Compass trackers, discovery mechanics,
  selection/scope cuts, fetch queues, or other internal workflow. Run the style
  checker after the final feedback edit.
- Synchronize the assembled draft and section source files after each feedback
  batch, then rerun continuity, style, paragraph-link, topic-backlink, and full
  production-build gates.
- Keep every issue PR draft and unmerged until the user explicitly approves
  that issue for merge. The scheduled publication time and a refresh PASS do
  not constitute approval; record approval evidence in the handoff or
  prepublish artifact.

## Available Commands

### `/newsletter <links + notes>` — Run the full pipeline

Single Tuesday-morning command. Body of the invocation carries the user's project URLs and editorial notes. The OrchestratorAgent dispatches the eight-stage pipeline and halts at human-review handoff. See `agents/OrchestratorAgent.md`.

Stages (each gates on a file in `data/newsletter_workspace/`):

0. Pre-flight: `git fetch`, open PR check, last-newsletter detection, target-date computation
1. Intake: parse user URLs, verify repos, dedup against `data/projects.yml`, add new entries with correct category and priority. Owned by `agents/IntakeAgent.md`.
2. Fetch: run `scripts/fetch_all.sh --since-days 8` (project updates, NIP discussions, Nostr Recap, Shakespeare apps, NIP-34 repositories, Zapstore releases, grantee heartbeats, and the NIP/BUD/NAP/Marmot/Gamma/Concord/NWC spec-family sweep) plus `build_coverage_history.py` and `detect_non_github_sources.sh`.
3. Triage: per-item verdict (GREEN/MAYBE/SKIP) against Nostr Relay Test, So What Test, and scope rule. Owned by `agents/TriageAgent.md`.
4. Selection: scoring rubric, slot allocation, NIP deep dive rotation or last-Wednesday history mode, and all-history redundancy check via `data/coverage_history.json` plus a full read of the latest three newsletters. User-approval gate. Owned by `agents/NewsletterAgent.md` (select mode).
5. Section writing: parallel writers per section. Owned by `agents/NewsletterAgent.md` (write mode).
6. Assembly: concatenate sections into `content/en/newsletters/<date>-newsletter.md` with `draft: true` frontmatter.
7. Review swarm: five parallel reviewers (LinkChecker, ClaimCheck, ProseReview, TopicAudit, ContinuityValueCheck). The prose gate runs `check_newsletter_style.py` and `check_newsletter_paragraph_links.py`; continuity runs against all prior newsletters. Loop with section writers until all five pass. Owned by `agents/ReviewSwarmAgent.md`.
8. Handoff: write `handoff_<date>.md`, open/update the draft review PR, run verified outreach, surface it to the user, then park the parent task for the Wednesday clock gates.
9. Wednesday 14:00 UTC refresh: rerun all eight source fetchers (GitHub repos, direct Nostr/NIP discussions, Nostr Recap, Shakespeare apps, NIP-34, Zapstore, heartbeats/Sovereign Engineering, and all spec families), rebuild non-GitHub and coverage data, incorporate material late changes into the draft PR, and rerun review/build gates. Never merge, sign, broadcast, or deploy in this window.
10. Wednesday 16:00 UTC publication: if `prepublish_refresh_<date>.md` ends in evidence-bearing `GATE: PASS` and no explicit hold exists, merge the reviewed PR, verify deployment, sign/broadcast kind 30023 and kind 1, verify relay recovery, then complete the parent task.

### `/newsletter-fix "<feedback>"` — Iterate on the handed-off draft

After handoff, the user provides feedback (direct prose or pointers to GitHub PR comments once the draft PR is open). The Orchestrator routes each feedback item to its owning agent, re-runs the affected stages, and re-runs the review swarm.

### Mid-week link intake (CRITICAL — always update current, never queue)

Any new link, correction, or piece of news the user shares while an issue is still unpublished (no evidence-bearing `publish_log_<date>.md` proving deploy plus both Nostr events) gets folded into that **current** issue immediately, via the `/newsletter-fix` path. `draft: false` or an accidentally merged PR is not sufficient publication proof. There is no "save it for next Tuesday." `data/newsletter_workspace/link_queue.md` exists only to hold items that arrive *after* the current issue has actually published — it is not a default parking lot for anything that shows up mid-week.

When new material comes in before publish:

1. Treat it exactly like a `/newsletter-fix` feedback item: update the relevant section in `content/en/newsletters/<date>-newsletter.md` directly.
2. Update the matching pre-assembly section file under `data/newsletter_workspace/sections/*.md` with the same final text. A resumed Writing/Assembly stage regenerates section files from Selection output, and if the section file doesn't carry the manual addition, a resume silently reverts it. Section files are the source of truth the pipeline reads from — the assembled newsletter is not.
3. Add or update any topic pages the new material touches (see "Topic Management" below), and link to them from the newsletter on first mention.
4. Only write an entry to `link_queue.md` once the current issue has published — from that point forward, new links queue normally for the next issue's Tuesday intake.
5. If the material introduces a project that was absent from the current draft, resolve both its dedicated project identity and its maintainer identity from primary evidence. Add the verified pair as one blank-line-delimited group in that issue's `data/npubs.yml` additions section. A shared pubkey is sent once and labeled with both aliases; never guess a second project key.
6. Once the revised draft is visible in the open review PR, dry-run and then send the standard pre-publication review/podcast DM to only the newly added project and maintainer with `publish/dm-outreach.ts --only '<project>' --only '<maintainer>'`. Keep `no_dm` exclusions, preserve the original campaign receipt, and verify the targeted follow-up receipt before reporting success.

This is a one-way door: verified deployment plus both recovered Nostr events decide "update current" vs. "queue for next week," not the frontmatter flag, PR merge state, how far along the week is, or how much rewriting it takes.

### Wednesday publication windows — refresh at 14:00, publish at 16:00 UTC

The recurring Wednesday refresh runs at 14:00 UTC. It executes `scripts/fetch_all.sh --since-days 8`, `scripts/build_coverage_history.py`, and `scripts/detect_non_github_sources.sh`; this covers all tracked GitHub repos, direct Nostr relay sources, NIP discussions, Nostr Recap, Shakespeare apps, NIP-34 repositories, Zapstore releases, OpenSats/Sovereign Engineering heartbeats, and the NIP/BUD/NAP/Marmot/Gamma/Concord/NWC spec sweep. It triages only newly discovered material, updates the current draft PR and synchronized section artifacts when a material change exists, reruns all five reviewers and the production build, and writes `prepublish_refresh_<date>.md`. It must not merge, deploy, sign, or broadcast.

The recurring Wednesday publication runs at 16:00 UTC. It requires the same-day refresh artifact to end with evidence-bearing `GATE: PASS`, requires no explicit hold/cancellation, and follows `agents/PublishAgent.md`. Steps:

1. Recheck PR state, review evidence, bunker config, npubs, and the strict UTC clock gate
2. Strip `draft: true` and merge the reviewed PR (or a publication-day update PR if the base issue was already merged during incident recovery)
3. Wait for and verify Hugo deployment
4. Build NIP-23 long-form content via `scripts/publish.ts`
5. Sign and broadcast kind:30023 via Amber to the broad set in `publish/config/relays.json`, including `sendit.nosflare.com` as a write-only NIP-66 blaster; capture naddr and recover the exact event from at least five durable relays
6. Sign and broadcast kind:1 to the same broad set, and independently recover the exact event from at least five durable relays; blaster acceptance does not count as persistence
7. Record `publish_log_<date>.md`, then complete the parent task so translation and podcast prep promote

A manual `/publish` invocation before 16:00 UTC must stop unless the user explicitly overrides the clock gate.

### `/translate` — Auto-triggered after publish

Spawn 9 parallel translation agents (de, es, fr, it, ja, ko, nl, pt, zh), each with adversarial review. Open a `translate/<date>` PR against `andotherstuff/nostr-compass:main`. Owned by `agents/TranslationAgent.md`.

**Edition Types:**
- Regular: NIP Deep Dive covers two related NIPs not previously covered (the rotation is one-shot; every prior `## NIP Deep Dive` heading under `content/en/newsletters/` is the authoritative record)
- Monthly Recap (last Wednesday of month, detected by Orchestrator): `Six Years of Nostr <Month>s` replaces the two NIP deep dives. Never prefix the history title with `NIP Deep Dive`; give every year at least two substantive, primary-source-linked paragraphs.

**Data Sources (read by TriageAgent at Stage 3):**
- `data/project_updates/updates_*.json` — GitHub releases, PRs, commits across 440+ projects
- `data/nostr_nip_discussions/discussions_*.json` — NIP discussions from Nostr relays
- `data/nostr_recap/recap_*.json` — Nostr Recap weekly summaries (secondary source, discovery aid only)
- `data/newsletter_workspace/recap_followup.yml` — durable unresolved projects/items surfaced by Nostr Recap; pending records survive the rolling fetch window until promoted or rejected with evidence
- `data/nip34_repos/nip34_*.json` — NIP-34 git-over-nostr patches and issues (the NIP34_RELAYS list in `scripts/fetch_nip34_repos.sh` includes `wss://git.nostrhub.io/` for NostrHub-launched projects and NIP discussions hosted on that GRASP server)
- `data/zapstore_releases/zapstore_*.json` — Zapstore developer-signed app releases
- `data/shakespeare_apps/apps_*.json` — Soapbox MiniApps submissions
- `data/non_github_sources_*.json` — aggregated non-GitHub sources (Codeberg, Sourcehut, NIP-34, Zapstore non-GitHub)
- `data/non_github_updates.yml` — manual tracking for ngit (Codeberg) and nostr-rs-relay (Sourcehut)
- `data/heartbeats/heartbeat_*.json` — OpenSats activity plus Sovereign Engineering cohort archives and relay-backed `#SovEng`/current `#SECxx` project discovery
- `data/coverage_history.json` — per-project mention history for redundancy checks
- `data/spec_updates/spec_updates_*.json` — mandatory weekly status for NIPs, BUDs, NAPs, Marmot/MIPs, Gamma Markets, Concord/CORD, and NWC; quiet families remain explicit

**Fetch error handling:** The Orchestrator's Stage 2 surfaces empty results from each fetcher. When more than two fetchers return empty, Stage 2 halts and surfaces to the user. Single-fetcher failures are logged and the pipeline continues with the available data.

**Web research:** The legacy web-search step is retired. The TriageAgent uses primary sources only (GitHub, Nostr relays, project pages directly). Secondary sources like Nostr Recap are read as discovery aids, not cited in prose.

**High-Priority Projects (Nostr-native only):**
- **Clients**: Damus, Amethyst, Primal, Snort, Coracle, noStrudel, Gossip
- **Libraries**: NDK, nostr-tools, rust-nostr, go-nostr, nostrdb
- **Relays**: strfry, nostr-rs-relay, nostream, Ditto, Nosflare, Nostrify
- **Signers**: Amber, Alby, Frostr
- **Messaging**: 0xchat, White Noise
- **Protocols**: Blossom, Marmot, NIPs repository
- **DevTools**: ngit, GitWorkshop
- **Content**: Habla, YakiHonne, Wavlake, Zap.stream
- **Other**: Shopstr, Mostr, Nostr.band

Note: Projects like CDK, Cashu.me, Nutshell, eNuts, Bitcoin Connect, Geyser, and Angor are tracked as `priority: medium` in `projects.yml` because they are not Nostr-native. Their changes are only covered when they directly affect Nostr relay traffic or Nostr user experience.

**Content Curation Rules:**

1. **Nostr Relay Test (mandatory gate):** Does this change affect what happens on Nostr relays or what Nostr users experience? If NO, omit regardless of project priority.

2. **Relevance Scoring (0-10):** Every candidate item is scored across Nostr Relevance (0-3), User Impact (0-3), Ecosystem Breadth (0-2), and Novelty (0-2). Minimum score of 5 to include.

3. **So What? Test:** If you cannot explain in one sentence why a Nostr developer should care, omit it.

4. **Depth Minimum:** No item gets fewer than 2-3 sentences. One-sentence filler entries are forbidden.

5. **Slot Budgets (guidelines, not hard caps):** News typically 5-7 items, Releases 5-8, Notable Changes 3-5, NIP Updates uncapped. Flex up in busy weeks if items pass all quality gates. Target: 30 minutes max reading time, as short as necessary.

See [NewsletterAgent](agents/NewsletterAgent.md) for the full scoring rubric and agent prompts.

---

### Translation reference

Parallel 9-language translation runs as Stage 9 (auto-triggered by `/publish`), one agent per language spawned concurrently. Languages: de, es, fr, it, ja, ko, nl, pt, zh.

Character encoding (critical): use proper Unicode (German ä ö ü ß, French é è ê ë à â ç ô û ù î ï œ, Spanish á é í ó ú ñ ü, Portuguese ã õ á é í ó ú ç â ê ô, Italian à è é ì ò ù, Japanese hiragana/katakana/kanji, Korean Hangul, Chinese simplified). ASCII substitutes (ae for ä) fail review.

What stays in English: project names, NIP numbers, technical terms (pubkey, npub, nsec, relay, event, kind, tag, zap), code blocks, URLs.

Full workflow: `agents/TranslationAgent.md`.

### Podcast reference

Podcast prep + publish remain a separate workflow with their own commands (`/podcast-prep`, `/podcast-publish`). They are not part of the newsletter pipeline. Full workflow: `agents/PodcastAgent.md`.

### Legacy `/validate` and `/publish` standalone commands

The standalone `/validate` and PublishingAgent's text-only `/publish` are retired as user-facing commands. Their behaviour is folded into the orchestrated pipeline:

- Validation work happens in Stage 7 (ReviewSwarmAgent) with four parallel reviewers
- Publishing TLDR + announcement text generation happens inside PublishAgent's Step 7
- The TLDR (21 words) and announcement tweet rules from PublishingAgent still apply; see `agents/PublishingAgent.md` for the format spec

---

## Writing Style Guide

### Tone
- Technical, precise, neutral, academic
- Accessible to newcomers without dumbing down
- No hype, no promotional language
- Charitable interpretation of controversies
- Present multiple perspectives without taking sides

### Format
- **USE FLOWING PROSE, NOT BULLET LISTS** for news items
- Each news item: 3-6 flowing sentences
- Bullets ONLY for: NIP Updates section, Releases quick list, technical specs
- Never start a paragraph with **Bold:** followed by bullets

### Source Linking (CRITICAL)

**Every mention of a PR, release, commit, or NIP change MUST include a direct link.**

**Good examples:**
```markdown
[PR #375](https://github.com/nostr-dev-kit/ndk/pull/375) fixes a bug in the seenEvents tracking system.

The release [v1.05.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.05.0) adds bookmark support.

[NIP-71](/en/topics/nip-71/) is merged ([#1669](https://github.com/nostr-protocol/nips/pull/1669)), bringing addressable video events.
```

**Bad examples (NO SOURCE LINKS):**
```markdown
PR #375 fixes a bug in the seenEvents tracking system.  ❌
The release v1.05.0 adds bookmark support.  ❌
NIP-71 is merged, bringing addressable video events.  ❌
```

**Link anchor text (NON-NEGOTIABLE):** visible link text describes the fix or source; GHSA/CVE/advisory slugs and bare PR numbers are URL-only. Security prose matches Newsletter #35 (`2026-08-12-newsletter.md` Amber section): descriptive anchors like `[confused deputy in relay authentication](advisory-url)`, never `[GHSA-vx4h-56qj-wcp7](url)` or `one, GHSA-vx4h-56qj-wcp7,`. Gate: `python3 scripts/check_newsletter_style.py`.

### Prohibited Patterns
- **Em dashes (—)**: Replace with comma, period, or colon
- **AI buzzwords**: Remove "exciting", "dive into", "robust", "leverage", "cutting-edge", "game-changing", "seamless"
- **Filler phrases**: Remove "It's worth noting", "Interestingly", "At the end of the day"
- **Hedging**: Be direct - "This helps" not "This could potentially help"
- **Passive voice**: Convert to active

### Internal Linking
- Link every NIP/concept to its topic page on first mention
- Use format: `[NIP-55](/en/topics/nip-55/)`
- For translated content, update to target language: `[NIP-55](/de/topics/nip-55/)`

---

## Topic Management

### What Are Topics?

Topics are not just NIPs - they can be any advanced concept that deserves deeper explanation:
- NIPs (NIP-01, NIP-55, NIP-17)
- Protocols (Blossom, Marmot, Cashu)
- Concepts (Web of Trust, outbox model, MLS)
- Projects (Primal, Damus, Amethyst)

### Creating Topic Pages

**Location:** `content/en/topics/<slug>.md`

**Required Structure:**
```markdown
---
title: "NIP-XX: Title"
date: YYYY-MM-DD
draft: false
categories:
  - Category
---

Brief explanation of what this is (2-3 sentences).

## How It Works

Technical details.

## Implementations

- [Project](release-url) - description of implementation

---

**Primary sources:**
- [NIP-XX Specification](https://github.com/nostr-protocol/nips/blob/master/XX.md)
- [PR #NNNN](https://github.com/org/repo/pull/NNNN) - What this PR does
- [Release vX.Y.Z](https://github.com/org/repo/releases/tag/vX.Y.Z) - Implementation release

**Mentioned in:**
- [Newsletter #N: Section](/en/newsletters/YYYY-MM-DD-newsletter/#section)

**See also:**
- [Related Topic](/en/topics/related/)
```

**CRITICAL:** Every topic page MUST have a "Primary sources" section with links to:
- NIPs: Specification + PRs + implementation releases
- Projects: Specific releases or PRs being discussed
- Concepts: Defining documents, reference implementations

**DO NOT create topic pages without source links.**

### NIP Deep Dive Rotation

Track which NIPs have been covered to avoid duplicates:

```bash
grep -h "## NIP Deep Dive" content/en/newsletters/*.md | grep -oE "NIP-[0-9]+" | sort | uniq
```

Suggest NIPs based on:
1. NIPs that changed this week
2. NIPs mentioned in releases/PRs
3. Foundational NIPs not yet covered
4. NIPs relevant to current ecosystem trends

---

## Agent Architecture

### Weekly Git workspace isolation

Every weekly run must use `$COMPASS_OPS_DIR/compass_weekly_workspace.py <target-date>` before Stage 0. The resolver fetches `origin/main`, creates or reuses `$COMPASS_WORKTREE_ROOT/<target-date>` on `newsletter/<target-date>`, copies the accumulated link queue on first initialization, and preserves the shared `$COMPASS_DIR` checkout exactly as it is. Tuesday intake, Wednesday refresh, publication, translation, and podcast tasks must all use the returned absolute workspace path. Never make a shared-checkout branch, stash, reset, clean, or forced switch part of the weekly workflow; an ambiguous worktree or branch collision is a hard stop.

The pipeline is orchestrated across specialized agents with file-based handoffs. Each agent runs with fresh context and reads only the workspace files it owns. The Orchestrator stays lightweight because it reads only the `GATE:` line of each artifact.

### Pipeline diagram

```
/newsletter <links + notes>
        |
        v
 [0] Pre-flight  ── git fetch, open PR check, last newsletter, target date
        |
        v
 [1] IntakeAgent ── parse URLs, verify repos, dedup, add to projects.yml
        |
        v
 [2] Fetch (parallel via fetch_all.sh)
        |   project_updates / nostr_nip_discussions / nostr_recap
        |   nip34_repos / zapstore_releases / shakespeare_apps
        v
 [3] TriageAgent ── per-item GREEN/MAYBE/SKIP verdicts
        |
        v
 [4] NewsletterAgent (select mode) ── scoring, slot allocation, deep dive picks
        |          USER APPROVAL GATE
        v
 [5] NewsletterAgent (write mode, parallel section writers)
        |   News / Releases / Notable Changes / NIP Updates / NIP Deep Dive
        v
 [6] Assembly ── concatenate sections, write content/en/newsletters/<date>.md
        |
        v
 [7] ReviewSwarmAgent (parallel reviewers)
        |   LinkChecker / ClaimCheck / ProseReview / TopicAudit
        |   <--- loops back to section writers until all four pass
        v
 [8] Handoff to user

USER: "publish it"
        |
        v
 PublishAgent ── PR merge, NIP-23 broadcast, kind:1 announcement
        |
        v
 TranslationAgent ── 9 languages, translation PR
```

### Stage gate contract

Each agent ends its workspace artifact with one of:

```
GATE: PASS
GATE: FAIL — <one-line blocker>
GATE: HUMAN-INPUT-REQUIRED — <question>
```

The Orchestrator advances only on `PASS`. On `FAIL` it loops back to the owning agent with the failure context. On `HUMAN-INPUT-REQUIRED` it halts and surfaces the question.

### Context isolation rule

Raw JSON fetch files are 1-2 MB and must never enter agent context directly. Always extract via `jq` or `grep`:

```bash
# Right: extract a summary
jq -r '.projects | to_entries[] | select(.value.releases | length > 0) | "\(.key)\t\(.value.releases | length)"' data/project_updates/updates_*.json

# Wrong: load the whole file
Read("data/project_updates/updates_*.json")
```

### Workspace structure

```
data/newsletter_workspace/
├── preflight_<date>.md
├── intake_<date>.md
├── fetch_<date>.md
├── triage_<date>.md
├── selection_review_<date>.md
├── sections/
│   ├── intro.md
│   ├── news.md
│   ├── releases.md
│   ├── notable_changes.md
│   ├── nip_updates.md
│   └── nip_deep_dive.md
├── review_log_<date>.md
├── review_links_<date>.md
├── review_claims_<date>.md
├── review_prose_<date>.md
├── review_topics_<date>.md
├── handoff_<date>.md
├── publish_plan_<date>.md
├── publish_log_<date>.md
└── published/
    ├── <date>_30023.json
    └── <date>_1.json
```

### Agent registry

| Agent | Role | File |
|-------|------|------|
| OrchestratorAgent | Pipeline driver, stage gating | `agents/OrchestratorAgent.md` |
| IntakeAgent | Tuesday-morning URL parsing and projects.yml updates | `agents/IntakeAgent.md` |
| TriageAgent | Per-item Nostr Relay Test, So What Test, scope rule | `agents/TriageAgent.md` |
| NewsletterAgent | Selection + section writing | `agents/NewsletterAgent.md` |
| ReviewSwarmAgent | Coordinator for 4 parallel reviewers | `agents/ReviewSwarmAgent.md` |
| PublishAgent | Merge, NIP-23 broadcast, kind:1 announcement, translate trigger | `agents/PublishAgent.md` |
| TranslationAgent | 9-language translation with encoding rules | `agents/TranslationAgent.md` |
| ValidationAgent | Legacy validation (folded into ReviewSwarm) | `agents/ValidationAgent.md` |
| PublishingAgent | TLDR and announcement text (used by PublishAgent) | `agents/PublishingAgent.md` |
| PodcastAgent | Separate podcast prep + publish workflow | `agents/PodcastAgent.md` |

---

## Technical Conventions

### Newsletter Frontmatter
```yaml
---
title: 'Nostr Compass #N'
date: YYYY-MM-DD
publishDate: YYYY-MM-DD
draft: false
type: newsletters
---
```

### Translation Frontmatter
```yaml
---
title: 'Nostr Compass #2'  # Translated title
date: YYYY-MM-DD
translationOf: /en/newsletters/YYYY-MM-DD-newsletter.md
translationDate: YYYY-MM-DD
draft: false
type: newsletters
---
```

### Nostr Event Examples
**Must include ALL NIP-01 fields:**
```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": <unix timestamp>,
  "kind": <integer>,
  "tags": [...],
  "content": "...",
  "sig": "<128-char hex>"
}
```

### Internal Links
- Topic pages: `/en/topics/slug/`
- Newsletters: `/en/newsletters/YYYY-MM-DD-newsletter/`
- Sections: `/en/newsletters/YYYY-MM-DD-newsletter/#section-id`

---

## Data Fetching

### GitHub Project Updates

**Script:** `scripts/fetch_project_updates.py`

**Setup:**
```bash
# Install dependencies (requires Python 3.9+)
pip3 install -r scripts/requirements.txt

# Set up GitHub token (optional but recommended - 5000 req/hr vs 60)
cp scripts/.env.sample scripts/.env
# Edit scripts/.env and add your token
```

**Usage:**
```bash
# Fetch updates from last 7 days (required: --since-days)
python3 scripts/fetch_project_updates.py --since-days 7

# Preview which repos would be fetched
python3 scripts/fetch_project_updates.py --since-days 7 --dry-run

# Verbose output
python3 scripts/fetch_project_updates.py --since-days 7 -v
```

**Output:** `data/project_updates/updates_*.json`

### Nostr NIP Discussions

**Script:** `scripts/fetch_nostr_nip_discussions.sh`

**Usage:**
```bash
# Fetch discussions from last 7 days
bash scripts/fetch_nostr_nip_discussions.sh --since-days 7
```

**Output:** `data/nostr_nip_discussions/discussions_*.json`

### NIP-34 Git Repos

**Script:** `scripts/fetch_nip34_repos.sh`

**Two modes:**
- **Track**: Monitors known repos from `data/nip34_tracked.yml` for patches (kind 1617) and issues (kind 1621)
- **Discover**: Finds new NIP-34 repos, filters noise (shakespeare, backups, test repos, forks)

**Usage:**
```bash
bash scripts/fetch_nip34_repos.sh --since-days 7
bash scripts/fetch_nip34_repos.sh --track-only
bash scripts/fetch_nip34_repos.sh --discover-only
```

**Output:** `data/nip34_repos/nip34_*.json`

### Zapstore Releases

**Script:** `scripts/fetch_zapstore_releases.sh`

**Fetches:** Developer-signed app metadata (kind 32267) and release events (kind 30063) from `wss://relay.zapstore.dev`. Joins releases to apps via `app_id`, enforces the self-signature gate (release `pubkey` must equal app `pubkey`), applies a naive Nostr-relevance regex, cross-references repos against `data/projects.yml`, and tracks new-app vs. update via persistent `data/zapstore_releases/publishers_seen.yml`.

**Usage:**
```bash
bash scripts/fetch_zapstore_releases.sh --since-days 7
bash scripts/fetch_zapstore_releases.sh --since-days 30
bash scripts/fetch_zapstore_releases.sh --include-non-nostr   # debug: bypass relevance filter
```

**Output:** `data/zapstore_releases/zapstore_YYYY-MM-DD.json`

**Extracting data for newsletter:**
```bash
ZAPSTORE_FILE=$(ls -t data/zapstore_releases/zapstore_*.json | head -1)

# Nostr-relevant releases in window
jq -r '.releases[] | select(.nostr_relevant) | "\(.app_name) v\(.version) (\(if .new_app then "NEW" elif .update then "update" else "?" end)) - \(.app_repository)"' "$ZAPSTORE_FILE"

# Candidates for projects.yml (Nostr-relevant, not yet tracked)
jq -r '.releases[] | select(.nostr_relevant and .tracked_project == null) | "\(.app_name) - \(.app_repository)"' "$ZAPSTORE_FILE" | sort -u
```

**Newsletter rule:** Always run before drafting. Two buckets:
- `new_app and nostr_relevant and not tracked_project` → candidate new Nostr-app launch writeup
- `nostr_relevant and tracked_project == null` → candidates to add to `data/projects.yml`

Same NIP-34 scope rule applies: a Bitcoin-only or Lightning-only app does not become Nostr news because it's signed onto zapstore. Verify the project's runtime substance is Nostr-relevant.

**Relay quirk:** `wss://relay.zapstore.dev` caps `--limit` at ~50 events per request and silently returns zero for higher limits. The fetcher pages with `--until` cursors and 2-second sleeps between pages. Expect ~30-60 seconds per run.

### Non-GitHub Projects

**File:** `data/non_github_updates.yml`

**Manual tracking for:**
- **ngit** (Codeberg): https://codeberg.org/DanConwayDev/ngit-cli
- **nostr-rs-relay** (Sourcehut): https://sr.ht/~gheartsfield/nostr-rs-relay/

Update weekly before newsletter generation.

---

## Branch/PR Workflow

### English Content PR
1. Create branch: `newsletter/YYYY-MM-DD`
2. Create file: `content/en/newsletters/YYYY-MM-DD-newsletter.md`
3. Work through sections interactively
4. Create new topic pages as needed in `content/en/topics/`
5. Run `/validate` before creating PR
6. Create PR (includes newsletter + any new topics)

### Translation PR (after English is merged)
1. Create branch: `translate/YYYY-MM-DD`
2. Run `/translate` to generate translations for all 9 languages
3. Create separate PR for translations, referencing English PR

### Git Commit Messages
Follow the established pattern:
- `Add Newsletter #N (YYYY-MM-DD) and new topic pages`
- `Add translations for Newsletter #N and topic pages`

---

## Common Pitfalls

### Newsletter Generation
- **Don't mention PRs without links** - Every "PR #123" must be `[PR #123](url)`
- **Don't mention versions without links** - Every "v1.0.0" must link to release page
- **Don't guess PR numbers** - Always verify URLs exist
- **Don't invent release notes** - Only describe what's in actual release
- **Don't over-explain** - Technical audience, respect their time
- **Don't skip topic links** - Every NIP/protocol/concept mention should link to topic page
- **Don't forget new topics** - If concept doesn't have topic page, create one
- **Don't create topics without sources** - Every topic page MUST have "Primary sources" section
- **Don't use emojis** - Unless user explicitly requests them
- **Don't use em dashes** - Replace with comma, period, or colon
- **Don't use AI buzzwords** - Remove "exciting", "dive into", "robust", "leverage"
- **Don't use bullet lists for news** - Write flowing prose paragraphs

### Translation
- **Don't use ASCII substitutes** - Use proper Unicode (ä not ae, é not e)
- **Don't translate code** - Keep code blocks, commands, snippets in English
- **Don't translate project names** - Damus, Amethyst, Primal stay as-is
- **Don't guess technical terms** - When unsure, keep English with brief explanation
- **Don't change URLs** - External links stay the same
- **Don't forget _index.md** - Each new language section needs index files
- **Don't skip front matter** - Include `translationOf` and `translationDate`

### Validation
- **Don't skip validation before PR** - Always run `/validate` after writing
- **Don't ignore broken links** - Fix or remove them before publishing
- **Don't ignore style warnings** - They matter for consistency
- **Don't assume links work** - Validate external links return 200

---

## Integration with Global Shaka

This skill is designed to work with the global Shaka installation at `~/.claude/`.

**Settings Integration:**
```json
{
  "skills": {
    "_COMPASS": {
      "path": "$COMPASS_DIR/skills/_COMPASS",
      "enabled": true,
      "commands": [
        "newsletter",
        "translate",
        "validate",
        "publish",
        "podcast-prep",
        "podcast-publish"
      ]
    }
  }
}
```

**Environment Variables:**
```bash
COMPASS_DIR=$COMPASS_DIR
GITHUB_TOKEN=<your-token>  # For fetch scripts
```

---

## Success Metrics

- Developers cite Nostr Compass when explaining protocol decisions
- NIP authors reference our coverage in PR descriptions and discussions
- New developers understand Nostr evolution from archive
- Coverage seen as fair by all sides of debates
- Translations maintain technical accuracy across all 9 languages
- Zero broken links in published newsletters
- Consistent weekly publishing schedule (Wednesdays at 16:00 UTC)

---

## Support

**Contact:** NIP-17 DM to npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923

**Repository:** https://github.com/andotherstuff/nostr-compass

**Website:** https://nostrcompass.org

---

*Nostr Compass AI Infrastructure v1.0 - Integrated with Shaka*
