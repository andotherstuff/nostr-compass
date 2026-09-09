#!/bin/bash
#
# Common functions and configuration for Nostr fetch scripts
#
# Source this file at the top of any Nostr fetch script:
#   source "$(dirname "${BASH_SOURCE[0]}")/nostr_common.sh"
#
# Provides:
#   - PATH setup for nak
#   - Standard relay list
#   - Requirement checking
#   - Date calculation helpers
#   - Temp directory management
#

# Add nak locations to PATH
export PATH="$HOME/.local/bin:$HOME/go/bin:$PATH"

# Standard relay list for Nostr queries
# These relays have good uptime and broad event coverage
NOSTR_RELAYS=(
    "wss://relay.damus.io"
    "wss://nos.lol"
    "wss://relay.nostr.band"
    "wss://relay.snort.social"
    "wss://nostr.wine"
    "wss://relay.primal.net"
    "wss://ditto.pub/relay"
)

# Check for required tools (nak and jq)
check_nostr_requirements() {
    if ! command -v nak &> /dev/null; then
        echo "Error: nak is not installed" >&2
        echo "Install with: go install github.com/fiatjaf/nak@latest" >&2
        return 1
    fi

    if ! command -v jq &> /dev/null; then
        echo "Error: jq is not installed" >&2
        echo "Install with your package manager (apt install jq, brew install jq, etc.)" >&2
        return 1
    fi

    return 0
}

# Calculate start date (handles both GNU and BSD date)
# Usage: calc_start_date DAYS_AGO
# Returns: YYYY-MM-DD format date
calc_start_date() {
    local days_ago="$1"
    if [ -n "${COMPASS_WINDOW_SINCE:-}" ]; then
        date -u -d "$COMPASS_WINDOW_SINCE" +%Y-%m-%d
        return
    fi
    date -d "-${days_ago} days" +%Y-%m-%d 2>/dev/null || date -v-${days_ago}d +%Y-%m-%d
}

# Calculate Unix timestamp for N days ago
# Usage: calc_since_timestamp DAYS_AGO
calc_since_timestamp() {
    local days_ago="$1"
    if [ -n "${COMPASS_WINDOW_SINCE:-}" ]; then
        date -u -d "$COMPASS_WINDOW_SINCE" +%s
        return
    fi
    echo $(($(date +%s) - (days_ago * 86400)))
}

# Exclusive upper bound for exact-pass relay queries.
calc_until_timestamp() {
    if [ -n "${COMPASS_WINDOW_UNTIL:-}" ]; then
        # NIP-01 `until` is inclusive; subtract one second to implement the
        # workflow contract's exclusive upper bound.
        echo $(($(date -u -d "$COMPASS_WINDOW_UNTIL" +%s) - 1))
    else
        date +%s
    fi
}

# Persist one page exactly as observed by a bounded relay query.  Receipt
# validation rejects pages without both pass bounds or a terminal exhausted page.
record_exact_page() {
    local file="$1" source="$2" cursor="$3" count="$4" cap="$5" exhausted="$6"
    [ -n "${COMPASS_SOURCE_PASS_ID:-}" ] || return 0
    [ -n "${COMPASS_WINDOW_SINCE:-}" ] && [ -n "${COMPASS_WINDOW_UNTIL:-}" ] || {
        echo "Compass source pass environment is incomplete" >&2
        return 1
    }
    jq -nc --arg source "$source" --arg cursor "$cursor" \
        --argjson count "$count" --argjson cap "$cap" --argjson exhausted "$exhausted" \
        --arg since "$COMPASS_WINDOW_SINCE" --arg until "$COMPASS_WINDOW_UNTIL" \
        '{source:$source,cursor:(if $cursor == "" then null else $cursor end),count:$count,cap:$cap,exhausted:$exhausted,effective_since:$since,effective_until:$until}' >> "$file"
}

# Get current date in YYYY-MM-DD format
get_today() {
    if [ -n "${COMPASS_WINDOW_UNTIL:-}" ]; then
        date -u -d "$COMPASS_WINDOW_UNTIL" +%Y-%m-%d
        return
    fi
    date +%Y-%m-%d
}

# Format Unix timestamp for display (handles both GNU and BSD date)
# Usage: format_timestamp UNIX_TIMESTAMP
format_timestamp() {
    local ts="$1"
    date -d "@$ts" 2>/dev/null || date -r "$ts"
}

# Create temp directory with automatic cleanup
# Usage: setup_temp_dir
# Sets: NOSTR_TEMP_DIR variable
# Registers cleanup trap automatically
setup_temp_dir() {
    NOSTR_TEMP_DIR=$(mktemp -d)
    trap 'rm -rf "$NOSTR_TEMP_DIR"' EXIT
}

# Parse --since-days argument from command line
# Usage: parse_since_days DEFAULT_DAYS "$@"
# Returns: Number of days (prints to stdout)
# Note: Call with: SINCE_DAYS=$(parse_since_days 7 "$@")
parse_since_days() {
    local default="$1"
    shift
    local result="$default"

    while [[ $# -gt 0 ]]; do
        case $1 in
            --since-days)
                result="$2"
                shift 2
                ;;
            -h|--help)
                return 0
                ;;
            *)
                if [[ "$1" =~ ^[0-9]+$ ]]; then
                    result="$1"
                fi
                shift
                ;;
        esac
    done

    echo "$result"
}

# Standard help text for --since-days
print_since_days_help() {
    echo "  --since-days N  Number of days to look back (default: $1)"
}
