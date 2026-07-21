# Human overrides — Newsletter #32 (2026-07-22)

Applied post-Stage-8 during the second independent review round (2026-07-21, after
handoff). Any resumed Writing/Assembly stage MUST preserve these.

## Prose fixes (second review round, GATE: FAIL resolved)

- Line ~30 lead NIP-29 story: "its heaviest spec week in recent memory" → "an unusually
  heavy spec week" (unsupported superlative removed).
- NIP-47 sections (lines ~86 and ~118): "among/one of the most widely deployed NIPs" →
  reworded without the unsourced superlative ("implemented across a large share of Nostr
  wallets and apps" / "Given how widely NIP-47 is deployed across wallets and apps").

## Content additions (second-round coverage audit)

- Tagged releases: noscall v0.6.0 (UnifiedPush migration, tag is literally
  `v0.6.0-release`), nostr-vpn v4.1.1 (Zapstore launch), StableKraft and Hakari
  (new Zapstore apps) added as one-liners inside the renamed
  "nostr-social-graph 2.0.0 and the rest of the week's smaller launches" section.

## Redundancy cuts (second-round coverage audit)

- Nostrord v2.3.0 tagged-release section compressed to two sentences (was ~80%
  duplicate of the lead story); kept PR #192 which the lead does not list.
- nostr-social-graph 2.0.0 section compressed to three sentences (was duplicate of
  Iris lead story).

## Topic-page anchor fix

- nip-42.md and nip-43.md "Mentioned in" anchors corrected to
  `#nip-deep-dive` after verifying against Hugo's generated HTML (the assumed
  `#nip-deep-dive-nip-42-and-nip-43` anchor does not exist).

## Deliberately NOT changed (audit flags considered and rejected)

- Sonar v0.1-alpha.11 one-liner retained (follow-up convention for last week's lead).
- NIP-91 watch-list entry retained (draft correctly flags number as provisional).
- chama v5.3.0, n_cord v1.1, Whitenoise Linux NIP-34 announcement: omitted per
  triage/selection judgment; borderline, no override.
