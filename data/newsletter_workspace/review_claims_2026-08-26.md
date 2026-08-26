# Stage 7 ClaimCheck — Compass Newsletter #37 (rerun)

Reviewed: `content/en/newsletters/2026-08-26-newsletter.md` (current 148-line draft)

Verification time: 2026-08-26 UTC. This is a fresh live-source rerun. GitHub repository, PR, release, tag, compare, commit, and file data were queried through `gh api`; pakstr release metadata came from the live Forgejo API and every consecutive tag range was independently cloned and diffed; Postr was cloned from the URL in its NIP-34 announcement. The walls.rip deployment and exact pinned repository source were inspected directly. No project description was treated as proof of standards conformance when source or the normative NIP said otherwise.

## Result

No blocking factual contradiction remains. All eight prior blockers/major findings have been corrected in the revised draft. Every NIP label in the draft was checked against the live NIP registry, every internal NIP topic target exists, and every tagged release was checked against its complete release notes and full previous-tag diff.

## Prior-blocker recheck

| Prior issue | Revised text | Live primary-source verification | Result |
|---|---|---|---|
| Infans / NIP-44 mismatch | Lines 24–26 now say the repository labels its local cipher NIP-44 but the implementation uses AES-256-GCM, so it must not be presented as NIP-44 compatible; the Amber path is described without claiming end-to-end interoperability proof. | Infans remains at commit `34f0d8443dfa6dad18a137896efbeff5363b7385`. Its `Nip44.kt` uses `AES/GCM/NoPadding`, an AES key, and `GCMParameterSpec`. Live NIP-44 at NIP-registry head `735a25e44b8e7a01539864f2a2dcf3e728977fd3` specifies v2 as ECDH + HKDF + padding + ChaCha20 + HMAC-SHA256. Sources: <https://github.com/TurkeyNostr/infans/blob/34f0d8443dfa6dad18a137896efbeff5363b7385/app/src/main/java/com/turkbot/babytracker/nostr/crypto/Nip44.kt>, <https://github.com/nostr-protocol/nips/blob/735a25e44b8e7a01539864f2a2dcf3e728977fd3/44.md>. | **PASS** |
| NIP-5D and NAP-DISPLAY status | Line 94 calls NAP-DISPLAY an open draft and NIP-5D a separately unmerged proposal, links the local proposal topic page, and consistently uses “would.” | `5D.md`/`5d.md` is absent from live NIP master; NIP-5D PR #2303 is open and unmerged at head `24711d9c47bbdd07908bf1d52bf677d9cbc530f0`; NAP-DISPLAY PR #97 is open and unmerged at head `137acd0618c236bb78762246cf7ec8a8934640c7`. Sources: <https://github.com/nostr-protocol/nips/pull/2303>, <https://github.com/napplet/naps/pull/97>. | **PASS** |
| NIP-4e status | Line 58 explicitly calls it the “unmerged NIP-4e encryption-key proposal,” links the prior issue that introduced the draft, and preserves the implementation-divergence caveat. | `4e.md`/`4E.md` is absent from live NIP master; PR #1647 is open and unmerged at head `b22711d050df662bfba5f813a35d801daf067dc8`. Source: <https://github.com/nostr-protocol/nips/pull/1647>. | **PASS** |
| 2023/2024 replaceable-event distinction | Lines 102, 118–126 distinguish 2023 empty-identifier coordinates for regular/non-parameterized replaceable events from the 2024 rename of the separate parameterized-replaceable class to “addressable events.” Line 126 explicitly says NIP-01 still distinguishes the classes. | 2023 commits `208dee210249f84496ddfa823542d023e23b3edb` (NIP-19) and `e50bf508d9014cfb19bfa8a5c4ec88dc4788d490` (NIP-01) add the empty identifier/trailing-colon form for regular replaceables. Commit `ca3c52e3e74f0a4679f1c6c0d9ac6461ea748d2d` renames parameterized replaceables in 2024 without changing wire format. Current NIP-01 retains separate “replaceable” and “addressable” sections. Sources: <https://github.com/nostr-protocol/nips/commit/208dee210249f84496ddfa823542d023e23b3edb>, <https://github.com/nostr-protocol/nips/commit/e50bf508d9014cfb19bfa8a5c4ec88dc4788d490>, <https://github.com/nostr-protocol/nips/commit/ca3c52e3e74f0a4679f1c6c0d9ac6461ea748d2d>, <https://github.com/nostr-protocol/nips/blob/735a25e44b8e7a01539864f2a2dcf3e728977fd3/01.md>. | **PASS** |
| NIP-22 adoption scope | Line 84 limits the convergence claim to Snort and Ditto ordinary **text** replies and expressly says this is not an ecosystem-wide single reply kind. Line 138 preserves Ditto’s kind-1244 voice exception and NIP-10 read compatibility. | Snort commit `420ed60e2ff43bd373f2583e171a77002ec9f3a0` makes kind 1111 the default text-reply path while retaining fallback behavior. Ditto commit `8a0ffc6e3a5d9202ffc452fa0de8ae33b5883384` publishes text as 1111, voice as 1244, and continues reading kind-1/NIP-10 replies. Sources: <https://github.com/v0l/snort/commit/420ed60e2ff43bd373f2583e171a77002ec9f3a0>, <https://github.com/soapbox-pub/ditto/commit/8a0ffc6e3a5d9202ffc452fa0de8ae33b5883384>. | **PASS** |
| NIP-47 fee authority | Line 86 now states the precise protocol gap: no standard client-specified routing-fee ceiling. It does not claim wallets otherwise lack implementation policy or will pay literally any fee. | Current NIP-47 has `fees_paid` but no `max_fee`. Open PR #2444 at head `6210ddc67be489c786bdad624b14d48adb927215` proposes `max_fee`, `FEE_LIMIT_EXCEEDED`, no debit/payment attempt when no compliant route exists, mandatory `fees_paid` for supporting wallets, and unknown-parameter behavior for non-supporting wallets. Source: <https://github.com/nostr-protocol/nips/pull/2444/files>. | **PASS** |
| Postr bootstrap relays | Line 20 now says automatic publication uses NIP-65 write relays **plus encrypted bootstrap relays**, or a custom per-account list. | Canonical clone head `e730de52cdb6471f7bf2ae9575514acfd56e231b` says exactly this in `README.md`. `RelaySettings.kt` confirms automatic NIP-65 selection plus default `wss://` relays (`nos.lol`, `offchain.pub`, `relay.primal.net`) and a per-account manual override. Canonical clone: <https://relay.ngit.dev/npub1qwkd5wzftcxquuhtkcg0xn9ed7evksluuppf7qdmdh34ywe9uncs5uqfvl/postr.git>. | **PASS** |
| Marmot proposal tense | Line 98 opens “An open Marmot experiment would…” and describes the behavior as a draft, not adopted protocol. | PR #417 remains open and unmerged at head `994ba06878d7093e7ba2cf7f6c34b2fe37bc043b`; its full file diff supports component `0x800d`, bounded inline Add/Remove shapes, UpdatePath, five-leaf ceiling, QR/HKDF/ChaCha20-Poly1305 pairing, local kind-453 proofs, and post-Welcome proof. Source: <https://github.com/marmot-protocol/marmot/pull/417>. | **PASS** |

