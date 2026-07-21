# Selection Review — Newsletter #32 (2026-07-22)

Input: `triage_2026-07-22.md` (GATE: PASS, 14 GREEN / 30 MAYBE / 38 SKIP). Continuity baseline: #31 (2026-07-15). July 22 is NOT month-end (next Wednesday Jul 29 is still July — month-end history issue is #33) — regular two-NIP deep dive applies.

NIP-number citations this week were already verified at triage (`gh api repos/nostr-protocol/nips/contents/<NN>.md`): NIP-56, NIP-51, NIP-29, NIP-46, NIP-42, NIP-43, NIP-47, NIP-65, NIP-17, NIP-13, NIP-66 all exist. "NIP-9A" (noscall release notes) is 404 — describe the noscall push-notification feature without a number. "NIP-91" and "NIP-5D" are open-proposal numbers not in the repo — treat as drafts.

## NIP Deep Dive selection

**Primary: NIP-42 (Authentication of clients to relays)** and **Secondary: NIP-43 (Relay Access Metadata and Requests)** — neither appears in the rotation history (`grep -E "^## NIP Deep Dive" content/en/newsletters/*.md` confirms; covered list runs NIP-01…NIP-99, does not include NIP-42 or NIP-43). Both already have topic pages (`content/en/topics/nip-42.md`, `content/en/topics/nip-43.md`) needing "Mentioned in" updates. Editorial anchor: this week's nostream PRs [#702](https://github.com/Cameri/nostream/pull/702) (NIP-42 read-restriction of encrypted kinds to authenticated recipients) and [#676](https://github.com/Cameri/nostream/pull/676) (NIP-43 join/leave request strategies) ship exactly the relay-side access-control pair — the Deep Dive explains the two-NIP handshake (auth challenge → membership state) that nostream just implemented. Connection: NIP-42 proves *who you are* to a relay; NIP-43 manages *what members can do* once authenticated — together they are the access-control stack relay groups and paid/private relays are converging on.

## Section allocations

### News / Top Stories (5)

