---
title: 'Nostr Compass #19'
date: 2026-04-22
translationOf: /en/newsletters/2026-04-22-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** [Amethyst](https://github.com/vitorpamplona/amethyst)가 대규모 Marmot, 커뮤니티, MoQ 오디오 룸 작업을 마무리했고, [TollGate](https://github.com/OpenTollGate/tollgate)는 v0.1.0에서 Nostr와 Cashu 위의 종량제 인터넷 접속을 안정화했습니다. [nostream](https://github.com/Cameri/nostream)은 [NIP-45](/ko/topics/nip-45/), [NIP-62](/ko/topics/nip-62/), 압축, query hardening, 완전한 [NIP-11](/ko/topics/nip-11/) parity를 둘러싼 릴레이 작업 한 주를 마무리했습니다. Forgesworn은 Nostr용 signing, identity, paid-API 스택 전체를 공개했습니다. ShockWallet은 Nostr 네이티브 Lightning wallet 흐름을 계속 밀고 있습니다. Formstr 계열(Pollerama, Forms, Calendar)은 보안 강화와 RRULE 지원 전반에 걸쳐 26개의 PR을 병합했습니다. StableKraft, Keep, topaz, WoT Relay, Flotilla, NipLock도 이번 주 배포 목록에 포함됩니다. 심층 분석은 [NIP-72 moderated communities](/ko/topics/nip-72/)와 [NIP-57 zaps](/ko/topics/nip-57/)를 다룹니다.

## Top Stories

### Amethyst ships Marmot MIP compliance, NIP-72 communities, zap goals, and MoQ audio rooms

vitorpamplona가 유지 관리하는 Android 클라이언트 [Amethyst](https://github.com/vitorpamplona/amethyst)는 이번 주 57개의 PR을 병합했습니다. 이번 주 핵심 주제는 [Marmot](/ko/topics/marmot/) 암호화 그룹 준수, 1급 moderated community 지원, 라이브 스트림 zap goal, 그리고 Media over QUIC 기반의 새로운 audio room 스택입니다.

Marmot 준수 측면에서 [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462)는 내장 [MDK](https://github.com/marmot-protocol/mdk) 구현을 MIP-01 및 MIP-05 wire format과 맞추며, TLS 스타일 길이 prefix의 VarInt 인코딩과 MDK test vector에 대한 round-trip 검증을 추가합니다. [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435)는 MIP-00 KeyPackage Relay List 지원을 추가해 invitee가 자신의 KeyPackage를 어느 릴레이가 제공하는지 광고할 수 있게 하고, [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436)은 [White Noise](https://github.com/marmot-protocol/whitenoise)와의 교차 클라이언트 테스트에서 드러난 admin-gate 및 media 처리 공백을 닫았습니다. 같은 날 [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466)은 암호화된 welcome이 [mdk-core](https://github.com/marmot-protocol/mdk)가 만드는 바이트와 동일하게 직렬화되도록 MLS commit framing을 고쳤고, [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471)은 Marmot 공동 관리자 사이에서 상태 분기를 일으키던 outer-layer 복호화 버그를 해결했습니다. [PR #2477](https://github.com/vitorpamplona/amethyst/pull/2477)과 [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493)의 두 번째 준수 패스는 추가 commit 경로와 메시지 암호화 공백을 닫고, 서명, key schedule, welcome-message derivation을 참조 vector와 대조하는 완전한 MLS commit cryptography validator를 추가합니다.

프로토콜 작업과 함께 [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488)은 `amy`를 배포합니다. 이는 Amethyst 구현을 기반으로 Marmot와 MLS 그룹 작업을 수행하는 command-line tool입니다. Amy는 통합자에게 그룹 생성, KeyPackage 생성, welcome 시뮬레이션, 실제 Amethyst signer와의 commit 검증을 스크립트 방식으로 수행할 수 있게 해 주며, 이는 오늘날 cross-client Marmot interop에서 가장 큰 디버깅 공백을 메웁니다.

[PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468)은 1급 [NIP-72](/ko/topics/nip-72/) 커뮤니티 생성 및 관리 기능을 추가합니다. 사용자는 kind `34550` 커뮤니티 정의를 작성하고, moderator와 relay hint를 추가하고, 커뮤니티를 가리키는 `a` 태그가 포함된 게시물을 제출하고, kind `4549` approval 이벤트를 통해 대기 중인 승인을 관리할 수 있습니다. 이 기능은 community moderation 측면에서 Amethyst와 [noStrudel](https://github.com/hzrd149/nostrudel) 사이의 오랜 격차를 메웁니다. [PR #2458](https://github.com/vitorpamplona/amethyst/pull/2458)과 [PR #2473](https://github.com/vitorpamplona/amethyst/pull/2473)은 emoji set 지원과 완전한 [NIP-30](https://github.com/nostr-protocol/nips/blob/master/30.md) emoji-pack 관리 UI를 추가해 사용자가 자신의 custom emoji 라이브러리를 구성할 수 있게 합니다.

[PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469)는 [NIP-75](/ko/topics/nip-75/) zap goal을 [NIP-53](/ko/topics/nip-53/) Live Activities 화면에 연결합니다. 이제 각 라이브 스트림에는 progress bar, 원탭 zap 버튼, top-zappers 리더보드가 있는 fundraising goal 헤더가 붙습니다. 이 리더보드는 스트림의 kind `30311` 이벤트에 연결된 kind `9735` zap receipt를 읽고 goal의 `amount` 목표와 대조해 집계합니다. [PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486)은 전용 Live Streams 피드 화면을 추가하고, [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491)은 NIP-53 proof-of-agreement와 event-builder helper를 넣으며, [PR #2461](https://github.com/vitorpamplona/amethyst/pull/2461)은 피드 내 최저 해상도 HLS, picture-in-picture 재생, 전체 화면 자동 해상도 선택을 추가합니다.

가장 야심찬 새 표면은 실시간 오디오입니다. [PR #2494](https://github.com/vitorpamplona/amethyst/pull/2494)는 [Media over QUIC](https://datatracker.ietf.org/group/moq/about/) transport client와 audio room 지원을 추가합니다. QUIC 위의 pub-sub 모델을 가진 MoQ는, 클라이언트가 특정 track과 priority를 subscribe하고 congestion 처리를 transport에 맡길 수 있기 때문에 WebSocket relay보다 라이브 오디오에 더 잘 맞습니다. [PR #2487](https://github.com/vitorpamplona/amethyst/pull/2487)의 새 Public Chats 화면과 합쳐 보면, Amethyst는 이제 Marmot 암호화 메시징 옆에 놓이는 공개 audio room용 end-to-end 표면을 갖추게 되었습니다.

탐색과 신뢰성 측면에서는 [PR #2485](https://github.com/vitorpamplona/amethyst/pull/2485)와 [PR #2490](https://github.com/vitorpamplona/amethyst/pull/2490)이 Follow Pack 탐색 피드를 추가하고 curated follow set을 기본 onboarding preference에 연결해, 새 사용자가 첫 실행부터 내용이 있는 타임라인을 보게 합니다. [PR #1983](https://github.com/vitorpamplona/amethyst/pull/1983)는 실시간 relay 연결을 위한 상시 notification service를 도입해 Marmot DM과 mention이 앱이 foreground가 아니어도 도착하게 하고, [PR #2480](https://github.com/vitorpamplona/amethyst/pull/2480)은 adaptive cache sizing이 포함된 on-demand HLS video caching을 추가합니다.

### TollGate v0.1.0 stabilizes pay-per-use internet over Nostr and Cashu

[TollGate](https://github.com/OpenTollGate/tollgate)는 4월 21일 [v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)를 발표했습니다. 이는 종량제 네트워크 접속용 명세 세트의 첫 태그 스냅샷입니다. 이 프로토콜은 WiFi router, Ethernet switch, Bluetooth tether처럼 연결을 제어할 수 있는 장치가 가격을 광고하고, [Cashu](/ko/topics/cashu/) ecash token을 받고, 계정이나 구독 대신 선불 local token으로 세션을 관리할 수 있게 합니다. local Cashu wallet에 몇 sats만 있는 고객도 네트워크의 호환 TollGate 어디에서나 다음 1분 또는 다음 megabyte의 접속을 살 수 있습니다.

이번 릴리스는 아키텍처의 세 계층을 고정합니다. [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)에서 정의된 프로토콜 계층은 세 가지 기본 이벤트 형식(Advertisement, Session, Notice)을 규정하고, [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)는 그 위에 Cashu 결제를 얹어 고객이 gate가 광고한 임의의 mint에서 token을 상환할 수 있게 합니다. 그 위의 인터페이스 계층에서는 [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md)부터 HTTP-03까지가 제한적인 운영체제용 plain-HTTP 표면을 정의하고, [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)은 WebSocket을 열 수 있는 클라이언트용 Nostr-relay transport를 정의합니다. 마지막으로 [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)은 결제 고객을 위한 captive-portal routing을 설명하는 medium 계층을 다룹니다.

결제 자산이 credential이 아니라 bearer token이기 때문에, 고객은 이를 만들기 위해 사전 인터넷 접속이 필요하지 않습니다. 로컬 wallet 안의 Cashu token만으로 첫 1분의 연결을 살 수 있고, 그 뒤 더 많은 token으로 충전할 수 있습니다. Gate끼리 서로 uplink를 살 수도 있으므로, 도달 범위는 단일 운영자를 넘어 확장됩니다. 새 [TollGate topic page](/ko/topics/tollgate/)가 전체 계층 구조를 정리합니다.

### nostream merges 53 PRs for NIP-45, NIP-62, compression, and query hardening

[nostream](https://github.com/Cameri/nostream)는 Cameri의 TypeScript relay 구현으로, 이번 주 새로운 NIP 지원, query 성능, 보안 hardening, 운영 다듬기를 포함해 53개의 PR을 병합했습니다.

기능 작업으로는 [PR #522](https://github.com/Cameri/nostream/pull/522)가 [NIP-45](/ko/topics/nip-45/) `COUNT` 지원을 추가해 클라이언트가 이벤트를 받지 않고도 필터 일치 수를 물을 수 있게 했고, [PR #544](https://github.com/Cameri/nostream/pull/544)는 광고 기능 목록에 [NIP-62](/ko/topics/nip-62/) right-to-vanish를 추가했습니다. [PR #548](https://github.com/Cameri/nostream/pull/548)은 최근 태그 대소문자 규약에 맞춰 uppercase 태그 필터(`#A`부터 `#Z`)도 받을 수 있도록 필터 스키마를 확장했고, [PR #514](https://github.com/Cameri/nostream/pull/514)는 이벤트 import/export에 gzip과 xz 압축을 추가해 운영자가 별도 도구 없이도 대형 이벤트 덤프를 노드 간 이동할 수 있게 했습니다.

query 성능과 정확도 측면에서는 [PR #534](https://github.com/Cameri/nostream/pull/534)가 benchmarking harness와 filter-to-SQL 변환 최적화를 도입했고, [PR #524](https://github.com/Cameri/nostream/pull/524)는 prefix matching 대신 exact-match 검사로 바꾸어 whitelist/blacklist pubkey 매칭 버그를 수정했으며, [PR #553](https://github.com/Cameri/nostream/pull/553)은 `upsertMany`에 결정적 tie-breaker를 추가해 `created_at` timestamp가 같은 concurrent insert가 더 이상 경합하지 않게 했고, [PR #493](https://github.com/Cameri/nostream/pull/493)은 설정된 trusted proxy에서만 `X-Forwarded-For`를 신뢰하도록 제한했습니다. [PR #557](https://github.com/Cameri/nostream/pull/557)은 retention limit, authentication hint, 줄어든 optional field set을 포함한 모든 광고 필드를 현재 명세와 맞추며 relay를 완전한 [NIP-11](/ko/topics/nip-11/) parity 상태로 끌어올렸습니다.

## Shipping This Week

### Primal Android ships Explore tab, NIP-05 verification, and audio player

[Primal Android](https://github.com/PrimalHQ/primal-android-app)는 지난주 피드 재설계 위에 11개의 PR을 추가로 병합했습니다. [PR #1021](https://github.com/PrimalHQ/primal-android-app/pull/1021)은 인기 사용자, follow pack, curated feed 중심의 새 Explore 탭을 도입하고, [PR #1015](https://github.com/PrimalHQ/primal-android-app/pull/1015)는 Primal의 Advanced Search DSL을 미리 채워 넣는 feed editor를 추가합니다. [PR #994](https://github.com/PrimalHQ/primal-android-app/pull/994)는 프로필용 [NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md) verification UI를 제공하고, [PR #997](https://github.com/PrimalHQ/primal-android-app/pull/997)는 피드 안에서 바로 오디오 첨부를 재생하는 in-feed audio player를 넣습니다. [PR #1018](https://github.com/PrimalHQ/primal-android-app/pull/1018)은 wallet QR scanner 경로를 재사용해 signer pairing과 wallet linking을 모두 처리하는 [NIP-46](/ko/topics/nip-46/) nostr-connect pairing을 추가합니다.

### strfry adds Prometheus write-path metrics and fixes NIP-42 AUTH envelope

[strfry](https://github.com/hoytech/strfry)는 운영자 관점의 개선 묶음을 배포했습니다. [PR #194](https://github.com/hoytech/strfry/pull/194)는 전용 Prometheus write-path metrics exporter와 새 connection gauge를 추가하고, [PR #197](https://github.com/hoytech/strfry/pull/197)은 대역폭 추적용으로 연결별 업/다운 바이트와 압축 비율을 기록합니다. [PR #192](https://github.com/hoytech/strfry/pull/192)는 하드코딩된 filter tag limit를 런타임 설정 옵션으로 승격해 재컴파일 없이 조정할 수 있게 합니다. 프로토콜 정확성 측면에서는 [PR #201](https://github.com/hoytech/strfry/pull/201)이 [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) AUTH 실패 응답을 `NOTICE` 메시지에서, NIP가 실제로 요구하는 `OK` envelope로 바꿨습니다. 이는 auth-gated relay에서 오래된 interop 문제였습니다.

### Shopstr hardens storefront security across 13 PRs

[Shopstr](https://github.com/shopstr-eng/shopstr)는 Nostr marketplace 클라이언트로, 이번 주 13개의 PR 대부분이 보안 수정이었습니다. [PR #434](https://github.com/shopstr-eng/shopstr/pull/434)는 판매자가 방문자 브라우저에서 스크립트를 실행할 수 있게 하던 storefront link의 stored-JavaScript 취약점을 막고, [PR #417](https://github.com/shopstr-eng/shopstr/pull/417)은 reflected XSS를 막기 위해 storefront policy HTML 렌더링을 escape하며, [PR #418](https://github.com/shopstr-eng/shopstr/pull/418)은 인증 없이 cached event를 삭제할 수 있던 API를 닫아 교차 사용자 데이터 삭제를 막습니다. [PR #433](https://github.com/shopstr-eng/shopstr/pull/433)은 cached message 읽기에 인증을 요구하고, [PR #419](https://github.com/shopstr-eng/shopstr/pull/419)는 proper auth 뒤에 storefront mutation과 event-cache endpoint를 보호하며, [PR #435](https://github.com/shopstr-eng/shopstr/pull/435)와 [PR #414](https://github.com/shopstr-eng/shopstr/pull/414)는 code scanning에서 발견된 두 개의 SSRF 문제를 고칩니다. 기능 버그로는 [PR #421](https://github.com/shopstr-eng/shopstr/pull/421)이 failed-relay-publish queue의 replay 문제를 해결하고, [PR #425](https://github.com/shopstr-eng/shopstr/pull/425)는 wallet-events fetch를 수리하며, [PR #392](https://github.com/shopstr-eng/shopstr/pull/392)는 checkout 전에 저장된 cart discount를 다시 검증합니다.

### Nostria v3.1.26 through v3.1.28 add background music playback on Android

[Nostria](https://github.com/nostria-app/nostria)는 이번 주 [v3.1.22](https://github.com/nostria-app/nostria/releases/tag/v3.1.22)부터 [v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28)까지 여섯 개의 릴리스를 배포했습니다. 핵심 변화는 [v3.1.26](https://github.com/nostria-app/nostria/releases/tag/v3.1.26)의 Android background music playback입니다. 앱은 오디오가 재생되는 동안 살아 있으며, notification bar와 lock screen에서 media control을 제공합니다. 뒤이은 [v3.1.27](https://github.com/nostria-app/nostria/releases/tag/v3.1.27)과 [v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28)은 이 새 media-service 표면을 더 단단하게 만들었습니다. [뉴스레터 #18](/en/newsletters/2026-04-15-newsletter/)은 직전의 local-image-generation 릴리스(v3.1.19부터 v3.1.21)를 다뤘습니다.

### Wisp v0.18.0-beta adds Normie Mode, For You feed, and NIP-29 group config

[Wisp](https://github.com/barrydeen/wisp)는 Amethyst에서 갈라져 나온 Android 클라이언트로, 4월 16일 [v0.18.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.18.0-beta)를 배포했습니다. 이 릴리스는 Bitcoin 네이티브 맥락 밖에서 들어오는 사용자를 겨냥합니다. [PR #462](https://github.com/barrydeen/wisp/pull/462)는 앱 전반에 fiat 표시 금액을 보여 주는 Normie Mode를 추가하고, [PR #464](https://github.com/barrydeen/wisp/pull/464)는 topic picker와 첫 게시물 가이드를 포함한 onboarding overhaul을 수행합니다. [PR #469](https://github.com/barrydeen/wisp/pull/469)는 extended follows, trending event, followed hashtag를 혼합하는 For You 피드를 추가합니다.

프로토콜 작업으로는 [PR #471](https://github.com/barrydeen/wisp/pull/471)이 flags, invites, roles, AUTH prompt를 위한 [NIP-29](/ko/topics/nip-29/) 그룹 설정을 추가하고, [PR #478](https://github.com/barrydeen/wisp/pull/478)은 [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) AUTH가 끝나기 전에 그룹 `9021`, `9007`, `9009` 이벤트를 보내지 않도록 순서 버그를 고치며 admin 측 실패도 표시합니다. [PR #481](https://github.com/barrydeen/wisp/pull/481)은 mention된 pubkey의 [NIP-65](/ko/topics/nip-65/) inbox relay로 노트를 방송해, 발신자와 수신자의 relay 집합이 겹치지 않아도 답글이 도달하게 합니다.

### NoorNote v0.8.4 adds Scheduled Posts and live stream zapping

[NoorNote](https://github.com/77elements/noornote)는 [v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4)와 [v0.8.5](https://github.com/77elements/noornote/releases/tag/v0.8.5)를 배포했습니다. v0.8.4의 핵심 기능은 Scheduled Posts add-on입니다. 앱은 완전히 서명된 이벤트를 NoorNote가 운영하는 릴레이에 넘기고, 릴레이가 지정 시각에 이를 게시하므로 개인 키는 장치를 떠나지 않습니다. 같은 릴리스는 라이브 스트림 카드에서 한 번 탭하는 것만으로 zap을 보낼 수 있게 했고, 보낸 sats는 [NIP-53](/ko/topics/nip-53/)을 통해 스트림의 chat overlay에 나타납니다. 또한 fiat-rate API가 잠시 불안정할 때도 wallet balance를 계속 표시합니다. v0.8.5는 긴 Android 스크롤에서 중복 게시물을 만들던 timeline deduplication 버그를 수정합니다.

### topaz v0.0.2 ships a Nostr relay for Android

[topaz](https://github.com/fiatjaf/topaz)는 [fiatjaf](https://github.com/fiatjaf)가 만든 Android 휴대폰용 Nostr relay로, 2026-04-17에 [v0.0.2](https://github.com/fiatjaf/topaz/releases/tag/v0.0.2)를 배포했습니다. 이 프로젝트는 Kotlin-first이며, 휴대폰을 항상 켜져 있는 개인 relay로 위치시킵니다. 현재 범위는 좁습니다. 설치 가능한 Android 패키지 안에서 동작하는 relay라는 점 자체가 핵심입니다.

### StableKraft v1.0.0 ships the first stable music-and-podcast PWA release

[StableKraft](https://github.com/ChadFarrow/stablekraft-app)는 podcast 피드에서 가져온 음악을 발견하고 정리하고 스트리밍하는 Next.js PWA로, auth와 social 기능에는 Nostr를, V4V 결제에는 Lightning을 사용합니다. 2026-04-18에 [v1.0.0](https://github.com/ChadFarrow/stablekraft-app/releases/tag/v1.0.0)에 도달했습니다. 같은 주에는 [15분 OPML cache와 잘못된 XML 제거](https://github.com/ChadFarrow/stablekraft-app/commit/7ac90f6)로 feed ingestion을 강화했고, [후속 수정](https://github.com/ChadFarrow/stablekraft-app/commit/fbf337b)에서 nightly reparse window를 720시간에서 24시간으로 줄여 새로 추가된 feed가 더 빨리 스스로 복구되도록 했습니다.

### NipLock ships a NIP-17-based password manager

[NipLock](https://gitworkshop.dev/npub1z5jf78uhd68znuwwwu926th55rzd0wy8nd9clkr03cx22mwme0jqazk56h/relay.ngit.dev/passwd)는 [NIP-17](/ko/topics/nip-17/) gift-wrapped direct message를 사용해 장치 간 자격 증명을 저장하고 동기화하는 password manager입니다. 각 password entry는 사용자 키에서 자기 자신으로 보내는 NIP-17 DM이므로, 같은 키로 인증한 모든 장치에 같은 이벤트가 복제됩니다. 서명은 raw `nsec`, [nos2x](https://github.com/fiatjaf/nos2x) 같은 browser extension, 또는 [NIP-46](/ko/topics/nip-46/)를 통한 [Amber](https://github.com/greenart7c3/Amber)로 할 수 있어 master key를 클라이언트 장치 밖에 둘 수 있습니다.

### flotilla-budabit polishes its NIP-34 repo surface

Budabit 커뮤니티의 [Flotilla](https://gitea.coracle.social/coracle/flotilla) fork인 [flotilla-budabit](https://github.com/Pleb5/flotilla-budabit)는 NIP-34 git-over-nostr 워크플로를 다듬는 수정 묶음을 배포했습니다. 이번 주 업데이트는 [repo discussion control 복원](https://github.com/Pleb5/flotilla-budabit/commit/a6fb67e), [detail page에서 sticky repo tab 유지](https://github.com/Pleb5/flotilla-budabit/commit/e2b891a), [저장된 GRASP relay에서 repo announcement 불러오기](https://github.com/Pleb5/flotilla-budabit/commit/43d5e9e), [maintainer가 적용한 patch 상태 동기화 유지](https://github.com/Pleb5/flotilla-budabit/commit/2dbb9f0)를 포함합니다. upstream Flotilla와 가깝게 움직이면서도, 이 fork는 Budabit 기여자를 위한 repo view를 우선합니다.

### rx-nostr 3.7.2 through 3.7.4 add default verifier and optional constructor args

[rx-nostr](https://github.com/penpenpng/rx-nostr)는 RxJS 기반 Nostr 라이브러리로, [3.7.2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.2), [3.7.3](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.3), [3.7.4](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.4)를 배포했습니다. [PR #192](https://github.com/penpenpng/rx-nostr/pull/192)는 기본 Schnorr signature verifier를 추가해 호출자가 이를 수동으로 연결할 필요를 없앴고, 짝을 이루는 [crypto@3.1.6](https://github.com/penpenpng/rx-nostr/releases/tag/crypto%403.1.6)은 `@noble/curves` 사용 버그를 바로잡아 가짜 검증 실패를 제거했습니다. [PR #195](https://github.com/penpenpng/rx-nostr/pull/195)는 3.7.4에서 `createRxNostr()` 인수를 optional로 만들어, 빠른 통합에서는 zero configuration으로 라이브러리를 만들 수 있게 합니다.

### Keep Android v1.0.0 ships with reproducible builds and zero trackers

[Keep](https://github.com/privkeyio/keep-android)는 Nostr 네이티브 password 및 secret manager로, hardening PR 연속 이후 4월 21일 [v1.0.0](https://github.com/privkeyio/keep-android/releases/tag/v1.0.0)을 배포했습니다. [PR #241](https://github.com/privkeyio/keep-android/pull/241)은 고정되고 검증된 toolchain을 사용하는 reproducible build recipe를 추가하고, [PR #248](https://github.com/privkeyio/keep-android/pull/248)은 Google Play Services 의존성을 없애기 위해 Google ML Kit를 ZXing으로 교체하며, [PR #252](https://github.com/privkeyio/keep-android/pull/252)는 [Exodus Privacy scan](https://reports.exodus-privacy.eu.org/en/)를 공개해 v1.0.0 빌드에 tracker가 0개임을 보여 줍니다. [PR #256](https://github.com/privkeyio/keep-android/pull/256)은 [zapstore](https://zapstore.dev)를 통한 배포를 위해 `zapstore.yaml` manifest를 추가합니다.

### Flotilla 1.7.3 and 1.7.4 add kind-9 wrapping for richer NIP-29 rooms

[Flotilla](https://gitea.coracle.social/coracle/flotilla)는 hodlbod의 [NIP-29](/ko/topics/nip-29/) groups 클라이언트로, [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3)과 [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)를 배포했습니다. 핵심 프로토콜 변화는 [hodlbod의 release note](nostr:nevent1qvzqqqqqqypzp978pfzrv6n9xhq5tvenl9e74pklmskh4xw6vxxyp3j8qkke3cezqyvhwumn8ghj76rzwghxxmmjv93kcefwwdhkx6tpdshszrnhwden5te0dehhxtnvdakz7qgawaehxw309a5x7ervvfhkgtnrdaexzcmvv5h8xmmrd9skctcqyrrclae7mhmm5dnumwfzhg3fxu74a4hh24jd8pvn8v0hye9w3g6tuljtr85)에 공지되고 [NIP PR #2310](https://github.com/nostr-protocol/nips/pull/2310)과 연계된, 비채팅 콘텐츠 타입의 kind-9 wrapping입니다. 캘린더 이벤트, poll, 기타 비채팅 payload를 kind `9` 안에 감싸 그룹에 보내면, 클라이언트는 포함된 객체를 렌더링하면서도 그것이 어느 room에서 왔는지 문맥을 유지할 수 있습니다.

같은 릴리스 계열은 poll, [NIP-46](/ko/topics/nip-46/) 로그인용 Aegis URL scheme, space invite를 위한 native share, room mention, 모바일 clipboard 이미지 붙여넣기, draft, 통화 중 video, feed pagination 개선도 추가합니다. 이는 [voice room과 email login](/en/newsletters/2026-04-01-newsletter/)으로 다뤘던 [1.7.0과 1.7.1](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.0) 이후 첫 Flotilla 릴리스입니다.

### WoT Relay v0.2.1 migrates eventstore to LMDB

[WoT Relay](https://github.com/bitvora/wot-relay)는 bitvora의 web-of-trust filtered relay로, 2026-04-22에 [v0.2.1](https://github.com/bitvora/wot-relay/releases/tag/v0.2.1)을 배포했습니다. [PR #97](https://github.com/bitvora/wot-relay/pull/97)은 eventstore를 [LMDB](http://www.lmdb.tech/)로 옮기고 WoT bootstrap fetch를 재조정해 relay가 upstream read budget을 소진하지 않고 초기 trust graph를 만들게 했으며, [PR #99](https://github.com/bitvora/wot-relay/pull/99)는 대응하는 보안 수정을 위해 `golang.org/x/crypto`를 v0.45.0으로 올렸습니다. [PR #100](https://github.com/bitvora/wot-relay/pull/100)은 릴리스에 맞춰 광고되는 [NIP-11](/ko/topics/nip-11/) software URL과 version string을 갱신합니다.

### Formstr suite: Pollerama security pass, Forms i18n, Calendar RRULE support

Formstr 계열은 이번 주 Pollerama, Formstr forms, Nostr Calendar 전반에 걸쳐 26개의 PR을 병합했습니다. 투표 앱 쪽에는 보안 테마가 강했고, 나머지 제품에는 기능 작업이 들어갔습니다.

[Pollerama](https://pollerama.fun)는 [nostr-polls](https://github.com/formstr-hq/nostr-polls) 기반 Nostr poll 생성 및 투표 앱으로, 키 처리 방식을 강화했습니다. [PR #182](https://github.com/formstr-hq/nostr-polls/pull/182)는 로그아웃 시 캐시된 direct message를 만료시켜 공유 기기에서 이전 사용자 상태가 남지 않게 했고, [PR #175](https://github.com/formstr-hq/nostr-polls/pull/175)는 로컬 키를 안전한 browser storage로 옮겼으며, [PR #171](https://github.com/formstr-hq/nostr-polls/pull/171)은 모든 login 경로에서 kind `0` profile content에 대한 `JSON.parse`를 방어해 잘못된 프로필이 세션을 깨지 못하게 했습니다. 제품 측면에서는 [PR #186](https://github.com/formstr-hq/nostr-polls/pull/186)이 `pollerama.fun`용 HTTPS deep linking을 연결해 공유된 poll URL이 앱을 직접 열게 했고, [PR #169](https://github.com/formstr-hq/nostr-polls/pull/169)은 poll 결과에서 작성자 이름을 클릭 가능하게 만들었습니다.

[Formstr](https://formstr.app)는 [nostr-forms](https://github.com/formstr-hq/nostr-forms) 기반 Nostr 네이티브 form 제품군으로, 입력 방식과 onboarding 표면을 넓혔습니다. [PR #475](https://github.com/formstr-hq/nostr-forms/pull/475)는 audio와 video URL 지원을 추가해 form 안에 미디어를 직접 임베드할 수 있게 했고, [PR #439](https://github.com/formstr-hq/nostr-forms/pull/439)는 웹 앱에 i18n을 도입했으며, [PR #466](https://github.com/formstr-hq/nostr-forms/pull/466)은 기존 제작자가 설문을 다시 만들지 않고도 이전할 수 있도록 Google Forms onboarding importer를 추가했습니다. [PR #463](https://github.com/formstr-hq/nostr-forms/pull/463)은 browser console에서 민감한 키 로그를 제거해 privacy leak를 막았습니다.

[Nostr Calendar by Formstr](https://calendar.formstr.app)는 같은 날 [v1.3.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.3.0)과 [v1.4.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.4.0)을 배포했고, 핵심은 제대로 된 recurrence-rule 표면입니다. [PR #107](https://github.com/formstr-hq/nostr-calendar/pull/107)은 multiple 및 custom RRULE 지원을 추가해 이벤트가 단일 cadence를 넘어 복잡한 일정으로 반복되게 하고, [PR #101](https://github.com/formstr-hq/nostr-calendar/pull/101)은 floating RRULE date를 RFC 5545에 맞춰 UTC로 해석해 timezone 간 event-time drift를 일으키던 오래된 버그를 고칩니다. [PR #97](https://github.com/formstr-hq/nostr-calendar/pull/97)은 공유 이벤트를 자신의 캘린더에 추가할 수 있게 하고, [PR #86](https://github.com/formstr-hq/nostr-calendar/pull/86)은 list 단위 notification preference를 도입하며, [PR #112](https://github.com/formstr-hq/nostr-calendar/pull/112)은 v1.4.0에 들어간 재작업된 login/loading 경로를 배포합니다. 세 프로젝트 모두 [NIP-52](/ko/topics/nip-52/) calendar event 위에 구축되며 공통 login stack을 공유합니다.

### Also shipped: notedeck, nostr.blue, cliprelay, Captain's Log

몇몇 클라이언트도 큰 headline 기능 없이 반복적 릴리스를 내놓았습니다. Damus의 Rust 데스크톱 및 모바일 클라이언트 [notedeck](https://github.com/damus-io/notedeck)는 [v0.10.0-beta.4](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.4)를 배포하며 column rendering과 relay pool 버그를 고쳤습니다. Dioxus 기반 Rust 클라이언트 [nostr.blue v0.8.6](https://github.com/patrickulrich/nostr.blue/releases/tag/v0.8.6)은 [Dioxus 0.7.5](https://github.com/patrickulrich/nostr.blue/commit/d90b4ff)를 끌어왔고, 네이티브 오디오 bridge를 `manganis::ffi` plugin으로 [변환](https://github.com/patrickulrich/nostr.blue/commit/4207f0c)해 Android 빌드를 다시 가능하게 했습니다. Nostr를 통해 장치 간 clipboard를 동기화하는 [cliprelay](https://github.com/tajava2006/cliprelay)는 [Desktop v0.0.3](https://github.com/tajava2006/cliprelay/releases/tag/desktop%2Fv0.0.3)과 [Android v0.0.4](https://github.com/tajava2006/cliprelay/releases/tag/android%2Fv0.0.4)를 배포하며 sync loop를 다듬고 32-bit Android variant를 제거했습니다. [Captain's Log](https://github.com/nodetec/comet)는 dropped socket을 사용자 개입 없이 교체하는 sync-relay [liveness detection](https://github.com/nodetec/comet/releases/tag/alpha-95f47bd)을 포함한 세 개의 alpha build를 배포했습니다.

## In Development

### whitenoise-rs refactors to session-scoped account views

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)는 [Marmot](/ko/topics/marmot/) 클라이언트 아래에서 동작하는 Rust daemon으로, 전역 singleton에서 계정별 `AccountSession` 뷰로 바꾸는 다단계 리팩터링을 진전시키는 15개의 PR을 병합했습니다. 목표는 하나의 공유 모놀리스를, 부작용이 daemon 전체에 새어나가지 않고 더 쉽게 추론하고 테스트하고 진화시킬 수 있는 계정별 표면으로 쪼개는 것입니다.

기반은 [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743)의 `AccountSession`과 `AccountManager` scaffolding에서 시작됐고, 이어서 [PR #753](https://github.com/marmot-protocol/whitenoise-rs/pull/753)에서 scoped relay handle이 추가됐습니다. 그 뒤 단계들은 [PR #760부터 #769까지](https://github.com/marmot-protocol/whitenoise-rs/pulls?q=is%3Apr+is%3Amerged+768+OR+763+OR+766)에서 draft와 settings, message ops, 그룹 읽기와 쓰기, membership, push notification, key-package 읽기, 그룹 생성을 모두 session 소유 표면으로 옮겼습니다. 마지막으로 [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770)은 이벤트 dispatch를 session에 재배치해 각 계정이 공유 dispatcher 경합 없이 자기 relay 트래픽만 소비하게 했습니다.

### White Noise app adds block/unblock UI, leave-group, and offline notices

[White Noise](https://github.com/marmot-protocol/whitenoise)는 [Marmot](/ko/topics/marmot/) 클라이언트로, 빠져 있던 group lifecycle control을 추가했습니다. [PR #578](https://github.com/marmot-protocol/whitenoise/pull/578)은 [PR #573](https://github.com/marmot-protocol/whitenoise/pull/573)의 block hook 위에 block/unblock UI를 올렸고, [PR #571](https://github.com/marmot-protocol/whitenoise/pull/571)과 [PR #572](https://github.com/marmot-protocol/whitenoise/pull/572)는 Rust 쪽 `clear_chat`, `delete_chat`, `leave_and_delete_group`를 앱에 연결했습니다. [PR #569](https://github.com/marmot-protocol/whitenoise/pull/569)와 [PR #576](https://github.com/marmot-protocol/whitenoise/pull/576)은 daemon이 relay에 닿지 못할 때 사용자가 이를 알 수 있도록 chat과 settings 화면에 offline notice를 추가했습니다. [PR #585](https://github.com/marmot-protocol/whitenoise/pull/585)는 광범위한 "delete all key packages" 경로를 "delete legacy key packages" 작업으로 좁혀, KeyPackage 형식 마이그레이션 중 현재 키까지 같이 지우는 일을 막습니다.

### MDK adds mixed-version invite support and SelfUpdate convergence

[MDK](https://github.com/marmot-protocol/mdk)는 [Marmot](/ko/topics/marmot/) Development Kit로, 7개의 PR을 병합했습니다. 작업을 관통하는 주제는 호환성입니다. Marmot 버전이 조금씩 다른 클라이언트들도 서로 초대하고, 자기 상태를 회전시키고, 잘못된 입력에서 깨끗하게 복구할 수 있게 하는 데 초점이 있습니다.

핵심 수정은 [PR #261](https://github.com/marmot-protocol/mdk/pull/261)로, 그룹의 `RequiredCapabilities`를 초대받는 쪽 capability의 LCD로 계산해 [Amethyst](https://github.com/vitorpamplona/amethyst)와 [White Noise](https://github.com/marmot-protocol/whitenoise) 사이의 mixed-version invite를 가능하게 합니다. [PR #264](https://github.com/marmot-protocol/mdk/pull/264)는 구현체 간 SelfUpdate wire format을 수렴시킵니다. SelfUpdate는 그룹 구성원이 자기 KeyPackage 또는 capability 상태를 회전할 때 보내는 control message이므로, 여기서 drift가 생기면 invite와 welcome이 계속 파싱되더라도 self-rotation이 조용히 깨집니다. robustness 측면에서 [PR #262](https://github.com/marmot-protocol/mdk/pull/262)는 생성자의 signer를 저장하기 전에 invitee key package를 파싱하게 해 잘못된 invitee가 찌꺼기 state를 남기지 못하게 하고, [PR #256](https://github.com/marmot-protocol/mdk/pull/256)은 receiver 쪽 admin depletion validation을 고치며, [PR #259](https://github.com/marmot-protocol/mdk/pull/259)는 메모리 저장소 backend가 압박 상황에서 보안상 중요한 state를 밀어내지 못하게 막습니다. [PR #265](https://github.com/marmot-protocol/mdk/pull/265)는 클라이언트가 MDK 내부를 직접 건드리지 않고도 다음 commit이 유효하려면 반드시 들어가야 할 proposal을 검사할 수 있는 `group_required_proposals` accessor를 노출합니다.

### nostter adds NIP-44 encryption across people lists, bookmarks, and mutes

[nostter](https://github.com/SnowCait/nostter)는 10개의 PR을 병합했습니다. [PR #2088](https://github.com/SnowCait/nostter/pull/2088)은 mute list에 [NIP-44](/ko/topics/nip-44/) 암호화를 추가하고, [PR #2089](https://github.com/SnowCait/nostter/pull/2089)는 bookmark에, [PR #2090](https://github.com/SnowCait/nostter/pull/2090)는 people list에 같은 암호화를 추가해 가능한 범위에서 [NIP-04](/ko/topics/nip-04/)를 대체합니다. [PR #2087](https://github.com/SnowCait/nostter/pull/2087)은 encrypted kind-10000 흐름이 안정화된 الآن, 예전 kind-30000 mute migration 경로를 제거합니다.

### zap.cooking ships Nourish scoring and a reusable comment thread

[zap.cooking](https://github.com/zapcooking/frontend)은 Nostr 레시피 클라이언트로, 이번 주 20개의 PR을 병합했습니다. 핵심 기능은 nutritional axis를 기준으로 레시피를 평가하는 새 Nourish recipe-scoring 모듈([PR #317](https://github.com/zapcooking/frontend/pull/317), [PR #319](https://github.com/zapcooking/frontend/pull/319))입니다. 동시에 [PR #299](https://github.com/zapcooking/frontend/pull/299)부터 [PR #302](https://github.com/zapcooking/frontend/pull/302)까지 이어지는 4단계 리팩터링은 Comments 모듈을 어디에나 넣을 수 있는 재사용 가능한 `CommentThread`로 뽑아냈습니다. 레시피 측 polish에는 [PR #309](https://github.com/zapcooking/frontend/pull/309)의 scaling, [PR #307](https://github.com/zapcooking/frontend/pull/307)의 통합 media-upload 버튼, [PR #310](https://github.com/zapcooking/frontend/pull/310)의 profile Replies 탭이 포함됩니다.

### ridestr extracts shared rider coordinator

[ridestr](https://github.com/variablefate/ridestr)는 분산 ride-sharing 앱으로, 10개의 PR을 병합하며 Compose 화면을 더 집중된 컴포넌트로 리팩터링하고 rider 및 driver 프로토콜 로직을 공통 `:common` coordinator 모듈로 추출했습니다([PR #70](https://github.com/variablefate/ridestr/pull/70)). [PR #60](https://github.com/variablefate/ridestr/pull/60)은 앱의 Roadflare 쪽을 위한 kind `3189` driver-ping receiver를 추가합니다.

### Blossom drafts a BUD-01 Sunset header for blob expiration

[Blossom](https://github.com/hzrd149/blossom)은 SHA-256 hash를 key로 삼아 HTTP 서버에 blob을 저장하는 hzrd149의 프로토콜로, [PR #99](https://github.com/hzrd149/blossom/pull/99)에서 BUD-01에 `Sunset` header를 추가하는 초안을 열었습니다. 서버는 이 header를 사용해 특정 blob이 언제부터 더 이상 제공되지 않을지를 미리 광고할 수 있어, 클라이언트가 404를 먼저 맞지 않고도 제한된 retention을 고려해 행동할 수 있습니다. 이 제안은 표준 [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html) 의미를 사용하고 참고용일 뿐이므로, 서버는 blob을 더 오래 유지할 수도 있고, 선언된 만료 시점을 best-effort 기준으로 따를 수도 있습니다.

## New Projects

### Forgesworn publishes a 29-repo cryptographic toolkit for Nostr

[Forgesworn](https://github.com/forgesworn)은 5일 동안 29개의 오픈소스 저장소를 공개하며 Nostr용 signing, identity, attestation, web-of-trust, paid-API discovery 전반을 한꺼번에 내놓았습니다.

signing stack의 중심은 하나의 master secret에서 무제한의 unlinkable Nostr identity를 파생하는 결정론적 하위 신원 도출 체계 [nsec-tree](https://github.com/forgesworn/nsec-tree)와, Tor를 기본으로 켠 Raspberry Pi용 NIP-46 remote signer [Heartwood](https://github.com/forgesworn/heartwood)입니다. [Sapwood](https://github.com/forgesworn/sapwood)는 Heartwood signer를 관리하기 위한 웹 UI를 제공하고, [heartwood-esp32](https://github.com/forgesworn/heartwood-esp32)는 Heltec WiFi LoRa 32 보드 위에 같은 signing token 로직의 스파이크 구현을 올립니다. [nsec-tree-cli](https://github.com/forgesworn/nsec-tree-cli)는 derivation, proof, Shamir recovery 흐름을 offline-first로 노출합니다.

identity와 trust 측면에서는 [Signet](https://github.com/forgesworn/signet)이 [v1.6.0](https://github.com/forgesworn/signet/releases/tag/v1.6.0)에 도달했습니다. 이는 Nostr용 탈중앙 identity verification 프로토콜로, session pubkey를 검증하고 relay에 pin하는 QR 기반 pairing 흐름을 가집니다. [nostr-attestations](https://github.com/forgesworn/nostr-attestations)는 credential, endorsement, vouch, provenance, licensing, trust를 포괄하는 단일 kind `31000` 이벤트(NIP-VA)를 정의해, 현재 여러 임시 이벤트 형식에 흩어져 있는 것을 하나로 모으려 합니다. [nostr-veil](https://github.com/forgesworn/nostr-veil)은 그 위에 privacy-preserving web of trust를 구축합니다. secp256k1 위 [LSAG ring signature](https://github.com/forgesworn/ring-sig)가 뒷받침하는 NIP-85 assertion을 통해, 어떤 vouch가 어느 멤버에게서 왔는지는 숨긴 채 그룹 소속 증명은 할 수 있게 합니다.

수익화 측면에서는 Lightning과 Nostr 위의 paid API를 다룹니다. [toll-booth](https://github.com/forgesworn/toll-booth)는 Express, Hono, Deno, Bun, Cloudflare Workers용 L402 middleware로, 어떤 API든 한 줄로 Lightning toll booth로 바꿉니다. [toll-booth-dvm](https://github.com/forgesworn/toll-booth-dvm)은 이 gated API를 [NIP-90](/ko/topics/nip-90/) Data Vending Machine으로 노출하고, [toll-booth-announce](https://github.com/forgesworn/toll-booth-announce)는 이를 [402-announce](https://github.com/forgesworn/402-announce)와 연결해 HTTP 402 서비스 발견용 kind `31402` parameterized replaceable event를 Nostr에 게시합니다. [402-indexer](https://github.com/forgesworn/402-indexer)는 이 공지를 수집하는 crawler입니다. 이 조직은 service coordination, trust, payment, dispute, key hierarchy, resource curation, paid API discovery를 다루는 [29개 NIP 초안 모음](https://github.com/forgesworn/nip-drafts)도 공개했습니다.

모든 것이 TypeScript이고, 가능한 경우 zero-dependency를 지향하며, multi-runner reproducible-build attestation과 OIDC trusted publishing이 포함된 bash-only 공급망 강화 도구 [anvil](https://github.com/forgesworn/anvil)로 배포됩니다. ring signature, range proof, Shamir word share를 포함한 이 세트의 여러 primitive는 Nostr 라이브러리 계층의 오래된 공백을 메웁니다.

### ShockWallet ships Nostr-native Lightning wallet sync and multi-node connections

[ShockWallet](https://github.com/shocknet/wallet2)은 self-custodial Lightning node에 연결하는 transport로 Nostr를 사용하는 Lightning wallet입니다. 앱은 하나 이상의 [Lightning.Pub](https://github.com/shocknet/Lightning.Pub) 노드와 `nprofile`을 통해 Nostr 위에서 pairing하고, wallet과 node 사이에서 end-to-end로 결제 승인을 서명합니다. 팀은 2026-04-18에 [PR #608](https://github.com/shocknet/wallet2/pull/608)을 배포하며 channels dashboard UI를 손봤고, 신규 PUB 사용자를 위한 admin invite-link QR 흐름([PR #606](https://github.com/shocknet/wallet2/pull/606))과 metrics dashboard 가독성 개선([PR #607](https://github.com/shocknet/wallet2/pull/607))도 함께 반영했습니다.

ShockWallet은 multi-device wallet state sync를 위해 [NIP-78](/ko/topics/nip-01/) application-specific data event를 사용하므로, 중앙 sync 서버 없이도 사용자의 wallet 뷰가 데스크톱 브라우저와 휴대폰 사이에서 일관되게 유지됩니다. 이는 [NIP-47](/ko/topics/nip-47/) (Nostr Wallet Connect)보다 한 계층 아래에 있습니다. NIP-47이 앱이 기존 wallet에 결제를 요청하는 인터페이스라면, ShockWallet은 Nostr를 wallet 자체의 account 및 session transport로 사용해 실제 Lightning node에 연결합니다. 팀은 wallet과 함께 wallet-to-app 연결용 Nostr 기반 session-pairing 프로토콜 [CLINK](https://github.com/shocknet/CLINK)도 밀고 있으며, web, Android, iOS로 빌드되는 단일 TypeScript 코드베이스를 유지하고 있습니다.

### Nostrability issues migrate to git over Nostr after GitHub censorship

[Nostrability](https://gitworkshop.dev/elsat@habla.news/nostrability/issues)는 elsat의 Nostr 클라이언트 및 relay 상호운용성 트래커로, GitHub 지원에서 2주 동안 응답을 받지 못한 채 조직이 내려간 뒤 issue 워크플로를 git over Nostr로 옮기고 있습니다. 이 issue 트래커는 이제 GitWorkshop/ngit에 있으며, 기존 issue도 옮겨졌고 앞으로의 interop report도 Nostr 네이티브 인프라 안에서 유지될 수 있습니다.

### nowhere encodes full websites into URL fragments and routes orders through Nostr

[nowhere](https://github.com/5t34k/nowhere)는 [5t34k](https://github.com/5t34k)의 새 AGPL-3.0 프로젝트로, 사이트 전체를 `#` 뒤 URL fragment에 직렬화하고 dictionary substitution과 raw DEFLATE로 압축한 뒤 base64url로 인코딩합니다. HTTP는 브라우저가 fragment를 서버로 보내지 못하게 하므로, 페이지를 전달하는 호스트는 콘텐츠를 보지 못하고 사이트 자체도 서버에 저장되지 않습니다. 이 프로젝트는 event, fundraiser, store, petition, message, drop, art, forum의 여덟 가지 site type을 제공하며, 각 site는 제작자의 암호학적 서명을 붙일 수 있고 URL 수준의 비밀번호 암호화도 가능합니다.

여덟 가지 중 다섯 가지는 순수 정적이지만, store, forum, petition은 order, post, signature를 위한 실시간 통신이 필요하고, 이 트래픽은 일회용 키와 [NIP-44](/ko/topics/nip-44/) 암호화를 사용해 Nostr relay를 통과합니다. 따라서 relay는 읽을 수 없는 이벤트를, 추적하기 어려운 일회용 키에서 받아 저장하게 됩니다. 단일 상품 store는 약 120자 안에 들어가므로, companion reader [nowhr.xyz](https://nowhr.xyz/install)를 통해 nowhere 링크를 오프라인용 인쇄 QR 코드로도 사용할 수 있습니다. 저장소는 standalone `codec` 패키지, Nostr 통합 및 결제 처리가 들어간 Svelte 5 `web` component library, [nowhr.xyz](https://nowhr.xyz/app)의 `nowhr` app shell로 나뉜 pnpm workspace입니다.

### Small new surfaces: relayk.it and Brainstorm Search

큰 changelog hook은 없지만 짧게 언급할 만한 두 프로젝트입니다. [relayk.it](https://relayk.it)은 Soapbox 팀의 [sam](https://nostr.com/sam@relayk.it)이 만든, [Shakespeare](https://shakespeare.diy) 기반의 relay discovery 클라이언트로 브라우저에서 완전히 실행되며 사용자에게 활성 Nostr relay를 안내합니다. [Brainstorm Search](https://brainstorm.world)는 네트워크 전반의 콘텐츠를 보여 주는 데 초점을 맞춘 single-page Nostr search UI로 출시됐습니다.

## Protocol and Spec Work

### NIP Updates

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 제안과 논의입니다:

**Open PRs and Discussions:**

- **[NIP-67](/ko/topics/nip-67/): EOSE Completeness Hint** ([PR #2317](https://github.com/nostr-protocol/nips/pull/2317)): [NIP-01](/ko/topics/nip-01/)의 `EOSE` 메시지에 선택적인 세 번째 요소를 추가해, 릴레이가 필터와 일치하는 저장 이벤트를 모두 전달했는지 표시하자는 제안입니다. 현재 `EOSE`는 저장 이벤트와 실시간 이벤트의 경계를 표시할 뿐 완전성 정보는 담지 않습니다. 예를 들어 300개 cap이 있는 릴레이에 이벤트 500개를 요청하면, 클라이언트는 300개와 `EOSE`를 받지만 이것이 "원래 300개뿐"인지 "중간에서 끊겼다"인지를 구분할 수 없습니다. 제안은 릴레이가 모든 결과를 보냈을 때 `[["EOSE", "<sub_id>", "finish"]]` 형식을 사용하고, 기존 두 요소 형식은 아무 주장도 하지 않는 legacy 형식으로 남겨 둡니다. 이 설계는 하위 호환적이며, 이를 아는 클라이언트는 `"finish"`를 보는 즉시 pagination을 멈출 수 있습니다.

- **NIP-5D: Nostr Applets** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Nostr 위에서 상호작용 applet을 배포하는 새 kind를 제안합니다. [NIP-5A](/ko/topics/nip-5a/)가 정적 웹사이트를, 개발 중인 [NIP-5C](/ko/topics/nip-5c/)가 실행 가능한 WASM scroll을 다룬다면, NIP-5D는 클라이언트의 sandboxed iframe 또는 WebView에서 실행되는 self-contained front-end applet이라는 중간 지대를 노립니다. 이로써 클라이언트는 각자 별도의 플러그인 시스템을 만들지 않고도 poll, 계산기, 미니게임 같은 서드파티 경험을 실을 수 있습니다. 열린 PR은 host와 applet 사이 message passing 보안 모델을 계속 다듬고 있습니다.

- **NIP-29: Subgroups spec** ([PR #2319](https://github.com/nostr-protocol/nips/pull/2319)): [NIP-29](/ko/topics/nip-29/) 릴레이 기반 그룹을 subgroup 계층으로 확장해, 같은 그룹 안에 여러 병렬 채널을 둘 수 있게 합니다. 이 PR은 기존 `h` 태그에 subgroup 식별자를 실어 보내는 방식을 정의하고, kind `9000`번대 moderation 이벤트가 subgroup에 어떻게 적용되는지와 클라이언트 렌더링 방식을 명확히 합니다. 변경은 일반 메시지의 단일 `h` 태그 형태를 유지하므로 오래된 클라이언트도 subgroup이 있는 room에서 계속 동작할 수 있습니다.

- **NIP-29: Explicit role permissions on kind 39003** ([PR #2316](https://github.com/nostr-protocol/nips/pull/2316)): [NIP-29](/ko/topics/nip-29/) kind `39003` 역할 이벤트에 명시적 권한 스키마를 정의합니다. 각 역할은 invite, add-user, remove-user, edit-metadata, delete-event, add-permission 같은 허용 작업의 이름 붙은 집합이 되고, 선택적인 만료 시각도 가질 수 있습니다. 현재 동일한 그룹을 운영하는 두 NIP-29 relay가 "moderator" 권한을 서로 다르게 해석할 수 있는데, 이 스키마는 그 차이를 클라이언트가 사용자에게 보여 줄 수 있게 합니다.

- **NIP-11: access_control field for gated-relay discovery** ([PR #2318](https://github.com/nostr-protocol/nips/pull/2318)): [NIP-11](/ko/topics/nip-11/) relay information document에 선택적 `access_control` 객체를 추가하는 제안입니다. 여기에는 relay의 게이팅 방식(open, invite, payment, allowlist)과 접근 요청 endpoint가 담깁니다. 이 필드는 참고용이며, 클라이언트와 디렉터리가 gated relay를 public discovery 목록에서 필터링하고 사용자가 왜 쓰기 요청이 거부되는지 미리 알 수 있게 합니다.

- **NIP-63a: Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)): [뉴스레터 #18](/en/newsletters/2026-04-15-newsletter/)에서 다뤘습니다. 이 PR은 kind `10164` payment-gateway-descriptor 형식과 tier별 subscription rule 레이아웃을 계속 다듬고 있습니다.

- **NIP-XX: Agent Reputation Attestations (Kind 30085)** ([PR #2320](https://github.com/nostr-protocol/nips/pull/2320)): Nostr의 자율 에이전트와 서비스에 대한 서명된 평판 attestations를 위한 kind `30085` addressable event를 제안합니다. 여기에 포함되는 평가는 reliability, honest-advertising, dispute-resolution 관련 주장입니다. 각 attestation은 대상 pubkey를 가리키고, bounded range 안의 score를 담으며, 그 score를 정당화하는 evidence event를 참조합니다. 동기는 [NIP-90](/ko/topics/nip-90/) Data Vending Machine과 기타 서비스 시장에 고객 피드백을 표준 방식으로 게시하고 필터링할 수 있는 규약이 아직 없다는 점입니다.

- **NIP-TPLD: Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)): [뉴스레터 #18](/en/newsletters/2026-04-15-newsletter/)에서 이어지는 작업으로, kind `20411` ephemeral 범위, 수신자별 [NIP-44](/ko/topics/nip-44/) 암호화 구조, relay retention을 위한 `ttl` 태그 의미를 더 다듬고 있습니다.

- **marmot-ts 0.5.0 release PR** ([PR #70](https://github.com/marmot-protocol/marmot-ts/pull/70)): 보류 중인 `@internet-privacy/marmot-ts@0.5.0` 릴리스 PR은 TypeScript Marmot 클라이언트의 첫 계획된 breaking change를 묶고 있습니다. 릴리스는 `KeyPackageManager`가 예전 kind `443`과 새 kind `30443` 이벤트를 둘 다 지원하도록 바꾸고, `KeyPackageStore`와 group-state storage 클래스를 제거하는 대신 일반 key-value store를 `KeyPackageManager`와 `MarmotGroup`에 직접 넘기도록 하며, invite와 group 관리를 `MarmotClient.invites`와 `MarmotClient.groups`로 옮깁니다. marmot-ts를 직접 임베드한 프로젝트는 이 릴리스를 적용하기 전에 constructor와 storage layer 변경이 필요합니다.

## NIP Deep Dive: NIP-72 (Moderated Communities)

[NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md)은, moderation이 otherwise-unrestricted write 위에 curated read view를 만드는 Nostr의 주제 기반 community 모델을 정의합니다. 멤버십과 moderation 모두를 릴레이가 권한으로 쥐는 [NIP-29](/ko/topics/nip-29/)와 달리, NIP-72 커뮤니티는 일반 Nostr 이벤트 위에 존재하며 관련 kind를 운반하는 모든 릴레이에서 제공할 수 있습니다. 누구나 커뮤니티에 게시할 수 있고, 인정된 moderator가 승인한 게시물만 커뮤니티 피드에 나타납니다.

커뮤니티는 생성자가 게시하는 kind `34550` addressable event로 정의됩니다. 이 이벤트는 `d` 태그를 가진 replaceable event이므로, 생성자는 identity를 유지한 채 메타데이터를 업데이트할 수 있습니다. `d` 태그는 안정적인 slug이고, `name`, `description`, `image`, `rules` 태그는 표시용 메타데이터를 담으며, `"moderator"` 마커가 붙은 일련의 `p` 태그는 어느 pubkey의 승인이 유효한지 나열합니다. 선택적인 `relay` 태그는 `author`, `requests`, `approvals` 마커와 함께 각 이벤트 유형을 어디서 게시하고 어디서 읽어야 하는지 힌트를 줍니다:

```json
{
  "id": "f1e2d3c4b5a69788f1e2d3c4b5a69788f1e2d3c4b5a69788f1e2d3c4b5a69788",
  "pubkey": "c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2",
  "created_at": 1745280000,
  "kind": 34550,
  "tags": [
    ["d", "bitcoin-devs"],
    ["name", "Bitcoin Devs"],
    ["description", "A moderated community for Bitcoin protocol discussion."],
    ["image", "https://example.com/bitcoin-devs.png"],
    ["rules", "Technical discussion only. No price talk."],
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876", "", "moderator"],
    ["p", "a1b2c3d4e5f6a7b8c9d0a1b2c3d4e5f6a7b8c9d0a1b2c3d4e5f6a7b8c9d0a1b2", "", "moderator"],
    ["relay", "wss://relay.example.com", "author"],
    ["relay", "wss://relay.moderator.com", "approvals"]
  ],
  "content": "",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

사용자는 일반 이벤트(kind `1` 노트, kind `30023` 장문 글, kind `31922` 캘린더 이벤트 등)를 게시하고, 값이 커뮤니티 좌표 `34550:<creator_pubkey>:<slug>`인 `a` 태그를 추가해 게시물을 제출합니다. 이 게시물은 그 자체로 완전히 유효한 Nostr 이벤트이며, NIP-72를 모르는 클라이언트는 단순히 커뮤니티 형태 좌표를 가리키는 노트로 보게 됩니다. 반면 community-aware 클라이언트는 인정된 moderator가 승인한 게시물만 커뮤니티 뷰에 보여 줍니다.

승인은 moderator가 게시하는 별도의 kind `4549` 이벤트입니다. 이 이벤트는 `e` 태그로 제출물을, `p` 태그로 제출자를, `a` 태그로 커뮤니티를 참조하고, 문자열화된 제출 이벤트를 `content`에 캐시 사본으로 내장합니다. 이 캐시 사본 덕분에 원 작성자가 나중에 원본 이벤트를 삭제해도 승인된 게시물은 계속 렌더링할 수 있습니다.

```json
{
  "id": "a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1745283600,
  "kind": 4549,
  "tags": [
    ["a", "34550:c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2:bitcoin-devs"],
    ["e", "b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4"],
    ["p", "e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5"],
    ["k", "1"]
  ],
  "content": "{\"id\":\"b3c4d5e6...\",\"pubkey\":\"e4f5a6b7...\",\"kind\":1,\"content\":\"Question about sighash flags\",\"tags\":[[\"a\",\"34550:c3d2e1f0...:bitcoin-devs\"]],\"created_at\":1745283500,\"sig\":\"...\"}",
  "sig": "bbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aa"
}
```

이 승인 모델에는 세 가지 유용한 성질이 있습니다. moderation 결정은 투명합니다. 각 승인은 누구나 가져올 수 있는 서명된 Nostr 이벤트이므로, 의심이 많은 사용자는 어느 moderator가 어느 게시물을 언제 승인했는지 감사할 수 있습니다. moderation은 배타적이지 않습니다. 같은 제출물이 여러 커뮤니티에서 승인될 수 있고, 한 커뮤니티가 거절한 글을 다른 커뮤니티는 승인할 수 있습니다. `a` 태그는 단지 curated view의 주소이기 때문입니다. moderation은 read layer에서 되돌릴 수 있습니다. 커뮤니티가 kind `34550` 이벤트에서 어떤 moderator를 제거하면, 현재 moderator 목록을 따르는 클라이언트에서는 그 moderator의 과거 승인도 더 이상 세지지 않습니다.

클라이언트 구현은 read 쪽에서 갈립니다. 대부분의 community-aware 클라이언트는 커뮤니티 좌표가 붙은 kind `4549` 이벤트를 필터링하고, 내부 event ID로 deduplicate한 뒤, 내장된 게시물을 렌더링합니다. 일부 클라이언트는 제출 이벤트를 직접 가져오고 approval을 whitelist로만 사용하기도 합니다. approval이 불완전하거나 stale할 때는 이 편이 더 실용적일 수 있습니다. [noStrudel](https://github.com/hzrd149/nostrudel)과, 이번 주 [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) 기준 [Amethyst](https://github.com/vitorpamplona/amethyst)를 포함한 몇몇 클라이언트는 moderator용 대기 제출 큐도 별도 뷰로 노출합니다.

[NIP-29](/ko/topics/nip-29/)와 비교한 tradeoff는 분명합니다. NIP-72 커뮤니티는 특별한 릴레이 지원 없이 어떤 릴레이 네트워크에서도 동작하므로 write path가 이식 가능하고 moderation이 가시적이며 fork 가능합니다. 반면 제출물은 게시되는 순간 public이고, 승인되지 않은 게시물은 클라이언트 렌더링 계층에서만 숨겨집니다. 스팸이 wire에 아예 올라오면 안 되는 공간이라면 NIP-29가 더 적합합니다. 승인이 gate라기보다 curated front page처럼 작동하는 공개 토픽 커뮤니티에는 NIP-72가 더 잘 맞습니다.

## NIP Deep Dive: NIP-57 (Zaps)

[NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md)은 Lightning 결제를 Nostr 신원과 이벤트에 연결하고, 검증 가능한 payment receipt를 릴레이 위에 다시 게시하는 zap을 정의합니다. zap은 특정 발신자가 특정 수신자에게 특정 대상에 대해 특정 금액을 지불했다는 사실을 증명하며, 그 증명은 발신자의 말을 신뢰하지 않고도 어떤 Nostr 클라이언트든 읽을 수 있습니다. 이 명세는 LNURL, Lightning, Nostr라는 세 시스템을 가로지르며 각자가 어떻게 협력해야 하는지 고정합니다.

흐름에는 네 명의 행위자가 있습니다. 발신자 클라이언트는 수신자의 kind `0` 프로필 메타데이터(`lud06` 또는 `lud16`)나 zap 대상 이벤트의 `zap` 태그에서 수신자의 LNURL endpoint를 발견합니다. 그 클라이언트는 의도된 결제를 설명하는 kind `9734` zap request 이벤트에 서명하고, 이를 릴레이가 아니라 수신자의 LNURL callback으로 게시합니다. 반대편에서 수신자의 LNURL 서버는 요청을 검증하고, description hash가 문자열화된 request 이벤트에 커밋되는 Lightning invoice를 반환합니다. 발신자가 이를 결제하면, 서버는 발신자가 요구한 relay 집합에 kind `9735` zap receipt를 게시합니다.

zap request(kind `9734`)는 결제 의도를 선언하는 서명된 이벤트입니다. 핵심 필드는 수신자 pubkey를 담은 `p` 태그, zap 대상 이벤트나 addressable 콘텐츠를 가리키는 선택적 `e` 또는 `a` 태그, millisats 단위 `amount` 태그, receipt 게시 릴레이 목록인 `relays` 태그입니다. `content`에는 zap과 함께 전달되는 발신자 메시지가 들어갈 수 있습니다. `k` 태그는 대상 kind를 기록해, 소비자가 어떤 종류의 콘텐츠에 자금이 갔는지 분류하게 합니다:

```json
{
  "id": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "pubkey": "a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876",
  "created_at": 1745280000,
  "kind": 9734,
  "tags": [
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["e", "b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4"],
    ["amount", "21000"],
    ["relays", "wss://relay.damus.io", "wss://nos.lol", "wss://relay.nostr.band"],
    ["k", "1"]
  ],
  "content": "great post",
  "sig": "ccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbcc"
}
```

zap receipt(kind `9735`)는 결제 확인 후 수신자의 wallet 서버가 게시합니다. 이 receipt는 발신자가 아니라, LNURL 응답에서 수신자가 광고한 `nostrPubkey`를 사용하는 wallet 서버가 서명합니다. 유효한 receipt는 `description` 태그 안에 문자열화된 zap request를, `bolt11` 태그에 지불된 인보이스를, `preimage` 태그에 결제 완료 증명을 담습니다:

```json
{
  "id": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "pubkey": "e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0",
  "created_at": 1745280060,
  "kind": 9735,
  "tags": [
    ["p", "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876"],
    ["P", "a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876a5b4c3d2e1f09876"],
    ["e", "b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4"],
    ["bolt11", "lnbc210n1pj...bolt11invoicestring"],
    ["description", "{\"id\":\"c1d2e3f4...\",\"pubkey\":\"a5b4c3d2...\",\"kind\":9734,\"content\":\"great post\",\"tags\":[...]}"],
    ["preimage", "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"]
  ],
  "content": "",
  "sig": "ddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccdd"
}
```

검증 규칙이 NIP-57의 신뢰 보장을 만듭니다. kind `9735` receipt를 zap으로 표시하는 클라이언트는 네 가지를 확인해야 합니다. receipt 서명이 LNURL 응답의 `nostrPubkey`와 일치하는지, `bolt11` 인보이스 금액이 내장 zap request의 `amount` 태그와 같은지, 인보이스 description hash가 문자열화된 zap request에 커밋되는지, `preimage`가 인보이스의 `payment_hash`로 해시되는지입니다. 이 중 하나라도 실패하면 그것은 결제 증명이 아니라 결제 주장일 뿐입니다. 이런 검증 없이 누적 zap count를 렌더링하는 클라이언트는 공격자가 게시한 위조 kind `9735` 이벤트에 쉽게 속습니다.

private zap은 여기에 기밀성 계층을 하나 더 얹습니다. 발신자는 zap request의 `content`를 수신자용으로 암호화하고 바깥 zap request에 `anon` 태그를 넣을 수 있어, 릴레이 네트워크는 결제 대상은 보되 메모는 읽지 못합니다. 어떤 클라이언트는 더 나아가 zap request 자체를 위해 새 일회용 키페어를 만들어, receipt는 결제가 일어났음을 증명하면서도 수신자가 이를 발신자의 장기 pubkey와 연결하지 못하게 합니다. 이 "anonymous zap" 패턴은 메시지는 숨지만 발신자 키는 요청 경로에 남을 수 있는 일반 private zap보다 강합니다.

NIP-57은 [NIP-75](/ko/topics/nip-75/)에서 정의한 zap-goal 시스템의 기반이기도 합니다. goal은 목표 금액과 receipt를 집계할 relay 집합을 선언하는 kind `9041` 이벤트이며, goal의 event ID에 연결된 모든 zap receipt가 그 진행률에 기여합니다. 클라이언트는 일치하는 kind `9735` 이벤트의 검증된 `bolt11` 금액을 합산해 진행률을 계산합니다. [Amethyst](https://github.com/vitorpamplona/amethyst)의 이번 주 [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469)는 goal을 [NIP-53](/ko/topics/nip-53/) Live Activities 화면에 연결하고, 같은 receipt로 top-zappers 리더보드도 렌더링합니다.

zap split은 이 NIP의 부록에 정의되어 있습니다. 수신자는 가중치가 다른 여러 `zap` 태그를 가진 kind `0` 프로필을 게시해, 하나의 zap 결제가 여러 pubkey 사이에 원자적으로 분배되게 할 수 있습니다. 콘텐츠 제작자, 협업자, 플랫폼 수수료 수취자를 모두 하나의 발신자 서명 zap request로 함께 지불할 수 있습니다. [Amethyst](https://github.com/vitorpamplona/amethyst), [Damus](https://github.com/damus-io/damus), [noStrudel](https://github.com/hzrd149/nostrudel)을 포함한 여러 클라이언트가 split-paying을 end-to-end로 구현합니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 있거나 소식을 나누고 싶다면 Nostr에서 DM을 보내거나 [nostrcompass.org](https://nostrcompass.org)에서 찾아 주세요.
