---
title: 'Nostr Compass #2'
date: 2025-12-24
publishDate: 2025-12-24
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr 프로토콜 생태계에 대한 주간 가이드입니다.

**이번 주:** 세 가지 [NIP-55](/ko/topics/nip-55/) 서명자 구현이 업데이트를 받았습니다: Amber는 성능 캐싱을 추가하고, Aegis는 `nostrsigner:` URI 지원을 확보했으며, Primal Android가 완전한 로컬 서명자로 합류했습니다. Shopstr는 zaps를 통한 플래시 세일을 위한 "Zapsnags"를 도입했습니다. Mostro는 개발 펀드를 추가했습니다. 공개 메시지(kind 24)와 그룹 프라이버시 개선을 포함한 네 가지 NIP 업데이트가 도착했습니다. NDK 캐시 쿼리가 162배 빨라졌고, Applesauce가 리액션과 NIP-60 지갑 지원을 추가했으며, Tenex가 AI 에이전트 위임을 위한 RAL 아키텍처를 도입했습니다. 심층 분석에서는 소셜 타임라인과 대화를 구축하기 위한 기초 사양인 [NIP-02](/ko/topics/nip-02/)(팔로우 리스트)와 [NIP-10](/ko/topics/nip-10/)(답글 스레딩)을 설명합니다.

## 뉴스 {#news}

