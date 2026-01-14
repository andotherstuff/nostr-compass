---
title: 'Nostr Compass #5'
date: 2026-01-13
publishDate: 2026-01-13
draft: false
type: newsletters
---

Nostr Compass에 다시 오신 것을 환영합니다. Nostr를 위한 주간 가이드입니다.

**이번 주:** Bitchat이 Signal과 [NIP-44](/ko/topics/nip-44/)를 감사한 것으로 유명한 Cure53의 전문 보안 감사를 받았으며, 중요한 발견 사항을 수정하는 17개 이상의 PR이 이미 병합되었습니다. [NIP-71](/ko/topics/nip-71/)이 병합되어 프로토콜에 주소 지정 가능한 비디오 event가 도입되었습니다. 양자 후 암호화 NIP가 Nostr를 양자 공격으로부터 미래 대비하는 것에 대한 논의를 시작했습니다. Amethyst v1.05.0은 북마크 목록, 음성 메모, 초기 데스크톱 릴리스를 제공하며, Nostur v1.25.3은 반응 및 답글을 통해 [NIP-17](/ko/topics/nip-17/) DM을 개선합니다. 라이브러리 소식으로는 rust-nostr가 SQLite 및 LMDB 백엔드 전반에 걸쳐 [NIP-62](/ko/topics/nip-62/) 지원을 확장하고, NDK가 구독 추적 버그를 수정했습니다.

## 뉴스

### Bitchat, Cure53 보안 감사 완료

Nostr와 Cashu를 결합한 iOS 암호화 메신저인 Bitchat이 업계에서 가장 존경받는 보안 회사 중 하나인 Cure53의 전문 보안 감사를 받았습니다. Cure53은 이전에 Signal, Mullvad VPN, 그리고 특히 현대 Nostr 비공개 메시징의 기반이 되는 [NIP-44](/ko/topics/nip-44/) 암호화 사양을 감사했습니다.

감사에서 12개 이상의 보안 문제(BCH-01-002부터 BCH-01-013까지)가 발견되었습니다. Bitchat 팀은 17개 이상의 pull request로 대응했습니다. 주요 수정 사항은 다음과 같습니다:

