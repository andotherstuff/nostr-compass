# ClaimCheck Review — 2026-08-05

Draft: `content/en/newsletters/2026-08-05-newsletter.md`
Workflow: global ClaimCheck skill, `NeedsCitation`
Final rerun: 2026-08-05 UTC, from the current synchronized draft

## Result

**Claims needing citations or correction: 0**

The final rerun opened the primary GitHub release records for all selected tagged releases and the current GitHub records for every mentioned protocol pull request. Important Nostr-facing release changes remain represented; generic UI, build, translation, Bitcoin-only, Lightning-only, and Cashu-only changes remain outside Compass scope. NIP PR #2357 was removed because it merged on 2026-06-06, before this issue's window, despite later metadata activity.

The current draft places primary release, pull-request, commit, repository, or specification links next to its empirical and technical claims. No unsupported causal claim, comparative superlative, ranking, or claim materially stronger than its cited evidence was found.

## Prior-fix verification

All six findings from the preceding ClaimCheck run were checked against the synchronized draft and their primary evidence.

| Prior finding | Current draft evidence | Result |
|---|---|---|
| Primal remote-signing overclaim | Line 26 now says the remote signer was updated for recent protocol changes and lists follow mute, connection recovery, 100 MB cache, and invalid follow-list fixes. The linked 3.5.25 release notes state each item. | FIXED |
| Nostur unsupported architectural inference | Line 30 now limits the claim to private replies, media handling, live-chat replies, and room-title notifications. Tag-reachable commits include `c64460b8` (private-reply lock), `41f87310` (DM media cache controls), `5f41f3d6` (live-chat reply parent context), and `37256b74` (chat-room titles in mention notifications). The separate-service inference is absent. | FIXED |
| Chama reinstall/cross-device recovery overclaim | Line 34 now scopes repair to events already in the device's durable cache and says recovered events are offered to the community relay. The linked v5.7.0 notes explicitly describe retrying an incomplete replay against the cache and re-offering recovered events. Reinstall and device-migration claims are absent. | FIXED |
| Auditable Voting organizer-signed questionnaire inference | Line 38 now repeats the linked v0.1.165 notes: authenticated delegation delivery/control-DM backfill, private-relay blind-credential DMs, and audit proxy v0.1.52. The unsupported questionnaire relationship is absent. | FIXED |
| Gamma Markets no-change claim | The Gamma Markets subsection and window-specific negative claim are absent from the synchronized draft. | FIXED |
| nostrsearch NIP-50 implementation contradiction | The nostrsearch paragraph and implementation claim are absent. The NIP-50 deep dive now relies on the canonical NIP-50 specification. | FIXED |

The obsolete phrases were also searched literally and were absent: `state transitions around signing sessions`, `separate account or notification service`, `reinstalled or moved to another device`, and `organizer-signed questionnaire`. Neither `Gamma Markets` nor `nostrsearch` appears in the current draft.

## Canonical NIP identifier verification

Every distinct `NIP-[0-9A-Z]+` identifier in the current draft was checked against `https://api.github.com/repos/nostr-protocol/nips/contents/<ID>.md` during this rerun. All 15 returned HTTP 200:

| Identifier | Canonical file result |
|---|---|
| NIP-01 | 200 (`01.md`) |
| NIP-07 | 200 (`07.md`) |
| NIP-11 | 200 (`11.md`) |
| NIP-17 | 200 (`17.md`) |
| NIP-22 | 200 (`22.md`) |
| NIP-29 | 200 (`29.md`) |
| NIP-33 | 200 (`33.md`) |
| NIP-44 | 200 (`44.md`) |
| NIP-46 | 200 (`46.md`) |
| NIP-47 | 200 (`47.md`) |
| NIP-49 | 200 (`49.md`) |
| NIP-50 | 200 (`50.md`) |
| NIP-51 | 200 (`51.md`) |
| NIP-77 | 200 (`77.md`) |
| NIP-B0 | 200 (`B0.md`) |

No fabricated or unmerged identifier is presented as an established NIP.

## Evidence summary

- Canonical NIP existence: GitHub Contents API against `nostr-protocol/nips`; 15/15 identifiers returned HTTP 200.
- Primal: linked 3.5.25 release notes matched every narrowed claim at line 26.
- Nostur: tag `1.30.2` resolves to an annotated Git tag; the tag-reachable commit history contains direct commits for the four narrowed behaviors at line 30.
- Chama: linked v5.7.0 release notes matched the cache-scoped repair and community-relay re-offer at line 34.
- Auditable Voting: linked v0.1.165 release notes matched all three statements at line 38.
- Former unsupported Gamma Markets and contradicted nostrsearch claims are absent.
- The NIP-50 and NIP-B0 deep dives cite their canonical specification sections for wire-format and event-model claims.

**Verdict:** WELL-SOURCED.

GATE: PASS — rerun against the final synchronized draft; the prior findings remain fixed and no unsupported current-window claim remains.