## NIP-reference liveness audit

Registry checked at live `nostr-protocol/nips` master `735a25e44b8e7a01539864f2a2dcf3e728977fd3` (2026-08-25T10:58:34Z). The draft contains 56 NIP-label occurrences covering 23 distinct labels. Every corresponding internal topic file under `content/en/topics/` also exists.

| Draft labels | Registry result | Draft treatment |
|---|---|---|
| NIP-01, 05, 09, 10, 17, 19, 22, 25, 29, 30, 34, 38, 44, 46, 47, 55, 59, 65, 73, 78, 99 | Live merged files present at registry head | Correctly treated as NIPs |
| NIP-4e | No live merged file; PR #1647 open/unmerged | Explicitly “unmerged … proposal,” with prior coverage linked and live PR verified in this review |
| NIP-5D | No live merged file; PR #2303 open/unmerged | Explicitly “unmerged … proposal,” “not a merged NIP,” with the sourced local topic page linked and live PR verified in this review |

Other protocol references were checked live as well: NIP-47 fee PR #2444, NWC-09 PR #5, NAP-DISPLAY PR #97, and Marmot PR #417 are all open/unmerged and are all identified as open drafts/proposals/experiments. NIP-30 PR #2448 is merged (2026-08-25T10:58:35Z), matching “merged addition.” NIP-25 external-content PR #2020 is merged (2025-08-22T16:44:53Z).

## Tagged-release audit against complete notes and diffs

Tag inventory found nine tagged releases cited by the draft. Each was checked against the full release body and full previous-tag diff, not only selected commits. Postr’s repository has no git tags at the checked head; its “Version 1.0.0” is therefore a launch/version claim rather than an omitted tagged-release comparison.

