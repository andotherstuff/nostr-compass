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
# Output:
#   JSON file in data/nostr_nip_discussions/ with NIP-related discussions
#

set -euo pipefail

# Get script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Parse arguments
SINCE_DAYS=7
while [[ $# -gt 0 ]]; do
    case $1 in
        --since-days)
            SINCE_DAYS="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 [--since-days N]"
            echo "  --since-days N  Number of days to look back (default: 7)"
            exit 0
            ;;
        *)
            # Support positional argument for backwards compatibility
            if [[ "$1" =~ ^[0-9]+$ ]]; then
                SINCE_DAYS="$1"
                shift
            else
                echo "Unknown option: $1"
                exit 1
            fi
            ;;
    esac
done
OUTPUT_DIR="$PROJECT_ROOT/data/nostr_nip_discussions"
RELAYS=(
    "wss://relay.damus.io"
    "wss://nos.lol"
    "wss://relay.nostr.band"
    "wss://relay.snort.social"
    "wss://nostr.wine"
)

# Calculate dates for filename
START_DATE=$(date -d "-${SINCE_DAYS} days" +%Y-%m-%d 2>/dev/null || date -v-${SINCE_DAYS}d +%Y-%m-%d)
END_DATE=$(date +%Y-%m-%d)
OUTPUT_FILE="$OUTPUT_DIR/discussions_${START_DATE}_${END_DATE}.json"

# Calculate since timestamp (Unix epoch)
SINCE_TIMESTAMP=$(($(date +%s) - (SINCE_DAYS * 86400)))

# Temp files for storing results (avoids argument list too long errors)
TEMP_DIR=$(mktemp -d)
LONGFORM_FILE="$TEMP_DIR/longform.json"
NOTES_FILE="$TEMP_DIR/notes.json"
COMMUNITY_FILE="$TEMP_DIR/community.json"

# Cleanup temp files on exit
cleanup() {
    rm -rf "$TEMP_DIR"
}
trap cleanup EXIT

# Check for required tools
check_requirements() {
    if ! command -v nak &> /dev/null; then
        echo "Error: nak is not installed"
        echo "Install with: go install github.com/fiatjaf/nak@latest"
        exit 1
    fi

    if ! command -v jq &> /dev/null; then
        echo "Error: jq is not installed"
        echo "Install with your package manager (apt install jq, brew install jq, etc.)"
        exit 1
    fi
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
    # Use jq with file inputs instead of command-line arguments
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

    # Initialize empty array
    echo "[]" > "$LONGFORM_FILE"

    for relay in "${RELAYS[@]}"; do
        echo "  Querying $relay..." >&2
        nak req -k 30817 --since "$SINCE_TIMESTAMP" --limit 50 "$relay" 2>/dev/null || true
    done | jq -s 'unique_by(.id)' > "$LONGFORM_FILE"

    local count=$(jq 'length' "$LONGFORM_FILE")
    echo "  Found $count custom NIP documents" >&2

    # Save progress after each fetch type
    save_progress
}

# Fetch long-form articles specifically discussing NIPs (kind 30023)
fetch_nip_articles() {
    local ARTICLES_FILE="$TEMP_DIR/articles.json"
    echo "Fetching long-form NIP articles (kind 30023)..." >&2

    # Initialize empty array
    echo "[]" > "$ARTICLES_FILE"

    for relay in "${RELAYS[@]}"; do
        echo "  Querying $relay..." >&2
        # Search for articles tagged with "nip" or "nips"
        nak req -k 30023 --since "$SINCE_TIMESTAMP" --limit 50 -t t=nip "$relay" 2>/dev/null || true
        nak req -k 30023 --since "$SINCE_TIMESTAMP" --limit 50 -t t=nips "$relay" 2>/dev/null || true
    done | jq -s 'unique_by(.id) | map(select(
        # Must contain actual NIP references like NIP-01, NIP-29, etc.
        .content | test("NIP-[0-9]+"; "i")
    ))' > "$ARTICLES_FILE"

    # Merge with LONGFORM_FILE (which has custom NIPs)
    jq -s 'flatten | unique_by(.id)' "$LONGFORM_FILE" "$ARTICLES_FILE" > "$TEMP_DIR/merged.json"
    mv "$TEMP_DIR/merged.json" "$LONGFORM_FILE"

    local count=$(jq 'length' "$LONGFORM_FILE")
    echo "  Total NIP-related long-form content: $count" >&2

    # Save progress after each fetch type
    save_progress
}

