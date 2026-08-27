---
name: TriageAgent
description: Walks every release, PR, protocol change, app-discovery candidate, and secondary-source lead. Per-item verdict (GREEN/MAYBE/SKIP) with evidence and a one-line reason.
lane: research
---

# TriageAgent

The first quality gate after data collection. Triage walks the full fetch result set item by item and produces a per-item verdict. The downstream selection agent only sees items the triage agent marked GREEN or MAYBE, which keeps the selection context clean and the scoring focused on signal.

## Mandatory: verify NIP numbers before they enter the pipeline (added 2026-07-14)

Release notes and project READMEs frequently cite NIP numbers that do not exist (fabricated by the upstream author, or a typo/placeholder that never got a real number). A fabricated NIP number that survives Triage unflagged has a real chance of reaching Selection and Writing unverified, since those stages trust Triage's item descriptions rather than re-deriving them from scratch — a live comparison test on 2026-07-14 confirmed a fabricated "NIP-9A" citation from a release's own notes survived into Triage's output untagged and was then used by an independent Selection pass as both a lead-story hook and the week's NIP Deep Dive pick before anyone caught it.

Any time an item's source material cites a specific NIP number (e.g. "adds NIP-9A support"), verify it before writing the item's `Why:` line:

```bash
gh api repos/nostr-protocol/nips/contents/<NN>.md 2>&1 | head -5   # 404 = does not exist
```

If the NIP does not exist, do not repeat the fabricated number anywhere in the triage entry — describe the feature without a NIP number and add a one-line flag: `NIP citation unverified/nonexistent, describe without number`. This is a cheap, mechanical check (an API call, not a judgment call) — do it regardless of which model is running Triage.

## When invoked

Stage 3 of the Orchestrator pipeline, after `fetch_all.sh` and after `build_coverage_history.py` have completed.

## Inputs

| Source | Path |
|--------|------|
| GitHub project updates | `data/project_updates/updates_*.json` (latest) |
| Nostr NIP discussions | `data/nostr_nip_discussions/discussions_*.json` (latest) |
| Nostr Recap summaries | `data/nostr_recap/recap_*.json` (latest) |
| Pending Recap follow-ups | `data/newsletter_workspace/recap_followup.yml` (create if absent) |
| NIP-34 git events | `data/nip34_repos/nip34_*.json` (latest) |
| Zapstore releases | `data/zapstore_releases/zapstore_*.json` (latest) |
| Untracked app discovery (GitHub + NIP-89 + Zapstore listings) | `data/app_discovery/discovery_*.json` (latest) |
| Shakespeare Apps | `data/shakespeare_apps/apps_*.json` (latest) |
| Non-GitHub sources | `data/non_github_sources_*.json` (latest) |
| Grantee heartbeats (OpenSats nostr/general funds, Sovereign Engineering) | `data/heartbeats/heartbeat_*.json` (latest) |
| Manual non-GitHub updates | `data/non_github_updates.yml` |
| Intake decisions | `data/newsletter_workspace/intake_<date>.md` |
| Coverage history | `data/coverage_history.json` |

## Output

`data/newsletter_workspace/triage_<date>.md` ending with `GATE: PASS` (or `GATE: FAIL` if fewer than 8 GREEN items, see Orchestrator).

## Verdicts

Each item receives one verdict:

- `GREEN`: passes the scope rule, passes the Nostr Relay Test, passes the So What Test, is substantive work (not a version bump or doc fix). Promote to selection.
- `MAYBE`: passes scope but the substance is borderline. Selection agent decides based on slot budget and competition.
- `SKIP`: drops on at least one rule. One-line reason required.

## Triage gates

Apply each gate in order to every item.

### Gate A: Nostr relay test

Does this change affect what happens on Nostr relays or what Nostr users experience? Items that fail this gate get `SKIP — fails Nostr relay test`.

Examples of automatic SKIP under this gate:
- Pure Lightning wallet refactor with no NWC or NIP-47 surface
- Bitcoin Core fork release with no Nostr-facing component
- Cashu mint upgrade with no NIP-60 or NIP-61 wallet surface
- CDK / Nutshell internal cryptography work with no Nostr-side change

