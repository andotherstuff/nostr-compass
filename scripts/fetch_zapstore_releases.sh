#!/bin/bash
#
# Fetch Zapstore app releases from Nostr relays
#
# Zapstore is a permissionless app store built on Nostr. Apps and releases are
# published as developer-signed Nostr events:
#   - Kind 32267 (addressable) — app metadata, d-tag = app id (e.g. com.example.app)
#   - Kind 30063 (addressable) — release metadata, d-tag = <app_id>@<version>
#   - Kind 3063  (regular)     — per-platform asset metadata (sha256 + url)
#
# Primary relay: wss://relay.zapstore.dev (canonical)
# Backup relays: standard Nostr relay set (sparse coverage)
#
# Filters applied (in order):
#   1. Self-signature gate: release.pubkey == app.pubkey
#      (zapstore's "developer-signed" guarantee — drops re-publishes & catalog mirrors)
#   2. Nostr-relevance gate: naive regex on app name / content / tags
#      (apps must mention nostr / nip-XX / known Nostr terms AND not be pure Bitcoin tools)
#   3. Newness gate: persistent publishers_seen.yml tracks (pubkey, app_id) pairs
#      (marks releases as new_app or update; refuses to mark if >20% are "new" — state corruption guard)
#
# Cross-reference with projects.yml: releases whose repository matches a tracked
# project get tracked_project=<name> set. Untracked Nostr-relevant releases are
# surfaced as candidates for adding to projects.yml.
#
# Requirements:
#   - nak (nostr army knife): go install github.com/fiatjaf/nak@latest
#   - jq: for JSON processing
#
# Usage:
#   ./fetch_zapstore_releases.sh [OPTIONS]
#
# Examples:
#   ./fetch_zapstore_releases.sh                    # Default: last 7 days
#   ./fetch_zapstore_releases.sh --since-days 30
#   ./fetch_zapstore_releases.sh --include-non-nostr  # Debug: bypass Nostr-relevance filter
#
# Output:
#   JSON file in data/zapstore_releases/zapstore_YYYY-MM-DD.json
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

source "$SCRIPT_DIR/nostr_common.sh"

DEFAULT_DAYS=7

# Parse arguments
SINCE_DAYS="$DEFAULT_DAYS"
INCLUDE_NON_NOSTR=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --since-days)
            SINCE_DAYS="$2"
            shift 2
            ;;
        --include-non-nostr)
            INCLUDE_NON_NOSTR=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Fetch Zapstore app releases from Nostr relays."
            echo ""
            echo "Options:"
            print_since_days_help "$DEFAULT_DAYS"
            echo "  --include-non-nostr  Debug: bypass Nostr-relevance filter"
            echo "  -h, --help           Show this help message"
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

# Paths
OUTPUT_DIR="$PROJECT_ROOT/data/zapstore_releases"
START_DATE=$(calc_start_date "$SINCE_DAYS")
END_DATE=$(get_today)
OUTPUT_FILE="$OUTPUT_DIR/zapstore_${END_DATE}.json"
SINCE_TIMESTAMP=$(calc_since_timestamp "$SINCE_DAYS")
SEEN_FILE="$OUTPUT_DIR/publishers_seen.yml"
PROJECTS_FILE="$PROJECT_ROOT/data/projects.yml"

# Relays
ZAPSTORE_RELAY="wss://relay.zapstore.dev"

setup_temp_dir
APPS_FILE="$NOSTR_TEMP_DIR/apps.json"
RELEASES_FILE="$NOSTR_TEMP_DIR/releases.json"
JOINED_FILE="$NOSTR_TEMP_DIR/joined.json"

# Change A3: Nostr-relevance uses two signals, with the discrimination
# coming from WHERE "nostr" appears (description text vs topic tags).
#
# STRONG_KEYWORDS: any single match qualifies, regardless of location.
# These are Nostr-specific identifiers, known project names, NIPs, kind
# numbers, and protocol-specific terms. False positives from this set
# are vanishingly rare.
NOSTR_STRONG_KEYWORDS='\bnpub\b|\bnsec\b|\bnaddr\b|\bnevent\b|\bnote1\b|nip-?[0-9]+|\bkind ?[0-9]{1,5}\b|damus|amethyst|primal|coracle|snort|nostrudel|gossip|nostrocket|habla|yakihonne|wavlake|zap\.stream|0xchat|whitenoise|marmot|blossom|nutzap|ndk|nostr-tools|rust-nostr|strfry|nostream|ditto\.|nosflare|nostrify|gift ?wrap|nostr identity|nostr account|publishing to nostr|share on nostr|via nostr|over nostr'
#
# NOSTR_MENTION: the word "nostr" appears anywhere in the text.
# Alone insufficient. The location matters (see filter logic below).
NOSTR_MENTION='\bnostr\b|\bnostr-|nostr_'

