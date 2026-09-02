# Independent Stage 4 discovery selection review — Newsletter #38 (2026-09-02)

Mode: selection only; no newsletter copy.

## Verdict

**PASS** — all 6 returned GitHub owner siblings, all 10 NIP-89 candidates, all 20 Recap events, and all 4 active NIP-34 repositories were dispositioned. Two candidates merit consideration: **Napstr (PASS, preferred new-project slot)** and **RSSNotes (PASS, backup compact update, not a discovery slot because it is already tracked)**. No app-discovery row or NIP-34 issue-only row independently clears a newsletter slot.

Coverage caveats are quarantined exactly as required: the six GitHub siblings are only the six rows returned before 417 quota-guard errors, not a complete owner sweep; NIP-89 is partial because one relay timed out; the 1,316-row Zapstore file is a baseline and proves no weekly delta. No negative ecosystem claim is inferred from those limitations.

## Slot recommendations

### PASS — Napstr — preferred new-project / New and Noteworthy slot — score 10/12

- Secondary lead: Recap event `68017a01fbc0c59d5034c3e5a91d28261b4b259705e39149665ed6c0d613bb6e`.
- Primary repository: https://github.com/lnbits/napstr
- Primary release: https://github.com/lnbits/napstr/releases/tag/v0.2.0, published `2026-08-26T17:27:48Z`.
- Primary comparison: https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0. In-window commits include `edbe06e` (`feat: audiobook + napstrfy support`) and `f2e8e4e` (handshake timeout and download hardening), plus Android release/build work.
- Canonical README pins the Nostr surface: Nostr carries searchable catalogues, live seeders, NIP-C7 discussion, and NIP-17 private download negotiation; Tor carries file transfers; the Napstrfy phone companion pairs by one-use QR.
- Coverage check: no `lnbits/napstr` entry in `coverage_history.json`, and no Napstr mention in the 2026-08-12, 2026-08-19, or 2026-08-26 newsletters.
- Selection constraint: call this an in-window `v0.2.0` release/new-project introduction, **not** a proven first launch. Recap's bare “New Exploration Tool” label is secondary and does not establish launch date. The release body itself is sparse, so factual detail must come from the canonical README and pinned comparison.

### PASS — RSSNotes — backup compact update only — score 8/12

- Secondary lead: Recap event `3dbcd96efe4feaa41442f108cac586cdf4c4d6ae2f5d8d38d936c9cd19474019`, which discusses `v0.1.3`.
- Primary tracked update: https://github.com/trinidz/rssnotes/releases/tag/v0.1.6, published `2026-08-25T22:49:58Z`; the release body is empty.
- Primary comparison: https://github.com/trinidz/rssnotes/compare/v0.1.4...v0.1.6. Commits include `cb8a8d0` (`relay list events`) and `e8b4cac` (`readonly relay profile`). The canonical README identifies RSSNotes as a read-only Nostr relay that turns RSS feeds into Nostr profiles and notes.
- Duplicate classification: `data/projects.yml` already tracks `trinidz/rssnotes`, and the same `v0.1.6` release plus commits are already present in `data/project_updates/updates_2026-08-18_2026-08-26.json`. Treat Recap as corroboration, not a second item and not discovery.
- Coverage check: no RSSNotes mention appears in the latest three newsletters or `coverage_history.json`.
- Selection constraint: use only if the main selection needs a compact relay/tool update. Do not repeat Recap's `v0.1.3` feature list as if it described `v0.1.6`; do not claim substance from the empty `v0.1.6` release notes beyond the pinned commits.

### FAIL — NIP-34 “activity” as a standalone slot

- Artifact: `data/nip34_repos/nip34_2026-08-18_2026-08-26.json` reports **0 patch events** and issue activity only.
- `gitworkshop.dev` repository event `2a22a37316bf8572af8b0ddb05a01286e769e6286e1565beaddb8732b04ab545`: 5 issue events (stacked-PR merge-base warning, merge-commit CI coverage, root-relative markdown links, profile management, markdown preview).
- `Whitenoise Linux` repository event `d53dbf9ed84908277e9ca41ef45b54f5134457e08c6cfb93473d7e8c6e1da90a`: 37 issue events, no patch event.
- `Vidstr` repository event `108641b1b8d357ff2e2e63ff0296e782921a6181bbb8b7347f66bf034613f091`: 2 issue events, no patch event.
- `flotilla-budabit` repository event `8f8672d7f2805899428a5b7551fe216ca70c3814c027c9f761d7e476ca3a6334`: one issue titled `test`, no patch event.
- Issue creation demonstrates NIP-34 collaboration, not shipped behavior. It is weaker than the available release candidates and does not merit a scarce slot. If retained at all, it must be a one-sentence ecosystem metric explicitly saying “issues, not patches/releases.” `gitworkshop.dev` was also mentioned in the 2026-08-12 and 2026-08-26 newsletters, reducing novelty.

