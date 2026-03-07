#!/bin/bash
#
# Fetch NIP-34 (git-over-nostr) repository data from Nostr relays
#
# Two modes:
#   1. TRACK: Monitor known projects from data/nip34_tracked.yml for
#      repo updates, patches (kind 1617), and issues (kind 1621)
#   2. DISCOVER: Find new NIP-34 repos published in the time window,
#      filtering out noise (shakespeare, backups, test repos, etc.)
#
# Requirements:
#   - nak (nostr army knife): go install github.com/fiatjaf/nak@latest
#   - jq: for JSON processing
#
# Usage:
#   ./fetch_nip34_repos.sh                    # Both modes, last 7 days
#   ./fetch_nip34_repos.sh --since-days 14    # Both modes, last 14 days
#   ./fetch_nip34_repos.sh --track-only       # Only track known repos
#   ./fetch_nip34_repos.sh --discover-only    # Only discover new repos
#
# Output:
#   JSON file in data/nip34_repos/ with tracked + discovered repos
#

set -euo pipefail

# Get script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Source common functions
source "$SCRIPT_DIR/nostr_common.sh"

# Configuration
DEFAULT_DAYS=7
OUTPUT_DIR="$PROJECT_ROOT/data/nip34_repos"
TRACKED_FILE="$PROJECT_ROOT/data/nip34_tracked.yml"

# NIP-34 specific relays (relay.ngit.dev is the primary NIP-34 relay)
NIP34_RELAYS=(
    "wss://relay.ngit.dev"
    "wss://relay.damus.io"
    "wss://nos.lol"
    "wss://relay.nostr.band"
)

# NIP-34 event kinds
KIND_REPO=30617       # Repository announcement
KIND_PATCH=1617       # Patches (PRs)
KIND_ISSUE=1621       # Issues

# Parse arguments
MODE="both"  # both, track, discover
SINCE_DAYS="$DEFAULT_DAYS"
while [[ $# -gt 0 ]]; do
    case $1 in
        --since-days)
            SINCE_DAYS="$2"
            shift 2
            ;;
        --track-only)
            MODE="track"
            shift
            ;;
        --discover-only)
            MODE="discover"
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [--since-days N] [--track-only] [--discover-only]"
            echo ""
            echo "Fetch NIP-34 repository data from Nostr relays."
            echo ""
            echo "Modes:"
            echo "  (default)         Run both tracking and discovery"
            echo "  --track-only      Only monitor known repos from nip34_tracked.yml"
            echo "  --discover-only   Only discover new NIP-34 repos"
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
START_DATE=$(calc_start_date "$SINCE_DAYS")
END_DATE=$(get_today)
OUTPUT_FILE="$OUTPUT_DIR/nip34_${START_DATE}_${END_DATE}.json"
SINCE_TIMESTAMP=$(calc_since_timestamp "$SINCE_DAYS")

# Setup temp directory (auto-cleanup on exit)
setup_temp_dir
REPOS_RAW="$NOSTR_TEMP_DIR/repos_raw.jsonl"
PATCHES_RAW="$NOSTR_TEMP_DIR/patches_raw.jsonl"
ISSUES_RAW="$NOSTR_TEMP_DIR/issues_raw.jsonl"
TRACKED_RESULTS="$NOSTR_TEMP_DIR/tracked.json"
DISCOVERED_RESULTS="$NOSTR_TEMP_DIR/discovered.json"

# Initialize empty files
> "$REPOS_RAW"
> "$PATCHES_RAW"
> "$ISSUES_RAW"
echo "[]" > "$TRACKED_RESULTS"
echo "[]" > "$DISCOVERED_RESULTS"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# ============================================================================
# NOISE FILTERING
# ============================================================================

