# Review Swarm Log — Newsletter #31 (2026-07-15)

Draft: `content/en/newsletters/2026-07-15-newsletter.md`

## LinkChecker — GATE: PASS

- 83 external links extracted and curled (`-L --max-time 15`). All returned HTTP 200 on first attempt; no retries needed.
- 20 internal `/en/topics/` links checked against `content/en/topics/*.md` on disk. All 20 resolve to existing files (nip-05, nip-13, nip-15, nip-17, nip-29, nip-30, nip-44, nip-46, nip-47, nip-49, nip-50, nip-55, nip-57, nip-59, nip-65, nip-66, nip-85, nip-99, marmot, blossom).
- 37 in-page anchor links (`#...`) checked against generated H2/H3 slugs. All 37 resolve; zero orphaned anchors.
- `hugo --buildFuture` (page is dated one day ahead of system clock, 2026-07-15 vs. today 2026-07-14, so `--buildFuture` was needed only for local preview; normal weekly `hugo` build succeeds once the publish date arrives) completes with exit 0, 277 EN pages generated, no template errors.

## ClaimCheck — GATE: PASS

- Every PR, release, and NIP claim in the draft carries a direct source link (spot-checked against the gh api/gh release bodies gathered during Selection/Writing).
- Confirmed no citation of the fabricated "NIP-9A" label Noscall's own changelog uses; the push-notification migration is described by mechanism (Firebase Cloud Messaging to Nostr-relay-based delivery via UnifiedPush) without asserting a NIP number, per the source-integrity flag raised in `selection_review_2026-07-15.md`.
- Tag names verified against live GitHub releases where triage URLs were ambiguous or wrong (n_cord v1.1, Nostr WoT 0.3.86, Noscall v0.6.0-release, echoes v.0.1) — final draft uses the corrected tags throughout.
- Discovery-slot mechanic honored: exactly one new `projects.yml` addition this issue (Cambium, under `signers`), matching the Selection stage's designated pick.
- No superlatives ("biggest release," "game-changing," etc.) carried into prose from source release notes.

## ProseReview — GATE: PASS (one fix applied)

- Zero em dashes, zero curly quotes, zero exclamation marks in the draft.
- Zero hits for banned hype/filler phrases (exciting, game-changing, groundbreaking, cutting-edge, seamless, leverage, it's worth noting, delve into, dive into, unlock the, paradigm shift).
- One rhetorical question found in the NIP Deep Dive opening paragraph ("...same question: how does a seller describe something for sale as a signed event, and how does a buyer find and act on it?") — rewritten to a declarative construction ("...same problem: how a seller describes something for sale as a signed event, and how a buyer finds and acts on it."). Re-scanned after fix: zero remaining rhetorical questions outside the standing closing-footer boilerplate ("Building something or have news to share?"), which is identical across every prior published issue (#1–#30) and not new prose introduced this run.
- No passive "was/were [verb]-ed by" constructions found.
- Paragraph-opener scan across all 34 `###` items: every lead sentence opens with the distinct linked project/PR name as required by the source-linking convention; no run of 3+ consecutive identical non-project openers.
- One-project-per-header rule respected, with the pre-existing, explicitly-documented exception carried from #30: Wired and TAO share a single header because they share one literal PR list (twin-app precedent already used in #30's proof-of-work item). "Also shipped" and "Also launching this week" grouped paragraphs used for low-signal items per the sanctioned grouping pattern, not as a way to dodge one-header-per-project for substantive items.

## TopicAudit — GATE: PASS

- NIP Deep Dive NIPs (NIP-15, NIP-99) confirmed to have existing topic pages; both received new "Mentioned in" entries pointing at the #31 deep-dive anchor.
- Eight additional topic pages with substantive #31 coverage (not just a passing inline link) received "Mentioned in" entries: nip-85 (Amethyst), nip-29 (message-pinning PR), nip-66 (relay-discovery restructure PR), nip-57 (Wired/TAO), nip-49 (Nostr WoT + Nostr Docs, two entries), nip-55 (Cambium), nip-47 (cdk), nip-46 (Vector + n_cord, two entries).
- No new topic pages required this issue; all cited NIPs already had pages.
- `data/projects.yml` Discovery-slot addition (Cambium) validated as parseable YAML (`python3 -c "import yaml; yaml.safe_load(...)"`).

## Build-environment fix (infrastructure, not content)

Hugo's default data-directory loader attempted to parse the pipeline's own workspace markdown files (`data/newsletter_workspace/sections/*.md`) as structured data and failed the build (`unmarshal of format "" is not supported`). Added `ignoreFiles = ['newsletter_workspace']` to `hugo.toml` so the workspace directory documented in `OrchestratorAgent.md` ("Workspace files for previously-published newsletters can be left in place as historical record") can coexist with Hugo's `data/` directory without breaking builds. This is a one-line, additive config change; no existing behavior changes for any other content.

## Outcome

All four reviewers report GATE: PASS after one ProseReview fix (rhetorical question rewrite, applied and re-verified). No further iteration needed.

GATE: PASS
