# Compass Data Fetching Scripts

Scripts for collecting data from various sources for the Nostr Compass newsletter.

## Requirements

### For Nostr Scripts (bash)
```bash
# Install nak (nostr army knife)
go install github.com/fiatjaf/nak@latest

# Install jq
apt install jq  # Debian/Ubuntu
brew install jq # macOS
```

### For GitHub Scripts (Python)
```bash
pip install -r requirements.txt

# Set GitHub token for higher rate limits
export GITHUB_TOKEN=your_token_here
# Or create scripts/.env with: GITHUB_TOKEN=your_token_here
```

## Scripts

### Nostr Data Fetchers

All Nostr scripts share common configuration via `nostr_common.sh`:
- Standardized relay list (7 relays)
- Common helper functions
- Consistent argument parsing

| Script | Purpose | Default Days | Output |
|--------|---------|--------------|--------|
| `fetch_nostr_recap.sh` | Weekly summaries from Nostr Recap | 14 | `data/nostr_recap/` |
| `fetch_nostr_nip_discussions.sh` | NIP-related discussions | 7 | `data/nostr_nip_discussions/` |
| `fetch_shakespeare_apps.sh` | Soapbox MiniApps showcase | 7 | `data/shakespeare_apps/` |

### GitHub Data Fetcher

| Script | Purpose | Default Days | Output |
|--------|---------|--------------|--------|
| `fetch_project_updates.py` | Releases, PRs, commits | 7 (auto-detect) | `data/project_updates/` |

## Usage Examples

```bash
# Fetch Nostr Recap posts from last 2 weeks
./fetch_nostr_recap.sh

# Fetch NIP discussions from last week
./fetch_nostr_nip_discussions.sh

# Fetch all Shakespeare apps
./fetch_shakespeare_apps.sh --since-days 30

# Fetch only featured Shakespeare apps
./fetch_shakespeare_apps.sh --featured-only

# Fetch GitHub project updates (auto-detects time range)
python3 fetch_project_updates.py

# Fetch specific projects only
python3 fetch_project_updates.py --projects "Damus,Amethyst"

# Fetch specific categories
python3 fetch_project_updates.py --categories "social_clients,wallets"
```

## Output Format

All scripts output JSON with consistent structure:

```json
{
  "generated_at": "2026-02-03T12:00:00Z",
  "period": {
    "start": "2026-01-27",
    "end": "2026-02-03",
    "days": 7
  },
  "summary": { ... },
  ...
}
```

Output files are named with date ranges: `{type}_{start}_{end}.json`

## Configuration

### Relay List

The standard relay list is defined in `nostr_common.sh`:
- wss://relay.damus.io
- wss://nos.lol
- wss://relay.nostr.band
- wss://relay.snort.social
- wss://nostr.wine
- wss://relay.primal.net
- wss://ditto.pub/relay

### Environment Variables

| Variable | Script | Purpose |
|----------|--------|---------|
| `GITHUB_TOKEN` | `fetch_project_updates.py` | Increase API rate limits |

## Data Flow

```
scripts/
├── fetch_nostr_recap.sh ─────────────► data/nostr_recap/
├── fetch_nostr_nip_discussions.sh ───► data/nostr_nip_discussions/
├── fetch_shakespeare_apps.sh ────────► data/shakespeare_apps/
└── fetch_project_updates.py ─────────► data/project_updates/
```

## Adding New Scripts

1. For Nostr scripts: source `nostr_common.sh` for shared functionality
2. Follow the established patterns:
   - Use `--since-days N` for time range
   - Support `-h|--help`
   - Output to `data/{source_name}/`
   - Use consistent JSON structure with `generated_at`, `period`, `summary`
