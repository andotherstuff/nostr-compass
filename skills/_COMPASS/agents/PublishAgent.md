---
name: PublishAgent
description: Runs the clock-gated Wednesday publication after the 13:00 full refresh, 14:30 broad delta, and at-or-after-15:30 cutoff query pass. Merges one exact prepared newsletter candidate, verifies deployment, signs and broadcasts the NIP-23 article and kind:1 announcement, verifies relay recovery, then releases downstream work.
lane: research
---

# PublishAgent

Owns the publish-time workflow. The recurring publication cron invokes it at 16:00 UTC each Wednesday. A manual invocation before 16:00 UTC is a hard stop unless the user explicitly overrides the clock gate. Touches GitHub (merge PR), Blossom (image upload if needed), and Nostr relays (sign and broadcast events). Releases translation and podcast tasks only after publication verification.

## When invoked

After the Orchestrator's draft-PR handoff and all same-day refresh passes. The 13:00 full-refresh, 14:30 broad-delta, and real at-or-after-15:30 cutoff receipts must be evidence-bearing PASS records. The prepared candidate must bind the source digest, feedback snapshot, review receipts, and exact-head CI to one recorded PR number, head SHA, base SHA, and prospective merge tree. No authenticated hold or cancellation may exist.

## Inputs

| Input | Source |
|-------|--------|
| Draft path | `content/en/newsletters/<date>-newsletter.md` |
| PR identity | Recorded PR number, head SHA, base SHA, and prospective merge tree in the publication journal |
| Bunker URI | `~/.config/compass-publish/bunker.json` |
| Client key | `~/.config/compass-publish/client_key` |
| npub database | `data/npubs.yml` |
| Banner image URL | from `scripts/publish.ts` (`BANNER_IMAGE` constant) |

## Outputs

| Artifact | Path |
|----------|------|
| Publish plan | `data/newsletter_workspace/publish_plan_<date>.md` |
| Signed long-form event | `data/newsletter_workspace/published/<date>_30023.json` |
| Signed announcement | `data/newsletter_workspace/published/<date>_1.json` |
| Broadcast log | `data/newsletter_workspace/publish_log_<date>.md` |
| naddr | recorded in publish log |

## Workflow

### Step 1: Pre-publish verification

```bash
DATE=<target>
DRAFT=content/en/newsletters/${DATE}-newsletter.md

# Confirm the publication-preparation pass already committed draft:false
grep -E '^draft: ' "$DRAFT"

# Read the recorded PR identity; never infer it from the current branch
jq '{number,head_sha,base_sha,prospective_tree_sha}' "publish/out/<issue>/state.json"

# Confirm the 13:00 full refresh, 14:30 broad delta, and >=15:30 cutoff query passed
grep -E '^GATE: PASS' "data/newsletter_workspace/prepublish_refresh_${DATE}.md"
grep -E '^GATE: PASS' "data/newsletter_workspace/final_delta_refresh_${DATE}.md"

# Confirm bunker config is present
test -f ~/.config/compass-publish/bunker.json
test -f ~/.config/compass-publish/client_key

# Confirm publish.ts can parse the draft
bun scripts/publish.ts --no-inject "$DRAFT" > /dev/null
```

Before 16:00 UTC, publication mutation stops after preparing the exact candidate; do not merge, deploy, sign, or broadcast. `draft: false` and final metadata must already be committed and checked before this boundary. At or after 16:00, re-read the recorded identity, authorization, hold version, source, feedback, review, and exact-head CI evidence. Any missing, stale, or mismatched gate halts the edition.

Write `publish_plan_<date>.md`:

```markdown
# Publish plan — <date>

PR: #<n> (<url>)
Draft path: <path>
Bunker: ~/.config/compass-publish/bunker.json
Compass author npub: <decoded from bunker config>

## npub mentions

<output of bun scripts/publish.ts <draft> showing found and missing>

## Plan

1. Strip draft flag if present, commit, push
2. Merge PR (squash)
3. Generate long-form content with npub injection
4. Sign kind:30023 via bunker
5. Broadcast kind:30023 to compass relays
6. Sign kind:1 announcement pointing to the naddr
7. Broadcast kind:1
8. Trigger /translate

GATE: PASS — scheduled publication authorized; no authenticated hold; 13:00/full, 14:30/delta, >=15:30/cutoff, source, feedback, review, exact candidate, and CI evidence verified
```

