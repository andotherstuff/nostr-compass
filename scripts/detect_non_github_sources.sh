#!/bin/bash
#
# Change G-F5: Non-GitHub source detector
#
# Surfaces projects whose primary repository lives outside github.com.
# Reads zapstore output, projects.yml, and nip34_repos discovery output,
# then writes a report listing tracked-worthy candidates by source host.
#
# Purpose: scope what Change G-F1 (Codeberg), G-F2 (Sourcehut), G-F3 (GitLab),
# and G-F4 (NIP-34 native promotion) need to cover.
#
# Usage:
#   ./detect_non_github_sources.sh
#
# Output:
#   data/non_github_sources_YYYY-MM-DD.json    (machine-readable)
#   stdout: a summary grouped by host
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

PROJECTS_FILE="$PROJECT_ROOT/data/projects.yml"
ZAPSTORE_LATEST=$(ls -t "$PROJECT_ROOT"/data/zapstore_releases/zapstore_*.json 2>/dev/null | head -1 || true)
NIP34_LATEST=$(ls -t "$PROJECT_ROOT"/data/nip34_repos/nip34_*.json 2>/dev/null | head -1 || true)
OUTPUT_DIR="$PROJECT_ROOT/data"
TODAY=$(date +%Y-%m-%d)
OUTPUT_FILE="$OUTPUT_DIR/non_github_sources_${TODAY}.json"

echo "=== Non-GitHub source detector ==="
echo ""

# Pull the set of tracked repo hosts from projects.yml.
# A "non-GitHub" tracked entry already exists for ngit (Codeberg) and
# nostr-rs-relay (Sourcehut) but most projects.yml entries are github.com.
TRACKED_NON_GITHUB=$(awk '
  /^[[:space:]]+repo:[[:space:]]*/ {
    repo = $0
    sub(/^[[:space:]]+repo:[[:space:]]*/, "", repo)
    gsub(/^["\x27]|["\x27]$/, "", repo)
    if (repo != "" && repo !~ /github\.com/) print repo
  }
' "$PROJECTS_FILE" | sort -u)

echo "Tracked non-GitHub repos in projects.yml:"
if [ -z "$TRACKED_NON_GITHUB" ]; then
    echo "  (none)"
else
    echo "$TRACKED_NON_GITHUB" | sed 's/^/  /'
fi
echo ""

# Extract from zapstore: app_repository values that are NOT github.com,
# and pair with tracked-worthy candidates (nostr_relevant, not yet tracked).
ZAPSTORE_NON_GITHUB="[]"
if [ -n "$ZAPSTORE_LATEST" ] && [ -f "$ZAPSTORE_LATEST" ]; then
    ZAPSTORE_NON_GITHUB=$(jq '
        [.releases[]
         | select(.nostr_relevant)
         | select(.app_repository != null)
         | select(.app_repository | test("github\\.com") | not)
         | {
             app_name,
             app_repository,
             tracked_project,
             nostr_match_reason,
             new_app
           }]
        | unique_by(.app_repository)
    ' "$ZAPSTORE_LATEST")
fi

ZAPSTORE_NG_COUNT=$(echo "$ZAPSTORE_NON_GITHUB" | jq 'length')
echo "Zapstore Nostr-relevant releases hosted outside github.com: $ZAPSTORE_NG_COUNT"
if [ "$ZAPSTORE_NG_COUNT" -gt 0 ]; then
    echo "$ZAPSTORE_NON_GITHUB" | jq -r '.[] | "  \(.app_name) | \(.app_repository) | tracked=\(.tracked_project // "no") | \(.nostr_match_reason)"'
fi
echo ""

# Group zapstore non-GitHub by host
echo "=== By host ==="
echo "$ZAPSTORE_NON_GITHUB" | jq -r '
    group_by(.app_repository | capture("https?://(?<host>[^/]+)").host)
    | map({host: .[0].app_repository | capture("https?://(?<host>[^/]+)").host, count: length, samples: [.[].app_name][:5]})
    | sort_by(.count) | reverse
    | .[] | "\(.host): \(.count) projects (\(.samples | join(", ")))"
'
echo ""

# NIP-34 native repos: discovered repos that have no GitHub mirror at all.
# These are first-class candidates for Change G-F4 (promote to scoring input).
NIP34_NATIVE="[]"
if [ -n "$NIP34_LATEST" ] && [ -f "$NIP34_LATEST" ]; then
    # nip34 schema: .discovered[] entries with .clone_urls[] (plural) and .name
    NIP34_NATIVE=$(jq '
        [.discovered[]?
         | select(.clone_urls != null)
         | select(.clone_urls | length > 0)
         | select((.clone_urls | map(test("github\\.com")) | any) | not)
         | {
             name,
             clone_urls,
             d_tag,
             description
           }]
    ' "$NIP34_LATEST" 2>/dev/null || echo "[]")
fi

NIP34_NATIVE_COUNT=$(echo "$NIP34_NATIVE" | jq 'length')
echo "NIP-34 discovered repos with NO GitHub mirror: $NIP34_NATIVE_COUNT"
if [ "$NIP34_NATIVE_COUNT" -gt 0 ]; then
    echo "$NIP34_NATIVE" | jq -r '.[] | "  \(.name) - \(.clone_urls | join(", ") | .[:80])"' | head -20 || true
    if [ "$NIP34_NATIVE_COUNT" -gt 20 ]; then
        echo "  ... and $((NIP34_NATIVE_COUNT - 20)) more"
    fi
fi
echo ""

# Combine into one report
jq -n \
    --argjson tracked_non_github "$(echo "$TRACKED_NON_GITHUB" | jq -R -s 'split("\n") | map(select(length > 0))')" \
    --argjson zapstore_non_github "$ZAPSTORE_NON_GITHUB" \
    --argjson nip34_native "$NIP34_NATIVE" \
    --arg generated_at "$(date -Iseconds)" \
    --arg zapstore_source "${ZAPSTORE_LATEST:-none}" \
    --arg nip34_source "${NIP34_LATEST:-none}" \
    '{
        generated_at: $generated_at,
        sources: {
            zapstore: $zapstore_source,
            nip34: $nip34_source
        },
        summary: {
            tracked_non_github_repos: ($tracked_non_github | length),
            zapstore_nostr_relevant_non_github: ($zapstore_non_github | length),
            nip34_native_repos: ($nip34_native | length)
        },
        tracked_non_github: $tracked_non_github,
        zapstore_non_github: $zapstore_non_github,
        nip34_native: $nip34_native
    }' > "$OUTPUT_FILE"

echo "Report saved to: $OUTPUT_FILE"
