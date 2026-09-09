#!/bin/bash
#
# Master fetch script - runs all data fetchers for Nostr Compass newsletter
#
# Usage:
#   ./fetch_all.sh                 # Auto-detect time range from last run
#   ./fetch_all.sh --since-days 7  # Explicit time range
#   ./fetch_all.sh --newsletter-date 2026-07-29  # Month-end history discovery
#
# Runs:
#   1. fetch_project_updates.py       (GitHub releases, PRs, commits)
#   2. fetch_nostr_nip_discussions.sh (NIP discussions from relays)
#   3. fetch_nostr_recap.sh           (Nostr Recap weekly summaries)
#   4. fetch_shakespeare_apps.sh      (Soapbox MiniApps submissions)
#   5. fetch_nip34_repos.sh           (NIP-34 git repos from relays)
#   6. fetch_zapstore_releases.sh     (Zapstore developer-signed app releases)
#   7. fetch_app_discovery.py          (candidate-only GitHub + NIP-89 + Zapstore listings)
#   8. fetch_heartbeats.sh             (OpenSats + Sovereign Engineering grantee activity)
#   9. fetch_monthly_history.py        (history candidates; final weekly issue only)
#  10. fetch_spec_updates.py           (NIP, BUD, NAP, Marmot, Gamma, Concord, NWC specs)
#
# Prerequisites:
#   - Python 3 + requirements.txt (for GitHub fetcher)
#   - nak + jq (for Nostr relay fetchers)
#   - GITHUB_TOKEN env var (recommended for rate limits)
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Source common functions (sets PATH for nak, provides helpers)
source "$SCRIPT_DIR/nostr_common.sh"

# Parse arguments
SINCE_DAYS=""
SINCE_ABSOLUTE=""
UNTIL_ABSOLUTE=""
VERBOSE=""
PASS_ID=""
NEWSLETTER_DATE="$(date -u +%F)"
while [[ $# -gt 0 ]]; do
    case $1 in
        --since-days)
            SINCE_DAYS="$2"
            shift 2
            ;;
        --newsletter-date)
            NEWSLETTER_DATE="$2"
            shift 2
            ;;
        --since)
            SINCE_ABSOLUTE="$2"; shift 2 ;;
        --until)
            UNTIL_ABSOLUTE="$2"; shift 2
            ;;
        --pass-id)
            PASS_ID="$2"; shift 2
            ;;
        -v|--verbose)
            VERBOSE="-v"
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [--since-days N] [--newsletter-date YYYY-MM-DD] [-v|--verbose]"
            echo ""
            echo "Runs all data fetchers for newsletter generation."
            echo ""
            echo "Options:"
            echo "  --since-days N       Number of days to look back (default: auto-detect)"
            echo "  --newsletter-date D  Planned issue date; runs history discovery on the final weekly issue"
            echo "  -v, --verbose        Show detailed progress"
            echo "  -h, --help      Show this help"
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done
[ -n "$PASS_ID" ] || { echo "--pass-id is required; each collection pass needs a caller-owned immutable identity" >&2; exit 2; }

SINCE_ARG=""
if [ -n "$SINCE_ABSOLUTE" ] || [ -n "$UNTIL_ABSOLUTE" ]; then
    if [ -z "$SINCE_ABSOLUTE" ] || [ -z "$UNTIL_ABSOLUTE" ] || [ -n "$SINCE_DAYS" ]; then
        echo "--since and --until are required together and cannot be combined with --since-days" >&2; exit 2
    fi
    PROJECT_ARG="--since $SINCE_ABSOLUTE --until $UNTIL_ABSOLUTE"
    SINCE_DAYS="$(python3 -c 'import datetime,sys,math; a=datetime.datetime.fromisoformat(sys.argv[1].replace("Z","+00:00")); b=datetime.datetime.fromisoformat(sys.argv[2].replace("Z","+00:00")); print(max(1,math.ceil((b-a).total_seconds()/86400)))' "$SINCE_ABSOLUTE" "$UNTIL_ABSOLUTE")"
    SINCE_ARG="--since-days $SINCE_DAYS"
    RUN_SINCE="$SINCE_ABSOLUTE"; RUN_UNTIL="$UNTIL_ABSOLUTE"
elif [ -n "$SINCE_DAYS" ]; then
    SINCE_ARG="--since-days $SINCE_DAYS"; PROJECT_ARG="$SINCE_ARG"
    RUN_SINCE="$(date -u -d "$SINCE_DAYS days ago" --iso-8601=seconds)"; RUN_UNTIL="$(date -u --iso-8601=seconds)"
