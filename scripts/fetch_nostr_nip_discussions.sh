#!/bin/bash
#
# Fetch NIP-related discussions from Nostr relays
#
# This script queries Nostr relays for NIP-related content that may not be
# captured by GitHub monitoring. It's designed to complement the newsletter
# generation process by finding discussions happening on Nostr itself.
#
# Requirements:
#   - nak (nostr army knife): go install github.com/fiatjaf/nak@latest
#   - jq: for JSON processing
#
# Usage:
#   ./fetch_nostr_nip_discussions.sh [--since-days N]
#
# Examples:
#   ./fetch_nostr_nip_discussions.sh              # Default: last 7 days
#   ./fetch_nostr_nip_discussions.sh --since-days 14
#   ./fetch_nostr_nip_discussions.sh 7            # Positional arg also works
#
# Output:
#   JSON file in data/nostr_nip_discussions/ with NIP-related discussions
#

set -euo pipefail

# Get script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Source common functions
source "$SCRIPT_DIR/nostr_common.sh"

# Configuration
DEFAULT_DAYS=7

# Parse arguments
SINCE_DAYS="$DEFAULT_DAYS"
while [[ $# -gt 0 ]]; do
    case $1 in
        --since-days)
            SINCE_DAYS="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 [--since-days N]"
            echo ""
            echo "Fetch NIP-related discussions from Nostr relays."
            echo ""
            echo "Options:"
            print_since_days_help "$DEFAULT_DAYS"
            echo "  -h, --help        Show this help message"
            exit 0
            ;;
        *)
            if [[ "$1" =~ ^[0-9]+$ ]]; then
                SINCE_DAYS="$1"
                shift
            else
                echo "Unknown option: $1" >&2
                exit 1
            fi
            ;;
    esac
done

# Setup paths and dates
OUTPUT_DIR="$PROJECT_ROOT/data/nostr_nip_discussions"
START_DATE=$(calc_start_date "$SINCE_DAYS")
END_DATE=$(get_today)
OUTPUT_FILE="$OUTPUT_DIR/discussions_${START_DATE}_${END_DATE}.json"
SINCE_TIMESTAMP=$(calc_since_timestamp "$SINCE_DAYS")
UNTIL_TIMESTAMP=$(calc_until_timestamp)
QUERY_STARTED_AT=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# Setup temp directory (auto-cleanup on exit)
setup_temp_dir
LONGFORM_FILE="$NOSTR_TEMP_DIR/longform.json"
NOTES_FILE="$NOSTR_TEMP_DIR/notes.json"
COMMUNITY_FILE="$NOSTR_TEMP_DIR/community.json"
RAW_CANDIDATES="$NOSTR_TEMP_DIR/raw-candidates.ndjson"
PAGES_FILE="$NOSTR_TEMP_DIR/pages.jsonl"
: > "$RAW_CANDIDATES"
: > "$PAGES_FILE"

relay_query() {
    local label="$1" cap="$2" output="$3"
    shift 3
    nak req "$@" --since "$SINCE_TIMESTAMP" --until "$UNTIL_TIMESTAMP" --limit "$cap" "${NOSTR_RELAYS[@]}" 2>/dev/null > "$output" || return 1
    local got exhausted=true
    got=$(grep -cve '^[[:space:]]*$' "$output" || true)
    [ "$got" -lt "$cap" ] || exhausted=false
    record_exact_page "$PAGES_FILE" "$label" "" "$got" "$cap" "$exhausted"
    [ "$exhausted" = true ] || { echo "$label reached its $cap-event cap" >&2; return 1; }
    cat "$output" >> "$RAW_CANDIDATES"
}

