---
title: 'Nostr Compass #7'
date: 2026-01-28
translationOf: /en/newsletters/2026-01-28-newsletter.md
translationDate: 2026-01-28
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 안내하는 주간 뉴스레터입니다.

**이번 주:** Ridestr가 [Cashu](/ko/topics/cashu/) 결제와 암호화된 위치 공유를 통해 탈중앙화 라이드셰어링을 Nostr에 도입했습니다. Pomade는 다중서명 서명자를 위한 이메일 기반 복구 기능을 선보였습니다. Damus는 안정적인 DM 동기화를 위해 [negentropy](/ko/topics/negentropy/)를 출시했습니다. Amethyst 데스크톱 앱에 검색, 북마크, zap 기능이 추가되었습니다. Amber v4.1.1은 relay 신뢰도 점수를 표시합니다. Marmot는 MIP-03을 병합하고 TypeScript 참조 채팅 앱을 개발 중입니다. diVine은 [NIP-46](/ko/topics/nip-46/) QR 인증과 멘션 지원을 추가했습니다. 새로운 NIP 제안들은 커뮤니티 관리, 시퀀스 기반 동기화, 암호화된 파일 저장을 다룹니다. 또한 Nostr 1월의 5년을 돌아보며, 2021년 소수의 얼리 어답터들부터 2023년 Damus의 폭발적인 App Store 출시, 2025년 성숙해진 클라이언트 생태계까지 프로토콜의 진화를 추적합니다.

## 뉴스

### Ridestr, Nostr에 탈중앙화 라이드셰어링 도입