# Anti-keywords. Apps matching any of these are excluded UNLESS they
# also match a strong keyword. Expanded from the original 10 patterns
# to cover the false-positive classes confirmed in the 2026-06-17
# baseline: parental controls, price alerts, meetup announcers,
# hardware wallet firmware, password managers, NFC payment apps,
# mixing tools, VPNs, and media players.
ANTI_KEYWORDS='coinjoin|whirlpool|payjoin|silent ?payment|bitcoin ?core|samourai|wasabi|joinmarket|tor ?relay|i2p ?router|hardware ?wallet ?firmware|parental ?control|price ?alert|meetup ?announce|nfc ?payment|wifi ?scanner|password ?manager|\bvpn\b|amnezia|mullvad|wireguard|file ?sync ?without ?nostr'

# Sanity check thresholds (Change A1: per-pubkey, not global percentage)
SANITY_MAX_NEW_TOTAL=50     # If >50 distinct (pubkey, app_id) pairs are new in one run, suspect corruption
SANITY_MAX_NEW_PER_PUBKEY=5 # If a single pubkey publishes >5 new app_ids in one week, suspect catalog mirror
SEEN_FILE_MIN_BYTES=1024    # Below this, treat as fresh install (data corruption guard)

# Paged fetch from relay.zapstore.dev.
# The relay silently returns zero events for limit > ~100 and rate-limits rapid
# repeat queries, so we page with --until cursors and a small sleep between pages.
# Args: <kind> <output_file> [<since_timestamp>]
paged_fetch() {
    local kind="$1"
    local out="$2"
    local since="${3:-}"
    local page_size=50
    local page_sleep=2
    local max_pages=200  # 200 * 50 = 10000 events ceiling, far above any real run
    local until_arg=""
    local page=0
    local total=0

    echo "[]" > "$out"
    local accum="$NOSTR_TEMP_DIR/accum_${kind}.ndjson"
    : > "$accum"

    local since_arg=""
    if [ -n "$since" ]; then
        since_arg="--since $since"
    fi

    while [ "$page" -lt "$max_pages" ]; do
        local page_file="$NOSTR_TEMP_DIR/page_${kind}_${page}.ndjson"
        nak req -k "$kind" $since_arg $until_arg --limit "$page_size" "$ZAPSTORE_RELAY" 2>/dev/null > "$page_file" || true
        local got=$(wc -l < "$page_file")

        if [ "$got" -eq 0 ]; then
            break
        fi

        cat "$page_file" >> "$accum"
        total=$((total + got))
        page=$((page + 1))

        # Cursor = oldest created_at in this page, minus 1 to avoid refetching it
        local oldest=$(jq -s 'map(.created_at) | min' "$page_file" 2>/dev/null || echo "")
        if [ -z "$oldest" ] || [ "$oldest" = "null" ]; then
            break
        fi
        until_arg="--until $((oldest - 1))"

        # Stop if since boundary crossed
        if [ -n "$since" ] && [ "$oldest" -le "$since" ]; then
            break
        fi

        # Stop if page wasn't full (relay had nothing more)
        if [ "$got" -lt "$page_size" ]; then
            break
        fi

        sleep "$page_sleep"
    done

    if [ -s "$accum" ]; then
        jq -s 'unique_by(.id)' "$accum" > "$out"
    else
        echo "[]" > "$out"
    fi
}

fetch_apps() {
    echo "Fetching app metadata (kind 32267) from $ZAPSTORE_RELAY (paged)..." >&2
    paged_fetch 32267 "$APPS_FILE"
    local count=$(jq 'length' "$APPS_FILE")
    echo "  Found $count apps" >&2
}