1. **IndieSats pivot — music platform becomes pure Nostr infrastructure** (LEAD). Announced 2026-07-20 via kind-1 note, corroborated by zapstore updates v1.1.1–v1.1.3. Drops publisher role (key custody, whitelist, mandatory 2% cut); relaunches as open relay + player + discovery layer with artists publishing under their own Nostr profiles, opt-in revenue splits, kind-5 deletion support. Score 10/10 (3 nostr + 3 impact + 3 breadth + 2 novelty, no bonus needed; sets ecosystem precedent for platform-to-protocol pivots).
2. **NIP-29 relay-groups spec week** — subgroups (PR #2319, merged 07-16), message pinning kind:9010 + kind:39005 (PRs #2379, #2416, merged 07-15/07-17), banner tag + invite-code suffix (PRs #2383, #2380, merged 07-16), all by nostrord contributor Anderson-Juhasc, matching shipped Nostrord v2.3.0 features (cross-platform NIP-51 mute lists, wired-up NIP-29 moderation, consent-gated group invites, Tor .onion relays). Spec and client landing in the same week from the same author. Score 9/10 (spec merges + shipped implementation, 3+3+2+2 = 10 base, -1 for split attribution across items → carried as one combined story).
3. **Zapstore 1.1.0** — portable encrypted device key with Amber backup, opt-in background auto-updates, app-catalog relays as device-signed kind:10067 events, NIP-56 verified app reporting, C1 proof verification before install. Last covered 2026-03-04 — big delta. Score 9/10.
4. **kind:10011 → kind:10021 favorite follow sets (fiatjaf)** — PR #2413 merged 07-15, open renumbering PR #2417 because 10011 was already in use. Live spec-coordination story: a merged list kind already moving. Score 8/10.
5. **Iris-ecosystem cluster (nostr-pubsub + fips-ts + nostr-social-graph 2.0.0, with Iris Stack as framing)** — three new-at-intake GREENs from the mmalmi ecosystem in one week: transport-neutral pubsub library (v0.1.3–v0.5.2), browser TypeScript FIPS runtime with Nostr signaling (0.0.24–0.0.30, wire-compatible with jmcorgan/fips), and nostr-social-graph 2.0.0 (signed identity roster ops, device-approval bootstrap URI, FIPS identity facets). Iris Stack site (stack.iris.to, no release) used as connective tissue only — the anchor items are the three released GREENs. Score 8/10 as a combined ecosystem item. (+2 first-coverage novelty bonus applies to nostr-pubsub and fips-ts individually; base floors met.)

### Releases (7)

- **Amber v6.3.0** — grouped multi-request approval for bunker signing, Expert List (kind:12022)/Expert Pack (kind:32022) support, privacy mode, NIP-65 relay-list fetch before profile metadata. Score 7/10. Continuity: follow-up to 2026-07-08.
- **Nostrord v2.3.0** — the client half of the NIP-29 story (shipped cross-platform mute lists, moderation actions, consent-gated invites, Tor relays); one short paragraph back-referencing the News item, not a duplicate writeup. Score 7/10. Continuity: last covered 2026-06-24.
- **Wisp v1.2.0** — multi-account switcher, collapsible reply threads, tracking-param stripping, wallet transaction history. Score 6/10. Continuity: follow-up to 2026-07-08.
- **ClipRelay v0.1.2 (NEW, Discovery slot)** — new Zapstore launch: clipboard sync across devices over Nostr relays. Simple, legible Nostr-native utility; strongest of the untracked candidates. Score 7/10 (base 5 + 2 first-coverage bonus; floor met). **projects.yml addition required** (intake-followup list).
- **Sonar v0.1-alpha.11** — one-line-to-short follow-up only: Rust mesh link engine, BLE/mesh fixes, relay diagnostics. Sonar was #31's lead; this is an incremental alpha cut. Score 5/10 (auto-demote -2 for coverage in last 2 issues).
- **nostr-social-graph 2.0.0** — one paragraph as the shipped component of the Iris-ecosystem News item (major version: signed roster ops, device approval, FIPS facets). Score 7/10.
- **Amethyst v1.13.0 pre-release QA** (PRs #3650, #3653, #3654; 81 merged PRs) — napplet account isolation, Concord authority fixes landing ahead of v1.13.0. Continuity framing from #31's lead-adjacent Concord/Vector coverage: the Concord client implementation story continues. Score 6/10.

### Notable Changes (4)

- **Cameri/nostream NIP-42/43 PRs** (#702, #676; 7 merged PRs) — relay-side access control, no release cut. This is the Deep Dive anchor; 2-3 sentences here pointing at the Deep Dive. Score 8/10.
- **NIP-47 simplification (PR #2419, open, frnandu)** — proposes simplifying the NWC core spec and moving functionality into extensions; structural debate on one of the most-deployed NIPs. Discussion-watch item. Score 6/10.
- **FIPS v0.4.1 (jmcorgan/fips)** — maintenance release (antipoison caps, convergence/MTU fixes, CPU cuts) but named here as the Rust transport the fips-ts browser runtime is wire-compatible with; one short supporting paragraph under the Iris cluster, not a standalone feature. Score 5/10 (maintenance -4 demote offset by connective-tissue role).
- **Trusted Relay Assertions draft (PR #2418, open, wisp contributor Letdown2491)** — new proposal for publishing relay trust assertions (NIP-66 metrics, operator reputation, reports). Early, no number assigned; describe as draft. Score 5/10.

### NIP Updates

**Merged (this window):**
- NIP-29 subgroups — [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) (merged 2026-07-16)
- NIP-29 message pinning, kind:9010 + kind:39005 — [PR #2379](https://github.com/nostr-protocol/nips/pull/2379) (merged 2026-07-15); `a`-tag pin lists — [PR #2416](https://github.com/nostr-protocol/nips/pull/2416) (merged 2026-07-17)
- NIP-29 banner tag — [PR #2383](https://github.com/nostr-protocol/nips/pull/2383) (merged 2026-07-16); invite-code suffix — [PR #2380](https://github.com/nostr-protocol/nips/pull/2380) (merged 2026-07-16)
- kind:10011 favorite follow sets — [PR #2413](https://github.com/nostr-protocol/nips/pull/2413) (merged 2026-07-15)
- NIP-46 silent-timeout guidance — [PR #2375](https://github.com/nostr-protocol/nips/pull/2375) (merged 2026-07-15)

(The NIP-29 cluster items cross-reference the News story; NIP Updates carries the bullet mechanics.)

**Open (watch list):**
- kind:10021 renumbering of favorite follow sets — [PR #2417](https://github.com/nostr-protocol/nips/pull/2417)
- NIP-47 simplification — [PR #2419](https://github.com/nostr-protocol/nips/pull/2419)
- Trusted Relay Assertions (no number yet, draft) — [PR #2418](https://github.com/nostr-protocol/nips/pull/2418)
- NIP-91 (proposed) AND operator for filters — [PR #2252](https://github.com/nostr-protocol/nips/pull/2252); number not in repo, describe as draft
- NIP-5D (proposed) nostr web applets — [PR #2303](https://github.com/nostr-protocol/nips/pull/2303); number not in repo, describe as draft; timely given Amethyst napplet work this week

### NIP Deep Dive (2)

- **NIP-42 (Authentication of clients to relays)** — not in rotation; anchor: nostream PR #702.
- **NIP-43 (Relay Access Metadata and Requests)** — not in rotation; anchor: nostream PR #676.
- Connection: relay-side access-control pair — authentication (42) then membership/authorization (43) — the stack nostream just shipped and relay groups are building on. Full JSON event examples with all 7 NIP-01 fields required per the Deep Dive JSON rule.

### Discovery Slot (Change C — exactly 1)

Selected candidate: **ClipRelay** ([tajava2006/cliprelay](https://github.com/tajava2006/cliprelay))
- Why it qualifies: new Zapstore app with a named Nostr surface (clipboard sync over Nostr relays); new_app, strong-keyword relevance.
- Newsletter placement: Releases (listed above), flagged as new project.
- projects.yml addition: YES (Assembler must add in the same PR).

## SKIP list (not included, with reasons)

- **Sonar beyond the one-line follow-up** — was #31's lead; alpha.11 is incremental (redundancy auto-demote).
- **VectorPrivacy/Vector v0.4.0/v0.4.1** — Concord move was lead-adjacent in #31 (2026-07-15); this week is incremental bots/slash-commands. Redundant.
- **fips-tcp v0.2.0** — Nostr surface too indirect (signaling lives in fips-ts); folded into Iris cluster as context only.
- **iris-kit v0.2.0–v0.2.4** — UI-primitive plumbing, no Nostr surface of its own; context only.
- **hashtree 0.2.114** — 22-tag monorepo churn; covered 2026-06-17; no per-item substance.
- **Origami74/myco v0.2.0** — follow-up to 2026-07-01 coverage, borderline substance; below depth minimum this week.
- **mattn/nostr-relay v0.0.247** — NIP-17 advertisement in supported_nips is real but one-line; covered 2026-07-08.
- **fiatjaf/nak v0.20.1** — 38 PRs of maintenance/bugfix, no headline feature; fails so-what.
- **AustinKelsay/snstr v0.5.0** — cleanup refactor, no new Nostr surface.
- **sanah9/noscall v0.6.0** — Cashu wallet has no NIP-60/61 surface; push-notification piece is thin and its "NIP-9A" citation is a 404. Below depth minimum.
- **jesuspirate/chama v5.3.0** — follow-up to 2026-06-17; market features ride rails already covered.
- **0n4t3/n_cord v1.1** — real NSEC-bunker surface but small; borderline, cut for depth budget.
- **block/buzz** — 315 PRs but release-level changes are fixes/polish; no headline this week.
- **moogmodular/earthly v0.0.1–0.0.3** — new collaborative-maps app, genuinely Nostr, but feature depth unverified; candidate for a future Discovery slot once it matures.
- **mmalmi/nostr-vpn v4.1.1** — Zapstore NEW app but no changelog detail; substance is the listing itself, below bar.
- **git.reya.su/reya/coop-mobile v0.2.5/v0.2.6** — steady incremental client work; below depth minimum.
- **divinevideo/divine-mobile** — follow-up to 2026-07-15 ProofMode lead; nothing headline-sized.
- **privkeyio/keep-android** — security hardening, real but incremental.
- **marmot-protocol/mdk** — dev-facing tooling (TUI revamp, epoch-stall forensics); covered 2026-07-15.
- **codeswot/ZapBook** — small-project feature work, borderline; cut for budget.
- **Conduit-BTC/conduit-mono** — zap hardening, covered 2026-07-15; incremental.
- **MostroP2P/mostro** — Cashu escrow DB helpers; Nostr surface thin this week.
- **Whitenoise Linux (darkmatter-linux) NIP-34 announcement** — announcement-only, 0 patches; intake-followup candidate, no coverage this week.
- **OpenDiscord (Recap #9)** — Recap-only sourcing, no primary-source verification this run. Intake-followup.
- **StableKraft, Hakari (Zapstore NEW)** — feature depth unverified; ClipRelay took the single Discovery slot. Intake-followup list.
- **PQ-hybrid signature NIP draft (nip_discussions)** — unofficial community draft, conversation-starter only; not cited as a NIP.
- **Encrypted Betting Pools (PR #2415), Metadata-and-drive (PR #2412), NIP-13 prefix filters (PR #2122)** — low signal, per triage.
- All 38 triage SKIP verdicts (relayer, elisym, nostr-mail-client, Haven-App, astraea, Alby extension, bitcoin-safe, Lightning.Pub, lnbits, angor, mesh-llm, nostr-codex-phone, auditable-voting, NostrAppShell, nostr-double-ratchet, bray, bark, smolgrrr/Wired+TAO, zapcooking, lumilumi, shopstr, dpyc-oracle, zeus, nutshell/cdk, ClauseShift, ngit/Codeberg, nostr-rs-relay/Sourcehut, remaining NIP-34 repos, other Recap items) — reasons documented per-item in `triage_2026-07-22.md`.

## Redundancy check against #31 (2026-07-15)

Checked against `data/coverage_history.json` and #31's selection review:

- **Sonar**: was #31's lead → demoted to a one-line follow-up in Releases; no feature paragraph.
- **Vector/Concord**: #31 covered the Concord-protocol move lead-adjacent → this week's Vector item skipped entirely; Amethyst's Concord QA item carries the continuity instead with explicit "follow-up to #31" framing.
- **kind:10011 favorite follow sets**: appeared in #31 as an OPEN PR bullet; this week it is MERGED plus a live renumbering story — fresh status, not duplicate coverage; framed as "merged last week, already moving."
- **NIP-29 pinning (PR #2379)**: was in #31's open-PR list; now merged, plus #2416 follow-up — status change justifies the bullet, clustered under the NIP-29 News item.
- **Amber, Wisp**: last covered 2026-07-08, new versions with new features — normal release continuity, no duplicated content.
- **Nostrord**: last covered 2026-06-24; v2.3.0 is new. Zapstore: last covered 2026-03-04; no redundancy.
- No item in this selection re-covers prose already published in #31.

## Verification notes

- Deep-dive rotation dedup confirmed via `grep -E "^## NIP Deep Dive" content/en/newsletters/*.md`: NIP-42 and NIP-43 absent.
- Deep-dive NIP existence: NIP-42 and NIP-43 verified at triage (both exist in nostr-protocol/nips).
- Topic pages exist for both: `content/en/topics/nip-42.md`, `content/en/topics/nip-43.md` — need "Mentioned in" updates at write time.
- Month-end check: 2026-07-22 + 7 days = 2026-07-29, same month → NOT month-end; standard two deep dives.
- Writers must NOT cite "NIP-9A" (noscall), "NIP-91", or "NIP-5D" as real NIPs; PR-number links above were pre-verified at triage but writers should re-verify any additional PR numbers before linking per the mandatory verify-before-citing rule.

GATE: PASS