else
    PROJECT_ARG=""
    RUN_SINCE="$(date -u -d "8 days ago" --iso-8601=seconds)"; RUN_UNTIL="$(date -u --iso-8601=seconds)"
fi
MANIFEST="$PROJECT_ROOT/data/source_runs/source_run_${NEWSLETTER_DATE}_${PASS_ID}.json"
SOURCE_FAMILIES=(projects nip-discussions nostr-recap shakespeare-apps nip34 zapstore app-discovery heartbeats monthly-history specs)
MANIFEST_ARGS=()
for family in "${SOURCE_FAMILIES[@]}"; do MANIFEST_ARGS+=(--expected "$family"); done
python3 "$SCRIPT_DIR/source_run_manifest.py" create --manifest "$MANIFEST" --pass-id "$PASS_ID" --since "$RUN_SINCE" --until "$RUN_UNTIL" "${MANIFEST_ARGS[@]}"
export COMPASS_WINDOW_SINCE="$RUN_SINCE" COMPASS_WINDOW_UNTIL="$RUN_UNTIL" COMPASS_SOURCE_PASS_ID="$PASS_ID"
declare -A SOURCE_EXIT
for family in "${SOURCE_FAMILIES[@]}"; do SOURCE_EXIT[$family]=127; done

# Absolute window for the heartbeat fetcher (defaults to 8 days back through today)
HB_SINCE="$(date -u -d "${SINCE_DAYS:-8} days ago" +%F)"
HB_UNTIL="$(date -u +%F)"

echo "==========================================="
echo "  Nostr Compass - Data Collection"
echo "==========================================="
echo ""

FAILED=0
SKIPPED=0

# 1. GitHub project updates (Python)
echo "[1/10] GitHub project updates..."
if command -v python3 &>/dev/null; then
    cd "$PROJECT_ROOT"
    if python3 scripts/fetch_project_updates.py $PROJECT_ARG --fresh $VERBOSE; then
        SOURCE_EXIT[projects]=0
        echo "  Done."
    else
        echo "  WARNING: GitHub fetcher failed (exit code $?)"
        FAILED=$((FAILED + 1))
    fi
else
    echo "  SKIPPED: python3 not found"
    SKIPPED=$((SKIPPED + 1))
fi
echo ""

# 2. NIP discussions (Nostr relay via nak)
echo "[2/10] NIP discussions from relays..."
if command -v nak &>/dev/null; then
    if "$SCRIPT_DIR/fetch_nostr_nip_discussions.sh" $SINCE_ARG; then
        SOURCE_EXIT[nip-discussions]=0
        echo "  Done."
    else
        echo "  WARNING: NIP discussion fetcher failed (exit code $?)"
        FAILED=$((FAILED + 1))
    fi
else
    echo "  SKIPPED: nak not installed (go install github.com/fiatjaf/nak@latest)"
    SKIPPED=$((SKIPPED + 1))
fi
echo ""

# 3. Nostr Recap weekly summaries (Nostr relay via nak)
echo "[3/10] Nostr Recap summaries..."
if command -v nak &>/dev/null; then
    if "$SCRIPT_DIR/fetch_nostr_recap.sh" $SINCE_ARG; then
        SOURCE_EXIT[nostr-recap]=0
        echo "  Done."
    else
        echo "  WARNING: Nostr Recap fetcher failed (exit code $?)"
        FAILED=$((FAILED + 1))
    fi
else
    echo "  SKIPPED: nak not installed"
    SKIPPED=$((SKIPPED + 1))
fi
echo ""

# 4. Shakespeare Apps / Soapbox MiniApps (Nostr relay via nak)
echo "[4/10] Shakespeare Apps (Soapbox MiniApps)..."
if command -v nak &>/dev/null; then
    if "$SCRIPT_DIR/fetch_shakespeare_apps.sh" $SINCE_ARG; then
        SOURCE_EXIT[shakespeare-apps]=0
        echo "  Done."
    else
        echo "  WARNING: Shakespeare Apps fetcher failed (exit code $?)"
        FAILED=$((FAILED + 1))
    fi
else
    echo "  SKIPPED: nak not installed"
    SKIPPED=$((SKIPPED + 1))
fi
echo ""

# 5. NIP-34 git repos (Nostr relay via nak)
echo "[5/10] NIP-34 git repos..."
if command -v nak &>/dev/null; then
    if "$SCRIPT_DIR/fetch_nip34_repos.sh" $SINCE_ARG; then
        SOURCE_EXIT[nip34]=0
        echo "  Done."
    else
        echo "  WARNING: NIP-34 repo fetcher failed (exit code $?)"
        FAILED=$((FAILED + 1))
    fi
else
    echo "  SKIPPED: nak not installed"
    SKIPPED=$((SKIPPED + 1))
