#!/bin/bash
# Fetch grantee activity feeds ("heartbeats") for discovery:
#   - OpenSats heartbeat: https://heartbeat.opensats.org/data/events.json
#     (static JSON, 90-day window, commits/PRs/issues/releases across funded repos)
#   - Sovereign Engineering: covered via the same heartbeat-style idea; the SEC
#     site links cohort projects, and most SEC cohort repos overlap with the
#     OpenSats nostr fund. We record the SEC projects page snapshot for triage.
#
# Output: data/heartbeats/heartbeat_<since>_<until>.json
#   { opensats: {nostr-fund events in window}, sovereign_engineering: {page fetch note} }
#
# Usage: fetch_heartbeats.sh <since_date> <until_date>   (YYYY-MM-DD)
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SINCE="${1:?usage: fetch_heartbeats.sh <since> <until>}"
UNTIL="${2:?usage: fetch_heartbeats.sh <since> <until>}"
OUT_DIR="$PROJECT_ROOT/data/heartbeats"
mkdir -p "$OUT_DIR"
OUT="$OUT_DIR/heartbeat_${SINCE}_${UNTIL}.json"

TMP_EVENTS="$(mktemp)"
trap 'rm -f "$TMP_EVENTS"' EXIT

echo "Fetching OpenSats heartbeat feed..."
if ! curl -sfL "https://heartbeat.opensats.org/data/events.json" -o "$TMP_EVENTS"; then
  echo "error: heartbeat feed fetch failed" >&2
  exit 1
fi

python3 - "$TMP_EVENTS" "$SINCE" "$UNTIL" "$OUT" <<'PYEOF'
import json, sys
src, since, until, out = sys.argv[1:5]
d = json.load(open(src))
nostr_repos = set(d.get('funds', {}).get('nostr', []))
general_repos = set(d.get('funds', {}).get('general', []))
def in_window(e):
    day = e['timestamp'][:10]
    return since <= day <= until
nostr_events = [e for e in d['events'] if e['repo'] in nostr_repos and in_window(e)]
general_events = [e for e in d['events'] if e['repo'] in general_repos and in_window(e)]
result = {
    'generated_at': d['generatedAt'],
    'window': {'since': since, 'until': until},
    'opensats_nostr_fund': {
        'repo_count': len(nostr_repos),
        'events': nostr_events,
    },
    'opensats_general_fund': {
        'repo_count': len(general_repos),
        'events': general_events,
    },
    'sovereign_engineering': {
        'note': 'SEC cohort projects page: https://sovereignengineering.io/ — no JSON feed; triage should treat OpenSats nostr-fund repos as the primary heartbeat source and check the SEC site manually for cohort-only projects not in the feed.',
        'url': 'https://sovereignengineering.io/',
    },
}
json.dump(result, open(out, 'w'), indent=2)
print(f"nostr-fund events in window: {len(nostr_events)} across {len(set(e['repo'] for e in nostr_events))} repos")
print(f"general-fund events in window: {len(general_events)} across {len(set(e['repo'] for e in general_events))} repos")
print(f"wrote {out}")
PYEOF