# Initialize output file with basic structure
init_output() {
    mkdir -p "$OUTPUT_DIR"
    cat > "$OUTPUT_FILE" << EOF
{
  "generated_at": "$(date -Iseconds)",
  "period": {
    "start": "$START_DATE",
    "end": "$END_DATE",
    "days": $SINCE_DAYS
  },
  "summary": {
    "nip_documents": 0,
    "nip_notes": 0,
    "nip_communities": 0
  },
  "nip_documents": [],
  "nip_notes": [],
  "nip_communities": []
}
EOF
    echo "Initialized output file: $OUTPUT_FILE" >&2
}

# Save current progress to output file
save_progress() {
    jq -n \
        --arg generated_at "$(date -Iseconds)" \
        --arg start "$START_DATE" \
        --arg end "$END_DATE" \
        --argjson days "$SINCE_DAYS" \
        --slurpfile nip_docs "$LONGFORM_FILE" \
        --slurpfile notes "$NOTES_FILE" \
        --slurpfile community "$COMMUNITY_FILE" \
        '{
            generated_at: $generated_at,
            period: {
                start: $start,
                end: $end,
                days: $days
            },
            summary: {
                nip_documents: ($nip_docs | flatten | length),
                nip_notes: ($notes | flatten | length),
                nip_communities: ($community | flatten | length)
            },
            nip_documents: ($nip_docs | flatten),
            nip_notes: ($notes | flatten),
            nip_communities: ($community | flatten)
        }' > "$OUTPUT_FILE"

    echo "Progress saved to $OUTPUT_FILE" >&2
}

# Fetch custom NIP documents (kind 30817) - NostrHub's NIP format
fetch_custom_nips() {
    echo "Fetching custom NIP documents (kind 30817)..." >&2

    echo "[]" > "$LONGFORM_FILE"

    local raw="$NOSTR_TEMP_DIR/custom-nips.ndjson"
    relay_query custom-nips 500 "$raw" -k 30817
    jq -s 'unique_by(.id) | map(select(
        .kind == 30817 and
        (.tags | any(.[0] == "client" and .[1] == "nostrhub.io")) and
        (.tags | any(.[0] == "title")) and
        (.tags | any(.[0] == "d"))
    ))' "$raw" > "$LONGFORM_FILE"

    local count=$(jq 'length' "$LONGFORM_FILE")
    echo "  Found $count custom NIP documents" >&2

    save_progress
}

# Fetch long-form articles specifically discussing NIPs (kind 30023)
fetch_nip_articles() {
    local ARTICLES_FILE="$NOSTR_TEMP_DIR/articles.json"
    echo "Fetching long-form NIP articles (kind 30023)..." >&2

    echo "[]" > "$ARTICLES_FILE"

    local raw_nip="$NOSTR_TEMP_DIR/articles-nip.ndjson" raw_nips="$NOSTR_TEMP_DIR/articles-nips.ndjson"
    relay_query articles-nip 500 "$raw_nip" -k 30023 -t t=nip
    relay_query articles-nips 500 "$raw_nips" -k 30023 -t t=nips
    jq -s 'unique_by(.id) | map(select(
        .content | test("NIP-[0-9]+"; "i")
    ))' "$raw_nip" "$raw_nips" > "$ARTICLES_FILE"

    jq -s 'flatten | unique_by(.id)' "$LONGFORM_FILE" "$ARTICLES_FILE" > "$NOSTR_TEMP_DIR/merged.json"
    mv "$NOSTR_TEMP_DIR/merged.json" "$LONGFORM_FILE"

    local count=$(jq 'length' "$LONGFORM_FILE")
    echo "  Total NIP-related long-form content: $count" >&2

    save_progress
}