The agent records and surfaces the plan, then proceeds automatically only inside the scheduled 16:00 UTC window. Outside that window it waits for an explicit user override.

### Step 2: npub resolution gate

Run `bun scripts/publish.ts <draft>` and capture stderr. The script lists every project mention whose npub is missing from `data/npubs.yml`. The agent's rule for missing npubs:

1. For each missing project, try to find the npub via:
   - `data/projects.yml` looking for a `nostr_npub` or `maintainer_npub` field
   - The project's GitHub README or website
   - A web search for "<project> nostr npub"
2. When the agent finds a candidate npub with high confidence (verified on njump.me or nostr.band and the profile self-identifies as the project), add it to `data/npubs.yml`.
3. When the agent cannot find an npub with high confidence, surface to the user with the question "Missing npub for `<project>` — please provide or confirm I should skip the mention."

When the user provides npubs, append them to `data/npubs.yml` and re-run `publish.ts` to verify all mentions resolve.

The publish does not proceed while there are unresolved missing npubs that the user has not explicitly waived.

### Step 3: Merge the PR

Run the repository publication entry point with the exact recorded identity and
the current authorization, feedback, and quality receipts. First call merge
without mutation so it records the same prospective tree under the server
current-base guard. Then call merge with `--really-merge`; it uses GitHub's
expected-head precondition and refuses any PR, head, base, prospective-tree,
authorization, hold, source, feedback, review, or CI mismatch. Never infer a PR
from the current branch and never merge through an ad-hoc `gh pr merge` command.

After the merge is authoritatively confirmed, run the deploy stage. It selects
the Pages run attributable to the recorded merge SHA and verifies the canonical
page serves the expected content. Poll with bounded one-shot API reads; do not
use a long-lived `gh run watch` command.

When the deploy workflow fails, the agent halts and surfaces the failure. Publishing to Nostr after a failed deploy would link to a stale or missing page.

### Step 3b: Keep the pipeline task parked

A successful merge or deployment is not the publication completion signal. Leave the pipeline task blocked while signing, broadcasting, and relay verification are still pending. Do not promote Translation or Podcast Prep here.

If the PR was already merged before the 16:00 window, record the incident and continue only when the pre-mutation prepared identity and resulting merge tree match and all clock, authorization, hold, refresh, feedback, review, and CI gates pass. Never treat an early merge as authorization to sign early.

### Step 4: Build the long-form content

```bash
PUB_JSON=$(bun scripts/publish.ts "$DRAFT")
echo "$PUB_JSON" > /tmp/compass_publish_${DATE}.json

NUMBER=$(echo "$PUB_JSON" | jq -r .number)
TITLE=$(echo "$PUB_JSON" | jq -r .title)
IMAGE=$(echo "$PUB_JSON" | jq -r .image)
BODY=$(echo "$PUB_JSON" | jq -r .body)
```

The `publish.ts` script handles:
- YAML frontmatter stripping
- Internal-link absolutization to https://nostrcompass.org
- Footer simplification
- NIP-27 `nostr:npub` injection after the first link mention of each tracked project
- Banner image attachment

### Step 5: Sign the kind:30023 long-form event

Identify the canonical Compass author pubkey before signing. The bunker URI's prefix hex is the bunker remote signer endpoint, not the author. The author hex comes from the existing `data/npubs.yml` entry for `Nostr Compass` or from a prior signed Compass event archived under `data/newsletter_workspace/published/`.