[Ridestr](https://github.com/variablefate/ridestr)는 Nostr 위에 완전히 구축된 P2P 라이드셰어 애플리케이션을 개발 중이며, Bitcoin과 [Cashu](/ko/topics/cashu/) 결제를 통한 드라이버-라이더 간 직접 거래를 가능하게 합니다. 이 프로토콜은 커스텀 event kind(30173, 3173-3175, 30180/30181)를 사용하여 라이드를 조정하면서 점진적 위치 공개와 [NIP-44](/ko/topics/nip-44/) 암호화를 통해 프라이버시를 유지합니다.

시스템은 신중하게 조율된 흐름으로 작동합니다: 드라이버는 kind 30173 event를 통해 geohash로 인코딩된 위치(약 5km 정밀도)로 가용성을 브로드캐스트하고, 라이더는 kind 3173을 통해 요금 견적과 함께 라이드를 요청하며, 라이드 시작 전에 HTLC 에스크로 토큰을 사용하여 결제가 보장됩니다. 위치 프라이버시는 점진적 공개를 통해 보존되며, 픽업 세부정보는 드라이버가 도착했을 때만 공개되고 목적지는 PIN 확인 후에 공유됩니다. 당사자 간의 모든 통신은 프라이버시를 위해 [NIP-44](/ko/topics/nip-44/) 암호화를 사용합니다.

Ridestr는 P2PK 서명이 포함된 HTLC 에스크로를 통해 결제 보안을 구현합니다. 라이더가 드라이버의 제안을 수락하면, 드라이버만 라이드 완료 후 청구할 수 있는 payment hash로 [Cashu](/ko/topics/cashu/) 토큰을 잠급니다. 현재 프로토콜은 단일 mint 아키텍처로 운영되어 라이더와 드라이버가 동일한 [Cashu](/ko/topics/cashu/) mint를 사용해야 합니다. 프로젝트의 Kotlin 기반 Android 구현은 NUT-07 상태 확인을 통해 증명 검증 및 오래된 증명 복구를 처리합니다.

Ridestr는 대부분의 Nostr 애플리케이션이 피하는 과제들을 해결합니다: 실시간 위치 조정, 분쟁 해결이 포함된 결제 에스크로, 물리적 세계 상호작용을 위한 평판 시스템. 이 프로젝트는 베타 단계이며 Nostr의 event 모델이 콘텐츠 공유뿐만 아니라 P2P 서비스 마켓플레이스도 지원할 수 있음을 보여줍니다.

### Pomade, 다중서명 서명자를 위한 알파 복구 시스템 출시

hodlbod가 개발한 [Pomade](https://github.com/coracle-social/pomade)는 기존 [FROSTR](https://github.com/FROSTR-ORG) 생태계 위에 구축되어 복구 중심의 임계값 서명 서비스를 제공합니다. @frostr/bifrost 라이브러리를 통한 [FROST](/ko/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) 서명을 사용하여, Pomade는 임계값 암호화 위에 이메일 기반 복구 흐름을 추가합니다. 시스템은 Shamir Secret Sharing을 사용하여 사용자의 비밀 키를 분할하고, 구성 가능한 임계값(2-of-3, 3-of-5 등)으로 여러 독립 서명자에게 분산합니다.

프로토콜은 [NIP-44](/ko/topics/nip-44/) 암호화 페이로드가 포함된 단일 event kind(28350)를 사용하여 Nostr를 통해 완전히 작동합니다. 서명 시, 클라이언트는 최소 `threshold` 서명자에게 부분 서명을 요청한 다음 이를 유효한 Schnorr 서명으로 집계합니다. 암호화의 경우, 서명자들은 어느 단일 당사자도 전체 키를 학습하지 않고 ECDH를 통해 공유 비밀을 도출하기 위해 협력합니다.

복구는 두 가지 인증 방법을 통해 작동합니다: 비밀번호 기반(서명자의 pubkey를 salt로 사용하는 argon2id) 또는 이메일 OTP. OTP 복구 중 MITM 공격을 방지하기 위해, 각 서명자는 클라이언트가 제공한 접두사로 자체 확인 코드를 생성하여 사용자가 각 서명자와 독립적으로 인증하도록 요구합니다. 프로토콜은 스팸 방지를 위해 등록 event에 작업 증명([NIP-13](/ko/topics/nip-13/)에 따라 20+ 비트)을 요구합니다.

신뢰 모델은 명시적입니다: `threshold` 서명자가 공모하면 키를 훔칠 수 있습니다. 이메일 제공자는 OTP를 가로챌 수 있으므로 완전히 신뢰됩니다. 사용자는 전체 비밀 키를 독립적으로 복구할 수 없으며, 이를 위해서는 `threshold` 서명자의 협력이 필요합니다. 프로토콜은 키 관리에 익숙하지 않은 신규 사용자 온보딩을 위해 설계되었으며, 사용자가 익숙해지면 자기 수탁으로 마이그레이션할 것을 명시적으로 권장합니다. Pomade는 감사되지 않은 알파 상태를 고려하여 "키 손실, 도난, 서비스 거부 또는 메타데이터 유출" 가능성에 대해 경고합니다.

## 릴리스

### Damus, 안정적인 DM 동기화를 위해 Negentropy 출시

[Damus v1.13](https://github.com/damus-io/damus/releases/tag/v1.13-6)은 [지난주 오픈 PR로 미리 본](/ko/newsletters/2026-01-21-newsletter/#damus-ios-client---open-prs) negentropy 구현을 출시했습니다. [PR #3536](https://github.com/damus-io/damus/pull/3536)은 네트워킹 레이어에 기본 [negentropy](/ko/topics/negentropy/) 지원을 추가하여, 프로토콜을 지원하는 relay와의 집합 조정을 가능하게 합니다. 동반 [PR #3547](https://github.com/damus-io/damus/pull/3547)은 표준 REQ 구독이 실패할 때 누락된 메시지를 복구하기 위해 negentropy를 사용하는 당겨서 새로고침 DM 동기화를 추가합니다.

구현은 보수적인 접근 방식을 따릅니다: 일반적인 DM 로딩은 변경 없이 계속되며, [negentropy](/ko/topics/negentropy/)는 사용자가 수동으로 새로고침할 때 복구 메커니즘으로 사용 가능합니다. 자동화된 테스트는 표준 쿼리가 놓칠 수 있는 오래된 타임스탬프의 DM을 생성한 다음 [negentropy](/ko/topics/negentropy/) 동기화를 사용하여 성공적으로 검색하는 것으로 수정을 시연합니다. [negentropy](/ko/topics/negentropy/) 지원은 호환되는 relay가 필요하지만, 구현은 가능한 곳에서 프로토콜을 사용하여 혼합 relay 환경을 우아하게 처리합니다.

### Amber v4.1.1 - Relay 신뢰도 점수

[Amber v4.1.1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.1)은 relay 신뢰도 점수 표시([PR #289](https://github.com/greenart7c3/Amber/pull/289))를 출시하여, [지난주 Trusted Relay Assertions NIP 보도](/ko/newsletters/2026-01-21-newsletter/#nip-updates)에서 논의된 relay 평가 개념을 구현합니다. 신뢰도 점수는 이제 Relays 페이지와 NostrConnect 연결 요청에 표시되어, 사용자가 연결을 승인하기 전에 relay 신뢰성을 평가할 수 있습니다. 이 릴리스에는 재설계된 로그인/이벤트/권한 UI와 `switch_relays` 메서드 지원도 포함됩니다. 성능 개선은 keystore 작업을 캐시하여, 구형 기기에서 20초 이상의 로드 시간에 대한 보고를 해결합니다.

### nak v0.18.2 - MCP 통합

fiatjaf의 [nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) [v0.18.2](https://github.com/fiatjaf/nak/releases/tag/v0.18.2)는 `nak mcp`를 통해 [Model Context Protocol](https://nostrify.dev/mcp) 지원을 추가하여, AI 에이전트가 Nostr에서 사람을 검색하고, 노트를 게시하고, 사용자를 멘션하고, outbox 모델을 사용하여 콘텐츠를 읽을 수 있게 합니다. 이 릴리스는 또한 사전 빌드된 바이너리를 다운로드하는 [원라인 설치 프로그램](https://github.com/fiatjaf/nak/blob/master/install.sh)(`curl -sSL https://raw.githubusercontent.com/fiatjaf/nak/master/install.sh | sh`)을 도입하여, 최종 사용자에게 Go 툴체인 요구 사항을 제거합니다. Bunker 모드는 이제 Unix 소켓과 `switch_relays`를 지원합니다.

### Zeus v0.12.2 Beta - NWC 수정

[Zeus v0.12.2-beta1](https://github.com/ZeusLN/zeus/releases)은 [지난주 Zeus 보도](/ko/newsletters/2026-01-21-newsletter/#zeus-lightning-wallet-with-nostr-wallet-connect)에서 다룬 문제를 해결하는 여러 NWC 수정 사항을 출시합니다.

## 프로젝트 업데이트

### Amethyst Desktop - 페이즈 2A 출시

[Amethyst](https://github.com/vitorpamplona/amethyst)는 [데스크톱 앱의 페이즈 2A](https://github.com/vitorpamplona/amethyst/pull/1676)를 출시하여, 데스크톱 경험에 검색, 북마크, Zap, 스레드 뷰, 장문 콘텐츠(Reads)를 추가했습니다. 동반 [PR #1683](https://github.com/vitorpamplona/amethyst/pull/1683)은 투명한 event 브로드캐스팅 피드백을 추가하여, 사용자가 이제 event가 네트워크 전체에 전파될 때 relay별 실시간 상태를 볼 수 있어 연결 문제를 진단하기 쉬워졌습니다.

### Notedeck 진행 상황: 캘린더 앱과 UX 개선

Damus 팀의 [Notedeck](https://github.com/damus-io/notedeck) 데스크톱 클라이언트는 모바일 뷰에서 더 많은 화면 공간을 위해 스크롤 속도에 반응하는 자동 숨김 툴바 동작([PR #1268](https://github.com/damus-io/notedeck/pull/1268))을 병합했습니다. [드래프트 PR #1271](https://github.com/damus-io/notedeck/pull/1271)은 월/주/일/의제 뷰, RSVP 지원, 캘린더 이벤트에 대한 [NIP-22](/ko/topics/nip-22/) 댓글이 포함된 전체 [NIP-52](/ko/topics/nip-52/) 캘린더 앱을 추가하며, 현재 테스트를 위해 기능 플래그로 설정되어 있습니다.

### Jumble, 커뮤니티 모드 추가

relay 중심 웹 클라이언트인 [Jumble](https://github.com/CodyTseng/jumble)은 [커뮤니티 모드](https://github.com/CodyTseng/jumble/pull/738)와 [환경 변수를 통한 relay 세트 프리셋](https://github.com/CodyTseng/jumble/pull/736) 지원을 추가하여, [nostr.moe](https://nostr.moe/)와 같은 테마별 인스턴스를 쉽게 배포할 수 있게 했습니다.

### Shopstr 주문 대시보드

[Shopstr](https://github.com/shopstr-eng/shopstr)는 채팅 기반 주문 관리를 전용 [주문 대시보드](https://github.com/shopstr-eng/shopstr/pull/219)로 교체했습니다. 새 인터페이스는 판매자가 주문 상태를 추적하고, 메시지를 읽음으로 표시하고, 채팅 스레드를 스크롤하지 않고도 이행을 관리할 수 있는 중앙 집중식 뷰를 제공합니다. 이 업데이트는 더 나은 필터링을 위해 주문 DM이 태그되는 방식을 수정하고 서버 측 주문 상태 API를 위해 IndexedDB 캐싱을 폐기합니다.

### Formstr, 그리드 질문 추가

Nostr 네이티브 폼 앱인 [Formstr](https://github.com/abh3po/nostr-forms)는 [그리드 질문](https://github.com/abh3po/nostr-forms/pull/419)을 추가하고 임베드 지원과 함께 [SDK를 재작성](https://github.com/abh3po/nostr-forms/pull/410)했습니다. [비-NIP-07 서명자를 위한 수정](https://github.com/abh3po/nostr-forms/pull/418)은 bunker나 로컬 서명자를 사용하여 자신의 신원으로 폼을 제출하려는 사용자의 문제를 해결했습니다.

### nostr-tools 암호화 의존성 업그레이드

핵심 JavaScript 라이브러리인 [nostr-tools](https://github.com/nbd-wtf/nostr-tools)는 [@noble/curves v2.0.1로 업그레이드](https://github.com/nbd-wtf/nostr-tools/pull/520)하여, 27개 파일에 걸친 브레이킹 API 변경을 해결하고 최신 감사된 noble 라이브러리를 채택했습니다. fiatjaf는 또한 [NIP-46](/ko/topics/nip-46/)에 `switch_relays` 지원을 추가하여, bunker 클라이언트가 relay 연결을 동적으로 변경할 수 있게 했습니다.

### Zeus, NIP-87 Mint 리뷰 작업 중

[Zeus](https://github.com/ZeusLN/zeus)는 [[NIP-87](/ko/topics/nip-87/) mint 리뷰를 위한 오픈 PR](https://github.com/ZeusLN/zeus/pull/3576)을 보유하고 있어, 사용자가 Nostr 팔로우로 필터링된 [Cashu](/ko/topics/cashu/) mint를 발견하고 리뷰할 수 있습니다. 리뷰에는 별점이 포함되며 익명으로 또는 사용자의 nsec로 제출할 수 있습니다.

### Camelus, 전체 DM 지원 출시

배터리 효율적인 모바일 성능을 위해 Dart NDK로 구축된 Flutter 기반 Android 클라이언트인 [Camelus](https://github.com/camelus-hq/camelus)는 이번 주 20개 이상의 커밋으로 포괄적인 다이렉트 메시징을 추가했습니다. 업데이트에는 채팅 카테고리, 메시지 날짜, 낙관적 전송 UI, 자신에게 노트 기능, 적절한 DM relay 처리가 포함됩니다.

### Marmot Protocol 업데이트

[지난주 오픈 PR로 다뤘던](/ko/newsletters/2026-01-21-newsletter/#marmot-protocol-white-noise-encrypted-group-chat-library) MIP-03 결정론적 커밋 해결이 이제 병합되었습니다. [MDK PR #152](https://github.com/marmot-protocol/mdk/pull/152)는 동일한 epoch에 대해 여러 유효한 커밋이 도착할 때 모든 [MLS](/ko/topics/mls/) 기반 그룹 채팅이 동일한 상태로 수렴하도록 보장합니다.

동반 [스펙 PR #28](https://github.com/marmot-protocol/marmot/pull/28)은 구현 감사에서 발견된 간극을 해결하는 init_key 수명 주기 요구 사항을 추가합니다: Welcome 메시지의 개인 키 자료는 처리 후 안전하게 삭제되어야 하며(영점화, 스토리지 정리), 새 멤버는 forward secrecy를 위해 24시간 이내에 자기 업데이트를 수행해야 합니다.

TypeScript SDK([marmot-ts](https://github.com/marmot-protocol/marmot-ts))는 참조 채팅 애플리케이션을 구축 중입니다. [PR #37](https://github.com/marmot-protocol/marmot-ts/pull/37)은 그룹 생성/목록, 게시/브로드캐스트/삭제 흐름이 포함된 키 패키지 관리, QR 코드 초대를 추가합니다. hzrd149의 [오픈 PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38)은 페이지네이션이 포함된 메시지 이력 지속성을 구현합니다. whitenoise-rs 백엔드는 다국어 지원([PR #455](https://github.com/marmot-protocol/whitenoise-rs/pull/455))과 MIP-04 v2 미디어 참조([PR #450](https://github.com/marmot-protocol/whitenoise-rs/pull/450))를 포함하여 이번 주 15개의 PR을 병합했습니다.

### diVine, Nostr 통합 기능 추가

짧은 동영상 앱인 [diVine](https://github.com/divinevideo/divine-mobile)은 빠른 Nostr 통합을 계속하고 있습니다.

최근 병합에는 [NIP-46](/ko/topics/nip-46/) QR 코드 인증([PR #1019](https://github.com/divinevideo/divine-mobile/pull/1019))과 [NIP-17](/ko/topics/nip-17/) 암호화 다이렉트 메시징([PR #834](https://github.com/divinevideo/divine-mobile/pull/834))이 포함됩니다. 이번 주 활동은 `nostr:` URI와 @멘션을 클릭 가능한 프로필 링크로 변환하는 [멘션 지원](https://github.com/divinevideo/divine-mobile/pull/1098), Nostr 프로필을 사용한 [Classic Viners 아바타 폴백](https://github.com/divinevideo/divine-mobile/pull/1097), [그리기](https://github.com/divinevideo/divine-mobile/pull/1056), [필터](https://github.com/divinevideo/divine-mobile/pull/1053), [스티커](https://github.com/divinevideo/divine-mobile/pull/1050)를 포함한 동영상 편집 도구에 집중했습니다.

## NIP 업데이트

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**오픈 PR과 논의:**

- **[Trusted Relay Assertions](https://github.com/nostr-protocol/nips/pull/1534)** - relay 신뢰도 점수 표준화를 위한 [지난주 다뤘던](/ko/newsletters/2026-01-21-newsletter/#nip-updates) 드래프트 제안이 논의를 계속합니다. 핵심 논쟁은 신뢰도 점수가 "전역"(모든 사용자에 대해 한 번 계산)이어야 하는지 "개인화"(각 관찰자의 소셜 그래프에 상대적)이어야 하는지에 집중됩니다. [nostr.band의 Trust Rank](https://trust.nostr.band/)와 [GrapeRank](https://github.com/Pretty-Good-Freedom-Tech/graperank-nodejs) 같은 PageRank 스타일 알고리즘은 가짜 계정을 통해 전달되는 순위를 봇 팜 크기로 나누어 시빌 공격에 저항합니다. 비평가들은 진정한 개인화 점수가 더 정확하지만 사용자별 비용이 많이 드는 계산이 필요하다고 주장합니다. 논의는 또한 클라이언트가 캐시할 수 있는 사전 계산된 kind 30382 증명 event 대신 온디맨드 점수 산정을 위해 DVM을 사용할지 여부를 탐구합니다.

- **Communikeys** - relay 기반 접근 방식 대신 기존 npub를 커뮤니티 식별자로 사용하는 커뮤니티 관리를 위한 [포괄적인 제안](https://nostrhub.io). 어떤 npub도 kind 10222 event를 게시하여 커뮤니티가 될 수 있습니다; 게시물은 kind 30222 event를 통해 커뮤니티를 대상으로 합니다. 접근 제어는 [NIP-58](/ko/topics/nip-58/) 배지를 사용하여 커뮤니티 키의 콜드 스토리지와 함께 위임된 멤버십 관리를 가능하게 합니다.

- **[NIP-CF: Changes Feed](https://njump.me/nevent1qqsyxrrdu09yktr7x5cqqrcj9v2hrqqqefem6f3stkrzwf8anr236sgcpzfmhxue69uhkummnw3ezu7nzvshxwec4wa0qn)** - 타임스탬프 기반 `since` 필터의 대안으로 시퀀스 기반 event 동기화를 제안하는 드래프트. 문제: `since` 타임스탬프를 사용하는 표준 Nostr 동기화는 여러 event가 동일한 초 정밀도 타임스탬프를 공유하거나, 클라이언트와 relay 시계가 어긋나거나, 체크포인트가 부정확할 때 event를 놓칠 수 있습니다. NIP-CF는 relay가 저장된 event에 단조 증가하는 시퀀스 번호를 할당하여 엄격한 전체 순서를 제공함으로써 이를 해결합니다. 클라이언트는 특정 시퀀스 번호 이후의 변경 사항을 요청하고 보장된 순서로 event를 수신하며, event를 절대 놓치지 않는 정확한 체크포인트를 제공합니다. 이 제안은 또한 초기 동기화 후 구독이 실시간 업데이트를 위해 열려 있는 라이브/연속 모드를 지원합니다.

- **[NIP-XX: Encrypted File Sync](https://njump.me/nevent1qqsr98tvcy7c4y5w03rd6cdujq9dpdt75uzv4kmkgpdlq7ggdmzptrqcpzfmhxue69uhkummnw3ezu7nzvshxwec4wa0qn)** - Nostr relay를 사용하여 기기 간에 암호화된 콘텐츠를 동기화하기 위한 kind 30800(암호화된 파일), 30801(볼트 인덱스), 30802(공유 문서)를 정의하는 프로토콜. 이 프로토콜은 로컬 퍼스트 노트 앱이 중앙 집중식 서버 없이 종단 간 암호화 동기화를 제공할 수 있게 합니다. 파일 내용, 경로, 이름, 폴더 구조가 모두 [NIP-44](/ko/topics/nip-44/) 자기 암호화를 사용하여 암호화되어, relay는 읽을 수 없는 blob을 저장합니다. 이미지와 같은 바이너리 첨부 파일은 클라이언트 측 암호화와 함께 [Blossom](/ko/topics/blossom/) 서버를 사용합니다. Kind 30802는 수신자의 공개 키로 암호화하여 사용자 간 문서 공유를 가능하게 합니다.

## Nostr 1월의 5년

[지난달 뉴스레터](/ko/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)는 fiatjaf의 첫 클라이언트 출시부터 Jack Dorsey의 촉매적 기부까지 Nostr의 12월 이정표를 추적했습니다. 이 회고록은 2021년부터 2025년까지 각 1월에 일어난 일을 검증된 기술 개발에 초점을 맞춰 기록합니다.

### 2021년 1월: 초기 개발

Nostr의 세 번째 달은 2020년 12월에 출시된 fiatjaf의 Vue.js 클라이언트인 Branle의 지속적인 개발을 보았습니다. 15명 미만으로 추정되는 소수의 얼리 어답터 그룹이 Telegram 그룹 [@nostr_protocol](https://t.me/nostr_protocol)(2020년 11월 16일 생성)을 통해 조율하며 하나 또는 두 개의 실험적 relay에서 프로토콜을 테스트했습니다. 커맨드라인 클라이언트 noscl은 터미널 기반 상호작용을 제공했습니다.

기술적 기반은 이미 고정되어 있었습니다: secp256k1 공개 키로 식별되는 사용자, Schnorr 서명으로 암호화 서명된 게시물, 서로 통신하지 않는 덤 스토리지 역할의 relay. 이것은 의도적으로 Bitcoin 네이티브 암호화였으며, 수년 후 채택 패턴을 형성할 설계 선택이었습니다.

### 2022년 1월: 개발자 발견

2022년 1월은 110포인트와 138개 댓글을 생성한 [첫 Hacker News 등장](https://news.ycombinator.com/item?id=29749061)(2021년 12월 31일)의 열기 속에서 시작되었습니다. 해당 게시물 당시, 전체 네트워크를 구동하는 relay는 약 7개에 불과했으며, 댓글 작성자들은 "nostr가 아주 새롭고 아무도 사용하지 않기 때문에 스팸은 아직 문제가 아니다"라고 언급했습니다. Robert C. Martin("Uncle Bob")은 Nostr를 "소셜 커뮤니케이션을 위한 최종 솔루션"이 될 가능성이 있다고 지지했습니다. 논의는 1월까지 계속되었고, 개발자들은 relay 아키텍처 대 진정한 P2P, 검열 저항 대 중재, 단순함이 확장될 수 있는지에 대해 토론했습니다.

HN 게시물은 새로운 구현의 물결을 촉발했습니다. Uncle Bob 자신이 1월 18일에 Clojure 데스크톱 클라이언트인 [more-speech](https://github.com/unclebob/more-speech)를 시작했습니다. fiatjaf의 [go-nostr](https://github.com/nbd-wtf/go-nostr) 라이브러리(2021년 1월 생성)와 [noscl](https://github.com/fiatjaf/noscl) 커맨드라인 클라이언트는 Go 도구를 제공했고, [nostr-tools](https://github.com/nbd-wtf/nostr-tools)는 JavaScript 지원을 제공했습니다. 2022년 12월까지 약 800개의 프로필이 바이오를 가지고 있었습니다. Branle은 개인 키 가져오기와 다중 relay 지원을 포함한 업데이트를 받으며 주요 웹 클라이언트로 남아 있었습니다. 기술적 과제는 분명했습니다: 64자 16진수 키는 직관적이지 않았고, 메시지 지연은 사용자를 좌절시켰으며, 커뮤니티는 아키텍처가 Twitter 규모의 트래픽을 처리할 수 있는지 의문을 제기했습니다.

### 2023년 1월: 폭발적 성장

2023년 1월은 Nostr를 실험에서 운동으로 변모시켰습니다. William Casarin(jb55)의 iOS 클라이언트인 Damus는 Apple의 App Store 승인 과정과 싸웠습니다. 1월 1일 거부, 1월 26일 다시 거부, 마침내 [1월 31일 승인](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store). 그 승인은 연쇄 반응을 일으켰습니다: Damus는 즉시 미국 소셜 네트워킹 10위에 올랐습니다. Jack Dorsey는 이를 "오픈 프로토콜의 이정표"라고 [평가했습니다](https://www.theblock.co/post/207448/nostr-based-decentralized-twitter-alternative-damus-goes-live-on-apple-app-store).

8일 전인 1월 23일, [Edward Snowden이 Nostr에서의 존재를 발표했습니다](https://x.com/Snowden/status/1617623779626352640): "Nostr의 멋진 점 중 하나는... 검열 저항 외에도 280자로 제한되지 않는다는 것입니다." NSA 내부 고발자의 지지는 프라이버시를 중시하는 커뮤니티에서 무게를 실었고, 사용자들은 즉시 Lightning을 통해 그에게 sats를 zap하기 시작했습니다.

웹 클라이언트들은 유입을 온보딩하기 위해 경쟁했습니다. 2022년 12월 kieran이 만든 [Snort](https://github.com/v0l/snort)는 기능이 풍부한 React 클라이언트로 부상했습니다; 1월 13일, Snort는 Nostr Plebs API를 통한 NIP-05 등록을 통합하여 새 사용자가 온보딩 중에 사람이 읽을 수 있는 신원을 주장할 수 있게 했습니다. Satoshi로부터 두 번째 Bitcoin 거래를 받은 초기 Bitcoin 기여자인 Martti Malmi가 풀타임으로 개발한 [Iris](https://iris.to)는 iris.to에서 무료 NIP-05 신원과 함께 웹 및 모바일 인터페이스를 모두 제공했습니다. monlovesmango가 Branle 포크로 Quasar(Vue.js)를 사용하여 구축한 [Astral](https://github.com/monlovesmango/astral)은 사용자가 게시 및 필터링을 위해 relay를 세트로 구성할 수 있는 relay 그룹화 기능으로 relay 관리에 집중했습니다. iOS 클라이언트용 TestFlight 베타는 몇 시간 만에 마감되었고, Amethyst가 Android를 장악했습니다.

인프라는 속도를 맞추기 위해 분주했습니다. 모든 relay는 자비를 들여 운영하는 열성팬들이 운영했습니다. Lightning 소액 결제를 사용하는 유료 relay는 자연스러운 스팸 필터링을 만들었지만 접근 장벽을 도입했습니다. [Damus는 승인 단 이틀 만에 중국 App Store에서 삭제되었습니다](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/), 보도에 따르면 중국 최고 인터넷 감시 기관의 요청에 따른 것이었습니다.

### 2024년 1월: 프로토콜 강화

2024년 1월은 프로토콜 표준화와 커뮤니티 구축에 집중했습니다. [Nostr PHX](https://www.nostrphx.com/events)는 1월 5일 Phoenix에서 지역 사이퍼펑크들을 모으는 밋업으로 한 해를 시작했습니다. 이것은 BTC Prague(6월), 리가의 Nostriga(8월), Nostrasia를 포함한 그해 많은 커뮤니티 이벤트 중 첫 번째였습니다.

가장 중요한 프로토콜 개발은 1월 29일에 병합된 [NIP-59 (Gift Wrap)](https://github.com/nostr-protocol/nips/pull/716)로, 암호화된 통신을 위한 메타데이터 보호를 제공했습니다. Gift Wrap은 relay로부터 발신자 신원을 숨기기 위해 [NIP-44의 암호화 표준](https://github.com/paulmillr/nip44)(2023년 12월 [Cure53에 의해 감사됨](https://cure53.de/audit-report_nip44-implementations.pdf)) 위에 구축됩니다. 이 프로토콜은 암호화된 메시지를 무작위의 일회용 키 쌍으로 서명된 외부 event 안에 래핑합니다. Relay는 일회용 pubkey만 보고, 실제 발신자의 신원은 수신자만 복호화할 수 있는 암호화된 페이로드 안에 묻혀 있습니다. 이는 relay 운영자와 네트워크 관찰자가 누가 누구에게 메시지를 보내는지 알 수 없게 합니다. 타임스탬프도 타이밍 분석을 무력화하기 위해 무작위화할 수 있습니다.

생태계는 소셜 미디어 너머로 확장되었습니다. [Plebeian Market](https://plebeian.market)은 [NIP-15](/ko/topics/nip-15/) 준수를 통해 완전한 Nostr 네이티브가 되어, 교차 상점 장바구니와 상인 발견을 위한 상점 브라우저를 가능하게 했습니다. [Shopstr](https://github.com/shopstr-eng/shopstr)는 Bitcoin 상거래를 촉진하는 무허가 마켓플레이스로 부상했습니다. kieran이 구축한 [Zap.stream](https://zap.stream/)은 분당 21 sats의 Lightning 결제와 함께 Nostr에 라이브 스트리밍을 가져왔습니다. 개발자 도구는 [NDK](https://github.com/nostr-dev-kit/ndk)가 TypeScript 추상화를 제공하고 [rust-nostr](https://github.com/rust-nostr/nostr)가 Rust 바인딩을 제공하면서 성숙해졌습니다. [Zeus v0.8.1](https://blog.zeusln.com/new-release-zeus-v0-8-1/)은 Nostr 연락처 가져오기와 영구 LND를 출시하여 이후 릴리스에서 Nostr Wallet Connect 통합의 기반을 마련했습니다.

그러나 인프라 지속 가능성은 [여전히 도전적이었습니다](https://arxiv.org/abs/2402.05709). 이 기간의 학술 연구에 따르면 relay의 95%가 운영 비용을 충당하는 데 어려움을 겪었으며, 20%가 상당한 다운타임을 경험했습니다. 유료 relay의 입장료는 평균 1,000 sats(약 $0.45) 미만으로 운영을 유지하기에 불충분했습니다.

*스캠에 대한 참고: 이 시기에 출시된 "Nostr Assets Protocol"과 관련 "$NOSTR" 토큰은 [fiatjaf에 의해 공개적으로 비난되어](https://www.aicoin.com/en/article/377704) 실제 Nostr 프로토콜과 아무런 연관이 없는 "100% 사기"이자 "친밀도 스캠"이라고 밝혀졌습니다.*

### 2025년 1월: 클라이언트 성숙

2025년 1월은 생태계 전반에 걸쳐 지속적인 클라이언트 개발을 보았습니다. [Nostur 1.17.0](https://www.nobsbitcoin.com/nostur-v1-17-0/)은 1월 13일 읽기 상태의 기기 간 동기화, [FROST](/ko/topics/frost/) 다중 서명 로그인 지원, 최적화된 로컬 데이터베이스 성능을 출시했습니다. Amethyst는 수동 구성 대신 팔로우 목록을 기반으로 relay 세트를 자동으로 컴파일하는 outbox 모델로의 전환을 계속했습니다.

주요 클라이언트들은 다이렉트 메시지를 위해 [NIP-04](/ko/topics/nip-04/)에서 벗어나 향상된 암호화와 메타데이터 보호를 위해 [NIP-17](/ko/topics/nip-17/)과 제안된 [NIP-104](/ko/topics/nip-104/)로 마이그레이션하기 시작했습니다. 생태계가 더 효율적인 relay 사용 패턴으로 수렴하면서 Gossip 모델(outbox/inbox 통신)이 채택을 얻었습니다. 업계 관찰자들은 올해가 Nostr가 틈새 프로토콜에서 주류 인식으로 전환하는 해가 될 것이라고 예측했으며, 일일 활동을 두 배로 늘릴 수 있는 잠재적인 고프로필 플랫폼 마이그레이션을 전망했습니다.

### 2026년 1월: 보안 및 서명 인프라

2026년 1월은 보안 및 서명 인프라에서 상당한 진전을 가져왔습니다. [Primal Android 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18)은 [NIP-46](/ko/topics/nip-46/) 원격 서명과 [NIP-55](/ko/topics/nip-55/) 로컬 서명자 지원을 출시하여, Amber 및 Aegis와 함께 다른 Android 앱을 위한 완전한 서명 허브에 합류했습니다. [Bitchat는 Cure53 보안 감사를 완료했습니다](https://github.com/permissionlesstech/bitchat/pulls), Signal과 NIP-44를 감사한 동일한 회사로, DH 비밀 지우기와 스레드 안전성 문제를 포함한 중요한 발견 사항을 수정하는 17개 이상의 PR이 있었습니다. Bitchat와 Damus 모두 향상된 신뢰성과 메모리 안전성을 위해 C Tor에서 Rust Arti로 마이그레이션했습니다.

프로토콜 작업은 [NIP-71](https://github.com/nostr-protocol/nips/pull/1669)(주소 지정 가능한 비디오 event)이 병합되고 양자 공격에 대한 Nostr의 미래 보장에 대한 논의를 여는 포스트 양자 암호화 NIP와 함께 계속되었습니다. Trusted Relay Assertions 드래프트는 서명된 증명을 통해 relay 신뢰도 점수를 표준화할 것을 제안했습니다. [Marmot Protocol](https://github.com/marmot-protocol/mdk)은 감사 발견 사항을 해결하는 18개의 병합된 PR로 [MLS](/ko/topics/mls/) 기반 암호화 메시징을 강화했습니다.

실제 응용 프로그램은 [Ridestr](https://github.com/variablefate/ridestr)가 [Cashu](/ko/topics/cashu/) 에스크로와 [NIP-44](/ko/topics/nip-44/) 암호화를 사용한 탈중앙화 라이드셰어링을 개발하고, [Pomade](https://github.com/coracle-social/pomade)가 [FROST](/ko/topics/frost/) 임계값 서명에 이메일 기반 복구 흐름을 추가하면서 확장되었습니다. Damus는 안정적인 DM 동기화를 위해 [negentropy](/ko/topics/negentropy/)를 출시했고, Amethyst의 데스크톱 앱은 검색, 북마크, zap과 함께 페이즈 2A에 도달했습니다.

### 앞으로

6년간의 1월은 Nostr의 진화를 보여줍니다: 초기 개발(2021)에서 대중적 발견(2022), 폭발적 성장(2023), 프로토콜 강화(2024), 클라이언트 성숙(2025), 보안 인프라(2026)까지. 이 패턴은 오픈 프로토콜의 성장을 지켜본 사람이라면 익숙할 것입니다: 수년간의 조용한 구축, 조건이 맞을 때 갑작스러운 폭발, 그 다음 모든 것을 신뢰할 수 있게 만드는 더 긴 작업. 7개의 relay와 Hacker News 스레드로 시작한 것이 이제 실제 응용 프로그램을 갖춘 감사된 인프라입니다. 2027년의 질문: 누군가가 라이드를 호출하고, 암호화된 메시지를 보내고, 또는 Nostr를 사용하여 분실된 키를 복구할 때, 그들은 Nostr를 사용하고 있다는 것을 알까요?

---

이번 주는 여기까지입니다. 무언가를 만들고 계신가요? 공유할 뉴스가 있나요? 프로젝트를 다뤄드릴까요? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DM으로 연락하시거나</a> Nostr에서 찾아주세요.
