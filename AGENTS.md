# Nostr Compass AI Infrastructure

**Technical resource for the Nostr protocol**

Weekly newsletter, podcast, and topic documentation with AI-powered workflows.

---

## System Overview

Nostr Compass is powered by a sophisticated AI infrastructure that handles:
- **Newsletter generation** through multi-phase research and writing workflows
- **Translation** to 9 languages with proper Unicode encoding
- **Validation** for technical accuracy and link integrity
- **Publishing** across multiple platforms with optimized content
- **Podcast production** from prep to publication

This is achieved through:
- **_COMPASS skill** at `skills/_COMPASS/` (5 specialized agents)
- **Claude Code integration** at `~/.claude/`
- **Legacy .opencode/** structure (preserved for backward compatibility)

---

## Architecture

```
$COMPASS_DIR/
├── skills/
│   └── _COMPASS/               # Primary skill system
│       ├── SKILL.md            # Comprehensive skill documentation
│       └── agents/             # Specialized agents
│           ├── NewsletterAgent.md      # Multi-phase newsletter generation
│           ├── TranslationAgent.md     # 9-language translation
│           ├── ValidationAgent.md      # Quality assurance
│           ├── PublishingAgent.md      # Distribution materials
│           └── PodcastAgent.md         # Podcast workflows
│
├── .opencode/                  # OpenCode structure (legacy, preserved)
│   ├── command/                # Command files
│   │   ├── newsletter.md
│   │   ├── translate.md
│   │   ├── validate.md
│   │   ├── publish.md
│   │   ├── podcast-prep.md
│   │   └── podcast-publish.md
│   └── skills/                 # OpenCode skills
│       ├── newsletter/SKILL.md
│       └── translate/SKILL.md
│
├── content/
│   ├── en/                     # English (primary)
│   │   ├── newsletters/        # Weekly editions (YYYY-MM-DD-newsletter.md)
│   │   └── topics/             # NIP and protocol documentation
│   └── de/, es/, fr/, it/, ja/, ko/, nl/, pt/, zh/  # Translations
│
├── data/
│   ├── projects.yml            # Master list of 440+ tracked projects
│   ├── project_updates/        # GitHub activity JSON
│   ├── app_discovery/          # Candidate-only GitHub search + tracked-owner sibling + NIP-89 + Zapstore-listing discovery
│   ├── nostr_nip_discussions/  # NIP discussions from Nostr relays
│   ├── nip34_repos/            # NIP-34 git-over-nostr repo tracking
│   ├── nip34_tracked.yml       # Known NIP-34 repos to monitor
│   ├── shakespeare_apps/       # Soapbox MiniApps submissions
│   ├── zapstore_releases/      # Developer-signed app releases from zapstore relay
│   ├── npubs.yml               # npub database
│   ├── non_github_updates.yml  # Manual updates (Codeberg/Sourcehut)
│   ├── coverage_history.json   # Per-project mention history across all newsletters (redundancy check)
│   ├── non_github_sources_YYYY-MM-DD.json  # Daily snapshot: tracked non-GH + zapstore non-GH + NIP-34 native repos
│   └── newsletter_workspace/   # In-progress workspace for current newsletter
│       ├── triage_YYYY-MM-DD.md         # Source triage for new projects
│       ├── selection_review_YYYY-MM-DD.md  # User-gated content selection review
│       └── sections/                    # Per-section drafts
│
├── scripts/
│   ├── fetch_all.sh                     # Master orchestrator (runs all 10 source families)
│   ├── fetch_project_updates.py         # GitHub data fetcher
│   ├── fetch_app_discovery.py           # Signature-verified untracked app candidate fetcher
│   ├── fetch_nostr_nip_discussions.sh   # NIP discussion scraper
│   ├── fetch_nip34_repos.sh             # NIP-34 repo tracker + discoverer
│   ├── fetch_zapstore_releases.sh       # Zapstore developer-signed app releases
│   ├── fetch_heartbeats.sh              # OpenSats + Sovereign Engineering grantee activity feeds
│   ├── fetch_shakespeare_apps.sh        # Soapbox MiniApps
│   ├── build_coverage_history.py        # Rebuilds coverage_history.json from content/en/newsletters/
│   ├── detect_non_github_sources.sh     # Builds non_github_sources_*.json (tracked + zapstore + NIP-34)
│   └── nostr_common.sh                  # Shared functions for nak-based scripts
│
└── podcastnotes/               # Podcast show notes (gitignored, YYYY-MM-DD-episode-NN.md)
```

---

## Available Commands

All commands work through the skill system. Use `/command` syntax in Claude Code sessions.

### `/newsletter` - Newsletter Generation

Multi-phase pipeline: data collection → strategy → research → writing → review → validation → build

**Usage:**
```
/newsletter                      # Generate from latest data
/newsletter draft                # Explicit draft mode
/newsletter draft 2026-01-14     # Generate for specific date
/newsletter fetch                # Run fetch scripts first, then generate
/newsletter fetch --since-days 7 # Fetch last 7 days, then generate
```

**Pipeline Phases:**
1. **Pre-flight Check** - Data freshness validation across GitHub, NIP discussions, NIP-34 repos, and Shakespeare Apps
2. **Data Collection** - Read GitHub updates, Nostr discussions, NIP-34 repo announcements, Shakespeare Apps, and manual entries
3. **Strategy** - Content selection, immediate-prior-issue continuity gate, NIP deep dive rotation
4. **Research** - Fetch NIP specs, implementation details, or historical data
5. **Writing** - Flowing prose (not bullet lists), source attribution, topic pages
6. **Style Review** - Remove em dashes, AI buzzwords, filler phrases
7. **Technical Review** - Link validation, NIP references, source links
8. **Build & Save** - Hugo build, summary report

**Agent:** NewsletterAgent ([documentation](skills/_COMPASS/agents/NewsletterAgent.md))

---

### `/translate` - Translation Workflow

Sequential translation to 9 languages with proper Unicode character encoding.

**Usage:**
```
/translate                       # Translate latest newsletter
/translate 2026-01-13            # Translate specific newsletter
/translate content/en/topics/nip-55.md  # Translate specific topic
```

**Languages:** de, es, fr, it, ja, ko, nl, pt, zh (processed sequentially)

**Character Encoding Rules (CRITICAL):**
- German: ä ö ü ß (NOT ae oe ue ss)
- French: é è ê ë à â ç ô û ù î ï œ
- Spanish: á é í ó ú ñ ü
- Portuguese: ã õ á é í ó ú ç â ê ô
- Italian: à è é ì ò ù
- Japanese: hiragana, katakana, kanji (no romaji)
- Korean: Hangul (no romanization)
- Chinese: Simplified characters (no pinyin)

**Agent:** TranslationAgent ([documentation](skills/_COMPASS/agents/TranslationAgent.md))

---

### `/validate` - Validation & Quality Assurance

Comprehensive technical accuracy and link integrity checking.

**Usage:**
```
/validate                        # Validate latest newsletter
/validate 2026-01-13             # Validate specific newsletter
/validate path/to/file.md        # Validate specific file
```

**Validation Checks (11 total):**
1. Internal link validation (all `/en/topics/X/` files exist)
2. NIP number validation (exist in NIPs repo)
3. External link validation (GitHub URLs return 200)
4. Unlinked PR/release mentions (every PR #XXX must be linked)
5. NIP Deep Dive duplication (rotation tracking)
6. Immediate-prior-issue continuity gate (`scripts/check_newsletter_continuity.py` plus manual confirmation of a distinct source and substantive user/protocol impact for every repeated project)
7. Style compliance (no em dashes, AI buzzwords)
8. Frontmatter validation (required YAML fields)
9. JSON event examples (all 7 NIP-01 fields)
10. Topic page source links (all have "Primary sources" section)
11. No version-only or low-value follow-up entries

**Agent:** ValidationAgent ([documentation](skills/_COMPASS/agents/ValidationAgent.md))

---

### `/publish` - Publishing Materials

Generate TLDR, social announcements, and email-ready content.

**Usage:**
```
/publish                         # Publish latest newsletter
/publish 2026-01-13              # Publish specific newsletter
```

**Output:**
- TLDR (exactly 21 words)
- Twitter/X announcement (under 280 chars)
- Nostr note (kind 1 containing the dense opening newsletter section)
- Email subject and preheader
- Newsletter with absolute URLs
- Distribution checklist
- Verified pre-publication Nostr outreach to every mentioned project and maintainer

If a new project is added after the issue's main outreach campaign but before publication, update the open review PR, resolve both the project and maintainer npubs from primary evidence, and run a targeted dry-run plus real send with `publish/dm-outreach.ts --pr-url '<newsletter PR URL>' --only '<project>' --only '<maintainer>'`. De-duplicate shared pubkeys, apply `data/npubs.yml` `no_dm` exclusions, and verify the separate targeted receipt without re-sending the full issue campaign. Newsletter-review DMs contain only the GitHub PR review request. Podcast outreach is separate, post-publication, and disabled until the owner approves the new recording setup and message; never reuse Riverside or append recording copy to review outreach.

If exhaustive primary-source, NIP-50, npub-directory, and relay searches do not verify a project or maintainer npub, always name the unresolved identity and completed search classes in the final owner handoff. Continue outreach to verified recipients under the standing omission policy; the notice is mandatory but is not an approval gate.

**Agent:** PublishingAgent ([documentation](skills/_COMPASS/agents/PublishingAgent.md))

---

### `/podcast-prep` - Podcast Preparation

Generate preparation materials BEFORE recording.

**Usage:**
```
/podcast-prep                    # Prep for latest newsletter
/podcast-prep 2026-01-13         # Prep for specific newsletter
```

**Output:**
- Episode overview and theme
- Segment breakdown with timing
- Discussion questions
- Research notes
- Technical term definitions
- Guest suggestions
- Clip suggestions for promotion

**Agent:** PodcastAgent ([documentation](skills/_COMPASS/agents/PodcastAgent.md))

---

### `/podcast-publish` - Podcast Publishing

Generate publishing materials AFTER recording.

**Usage:**
```
/podcast-publish                 # Publish latest podcast
/podcast-publish 2026-01-13      # Publish specific podcast
```

**Output:**
- Episode description
- Timestamps
- Show notes with links
- Nostr announcement (kind 1)
- Twitter/X announcement
- Distribution checklist
- Clip suggestions
- Guest thank you messages

**Agent:** PodcastAgent ([documentation](skills/_COMPASS/agents/PodcastAgent.md))

---

## Specialized Agents

### NewsletterAgent
**Purpose:** Multi-phase newsletter generation with research rigor and source integrity

**Capabilities:**
- Data collection and analysis (100+ projects)
- Content strategy and selection
- NIP deep dive research
- Flowing prose generation (not bullet lists)
- Topic page creation with source attribution
- Style compliance enforcement

**Critical Rules:**
- Every PR/release MUST be linked
- Use flowing prose, not bullet lists
- Every topic page MUST have "Primary sources" section
- No em dashes, AI buzzwords, or filler phrases

**[Full documentation →](skills/_COMPASS/agents/NewsletterAgent.md)**

---

### TranslationAgent
**Purpose:** Multi-language translation with encoding expertise

**Capabilities:**
- Unicode character encoding mastery
- Technical term preservation
- Internal link management (update to target language)
- Translation metadata tracking
- Staleness detection

**Critical Rules:**
- ALWAYS use proper Unicode (ä not ae, é not e)
- NEVER translate: project names, NIP numbers, technical terms, code
- Process one language at a time (sequential, not parallel)
- Include `translationOf` and `translationDate` in frontmatter

**[Full documentation →](skills/_COMPASS/agents/TranslationAgent.md)**

---

### ValidationAgent
**Purpose:** Technical accuracy and link integrity validation

**Capabilities:**
- Link integrity validation (internal and external)
- NIP reference validation
- Unlinked mention detection
- Style compliance detection
- Content quality checks

**Critical Rules:**
- Broken links are ERRORS (must fix)
- Unlinked PR/release mentions are ERRORS
- Topic pages without source links are ERRORS
- Style violations are WARNINGS (important for consistency)

**[Full documentation →](skills/_COMPASS/agents/ValidationAgent.md)**

---

### PublishingAgent
**Purpose:** Publishing materials generation for multi-platform distribution

**Capabilities:**
- TLDR generation (exactly 21 words)
- Social media content optimization
- Email distribution preparation
- URL absolutization
- Distribution checklists
- Outreach suggestions

**Critical Rules:**
- TLDR MUST be exactly 21 words (not 20, not 22)
- Twitter/X under 280 characters
- Neutral tone (no hype)
- Convert all relative URLs to absolute

**[Full documentation →](skills/_COMPASS/agents/PublishingAgent.md)**

---

### PodcastAgent
**Purpose:** Podcast preparation and publishing workflows

**Capabilities:**
- Discussion question generation
- Research note compilation
- Topic segmentation and timing
- Timestamp creation
- Show notes generation
- Content transformation (written → spoken)

**Critical Rules:**
- Prep materials BEFORE recording
- Publishing materials AFTER recording
- Transform technical writing to accessible conversation
- Weekly publishing (Fridays, 2 days after newsletter)

**[Full documentation →](skills/_COMPASS/agents/PodcastAgent.md)**

---

## Data Sources

### GitHub Project Updates
**Script:** `scripts/fetch_project_updates.py`

**Tracks the repositories currently listed in `data/projects.yml`** using
async HTTP with configurable concurrency:
- Releases
- Merged PRs
- Open PRs and commits (unless `--compact`)

**Setup:**
```bash
pip3 install -r scripts/requirements.txt  # includes httpx
# GitHub token: uses `gh auth token` or GITHUB_TOKEN env var
```

**Usage:**
```bash
python3 scripts/fetch_project_updates.py --since-days 7          # full fetch
python3 scripts/fetch_project_updates.py --since-days 1 --compact # quick check (skip commits/open PRs)
python3 scripts/fetch_project_updates.py --fresh                  # ignore partial results
python3 scripts/fetch_project_updates.py --concurrency 40         # more parallel connections
```

**Output:** `data/project_updates/updates_*.json`

**Restart and quota behavior:** The output also contains `fetched_repos`, a
completion journal that records successful fetches even when a repository had
no activity. Results are checkpointed atomically as individual concurrent
requests complete, rather than waiting for the slowest request in a whole
batch. A normal rerun resumes from this journal; `--fresh` deliberately drops
it and should only be used when a complete refetch is required. This prevents
worker or gateway restarts from repeatedly consuming the GitHub REST quota.

Run `python3 -m unittest tests/test_fetch_project_updates_resume.py` after
editing the resume/checkpoint path.

---

### Nostr NIP Discussions
**Script:** `scripts/fetch_nostr_nip_discussions.sh`

**Fetches:**
- NIP discussions from Nostr relays
- Community feedback
- Implementation notes

**Usage:**
```bash
bash scripts/fetch_nostr_nip_discussions.sh --since-days 7
```

**Output:** `data/nostr_nip_discussions/discussions_*.json`

---

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
bash scripts/fetch_nip34_repos.sh --tracked-file /path/to/project-specific-nip34.yml
```

**Output:** `data/nip34_repos/nip34_*.json`

**Newsletter rule:** Always run this for every newsletter before drafting. NIP-34 kind `30617` repo announcements include the maintainer pubkey, so ngit/GitWorkshop projects can often provide dev npubs automatically. Do not rely only on GitHub data for git-over-Nostr coverage.

---

### Zapstore Releases
**Script:** `scripts/fetch_zapstore_releases.sh`

**Fetches:** Developer-signed app metadata (kind 32267) and release events (kind 30063) from `wss://relay.zapstore.dev`. Joins releases to apps via `app_id`, enforces the self-signature gate (release `pubkey` must equal app `pubkey`), applies a naive Nostr-relevance regex (drops non-Nostr apps like LibChecker, Mullvad, NewPipe), cross-references repositories against `data/projects.yml`, and tracks new-app vs. update via persistent `data/zapstore_releases/publishers_seen.yml`.

**Usage:**
```bash
bash scripts/fetch_zapstore_releases.sh --since-days 7
bash scripts/fetch_zapstore_releases.sh --since-days 30
bash scripts/fetch_zapstore_releases.sh --include-non-nostr   # debug: bypass relevance filter
```

**Output:** `data/zapstore_releases/zapstore_YYYY-MM-DD.json`

**Schema (top-level):** `summary.{total_releases, nostr_relevant, new_apps, updates, tracked_in_projects_yml, candidates_for_projects_yml}` and `releases[]` with `nostr_relevant`, `new_app`, `update`, `tracked_project`, `app_repository`, `version`, `release_notes`, `pubkey`.

**Relay quirk:** `wss://relay.zapstore.dev` caps `--limit` at ~50 events per request and silently returns zero for higher limits. The fetcher pages with `--until` cursors and 2-second sleeps between pages. Expect ~30-60 seconds per run.

**Newsletter rule:** Always run and inspect this for every newsletter before drafting. Zapstore is a mandatory source for new app launches and developer-signed releases. Two buckets matter most:
- `releases[] | select(.new_app and .nostr_relevant and not .tracked_project)` → candidate **new Nostr-app launch** writeup
- `releases[] | select(.nostr_relevant and .tracked_project == null)` → candidates for adding to `data/projects.yml`

**Scope rule (CRITICAL):** Zapstore hosts plenty of non-Nostr apps. The naive regex filter will catch most, but a final editorial gate still applies — same NIP-34 scope rule: a Bitcoin-only or Lightning-only app does not become Nostr news just because it's signed onto zapstore. Always verify the project's runtime substance is Nostr-relevant before writing it up.

---

### Non-GitHub Projects
**File:** `data/non_github_updates.yml`

**Manual tracking for:**
- **ngit** (Codeberg): https://codeberg.org/DanConwayDev/ngit-cli
- **nostr-rs-relay** (Sourcehut): https://sr.ht/~gheartsfield/nostr-rs-relay/

Update weekly before newsletter generation.

---

## High-Priority Projects (Nostr-native only)

These projects receive extra attention when they have activity:

**Clients:** Damus, Amethyst, Primal, Snort, Coracle, noStrudel, Gossip
**Libraries:** NDK, nostr-tools, rust-nostr, go-nostr, nostrdb
**Relays:** strfry, nostr-rs-relay, nostream, Ditto, Nosflare, Nostrify
**Signers:** Amber, Alby, Frostr
**Messaging:** 0xchat, White Noise
**Protocols:** Blossom, Marmot, NIPs repository
**DevTools:** ngit, GitWorkshop
**Content:** Habla, YakiHonne, Wavlake, Zap.stream
**Other:** Shopstr, Mostr, Nostr.band

Note: Projects like CDK, Cashu.me, Nutshell, eNuts, Bitcoin Connect, Geyser, and Angor are tracked as `priority: medium` in `projects.yml` because they are not Nostr-native. Their changes are only covered when they directly affect Nostr relay traffic or Nostr user experience.

**NIP-34 hosting is delivery, not subject matter.** A Bitcoin-only or otherwise non-Nostr project does not become newsletter material because its source code is hosted on a NIP-34 GRASP server or `relay.ngit.dev`. CoinJoin coordinators (e.g. joinmarket-ng), on-chain mixers, Bitcoin Core forks, hardware-wallet firmware, and similar projects are out of scope regardless of patch volume on `relay.ngit.dev`. Only track NIP-34 repos whose project substance is itself Nostr-relevant (clients, relays, signers, NIP-34 tooling, schemata, etc.).

**Content Curation:** All items are scored 0-10 using a relevance rubric (Nostr Relevance, User Impact, Ecosystem Breadth, Novelty). Minimum score of 5 to include. Items must pass the Nostr Relay Test and the So What? Test. See [NewsletterAgent](skills/_COMPASS/agents/NewsletterAgent.md) for details.

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
- **NIP Updates items need FULL DETAIL (3-5 sentences minimum per item)**: explain what the existing NIP does, what the PR changes or proposes, why it matters, and include technical specifics (event kinds, tag formats, wire protocol changes). A one-sentence NIP summary is never acceptable. Use Newsletter #17's NIP Updates section as the reference standard.

### Source Linking (CRITICAL)
**Every mention of a PR, release, commit, or NIP change MUST include a direct link.**

✅ CORRECT:
```markdown
[PR #375](https://github.com/nostr-dev-kit/ndk/pull/375) fixes the bug.
[v1.05.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.05.0) adds bookmarks.
[NIP-71](/en/topics/nip-71/) is merged ([#1669](https://github.com/nostr-protocol/nips/pull/1669)).
```

❌ INCORRECT:
```markdown
PR #375 fixes the bug.
Version v1.05.0 adds bookmarks.
NIP-71 is merged.
```

**Link anchor text:** visible markdown link text must describe the destination, not an opaque ID. Never use `[GHSA-…](url)`, `[CVE-…](url)`, or bare `one, GHSA-…` enumeration in prose. Security advisories follow Newsletter #35 voice: descriptive anchors such as `[confused deputy in relay authentication](advisory-url)`. See `$COMPASS_DIR/CLAUDE.md` § "Link anchor text" and run `python3 scripts/check_newsletter_style.py` before handoff.

### Prohibited Patterns
- **Em dashes (—)**: Replace with comma, period, or colon
- **AI buzzwords**: Remove "exciting", "dive into", "robust", "leverage", "cutting-edge", "ecosystem"
- **Filler intensifiers**: Never use `actually`, `basically`, `clearly`, `definitely`, `essentially`, `eventually`, `fundamentally`, `literally`, `obviously`, `quite`, `really`, `simply`, `truly`, `very`, `virtually`
- **"Matters" as amplifier**: Never use "that matters most", "what matters is", "this matters", "why this matters". Name the specific property instead.
- **Comparison structures**: Never use "rather than", "not X but Y", "could not be more X". State the positive directly.
- **Semicolon negation flourish**: Never write "X is Y; Z is not." Restructure so both halves state a positive condition.
- **Filler phrases**: Remove "It's worth noting", "Interestingly", "At the end of the day"
- **Hedging**: Be direct - "This helps" not "This could potentially help"
- **Passive voice**: Convert to active

> Full rule set: `~/.claude/rules/base-antislop.md`

---

## Topic Management

### What Are Topics?
Topics are not just NIPs - they can be any advanced concept:
- NIPs (NIP-01, NIP-55, NIP-17)
- Protocols (Blossom, Marmot, Cashu)
- Concepts (Web of Trust, outbox model, MLS)
- Projects (when they warrant deep documentation)

### Creating Topic Pages
**Location:** `content/en/topics/<slug>.md`

**CRITICAL:** Every topic page MUST have a "Primary sources" section with links to:
- NIPs: Specification + PRs + implementation releases
- Projects: Specific releases or PRs being discussed
- Concepts: Defining documents, reference implementations

**Required Structure:**
```markdown
---
title: "NIP-XX: Title"
date: YYYY-MM-DD
draft: false
categories:
  - Category
---

Brief explanation (2-3 sentences).

## How It Works

Technical details.

## Implementations

- [Project](release-url) - description

---

**Primary sources:**
- [NIP-XX Specification](spec-url)
- [PR #NNNN](pr-url) - What this does
- [Release vX.Y.Z](release-url) - Implementation

**Mentioned in:**
- [Newsletter #N: Section](newsletter-url#section)

**See also:**
- [Related Topic](related-url)
```

**DO NOT create topic pages without source links.**

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
title: '[Translated title]'
date: YYYY-MM-DD
translationOf: /en/newsletters/YYYY-MM-DD-newsletter.md
translationDate: YYYY-MM-DD
draft: false
type: newsletters
---
```

### Nostr Event Examples
**Must include ALL 7 NIP-01 fields:**
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
- Translated: `/de/topics/slug/` (when translation exists)

---

## Branch/PR Workflow

### English Content PR
1. Draft locally first and stop for user review
2. Create branch/commit/push only after explicit user approval
3. Create PR only after separate explicit user approval
4. After PR approval, keep branch history to one clean commit; squash locally and update with `git push --force-with-lease`
5. Never force-push `main` or `master`

### Translation PR (after English is merged)
1. Draft translations locally first and stop for user review
2. Create branch/commit/push only after explicit user approval
3. Create PR only after separate explicit user approval

### Git Commit Messages
Follow established patterns:
- `Add Newsletter #N (YYYY-MM-DD) and new topic pages`
- `Add translations for Newsletter #N and topic pages`

---

## Tech Stack

- **Claude Code** - AI coding assistant
- **Shaka** - AI infrastructure framework
- **Hugo** - Static site generator
- **Python 3.9+** - Data fetching scripts
- **Bash** - Nostr relay scraping
- **GitHub Actions** - CI/CD
- **GitHub Pages** - Hosting at nostrcompass.org

---

## Publishing Schedule

### Newsletter
- **Day:** Wednesday
- **Time:** 16:00 UTC
- **Rationale:** Optimal for global audience (morning Americas, evening Europe/Africa, night Asia)

### Podcast
- **Day:** Friday (2 days after newsletter)
- **Time:** Flexible
- **Rationale:** Gives readers time to read first, podcast provides deeper dive

### Translations
- **Timeline:** Within 24-48 hours of English publication
- **Workflow:** Separate PR after English is merged

---

## Integration with Claude Code

This skill integrates with the Claude Code installation at `~/.claude/`.

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
GITHUB_TOKEN=<your-token>  # For fetch scripts (5000 req/hr vs 60)
```
---

## Success Metrics

- ✓ Developers cite Nostr Compass when explaining protocol decisions
- ✓ NIP authors reference our coverage in PR descriptions and discussions
- ✓ New developers understand Nostr evolution from archive
- ✓ Coverage seen as fair by all sides of debates
- ✓ Translations maintain technical accuracy across all 9 languages
- ✓ Zero broken links in published newsletters
- ✓ Consistent weekly publishing schedule (Wednesdays at 16:00 UTC)

---

## Support

**Contact:** NIP-17 DM to npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923

**Repository:** https://github.com/andotherstuff/nostr-compass

**Website:** https://nostrcompass.org

---

## Additional Documentation

- **Main Skill:** [skills/_COMPASS/SKILL.md](skills/_COMPASS/SKILL.md)
- **Strategy Guide:** [STRATEGY.md](STRATEGY.md)
- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md)

---

*Nostr Compass AI Infrastructure v1.0*

*Powered by Claude Code + Shaka*