**Noise Protocol DH Secret Clearing** - [PR #928](https://github.com/permissionlesstech/bitchat/pull/928)은 키 합의 후 Diffie-Hellman 공유 비밀이 0으로 초기화되지 않던 6개 위치를 수정하여 순방향 비밀성 보장을 복원합니다. 비밀이 필요 이상으로 오래 메모리에 남아 있으면, 메모리 덤프나 콜드 부트 공격이 과거 통신을 침해할 수 있습니다.

**서명 검증** - 여러 PR이 암호화 검증 경로를 강화하여 잘못된 입력을 통해 메시지 인증 검사를 우회할 수 없도록 합니다.

**스레드 안전성** - [PR #929](https://github.com/permissionlesstech/bitchat/pull/929)는 NostrTransport의 읽음 확인 큐에 배리어 동기화를 추가하여 높은 메시지 볼륨에서 데이터 손상이나 충돌을 일으킬 수 있는 경쟁 조건을 방지합니다.

**메모리 안전성** - [PR #920](https://github.com/permissionlesstech/bitchat/pull/920)은 높은 메시지 처리량에서 더 나은 성능을 위해 메시지 중복 제거기를 최적화하면서 메모리 고갈을 방지합니다.

**입력 유효성 검사** - [PR #919](https://github.com/permissionlesstech/bitchat/pull/919)는 잘못된 입력으로 인한 충돌을 방지하기 위해 16진수 문자열 파싱을 강화합니다. 이는 서비스 거부 공격의 일반적인 공격 벡터입니다.

Bitchat은 Cashu ecash를 처리하므로 전문적인 보안 검토가 필수적입니다. 이번 감사는 작년의 [Marmot](/ko/topics/marmot/) Protocol 감사와 암호화 계층을 검증한 NIP-44 감사에 이은 것입니다.

## NIP 업데이트

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**병합됨:**

- **[NIP-71](/ko/topics/nip-71/)** - 주소 지정 가능한 비디오 Event ([#1669](https://github.com/nostr-protocol/nips/pull/1669))는 주소 지정 가능한 event로 kind 34235(가로 비디오)와 34236(세로 비디오)을 도입합니다. 필수 `d` 태그는 고유 식별자를 제공하므로 전체 event를 다시 게시하지 않고도 비디오 메타데이터를 업데이트할 수 있습니다. 선택적 `origin` 태그는 가져오기 소스를 추적합니다. 이미 Amethyst와 nostrvine에 구현되어 있습니다.

**열린 PR:**

- **양자 후 암호화** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185)는 Nostr에 양자 저항 암호화 알고리즘을 추가할 것을 제안합니다. 이 사양은 개별 사용자가 아닌 애플리케이션 및 권한과 같은 "초고가치 event"를 대상으로 디지털 서명을 위한 ML-DSA-44와 Falcon-512를 도입합니다. [NIP-44](/ko/topics/nip-44/)의 대칭 암호화(ChaCha20)는 양자 저항성이 있지만, 키 교환은 Shor 알고리즘에 취약한 secp256k1 ECDH를 사용합니다. 이 제안은 이 격차를 해결하기 위해 키 합의를 위한 ML-KEM을 포함합니다. 이것은 Nostr의 장기 보안을 위한 암호화 민첩성에 대한 논의를 시작하는 초기 단계 제안입니다.
- **NIP-47용 BOLT12** - 137개의 댓글과 광범위한 논의 끝에, 커뮤니티는 BOLT12 offer가 [NIP-47](/ko/topics/nip-47/)을 확장하는 것보다 자체 사양을 갖는 것이 좋다고 결정했습니다. BOLT12 offer는 재사용 가능성, 블라인드 경로를 통한 더 나은 프라이버시, 선택적 지불자 정보를 포함하여 BOLT11 인보이스보다 상당한 업그레이드를 제공합니다. 새 NIP는 Nostr Wallet Connect 구현을 위한 `make_offer`, `pay_offer`, `list_offers`와 같은 메서드를 정의할 것입니다.
- **오디오 트랙 NIP** - [PR #1043](https://github.com/nostr-protocol/nips/pull/1043)은 음악 트랙을 위한 kind 32100과 팟캐스트 에피소드를 위한 32101을 제안하여 오디오 콘텐츠에 NIP-71이 비디오에 제공하는 것과 동일한 일급 대우를 부여합니다. 현재 Wavlake, Zapstr, Stemstr와 같은 오디오 플랫폼은 각각 독점 event 형식을 사용하여 생태계를 분열시키고 있습니다. 공통 표준은 사용자가 호환 가능한 클라이언트에서 오디오를 발견하고 재생할 수 있도록 상호 운용성을 가능하게 합니다.
- **NIP-A3 범용 결제 대상** - [PR #2119](https://github.com/nostr-protocol/nips/pull/2119)는 RFC-8905 `payto:` URI를 사용하여 여러 네트워크에서 결제 옵션을 노출하는 kind 10133 event를 제안합니다. Bitcoin, Lightning, Cashu 또는 기존 결제 레일에 대해 별도의 event kind를 만드는 대신, 이 추상화를 통해 클라이언트는 표준화된 태그를 파싱하고 네이티브 결제 핸들러를 호출할 수 있습니다. 새로운 결제 방법은 `payto:` URI 스킴만 필요하므로 이 접근 방식은 미래 지향적입니다.

## NIP 심층 분석: NIP-51과 NIP-65

이번 주에는 사용자 기본 설정을 저장하는 두 가지 NIP를 다룹니다: 콘텐츠 구성을 위한 NIP-51과 relay 연결 구성을 위한 NIP-65. 둘 다 교체 가능한 event를 사용하며, 이는 각 새 게시가 이전 버전을 덮어쓴다는 것을 의미합니다.

### [NIP-51](/ko/topics/nip-51/): 목록

[NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md)은 event, 사용자, 해시태그 및 기타 콘텐츠에 대한 참조를 구성하기 위한 여러 목록 유형을 정의합니다. Amethyst v1.05.0이 북마크 지원을 추가하여 목록 작동 방식을 이해하기 좋은 시기입니다.

사양은 각각 다른 목적을 수행하는 여러 목록 kind를 정의합니다. Kind 10000은 사용자, 스레드 또는 단어를 숨기기 위한 뮤트 목록입니다. Kind 10001은 프로필에 표시할 event를 고정합니다. Kind 30003은 북마크를 저장하며, 이것이 Amethyst가 이제 지원하는 것입니다. 다른 kind는 팔로우 세트(30000), 큐레이션된 기사 컬렉션(30004), 해시태그 관심사(30015), 사용자 정의 이모지 세트(30030)를 처리합니다.

목록은 태그를 통해 콘텐츠를 참조합니다. 북마크 목록은 특정 event에 대해 `e` 태그를 사용하고 기사와 같은 주소 지정 가능한 콘텐츠에 대해 `a` 태그를 사용합니다:

```json
{
  "id": "ae3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 30003,
  "tags": [
    ["d", "saved-articles"],
    ["e", "abc123def456...", "wss://relay.example"],
    ["a", "30023:author-pubkey:article-id", "wss://relay.example"]
  ],
  "content": "<encrypted-private-bookmarks>",
  "sig": "908a15e46fb4d8675bab026fc230a0e3542bfade63da02d542fb78b2a8513fcd0092619a2c8c1221e581946e0191f2af505dfdf8657a414dbca329186f009262"
}
```

`d` 태그는 고유 식별자를 제공하므로 동일한 kind에서 "saved-articles", "read-later" 또는 "favorites"와 같은 여러 북마크 세트를 유지할 수 있습니다.

목록은 공개 항목과 비공개 항목을 모두 지원합니다. 공개 항목은 태그 배열에 나타나며 event를 가져오는 누구에게나 표시됩니다. 비공개 항목은 `content` 필드에 들어가며 [NIP-44](/ko/topics/nip-44/)를 사용하여 자신에게 암호화됩니다. 이 이중 구조를 통해 공개 북마크를 유지하면서 비공개 메모를 첨부하거나, 누구를 뮤트했는지 공개하지 않고 뮤트 목록을 유지할 수 있습니다. 자신에게 암호화하려면 자신의 pubkey를 수신자로 하여 NIP-44를 사용하세요.

10000 시리즈 kind는 교체 가능하며, 이는 relay가 pubkey당 하나의 event만 유지한다는 것을 의미합니다. 30000 시리즈는 매개변수화된 교체 가능으로, pubkey와 `d` 태그 조합당 하나의 event를 허용합니다. 두 경우 모두 목록을 업데이트한다는 것은 완전한 교체를 게시하는 것을 의미합니다. 증분 변경을 보낼 수 없습니다. 클라이언트는 다른 애플리케이션에서 추가한 데이터를 덮어쓰지 않도록 목록을 수정할 때 알 수 없는 태그를 보존해야 합니다.

### [NIP-65](/ko/topics/nip-65/): Relay 목록 메타데이터

[NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md)는 사용자가 읽기 및 쓰기에 선호하는 relay를 광고하는 kind 10002 event를 정의합니다. 이것은 다른 사용자와 클라이언트가 귀하의 콘텐츠를 찾는 데 도움이 됩니다.

```json
{
  "id": "bd2217a96b5835b59f9a6a42d8d8a36f8c9b7d4e5f0a1b2c3d4e5f6a7b8c9d0e1",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "f1c2d3e4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2"
}
```

각 `r` 태그는 relay URL과 선택적 마커를 포함합니다. `write` 마커는 귀하의 outbox를 지정합니다: 귀하가 콘텐츠를 게시하는 relay입니다. `read` 마커는 귀하의 inbox를 지정합니다: 멘션, 답글 및 태그를 확인하는 relay입니다. 마커를 생략하면 둘 다를 나타냅니다.

Alice가 Bob의 게시물을 찾으려면, 그녀의 클라이언트는 Bob의 kind 10002를 가져와서 그의 write relay(그의 outbox)를 추출하고 거기서 구독합니다. Alice가 Bob에게 답글을 달면, 그녀의 클라이언트는 그가 멘션을 볼 수 있도록 그의 read relay(그의 inbox)에 게시합니다. 이 relay 인식 라우팅은 "outbox 모델"이며, 몇몇 중앙 서버에 모두를 집중시키는 대신 많은 relay에 사용자를 분산시킵니다.

NIP-65는 공개 콘텐츠 라우팅을 처리하지만, 비공개 메시지는 별도의 목록을 사용합니다. [NIP-17](/ko/topics/nip-17/)은 `r` 태그 대신 `relay` 태그를 사용하여 DM inbox relay를 위한 kind 10050을 정의합니다. 누군가에게 비공개 메시지를 보낼 때, 클라이언트는 수신자의 kind 10050 event를 찾아 거기에 암호화된 gift-wrapped 메시지를 게시합니다. 이 분리는 DM 라우팅을 공개 콘텐츠 라우팅과 구별하고, 사용자가 비공개 대 공개 통신에 다른 relay를 지정할 수 있게 합니다.

outbox 모델은 단일 relay가 모든 사람의 콘텐츠를 저장하거나 제공할 필요가 없기 때문에 검열 저항성을 향상시킵니다. 클라이언트는 팔로우하는 사용자의 NIP-65 event에 나열된 relay에 대한 연결을 유지하며, 새 계정을 발견하면 동적으로 새 relay에 연결합니다. NIP-65는 다른 NIP에서 발견되는 relay 힌트를 보완합니다. `["p", "pubkey", "wss://hint.relay"]`로 누군가를 태그하면, 힌트는 클라이언트에게 해당 특정 참조를 어디서 찾아야 하는지 알려줍니다. NIP-65는 권위 있는 사용자 제어 목록을 제공하고, 힌트는 개별 event에 포함된 바로가기를 제공합니다.

최상의 결과를 위해 relay 목록을 최신 상태로 유지하세요. 오래된 항목은 당신을 찾기 어렵게 만듭니다. 사양에서는 카테고리당 2~4개의 relay를 권장합니다. 너무 많은 relay를 나열하면 귀하의 콘텐츠를 가져오려는 모든 클라이언트에 부담을 주어 경험을 느리게 하고 네트워크 부하를 증가시킵니다. 클라이언트는 NIP-65 event를 캐시하고 사용자가 기본 설정을 업데이트함에 따라 정기적으로 새로 고침합니다.

## 릴리스

**Amethyst v1.05.0** - 인기 있는 Android 클라이언트가 여러 주요 기능을 포함한 [주요 업데이트를 출시했습니다](https://github.com/vitorpamplona/amethyst/releases). [NIP-51](/ko/topics/nip-51/) kind 30003 북마크 목록을 통해 사용자는 나중에 참조할 게시물을 저장하고 호환 클라이언트 간에 동기화할 수 있습니다. 음성 메모는 이제 파형 시각화, 미디어 서버 선택 및 업로드 진행률 표시기와 함께 DM 및 일반 게시물에서 작동합니다. [Web of Trust](/ko/topics/web-of-trust/) 점수가 이제 인터페이스에 표시되어 사용자가 알고리즘이 자신의 소셜 그래프를 기준으로 계정을 어떻게 평가하는지 이해하는 데 도움이 됩니다. [Quartz](/ko/topics/quartz/) 데이터베이스 마이그레이션은 OpenSats 자금 지원 Kotlin Multiplatform 작업의 일환으로 쿼리 성능을 향상시킵니다. 초기 데스크톱 릴리스는 Android 앱과 동일한 코드베이스를 공유하면서 Compose Multiplatform을 통해 Amethyst를 Windows, macOS 및 Linux로 가져옵니다. 새로운 사용자 온보딩 흐름은 처음 Nostr 사용자를 위한 경험을 매끄럽게 합니다.

**Nostur v1.25.3** - iOS 및 macOS 클라이언트가 [NIP-17](/ko/topics/nip-17/) 개선 사항과 함께 [비공개 메시징에 집중합니다](https://github.com/nostur-com/nostur-ios-public/releases). DM 대화는 이제 반응과 답글을 지원하여 공개 게시물의 상호 작용성을 암호화된 메시지에 도입합니다. 대화 보기가 더 나은 스레딩으로 재작업되어 다중 메시지 교환을 더 쉽게 따라갈 수 있으며, DM 목록에 "시간 전" 타임스탬프가 표시되어 빠른 스캔이 가능합니다. 데스크톱 사용자는 여러 피드나 대화를 나란히 보기 위한 다중 열 레이아웃을 얻습니다. [NIP-46](/ko/topics/nip-46/) 원격 서명자 지원을 통해 사용자는 Amber나 nsec.app과 같은 전용 서명자 앱에 개인 키를 보관할 수 있습니다. 추가 수정 사항은 iOS 15 및 iOS 16에서 DM 기능을 복원하고, 알림 지연을 해결하며, 게시된 DM을 수신하는 relay를 구성하는 기능을 추가합니다.

## 주목할 만한 코드 및 문서 변경 사항

*이것들은 열린 pull request와 초기 단계 작업으로, 병합되기 전에 피드백을 받기에 완벽합니다. 눈에 띄는 것이 있다면 리뷰하거나 댓글을 달아보세요!*

### Citrine (Android Relay)

[PR #89](https://github.com/greenart7c3/Citrine/pull/89)는 Android 개인 relay 앱의 SQL 인젝션 취약점을 수정합니다. 이 문제로 인해 잘못된 event 데이터가 임의의 데이터베이스 쿼리를 실행할 수 있었으며, 이는 신뢰할 수 없는 입력을 저장하고 처리하는 모든 앱에 심각한 결함입니다. 수정 사항은 매개변수화된 쿼리를 사용하여 모든 데이터베이스 작업을 적절히 살균합니다. 아직 릴리스가 태그되지 않았으므로 사용자는 다음 버전을 기다리거나 소스에서 빌드해야 합니다. [PR #90](https://github.com/greenart7c3/Citrine/pull/90)은 데이터베이스 수준 필터링 및 페이지네이션으로 ContentProvider 쿼리 성능을 최적화하여 Amethyst와 같은 외부 앱이 Android의 프로세스 간 통신 계층을 통해 Citrine의 event 데이터베이스에 액세스할 때 지연 시간을 줄입니다.

### rust-nostr (라이브러리)

[NIP-62](/ko/topics/nip-62/) (Vanish Requests) 지원이 rust-nostr의 데이터베이스 백엔드 전반에 확장되고 있습니다. 2주 전에 병합된 [PR #1180](https://github.com/rust-nostr/nostr/pull/1180)은 SQLite에 NIP-62 지원을 추가했으며, 데이터베이스 계층이 특정 relay URL을 알지 못하므로 `ALL_RELAYS` vanish 요청을 처리합니다. [PR #1210](https://github.com/rust-nostr/nostr/pull/1210)은 이를 LMDB 백엔드로 확장하여 vanish 요청이 디스크에 지속되고 relay 재시작 후에도 유지되도록 합니다. 브라우저 환경을 위한 IndexedDB 구현도 진행 중입니다. 이러한 변경 사항을 통해 개발자는 SQLite, LMDB 및 곧 브라우저 스토리지 전반에 걸쳐 일관된 NIP-62 지원을 얻습니다.

### NDK (Nostr Development Kit)

[PR #375](https://github.com/nostr-dev-kit/ndk/pull/375)는 seenEvents 추적 시스템의 버그를 수정합니다. 이 문제로 인해 특정 구독 패턴이 event를 이미 본 것으로 잘못 표시하여 사용자가 새 구독을 열거나 relay에 다시 연결할 때 콘텐츠를 놓치게 되었습니다. 수정 사항은 구독 수명 주기 전반에 걸쳐 event가 정확하게 추적되도록 하며, 이는 사용자 탐색에 따라 동적으로 구독 및 구독 취소하는 애플리케이션에 특히 중요합니다. NDK는 이 수정 사항이 포함된 beta.70으로 업데이트되었습니다.

### Damus (iOS)

[PR #3515](https://github.com/damus-io/damus/pull/3515)는 iOS 17 사용자에게 영향을 미치는 시작 시 충돌을 수정합니다. 이 문제는 Swift Mutex가 iOS 17에서 사용할 수 없기 때문에 사용되는 대체 클래스인 `NdbUseLock`의 산술 오버플로우에서 비롯되었습니다. 수정 사항은 이전 동기화 접근 방식을 iOS 17에서 사용 가능하고 나머지 경쟁 조건을 적절히 처리하는 `NSLock`으로 대체합니다. iOS 18+ 사용자는 네이티브 Swift Mutex 구현에 액세스할 수 있으므로 영향을 받지 않았습니다.

별도로, [PR #3509](https://github.com/damus-io/damus/pull/3509)를 통해 장문 기사 개선 사항이 도입되었습니다. 읽기 진행 막대가 기사 내 위치를 추적하고, 예상 읽기 시간이 미리보기에 표시되며, 세피아 모드와 조절 가능한 줄 높이 설정이 더 편안한 읽기를 제공합니다. 포커스 모드는 아래로 스크롤할 때 탐색 크롬을 자동으로 숨기고 탭하면 복원하여 집중 읽기를 위한 시각적 혼잡을 줄입니다. 여러 수정 사항이 마크다운 콘텐츠의 이미지 표시 문제를 해결하고 기사가 중간이 아닌 맨 위에서 열리도록 합니다.

### Zap.stream (라이브 스트리밍)

YouTube 및 Kick 채팅 통합은 외부 스트리밍 플랫폼의 메시지를 Nostr로 연결합니다. YouTube, Kick 및 Zap.stream으로 멀티캐스트하는 스트리머는 이제 각 플랫폼의 메시지가 네이티브 Nostr 댓글과 함께 표시되는 통합 보기에서 모든 채팅 메시지를 볼 수 있습니다. 이것은 스트리밍에 Nostr를 사용하고 싶지만 기존 플랫폼의 청중을 포기할 수 없는 크리에이터의 주요 마찰 지점을 제거합니다. 통합은 각 메시지가 어느 플랫폼에서 왔는지 표시하고 외부 계정 연결을 위한 인증 흐름을 처리합니다.

### Chachi (NIP-29 그룹)

[NIP-29](/ko/topics/nip-29/) 그룹 채팅 클라이언트가 이번 주에 6개의 병합된 PR을 출시했습니다. 보안 업데이트는 오픈 리디렉트 공격을 가능하게 할 수 있는 react-router의 XSS 취약점인 [CVE-2026-22029](https://github.com/purrgrammer/chachi/pull/89)를 해결합니다. 수정 사항은 react-router-dom 6.30.0으로 업데이트합니다. [PR #92](https://github.com/purrgrammer/chachi/pull/92)는 그룹 채팅에 페이지네이션된 메시지 로딩을 추가하여 긴 대화가 한 번에 모두가 아닌 점진적으로 로드됩니다. [PR #91](https://github.com/purrgrammer/chachi/pull/91)은 초기 로드 시 빈 그룹 이름을 유발하는 경쟁 조건과 멤버 보기를 충돌시키는 정의되지 않은 참가자 목록을 포함한 여러 NIP-29 버그를 수정합니다. 번역 범위는 이제 각각 1060개의 키를 가진 31개의 지원되는 로케일 모두를 포함합니다.

### 0xchat (메시징)

Telegram 스타일 메시징 클라이언트는 외부 서명 앱을 사용할 때 서명자 패키지 이름을 적절히 저장하여 [NIP-55](/ko/topics/nip-55/) 준수를 개선했으며, 재시작 후 어떤 서명자를 사용할지 앱이 추적을 잃는 문제를 수정했습니다. NIP-17 답글 처리는 이제 스레딩을 위한 `e` 태그를 올바르게 포함하여 클라이언트 전반에 걸쳐 답글이 올바른 대화 컨텍스트에 표시되도록 합니다. 성능 최적화는 긴 채팅 기록을 로드할 때 일반적인 문제인 메시지 목록의 스크롤 지연을 해결합니다. 임시 저장 자동 저장은 작성 중 다른 곳으로 이동해도 메시지 손실을 방지하며, 파일 저장 옵션에는 이제 기본 FileDropServer 및 BlossomServer 엔드포인트가 포함됩니다.

### Primal (iOS)

[NIP-46](/ko/topics/nip-46/) 원격 서명자 지원이 [PR #184](https://github.com/PrimalHQ/primal-ios-app/pull/184)를 통해 iOS에 도입되어 몇 주 전 Android에서 시작된 크로스 플랫폼 롤아웃을 완료합니다. 사용자는 이제 nsec.app이나 자체 호스팅 nsecBunker 인스턴스와 같은 전용 벙커 서비스에 개인 키를 보관하고, 클라이언트 앱에 키를 노출하지 않고 Nostr relay를 통해 연결하여 event에 서명할 수 있습니다. 이 분리는 Primal의 기능을 사용하면서 더 엄격한 키 관리 관행을 유지하려는 사용자의 보안 태세를 개선합니다. 구현에는 벙커 연결 URI를 위한 QR 코드 스캔이 포함되며 암호화된 relay 메시지를 통한 NIP-46 요청/응답 흐름을 처리합니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 계신가요? 공유할 뉴스가 있으신가요? 프로젝트를 다뤄드릴까요? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DM으로 연락하거나</a> Nostr에서 찾아주세요.
