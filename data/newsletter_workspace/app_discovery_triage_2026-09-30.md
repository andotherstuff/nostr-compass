# App discovery triage — September 30 Compass

Source: [`discovery_2026-09-29.json`](../app_discovery/discovery_2026-09-29.json), generated 2026-09-29 14:38 UTC, covering 2026-09-21 14:00 UTC through September 29. The collector returned **217 candidate records**: 198 GitHub candidates, 20 Zapstore listing candidates, one NIP-89 candidate, with overlaps. It swept 419 tracked owners and labelled 143 owner-sibling candidates. All three source families reported `ok`; the NIP-89 sweep had one relay warning, and 15 Zapstore signatures were rejected before candidacy. These are discovery records, not publication evidence.

**Verdicts:** 4 GREEN (editorially eligible with primary corroboration), 37 MAYBE (hold for a later issue or stronger evidence), 176 SKIP. The scoring axes, in order, are significance, impact, novelty, evidence maturity, and explanatory value, each 0–2. GREEN requires at least 8/10 and no zero. Each number below is the zero-based index in the source `candidates` array; the groups partition all IDs 0–216 exactly once.

## GREEN — primary evidence and score

| ID | Candidate | Score | September evidence and editorial use | Caveat |
| --- | --- | --- | --- | --- |
| 41 | **deed** | **8/10** (2, 2, 1, 2, 1) | [v0.3.2 release](https://github.com/zig-nostr/deed/releases/tag/v0.3.2), published **Sep 24 09:10 UTC**, documents a Zig Nostr CLI with keys, signing, NIP-19/44, relay queries, publishing, local event store, an agent skill and a relay deadline fix. [Source](https://github.com/zig-nostr/deed). Use in Releases if not already covered. | Repo creation Sep 21 13:27 UTC predates the sweep by 32 minutes; the **release** is the in-window milestone. Performance figures are maintainer benchmarks. |
| 44 | **Dossier** | **9/10** (2, 2, 2, 2, 1) | [Source/README](https://github.com/satanrayshe/dossier) and [deployed site](https://satanrayshe.github.io/dossier/) (HTTP 200, last modified Sep 27) support an in-window **Sep 27** launch. Browser-side audit of an npub's public profile, old NIP-04 DM metadata, zaps, timestamps, media EXIF and relay-retained deletions; NIP-07 can sign remedial events. Good New Apps item. | Three commits and no tagged release. Audit coverage depends on relay responses; any privacy exposure score is heuristic and should not be presented as a security finding. |
| 135 | **Opal** | **9/10** (2, 2, 2, 2, 1) | [v0.3.3 release](https://github.com/derekross/opal/releases/tag/v0.3.3), published **Sep 28 14:54 UTC**, and [source](https://github.com/derekross/opal). New Omarchy panel with a NIP-46 remote signer, local keyring-backed secret, signer permission UI and notifications. Use in Releases or New Apps, once. | Developer is a tracked owner but this is a distinct signer product. The release page has sparse notes; feature details come from the repo README. Do not imply a security audit. |
| 209 | **WatchTower** | **8/10** (2, 1, 2, 2, 1) | [Source/README](https://github.com/iqbqioza/watchtower) and [served panel](https://watchtower.nostrfy.org/) (HTTP 200) corroborate a new **Sep 22** NIP-86 relay administration app. Supports relay info and management methods according to its README. Useful with the NIP-86 protocol update. | No tagged release. A page response proves deployment, not successful authenticated administration; use “new panel” rather than claiming production adoption. |

## MAYBE — recognizable Nostr work, insufficient September publication proof

**126 Nymbot — MAYBE after cross-feed reconciliation.** Its September 29 signed listing is later than a signed 1.0.6 listing dated September 19. The in-window 1.0.7 change is on-device file reading, without a distinct Nostr transport or identity milestone. The service and its gift-wrapped messaging are real, but this week’s descriptor does not clear the material Nostr progress and continuity gates.

The following signed listings or served pages have a recognizable product, but lack a verified in-window release, a distinct delta, enough maturity, or evidence beyond developer assertions. They are **not** issue-ready on this sweep:

23 Bookshelf; 47 Echoes; 75 Kairos; 86 Linky; 97 Newlay; 102 Nostr Clips; 117 nostrich-client; 150 PosterChan; 154 PsstPsst; 174 signet-lite; 178 SkateSpots; 181 Staircase; 190 Tenna; 193 The Habit.

Specific cautions: #117 **Nostrich** has a signed listing and live site but is a general client with limited new explanatory value; #174 **My Signet Lite** has a served NIP-46 PWA but only two source commits and overlaps the owner's existing signer; #47 **Echoes** and #75 **Kairos** are siblings from one owner; #190 **Tenna** points to a Nostr-hosted source page without a clear versioned launch. Recheck their own release histories before future inclusion.

The following GitHub discoveries show code or descriptions but no verified released or deployed September milestone, or remain prototypes:

10 arca; 15 bies-code; 30 carnelian; 32 Cinderous; 34 cloudron-nostr-relay-app; 35 cloudron-nostr-vpn-app; 52 flock; 53 flutter-nostr-chat; 54 fold-kit; 60 heartwood-ledger; 64 hivescope-relay; 65 hivescope-relay-web; 68 hubstr-relay; 83 lazarus; 100 nostermentor; 116 nostrhost-apps; 121 NostrXT; 157 quiet-relay; 160 real-open-bidding; 168 sidestr-rs; 177 SIP-dashboard.

#34 and #35 are related Cloudron packages, not independent app launches; #64 and #65 are one HiveScope backend/frontend; #83 **lazarus** should be checked against any Lazarus story already in the issue before reuse. #160 explicitly calls itself a prototype. #129 **obelisk-apps** is a concrete test deployment of Nostr kind 32390 games ([source](https://github.com/obelisk-app/obelisk-apps)), but **Obelisk is already tracked**; fold it into an Obelisk update rather than presenting a new app.

## SKIP — exhaustive grouped IDs

Each row lists every remaining source index once. The grouping is by the first applicable discovery mechanism, not a claim that every project in the group has the same product scope. A first-seen or owner match, by itself, supplies no new September app milestone.

| Group | Count | IDs | Reason |
| --- | ---: | --- | --- |
| Zapstore listing only | 6 | 25, 28, 70, 78, 84, 170 | Signed descriptor or old known app, without independently verified new release; Knit (#78) has no demonstrated Nostr transport. |
| Tracked-owner sibling | 135 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 16, 17, 18, 19, 21, 22, 24, 26, 27, 29, 31, 33, 37, 38, 39, 40, 42, 45, 46, 48, 49, 50, 51, 55, 56, 57, 58, 59, 62, 63, 66, 67, 69, 71, 72, 73, 74, 76, 77, 80, 81, 82, 85, 87, 88, 91, 92, 93, 94, 96, 98, 99, 101, 103, 104, 105, 106, 108, 113, 114, 124, 125, 127, 131, 132, 133, 134, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 153, 155, 156, 158, 159, 161, 163, 164, 166, 169, 171, 172, 173, 175, 176, 182, 183, 184, 186, 187, 188, 189, 191, 192, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 210, 211, 212, 214, 215 | Owner adjacency or minor/recycled repository, with no distinct verified new Nostr app milestone. Includes unrelated non-Nostr repositories. |
| Topic first seen | 11 | 20, 109, 110, 128, 130, 148, 162, 165, 167, 185, 213 | Search discovery date is not a launch date; older projects lack an in-window release/site delta or are Obelisk sibling components. |
| NIP-89 handler | 1 | 43 | One signed handler descriptor (#43) offers no verified released product or independent service behavior. |
| Other new/active source | 23 | 14, 36, 61, 79, 89, 90, 95, 107, 111, 112, 115, 118, 119, 120, 122, 123, 140, 146, 151, 152, 179, 180, 216 | GitHub description/topic or early source only; weak Nostr fit, sparse implementation or no corroborated app launch. |

**Reconciliation:** 4 GREEN + 37 MAYBE + 176 SKIP = 217 unique source IDs. No project registry or newsletter draft was changed by this triage. Before final copy, the editor should ensure the four GREEN items do not duplicate release paragraphs already selected from the primary release sweep. A signed Zapstore descriptor verifies its publisher's event, not the underlying app's claims; source links above provide the corroboration available here.