fetch_releases() {
    echo "Fetching releases (kind 30063) since $(format_timestamp "$SINCE_TIMESTAMP") (paged)..." >&2
    paged_fetch 30063 "$RELEASES_FILE" "$SINCE_TIMESTAMP"
    # Filter to window (paging may return slightly older events due to relay quirks)
    jq --argjson since "$SINCE_TIMESTAMP" '[.[] | select(.created_at >= $since)]' "$RELEASES_FILE" > "$RELEASES_FILE.tmp"
    mv "$RELEASES_FILE.tmp" "$RELEASES_FILE"
    local count=$(jq 'length' "$RELEASES_FILE")
    echo "  Found $count releases in window" >&2

    if [ "$count" -eq 0 ]; then
        echo "  WARNING: zero releases returned. Either nothing was published this week" >&2
        echo "           or $ZAPSTORE_RELAY is degraded. Investigate before trusting output." >&2
    fi
}

join_and_filter() {
    echo "Joining releases with apps, applying self-signature gate..." >&2

    jq --slurpfile apps "$APPS_FILE" \
       --argjson since_ts "$SINCE_TIMESTAMP" \
       '
        # Index apps by d-tag (app_id) for quick lookup
        ($apps[0] | map({key: (.tags | map(select(.[0] == "d")) | .[0][1] // ""), value: .}) | from_entries) as $apps_by_id
        |
        [
          .[]
          | . as $rel
          # Extract release fields
          | (.tags | map(select(.[0] == "i")) | .[0][1] // "") as $app_id
          | (.tags | map(select(.[0] == "version")) | .[0][1] // "") as $version
          | (.tags | map(select(.[0] == "d")) | .[0][1] // "") as $d_tag
          | ($apps_by_id[$app_id]) as $app
          # Self-signature gate: drop if no matching app, or pubkey mismatch
          | select($app != null)
          | select($app.pubkey == $rel.pubkey)
          | {
              release_id: .id,
              release_created_at: .created_at,
              release_created_at_iso: (.created_at | todateiso8601),
              pubkey: .pubkey,
              app_id: $app_id,
              version: $version,
              d_tag: $d_tag,
              release_notes: .content,
              app_name: ($app.tags | map(select(.[0] == "name")) | .[0][1] // $app_id),
              app_summary: ($app.tags | map(select(.[0] == "summary")) | .[0][1] // ""),
              app_content: $app.content,
              app_repository: ($app.tags | map(select(.[0] == "repository")) | .[0][1] // ""),
              app_url: ($app.tags | map(select(.[0] == "url")) | .[0][1] // ""),
              app_icon: ($app.tags | map(select(.[0] == "icon")) | .[0][1] // ""),
              app_license: ($app.tags | map(select(.[0] == "license")) | .[0][1] // ""),
              app_topics: [$app.tags | .[] | select(.[0] == "t") | .[1]],
              app_platforms: [$app.tags | .[] | select(.[0] == "f") | .[1]]
            }
        ]
        | sort_by(.release_created_at) | reverse
       ' "$RELEASES_FILE" > "$JOINED_FILE"

    local count=$(jq 'length' "$JOINED_FILE")
    echo "  After self-signature gate: $count releases" >&2
}

apply_nostr_filter() {
    if [ "$INCLUDE_NON_NOSTR" = true ]; then
        echo "Skipping Nostr-relevance filter (--include-non-nostr)" >&2
        jq '[.[] | . + {nostr_relevant: true, nostr_match_reason: "filter-bypassed"}]' "$JOINED_FILE" > "$JOINED_FILE.tmp"
        mv "$JOINED_FILE.tmp" "$JOINED_FILE"
        return
    fi

    echo "Applying Nostr-relevance filter (Change A3: strong-keyword OR nostr-in-description)..." >&2

    # Decision rule (refined after diff-testing against the 2026-06-17 baseline):
    #
    # The discriminating signal is WHERE "nostr" appears:
    #   - Apps using nostr for SEO (PearGuard, SatScream, Keyguard) mention nostr
    #     ONLY in app_topics tag, never in app_summary or app_content.
    #   - Real Nostr apps (Iris Drive, Memely, Flare) describe their Nostr behavior
    #     in app_summary or app_content text.
    #
    # Therefore we search description text (name+summary+content) separately from
    # topic tags + repo URL. Mentioning nostr in description = real signal.
    # Mentioning nostr only in topic tag = SEO tag, requires anti-keyword check.
    #
    # Priority:
    #   1. strong-keyword in description-or-tags -> relevant, "strong-keyword"
    #   2. nostr in description text AND no anti -> relevant, "nostr-in-description"
    #   3. nostr in description text AND anti     -> not relevant, "anti-keyword-veto"
    #   4. nostr only in tags/repo, not description -> not relevant, "nostr-tag-only"
    #   5. else -> not relevant, "no-match"
    jq --arg strong "$NOSTR_STRONG_KEYWORDS" \
       --arg mention "$NOSTR_MENTION" \
       --arg anti "$ANTI_KEYWORDS" \
       '
        [
          .[]
          | . as $r
          # Description text: name + summary + content (where real Nostr apps
          # describe themselves). Tags+repo searched separately.
          | (([.app_name, .app_summary, .app_content]) | join(" ") | ascii_downcase) as $desc
          | (([.app_repository, .app_url] + .app_topics) | join(" ") | ascii_downcase) as $meta
          | (($desc + " " + $meta) | test($strong; "i")) as $has_strong
          | ($desc | test($mention; "i")) as $nostr_in_desc
          | ($meta | test($mention; "i")) as $nostr_in_meta
          | (($desc + " " + $meta) | test($anti; "i")) as $has_anti
          | (.tracked_project != null) as $is_tracked
          | . + (
              # Tracked-project override: if projects.yml already lists this
              # repo, the editorial decision to track it stands. The Analyst
              # will apply the Nostr Relay Test per-release. Without this
              # override, projects like Alby Go (NWC signer, Nostr-relevant
              # in spirit but with Lightning-focused descriptions) would be
              # silently dropped from the candidate pool.
              if $is_tracked then
                {nostr_relevant: true, nostr_match_reason: "tracked-project-override", nostr_match_strength: 2}
              elif $has_strong then
                {nostr_relevant: true, nostr_match_reason: "strong-keyword", nostr_match_strength: 3}
              elif $nostr_in_desc and ($has_anti | not) then
                {nostr_relevant: true, nostr_match_reason: "nostr-in-description", nostr_match_strength: 2}
              elif $nostr_in_desc and $has_anti then
                {nostr_relevant: false, nostr_match_reason: "anti-keyword-veto", nostr_match_strength: 0}
              elif $nostr_in_meta and ($nostr_in_desc | not) then
                {nostr_relevant: false, nostr_match_reason: "nostr-tag-only", nostr_match_strength: 0}
              else
                {nostr_relevant: false, nostr_match_reason: "no-match", nostr_match_strength: 0}
              end
            )
        ]
       ' "$JOINED_FILE" > "$JOINED_FILE.tmp"
    mv "$JOINED_FILE.tmp" "$JOINED_FILE"

    local total=$(jq 'length' "$JOINED_FILE")
    local relevant=$(jq '[.[] | select(.nostr_relevant)] | length' "$JOINED_FILE")
    echo "  Nostr-relevant: $relevant / $total" >&2
}

cross_reference_projects() {
    if [ ! -f "$PROJECTS_FILE" ]; then
        echo "  WARNING: projects.yml not found at $PROJECTS_FILE, skipping cross-reference" >&2
        jq '[.[] | . + {tracked_project: null}]' "$JOINED_FILE" > "$JOINED_FILE.tmp"
        mv "$JOINED_FILE.tmp" "$JOINED_FILE"
        return
    fi

    echo "Cross-referencing repositories with projects.yml..." >&2

    # Extract (name, repo) pairs from projects.yml using grep/sed
    # projects.yml has entries like:
    #   - name: Damus
    #     repo: https://github.com/damus-io/damus
    local repo_map="$NOSTR_TEMP_DIR/repo_map.json"
    awk '
      /^[[:space:]]*-[[:space:]]*name:[[:space:]]*/ {
        name = $0
        sub(/^[[:space:]]*-[[:space:]]*name:[[:space:]]*/, "", name)
        gsub(/^["'\'']|["'\'']$/, "", name)
        next
      }
      /^[[:space:]]+repo:[[:space:]]*/ {
        repo = $0
        sub(/^[[:space:]]+repo:[[:space:]]*/, "", repo)
        gsub(/^["'\'']|["'\'']$/, "", repo)
        if (name != "" && repo != "") {
          print repo "\t" name
          name = ""
        }
      }
    ' "$PROJECTS_FILE" | jq -R -s '
      # Change A2: build a normalized lookup map.
      # Normalize: lowercase, strip http(s):// scheme stays as-is on the lookup side,
      # http -> https, strip trailing slash, strip trailing .git, strip leading www.
      # Both projects.yml entries and zapstore app_repository values go through the
      # same normalization function before any lookup.
      def normalize_repo:
        ascii_downcase
        | sub("^http://"; "https://")
        | sub("^https://www\\."; "https://")
        | sub("\\.git$"; "")
        | sub("/$"; "");
      split("\n") | map(select(length > 0))
      | map(split("\t") | {key: (.[0] | normalize_repo), value: .[1]})
      | from_entries
    ' > "$repo_map"

    jq --slurpfile repos "$repo_map" \
       '
        def normalize_repo:
          ascii_downcase
          | sub("^http://"; "https://")
          | sub("^https://www\\."; "https://")
          | sub("\\.git$"; "")
          | sub("/$"; "");
        ($repos[0]) as $rmap
        |
        [
          .[]
          | . as $r
          | ($rmap[$r.app_repository | normalize_repo] // null) as $matched
          | . + {tracked_project: $matched}
        ]
       ' "$JOINED_FILE" > "$JOINED_FILE.tmp"
    mv "$JOINED_FILE.tmp" "$JOINED_FILE"

    local tracked=$(jq '[.[] | select(.tracked_project != null)] | length' "$JOINED_FILE")
    echo "  Releases matched to tracked projects: $tracked" >&2
}

apply_newness_gate() {
    echo "Applying newness gate..." >&2

    # Change A1: fresh-install detector
    # Fresh install means: seen file missing, or smaller than SEEN_FILE_MIN_BYTES.
    # In that case, suppress new_app flags for the first run so we don't flood the
    # newsletter with "everything is new" on baseline runs.
    local fresh_install=false
    if [ ! -f "$SEEN_FILE" ]; then
        echo "  Fresh install detected (seen file missing). Baselining state, no new_app flags this run." >&2
        echo "# Persistent state for zapstore newness detection." > "$SEEN_FILE"
        echo "# Format: { <pubkey>: [<app_id>, ...] }" >> "$SEEN_FILE"
        echo "# DO NOT delete this file. Fresh install suppresses new_app flags on next run." >&2
        echo "{}" >> "$SEEN_FILE"
        fresh_install=true
    else
        local size=$(stat -c %s "$SEEN_FILE" 2>/dev/null || echo 0)
        if [ "$size" -lt "$SEEN_FILE_MIN_BYTES" ]; then
            echo "  Seen file under ${SEEN_FILE_MIN_BYTES} bytes (size=$size). Treating as fresh install." >&2
            fresh_install=true
        fi
    fi

    # Convert YAML-ish seen file to JSON (we store as JSON below the comment lines)
    local seen_json="$NOSTR_TEMP_DIR/seen.json"
    grep -v '^[[:space:]]*#' "$SEEN_FILE" | grep -v '^[[:space:]]*$' > "$seen_json.raw" || echo "{}" > "$seen_json.raw"
    if [ ! -s "$seen_json.raw" ]; then
        echo "{}" > "$seen_json"
    else
        # Try to parse as JSON; if it fails, reset to empty
        if jq empty "$seen_json.raw" 2>/dev/null; then
            cp "$seen_json.raw" "$seen_json"
        else
            echo "  WARNING: seen file is malformed, resetting and treating as fresh install" >&2
            echo "{}" > "$seen_json"
            fresh_install=true
        fi
    fi

    # Annotate each release with new_app / update flags
    jq --slurpfile seen "$seen_json" \
       '
        ($seen[0]) as $s
        |
        [
          .[]
          | . as $r
          | ($s[$r.pubkey] // []) as $known_apps
          | ($known_apps | index($r.app_id) != null) as $known
          | . + {
              new_app: (($known | not)),
              update: $known,
              sanity_demoted: false
            }
        ]
       ' "$JOINED_FILE" > "$JOINED_FILE.tmp"
    mv "$JOINED_FILE.tmp" "$JOINED_FILE"

    local total=$(jq 'length' "$JOINED_FILE")
    local new_count=$(jq '[.[] | select(.new_app)] | length' "$JOINED_FILE")
    echo "  new_app (raw): $new_count / $total" >&2

    if [ "$fresh_install" = true ]; then
        echo "  Fresh-install guard: suppressing all new_app flags on baseline run." >&2
        jq '[.[] | . + {new_app: false, update: false, first_run: true}]' "$JOINED_FILE" > "$JOINED_FILE.tmp"
        mv "$JOINED_FILE.tmp" "$JOINED_FILE"
    else
        # Change A1: per-pubkey sanity gate (replaces global percentage threshold).
        # Two independent triggers, applied per-publisher rather than as a batch wipe:
        # 1. Global cap: if more than SANITY_MAX_NEW_TOTAL distinct new pairs in one run,
        #    something is wrong with seen-state (partial wipe, relay quirk). Log loudly.
        # 2. Per-pubkey cap: any single pubkey publishing more than SANITY_MAX_NEW_PER_PUBKEY
        #    new app_ids in one week is more likely a catalog mirror than a real launch wave.
        #    Demote that pubkey's events only.
        if [ "$new_count" -gt "$SANITY_MAX_NEW_TOTAL" ]; then
            echo "  WARNING: $new_count new (pubkey, app_id) pairs exceeds global cap ${SANITY_MAX_NEW_TOTAL}." >&2
            echo "           Possible seen-state corruption. Inspect $SEEN_FILE before next run." >&2
            echo "           (Continuing with per-pubkey demotion only; global wipe NOT applied.)" >&2
        fi

        # Per-pubkey demotion: list pubkeys whose new-app count this run exceeds cap.
        local offenders_file="$NOSTR_TEMP_DIR/sanity_offenders.json"
        jq --argjson cap "$SANITY_MAX_NEW_PER_PUBKEY" \
           '[.[] | select(.new_app)] | group_by(.pubkey)
            | map({pubkey: .[0].pubkey, new_count: length})
            | map(select(.new_count > $cap))' \
           "$JOINED_FILE" > "$offenders_file"

        local offender_count=$(jq 'length' "$offenders_file")
        if [ "$offender_count" -gt 0 ]; then
            echo "  Per-pubkey sanity: $offender_count pubkey(s) exceeded cap of ${SANITY_MAX_NEW_PER_PUBKEY} new app_ids:" >&2
            jq -r '.[] | "    - \(.pubkey[:16])... (\(.new_count) new app_ids)"' "$offenders_file" >&2

            # Demote new_app for offending pubkeys only
            jq --slurpfile off "$offenders_file" \
               '
                ($off[0] | map(.pubkey) | map({key: ., value: true}) | from_entries) as $bad
                |
                [
                  .[]
                  | if (.new_app and ($bad[.pubkey] // false))
                    then . + {new_app: false, update: true, sanity_demoted: true}
                    else .
                    end
                ]
               ' "$JOINED_FILE" > "$JOINED_FILE.tmp"
            mv "$JOINED_FILE.tmp" "$JOINED_FILE"
        fi

        local final_new=$(jq '[.[] | select(.new_app)] | length' "$JOINED_FILE")
        local demoted=$(jq '[.[] | select(.sanity_demoted)] | length' "$JOINED_FILE")
        echo "  new_app (after sanity): $final_new / $total (demoted $demoted)" >&2
    fi

    # Update seen file with everything we just saw (regardless of new/update outcome)
    jq -s '
        .[0] as $seen
        | .[1] as $releases
        | reduce $releases[] as $r ($seen;
            .[$r.pubkey] = (((.[$r.pubkey] // []) + [$r.app_id]) | unique)
          )
       ' "$seen_json" "$JOINED_FILE" > "$NOSTR_TEMP_DIR/seen_updated.json"

    # Rewrite seen file (preserve header comment)
    {
        echo "# Persistent state for zapstore newness detection."
        echo "# Format: { <pubkey>: [<app_id>, ...] }"
        echo "# DO NOT delete this file. Fresh install suppresses new_app flags on next run."
        cat "$NOSTR_TEMP_DIR/seen_updated.json"
    } > "$SEEN_FILE"
}

save_output() {
    jq --arg generated_at "$(date -Iseconds)" \
       --arg start "$START_DATE" \
       --arg end "$END_DATE" \
       --argjson days "$SINCE_DAYS" \
       --argjson since_ts "$SINCE_TIMESTAMP" \
       '
        . as $releases
        | {
            generated_at: $generated_at,
            period: {
              start: $start,
              end: $end,
              days: $days
            },
            summary: {
              total_releases: ($releases | length),
              nostr_relevant: ([$releases[] | select(.nostr_relevant)] | length),
              nostr_relevant_strong: ([$releases[] | select(.nostr_match_reason == "strong-keyword")] | length),
              nostr_relevant_tracked_override: ([$releases[] | select(.nostr_match_reason == "tracked-project-override")] | length),
              nostr_relevant_in_description: ([$releases[] | select(.nostr_match_reason == "nostr-in-description")] | length),
              anti_keyword_vetoed: ([$releases[] | select(.nostr_match_reason == "anti-keyword-veto")] | length),
              nostr_tag_only_excluded: ([$releases[] | select(.nostr_match_reason == "nostr-tag-only")] | length),
              new_apps: ([$releases[] | select(.new_app and .nostr_relevant)] | length),
              updates: ([$releases[] | select(.update and .nostr_relevant)] | length),
              sanity_demoted: ([$releases[] | select(.sanity_demoted)] | length),
              first_run_baseline: ([$releases[] | select(.first_run)] | length),
              tracked_in_projects_yml: ([$releases[] | select(.tracked_project != null)] | length),
              candidates_for_projects_yml: ([$releases[] | select(.nostr_relevant and .tracked_project == null)] | length)
            },
            releases: $releases
          }
       ' "$JOINED_FILE" > "$OUTPUT_FILE"

    echo "Output saved to: $OUTPUT_FILE" >&2
}

print_summary() {
    echo "" >&2
    echo "========================================" >&2
    echo "ZAPSTORE RELEASES SUMMARY" >&2
    echo "========================================" >&2
    jq -r '
        "Total releases in window: \(.summary.total_releases)",
        "Nostr-relevant: \(.summary.nostr_relevant)",
        "  strong-keyword match:        \(.summary.nostr_relevant_strong)",
        "  tracked-project-override:    \(.summary.nostr_relevant_tracked_override)",
        "  nostr-in-description:        \(.summary.nostr_relevant_in_description)",
        "  anti-keyword vetoed:         \(.summary.anti_keyword_vetoed)",
        "  nostr-tag-only excluded:     \(.summary.nostr_tag_only_excluded)",
        "  New apps: \(.summary.new_apps)",
        "  Updates: \(.summary.updates)",
        "Sanity-demoted (per-pubkey): \(.summary.sanity_demoted)",
        "First-run baseline (no new_app flags): \(.summary.first_run_baseline)",
        "Tracked in projects.yml: \(.summary.tracked_in_projects_yml)",
        "Candidates for projects.yml: \(.summary.candidates_for_projects_yml)",
        "",
        "Nostr-relevant releases (top 20):",
        (.releases | map(select(.nostr_relevant))[:20] | .[]
          | "  - \(.app_name) v\(.version) (\(if .new_app then "NEW" elif .update then "update" else "?" end))\(if .tracked_project then " [tracked: \(.tracked_project)]" else "" end) [\(.nostr_match_reason)]")
    ' "$OUTPUT_FILE" >&2
    echo "" >&2
}

main() {
    check_nostr_requirements || exit 1

    echo "========================================" >&2
    echo "Zapstore Release Fetcher" >&2
    echo "========================================" >&2
    echo "Relay: $ZAPSTORE_RELAY" >&2
    echo "Looking back: $SINCE_DAYS days (since $(format_timestamp "$SINCE_TIMESTAMP"))" >&2
    if [ "$INCLUDE_NON_NOSTR" = true ]; then
        echo "Filter: DEBUG mode (all apps, no Nostr-relevance filter)" >&2
    fi
    echo "" >&2

    mkdir -p "$OUTPUT_DIR"

    fetch_apps
    fetch_releases
    join_and_filter
    cross_reference_projects     # before filter so tracked status can override
    apply_nostr_filter
    apply_newness_gate
    save_output
    print_summary
}

main "$@"
