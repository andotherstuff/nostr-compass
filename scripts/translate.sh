#!/usr/bin/env bash
# translate.sh — durable, resumable newsletter translation driver.
#
# WHY THIS EXISTS
# ---------------
# Translation used to run as a detached background process.
# That has no durability: a gateway restart, an API timeout, or an OOM killed the run
# with no status, no checkpoint, and no way to resume. Newsletter #31's translation
# died this way twice and had to be reconstructed by hand.
#
# The fix is not a smarter background process. It is checkpointing:
#   1. status  — deterministically compute what is missing, per language (resumable)
#   2. verify  — mechanically check one language's output (encoding, link leaks)
#   3. commit  — commit ONE language = one durable checkpoint
#
# Generation itself needs an LLM and stays an Opus agent. Everything around it is
# deterministic and lives here. A crash loses at most the one in-flight language;
# `status` always tells you exactly where to resume.
#
# USAGE
#   scripts/translate.sh status <YYYY-MM-DD>
#   scripts/translate.sh verify <lang> <YYYY-MM-DD>
#   scripts/translate.sh commit <lang> <YYYY-MM-DD>
#
set -uo pipefail

LANGS=(es pt de fr it ja ko nl zh)
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT" || exit 1

die() { echo "error: $*" >&2; exit 1; }

# NOTIFY: announce a finished step on the configured channel.
#
# The owner asked to hear about every completed step, not just the end of a run.
# A translation commit, a PR opening, and a merge are each a finished step. This
# is best-effort by design: a messaging failure must never fail a translation.
#
# Transport and target come from publish/config/notify.json, which is gitignored
# because it is host wiring; publish/lib/notify.ts reads the same file, so the
# two emitters cannot drift. command is argv with {target} and {body}
# placeholders. With nothing configured, notification is skipped silently.
# Translation runs in a per-issue worktree, where publish/config/notify.json is
# absent because it is gitignored. The shared checkout is the worktree's git
# common dir parent, so the config resolves without depending on an env var.
resolve_notify_config() {
  if [ -n "${COMPASS_NOTIFY_CONFIG:-}" ]; then printf '%s\n' "$COMPASS_NOTIFY_CONFIG"; return; fi
  if [ -f "$REPO_ROOT/publish/config/notify.json" ]; then
    printf '%s\n' "$REPO_ROOT/publish/config/notify.json"; return
  fi
  local common shared
  common="$(git -C "$REPO_ROOT" rev-parse --path-format=absolute --git-common-dir 2>/dev/null)" || return 0
  shared="$(dirname "$common")"
  [ -f "$shared/publish/config/notify.json" ] && printf '%s\n' "$shared/publish/config/notify.json"
  return 0
}
NOTIFY_CONFIG="$(resolve_notify_config)"
notify() {
  [ "${COMPASS_NOTIFY:-1}" = "0" ] && return 0
  COMPASS_NOTIFY_TARGET="${COMPASS_NOTIFY_TARGET:-}" \
  COMPASS_NOTIFY_COMMAND="${COMPASS_NOTIFY_COMMAND:-}" \
  python3 - "$NOTIFY_CONFIG" "$1" <<'PYNOTIFY' 2>/dev/null || \
    echo "  warn notify failed (continuing)" >&2
import json, os, subprocess, sys

config_path, body = sys.argv[1], sys.argv[2]
try:
    cfg = json.load(open(config_path, encoding="utf-8"))
except (OSError, ValueError):
    cfg = {}

target = os.environ.get("COMPASS_NOTIFY_TARGET") or cfg.get("target")
raw = os.environ.get("COMPASS_NOTIFY_COMMAND")
command = None
if raw:
    try:
        parsed = json.loads(raw)
        if isinstance(parsed, list) and all(isinstance(a, str) for a in parsed):
            command = parsed
    except ValueError:
        pass
command = command or cfg.get("command")

if not cfg.get("enabled", False) and not os.environ.get("COMPASS_NOTIFY_TARGET"):
    sys.exit(0)
if not target or not command:
    sys.exit(0)

argv = [a.replace("{target}", target).replace("{body}", body) for a in command]
subprocess.run(argv, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
PYNOTIFY
  return 0
}



lang_name() {
  case "$1" in
    es) echo "Spanish" ;; pt) echo "Portuguese" ;; de) echo "German" ;;
    fr) echo "French" ;;  it) echo "Italian" ;;    ja) echo "Japanese" ;;
    ko) echo "Korean" ;;  nl) echo "Dutch" ;;      zh) echo "Chinese" ;;
    *) echo "$1" ;;
  esac
}

