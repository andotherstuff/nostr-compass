#!/bin/bash
#
# Fetch Shakespeare app submissions from Nostr relays
#
# Shakespeare is Soapbox's app showcase for MiniApps built on Nostr.
# Apps are published as Nostr events:
#   - Kind 31733 (addressable event)
#   - Tag: #t soapbox-app-submission
#
# Requirements:
#   - nak (nostr army knife): go install github.com/fiatjaf/nak@latest
#   - jq: for JSON processing
#
# Usage:
#   ./fetch_shakespeare_apps.sh [OPTIONS]
#
# Examples:
#   ./fetch_shakespeare_apps.sh                    # Default: last 7 days
#   ./fetch_shakespeare_apps.sh --since-days 30
#   ./fetch_shakespeare_apps.sh --approved-only
#   ./fetch_shakespeare_apps.sh --featured-only
#
# Output:
#   JSON file in data/shakespeare_apps/ with app submissions
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
APPROVED_ONLY=false
FEATURED_ONLY=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --since-days)
            SINCE_DAYS="$2"
            shift 2
            ;;
        --approved-only)
            APPROVED_ONLY=true
            shift
            ;;
        --featured-only)
            FEATURED_ONLY=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Fetch Shakespeare app submissions from Nostr relays."
            echo ""
            echo "Options:"
            print_since_days_help "$DEFAULT_DAYS"
            echo "  --approved-only   Only include approved apps"
            echo "  --featured-only   Only include featured apps"
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
OUTPUT_DIR="$PROJECT_ROOT/data/shakespeare_apps"
START_DATE=$(calc_start_date "$SINCE_DAYS")
END_DATE=$(get_today)
OUTPUT_FILE="$OUTPUT_DIR/apps_${START_DATE}_${END_DATE}.json"
SINCE_TIMESTAMP=$(calc_since_timestamp "$SINCE_DAYS")

# Setup temp directory (auto-cleanup on exit)
setup_temp_dir
APPS_FILE="$NOSTR_TEMP_DIR/apps.json"

# Save current progress to output file
save_progress() {
    jq --arg generated_at "$(date -Iseconds)" \
       --arg start "$START_DATE" \
       --arg end "$END_DATE" \
       --argjson days "$SINCE_DAYS" \
       --argjson since_ts "$SINCE_TIMESTAMP" \
       '
        [.[] | {
            id: .id,
            pubkey: .pubkey,
            created_at: .created_at,
            created_at_iso: (.created_at | todateiso8601),
            d_tag: (.tags | map(select(.[0] == "d")) | .[0][1] // ""),
            title: (.tags | map(select(.[0] == "title")) | .[0][1] // ""),
            website: (.tags | map(select(.[0] == "website")) | .[0][1] // ""),
            repository: (.tags | map(select(.[0] == "repository")) | .[0][1] // ""),
            icon: (.tags | map(select(.[0] == "icon")) | .[0][1] // ""),
            screenshot: (.tags | map(select(.[0] == "screenshot")) | .[0][1] // ""),
            author_npub: (.tags | map(select(.[0] == "author")) | .[0][1] // ""),
            app_tags: [.tags | .[] | select(.[0] == "app-tag") | .[1]],
            is_approved: ([.tags | .[] | select(.[0] == "approved")] | length > 0),
            is_featured: ([.tags | .[] | select(.[0] == "featured")] | length > 0),
            content: .content
        }]
        | sort_by(.created_at) | reverse
        | . as $all_submissions
        | unique_by(.website)
        | . as $unique_apps
        | {
            generated_at: $generated_at,
            period: {
                start: $start,
                end: $end,
                days: $days
            },
            summary: {
                total_submissions: ($all_submissions | length),
                unique_apps: ($unique_apps | length),
                new_in_period: [$unique_apps[] | select(.created_at >= $since_ts)] | length
            },
            apps: $unique_apps
        }
       ' "$APPS_FILE" > "$OUTPUT_FILE"

    echo "Progress saved to $OUTPUT_FILE" >&2
}

# Fetch Shakespeare app submissions (kind 31733)
fetch_apps() {
    echo "Fetching Shakespeare app submissions (kind 31733)..." >&2
    echo "" >&2

    echo "[]" > "$APPS_FILE"

    for relay in "${NOSTR_RELAYS[@]}"; do
        echo "  Querying $relay..." >&2
        nak req -k 31733 -t t=soapbox-app-submission --limit 200 "$relay" 2>/dev/null || true
    done | jq -s 'unique_by(.id)' > "$APPS_FILE"

    local count=$(jq 'length' "$APPS_FILE")
    echo "" >&2
    echo "  Found $count total app submissions" >&2

    # Apply status filters if requested
    if [ "$FEATURED_ONLY" = true ]; then
        echo "  Filtering for featured apps only..." >&2
        jq '[.[] | select(.tags | map(select(.[0] == "featured")) | length > 0)]' "$APPS_FILE" > "$NOSTR_TEMP_DIR/filtered.json"
        mv "$NOSTR_TEMP_DIR/filtered.json" "$APPS_FILE"
        count=$(jq 'length' "$APPS_FILE")
        echo "  $count featured apps" >&2
    elif [ "$APPROVED_ONLY" = true ]; then
        echo "  Filtering for approved apps only..." >&2
        jq '[.[] | select(.tags | map(select(.[0] == "approved")) | length > 0)]' "$APPS_FILE" > "$NOSTR_TEMP_DIR/filtered.json"
        mv "$NOSTR_TEMP_DIR/filtered.json" "$APPS_FILE"
        count=$(jq 'length' "$APPS_FILE")
        echo "  $count approved apps" >&2
    fi

    save_progress
}

# Print summary
print_summary() {
    echo "" >&2
    echo "========================================" >&2
    echo "SHAKESPEARE APPS SUMMARY" >&2
    echo "========================================" >&2
    jq -r '
        "Total submissions: \(.summary.total_submissions)",
        "Unique apps: \(.summary.unique_apps)",
        "New in last \(.period.days) days: \(.summary.new_in_period)",
        "",
        "Apps:",
        (.apps[:20] | .[] | "  - \(.title // .d_tag // "Untitled") (\(.website // "no website"))")
    ' "$OUTPUT_FILE" >&2

    local total=$(jq '.summary.unique_apps' "$OUTPUT_FILE")
    if [ "$total" -gt 20 ]; then
        echo "  ... and $((total - 20)) more" >&2
    fi
    echo "" >&2
}

# Main execution
main() {
    check_nostr_requirements || exit 1

    echo "========================================" >&2
    echo "Shakespeare App Fetcher" >&2
    echo "========================================" >&2
    echo "Looking back: $SINCE_DAYS days" >&2
    echo "Since timestamp: $SINCE_TIMESTAMP ($(format_timestamp "$SINCE_TIMESTAMP"))" >&2
    if [ "$FEATURED_ONLY" = true ]; then
        echo "Filter: Featured only" >&2
    elif [ "$APPROVED_ONLY" = true ]; then
        echo "Filter: Approved only" >&2
    fi
    echo "" >&2

    # Create output directory
    mkdir -p "$OUTPUT_DIR"

    # Fetch apps
    fetch_apps

    # Print summary
    print_summary

    echo "Results saved to: $OUTPUT_FILE" >&2
}

main "$@"
