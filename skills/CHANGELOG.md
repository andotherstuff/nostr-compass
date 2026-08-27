# Changelog - Nostr Compass Shaka Integration

All notable changes to the Nostr Compass Shaka integration will be documented in this file.

## [1.0.0] - 2026-01-20

### Added
- **_COMPASS skill** - Comprehensive Shaka skill for Nostr Compass workflows
- **5 specialized agents:**
  - NewsletterAgent - Multi-phase newsletter generation with research rigor
  - TranslationAgent - 9-language translation with Unicode encoding expertise
  - ValidationAgent - Technical accuracy and link integrity validation
  - PublishingAgent - Publishing materials generation for multi-platform distribution
  - PodcastAgent - Podcast preparation and publishing workflows
- **6 commands:**
  - `/newsletter` - Newsletter generation pipeline
  - `/translate` - Sequential translation workflow
  - `/validate` - Comprehensive validation
  - `/publish` - Publishing materials generation
  - `/podcast-prep` - Pre-recording preparation
  - `/podcast-publish` - Post-recording publishing
- **Setup automation:**
  - `setup-shaka.sh` - Automated Shaka registration script
  - Comprehensive documentation in AGENTS.md
  - Agent-specific documentation files
- **Backward compatibility:**
  - Preserved `.opencode/` structure
  - Dual command interface (Shaka + OpenCode)

### Architecture
- Shaka integration at `~/.claude/`
- Skill location: `skills/_COMPASS/`
- Agent definitions: `skills/_COMPASS/agents/`
- Legacy OpenCode: `.opencode/` (preserved)

### Documentation
- `AGENTS.md` - Enhanced system overview and usage guide
- `skills/_COMPASS/SKILL.md` - Comprehensive skill documentation
- `skills/_COMPASS/agents/*.md` - Individual agent documentation
- `skills/README.md` - Quick start guide
- `scripts/setup-shaka.sh` - Automated setup script

### Features

#### NewsletterAgent
- 8-phase pipeline (pre-flight → data → strategy → research → writing → style → technical → build)
- Data collection from 100+ GitHub projects
- Nostr relay discussion integration
- NIP deep dive rotation tracking
- Topic page generation with source attribution
- Style compliance enforcement (no em dashes, AI buzzwords)
- Flowing prose generation (not bullet lists)
- Critical source linking validation

#### TranslationAgent
- Sequential 9-language translation (de, es, fr, it, ja, ko, nl, pt, zh)
- Unicode character encoding validation (ä not ae, é not e)
- Technical term preservation
- Internal link management
- Staleness detection
- Translation metadata tracking

#### ValidationAgent
- 10 comprehensive validation checks
- Link integrity (internal and external)
- NIP reference validation
- Unlinked mention detection (PR #XXX without link)
- Deep dive duplication check
- Redundancy analysis
- Style compliance detection
- Frontmatter validation
- JSON event field validation
- Topic page source link validation

#### PublishingAgent
- TLDR generation (exactly 21 words)
- Social media content (Twitter/X, Nostr)
- Email distribution preparation
- URL absolutization
- Distribution checklists
- Outreach suggestions

#### PodcastAgent
- Pre-recording: Discussion questions, research notes, timing
- Post-recording: Timestamps, show notes, announcements
- Content transformation (written → spoken)
- Guest coordination materials
- Clip suggestions for promotion

### Integration
- Global Shaka settings integration
- Environment variable support (COMPASS_DIR, GITHUB_TOKEN)
- Dual interface (Shaka commands + OpenCode compatibility)

### Quality Assurance
- Source attribution enforcement (every PR/release must be linked)
- Unicode encoding validation (proper characters, not ASCII substitutes)
- Style guideline enforcement (no em dashes, AI buzzwords)
- Link integrity validation (internal and external)
- NIP reference validation

## [Unreleased]

### Planned
- Automated testing for validation checks
- GitHub Actions integration for CI/CD
- Additional language support beyond 9 current languages
- Voice synthesis integration for podcast narration
- Automated social media posting integration

## Version History

### Version Numbering
- **Major (X.0.0)**: Breaking changes to skill interface or agent behavior
- **Minor (1.X.0)**: New features, agents, or commands
- **Patch (1.0.X)**: Bug fixes, documentation updates, minor improvements

---

*Building with Shaka - Magnifying human capabilities through personalized AI infrastructure*
