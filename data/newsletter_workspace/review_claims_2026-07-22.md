# ClaimCheck review — 2026-07-22 draft

Draft: `content/en/newsletters/2026-07-22-newsletter.md`
Reviewer: ClaimCheck (Stage 7 swarm). Method: `gh pr view` / `gh release view`, `nak req` against wss://relay.primal.net, `curl` of raw NIP spec files, and `data/zapstore_releases/zapstore_2026-07-21.json`.

## (a) PR number + repo + state

| Claim | Evidence | Verdict |
|---|---|---|
| nips#2319 merged, subgroups | gh: MERGED 2026-07-16, "NIP-29: add subgroups spec" | VERIFIED |
| nips#2379 merged 07-15, pinning (kind:9010 + 39005) | gh: MERGED 2026-07-15, "NIP-29: add message pinning (update-pin-list and kind:39005)" | VERIFIED |
| nips#2416 merged 07-17, `a` tags in pin list | gh: MERGED 2026-07-17, "NIP-29: allow a tags in pin list" | VERIFIED |
| nips#2383 merged 07-16, banner tag | gh: MERGED 2026-07-16, "NIP-29: add banner tag to group metadata (kind:39000)" | VERIFIED |
| nips#2380 merged 07-16, invite-code suffix | gh: MERGED 2026-07-16, "NIP-29: invite code suffix for group identifiers" | VERIFIED |
| nips#2413 merged 07-15, kind:10011 favorite follow sets | gh: MERGED 2026-07-15, "add kind:10011, favorite follow sets" | VERIFIED |
| nips#2417 OPEN, renumber to kind:10021 | gh: OPEN, "move favorite follow sets to kind:10021 as that other is already being used" | VERIFIED |
| nips#2375 merged 07-15, NIP-46 silent timeouts | gh: MERGED 2026-07-15, "Avoid nip46 silent timeouts" | VERIFIED |
| nips#2419 OPEN, NIP-47 simplification (frnandu) | gh: OPEN, "NIP-47: simplify core spec and introduce extensions" | VERIFIED |
| nips#2418 OPEN, Trusted Relay Assertions | gh: OPEN, "NIP-XX: Trusted Relay Assertions" | VERIFIED |
| nips#2252 OPEN, NIP-91 AND operator | gh: OPEN, "NIP-91: AND operator for filters" | VERIFIED |
| nips#2303 OPEN, NIP-5D web applets | gh: OPEN, "NIP-5D: nostr web applets" | VERIFIED |
| nostrord#188 merged, NIP-51 mute lists | gh: MERGED 2026-07-10, "feat: mute user (NIP-51 kind:10000) across all platforms" | VERIFIED |
| nostrord#192 merged, wire NIP-29 moderation on all UIs | gh: MERGED 2026-07-13, "fix: wire and surface NIP-29 moderation actions on all UIs" | VERIFIED |
| nostrord#195 merged, consent-gated invites | gh: MERGED 2026-07-17, "Group invites: consent-gated adds, cross-relay detection, and list sync" | VERIFIED |
| amethyst#3650 merged, v1.13.0 pre-release QA | gh: MERGED 2026-07-20, "fix: v1.13.0 pre-release QA — napplet account isolation, Concord authority, and 30 other fixes" | VERIFIED |
| amethyst#3653/#3654 "continuing the same hardening line" | gh: both MERGED 2026-07-21, but titles are "Add infinite-scroll backward pagination for notification history" and "Share a note (link) as a QR code" — neither is QA/hardening | MISMATCH |
| nostream#702 merged, NIP-42 read restriction | gh: MERGED 2026-07-20, "feat(nip42): restrict reads of encrypted kinds to authenticated recipients" | VERIFIED |
| nostream#676 merged, NIP-43 join/leave strategies | gh: MERGED 2026-07-20, "feat(nip43): add join/leave request event strategies" | VERIFIED |

## (b) Release tags

| Claim | Evidence | Verdict |
|---|---|---|
| zapstore/zapstore 1.1.0 | gh: tag 1.1.0, published 2026-07-17 | VERIFIED |
| greenart7c3/Amber v6.3.0 | gh: published 2026-07-20 | VERIFIED |
| nostrord/nostrord v2.3.0 | gh: published 2026-07-17 | VERIFIED |
| barrydeen/wisp v1.2.0 | gh: published 2026-07-20 | VERIFIED |
| hedwig-corp/bitchat-to-sonar v0.1-alpha.11 | gh: prerelease, published 2026-07-18 | VERIFIED |
| mmalmi/nostr-social-graph v2.0.0 | gh: published 2026-07-16 | VERIFIED |
| jmcorgan/fips v0.4.1 | gh: published 2026-07-19 | VERIFIED |
| nostr-pubsub "first tracked releases v0.1.3 through v0.5.2" | gh release list: v0.1.3 (07-14) → 0.5.2 (07-18), 10 releases | VERIFIED |
| fips-ts releases "0.0.24 through 0.0.30" | gh release list: runtime-v0.0.24 (07-15) → 0.0.30 (07-20) | VERIFIED |

## (c) IndieSats pivot note (nak)