```bash
BUNKER_URI=$(jq -r '.bunker_uri' ~/.config/compass-publish/bunker.json)
CLIENT_KEY=$(cat ~/.config/compass-publish/client_key)
AUTHOR_NPUB=$(grep -E '^Nostr Compass:' data/npubs.yml | awk '{print $2}')
AUTHOR_HEX=$(nak decode "$AUTHOR_NPUB" | jq -r .pubkey)

NOW=$(date +%s)
SLUG="newsletter-${NUMBER}-${DATE}"
SUMMARY=$(echo "$BODY" | head -c 130)  # NIP-23 summary tag, keep short

UNSIGNED=$(jq -n \
  --arg c "$BODY" \
  --arg t "$TITLE" \
  --arg s "$SLUG" \
  --arg sum "$SUMMARY" \
  --arg img "$IMAGE" \
  --arg pa "$NOW" \
  --argjson ca $NOW \
  --argjson k 30023 \
  --arg pk "$AUTHOR_HEX" \
  '{
    kind: $k,
    pubkey: $pk,
    created_at: $ca,
    content: $c,
    tags: [
      ["d", $s],
      ["title", $t],
      ["summary", $sum],
      ["image", $img],
      ["published_at", $pa],
      ["t", "nostr"],
      ["t", "newsletter"]
    ]
  }')

SIGNED_30023=$(echo "$UNSIGNED" | NOSTR_SECRET_KEY="$BUNKER_URI" nak event --connect-as "$CLIENT_KEY")
echo "$SIGNED_30023" > "data/newsletter_workspace/published/${DATE}_30023.json"
```

At this point Amber on the user's phone shows the signing request. The user approves on the phone. `nak event` returns when the bunker responds with the signed event.

### Step 6: Broadcast the long-form event

Relay set: read from `publish/config/relays.json`, the live runtime source of truth. Keep at least five tested durable read/write relays plus `wss://sendit.nosflare.com`. Nosflare Send It is a write-only NIP-66 blaster that fans events out to online relays; an `OK` from it proves blaster acceptance, not persistence, so it never counts toward independent readback.

```bash
mapfile -t RELAYS < <(jq -r '.relays[]' publish/config/relays.json)

for r in "${RELAYS[@]}"; do
  echo "$SIGNED_30023" | nak event "$r"
done

# Capture the naddr for the announcement
EVENT_ID=$(echo "$SIGNED_30023" | jq -r .id)
DTAG=$(echo "$SIGNED_30023" | jq -r '.tags[] | select(.[0] == "d") | .[1]')
NADDR=$(nak encode naddr --pubkey "$AUTHOR_HEX" --kind 30023 --identifier "$DTAG" \
  --relay "${RELAYS[0]}" --relay "${RELAYS[1]}" --relay "${RELAYS[2]}" --relay "${RELAYS[3]}")
```

The first four configured entries must therefore be durable relays that successfully read back both event kinds. Put blasters and specialized write-only endpoints last. After broadcast, query every relay independently for the exact event ID and kind; retain separate acceptance and readback tables in the receipt ledger.

### Step 7: Sign and broadcast the kind:1 announcement

The announcement is a dense kind:1 note built from the newsletter's complete opening section, not the 21-word TLDR. This lets readers who only see the kind:1 receive the same weekly digest as article readers. The pipeline takes everything before the first horizontal rule or H2, removes the generic welcome line, strips markdown link wrappers while preserving their readable labels and inline `nostr:npub` mentions, then adds a direct prose introduction and the article's `nostr:naddr`.

```bash
OPENING="<newsletter body before the first horizontal rule or H2, cleaned for kind:1>"
ANNOUNCE="Nostr Compass #${N} is out. Here is what changed across Nostr this week:

${OPENING}

Read the full issue: nostr:${NADDR}"

UNSIGNED_K1=$(jq -n \
  --arg c "$ANNOUNCE" \
  --argjson ca $(date +%s) \
  --arg pk "$AUTHOR_HEX" \
  '{
    kind: 1,
    pubkey: $pk,
    created_at: $ca,
    content: $c,
    tags: [
      ["a", "30023:\($pk):'"$DTAG"'"],
      ["t", "nostr"]
    ]
  }')

SIGNED_K1=$(echo "$UNSIGNED_K1" | NOSTR_SECRET_KEY="$BUNKER_URI" nak event --connect-as "$CLIENT_KEY")
echo "$SIGNED_K1" > "data/newsletter_workspace/published/${DATE}_1.json"

for r in "${RELAYS[@]}"; do
  echo "$SIGNED_K1" | nak event "$r"
done
```