en_newsletter() { echo "content/en/newsletters/$1-newsletter.md"; }

# Topic slugs the English issue actually links to. This is how we detect "new topic
# pages" without a hardcoded list: any topic the issue references that is missing in a
# target language needs translating.
referenced_topics() {
  local src; src="$(en_newsletter "$1")"
  [ -f "$src" ] || return 0
  grep -oE '/topics/[a-z0-9-]+' "$src" | sed 's|/topics/||' | sort -u
}

# Missing topic pages for one language.
missing_topics() {
  local lang="$1" date="$2" slug
  while read -r slug; do
    [ -n "$slug" ] || continue
    [ -f "content/$lang/topics/$slug.md" ] || echo "$slug"
  done < <(referenced_topics "$date")
}

# STALE: English source committed more recently than the translation.
is_stale() {
  local lang="$1" date="$2"
  local tgt="content/$lang/newsletters/$date-newsletter.md"
  [ -f "$tgt" ] || return 1
  local en_t tr_t
  en_t="$(git log -1 --format=%ct -- "$(en_newsletter "$date")" 2>/dev/null)"
  tr_t="$(git log -1 --format=%ct -- "$tgt" 2>/dev/null)"
  [ -n "$en_t" ] && [ -n "$tr_t" ] && [ "$en_t" -gt "$tr_t" ]
}

cmd_status() {
  local date="${1:?usage: translate.sh status <YYYY-MM-DD>}"
  [ -f "$(en_newsletter "$date")" ] || die "no English source: $(en_newsletter "$date")"

  local topics_n; topics_n="$(referenced_topics "$date" | wc -l)"
  echo "Issue $date — English source references $topics_n topic pages"
  echo ""
  printf "%-4s %-11s %-11s %-8s %s\n" "LANG" "NAME" "NEWSLETTER" "TOPICS" "STATUS"
  echo "---------------------------------------------------------------"

  local incomplete=0
  for lang in "${LANGS[@]}"; do
    local nl_file="content/$lang/newsletters/$date-newsletter.md"
    local has_nl status miss miss_n
    [ -f "$nl_file" ] && has_nl="present" || has_nl="MISSING"
    miss="$(missing_topics "$lang" "$date")"
    miss_n="$(echo -n "$miss" | grep -c . || true)"

    if [ "$has_nl" = "MISSING" ]; then
      status="TODO (full)"; incomplete=$((incomplete+1))
    elif [ "$miss_n" -gt 0 ]; then
      status="TODO ($miss_n topics)"; incomplete=$((incomplete+1))
    elif is_stale "$lang" "$date"; then
      status="STALE (retranslate)"; incomplete=$((incomplete+1))
    else
      status="done"
    fi

    printf "%-4s %-11s %-11s %-8s %s\n" \
      "$lang" "$(lang_name "$lang")" "$has_nl" "$((topics_n - miss_n))/$topics_n" "$status"
    [ "$miss_n" -gt 0 ] && echo "     missing topics: $(echo $miss | tr '\n' ' ')"
  done

  echo ""
  if [ "$incomplete" -eq 0 ]; then
    echo "All ${#LANGS[@]} languages complete for $date."
  else
    echo "$incomplete language(s) need work. Resume with those only — completed languages are already committed."
  fi
}

