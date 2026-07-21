# Topic-page audit — Newsletter #32 (2026-07-22)

Reviewer: TopicAudit (Stage 7 review swarm)
Draft audited: `content/en/newsletters/2026-07-22-newsletter.md` (draft: true)
Run: 2026-07-21

## 1. Topic links found in draft (12 unique slugs, 22 link instances)

| Slug | Instances | Lines |
|---|---|---|
| fips | 1 | 42 |
| nip-09 | 1 | 26 |
| nip-11 | 1 | 120 |
| nip-29 | 5 | 30, 54, 104, 106, 108 |
| nip-42 | 2 | 82, 134 |
| nip-43 | 2 | 82, 157 |
| nip-46 | 3 | 34, 50, 112 |
| nip-47 | 2 | 86, 118 |
| nip-51 | 4 | 30, 38, 54, 110 |
| nip-56 | 1 | 34 |
| nip-65 | 1 | 50 |
| nip-66 | 2 | 94, 120 |

Extraction: `grep -oE '\]\(/en/topics/[a-z0-9-]+/'` on the draft, deduped.

## 2. Per-topic verification

All 12 files exist under `content/en/topics/`. Note: this site's topic pages do not use a `## Primary sources` heading; they use a bold `**Primary sources:**` list block (verified in nip-09.md as canonical example). Judged against that house format:

| Topic file | **Primary sources:** block with links | **Mentioned in:** block exists | Lists Newsletter #32 (2026-07-22)? |
|---|---|---|---|
| fips.md | YES (2 links) | YES (line 37) | NO — needs entry |
| nip-09.md | YES (1 link) | YES | NO — needs entry |
| nip-11.md | YES (6 links) | YES (line 57) | NO — needs entry |
| nip-29.md | YES (9 links) | YES (line 63) | NO — needs entry |
| nip-42.md | YES (1 link) | YES (line 49) | NO — needs entry |
| nip-43.md | YES (2 links) | YES (line 44) | NO — needs entry |
| nip-46.md | YES (1 link) | YES (line 47) | NO — needs entry |
| nip-47.md | YES (3 links) | YES (line 41) | NO — needs entry |
| nip-51.md | YES (1 link) | YES (line 54) | NO — needs entry |
| nip-56.md | YES (1 link) | YES (line 39) | NO — needs entry |
| nip-65.md | YES (1 link) | YES (line 71) | NO — needs entry |
| nip-66.md | YES (2 links) | YES (line 51) | NO — needs entry |

Cross-check: `grep -n '2026-07-22\|Newsletter #32' content/en/topics/{12 files}.md` returned zero hits, as expected pre-publish.

## 3. Missing topic pages (referenced concepts without pages)

None — ERROR count: 0. Every concept linked as `/en/topics/<slug>/` resolves to an existing page. Additional spot check on unlinked concept mentions in the draft:

- `trusted-relay-assertions.md` EXISTS (covered in two draft sections, lines 92–96 and 120) but is never linked from the draft — see fix-list item 13.
- `nip-32.md` EXISTS (mentioned by name on line 120, "reuses NIP-32 labels") but is not linked — see fix-list item 14.
- IndieSats, Nostrord, Zapstore, Amber, Wisp, ClipRelay, Sonar, nostr-pubsub, fips-ts, nostr-social-graph, Iris Stack, nostream: no topic pages, and none warranted — projects/apps with single-release or release-cluster coverage this week, per the rule that a single-release app does not warrant a topic page.

## 4. New topic page warranted this week?

NO. The week's material is: spec PRs on existing NIPs (29, 51, 46, 47, plus draft #2418 which already has trusted-relay-assertions.md), app releases, and the Iris TypeScript library cluster. The Iris Stack is a candidate to watch (three interlocking libraries shipping together), but a topic page requires sustained deep documentation value; one release week does not clear that bar. No new page required.

