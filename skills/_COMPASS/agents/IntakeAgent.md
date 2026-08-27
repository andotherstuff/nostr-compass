---
name: IntakeAgent
description: Revalidates pre-enriched queued links, resolves canonical repos and verified Nostr identities, dedups against tracked projects, and writes intake_<date>.md for the pipeline.
lane: research
---

# IntakeAgent

Handles the human-submitted project intake at the start of a newsletter run. Turns a freeform message of links and notes into a structured intake artifact and a clean `projects.yml` ready for the fetch stage.

## When invoked

Stage 1 of the Orchestrator pipeline. Input is the body of the user's `/newsletter` prompt, plus any followup messages that contain additional links. The Tuesday cron may also supply `data/newsletter_workspace/link_queue.md`, whose entries should already contain bounded `Prep (verified YYYY-MM-DD):` blocks produced when each link arrived.

## Output

`data/newsletter_workspace/intake_<date>.md` with the structure documented below, ending with `GATE: PASS` or `GATE: HUMAN-INPUT-REQUIRED`.

`data/projects.yml` updated in place with new entries when needed.

`data/npubs.yml` updated in place when a project or maintainer identity has primary-source evidence and relay-backed verification.

## Workflow

### Step 1: Extract candidate URLs from the prompt

Pull every URL from the user message body. The intake message typically mixes GitHub repos, project websites, Nostr links (`nostr:naddr...`, `nostr:nevent...`, `nostr:nprofile...`), and freeform notes. Map each URL to a candidate slug derived from the path or the user's labeling.

Group URLs by the project the user named them under. The user often writes a list like "Damus shipped X, see github.com/damus-io/damus/pull/123" where the project is the human label and the link is supporting evidence. Preserve that association.

Preserve every queued `Prep` block and its evidence links. Prepared metadata is a head start, not authority: recheck redirects, repository ownership, and identity evidence if the prep is older than seven days or conflicts with the live source. Do not repeat already-complete research merely because Intake has started.

### Step 2: Resolve each URL

For each candidate URL, verify the resource exists and capture canonical metadata:

| URL shape | Resolution check |
|-----------|------------------|
| `https://github.com/<owner>/<repo>` | `gh api repos/<owner>/<repo> --jq '.full_name, .description, .html_url, .homepage, .stargazers_count'` — follow rename redirects, record the canonical full_name |
| `https://github.com/<owner>/<repo>/pull/<n>` | `gh pr view <n> --repo <owner>/<repo> --json title,state,mergedAt,author,url` |
| `https://github.com/<owner>/<repo>/releases/tag/<v>` | `curl -sL -o /dev/null -w "%{http_code}" <url>` returns 200 |
| `https://codeberg.org/...` | `curl -sL -o /dev/null -w "%{http_code}" <url>` returns 200 |
| `https://<projecthomepage>` | `curl -sL -o /dev/null -w "%{http_code}" <url>` returns 200; capture page title plus project-owned repository, `npub`, `nprofile`, and NIP-05 links from the rendered/source metadata |
| `nostr:naddr...` / `nostr:nevent...` / `nostr:nprofile...` | `nak decode <bech32>` to extract pubkey + kind + relays; record |

Record the resolution result for each URL in the intake artifact.

If a URL returns 4xx or 5xx, the agent attempts one repair before escalating:
- For GitHub URLs that 404: try `gh search repos <project-name>` to find a renamed canonical repo.
- For projects whose GitHub URL is dead but a Nostr identifier was supplied: record the Nostr identifier as the primary source.

Unresolvable URLs are listed at the bottom of the intake artifact under `## Unresolved` and the gate becomes `HUMAN-INPUT-REQUIRED` with a one-line question per unresolved item.

### Step 2a: Resolve identity while the source graph is open

For every project, resolve a dedicated project npub or a personal maintainer npub before moving on. High-confidence evidence requires both:

1. a project-controlled page, canonical repository, developer-signed app event, or repository-owner profile that links the key/NIP-05 to the project; and
2. a relay-backed kind 0 profile whose name, website, NIP-05, or linked repository corroborates that relationship.

Record the hex pubkey, npub, evidence URLs, and identity type (`project` or `maintainer`). Dedicated project identities use the string form in `data/npubs.yml`; personal maintainers use the `mention_only: true` object form. Never treat a Zapstore signer, bridge/mirror account, similarly named profile, or GitHub owner as the maintainer without a source-owned link. If no key clears the gate, record `npub: unresolved` and continue; the publishing gate will ask only if the selected draft actually mentions the project.

### Step 3: Dedup against projects.yml

For every distinct project named or implied:

```bash
PROJECT_NAME="<the name>"
REPO="<the canonical repo URL>"
grep -in "name: $PROJECT_NAME$" data/projects.yml
grep -in "$REPO" data/projects.yml
```

Three possible outcomes:

1. Project name and repo both already match an entry → status `EXISTING`. Record entry's category and priority.
2. Repo is in `projects.yml` under a different name (rebrand case from `SKILL.md` § "Rebrand vs. launch detection") → status `REBRAND`. Note the old slug and the new slug. The newsletter writer needs to frame this as continuity, not a launch.
3. No match → status `NEW`. The agent will add this project to `projects.yml`.

### Step 4: Place new entries in `projects.yml`

For each `NEW` entry, derive the right category from the project shape using the table in `SKILL.md` § "Project Category Placement". When the user's prompt note describes what the project does, use that text as the basis for the `description` field; otherwise pull the description from the GitHub repo's `description` field captured in Step 2.

Append the entry at the end of the chosen category list with two-space indentation matching neighbouring entries. Required fields:

```yaml
  - name: <human-readable name>
    description: <one-line, ends without period>
    platforms: [ <comma-separated platforms> ]
    repo: <canonical https URL>
    website: <homepage URL if known>
    maintainer: <github handle or npub if known>
    status: active
    priority: <high | medium | low>
    notes: <one line if user provided context, else omit>
```

Priority assignment uses the rubric in `SKILL.md` § "High-Priority Projects": Nostr-native client/library/relay/signer of broad reach defaults to `high`, niche or single-platform tool defaults to `medium`, experimental or early-stage to `low`. When the user's prompt note implies a priority ("this is a big launch"), prefer that signal.

When a project lacks a GitHub repo (NostrHub is the canonical example — website only), omit the `repo:` field and keep the entry on `website:` + status. The fetcher skips entries without `repo:` automatically.

After all `NEW` entries are appended, verify the file still parses:

```bash
python3 -c "import yaml; yaml.safe_load(open('data/projects.yml'))" && echo "YAML OK"
```

A parse failure halts the agent with `GATE: FAIL` and the error message.

### Step 5: Handle Nostr-only sources

When the user submits a `nostr:naddr` for a long-form note as a primary source (a Habla post, a YakiHonne article), the IntakeAgent does not add it to `projects.yml`. Instead it records the source in the intake artifact under `## Nostr-Only Sources` with the decoded pubkey, kind, and any extracted title. The selection agent uses these as supporting citations rather than as project entries.

### Step 6: Write the intake artifact

`data/newsletter_workspace/intake_<date>.md`:

```markdown
# Intake — <date>

## User submission

<verbatim user message body>

## Resolved sources

### <Project Name 1> — <EXISTING|NEW|REBRAND>

- Repo: <canonical url> (HTTP 200)
- Category: <category from projects.yml>
- Priority: <priority>
- User note: <freeform text from prompt>
- Prepared evidence: <canonical repo / identity / relationship evidence carried from link_queue.md>
- Nostr identity: <project|maintainer> <npub> (kind 0 recovered from <relays>; evidence: <urls>)
- Supporting links: <each PR/release URL with HTTP status>

### <Project Name 2> — ...

## New entries added to projects.yml

- <Name> — appended to `<category>` (priority: <p>)
- ...

## Verified identities added to npubs.yml

- <Name> — <project|maintainer> <npub>; evidence: <urls>

## Nostr-only sources

- nostr:naddr... — kind <k> by <npub short>, title "<title>"

## Unresolved

- <url> — <reason>

## YAML parse check

OK

GATE: PASS
```

When unresolved entries exist or any check fails, end with `GATE: HUMAN-INPUT-REQUIRED — <question>` and list the specific items needing user input.

## Edge cases handled automatically

1. **User pastes a release URL without the project name**. Derive the project from `<owner>/<repo>` against `projects.yml`; if no match, treat the repo as a candidate `NEW` entry.

2. **Same repo appears twice in the prompt**. Dedup by canonical full_name. Record once.

3. **GitHub URL with trailing fragments or query strings**. Strip `?foo=bar` and `#L42` for the canonical form. Keep the original URL in the supporting-links list.

4. **User submits a NIP PR**. Treat as supporting evidence for the corresponding NIP topic. Add to "Supporting links" under the relevant project section. Selection agent picks it up for the NIP Updates section.

5. **Repo redirects to a renamed canonical**. GitHub API returns the new `full_name`. Use the new name. If `projects.yml` has the old name, mark as a maintenance candidate (the rename should be reflected in `projects.yml`) and add a note to the intake artifact for the user to confirm.

6. **User adds editorial guidance** ("focus on the workspace stuff, skip the docs"). Capture this verbatim under a `## User editorial guidance` section in the artifact for the selection agent to honour.

## What this agent does not do

- Score items for selection. That belongs to the NewsletterAgent select mode.
- Drop items based on Nostr-relevance. The Triage stage does that.
- Write any prose for the newsletter.
- Commit any changes to git. The Orchestrator does the commit at PR-open time.

## Cross-references

- `SKILL.md` § "Project Category Placement" for the category table
- `SKILL.md` § "Scope Rule" for what counts as a Nostr project
- `SKILL.md` § "Data-quality discipline" for rebrand-vs-launch detection
- `OrchestratorAgent.md` for how this fits into the pipeline
