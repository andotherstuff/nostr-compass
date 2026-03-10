#!/usr/bin/env bash
set -euo pipefail

get_cpu_count() {
  if command -v nproc >/dev/null 2>&1; then
    nproc
    return
  fi

  if command -v getconf >/dev/null 2>&1; then
    getconf _NPROCESSORS_ONLN
    return
  fi

  printf '1\n'
}

get_default_headroom() {
  if [[ -n "${CI:-}" ]]; then
    printf '0\n'
  else
    printf '2\n'
  fi
}

total_cores="$(get_cpu_count)"
reserved_cores="${BUILD_HEADROOM_CORES:-$(get_default_headroom)}"

if [[ ! "$reserved_cores" =~ ^[0-9]+$ ]]; then
  echo "BUILD_HEADROOM_CORES must be a non-negative integer" >&2
  exit 1
fi

if [[ -n "${BUILD_MAX_CORES:-}" && ! "${BUILD_MAX_CORES}" =~ ^[0-9]+$ ]]; then
  echo "BUILD_MAX_CORES must be a non-negative integer" >&2
  exit 1
fi

build_cores=$((total_cores - reserved_cores))
if (( build_cores < 1 )); then
  build_cores=1
fi

build_reason="reserved ${reserved_cores}"
if [[ -n "${BUILD_MAX_CORES:-}" ]] && (( BUILD_MAX_CORES > 0 && build_cores > BUILD_MAX_CORES )); then
  build_cores="$BUILD_MAX_CORES"
  build_reason="reserved ${reserved_cores}, capped at ${BUILD_MAX_CORES}"
fi

export GOMAXPROCS="$build_cores"
export RAYON_NUM_THREADS="$build_cores"
export TOKIO_WORKER_THREADS="$build_cores"

echo "Building with ${build_cores}/${total_cores} CPU cores (${build_reason})."

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