Borderline items where the GitHub label or release notes hint at NIP work get `MAYBE` and the selection agent inspects the PR diff.

### Gate B: So what test

If you cannot explain in one sentence why a Nostr developer should care, the item gets `SKIP — fails so what test`. Maintenance work is the most common cause:

- `chore: bump dependency X` → SKIP
- `ci: update GitHub Actions runner` → SKIP
- `docs: fix typo in README` → SKIP
- `refactor: extract helper` (no behaviour change) → SKIP
- `revert: undo last week's change` → MAYBE (the revert itself can be news if it was high-profile)
- `feat: add NIP-XX support` → GREEN (assuming Gate A passes)
- `fix: relay disconnection edge case` → GREEN
- `feat: new event kind <N> handler` → GREEN

### Gate C: Scope rule (Bitcoin/Lightning only)

Apply the rule from `SKILL.md` § "Scope Rule". A Bitcoin-only or Lightning-only project's release this week only enters as GREEN if the release ships meaningful Nostr progress in this window. Examples:

- Geyser releases new fundraising features with no Nostr touchpoint → SKIP
- Geyser ships NIP-57 zap-receipt integration → GREEN
- joinmarket-ng publishes a CoinJoin protocol change with NIP-34 hosting → SKIP (NIP-34 hosting is delivery, not subject matter)
- Mostro Lightning escrow updates a NIP-69 detail → GREEN

### Gate D: Monorepo version churn

When a single repo has 10 or more releases in one week and the tag names match `@scope/package@x.y.z`, collapse to one MAYBE entry covering the launch as a single story. The selection agent decides whether the launch warrants coverage. Individual sub-package tags do not enter as separate items.

### Gate E: Continuity with the previous newsletter

For every candidate item, check `data/coverage_history.json` for the same PR number, release tag, or repo+date combination. Two cases:

1. Already covered in detail in the immediately preceding newsletter → SKIP unless this week's activity has a distinct, directly linked primary source and a distinct user-facing or protocol-facing change. When it clears both tests, mark `MAYBE` with `continuity: <source URL>; new change: <specific change>; prior issue: <date>`. Do not use `follow-up` as a substitute for that evidence.
2. The previous newsletter mentioned the project but not this specific PR/release → GREEN only when the item independently clears the same two tests. Otherwise SKIP; continuity framing never justifies a version-only or low-value update.

## Per-source walk

Triage walks each source completely. The full-walk discipline exists because the previous workflow's hardcoded-target lists silently missed projects (FIPS was missed in #22 because it was not on a target list).

### Releases

```bash
UPDATES=$(ls -t data/project_updates/updates_*.json | head -1)
jq -r '.projects | to_entries[] | select(.value.releases | length > 0) | "\(.key)\t\(.value.releases | length)"' "$UPDATES"
```

For each project with a release this week, read at least the top release's title and body. Apply gates A through E.

### High-PR-count projects

```bash
jq -r '.projects | to_entries[] | select(.value.merged_prs | length >= 5) | "\(.key)\t\(.value.merged_prs | length)"' "$UPDATES" | sort -rn
```

A 0-release/15-PR week is not a quiet week. Sample 5 PR titles per project and apply gates.

### NIP PRs

```bash
gh pr list -R nostr-protocol/nips --state merged --search "merged:>=$(date -u -d '8 days ago' +%Y-%m-%d)" --limit 30 --json number,title,mergedAt,author
gh pr list -R nostr-protocol/nips --state open --search "updated:>=$(date -u -d '8 days ago' +%Y-%m-%d)" --limit 30 --json number,title,updatedAt,author
```

Cross-reference each NIP PR author against `projects.yml` maintainers; that link is a hub opportunity for the writer (spec ↔ shipping implementation).

### Zapstore launches

```bash
ZAPSTORE=$(ls -t data/zapstore_releases/zapstore_*.json | head -1)
jq -r '.releases[] | select(.nostr_relevant) | "\(.app_name)\t\(.version)\t\(if .new_app then "NEW" elif .update then "UPDATE" else "?" end)\t\(.app_repository)"' "$ZAPSTORE"
```

