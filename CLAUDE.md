# Nostr Compass Newsletter Guidelines

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