Note id 3af5ce9a…9764 fetched from wss://relay.primal.net. Kind 1, created_at 1784548201 = 2026-07-20. Content confirms every draft claim: publisher role retired ("We held keys, managed a whitelist… took a mandatory 2% cut"), relay/player/discovery-layer relaunch, own-profile publishing now the only option, whitelist removed, fees opt-in only, kind 5 self-deletion honored. Note text says "kind 5 event"; draft frames it as "NIP-09 kind:5 deletion requests" — accurate. Date "2026-07-20" matches created_at. VERIFIED.

## (d) NIP spec text (raw.githubusercontent.com/nostr-protocol/nips/master)

| Claim | Evidence | Verdict |
|---|---|---|
| NIP-42 kind 22242, relay+challenge tags, AUTH/OK flow | 42.md lines 41–48 confirm | VERIFIED |
| created_at "within about ten minutes" | 42.md:106 "within ~10 minutes" | VERIFIED |
| `auth-required:` / `restricted:` prefixes | 42.md lines 58–59 | VERIFIED |
| NIP-43 kind 13534 membership list signed by NIP-11 `self` pubkey, `member` tags | 43.md lines 47–52 | VERIFIED |
| kind 8000 add-member, 8001 remove-member | 43.md lines 73, 96 | VERIFIED |
| kind 28934 join request w/ `claim` tag; 28935 ephemeral invite; 28936 leave request | 43.md lines 119, 148, 166 | VERIFIED |
| "Clients must only send… to relays that advertise this NIP in supported_nips" | 43.md:180 (says this for 28934/28935; draft extends it to leave requests — spec literally lists only join/invite kinds) | VERIFIED (minor overgeneralization, not a factual error worth fixing) |
| NIP-29 subgroups: `parent` tag on kind:39000, no membership/admin inheritance, kind:9000/9001 per group, NIP-11 `nip29.subgroups: true` | 29.md lines 287–345 confirm all | VERIFIED |
| kind:9010 `update-pin-list`, kind:39005 group pinned events, `e`+`a` tags, relay may cap pins, display order = tag order | 29.md lines 142, 264–266 | VERIFIED |
| `banner` tag joins name/picture/about in kind:39000 | 29.md lines 164, 174 | VERIFIED |
| invite suffix `naddr1...?invite=<code>`, `code` tag on kind:9021, pairs with kind:9009 create-invite | 29.md lines 25–31, 91, 96, 141 | VERIFIED |
| NIP-51 kind:10011 favorite follow sets, `a` tags → kind:30000; mirror of 10012 relay feeds → kind:30002 | 51.md lines 36–37 | VERIFIED |
| NIP-46 "unknown or unsupported methods MUST be replied with an error" | 46.md:164 verbatim | VERIFIED |
| Zapstore catalog as kind:10067 events | Zapstore 1.1.0 release notes: "App catalog relays as device-signed kind 10067 events" | VERIFIED |
| Draft's NIP-51 Deep-Dive-adjacent claim "NIP-42 ephemeral kind" | 42.md: "ephemeral event not meant to be published or queried" | VERIFIED |

## (e) Zapstore releases JSON (data/zapstore_releases/zapstore_2026-07-21.json)

| Claim | Evidence | Verdict |
|---|---|---|
| IndieSats v1.1.1–v1.1.3 shipped same week | JSON: com.indiesats.app 1.1.1 (07-20 11:09), 1.1.2 (07-21 11:19), 1.1.3 (07-21 13:57); 1.1.2 notes include "Relay: Removed whitelist, open publishing to all" — corroborates pivot | VERIFIED |
| ClipRelay v0.1.2 new app, clipboard sync over Nostr relays | JSON: com.hoppe.cliprelay 0.1.2 (07-21 11:56), new_app: true, summary "Clipboard sync across your devices via Nostr", repo tajava2006/cliprelay | VERIFIED |

## Release-notes spot checks

- Zapstore 1.1.0 body confirms: portable encrypted device key + Amber backup, opt-in background auto-updates, kind 10067 catalog events, NIP-56 reporting, C1 proof verification before install. VERIFIED.
- Amber v6.3.0 body confirms: grouped multi-request approval, Expert List kind 12022 / Expert Pack kind 32022, privacy mode, NIP-65-before-profile fetch. VERIFIED.
- Wisp v1.2.0 body confirms: multi-account switcher, collapsible reply threads, tracking-param stripping, wallet transaction history. VERIFIED.
- Nostrord v2.3.0 body confirms PRs #188/#192/#195 + Tor .onion support (#194). VERIFIED.
- nostr-social-graph v2.0.0 body confirms signed roster ops, three-field bootstrap URI, FIPS identity facets, shared Rust/TS vectors. VERIFIED.
- fips v0.4.1 body confirms antipoison cap, convergence/MTU fixes, CPU cuts. VERIFIED.

## Fix list

1. **Amethyst section (line 74)** — MISMATCH: "with PR #3653 and PR #3654 continuing the same hardening line" is wrong. #3653 is "Add infinite-scroll backward pagination for notification history" and #3654 is "Share a note (link) as a QR code" — feature PRs, not QA hardening. Fix: either drop the two PR references or reword to "with further v1.13.0 prep PRs landing through 07-21".

All other claims verified against primary sources.

GATE: FAIL — 1 mismatch (Amethyst PR #3653/#3654 mischaracterized as QA hardening; they are feature PRs per gh) out of 40+ claims verified via gh/curl/nak
