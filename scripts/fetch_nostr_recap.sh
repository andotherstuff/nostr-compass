#!/bin/bash
#
# Fetch Nostr Recap weekly summaries from Nostr relays
#
# Nostr Recap publishes weekly ecosystem summaries with 9 sections:
#   #1 Quotes of the Week
#   #2 Community Highlights
#   #3 Ecosystem Growth
#   #4 Educational Guides
#   #5 Upcoming Events
#   #6 Nostr in the Media
#   #7 Most Zapped Last Week
#   #8 Nostr Memes
#   #9 Tools, Updates and Releases
#
# Usage:
#   ./fetch_nostr_recap.sh                # Default: last 7 days
#   ./fetch_nostr_recap.sh --since-days 7 # Custom range
#
# Prerequisites: nak, jq
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/nostr_common.sh"

# Configuration
DEFAULT_DAYS=7
OUTPUT_DIR="$(dirname "$SCRIPT_DIR")/data/nostr_recap"

# Nostr Recap author pubkey (npub1etjm06353tl0cnqs9wmmzfwyj283z3ee5facwlrte7l957fgqwzqsznr68)
RECAP_PUBKEY="cae5b7ea348afefc4c102bb7b125c4928f114739a27b877c6bcfbe5a79280384"

# Recap hashtag suffixes used on kind 1 posts
RECAP_TAGS=("tools_nostr_recap" "dev-tools_nostr_recap" "eco-growth_nostr_recap" "events_nostr_recap" "media_nostr_recap" "community_nostr_recap" "quote_nostr_recap" "most-zapped_nostr_recap" "memes_nostr_recap" "education_nostr_recap" "relays_nostr_recap" "bots_nostr_recap")

# Help
if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
    echo "Usage: $0 [--since-days N]"
    echo ""
    echo "Fetches Nostr Recap weekly summaries from relays."
    echo ""
    echo "Options:"
    print_since_days_help "$DEFAULT_DAYS"
    echo "  -h, --help      Show this help"
    exit 0
fi

# Check requirements
if ! check_nostr_requirements; then
    exit 1
fi

# Parse arguments
SINCE_DAYS=$(parse_since_days "$DEFAULT_DAYS" "$@")

# Calculate time range
SINCE_TS=$(calc_since_timestamp "$SINCE_DAYS")
START_DATE=$(calc_start_date "$SINCE_DAYS")
END_DATE=$(get_today)

echo "Fetching Nostr Recap posts from last $SINCE_DAYS days..."
echo "  Time range: $START_DATE to $END_DATE"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Setup temp directory
setup_temp_dir

# Build relay arguments
RELAY_ARGS=""
for relay in "${NOSTR_RELAYS[@]}"; do
    RELAY_ARGS="$RELAY_ARGS $relay"
done

RESULTS_FILE="$NOSTR_TEMP_DIR/recap_results.json"
echo "[]" > "$RESULTS_FILE"

# Strategy 1: Fetch all kind 1 notes from the Nostr Recap author in the time window
echo "Fetching posts from Nostr Recap author ($RECAP_PUBKEY)..."
nak req \
    --kind 1 \
    --author "$RECAP_PUBKEY" \
    --since "$SINCE_TS" \
    $RELAY_ARGS 2>/dev/null | \
jq -c '{
    id: .id,
    pubkey: .pubkey,
    kind: .kind,
    created_at: .created_at,
    tags: [.tags[] | select(.[0] == "t" or .[0] == "subject" or .[0] == "title" or .[0] == "p")],
    content: .content
}' >> "$NOSTR_TEMP_DIR/raw_results.jsonl" 2>/dev/null || true

# Strategy 2: Also fetch long-form articles (kind 30023) from the same author
echo "Fetching long-form articles from Nostr Recap author..."
nak req \
    --kind 30023 \
    --author "$RECAP_PUBKEY" \
    --since "$SINCE_TS" \
    $RELAY_ARGS 2>/dev/null | \
jq -c '{
    id: .id,
    pubkey: .pubkey,
    kind: .kind,
    created_at: .created_at,
    tags: [.tags[] | select(.[0] == "t" or .[0] == "title" or .[0] == "summary" or .[0] == "d")],
    content: .content
}' >> "$NOSTR_TEMP_DIR/raw_results.jsonl" 2>/dev/null || true

# Deduplicate by event ID
if [ -f "$NOSTR_TEMP_DIR/raw_results.jsonl" ] && [ -s "$NOSTR_TEMP_DIR/raw_results.jsonl" ]; then
    TOTAL=$(wc -l < "$NOSTR_TEMP_DIR/raw_results.jsonl")
    echo "Found $TOTAL raw results, deduplicating..."

    # Deduplicate and convert to array
    jq -s 'unique_by(.id) | sort_by(-.created_at)' \
        "$NOSTR_TEMP_DIR/raw_results.jsonl" > "$RESULTS_FILE"

    UNIQUE=$(jq 'length' "$RESULTS_FILE")
    echo "After dedup: $UNIQUE unique events"
else
    echo "No results found."
    echo "[]" > "$RESULTS_FILE"
fi

# Build output file
OUTPUT_FILE="$OUTPUT_DIR/recap_${START_DATE}_${END_DATE}.json"

jq --arg start "$START_DATE" \
   --arg end "$END_DATE" \
   --arg days "$SINCE_DAYS" \
   --arg generated "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
   '{
    generated_at: $generated,
    period: {
        start: $start,
        end: $end,
        days: ($days | tonumber)
    },
    summary: {
        total_events: length
    },
    events: .
}' "$RESULTS_FILE" > "$OUTPUT_FILE"

echo ""
echo "Output saved to: $OUTPUT_FILE"
echo "Events found: $(jq '.summary.total_events' "$OUTPUT_FILE")"
