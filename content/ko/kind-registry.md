---
title: Kind 레지스트리
url: /ko/kind-registry/
translationOf: /en/kind-registry.md
translationDate: 2025-12-26
---

이벤트 kind는 Nostr 이벤트를 분류하는 정수입니다. 이 레지스트리는 모든 표준화된 kind와 해당 설명 및 정의 NIP를 나열합니다.

**Kind 범위** ([NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) 참조):
- **0-999**: 일반 이벤트 (모든 버전 유지)
- **1000-9999**: 일반 이벤트 (계속)
- **10000-19999**: 대체 가능 이벤트 (pubkey당 최신 버전만 유지)
- **20000-29999**: 임시 이벤트 (저장되지 않고 전달만 됨)
- **30000-39999**: 주소 지정 가능 이벤트 (pubkey + kind + d-tag당 최신 버전)

## 핵심 이벤트 (0-99)

| Kind | 설명 | NIP |
|------|------|-----|
| 0 | User Metadata | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 1 | Short Text Note | [10](https://github.com/nostr-protocol/nips/blob/master/10.md) |
| 2 | Recommend Relay (deprecated) | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 3 | Follows | [02](https://github.com/nostr-protocol/nips/blob/master/02.md) |
| 4 | Encrypted Direct Messages | [04](https://github.com/nostr-protocol/nips/blob/master/04.md) |
| 5 | Event Deletion Request | [09](https://github.com/nostr-protocol/nips/blob/master/09.md) |
| 6 | Repost | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 7 | Reaction | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 8 | Badge Award | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 9 | Chat Message | [C7](https://github.com/nostr-protocol/nips/blob/master/C7.md) |
| 10 | Group Chat Threaded Reply (deprecated) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 11 | Thread | [7D](https://github.com/nostr-protocol/nips/blob/master/7D.md) |
| 12 | Group Thread Reply (deprecated) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 13 | Seal | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 14 | Direct Message | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 15 | File Message | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 16 | Generic Repost | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 17 | Reaction to a website | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 20 | Picture | [68](https://github.com/nostr-protocol/nips/blob/master/68.md) |
| 21 | Video Event | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 22 | Short-form Portrait Video | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 40 | Channel Creation | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 41 | Channel Metadata | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 42 | Channel Message | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 43 | Channel Hide Message | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 44 | Channel Mute User | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 62 | Request to Vanish | [62](https://github.com/nostr-protocol/nips/blob/master/62.md) |
| 64 | Chess (PGN) | [64](https://github.com/nostr-protocol/nips/blob/master/64.md) |

## MLS 암호화 (443-445)

| Kind | 설명 | NIP |
|------|------|-----|
| 443 | KeyPackage | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 444 | Welcome Message | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 445 | Group Event | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |

## 일반 이벤트 (1000-9999)

| Kind | 설명 | NIP |
|------|------|-----|
| 1018 | Poll Response | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1021 | Bid | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1022 | Bid confirmation | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1040 | OpenTimestamps | [03](https://github.com/nostr-protocol/nips/blob/master/03.md) |
| 1059 | Gift Wrap | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 1063 | File Metadata | [94](https://github.com/nostr-protocol/nips/blob/master/94.md) |
| 1068 | Poll | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1111 | Comment | [22](https://github.com/nostr-protocol/nips/blob/master/22.md) |
| 1222 | Voice Message | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1244 | Voice Message Comment | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1311 | Live Chat Message | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 1337 | Code Snippet | [C0](https://github.com/nostr-protocol/nips/blob/master/C0.md) |
| 1617 | Patches | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1618 | Pull Requests | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1619 | Pull Request Updates | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1621 | Issues | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1984 | Reporting | [56](https://github.com/nostr-protocol/nips/blob/master/56.md) |
| 1985 | Label | [32](https://github.com/nostr-protocol/nips/blob/master/32.md) |
| 2003 | Torrent | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 2004 | Torrent Comment | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 4550 | Community Post Approval | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 5000-5999 | Job Request | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 6000-6999 | Job Result | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7000 | Job Feedback | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7374 | Reserved Cashu Wallet Tokens | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7375 | Cashu Wallet Tokens | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7376 | Cashu Wallet History | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 8000 | Add User | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 8001 | Remove User | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 9000-9030 | Group Control Events | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 9041 | Zap Goal | [75](https://github.com/nostr-protocol/nips/blob/master/75.md) |
| 9321 | Nutzap | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 9734 | Zap Request | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9735 | Zap | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9802 | Highlights | [84](https://github.com/nostr-protocol/nips/blob/master/84.md) |

## 대체 가능 이벤트 (10000-19999)

| Kind | 설명 | NIP |
|------|------|-----|
| 10000 | Mute list | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10001 | Pin list | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10002 | Relay List Metadata | [65](https://github.com/nostr-protocol/nips/blob/master/65.md) |
| 10003 | Bookmark list | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10004 | Communities list | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10005 | Public chats list | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10006 | Blocked relays list | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10007 | Search relays list | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10009 | User groups | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10012 | Favorite relays list | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10013 | Private event relay list | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 10015 | Interests list | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10019 | Nutzap Mint Recommendation | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 10020 | Media follows | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10030 | User emoji list | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10050 | Relay list to receive DMs | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 10051 | KeyPackage Relays List | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 10063 | User server list | Blossom |
| 10166 | Relay Monitor Announcement | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 10312 | Room Presence | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 13194 | Wallet Info | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 13534 | Membership Lists | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 17375 | Cashu Wallet Event | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |

## 인증 및 지갑 (22000-27999)

| Kind | 설명 | NIP |
|------|------|-----|
| 22242 | Client Authentication | [42](https://github.com/nostr-protocol/nips/blob/master/42.md) |
| 23194 | Wallet Request | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 23195 | Wallet Response | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 24133 | Nostr Connect | [46](https://github.com/nostr-protocol/nips/blob/master/46.md) |
| 24242 | Blobs stored on mediaservers | Blossom |
| 27235 | HTTP Auth | [98](https://github.com/nostr-protocol/nips/blob/master/98.md) |

## 접근 제어 (28000-29999)

| Kind | 설명 | NIP |
|------|------|-----|
| 28934 | Join Request | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28935 | Invite Request | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28936 | Leave Request | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |

## 주소 지정 가능 이벤트 (30000-39999)

| Kind | 설명 | NIP |
|------|------|-----|
| 30000 | Follow sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30002 | Relay sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30003 | Bookmark sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30004 | Curation sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30005 | Video sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30007 | Kind mute sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30008 | Profile Badges | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30009 | Badge Definition | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30015 | Interest sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30017 | Create or update a stall | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30018 | Create or update a product | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30019 | Marketplace UI/UX | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30020 | Product sold as an auction | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30023 | Long-form Content | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30024 | Draft Long-form Content | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30030 | Emoji sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30063 | Release artifact sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30078 | Application-specific Data | [78](https://github.com/nostr-protocol/nips/blob/master/78.md) |
| 30166 | Relay Discovery | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 30267 | App curation sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30311 | Live Event | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30312 | Interactive Room | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30313 | Conference Event | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30315 | User Statuses | [38](https://github.com/nostr-protocol/nips/blob/master/38.md) |
| 30402 | Classified Listing | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30403 | Draft Classified Listing | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30617 | Repository announcements | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30618 | Repository state announcements | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30818 | Wiki article | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 30819 | Redirects | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 31234 | Draft Event | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 31922 | Date-Based Calendar Event | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31923 | Time-Based Calendar Event | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31924 | Calendar | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31925 | Calendar Event RSVP | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31989 | Handler recommendation | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 31990 | Handler information | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 34550 | Community Definition | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 38172 | Cashu Mint Announcement | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38173 | Fedimint Announcement | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38383 | Peer-to-peer Order events | [69](https://github.com/nostr-protocol/nips/blob/master/69.md) |
| 39000-39009 | Group metadata events | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 39089 | Starter packs | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39092 | Media starter packs | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39701 | Web bookmarks | [B0](https://github.com/nostr-protocol/nips/blob/master/B0.md) |

*최종 업데이트: 2025년 12월*

공식 소스는 [NIPs 저장소](https://github.com/nostr-protocol/nips)를 참조하세요.