## App discovery audit

### Six returned GitHub owner siblings — all FAIL

| Candidate | Live primary-source finding | Verdict |
|---|---|---|
| `ksedgwic/clboss` | Live repo shipped `v0.17.0-rc1/rc2` on Aug 24–25, but it is a Core Lightning node manager; no candidate evidence names a Nostr relay/NIP surface. | **FAIL — off scope.** Triage's implied lack of activity is unsupported; the correct reason is scope. |
| `ksedgwic/xrebalance` | Live repo had Aug 20–26 commits and describes an askrene-based Core Lightning rebalance plugin; no Nostr/NWC behavior is pinned. | **FAIL — off scope.** It was active, so “no in-window change” would be false. |
| `nostriphant/nip-01` | Live Aug 25 commit `eb89744` only updates the license; earlier substantive commits were July. | **FAIL — Nostr-relevant project, maintenance-only in window.** Tracking follow-up may be reasonable, not a slot. |
| `nostriphant/nip-19` | Live Aug 25 commits change copyright and author email; no release. | **FAIL — maintenance-only.** Tracking follow-up may be reasonable, not a slot. |
| `nostriphant/noxtr` | Live Aug 18 commit `e7be707` adds a 22-line `BlossomController.php`, but the class has an empty `hash()` method and no released version in-window. | **FAIL — stub, not working/shipped capability.** Triage's “no change captured” is false; “material Blossom support shipped” would also be unsupported. |
| `nostriphant/relay` | Live Aug 25 commits revise license/contact email and tests; no release. | **FAIL — maintenance-only.** Tracking follow-up may be reasonable, not a slot. |

These are all the returned siblings, not evidence that other owner siblings do not exist. Owner adjacency alone never proves relevance, ownership continuity, or release status.

### Ten NIP-89 handlers — all FAIL for this issue

The relay event IDs are primary evidence that handlers self-published metadata. They do **not** prove repository ownership, implementation completeness, release timing, or every feature in the descriptions.

| Candidate | Evidence checked | Verdict |
|---|---|---|
| Barattolo | Event `85929bfba23d315beae03cf2afbfd7ab9158bb36b7b147dccd280555af4bec75`, multi-relay, kind 30402; `https://barattolo.store` responds but exposes no pinned repository/release in the candidate. | **FAIL — no verified in-window material change.** |
| BlindOracle | Event `5e3cfe19e344d029c3709111a80dfee1ff256831c07c69aa4ed6b64b8fc8df83`, multi-relay; website responds. | **FAIL — extensive privacy/cross-chain/CaMel claims are self-description only; no pinned code/release.** |
| Clestr | Event `ad535a1c170ce6ce49e251721b9d4825e69b5c4d6b82f7be2ef3040f12a6532d`, single-relay; nsite responds. | **FAIL — live surface but no verified repository, release, or in-window change.** |
| Inkan | Event `cb33876173811943105d5bc2a3c6ee4dfe710a17d3b04e42073f033889d4e05a`, multi-relay; `inkan.cc` responds. | **FAIL — “cold-storage identities” claim lacks pinned implementation/release evidence.** |
| Lightning FM | Event `62cafb304ddd9ae152954df3e5fe251254756cd257bc80aac1fa4a7dc529a043`, single-relay; website responds. | **FAIL — working website is not an in-window delta; artist-payment claim remains unsupported here.** |
| MeshLine | Event `85b935e9e526fe6997fc8a43075c81993bf61c8901d931d54bb1d539ad1cac66`, single-relay; website responds. | **FAIL — encrypted messaging/calls/own-relay claims lack pinned code and release evidence.** |
| ox402-utils | Event `a9136ec4099f84017d55e02292de652f355c5b9d8627c50025cfec968f0cb215`, multi-relay; temporary `trycloudflare.com` hostname no longer resolves. | **FAIL — no durable project identity or live release source.** |
| VidStr | Event `617a5dbb77ad5cdc65601d9f066e5e4355e3eb8e76687c5058b818668c3594bf`, multi-relay; website responds. It is the same project as tracked NIP-34 repository event `108641b1...`, which has only two issue events. | **FAIL — duplicate across discovery/NIP-34; feature-rich handler text is not release proof.** |
| Wikistar | Event `d23d0478748427db29cc10f89434def60de0d9985c3da28f077f6795686c412a`, single-relay; website responds. | **FAIL — no verified repository/release or in-window material change.** |
| wordstr | Event `99394f0043a107825f1ea5778bd72e3d904c0211876681a9e377d139584fde37`, multi-relay; website responds. | **FAIL — publication site/handler metadata, not a verified software release.** |