fi
echo ""

# 6. Zapstore developer-signed releases (Nostr relay via nak)
echo "[6/10] Zapstore releases..."
if command -v nak &>/dev/null; then
    if "$SCRIPT_DIR/fetch_zapstore_releases.sh" $SINCE_ARG; then
        SOURCE_EXIT[zapstore]=0
        echo "  Done."
    else
        echo "  WARNING: Zapstore fetcher failed (exit code $?) — soft-fail, continuing"
        FAILED=$((FAILED + 1))
    fi
else
    echo "  SKIPPED: nak not installed"
    SKIPPED=$((SKIPPED + 1))
fi
echo ""

# 7. Untracked application candidates (GitHub + NIP-89 handlers + Zapstore listings)
echo "[7/10] Untracked Nostr application discovery..."
if command -v python3 &>/dev/null && command -v gh &>/dev/null && command -v nak &>/dev/null; then
    cd "$PROJECT_ROOT"
    if python3 scripts/fetch_app_discovery.py $SINCE_ARG; then
        SOURCE_EXIT[app-discovery]=0
        echo "  Done."
    else
        echo "  WARNING: application discovery failed (exit code $?) — soft-fail, continuing"
        FAILED=$((FAILED + 1))
    fi
else
    echo "  SKIPPED: python3, gh, or nak not found"
    SKIPPED=$((SKIPPED + 1))
fi
echo ""

# 8. Grantee heartbeat feeds (OpenSats nostr/general funds + Sovereign Engineering note)
echo "[8/10] Grantee heartbeat feeds (OpenSats / Sovereign Engineering)..."
if "$SCRIPT_DIR/fetch_heartbeats.sh" "$HB_SINCE" "$HB_UNTIL"; then
    SOURCE_EXIT[heartbeats]=0
    echo "  Done."
else
    echo "  WARNING: Heartbeat fetcher failed (exit code $?) — soft-fail, continuing"
    FAILED=$((FAILED + 1))
fi
echo ""

# 9. Same-calendar-month history candidates (final weekly issue only)
ISSUE_MONTH="$(date -d "$NEWSLETTER_DATE" +%m)"
ISSUE_YEAR="$(date -d "$NEWSLETTER_DATE" +%Y)"
NEXT_WEEK_MONTH="$(date -d "$NEWSLETTER_DATE +7 days" +%m)"
echo "[9/10] Month-end history candidates..."
if [ "$ISSUE_MONTH" != "$NEXT_WEEK_MONTH" ]; then
    if python3 "$SCRIPT_DIR/fetch_monthly_history.py" \
        --month "$((10#$ISSUE_MONTH))" \
        --through-year "$ISSUE_YEAR"; then
        SOURCE_EXIT[monthly-history]=0
        echo "  Done."
    else
        echo "  WARNING: monthly history fetcher failed (exit code $?)"
        FAILED=$((FAILED + 1))
    fi
else
    echo "  SKIPPED: $NEWSLETTER_DATE is not the final weekly issue of its month"
    SKIPPED=$((SKIPPED + 1))
fi
echo ""

# 10. Protocol/spec-family activity (GitHub)
echo "[10/10] Specification families (NIP / BUD / NAP / Marmot / Gamma / Concord / NWC)..."
if command -v python3 &>/dev/null && command -v gh &>/dev/null; then
    cd "$PROJECT_ROOT"
    SPEC_ARGS=()
    if [ -n "$SINCE_DAYS" ]; then
        SPEC_ARGS+=(--since-days "$SINCE_DAYS")
    fi
    if python3 scripts/fetch_spec_updates.py "${SPEC_ARGS[@]}"; then
        SOURCE_EXIT[specs]=0
        echo "  Done."
    else
        echo "  WARNING: specification-family fetcher failed (exit code $?)"
        FAILED=$((FAILED + 1))
    fi
else
    echo "  SKIPPED: python3 or gh not found"
    SKIPPED=$((SKIPPED + 1))
fi
echo ""

