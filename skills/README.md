# Nostr Compass Skills

Shaka skills for the Nostr Compass AI infrastructure.

## Quick Start

### 1. Register Skill with Global Shaka

The `_COMPASS` skill should be registered in your global Shaka settings.

**Option A: Automatic (Recommended)**
```bash
# From the compass directory
bash scripts/setup-pai.sh
```

**Option B: Manual**

Edit `~/.claude/settings.json` to include:

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

### 2. Environment Setup

Set environment variables in `~/.claude/.env` or your shell:

```bash
COMPASS_DIR=$COMPASS_DIR
GITHUB_TOKEN=<your-github-token>  # Optional but recommended for fetch scripts
```

### 3. Verify Installation

```bash
# In a Shaka-enabled Claude Code session
/newsletter --help

# Should show the newsletter command documentation
```

## Available Skills

### _COMPASS

**Description:** Comprehensive Nostr Compass AI infrastructure

**Commands:**
- `/newsletter` - Multi-phase newsletter generation
- `/translate` - Sequential 9-language translation
- `/validate` - Technical accuracy and link integrity validation
- `/publish` - Publishing materials generation
- `/podcast-prep` - Podcast preparation (before recording)
- `/podcast-publish` - Podcast publishing (after recording)

**Agents:**
- **NewsletterAgent** - Multi-phase newsletter generation specialist
- **TranslationAgent** - Multi-language translation with encoding expertise
- **ValidationAgent** - Technical accuracy and link integrity validator
- **PublishingAgent** - Publishing materials generator
- **PodcastAgent** - Podcast preparation and publishing specialist

**Documentation:**
- [Main Skill Documentation](\_COMPASS/SKILL.md)
- [NewsletterAgent](\_COMPASS/agents/NewsletterAgent.md)
- [TranslationAgent](\_COMPASS/agents/TranslationAgent.md)
- [ValidationAgent](\_COMPASS/agents/ValidationAgent.md)
- [PublishingAgent](\_COMPASS/agents/PublishingAgent.md)
- [PodcastAgent](\_COMPASS/agents/PodcastAgent.md)

## Architecture

```
skills/
└── _COMPASS/                   # Main skill
    ├── SKILL.md                # Comprehensive documentation
    └── agents/                 # Specialized agents
        ├── NewsletterAgent.md
        ├── TranslationAgent.md
        ├── ValidationAgent.md
        ├── PublishingAgent.md
        └── PodcastAgent.md
```

## Integration with .opencode/

The `_COMPASS` skill provides the primary Shaka interface, while the `.opencode/` directory structure is preserved for backward compatibility with OpenCode.

**Both systems work in parallel:**
- Shaka commands: `/newsletter`, `/translate`, etc.
- OpenCode commands: Same commands through OpenCode interface

**Recommendation:** Use Shaka commands for new workflows, as they benefit from the enhanced agent system.

## Development

### Adding New Agents

1. Create agent file: `skills/_COMPASS/agents/NewAgent.md`
2. Follow the agent documentation template
3. Update `skills/_COMPASS/SKILL.md` to reference the new agent
4. Update `AGENTS.md` to document the new capability

### Modifying Existing Workflows

1. Edit the relevant agent documentation in `skills/_COMPASS/agents/`
2. Test changes in a Shaka-enabled session
3. Update `AGENTS.md` if user-facing changes
4. Consider backward compatibility with `.opencode/`

## Support

**Issues:** Report at https://github.com/andotherstuff/nostr-compass/issues

**Contact:** NIP-17 DM to npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923

## Version

**Shaka Integration:** v1.0
**Compass:** nostrcompass.org

---

*Building with Shaka - Magnifying human capabilities through personalized AI infrastructure*