## Recap audit and duplicates

All 20 Recap events were inspected. Recap is secondary and cannot itself prove shipping.

- **PASS leads after primary-source verification:** Napstr and RSSNotes, bounded above.
- **FAIL as new discovery:** Iris Drive event `817f25747753eb40b32218455484506b6348b95011ccf8f479091613ffd3081`. `data/projects.yml` already contains Iris Drive and explicitly flags its substance as unverified; no in-window release or patch event was pinned. Its Recap description of decentralized sync, htree storage, and DNS/SSL/CDN independence is unsupported as a newsletter claim from the available primary evidence.
- **Duplicates/corroboration, not independent slots:** the Recap mobile-release roundup overlaps tracked Divine Mobile, Amethyst, Mostro, nostrord, and other fetched releases; event `4eb904998a53976083d03fc09c662394a9eb3a46b78b896b5daa4c1803b38941` corroborates the already-promoted Nostr Java release; RSSNotes duplicates the tracked update artifact; Lightning.Pub/Nostr VPN and other release roundups must resolve to their canonical release pages before selection.
- **FAIL categories:** memes, meetups, videos/media lists, growth statistics, zap leaderboards, thank-you/quote/challenge posts, and generic roundups do not establish developer shipping. The Recap wording “new,” “biggest release,” “latest,” and feature summaries are unsupported unless independently matched to a project-controlled release/commit.

## Duplicate and unsupported-claim register

1. **RSSNotes:** Recap `v0.1.3` + tracked GitHub `v0.1.6` are one project thread, not two stories.
2. **VidStr:** NIP-89 event + NIP-34 repository/issues are one project, not two stories.
3. **GitWorkshop:** NIP-34 issue activity is repeat coverage after mentions in two of the latest three newsletters; it is also issue-only, not shipping.
4. **Iris Drive:** already in `projects.yml`; it is not an untracked discovery.
5. **Owner siblings:** `clboss` and `xrebalance` were active, contrary to any blanket “no activity” rationale, but are still out of Nostr scope. `noxtr` changed, but only by an empty controller stub. `nip-01`, `nip-19`, and `relay` had maintenance-only commits.
6. **NIP-89 metadata:** self-published descriptions prove advertised handler intent, not implementation, privacy guarantees, payment routing, supported-feature completeness, or release date.
7. **Recap “new” labels:** do not claim first launch for Napstr or Iris Drive. For Napstr, claim only the verified in-window `v0.2.0` release and pinned functionality.
8. **NIP-34 counts:** issue events prove issue publication, not merged fixes, patches, releases, or adoption.
9. **Zapstore:** `first_run_baseline: 1316`, `new_apps: 0`, and `updates: 0` are initialization semantics. No baseline row may be described as new, updated, or absent this week.

## Final handoff

1. Allocate the single new-project slot to **Napstr** if it survives comparison with the main GREEN list.
2. Keep **RSSNotes** as a compact backup from the tracked-release pool, never as a second Recap/discovery item.
3. Omit all 16 app-discovery rows as weekly shipped news and omit the NIP-34 issue-only aggregate as a standalone item.
4. Preserve all partial-source and baseline caveats; make no completeness or ecosystem-quietness claim from GitHub discovery, NIP-89 discovery, or Zapstore.

**GATE: PASS** — selection decisions are backed by pinned event IDs, canonical repository/release/compare evidence, coverage history, `projects.yml`, and the latest three newsletters; duplicates and unsupported claims are explicitly quarantined.
