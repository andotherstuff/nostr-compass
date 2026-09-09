#!/bin/bash
# Collect OpenSats and Sovereign Engineering heartbeat candidates for [since, until).
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SINCE="${1:?usage: fetch_heartbeats.sh <since> <until>}"
UNTIL="${2:?usage: fetch_heartbeats.sh <since> <until>}"
EFFECTIVE_SINCE="${COMPASS_WINDOW_SINCE:-${SINCE}T00:00:00Z}"
EFFECTIVE_UNTIL="${COMPASS_WINDOW_UNTIL:-${UNTIL}T00:00:00Z}"
OUT_DIR="$PROJECT_ROOT/data/heartbeats"; mkdir -p "$OUT_DIR"
OUT="$OUT_DIR/heartbeat_${SINCE}_${UNTIL}.json"
TMP_EVENTS="$(mktemp)"; TMP_SEC="$(mktemp)"; EVIDENCE="$(mktemp)"
trap 'rm -f "$TMP_EVENTS" "$TMP_SEC" "$EVIDENCE"' EXIT
STARTED=$(date -u +%Y-%m-%dT%H:%M:%SZ)

curl -sfL "https://heartbeat.opensats.org/data/events.json" -o "$TMP_EVENTS" || { echo "error: heartbeat feed fetch failed" >&2; exit 1; }
python3 "$SCRIPT_DIR/fetch_sovereign_engineering.py" --since "$EFFECTIVE_SINCE" --until "$EFFECTIVE_UNTIL" --output "$TMP_SEC" || { echo "error: Sovereign Engineering discovery failed" >&2; exit 1; }

python3 - "$TMP_EVENTS" "$TMP_SEC" "$EFFECTIVE_SINCE" "$EFFECTIVE_UNTIL" "$OUT" <<'PYEOF'
import json, sys
from datetime import datetime
src, sec_src, since, until, out = sys.argv[1:]
d=json.load(open(src)); sec=json.load(open(sec_src)); start=datetime.fromisoformat(since.replace('Z','+00:00')); end=datetime.fromisoformat(until.replace('Z','+00:00'))
nostr=set(d.get('funds',{}).get('nostr',[])); general=set(d.get('funds',{}).get('general',[]))
def inside(e):
    value=datetime.fromisoformat(e['timestamp'].replace('Z','+00:00'))
    return start <= value < end
ne=[e for e in d['events'] if e['repo'] in nostr and inside(e)]; ge=[e for e in d['events'] if e['repo'] in general and inside(e)]
result={'generated_at':d['generatedAt'],'window':{'since':since,'until':until},'opensats_nostr_fund':{'repo_count':len(nostr),'events':ne},'opensats_general_fund':{'repo_count':len(general),'events':ge},'sovereign_engineering':sec}
json.dump(result,open(out,'w'),indent=2)
print(f"nostr-fund events in window: {len(ne)}"); print(f"general-fund events in window: {len(ge)}"); print(f"wrote {out}")
PYEOF

if [ -n "${COMPASS_SOURCE_PASS_ID:-}" ]; then
python3 - "$TMP_EVENTS" "$TMP_SEC" "$OUT" "$EFFECTIVE_SINCE" "$EFFECTIVE_UNTIL" "$STARTED" "$EVIDENCE" <<'PYEOF'
import json, sys
from datetime import datetime, timezone
raw_path,sec_path,out_path,since,until,started,target=sys.argv[1:]
raw=json.load(open(raw_path)); sec=json.load(open(sec_path)); out=json.load(open(out_path)); events=raw.get('events',[])
def eid(e,i): return str(e.get('id') or f"opensats:{e.get('repo')}:{e.get('timestamp')}:{i}")
kept_events=out['opensats_nostr_fund']['events']+out['opensats_general_fund']['events']; kept={eid(e,i) for i,e in enumerate(kept_events)}
ids=[]; dispositions={}
for i,event in enumerate(events):
    candidate=eid(event,i); ids.append(candidate); dispositions[candidate]={"decision":"include" if candidate in kept else "skip","reason":"retained by fund and exact-window filters" if candidate in kept else "outside selected funds or exact window"}
for event in sec['nostr']['events']:
    candidate=str(event['id']); ids.append(candidate); dispositions[candidate]={"decision":"include","reason":"verified Sovereign Engineering tagged event in exact window"}
pages=[{"source":"opensats-heartbeat-static-feed","cursor":None,"count":len(events),"cap":max(1,len(events)+1),"exhausted":True,"effective_since":since,"effective_until":until},*sec['_collector_evidence']['pages']]
evidence={"effective_since":since,"effective_until":until,"query_started_at":started,"query_finished_at":datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),"canonical_query":{"family":"heartbeats","since":since,"until":until,"sources":["opensats","sovereign-engineering"],"upper_bound_enforced":"collector"},"pages":pages,"failures":[],"candidate_ids":sorted(set(ids)),"dispositions":dispositions}
json.dump(evidence,open(target,'w'),indent=2)
PYEOF
python3 "$SCRIPT_DIR/source_collector_receipt.py" --family heartbeats --artifact "$OUT" --collector "$0" --evidence "$EVIDENCE"
fi
