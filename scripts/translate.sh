#!/usr/bin/env bash
# translate.sh — durable, resumable newsletter translation driver.
#
# WHY THIS EXISTS
# ---------------
# Translation used to run as a detached background process (`nohup hermes chat &`).
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
  echo "committed $(lang_name "$lang") — checkpoint saved ($(git rev-parse --short HEAD))"
}

case "${1:-}" in
  status) shift; cmd_status "$@" ;;
  verify) shift; cmd_verify "$@" ;;
  commit) shift; cmd_commit "$@" ;;
  *) cat <<EOF
translate.sh — durable, resumable newsletter translation driver

  status <YYYY-MM-DD>          what is missing, per language (safe to run anytime)
  verify <lang> <YYYY-MM-DD>   check one language: files, links, encoding
  commit <lang> <YYYY-MM-DD>   verify then commit one language (a checkpoint)

Languages: ${LANGS[*]}

Generation stays an Opus agent (see skills/_COMPASS/agents/TranslationAgent.md).
Run one language at a time and commit each; a crash then loses at most one language,
and 'status' tells you exactly where to resume.
EOF
  ;;
esac