| Release | Complete audit | Assessment |
|---|---|---|
| pakstr v0.13.0 | Forgejo release body plus cloned `v0.12.1..v0.13.0`: 4 commits, 13 files, 748 additions/29 deletions | Automatic release versioning and its review fixes are accurately summarized. |
| pakstr v0.13.1 | Release body plus `v0.13.0..v0.13.1`: 2 commits, 2 files, 6 additions/4 deletions | Base64url Blossom authorization is accurate. |
| pakstr v0.13.2 | Release body plus `v0.13.1..v0.13.2`: 2 commits, 2 files, 5 additions/2 deletions | `Content-Digest` upload header is accurate. |
| pakstr v0.13.3 | Release body plus `v0.13.2..v0.13.3`: 3 commits, 5 files, 241 additions/58 deletions | Publishing the Zapstore application event before Blossom upload is accurate. |
| pakstr v0.14.0 | Release body plus `v0.13.3..v0.14.0`: 2 commits, 9 files, 583 additions/41 deletions | Pre-publish Zapstore publisher validation is accurate. |
| pakstr v0.15.0 | Release body plus `v0.14.0..v0.15.0`: 2 commits, 7 files, 370 additions/23 deletions | Kind-32267 metadata and kind-30063 release-note support are accurate. |
| nostr-java v2.0.8 | GitHub release body plus `v2.0.7...v2.0.8`: 3 commits, 12 files | Lines 44–46 accurately cover subscription-id routing, connection-scoped frames, lightweight ChaCha20, removal of provider side effects, Android behavior, and caller impact. Complete notes also mention the added BC-deregistered reference-vector tests; omission is not misleading. |
| NoorNote v1.3.6 | GitHub release body plus `v1.3.5...v1.3.6`: 6 commits, 36 files | Lines 50–52 accurately cover NIP-38 statuses, NIP-99 rendering, marketplace-addon scope, and private petname styling. Omitted long-unbreakable-draft scrolling and system-log status entry are unrelated, non-misleading omissions. |
| nostrord v2.9.0 | GitHub release body plus `v2.8.0...v2.9.0`: 79 commits, 170 files | Lines 56–58 accurately describe relay-scoped leave/delete state, already-member self-heal, markdown images, NIP-17 kind-15 media, and selected NIP-4e work, now correctly marked unmerged. The full tag is much broader (including NIP-78 muting, NIP-46 QR fix, mentions, notification deduplication, pairing/history backup, and many group/DM/cache fixes), but the paragraph uses “also” as selected highlights and makes no completeness claim. |

Primary release/compare sources: <https://git.nostrdev.com/stuff/pakstr/releases>, <https://github.com/tcheeric/nostr-java/releases/tag/v2.0.8>, <https://github.com/tcheeric/nostr-java/compare/v2.0.7...v2.0.8>, <https://github.com/77elements/noornote/releases/tag/v1.3.6>, <https://github.com/77elements/noornote/compare/v1.3.5...v1.3.6>, <https://github.com/nostrord/nostrord/releases/tag/v2.9.0>, <https://github.com/nostrord/nostrord/compare/v2.8.0...v2.9.0>.

## Remaining claim matrix

| Section | Live evidence checked | Assessment |
|---|---|---|
| Postr launch | Canonical repository head, README, relay selection, outbox/readback, attachment, draft, privacy and NIP-34 publication sources | Supported; bootstrap-relay omission corrected. |
| Infans launch | Repository head, README, local database/backup/sync paths, actual cipher source, NIP-44 normative text | Supported only with the caveats now present; revised text is accurate. |
| walls.rip Ghost Chat | Live deployment plus repository `cf40bda32df5f106007631b21afc3cd193ac0cda`: `useGhostWire.ts`, `nostrService.ts`, OpenPGP identity flow, default relay list, kind 1 template, room-tag filter, and local session storage | Nostr Relay test passes because relay traffic is the actual transport. So What test passes as a concrete, caveated example of decentralized transport with recipient-derived metadata and no NIP-17 interoperability. |
| Heterodyne | Live Radicle repository/readme at the cited RID and KERI primary paper | Four-layer/four-draft, incomplete Control, pre-client, 0.x-draft framing remains supported. |
| Shopstr | Merged PRs #436 and #437 (merged 2026-08-24) and full diffs | Browser-storage secret removal, memory lifetime, legacy cleanup, and active-origin caveat are supported. |
| Routstr SDK | Merged PR #47 (merged 2026-08-24) and full diff | Signature verification, future-time filtering on live/stored paths, fail-closed review gate, identity binding, and manual override are supported. |
| nostr-tools | Merged PR #545 and NIP-59 | Wrap/seal kind checks, seal signature, rumor/seal pubkey bind, and batch skip behavior are supported. |
| NWC-09 | Open NWC PR #5 at head `bc13b2c32c897ae3cad7ec4cd79ba8e6998a8331` | Selector exclusivity, common result envelope, visibility/non-disclosure, ambiguity handling, and no enumeration are correctly presented as a draft. |
| August 2021–2026 history | Repository commit windows and cited commits/PRs, current NIP text, Snort/Ditto commits | Chronology is supported. The former replaceable/addressable conflation and ecosystem-wide NIP-22 claim are corrected. Interpretive “six-year shift” language is clearly synthesis, not a false causal claim. |

## Gate

The revised draft corrects every prior blocker, accurately distinguishes merged NIPs from open proposals, preserves the 2023/2024 replaceable-event distinction, limits NIP-22 adoption claims to the evidenced clients and text-reply scope, states NIP-47 fee authority precisely, includes Postr’s bootstrap relays, keeps Marmot in proposal tense, and describes walls.rip from its deployed application and pinned source without presenting its app-specific kind 1 transport as a standard private-message protocol. All NIP references are live or explicitly identified as unmerged, and all nine tagged releases were verified against complete notes and full diffs.

GATE: PASS (fresh live-source rerun at registry head `735a25e`: eight prior blockers corrected; walls.rip Nostr Relay and So What tests source-verified; 23 distinct NIP labels checked; nine tagged releases audited against complete notes and full previous-tag diffs; remaining claim matrix source-verified)