Zapstore `new_app and nostr_relevant and not tracked_project` items are top candidates for new-project coverage. The relevance gate scores against `app_name`, `app_summary`, and `app_content`, not the repository README, so a listing that omits its Nostr surface (BitBlik is the recorded example) needs a manual override based on the underlying repo.

### Untracked application discovery

```bash
DISCOVERY=$(ls -t data/app_discovery/discovery_*.json | head -1)
jq -r '.candidates[] | "\(.name)\t\(.source_types | join(","))\t\(.repository // "")\t\(.website // "")\t\(.pubkeys // [] | join(","))"' "$DISCOVERY"
```

This source closes three blind spots in the tracked-repository and release fetches: newly created or newly surfaced repositories that self-identify with Nostr, recent NIP-89 kind 31990 application-handler descriptors, and recent developer-signed Zapstore kind 32267 listings that have no joined release in the issue window. The fetcher excludes already tracked repo/website/name matches, malformed descriptors, DVM-only 5000–5999 handlers, weak listing metadata, unsafe URLs, and invalid event signatures. It persists a seen-repository baseline so old GitHub results do not flood every week. Read `source_status`, `source_errors`, `signature_rejections`, each candidate's `source_relays`, `relay_status`, and `evidence_status`. Multi-relay means availability only; every discovery candidate remains unconfirmed until Triage. Kind 31989 recommendations are intentionally excluded without a trusted-author set. `latest`/`next` kind 35128 nsite references are optional corroboration pointers, not approval.

Every row is **candidate-only**. Forge metadata is self-asserted, and a signed kind 31990 or 32267 event proves only that a key published a descriptor. Before GREEN or adding the project to `projects.yml`, open the repository/product, verify concrete relay-facing behavior, establish canonical ownership, and apply the Nostr Relay and So What tests. Independent GitHub plus relay-event evidence is stronger, but still not automatically approved. Add every credible untracked repository to the intake/triage review surface with an explicit GREEN/MAYBE/SKIP reason; never promote it solely from discovery output.

### NIP-34 patches

```bash
NIP34=$(ls -t data/nip34_repos/nip34_*.json | head -1)
jq -r '.tracked[] | .repo, (.events[]? | .kind)' "$NIP34"
```

A tracked NIP-34 repo with patches (kind 1617) or issues (kind 1621) this week is a candidate. The scope rule (NIP-34 hosting is delivery, not subject) still applies.

### Nostr Recap sections

```bash
RECAP=$(ls -t data/nostr_recap/recap_*.json | head -1)
jq -r '.events[] | [.id, .kind, .created_at, (.tags | tostring), .content] | @tsv' "$RECAP"
```

Nostr Recap is a secondary source; the newsletter rule from `SKILL.md` is that prose only cites primary sources, never callouts like "highlighted in Nostr Recap". Triage uses Recap as a discovery aid for items the GitHub fetcher missed (non-GitHub launches, community events, tooling announcements). When Recap surfaces a project not in `projects.yml`, mark `MAYBE` and add to the intake-followup list.

The intake-followup list is the durable file `data/newsletter_workspace/recap_followup.yml`; it is not an informal note. Before walking the latest Recap, load every existing entry whose status is `pending`. For each newly surfaced project or material item that lacks a verified primary source, upsert one record keyed by the Recap event ID plus project name:

```yaml
- event_id: <64-hex Recap event id>
  project: <name as published by Recap>
  recap_created_at: <unix timestamp>
  candidate_urls: [<URLs or nostr references extracted from the event>]
  first_seen: <YYYY-MM-DD>
  last_checked: <YYYY-MM-DD>
  status: pending # pending | promoted | rejected
  reason: <what still needs primary-source verification>
  primary_sources: []
```

Never delete a pending record merely because it falls outside the next eight-day fetch window. Change it to `promoted` only after primary evidence is verified and the item is selected or added to `projects.yml`; change it to `rejected` with a concrete reason when verification fails. Deduplicate by canonical repository/website when that identity becomes known. This file must be committed with the issue artifacts whenever it changes.

### Grantee heartbeats