cmd_verify() {
  local lang="${1:?usage: translate.sh verify <lang> <YYYY-MM-DD>}"
  local date="${2:?usage: translate.sh verify <lang> <YYYY-MM-DD>}"
  local nl_file="content/$lang/newsletters/$date-newsletter.md"
  local fail=0

  echo "Verifying $(lang_name "$lang") ($lang) for $date"

  if [ -f "$nl_file" ]; then
    echo "  ok   newsletter present ($(wc -l < "$nl_file") lines)"
  else
    echo "  FAIL newsletter missing: $nl_file"; fail=1
  fi

  local miss; miss="$(missing_topics "$lang" "$date")"
  if [ -z "$miss" ]; then
    echo "  ok   all referenced topic pages present"
  else
    echo "  FAIL missing topic pages: $(echo $miss | tr '\n' ' ')"; fail=1
  fi

  # Internal links must use this language's prefix, not another language's.
  local leaks
  leaks="$(grep -ohE "\(/(en|es|pt|de|fr|it|ja|ko|nl|zh)/topics/" \
            "$nl_file" content/"$lang"/topics/*.md 2>/dev/null \
          | grep -v "(/$lang/topics/" | sort -u)"
  if [ -z "$leaks" ]; then
    echo "  ok   no cross-language link leaks"
  else
    echo "  FAIL link leaks to other languages: $(echo $leaks | tr '\n' ' ')"; fail=1
  fi

  # Is it actually translated?
  #
  # NOTE: do NOT gate Latin-script languages on a diacritic count. Real Dutch prose
  # carries ~5 diacritics per issue (ë/ï are rare), so any sane threshold either
  # rejects valid Dutch or is too low to mean anything. Caught during testing: a
  # >10 threshold failed the correct, committed nl translation.
  #
  # So: CJK/Hangul get a native-script count (unambiguous, thousands of chars).
  # Latin-script languages get checked for untranslated English prose instead —
  # that is the failure we actually care about.
  if [ -f "$nl_file" ]; then
    case "$lang" in
      ja|ko|zh)
        local hits
        hits="$(python3 - "$nl_file" "$lang" <<'PY'
import sys
path, lang = sys.argv[1], sys.argv[2]
t = open(path, encoding="utf-8").read()
ranges = {"ja": [("぀","ヿ"), ("一","鿿")], "ko": [("가","힯")], "zh": [("一","鿿")]}
print(sum(1 for c in t if any(a <= c <= b for a, b in ranges[lang])))
PY
)"
        if [ "${hits:-0}" -gt 100 ]; then
          echo "  ok   script: $hits native characters"
        else
          echo "  FAIL script: only ${hits:-0} native characters — likely untranslated"; fail=1
        fi
        ;;
      *)
        # Distinctive English prose that cannot survive a real translation.
        local eng
        eng="$(grep -oF -e "Welcome back to Nostr Compass" \
                        -e "your weekly guide to Nostr" \
                        -e "Tagged releases bring" \
                        -e "On the unreleased side" \
                        "$nl_file" 2>/dev/null | sort -u)"
        if [ -z "$eng" ]; then
          echo "  ok   translated (no untranslated English marker prose)"
        else
          echo "  FAIL untranslated English found: $(echo $eng | tr '\n' '|')"; fail=1
        fi
        # Diacritics are reported for information only, never a gate.
        local dia
        dia="$(python3 - "$nl_file" "$lang" <<'PY'
import sys
path, lang = sys.argv[1], sys.argv[2]
marks = {"es":"áéíóúñü","pt":"ãõáéíóúçâêô","de":"äöüß","fr":"éèêëàâçôûùîï","it":"àèéìòù","nl":"ëï"}
t = open(path, encoding="utf-8").read()
print(sum(1 for c in t if c in marks.get(lang, "")))
PY
)"
        echo "  info diacritics: ${dia:-0} (informational; Dutch is legitimately low)"
        ;;
    esac
  fi

  # German ASCII-substitute check — the #1 documented quality defect.
  if [ "$lang" = "de" ] && [ -f "$nl_file" ]; then
    local sub
    sub="$(grep -oiE '\b(fuer|ueber|groesser|schluessel|oeffentlich|aenderung|moeglich)\b' "$nl_file" 2>/dev/null | sort -u)"
    if [ -z "$sub" ]; then echo "  ok   no ASCII substitutes for umlauts"
    else echo "  FAIL ASCII substitutes instead of umlauts: $(echo $sub | tr '\n' ' ')"; fail=1; fi
  fi

  # Traditional-Chinese probe (spec requires Simplified).
  if [ "$lang" = "zh" ] && [ -f "$nl_file" ]; then
    local trad; trad="$(grep -oE '們|開|關|實|協|訊|網|據' "$nl_file" 2>/dev/null | wc -l)"
    if [ "$trad" -eq 0 ]; then echo "  ok   Simplified Chinese (no Traditional forms)"
    else echo "  FAIL $trad Traditional-Chinese characters found; spec requires Simplified"; fail=1; fi
  fi

  [ "$fail" -eq 0 ] && echo "  PASS" || echo "  FAILED"
  return "$fail"
}