**Primal Android가 NIP-55 서명자가 됨** - 지난주의 [Nostr Connect 지원](/ko/newsletters/2025-12-17-newsletter/#primal-android)을 바탕으로, Primal은 8개의 병합된 풀 리퀘스트를 통해 완전한 로컬 서명 기능을 구현했습니다. 구현에는 Android의 콘텐츠 프로바이더 인터페이스를 통해 다른 Android 앱에 서명 작업을 노출하는 완전한 `LocalSignerContentProvider`가 포함되어 있으며, [NIP-55](/ko/topics/nip-55/) 사양을 따릅니다. 아키텍처는 관심사를 깔끔하게 분리합니다: `SignerActivity`는 사용자 대면 승인 흐름을 처리하고, `LocalSignerService`는 백그라운드 작업을 관리하며, 새로운 권한 시스템을 통해 사용자가 어떤 앱이 서명을 요청할 수 있는지 제어할 수 있습니다. 이로써 Primal은 다른 Nostr 경험을 위해 다른 앱을 사용하면서 키를 한 앱에 보관하려는 Android 사용자를 위한 Amber의 실행 가능한 대안이 되었습니다.

**Shopstr Zapsnags: Lightning을 통한 플래시 세일** - Nostr 네이티브 마켓플레이스가 ["Zapsnags"](https://github.com/shopstr-eng/shopstr/pull/211)를 도입했습니다. 구매자가 단일 zap으로 소셜 피드에서 직접 아이템을 구매할 수 있는 플래시 세일 기능입니다. 구현은 `#shopstr-zapsnag`으로 태그된 kind 1 노트를 필터링하고 표준 장바구니 흐름 대신 "Zap to Buy" 버튼이 있는 제품 카드로 렌더링합니다. 구매자가 zap을 보내면 시스템이 [NIP-57](/ko/topics/nip-57/)을 사용하여 결제 요청을 생성하고, kind 9735 zap 영수증을 폴링하여 결제를 확인한 다음, [NIP-17](/ko/topics/nip-17/) gift wrapping을 사용하여 배송 정보를 암호화한 후 판매자에게 비공개로 전송합니다. 이 기능은 반복 구매를 위해 구매자 세부 정보를 로컬에 저장하고 플래시 세일 리스팅 생성을 위한 판매자 대시보드를 포함합니다. 이는 Nostr의 조합 가능한 설계가 새로운 상거래 패턴을 가능하게 하는 방식을 보여주는 소셜, 결제, 프라이버시 프리미티브의 영리한 조합입니다.

**Mostro 개발 펀드 도입** - [NIP-69](/ko/topics/nip-69/) P2P Bitcoin 거래 플랫폼이 지속 가능한 유지보수를 지원하기 위해 [구성 가능한 개발 수수료를 구현](https://github.com/MostroP2P/mostro/pull/555)했습니다. 운영자는 Mostro 거래 수수료의 10-100%(기본값 30%) 사이에서 `dev_fee_percentage`를 설정할 수 있으며, 이는 각 성공적인 거래에서 개발 펀드로 자동 라우팅됩니다. 구현은 기여를 추적하기 위해 세 개의 데이터베이스 컬럼(`dev_fee`, `dev_fee_paid`, `dev_fee_payment_hash`)을 추가하고 데몬 시작 시 백분율을 검증합니다. [`docs/DEV_FEE.md`](https://github.com/MostroP2P/mostro/blob/main/docs/DEV_FEE.md)의 기술 문서가 시스템을 설명합니다. 이 옵트인 모델을 통해 운영자는 수수료 할당에 대한 완전한 투명성을 유지하면서 지속적인 개발을 지원할 수 있습니다.

## NIP 업데이트 {#nip-updates}

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**새로운 NIP:**
- **[NIP-A4](/ko/topics/nip-a4/) (공개 메시지, kind 24)** - 광범위한 클라이언트 지원을 목표로 설계된 알림 화면 메시지를 위한 새로운 kind ([#1988](https://github.com/nostr-protocol/nips/pull/1988)). 스레드 대화와 달리 이 메시지에는 채팅 기록이나 메시지 체인 개념이 없습니다. 스레딩 복잡성을 피하기 위해 `e` 태그 대신 `q` 태그(인용)를 사용하여 대화 상태를 생성하지 않고 수신자의 알림 피드에 나타나는 간단한 공개 알림에 이상적입니다.

**주요 변경 사항:**
- **[NIP-29](/ko/topics/nip-29/)** - 그룹 의미론의 주요 명확화 ([#2106](https://github.com/nostr-protocol/nips/pull/2106)). `closed` 태그는 이제 "쓰기 불가"(비회원에게 읽기 전용)를 의미하며, 가입 메커니즘과 분리되었습니다. 새로운 `hidden` 태그는 릴레이가 비회원에게 메타데이터나 멤버 이벤트를 제공하는 것을 방지하여 대역 외 초대 없이는 발견할 수 없는 진정한 비공개 그룹을 가능하게 합니다. `private` 태그는 검색을 위한 공개 메타데이터는 허용하면서 메시지 가시성을 제어합니다.
- **[NIP-51](/ko/topics/nip-51/)** - 큐레이션된 사진 세트를 위한 kind 30006 추가 ([#2170](https://github.com/nostr-protocol/nips/pull/2170)), 30004(기사)와 30005(비디오)의 패턴을 따릅니다. 이미 Nostria에서 구현되었습니다.
- **[NIP-55](/ko/topics/nip-55/)** - Android 서명자의 연결 시작에 대한 명확화 ([#2166](https://github.com/nostr-protocol/nips/pull/2166)). 다중 사용자 세션을 구현하는 개발자들이 백그라운드 프로세스에서 호출하여 `get_public_key`를 잘못 사용하고 있었습니다. 업데이트된 사양은 일반적인 구현 함정을 방지하기 위해 초기 연결 시에만 한 번 호출할 것을 권장합니다.

## NIP 심층 분석: NIP-02와 NIP-10 {#nip-deep-dive-nip-02-and-nip-10}

이번 주에는 소셜 기능에 필수적인 두 가지 NIP를 다룹니다: 클라이언트가 누구를 팔로우하는지 알고 대화가 스레드되는 방식입니다.

### [NIP-02](/ko/topics/nip-02/): 팔로우 리스트

[NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md)는 팔로우 리스트를 저장하는 kind 3 이벤트를 정의합니다. 이 간단한 메커니즘이 타임라인을 가능하게 하는 소셜 그래프를 구동합니다.

**구조:** kind 3 이벤트에는 팔로우한 pubkey를 나열하는 `p` 태그가 포함됩니다:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

각 `p` 태그에는 네 가지 위치가 있습니다: 태그 이름, 팔로우한 pubkey(hex), 선택적 릴레이 URL 힌트, 선택적 "petname"(로컬 닉네임). 릴레이 힌트는 다른 클라이언트에게 해당 사용자의 이벤트를 어디서 찾을 수 있는지 알려줍니다. petname을 사용하면 자체 선언된 표시 이름에 의존하지 않고 연락처에 기억하기 쉬운 이름을 지정할 수 있습니다.

**교체 가능 동작:** Kind 3은 교체 가능 범위(0, 3, 10000-19999)에 속하므로 릴레이는 pubkey당 최신 버전만 유지합니다. 새 사람을 팔로우하면 클라이언트가 기존의 모든 팔로우와 새 팔로우를 포함하는 완전히 새로운 kind 3을 게시합니다. 즉, 팔로우 리스트는 매번 완전해야 하며 증분 업데이트를 게시할 수 없습니다.

**타임라인 구축:** 홈 피드를 구성하기 위해 클라이언트는 사용자의 kind 3을 가져와 모든 `p` 태그 pubkey를 추출한 다음 해당 작성자의 kind 1 이벤트를 구독합니다:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

릴레이가 일치하는 노트를 반환하면 클라이언트가 렌더링합니다. kind 3의 릴레이 힌트는 클라이언트가 각 팔로우한 사용자에 대해 어떤 릴레이를 쿼리할지 알 수 있게 도와줍니다.

**Petname과 신원:** petname 필드는 탈중앙화된 명명 체계를 가능하게 합니다. 사용자가 프로필에서 주장하는 이름을 신뢰하는 대신 자신만의 레이블을 지정할 수 있습니다. 클라이언트는 "alice (내 동생)"처럼 표시할 수 있으며, 여기서 "alice"는 그녀의 kind 0 프로필에서 가져오고 "내 동생"은 당신의 petname입니다. 이는 전역 사용자 이름이 제공할 수 없는 맥락을 제공합니다.

**실용적 고려 사항:** kind 3 이벤트는 교체 가능하고 완전해야 하므로 클라이언트는 업데이트 시 알 수 없는 태그를 보존해야 합니다. 다른 클라이언트가 당신의 클라이언트가 이해하지 못하는 태그를 추가한 경우, 맹목적으로 덮어쓰면 해당 데이터가 손실됩니다. 처음부터 다시 구축하지 말고 새 팔로우를 추가하세요.

### [NIP-10](/ko/topics/nip-10/): 텍스트 노트 스레딩

[NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md)은 kind 1 노트가 서로 참조하여 답글 스레드를 형성하는 방법을 지정합니다. 대화 뷰를 구축하는 데 이해가 필수적입니다.

**문제:** 누군가 노트에 답글을 달 때 클라이언트는 알아야 합니다: 무엇에 대한 답글인가? 대화의 루트는 무엇인가? 누구에게 알려야 하는가? NIP-10은 `e` 태그(이벤트 참조)와 `p` 태그(pubkey 멘션)를 통해 이러한 질문에 답합니다.

**마킹된 태그 (권장):** 현대 클라이언트는 `e` 태그에 명시적 마커를 사용합니다:

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "좋은 지적이에요! 동의합니다.",
  "sig": "b7d3f..."
}
```

`root` 마커는 스레드를 시작한 원래 노트를 가리킵니다. `reply` 마커는 답변하는 특정 노트를 가리킵니다. 루트에 직접 답글하는 경우 `root`만 사용합니다(`reply` 태그 필요 없음). 이 구분은 렌더링에 중요합니다: `reply`는 스레드 뷰에서 들여쓰기를 결정하고, `root`는 모든 답글을 함께 그룹화합니다.

**스레딩 규칙:**
- **루트에 직접 답글:** `root` 마커가 있는 `e` 태그 하나
- **답글에 대한 답글:** `root` 하나와 `reply` 하나로 두 개의 `e` 태그
- `root`는 스레드 전체에서 일정하게 유지됩니다; `reply`는 응답하는 대상에 따라 변경됩니다

**알림을 위한 Pubkey 태그:** 알림을 받아야 하는 모든 사람에 대해 `p` 태그를 포함합니다. 최소한 답글하는 노트의 작성자를 태그하세요. 관례적으로 부모 이벤트의 모든 `p` 태그도 포함합니다(대화의 모든 사람이 계속 알 수 있도록), 그리고 콘텐츠에서 @멘션하는 모든 사용자도 포함합니다.

**릴레이 힌트:** `e` 및 `p` 태그의 세 번째 위치에는 해당 이벤트나 사용자의 콘텐츠를 찾을 수 있는 릴레이 URL이 포함될 수 있습니다. 이는 클라이언트가 원래 릴레이에 연결되어 있지 않아도 참조된 콘텐츠를 가져오는 데 도움이 됩니다.

**더 이상 사용되지 않는 위치 기반 태그:** 초기 Nostr 구현은 마커가 아닌 태그 위치에서 의미를 유추했습니다: 첫 번째 `e` 태그가 루트, 마지막이 답글, 중간이 멘션이었습니다. 이 접근 방식은 모호성을 만들기 때문에 더 이상 사용되지 않습니다. 마커 없는 `e` 태그가 보이면 오래된 클라이언트에서 온 것일 가능성이 높습니다. 현대 구현은 항상 명시적 마커를 사용해야 합니다.

**스레드 뷰 구축:** 스레드를 표시하려면 루트 이벤트를 가져온 다음 해당 루트를 참조하는 `e` 태그가 있는 모든 이벤트를 쿼리합니다:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

`created_at`으로 결과를 정렬하고 `reply` 마커를 사용하여 트리 구조를 구축합니다. `reply`가 루트를 가리키는 이벤트는 최상위 답글입니다; `reply`가 다른 답글을 가리키는 이벤트는 중첩된 응답입니다.

## 릴리스 {#releases}

**Zeus v0.12.0** - 지난주의 [NWC 병렬 결제 지원](/ko/newsletters/2025-12-17-newsletter/#zeus-lightning-wallet)을 바탕으로, Lightning 지갑의 [주요 릴리스](https://github.com/ZeusLN/zeus/releases/tag/v0.12.0)가 커스텀 릴레이 지원과 예산 추적이 포함된 완전한 [NIP-47](/ko/topics/nip-47/) Nostr Wallet Connect 서비스를 제공합니다. [예산 리로드 수정](https://github.com/ZeusLN/zeus/pull/3455)으로 연결이 현재 제한을 사용하도록 보장합니다. [Lightning 주소 복사](https://github.com/ZeusLN/zeus/pull/3460)가 더 이상 `lightning:` 접두사를 포함하지 않아 Nostr 프로필 필드에 붙여넣기 문제를 수정합니다.

**Amber v4.0.6** - Android [NIP-55](/ko/topics/nip-55/) 서명자가 서명 작업에 [성능 캐싱을 추가](https://github.com/greenart7c3/Amber/releases/tag/v4.0.6)하고 잘못된 콘텐츠 복호화 시 오류 처리를 개선했습니다. 릴레이 연결 이벤트에 대한 재시도 로직으로 연결 신뢰성이 향상되었고, 여러 충돌 수정이 잘못된 `nostrconnect://` URI와 권한 화면 상호작용에 관한 엣지 케이스를 해결합니다.

**nak v0.17.3** - 명령줄 Nostr 도구의 [최신 릴리스](https://github.com/fiatjaf/nak/releases/tag/v0.17.3)가 LMDB 빌드를 Linux로 제한하여 크로스 플랫폼 컴파일 문제를 수정합니다.

**Aegis v0.3.4** - 크로스 플랫폼 Nostr 서명자가 [NIP-55](/ko/topics/nip-55/)에 정의된 `nostrsigner:` URI 스킴 [지원을 추가](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.4)하여 Amber의 연결 흐름과 일치합니다. 이제 로컬 릴레이 데이터를 백업용으로 가져오고 내보낼 수 있으며, 릴리스에는 릴레이 소켓 오류에 대한 버그 수정과 로컬 릴레이 인터페이스의 UI 개선이 포함됩니다.

## 주목할 만한 코드 및 문서 변경 {#notable-code-and-documentation-changes}

*이것들은 오픈 풀 리퀘스트와 초기 단계 작업으로, 병합 전에 피드백을 받기에 완벽합니다. 관심이 가는 것이 있다면 리뷰하거나 댓글을 달아보세요!*

### Damus (iOS) {#damus}

[뮤트 리스트 지속성](https://github.com/damus-io/damus/pull/3469)이 콜드 스타트 시 뮤트 리스트가 지워지는 문제를 수정합니다. 수정은 앱 초기화 중 실수로 덮어쓰는 것을 방지하는 가드를 추가합니다. [프로필 스트림 타이밍](https://github.com/damus-io/damus/pull/3457)이 캐시된 프로필이 나타나기 전의 약 1초 지연을 제거합니다. 이전에는 뷰가 구독 작업이 다시 시작될 때까지 기다렸습니다; 이제 `streamProfile()`이 NostrDB에서 캐시된 데이터를 즉시 반환하여 축약된 pubkey와 플레이스홀더 이미지가 표시되는 창을 제거합니다.

### White Noise (암호화 메시징) {#white-noise}

[실시간 메시지 스트리밍](https://github.com/marmot-protocol/whitenoise/pull/919)이 이전 폴링 메커니즘을 스트림 기반 아키텍처로 대체합니다. 새로운 `ChatStreamNotifier`는 Rust SDK의 메시지 스트림을 직접 소비하여 시간순 순서를 유지하고 증분 업데이트를 효율적으로 처리합니다. 테스트에서 응답성이 크게 향상되었습니다. [채팅 리스트 API](https://github.com/marmot-protocol/whitenoise/pull/921)가 대화 요약 검색을 위한 `get_chat_list`를 추가하고, [안정적인 정렬 수정](https://github.com/marmot-protocol/whitenoise/pull/905)이 `createdAt`과 메시지 ID를 타이브레이커로 사용하여 메시지 재정렬 루프를 방지합니다.

### NDK (라이브러리) {#ndk}

두 개의 풀 리퀘스트가 극적인 캐시 성능 향상을 제공했습니다. [PR #371](https://github.com/nostr-dev-kit/ndk/pull/371)이 SQLite 캐시에서 읽은 이벤트가 즉시 다시 쓰여지는 버그를 수정하여 앱 부팅 시 100% 중복 쓰기가 발생했습니다. 수정은 `fromCache` 가드를 추가하고 인메모리 Set을 통한 O(1) 중복 검사를 구현합니다. 작은 결과 집합(<100 이벤트)의 경우 직접 JSON 전송이 바이너리 인코딩 오버헤드를 대체합니다. [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372)가 캐시된 이벤트에 대한 불필요한 `seenEvent` 호출을 제거했습니다. LRU 캐시 조회에 이벤트당 0.24-0.64ms가 소요되었습니다; 5,700개의 캐시된 이벤트에 대해 약 1.4초의 오버헤드가 추가되었습니다. 결과: 캐시 쿼리가 약 3,690ms에서 약 22ms로 감소(162배 빨라짐).

### rust-nostr (라이브러리) {#rust-nostr}

[다중 필터 REQ 지원](https://github.com/rust-nostr/nostr/pull/1176)이 이전 리팩터링에서 제거된 후 복원되었습니다. SDK가 다시 구독 요청에 대해 `Vec<Filter>`를 수용하여 OR 논리로 여러 필터 조건을 결합하는 효율적인 쿼리를 가능하게 합니다. [릴레이 출처](https://github.com/rust-nostr/nostr/pull/1156)가 `stream_events*` 메서드에 추가되어 각 스트리밍된 이벤트에 이제 출처 `RelayUrl`과 성공 또는 실패를 나타내는 `Result`가 포함되어 릴레이 신뢰성 추적과 연결 문제 디버깅에 유용합니다. [보안 수정](https://github.com/rust-nostr/nostr/pull/1179)이 RUSTSEC-2024-0421에 따라 `url-fork` 의존성을 제거하여 알려진 취약점을 제거했습니다.

### Applesauce (라이브러리) {#applesauce}

[noStrudel](https://github.com/hzrd149/nostrudel)을 구동하는 TypeScript 라이브러리가 이번 주에 상당한 개발을 보았습니다. 새로운 모델에는 [리액션 시스템](https://github.com/hzrd149/applesauce)과 사용자 그룹 캐스팅이 포함됩니다. 지갑 기능이 NIP-60 지원, 전송 탭, 개선된 토큰 복구 도구로 확장되었습니다. 새로운 `user.directMessageRelays$` 속성이 DM 릴레이 구성을 노출합니다. 모든 액션이 비동기 인터페이스를 사용하도록 리팩터링되었고(비동기 제너레이터 제거), 버그 수정이 암호화된 콘텐츠 복원 및 시간 기반 이벤트 필터 엣지 케이스를 해결했습니다.

### Tenex (AI 에이전트) {#tenex}

Nostr에 구축된 [다중 에이전트 조정 시스템](https://github.com/tenex-chat/tenex)이 [다섯 개의 병합된 PR](https://github.com/pablof7z/tenex/pull/38)에서 RAL(Request-Action-Lifecycle) 아키텍처를 도입했습니다. RAL은 에이전트가 작업을 위임할 때 일시 중지하고 결과가 도착하면 재개할 수 있게 하며, 대화 범위 상태 지속성을 제공합니다. 위임 도구(`delegate`, `ask`, `delegate_followup`, `delegate_external`)가 이제 Nostr 이벤트를 게시하고 차단 대신 중지 신호를 반환합니다. 리팩터링에는 AI SDK v6 마이그레이션, 결정론적 LLM 상호작용 기록을 위한 VCR 테스팅 인프라, 멀티모달 이미지 지원이 포함됩니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 계신가요? 공유할 뉴스가 있으신가요? 프로젝트를 다뤄주길 원하시나요? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DM으로 연락하세요</a> 또는 Nostr에서 찾아주세요.

