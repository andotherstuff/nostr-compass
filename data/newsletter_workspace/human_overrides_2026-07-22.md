# Human overrides — Newsletter #32 (2026-07-22)

Applied post-Stage-8 during review rounds (2026-07-21, after handoff). Any resumed
Writing/Assembly stage MUST preserve these. NOTE: the assembled draft is now the
authoritative text; section files were re-synced from it after the final restructure.

## Editorial restructure (user feedback round, 2026-07-21)

- Lead stories: NIP-29 spec lead replaced with a Nostrord v2.3.0 app lead
  ("Nostrord v2.3.0 ships group moderation, mute lists, and onion relays"); spec
  detail lives only in the protocol section. Apps first; spec in spec section.
- Unreleased changes is apps-only: NIP-47 simplification and Trusted Relay
  Assertions items moved out, covered only in Protocol work and NIP updates.
- Zapstore 1.1.0: Amber connection is NIP-55 (Android signer), not NIP-46;
  background auto-updates highlighted as the headline feature.
- IndieSats: "published as a kind:1 note on 2026-07-20" → "published on July 20"
  (never narrate where content was found; human-readable dates only). Removed
  the Zapstore v1.1.1–v1.1.3 corroboration sentence.
- Iris story: removed "the stack site shipped no release of its own".
- nostr-social-graph consolidated: full treatment in the Iris lead only; the
  tagged-release slot became "The week's smaller launches" (noscall, nostr-vpn,
  StableKraft, Hakari) with no social-graph repeat.
- nostr-vpn: "shipped an update on Zapstore", not "launched" (already listed).
- Nostrord tagged-release duplicate cut to a two-sentence follow-up pointer.
- ClipRelay and Wisp descriptions rewritten denser (mechanism, platforms,
  encryption, concrete fixes) — general rule: more meat, fewer thin sentences.
- NIP Deep Dive fully rewritten to house format: TWO related NIPs (42+43),
  problem framing, one annotated JSON event per NIP, history (first commits),
  verified Implementations section, "How They Work Together". Matches the
  NIP-86/NIP-99 format from 3-5 issues back.

## Second review round fixes (earlier same day)

- Prose: removed two unsupported superlatives ("heaviest spec week in recent
  memory", "most widely deployed NIPs" x2).
- Coverage additions: noscall v0.6.0, nostr-vpn v4.1.1, StableKraft, Hakari.
- ClipRelay + StableKraft + Hakari added to data/projects.yml.
- 14 topic-page Mentioned-in entries added and anchors verified against Hugo
  HTML output (deep-dive anchor is #nip-deep-dive-nip-42-and-nip-43; nip-29
  points at the Nostrord lead; nip-47/66/TRA point at the protocol section).

## Deliberately NOT changed

- Sonar v0.1-alpha.11 one-liner retained (follow-up convention for last week's lead).
- NIP-91 watch-list entry retained (flagged provisional in text).
- chama v5.3.0, n_cord v1.1, Whitenoise Linux NIP-34 announcement: omitted per
  triage/selection judgment.