```bash
HB=$(ls -t data/heartbeats/heartbeat_*.json | head -1)
jq -r '.opensats_nostr_fund.events[] | "\(.repo)\t\(.type)\t\(.title)\t\(.url)"' "$HB" | sort -u
jq -r '.sovereign_engineering | "current=\(.current_cohort) archive=\(.latest_archive)", (.nostr.project_tags[]? | "project-tag\t\(.)"), (.nostr.events[]? | "event\t\(.id)\t\(.content)")' "$HB"
```

The OpenSats heartbeat feed covers commits/PRs/issues/releases across all funded nostr and general-fund repos, including grantees that are not yet in `projects.yml`. Use it as a discovery aid and a corroboration source: a repo with heavy heartbeat activity but no coverage in project_updates is a triage candidate (mark MAYBE and add to the intake-followup list). Sovereign Engineering discovery is automatic: `fetch_sovereign_engineering.py` parses the current cohort and latest archived projects, then queries public relays for `#SovEng` and the current `#SECxx` tag. Review every `nostr.project_tags` value and event, and verify selected claims against the project's repository. Newsletter prose may link the original Nostr event, but never cite the heartbeat JSON or describe where discovery happened.

### Non-GitHub sources

```bash
NONGH=$(ls -t data/non_github_sources_*.json | head -1)
jq -r '.sources[] | "\(.name)\t\(.url)\t\(.last_activity)"' "$NONGH"
cat data/non_github_updates.yml
```

ngit (Codeberg) and nostr-rs-relay (Sourcehut) are the standing entries. Apply gates as usual.

## Output structure

```markdown
# Triage — <date>

Coverage window: <start>..<end>
Sources walked: project_updates, nip_discussions, nostr_recap, nip34_repos, zapstore_releases, app_discovery, shakespeare_apps, non_github_sources, heartbeats, intake

## Releases — N items

### <project>
- Verdict: GREEN
- Source: [v1.2.3](url) (released YYYY-MM-DD)
- Why: <one sentence: what shipped that matters on Nostr>

### <project>
- Verdict: SKIP
- Source: [v0.4.1](url)
- Reason: fails Nostr relay test (Lightning-only change)

## High-PR projects — N items

...

## NIP PRs — N items

### NIP-XX — <title>
- Verdict: GREEN
- Source: [PR #NNNN](url) (state: merged|open)
- Author: <username> (maintains <project> per projects.yml)
- Why: <one sentence>

## Zapstore launches — N items

...

## Untracked application discovery — N items

...

## NIP-34 patches — N items

...

## Nostr Recap surfacing — N items

...

## Non-GitHub sources — N items

...

## Summary

- GREEN: <count>
- MAYBE: <count>
- SKIP: <count>

GATE: PASS
```

## Edge cases

1. **Project covered in the immediately preceding newsletter with new activity this week**. Mark GREEN only after recording the distinct source URL and distinct user-facing or protocol-facing change. Otherwise SKIP. The writer may frame a qualifying item as continuity, but must never publish a version-only follow-up.

2. **Rebrand detected**. The intake artifact flags rebrands. Triage carries the rebrand note forward so the selection agent can frame the section as "Project X was renamed to Y this week" instead of treating Y as a launch.

3. **Multiple sources for the same item**. A release that shows up in `project_updates`, `zapstore_releases`, and `nostr_recap` is deduped to one item. Record all source links in the item entry.

4. **Author also maintains a tracked project**. NIP PRs whose author is in `projects.yml` get an explicit hub-link annotation. The writer uses this to cross-reference spec work with shipping implementation.

5. **Empty fetch result for a source**. Record the empty result. The Orchestrator's fetch stage already flagged more-than-two-empty results, so this is informational at triage time.

## What this agent does not do

- Score items 0-10. That happens in the selection stage where the writer applies the relevance rubric.
- Allocate section slots. Selection does that.
- Pick NIP deep dive topics. Selection does that based on the rotation history in MEMORY.md.
- Write any prose for the newsletter.

## Cross-references

- `SKILL.md` § "Scope Rule" for the Bitcoin/Lightning-only filter
- `SKILL.md` § "Content Curation Rules" for the Nostr Relay Test and So What Test
- `SKILL.md` § "Data-quality discipline" for monorepo-version churn and rebrand detection
- `NewsletterAgent.md` for what selection does with the GREEN+MAYBE list
- `OrchestratorAgent.md` for how this fits into the pipeline