cmd_commit() {
  local lang="${1:?usage: translate.sh commit <lang> <YYYY-MM-DD>}"
  local date="${2:?usage: translate.sh commit <lang> <YYYY-MM-DD>}"

  cmd_verify "$lang" "$date" || die "verify failed for $lang — not committing"

  local files=("content/$lang/newsletters/$date-newsletter.md")
  local slug
  while read -r slug; do
    [ -n "$slug" ] && [ -f "content/$lang/topics/$slug.md" ] && files+=("content/$lang/topics/$slug.md")
  done < <(referenced_topics "$date")

  # Stage ONLY this language's files for this issue. Never `git add .` — the working
  # tree routinely holds unrelated scratch (workspace state, lockfiles, stray scripts).
  git add -- "${files[@]}" 2>/dev/null

  if git diff --cached --quiet; then
    echo "nothing new to commit for $lang (already committed)"
    return 0
  fi

  local n; n="$(basename "$(en_newsletter "$date")" | sed 's/-newsletter.md//')"
  git commit -q -m "Add $(lang_name "$lang") translation for Newsletter $date and topic pages"
  local sha; sha="$(git rev-parse --short HEAD)"
  echo "committed $(lang_name "$lang") — checkpoint saved ($sha)"
  notify "$(printf '**Nostr Compass %s — Language translated (%s)**\n- Verified and committed as \`%s\`.\n- Run \`translate.sh status %s\` for the remaining languages.' \
    "$date" "$(lang_name "$lang")" "$sha" "$date")"
}

