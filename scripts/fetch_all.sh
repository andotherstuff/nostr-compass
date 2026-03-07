#!/bin/bash
#
# Master fetch script - runs all data fetchers for Nostr Compass newsletter
#
# Usage:
#   ./fetch_all.sh                 # Auto-detect time range from last run
#   ./fetch_all.sh --since-days 7  # Explicit time range
#
# Runs:
#   1. fetch_project_updates.py    (GitHub releases, PRs, commits)
#   2. fetch_nostr_nip_discussions.sh (NIP discussions from relays)
#   3. fetch_nostr_recap.sh        (Nostr Recap weekly summaries)
#   4. fetch_shakespeare_apps.sh   (Soapbox MiniApps submissions)
#   5. fetch_nip34_repos.sh        (NIP-34 git repos from relays)
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
VERBOSE=""
while [[ $# -gt 0 ]]; do
    case $1 in
        --since-days)
            SINCE_DAYS="$2"
            shift 2
            ;;
        -v|--verbose)
            VERBOSE="-v"
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [--since-days N] [-v|--verbose]"
            echo ""
            echo "Runs all data fetchers for newsletter generation."
            echo ""
            echo "Options:"
            echo "  --since-days N  Number of days to look back (default: auto-detect)"
            echo "  -v, --verbose   Show detailed progress"
            echo "  -h, --help      Show this help"
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

SINCE_ARG=""
if [ -n "$SINCE_DAYS" ]; then
    SINCE_ARG="--since-days $SINCE_DAYS"
fi

echo "==========================================="
echo "  Nostr Compass - Data Collection"
echo "==========================================="
echo ""

FAILED=0
SKIPPED=0

# 1. GitHub project updates (Python)
echo "[1/5] GitHub project updates..."
if command -v python3 &>/dev/null; then
    cd "$PROJECT_ROOT"
    if python3 scripts/fetch_project_updates.py $SINCE_ARG $VERBOSE; then
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
echo "[2/5] NIP discussions from relays..."
if command -v nak &>/dev/null; then
    if "$SCRIPT_DIR/fetch_nostr_nip_discussions.sh" $SINCE_ARG; then
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
echo "[3/5] Nostr Recap summaries..."
if command -v nak &>/dev/null; then
    if "$SCRIPT_DIR/fetch_nostr_recap.sh" $SINCE_ARG; then
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
echo "[4/5] Shakespeare Apps (Soapbox MiniApps)..."
if command -v nak &>/dev/null; then
    if "$SCRIPT_DIR/fetch_shakespeare_apps.sh" $SINCE_ARG; then
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
echo "[5/5] NIP-34 git repos..."
if command -v nak &>/dev/null; then
    if "$SCRIPT_DIR/fetch_nip34_repos.sh" $SINCE_ARG; then
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

# Summary
echo "==========================================="
echo "  Collection Summary"
echo "==========================================="
echo "  Completed: $((5 - FAILED - SKIPPED))/5"
echo "  Failed:    $FAILED"
echo "  Skipped:   $SKIPPED"
echo ""

# Show data freshness
echo "Data freshness:"
for dir in project_updates nostr_nip_discussions nostr_recap shakespeare_apps nip34_repos; do
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