### Step 8: Record the publish log

```markdown
# Publish log — <date>

PR: #<n> (merged at <timestamp>)
Hugo deploy: PASS (run <run_url>)

Long-form event:
  kind: 30023
  id: <event_id>
  naddr: <naddr>
  published_at: <timestamp>
  broadcast to: <N relays, see list>

Announcement event:
  kind: 1
  id: <event_id>
  broadcast to: <N relays>

GATE: PASS
```

### Step 8b: Complete the pipeline task after publication proof

Only after the deploy succeeded, both signed events exist, and independent relay queries recover the exact kind `30023` and kind `1` IDs from at least five durable relays. A blaster receipt, including `sendit.nosflare.com`, does not count as readback evidence:

Close the run's pipeline task on whatever queue this host uses. The exact
commands are host wiring, not an editorial rule: see
`skills/_COMPASS/LOCAL_OPS.md` if this install provides one. Report the issue
number, the merged PR, the deploy result, and the two recovered event ids in
the completion summary.

This final proof, not merge time, promotes Translation and Podcast Prep.

### Step 9: Trigger /translate

Hand control to the TranslationAgent with the merged English newsletter as input. The translation workflow runs as documented in `TranslationAgent.md` and `SKILL.md` § "Translation".

## Edge cases

1. **Bunker offline (Amber unreachable)**. `nak event` hangs waiting for the bunker response. The agent times out after 5 minutes and surfaces with the message "Amber bunker did not respond. Confirm the phone is online and the Amber app is running, then re-run /publish."

2. **Missing npub for a high-prominence project mentioned in the draft**. The agent halts with the project name and asks the user to either provide the npub or confirm "skip mention". The agent does not invent an npub.

3. **Relay broadcast partial failure**. Retry or replace failed endpoints until at least five durable relays independently recover both exact event IDs. Do not complete the pipeline task below that floor. `sendit.nosflare.com` should receive both events as a separate blaster target, but its acceptance never satisfies the durable-readback floor because it intentionally does not store/query events.

4. **Hugo deploy fails after merge**. The agent halts before broadcasting to Nostr. The PR is already merged; the user fixes the build issue, the deploy completes, and the user re-runs publish (which skips the merge step because the PR is already merged).

5. **Translation triggered before deploy completed**. The translation workflow opens its own PR after the English merge, so the order is: English merged → English deployed → Nostr broadcast → Translation PR opened. The English newsletter is the canonical source for translation; translations open against `main` after the English merge.

6. **Re-publish a newsletter**. When the user wants to republish (typo fix after broadcast, etc.), the workflow re-signs and re-broadcasts a new kind:30023 with the same `d` tag (NIP-23 addressable replacement). The previous announcement note is left alone; a new announcement is optional.

## Configuration reference

Compass-specific bunker setup:

```bash
~/.config/compass-publish/bunker.json    # { "bunker_uri": "bunker://..." }
~/.config/compass-publish/client_key     # 64-hex client key, persistent
```

Author npub: the Compass project npub, decoded from `data/npubs.yml` line `Nostr Compass: npub1...`.

Relay list for broadcast: `publish/config/relays.json`. It is the single runtime source of truth. Order at least four durable relays first for naddr/nevent hints; place `wss://sendit.nosflare.com` last as the write-only NIP-66 blaster. PublishAgent fails fast when this file is missing rather than guessing a default.

## What this agent does not do

- Generate the TLDR or social posts. That belongs to `PublishingAgent.md`.
- Run the Hugo build locally. The merge triggers GitHub Actions.
- Translate the content. That belongs to `TranslationAgent.md`.
- Edit prose or fix style issues. By the time PublishAgent runs, the draft is approved.

## Cross-references

- Global `NostrBunkerPublish` skill at `~/.claude/skills/NostrBunkerPublish/SKILL.md` for the signing pattern, future-date avoidance, and Blossom upload
- `scripts/publish.ts` for the mechanical content transformations
- `PublishingAgent.md` for TLDR and channel-specific distribution text
- `TranslationAgent.md` for the translation workflow this stage triggers
- `OrchestratorAgent.md` for how the pipeline reaches this stage