# Known noise pubkeys - these accounts consistently publish non-Nostr-project
# repos (daily backups, test repos, unrelated software, website builder output)
#
# To identify new noise pubkeys, run discovery mode and look for pubkeys with
# many unrelated repos. Then query:
#   nak req -k 30617 -a PUBKEY --limit 50 wss://relay.ngit.dev | jq '.tags[] | select(.[0]=="name")'
NOISE_PUBKEYS=(
    # melvincarvalho: daily date-named backups (20260101, 20260102...), plus
    # JavaScriptSolidServer, json-os, webacl, nip7, nip98 ecosystem repos
    # that are tangentially nostr-related at best
    "d769d2b81c051d2f2c0b437d0ffe39e00ff0f7161b520f0bd30811f4c057795f"

    # daniyal-dev96 / Pleb5 test account: grasp-N, test-N, pr-test-*, forks
    "40d8f6d79c105f34a426aa91c2bf1826ed77970a84e69702eb1e86138ed6e4c6"

    # Pleb5 alt: Amber-fork, cdk-fork, test-1-fork-*, TollGate-fork
    "d04ecf33a303a59852fdb681ed8b412201ba85d8d2199aec73cb62681d62aa90"

    # Random unrelated repos: algorithms, Super-mario-bros, Whisper-Live,
    # azure-aks-istio, pet-detector, shopstr forks
    "622b455cffa9c6100afe2bf0101b5a07e5f2bfc349cd08290526dddfd57ae91a"

    # Shakespeare website builder output (AI-generated app names)
    "06de1b0bb20adf5b125fbcbad1cb951cf8f7194bf4b24e8d0b588ed5cd609a4a"

    # npub14rg4...: experimental repos (backrooms-simulator, calendrier-republicain,
    # cashu-token-booklet, fal-ai-integration, nostr-keypair-booklet)
    "a8d1560d6a647d501699167246f237b36fb123f89168fda11dc743533fec7a08"

    # Agent Profile publisher (nostr.life hex-ID repos)
    "06c5d1f7b245885da93fc35521c32b467b315b3cf0c4ab928a8ff19ebc908220"
)