# BACKLOG: every issue whose English newsletter has no translation yet.
#
# Translations used to stall silently. #35's PR sat open for six days while #36's
# merged ahead of it, and #37 had none at all until it was chased by hand. Four
# issues from June and July are still untranslated. A gap that nothing reports is
# a gap that grows, so `backlog` makes the whole set visible in one command.
cmd_backlog() {
  local en missing=0
  echo "Untranslated issues (English present, at least one language missing)"
  echo ""
  for en in content/en/newsletters/*-newsletter.md; do
    local date; date="$(basename "$en" | sed 's/-newsletter.md//')"
    [ "$date" = "_index" ] && continue
    local gaps=()
    for lang in "${LANGS[@]}"; do
      [ -f "content/$lang/newsletters/$date-newsletter.md" ] || gaps+=("$lang")
    done
    if [ ${#gaps[@]} -gt 0 ]; then
      printf "  %s  missing: %s\n" "$date" "$(echo "${gaps[@]}" | tr ' ' ',')"
      missing=$((missing+1))
    fi
  done
  echo ""
  if [ "$missing" -eq 0 ]; then
    echo "No gaps: every English issue is translated into all ${#LANGS[@]} languages."
  else
    echo "$missing issue(s) need translation."
  fi
}

# SHIP: push the translation branch, open the PR, and merge it once checks pass.
#
# The generation step needs an agent, but nothing after it does. Leaving the
# merge to a human is what turned a finished translation into a six-day-old open
# PR. This blocks on the build check rather than merging blind.
cmd_ship() {
  local date="${1:?usage: translate.sh ship <YYYY-MM-DD> [--no-merge]}"
  local no_merge="${2:-}"
  local branch="translate/$date"
  # Titles appear as "Nostr Compass #37", 'Nostr Compass #27', and unquoted.
  local n; n="$(grep -m1 -oE "^title: *['\"]?Nostr Compass #[0-9]+" "$(en_newsletter "$date")" | grep -oE '[0-9]+$')"
  [ -n "$n" ] || die "cannot read issue number from $(en_newsletter "$date")"

  local lang
  for lang in "${LANGS[@]}"; do
    cmd_verify "$lang" "$date" >/dev/null || die "verify failed for $lang — refusing to ship an incomplete set"
  done
  echo "all ${#LANGS[@]} languages verified"

  git push -q --force-with-lease -u origin "$branch" || die "push failed for $branch"

  local pr
  pr="$(gh pr list --head "$branch" --state open --json number --jq '.[0].number // empty')"
  if [ -z "$pr" ]; then
    gh pr create \
      --title "Add translations for Newsletter #$n and topic pages" \
      --body "$(printf 'Translations for Newsletter #%s (%s).\n\nLanguages: %s\n\nGenerated and verified by `scripts/translate.sh`: every language passes the encoding, link-leak, and native-script checks, and all referenced topic pages are present.\n' \
        "$n" "$date" "$(echo "${LANGS[@]}" | tr ' ' ',' | sed 's/,/, /g')")" \
      >/dev/null || die "gh pr create failed"
    pr="$(gh pr list --head "$branch" --state open --json number --jq '.[0].number // empty')"
  fi
  [ -n "$pr" ] || die "could not determine PR number for $branch"
  echo "translation PR #$pr"
  notify "$(printf '**Nostr Compass issue %s — Translation PR opened**\n- [#%s](https://github.com/andotherstuff/nostr-compass/pull/%s) covers all %s languages for %s.\n- Waiting on the build check before merge.' \
    "$n" "$pr" "$pr" "${#LANGS[@]}" "$date")"

  if [ "$no_merge" = "--no-merge" ]; then
    echo "--no-merge: leaving PR #$pr open"
    return 0
  fi

  # Wait for the build check. Merging before CI is how a broken translation
  # would reach the website.
  local waited=0 conclusion=""
  while [ "$waited" -lt 900 ]; do
    conclusion="$(gh pr view "$pr" --json statusCheckRollup \
      --jq '[.statusCheckRollup[] | select(.name=="build")] | .[0].conclusion // ""')"
    [ -n "$conclusion" ] && break
    sleep 20; waited=$((waited+20))
  done
  if [ "$conclusion" != "SUCCESS" ]; then
    notify "$(printf '**Nostr Compass issue %s — Translation PR opened**\n- [#%s](https://github.com/andotherstuff/nostr-compass/pull/%s) is NOT merged: build check is \`%s\` after %ss.\n- Needs a look.' \
      "$n" "$pr" "$pr" "${conclusion:-pending}" "$waited")"
    die "build check on PR #$pr is '${conclusion:-pending}' after ${waited}s — not merging"
  fi
  gh pr merge "$pr" --squash || die "merge failed for PR #$pr"
  echo "merged PR #$pr"
  notify "$(printf '**Nostr Compass issue %s — Translations merged**\n- [#%s](https://github.com/andotherstuff/nostr-compass/pull/%s) merged after a passing build.\n- All %s languages are live for %s.' \
    "$n" "$pr" "$pr" "${#LANGS[@]}" "$date")"
}

# NEXT: the single oldest issue still needing translation, or nothing.
#
# This is the hook the automation drives. `backlog` is for humans; `next` is
# machine-readable so a cron can loop until it prints nothing. #35 stalled and
# four June/July issues were never translated because no scheduled step ever
# asked "what is still missing?".
cmd_next() {
  local en date lang
  for en in content/en/newsletters/*-newsletter.md; do
    date="$(basename "$en" | sed 's/-newsletter.md//')"
    [ "$date" = "_index" ] && continue
    # Only translate what is actually published: a draft issue is not ready.
    grep -qE '^draft: *false' "$en" || continue
    for lang in "${LANGS[@]}"; do
      if [ ! -f "content/$lang/newsletters/$date-newsletter.md" ]; then
        echo "$date"
        return 0
      fi
    done
  done
  return 0
}

# REPORT-BACKLOG: announce the current gap on the Marmot channel.
cmd_report_backlog() {
  local body; body="$(cmd_backlog)"
  local count; count="$(echo "$body" | sed -n 's/^\([0-9]\+\) issue(s) need translation.$/\1/p')"
  if [ -z "$count" ]; then
    notify "$(printf '**Compass translations — Translation backlog**\n- No gaps: every published English issue is translated into all %s languages.' "${#LANGS[@]}")"
  else
    local list; list="$(echo "$body" | sed -n 's/^  \([0-9-]\+\)  missing: \(.*\)$/- \1 missing \2/p')"
    notify "$(printf '**Compass translations — Translation backlog**\n%s\n- %s issue(s) outstanding.' "$list" "$count")"
  fi
  echo "$body"
}

case "${1:-}" in
  status) shift; cmd_status "$@" ;;
  verify) shift; cmd_verify "$@" ;;
  commit) shift; cmd_commit "$@" ;;
  backlog) shift; cmd_backlog "$@" ;;
  next) shift; cmd_next "$@" ;;
  report-backlog) shift; cmd_report_backlog "$@" ;;
  ship) shift; cmd_ship "$@" ;;
  *) cat <<EOF
translate.sh — durable, resumable newsletter translation driver

  status <YYYY-MM-DD>          what is missing, per language (safe to run anytime)
  verify <lang> <YYYY-MM-DD>   check one language: files, links, encoding
  commit <lang> <YYYY-MM-DD>   verify then commit one language (a checkpoint)
  ship <YYYY-MM-DD>            verify all, push, open the PR, merge when the build passes
  backlog                      every English issue still missing a translation
  next                         oldest published issue still needing translation (empty = none)
  report-backlog               print the backlog and announce it on Marmot

Languages: ${LANGS[*]}

Generation stays an Opus agent (see skills/_COMPASS/agents/TranslationAgent.md).
Run one language at a time and commit each; a crash then loses at most one language,
and 'status' tells you exactly where to resume.
EOF
  ;;
esac