# Fetch notes mentioning specific NIPs (kind 1)
fetch_nip_notes() {
    echo "Fetching notes mentioning NIPs (kind 1)..." >&2

    # Initialize empty array
    echo "[]" > "$NOTES_FILE"

    for relay in "${RELAYS[@]}"; do
        echo "  Querying $relay..." >&2
        # Search for notes tagged with nip/nips
        nak req -k 1 --since "$SINCE_TIMESTAMP" --limit 100 -t t=nip "$relay" 2>/dev/null || true
        nak req -k 1 --since "$SINCE_TIMESTAMP" --limit 100 -t t=nips "$relay" 2>/dev/null || true
        nak req -k 1 --since "$SINCE_TIMESTAMP" --limit 100 -t t=nostrhub "$relay" 2>/dev/null || true
    done | jq -s 'unique_by(.id) | map(select(
        # Must contain actual NIP references like NIP-01, NIP-29, etc. OR mention nostrhub
        .content | test("NIP-[0-9]+|nostrhub"; "i")
    ))' > "$NOTES_FILE"

    local count=$(jq 'length' "$NOTES_FILE")
    echo "  Found $count notes" >&2

    # Save progress after each fetch type
    save_progress
}

# Fetch NIP-72 community posts related to NIPs
fetch_community_posts() {
    echo "Fetching community posts (NIP-72)..." >&2

    # Initialize empty array
    echo "[]" > "$COMMUNITY_FILE"

    for relay in "${RELAYS[@]}"; do
        echo "  Querying $relay..." >&2
        # Kind 34550 = community definition
        nak req -k 34550 --since "$SINCE_TIMESTAMP" --limit 20 "$relay" 2>/dev/null || true
    done | jq -s 'unique_by(.id) | map(select(
        # Only include communities specifically about NIPs
        (.content | test("NIP-[0-9]+"; "i")) or
        (.tags | map(select(.[0] == "d")) | flatten | any(test("^nip"; "i")))
    ))' > "$COMMUNITY_FILE"

    local count=$(jq 'length' "$COMMUNITY_FILE")
    echo "  Found $count community posts" >&2

    # Save progress after each fetch type
    save_progress
}

# Main execution
main() {
    check_requirements

    echo "Fetching NIP discussions from Nostr relays (last $SINCE_DAYS days)..." >&2
    echo "Since timestamp: $SINCE_TIMESTAMP ($(date -d "@$SINCE_TIMESTAMP" 2>/dev/null || date -r "$SINCE_TIMESTAMP"))" >&2
    echo "" >&2

    # Initialize temp files with empty arrays
    echo "[]" > "$LONGFORM_FILE"
    echo "[]" > "$NOTES_FILE"
    echo "[]" > "$COMMUNITY_FILE"

    # Initialize output file
    init_output

    # Fetch each type (saves progress after each)
    # 1. Custom NIP documents (kind 30817)
    fetch_custom_nips
    # 2. Long-form articles discussing NIPs (kind 30023 with NIP-XX references)
    fetch_nip_articles
    # 3. Notes mentioning NIPs (kind 1)
    fetch_nip_notes
    # 4. Community posts about NIPs
    fetch_community_posts

    echo "" >&2
    echo "Final results saved to: $OUTPUT_FILE" >&2
    echo "Summary:" >&2
    jq '.summary' "$OUTPUT_FILE" >&2
}

main "$@"