# Full noise check on a JSON repo event (passed via stdin)
# Outputs the event if it passes (is NOT noise), nothing if noise
filter_noise() {
    # Build pubkey exclusion list for jq
    local pubkey_json
    pubkey_json=$(printf '%s\n' "${NOISE_PUBKEYS[@]}" | jq -R -s 'split("\n") | map(select(. != ""))')

    jq -c --argjson noise_pubkeys "$pubkey_json" '
        # Extract fields for filtering
        . as $event |
        .pubkey as $pubkey |
        ([.tags[] | select(.[0]=="d")][0][1] // "") as $d_tag |
        ([.tags[] | select(.[0]=="name")][0][1] // "") as $name |
        ([.tags[] | select(.[0]=="clone")] | map(.[1]) | join(" ")) as $clones |
        ([.tags[] | select(.[0]=="description")][0][1] // "") as $desc |

        # Skip if no d_tag
        if ($d_tag == "") then empty

        # Skip known noise pubkeys
        elif ($noise_pubkeys | index($pubkey) != null) then empty

        # Skip shakespeare.diy clones
        elif ($clones | test("git\\.shakespeare\\.diy")) then empty

        # Skip melvincarvalho backups (catch any that slip through pubkey filter)
        elif ($clones | test("melvin\\.me")) then empty

        # Skip nostr.life agent profiles
        elif ($clones | test("nostr\\.life")) then empty

        # Skip localhost clone URLs (development/testing)
        elif ($clones | test("localhost")) then empty

        # Skip grasp-N and my-grasp-* test repos
        elif ($d_tag | test("^(my-)?grasp-?[0-9]*$")) then empty

        # Skip tmp.* test repos
        elif ($d_tag | test("^tmp\\.")) then empty

        # Skip test repos (test-*, pr-test-*, *-test, *-test-*, testN, *-tset)
        elif ($d_tag | test("^(pr-)?test[-_]|[-_]test$|[-_]test[-_]|^test[0-9]+$|tset$")) then empty

        # Skip pure hex identifiers (agent profiles)
        elif ($d_tag | test("^[0-9a-f]{8,}$")) then empty

        # Skip fork repos (*-fork, *-fork-N, *-fork-gh)
        elif ($d_tag | test("-fork(-[a-z0-9]+)*$")) then empty

        # Skip hello-* demo repos
        elif ($d_tag | test("^hello-")) then empty

        # Skip date-named repos (YYYYMMDD daily backups)
        elif ($d_tag | test("^[0-9]{8}$")) then empty

        # Skip d_tags containing ! (malformed, e.g. git@github.com!org!repo.git)
        elif ($d_tag | test("!")) then empty

        # Skip very short d_tags (likely test)
        elif ($d_tag | length) <= 2 then empty

        # Skip repos with no clone URLs and no web URLs
        elif (([.tags[] | select(.[0]=="clone")] | length) == 0 and
              ([.tags[] | select(.[0]=="web")] | length) == 0) then empty

        # Passes all filters
        else $event
        end
    '
}

# ============================================================================
# DATA EXTRACTION
# ============================================================================

# Extract structured data from a raw kind 30617 event
extract_repo_data() {
    jq -c '{
        event_id: .id,
        pubkey: .pubkey,
        created_at: .created_at,
        d_tag: ([.tags[] | select(.[0]=="d")][0][1] // ""),
        name: ([.tags[] | select(.[0]=="name")][0][1] // ""),
        description: ([.tags[] | select(.[0]=="description")][0][1] // ""),
        clone_urls: [.tags[] | select(.[0]=="clone")] | map(.[1]),
        web_urls: [.tags[] | select(.[0]=="web")] | map(.[1]),
        relays: [.tags[] | select(.[0]=="relays")] | map(.[1]),
        maintainers: [.tags[] | select(.[0]=="maintainers")] | map(.[1]),
        hashtags: [.tags[] | select(.[0]=="t")] | map(.[1])
    }'
}

# ============================================================================
# MODE 1: TRACK KNOWN REPOS
# ============================================================================

fetch_tracked_repos() {
    echo "=== Tracking known NIP-34 repos ===" >&2

    if [ ! -f "$TRACKED_FILE" ]; then
        echo "  WARNING: $TRACKED_FILE not found, skipping tracking" >&2
        return
    fi

    # Extract tracked d_tags from YAML (simple grep, no YAML parser needed)
    local d_tags
    d_tags=$(grep '^\s*d_tag:' "$TRACKED_FILE" | sed 's/.*d_tag:\s*//' | tr -d '"' | tr -d "'" | xargs)

    if [ -z "$d_tags" ]; then
        echo "  No tracked repos found in $TRACKED_FILE" >&2
        return
    fi

    echo "  Tracked repos: $d_tags" >&2
    echo "" >&2

    local tracked_array="[]"

    for d_tag in $d_tags; do
        echo "  Fetching repo: $d_tag" >&2

        local repo_data="null"
        local patch_count=0
        local issue_count=0

        # Fetch the repo announcement (kind 30617) - get latest version
        local repo_event
        repo_event=$(
            for relay in "${NIP34_RELAYS[@]}"; do
                nak req -k "$KIND_REPO" -t d="$d_tag" --limit 5 "$relay" 2>/dev/null || true
            done | jq -s 'sort_by(-.created_at) | .[0] // empty' 2>/dev/null
        )

        if [ -n "$repo_event" ] && [ "$repo_event" != "null" ]; then
            repo_data=$(echo "$repo_event" | extract_repo_data)
            echo "    Found repo announcement ($(echo "$repo_data" | jq -r '.name'))" >&2

            # Get the "a" tag reference for this repo to find patches/issues
            local repo_pubkey
            repo_pubkey=$(echo "$repo_event" | jq -r '.pubkey')
            local a_tag="$KIND_REPO:$repo_pubkey:$d_tag"

            # Fetch patches (kind 1617) referencing this repo
            local patches
            patches=$(
                for relay in "${NIP34_RELAYS[@]}"; do
                    nak req -k "$KIND_PATCH" -t a="$a_tag" --since "$SINCE_TIMESTAMP" --limit 50 "$relay" 2>/dev/null || true
                done | jq -s 'unique_by(.id)' 2>/dev/null
            )
            patch_count=$(echo "$patches" | jq 'length' 2>/dev/null || echo 0)
            echo "    Patches in period: $patch_count" >&2

            # Fetch issues (kind 1621) referencing this repo
            local issues
            issues=$(
                for relay in "${NIP34_RELAYS[@]}"; do
                    nak req -k "$KIND_ISSUE" -t a="$a_tag" --since "$SINCE_TIMESTAMP" --limit 50 "$relay" 2>/dev/null || true
                done | jq -s 'unique_by(.id)' 2>/dev/null
            )
            issue_count=$(echo "$issues" | jq 'length' 2>/dev/null || echo 0)
            echo "    Issues in period: $issue_count" >&2

            # Build patch summaries
            local patch_summaries="[]"
            if [ "$patch_count" -gt 0 ]; then
                patch_summaries=$(echo "$patches" | jq '[.[] | {
                    event_id: .id,
                    pubkey: .pubkey,
                    created_at: .created_at,
                    subject: ([.tags[] | select(.[0]=="subject")][0][1] // ""),
                    is_root: ([.tags[] | select(.[0]=="t" and .[1]=="root")] | length > 0)
                }]')
            fi

            # Build issue summaries
            local issue_summaries="[]"
            if [ "$issue_count" -gt 0 ]; then
                issue_summaries=$(echo "$issues" | jq '[.[] | {
                    event_id: .id,
                    pubkey: .pubkey,
                    created_at: .created_at,
                    subject: ([.tags[] | select(.[0]=="subject")][0][1] // ""),
                    content_preview: (.content[:200])
                }]')
            fi

            # Combine into tracked entry
            local entry
            entry=$(jq -n \
                --argjson repo "$repo_data" \
                --argjson patches "$patch_summaries" \
                --argjson issues "$issue_summaries" \
                --argjson patch_count "$patch_count" \
                --argjson issue_count "$issue_count" \
                '{
                    repo: $repo,
                    activity: {
                        patches_in_period: $patch_count,
                        issues_in_period: $issue_count,
                        patches: $patches,
                        issues: $issues
                    }
                }')

            tracked_array=$(echo "$tracked_array" | jq --argjson entry "$entry" '. + [$entry]')
        else
            echo "    No repo announcement found" >&2
        fi

        echo "" >&2
    done

    echo "$tracked_array" > "$TRACKED_RESULTS"
    local total
    total=$(jq 'length' "$TRACKED_RESULTS")
    echo "  Tracked repos found: $total" >&2
}

# ============================================================================
# MODE 2: DISCOVER NEW REPOS
# ============================================================================

fetch_discovered_repos() {
    echo "=== Discovering new NIP-34 repos ===" >&2

    # Fetch ALL kind 30617 events from the time window
    echo "  Querying relays for repo announcements..." >&2

    local raw_count=0
    for relay in "${NIP34_RELAYS[@]}"; do
        echo "    Querying $relay..." >&2
        nak req -k "$KIND_REPO" --since "$SINCE_TIMESTAMP" --limit 200 "$relay" 2>/dev/null || true
    done | jq -c '.' >> "$REPOS_RAW"

    raw_count=$(wc -l < "$REPOS_RAW")
    echo "  Raw events fetched: $raw_count" >&2

    if [ "$raw_count" -eq 0 ]; then
        echo "  No events found in time window" >&2
        return
    fi

    # Deduplicate by event ID
    local deduped_file="$NOSTR_TEMP_DIR/repos_deduped.json"
    jq -s 'unique_by(.id)' "$REPOS_RAW" > "$deduped_file"
    local deduped_count
    deduped_count=$(jq 'length' "$deduped_file")
    echo "  After dedup: $deduped_count" >&2

    # Apply noise filter
    local filtered_file="$NOSTR_TEMP_DIR/repos_filtered.json"
    jq '.[]' "$deduped_file" | filter_noise | jq -s '.' > "$filtered_file"
    local filtered_count
    filtered_count=$(jq 'length' "$filtered_file")
    echo "  After noise filter: $filtered_count (removed $((deduped_count - filtered_count)) noise events)" >&2

    # Remove repos that are already tracked (by d_tag)
    if [ -f "$TRACKED_FILE" ]; then
        local tracked_d_tags
        tracked_d_tags=$(grep '^\s*d_tag:' "$TRACKED_FILE" | sed 's/.*d_tag:\s*//' | tr -d '"' | tr -d "'" | jq -R -s 'split("\n") | map(select(. != "") | ltrimstr(" ") | rtrimstr(" "))')

        local new_only_file="$NOSTR_TEMP_DIR/repos_new.json"
        jq --argjson tracked "$tracked_d_tags" '
            map(select(
                ([.tags[] | select(.[0]=="d")][0][1] // "") as $d |
                ($tracked | index($d)) == null
            ))
        ' "$filtered_file" > "$new_only_file"
        local new_count
        new_count=$(jq 'length' "$new_only_file")
        echo "  After removing tracked: $new_count new repos" >&2

        # Deduplicate by d_tag (keep most recent event per repo)
        local final_file="$NOSTR_TEMP_DIR/repos_final.json"
        jq '
            group_by([.tags[] | select(.[0]=="d")][0][1]) |
            map(sort_by(-.created_at) | .[0])
        ' "$new_only_file" > "$final_file"
    else
        cp "$filtered_file" "$NOSTR_TEMP_DIR/repos_final.json"
    fi

    # Extract structured data
    jq '[.[] | {
        event_id: .id,
        pubkey: .pubkey,
        created_at: .created_at,
        d_tag: ([.tags[] | select(.[0]=="d")][0][1] // ""),
        name: ([.tags[] | select(.[0]=="name")][0][1] // ""),
        description: ([.tags[] | select(.[0]=="description")][0][1] // ""),
        clone_urls: [.tags[] | select(.[0]=="clone")] | map(.[1]),
        web_urls: [.tags[] | select(.[0]=="web")] | map(.[1]),
        relays: [.tags[] | select(.[0]=="relays")] | map(.[1]),
        maintainers: [.tags[] | select(.[0]=="maintainers")] | map(.[1]),
        hashtags: [.tags[] | select(.[0]=="t")] | map(.[1])
    }] | sort_by(-.created_at)' "$NOSTR_TEMP_DIR/repos_final.json" > "$DISCOVERED_RESULTS"

    local final_count
    final_count=$(jq 'length' "$DISCOVERED_RESULTS")
    echo "  Discovered repos: $final_count" >&2

    # Print discovered repos for quick review
    if [ "$final_count" -gt 0 ]; then
        echo "" >&2
        echo "  Discovered repos:" >&2
        jq -r '.[] | "    - \(.name) (\(.d_tag)) - \(.clone_urls | join(", "))"' "$DISCOVERED_RESULTS" >&2
    fi
}

# ============================================================================
# OUTPUT
# ============================================================================

build_output() {
    echo "" >&2
    echo "=== Building output ===" >&2

    local tracked_count
    tracked_count=$(jq 'length' "$TRACKED_RESULTS")
    local discovered_count
    discovered_count=$(jq 'length' "$DISCOVERED_RESULTS")

    # Count total patches and issues across tracked repos
    local total_patches
    total_patches=$(jq '[.[].activity.patches_in_period] | add // 0' "$TRACKED_RESULTS")
    local total_issues
    total_issues=$(jq '[.[].activity.issues_in_period] | add // 0' "$TRACKED_RESULTS")

    jq -n \
        --arg generated_at "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
        --arg start "$START_DATE" \
        --arg end "$END_DATE" \
        --argjson days "$SINCE_DAYS" \
        --argjson tracked_count "$tracked_count" \
        --argjson discovered_count "$discovered_count" \
        --argjson total_patches "$total_patches" \
        --argjson total_issues "$total_issues" \
        --slurpfile tracked "$TRACKED_RESULTS" \
        --slurpfile discovered "$DISCOVERED_RESULTS" \
        '{
            generated_at: $generated_at,
            period: {
                start: $start,
                end: $end,
                days: $days
            },
            summary: {
                tracked_repos: $tracked_count,
                discovered_repos: $discovered_count,
                total_patches_in_period: $total_patches,
                total_issues_in_period: $total_issues
            },
            tracked: ($tracked | flatten),
            discovered: ($discovered | flatten)
        }' > "$OUTPUT_FILE"

    echo "Output saved to: $OUTPUT_FILE" >&2
    echo "" >&2
    echo "Summary:" >&2
    jq '.summary' "$OUTPUT_FILE" >&2
}

# ============================================================================
# MAIN
# ============================================================================

main() {
    check_nostr_requirements || exit 1

    echo "Fetching NIP-34 repo data (last $SINCE_DAYS days, mode: $MODE)..." >&2
    echo "Since timestamp: $SINCE_TIMESTAMP ($(format_timestamp "$SINCE_TIMESTAMP"))" >&2
    echo "Relays: ${NIP34_RELAYS[*]}" >&2
    echo "" >&2

    if [ "$MODE" = "both" ] || [ "$MODE" = "track" ]; then
        fetch_tracked_repos
    fi

    echo "" >&2

    if [ "$MODE" = "both" ] || [ "$MODE" = "discover" ]; then
        fetch_discovered_repos
    fi

    build_output
}

main "$@"
