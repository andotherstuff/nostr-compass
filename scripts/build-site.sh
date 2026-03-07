#!/usr/bin/env bash
set -euo pipefail

if [[ -n "${HUGO_BASE_URL:-}" ]]; then
  hugo \
    --gc \
    --minify \
    --ignoreVendorPaths "hugo_modules" \
    --baseURL "$HUGO_BASE_URL"
else
  hugo \
    --gc \
    --minify \
    --ignoreVendorPaths "hugo_modules"
fi

bunx pagefind --site public