# Ingest only collector-authored exact-pass receipts. An exit code, mtime, or
# post-hoc item count is never promoted into pagination/query evidence.
record_source() {
    local family="$1" collector="$2" applicability="${3:-required}"
    local receipt="$PROJECT_ROOT/data/source_runs/collector_${PASS_ID}_${family}.json"
    if [ "$applicability" = not_applicable ]; then
        local query; query="$(python3 -c 'import json,sys; print(json.dumps({"family":sys.argv[1],"pass_id":sys.argv[2],"since":sys.argv[3],"until":sys.argv[4]},separators=(",",":")))' "$family" "$PASS_ID" "$RUN_SINCE" "$RUN_UNTIL")"
        python3 "$SCRIPT_DIR/source_run_manifest.py" record --manifest "$MANIFEST" --pass-id "$PASS_ID" --family "$family" --status not_applicable --collector "$PROJECT_ROOT/$collector" --query-json "$query" --item-count 0 --page-count 0 --include-count 0 --skip-count 0 --skip-evidence-json '[]'
    elif [ -f "$receipt" ]; then
        python3 "$SCRIPT_DIR/source_run_manifest.py" ingest --manifest "$MANIFEST" --receipt "$receipt"
    else
        echo "Collector $family did not emit exact-pass receipt $receipt" >&2
        FAILED=$((FAILED + 1))
    fi
}
record_source projects scripts/fetch_project_updates.py
record_source nip-discussions scripts/fetch_nostr_nip_discussions.sh
record_source nostr-recap scripts/fetch_nostr_recap.sh
record_source shakespeare-apps scripts/fetch_shakespeare_apps.sh
record_source nip34 scripts/fetch_nip34_repos.sh
record_source zapstore scripts/fetch_zapstore_releases.sh
record_source app-discovery scripts/fetch_app_discovery.py
record_source heartbeats scripts/fetch_heartbeats.sh
if [ "$ISSUE_MONTH" != "$NEXT_WEEK_MONTH" ]; then record_source monthly-history scripts/fetch_monthly_history.py; else record_source monthly-history scripts/fetch_monthly_history.py not_applicable; fi
record_source specs scripts/fetch_spec_updates.py
if ! python3 "$SCRIPT_DIR/source_run_manifest.py" finalize --manifest "$MANIFEST"; then
    echo "Required source evidence is incomplete: $MANIFEST" >&2
    FAILED=$((FAILED + 1))
fi

# Summary
echo "==========================================="
echo "  Collection Summary"
echo "==========================================="
echo "  Completed: $((10 - FAILED - SKIPPED))/10"
echo "  Failed:    $FAILED"
echo "  Skipped:   $SKIPPED"
echo ""

# Release digest — MANDATORY post-pass.
#
# Stage 3 reads the fetch summary, not the raw JSON. When the summary carried
# only aggregates ("100 releases, 146 active repos"), a release could exist in
# the data and in no downstream artifact. Newsletter #37 lost Nail v0.1.0 that
# way: present in project_updates AND in the Zapstore feed, named nowhere.
#
# This names every release so a drop is a recorded editorial decision.
echo "==========================================="
echo "  Release digest (names every release)"
echo "==========================================="
LATEST_UPDATES=$(ls -t "$PROJECT_ROOT/data/project_updates"/updates_*.json 2>/dev/null | head -1)
LATEST_ZAPSTORE=$(ls -t "$PROJECT_ROOT/data/zapstore_releases"/zapstore_*.json 2>/dev/null | head -1)
DIGEST_MD="$PROJECT_ROOT/data/newsletter_workspace/release_digest_${NEWSLETTER_DATE:-$(date -u +%F)}.md"
DIGEST_JSON="$PROJECT_ROOT/data/project_updates/release_digest_${NEWSLETTER_DATE:-$(date -u +%F)}.json"
if [ -n "$LATEST_UPDATES" ] && command -v python3 >/dev/null 2>&1; then
    if python3 "$SCRIPT_DIR/build_release_digest.py"         --updates "$LATEST_UPDATES"         ${LATEST_ZAPSTORE:+--zapstore "$LATEST_ZAPSTORE"}         --out "$DIGEST_MD"         --json-out "$DIGEST_JSON"; then
        echo "  Digest: $DIGEST_MD"
        echo "  Triage MUST record a write-up-or-skip decision for every project listed."
    else
        echo "  FAILED to build the release digest. Stage 3 cannot enumerate releases without it."
        FAILED=$((FAILED + 1))
    fi
else
    echo "  SKIPPED: no updates_*.json found or python3 missing — Stage 3 has no release enumeration."
    SKIPPED=$((SKIPPED + 1))
fi
echo ""

# Show data freshness
echo "Data freshness:"
for dir in project_updates nostr_nip_discussions nostr_recap shakespeare_apps nip34_repos zapstore_releases app_discovery heartbeats spec_updates; do
    latest=$(ls -t "$PROJECT_ROOT/data/$dir"/*.json 2>/dev/null | head -1)
    if [ -n "$latest" ]; then
        age_hours=$(( ($(date +%s) - $(stat -c %Y "$latest")) / 3600 ))
        echo "  $dir: ${age_hours}h old"
    else
        echo "  $dir: NO DATA"
    fi
done

if [ $FAILED -gt 0 ]; then
    exit 1
fi