# Fetch notes mentioning specific NIPs (kind 1)
fetch_nip_notes() {
    echo "Fetching notes mentioning NIPs (kind 1)..." >&2

    echo "[]" > "$NOTES_FILE"

    local raw_nip="$NOSTR_TEMP_DIR/notes-nip.ndjson" raw_nips="$NOSTR_TEMP_DIR/notes-nips.ndjson" raw_hub="$NOSTR_TEMP_DIR/notes-hub.ndjson"
    relay_query notes-nip 1000 "$raw_nip" -k 1 -t t=nip
    relay_query notes-nips 1000 "$raw_nips" -k 1 -t t=nips
    relay_query notes-nostrhub 1000 "$raw_hub" -k 1 -t t=nostrhub
    jq -s 'unique_by(.id) | map(select(
        .content | test("NIP-[0-9]+|nostrhub"; "i")
    ))' "$raw_nip" "$raw_nips" "$raw_hub" > "$NOTES_FILE"

    local count=$(jq 'length' "$NOTES_FILE")
    echo "  Found $count notes" >&2

    save_progress
}

# Fetch NIP-72 community posts related to NIPs
fetch_community_posts() {
    echo "Fetching community posts (NIP-72)..." >&2

    echo "[]" > "$COMMUNITY_FILE"

    local raw="$NOSTR_TEMP_DIR/community.ndjson"
    relay_query communities 500 "$raw" -k 34550
    jq -s 'unique_by(.id) | map(select(
        (.content | test("NIP-[0-9]+"; "i")) or
        (.tags | map(select(.[0] == "d")) | flatten | any(test("^nip"; "i")))
    ))' "$raw" > "$COMMUNITY_FILE"

    local count=$(jq 'length' "$COMMUNITY_FILE")
    echo "  Found $count community posts" >&2

    save_progress
}

# Main execution
main() {
    check_nostr_requirements || exit 1

    echo "Fetching NIP discussions from Nostr relays (last $SINCE_DAYS days)..." >&2
    echo "Since timestamp: $SINCE_TIMESTAMP ($(format_timestamp "$SINCE_TIMESTAMP"))" >&2
    echo "" >&2

    # Initialize temp files with empty arrays
    echo "[]" > "$LONGFORM_FILE"
    echo "[]" > "$NOTES_FILE"
    echo "[]" > "$COMMUNITY_FILE"

    # Initialize output file
    init_output

    # Fetch each type (saves progress after each)
    fetch_custom_nips
    fetch_nip_articles
    fetch_nip_notes
    fetch_community_posts

    echo "" >&2
    echo "Final results saved to: $OUTPUT_FILE" >&2
    echo "Summary:" >&2
    jq '.summary' "$OUTPUT_FILE" >&2

    if [ -n "${COMPASS_SOURCE_PASS_ID:-}" ]; then
        local evidence="$NOSTR_TEMP_DIR/source-evidence.json" finished
        finished=$(date -u +%Y-%m-%dT%H:%M:%SZ)
        jq -n --arg since "$COMPASS_WINDOW_SINCE" --arg until "$COMPASS_WINDOW_UNTIL" \
          --arg started "$QUERY_STARTED_AT" --arg finished "$finished" \
          --slurpfile pages "$PAGES_FILE" --slurpfile raw "$RAW_CANDIDATES" --slurpfile output "$OUTPUT_FILE" '
          ($raw | flatten | map(.id) | unique) as $ids |
          ([$output[0].nip_documents[]?.id,$output[0].nip_notes[]?.id,$output[0].nip_communities[]?.id] | unique) as $included |
          {effective_since:$since,effective_until:$until,query_started_at:$started,query_finished_at:$finished,
           canonical_query:{family:"nip-discussions",since:$since,until:$until,kinds:[1,30023,30817,34550],relay_count:7},
           pages:($pages|flatten),failures:[],candidate_ids:$ids,
           dispositions:($ids | map(. as $id | {key:$id,value:(if ($included|index($id)) then {decision:"include",reason:"matched a NIP discussion content and identity filter"} else {decision:"skip",reason:"did not match the collector NIP discussion filter"} end)}) | from_entries)}' > "$evidence"
        python3 "$SCRIPT_DIR/source_collector_receipt.py" --family nip-discussions --artifact "$OUTPUT_FILE" --collector "$0" --evidence "$evidence"
    fi
}

main "$@"