## 5. Fix-list (assembler applies before publish)

Add one `**Mentioned in:**` entry to each of these 12 topic files, in the house format `- [Newsletter #32: <Section>](/en/newsletters/2026-07-22-newsletter/#<anchor>)`:

1. `content/en/topics/fips.md` — `- [Newsletter #32: News](/en/newsletters/2026-07-22-newsletter/#the-iris-ecosystem-ships-a-pubsub-library-a-browser-fips-runtime-and-a-social-graph-20-in-one-week)`
2. `content/en/topics/nip-09.md` — `- [Newsletter #32: News](/en/newsletters/2026-07-22-newsletter/#indiesats-drops-its-publisher-role-and-relaunches-as-open-nostr-music-infrastructure)`
3. `content/en/topics/nip-11.md` — `- [Newsletter #32: NIP Updates](/en/newsletters/2026-07-22-newsletter/#protocol-work-and-nip-updates)`
4. `content/en/topics/nip-29.md` — `- [Newsletter #32: News](/en/newsletters/2026-07-22-newsletter/#nip-29-relay-groups-get-a-full-spec-week-with-a-shipping-client-landing-the-same-features)`
5. `content/en/topics/nip-42.md` — `- [Newsletter #32: NIP Deep Dive](/en/newsletters/2026-07-22-newsletter/#nip-deep-dive-nip-42-and-nip-43)` (deep-dive section; also referenced in Unreleased/nostream)
6. `content/en/topics/nip-43.md` — `- [Newsletter #32: NIP Deep Dive](/en/newsletters/2026-07-22-newsletter/#nip-deep-dive-nip-42-and-nip-43)` (same deep-dive; also Unreleased/nostream)
7. `content/en/topics/nip-46.md` — `- [Newsletter #32: News](/en/newsletters/2026-07-22-newsletter/#zapstore-110-makes-the-device-key-portable-and-the-app-catalog-relay-native)` (also Amber v6.3.0 in Tagged releases and PR #2375 in NIP updates)
8. `content/en/topics/nip-47.md` — `- [Newsletter #32: Unreleased](/en/newsletters/2026-07-22-newsletter/#open-nip-47-simplification-proposal)` (also NIP updates section)
9. `content/en/topics/nip-51.md` — `- [Newsletter #32: News](/en/newsletters/2026-07-22-newsletter/#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house)` (also Nostrord v2.3.0 in Tagged releases and PR #2413 in NIP updates)
10. `content/en/topics/nip-56.md` — `- [Newsletter #32: News](/en/newsletters/2026-07-22-newsletter/#zapstore-110-makes-the-device-key-portable-and-the-app-catalog-relay-native)`
11. `content/en/topics/nip-65.md` — `- [Newsletter #32: Tagged releases](/en/newsletters/2026-07-22-newsletter/#amber-v630-groups-bunker-signing-approvals-and-adds-expert-list-support)`
12. `content/en/topics/nip-66.md` — `- [Newsletter #32: Unreleased](/en/newsletters/2026-07-22-newsletter/#open-trusted-relay-assertions-draft)` (also NIP updates section)

Optional (not gate-blocking):
13. Link the existing `trusted-relay-assertions.md` page from the draft on first mention ("Open: Trusted Relay Assertions draft", line ~94), then add a Newsletter #32 Mentioned-in entry to that file too. Currently a topic page exists with zero inbound links from the issue that covers it in two sections.
14. Consider linking `nip-32.md` at "reuses NIP-32 labels" (line 120) for consistency with the deep-dive's practice of linking NIPs on first mention.

Anchor slugs in items 5–6 derived from section headings; assembler should verify final Hugo-generated anchors after build.

GATE: PASS (12/12 topic pages verified: all exist with Primary sources blocks carrying 1–9 spec/source links each; 0 missing-page ERRORs; 12 Mentioned-in updates queued for assembler; 2 optional link-consistency suggestions)
