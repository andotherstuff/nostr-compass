---
title: 'Nostr Compass #1'
date: 2025-12-17
publishDate: 2025-12-15
draft: false
type: newsletters
---

Nostr Compass에 오신 것을 환영합니다. Nostr 프로토콜 생태계를 다루는 주간 뉴스레터입니다. 우리의 임무는 개발자, 릴레이 운영자, 빌더들에게 네트워크 전반의 중요한 발전 상황을 알리는 것입니다. 우리는 NIP 제안부터 클라이언트 릴리스, 구현 모범 사례에 이르기까지 기술적 정확성, 중립성, 깊이를 갖추어 프로토콜 진화를 문서화합니다.

Nostr Compass는 [Bitcoin Optech](https://bitcoinops.org/)에서 영감을 받았습니다. Bitcoin Optech는 수년간 Bitcoin 기술 지식 발전에 헌신하여 프로토콜 중심 뉴스레터의 표준을 세웠습니다. 그들의 모범에 감사드리며, Nostr 생태계에도 동일한 엄격함을 가져오고자 합니다.

이번 창간호에서 주간 형식을 확립합니다. 매주 수요일 NIP 업데이트, 릴리스 노트, 개발 하이라이트, 기술 가이드를 전달해 드립니다. 클라이언트를 개발하든, 릴레이를 운영하든, 프로토콜에 기여하든, Nostr Compass는 생태계 전반에서 일어나는 일에 대한 신뢰할 수 있는 정보원이 되고자 합니다.

## Nostr란 무엇인가?

*이것이 첫 번째 호이므로, Nostr의 작동 방식에 대한 입문서로 시작합니다. 정기 독자는 [뉴스 및 업데이트로 건너뛰기](#뉴스)할 수 있습니다.*

Nostr(Notes and Other Stuff Transmitted by Relays)는 소셜 네트워킹과 메시징을 위한 탈중앙화 프로토콜입니다. 기존 플랫폼과 달리 Nostr에는 중앙 서버도, 이를 통제하는 회사도, 단일 장애 지점도 없습니다. 사용자는 암호화 키 쌍을 통해 자신의 신원을 소유하며, 콘텐츠는 누구나 운영할 수 있는 독립적인 릴레이 서버를 통해 흐릅니다.

**작동 방식:** 사용자는 키 쌍(nsec라는 개인 키와 npub라는 공개 키)을 생성합니다. 개인 키는 "이벤트"라는 메시지에 서명하고, 공개 키는 당신의 신원 역할을 합니다. 이벤트는 릴레이로 전송되며, 릴레이는 이를 저장하고 다른 사용자에게 전달합니다. 당신이 키를 통제하기 때문에, 신원이나 팔로워를 잃지 않고 클라이언트나 릴레이를 전환할 수 있습니다.

**중요한 이유:** Nostr는 릴레이 다양성(한 릴레이가 당신을 차단해도 다른 릴레이가 여전히 콘텐츠를 제공할 수 있음)을 통한 검열 저항성, 이식성(당신의 신원은 모든 Nostr 앱에서 작동), 상호운용성(모든 Nostr 클라이언트는 동일한 프로토콜을 사용)을 제공합니다. 무엇을 볼지 결정하는 알고리즘도, 광고도, 데이터 수집도 없습니다.

**오늘날의 생태계:** Nostr는 마이크로블로깅(Twitter/X와 유사), 장문 콘텐츠(Medium과 유사), 다이렉트 메시지, 마켓플레이스, 라이브 스트리밍 등을 지원합니다. 클라이언트에는 Damus(iOS), Amethyst(Android), Primal, Coracle 및 수십 개의 다른 앱이 있습니다. Lightning Network 통합으로 "zaps"를 통한 즉시 결제가 가능합니다. 프로토콜은 기능을 확장하는 커뮤니티 주도 사양인 NIP(Nostr Implementation Possibilities)를 통해 계속 진화하고 있습니다.

## 뉴스 {#news}

**NIP-BE 병합: Bluetooth Low Energy 지원** - 프로토콜에 중요한 새로운 기능이 [추가되었습니다](https://github.com/nostr-protocol/nips/pull/1979). [NIP-BE](/ko/topics/nip-be/)는 Nostr 애플리케이션이 Bluetooth Low Energy를 통해 통신하고 동기화하는 방법을 명시합니다. 이를 통해 오프라인 지원 앱이 인터넷 연결 없이 근처 기기 간에 데이터를 동기화할 수 있습니다. 이 사양은 WebSocket 릴레이 패턴을 BLE의 제약에 맞게 조정하여, DEFLATE 압축과 청크 메시징을 사용해 BLE의 작은 MTU 크기(20-256바이트)를 처리합니다. 기기는 UUID 비교를 기반으로 역할을 협상하며, 더 높은 UUID를 가진 기기가 GATT 서버가 됩니다.

**MIP-05: 프라이버시 보존 푸시 알림** - [Marmot Protocol](/ko/topics/marmot/)이 [MIP-05](/ko/topics/mip-05/)([사양](https://github.com/marmot-protocol/mips/blob/main/mip-05.md))를 발표했습니다. 이는 프라이버시를 유지하는 푸시 알림 사양입니다. 기존 푸시 시스템은 서버가 기기 토큰과 사용자 신원을 알아야 합니다. MIP-05는 ECDH+HKDF와 ChaCha20-Poly1305로 기기 토큰을 암호화하고, 임시 키를 사용하여 상관관계를 방지함으로써 이를 해결합니다. 세 가지 이벤트 가십 프로토콜(kind 447-449)이 그룹 멤버 간에 암호화된 토큰을 동기화하며, 알림은 [NIP-59](/ko/topics/nip-59/) gift wrapping과 디코이 토큰을 사용하여 그룹 크기를 숨깁니다. 이를 통해 WhiteNoise 및 기타 Marmot 클라이언트가 사용자 프라이버시를 침해하지 않고 적시에 알림을 전달할 수 있습니다.

**Blossom BUD-10: 새로운 URI 스킴** - [Blossom](/ko/topics/blossom/) 미디어 프로토콜이 [BUD-10](/ko/topics/bud-10/)([사양](https://github.com/hzrd149/blossom/blob/master/buds/10.md))을 통해 커스텀 URI 스킴을 도입합니다. 새로운 `blossom:<sha256>.ext` 형식은 파일 해시, 확장자, 크기, 다중 서버 힌트, [BUD-03](/ko/topics/bud-03/) 서버 검색을 위한 작성자 공개 키를 포함합니다. 이를 통해 blob 링크가 서버 간 자동 폴백을 가능하게 하여 정적 HTTP URL보다 더 탄력적입니다.

**Shopstr 마켓플레이스 업데이트** - Nostr 네이티브 마켓플레이스가 결제를 위해 [Nostr Wallet Connect를 구현](https://github.com/shopstr-eng/shopstr/pull/202)([NIP-47](/ko/topics/nip-47/))했고, [NIP-40](/ko/topics/nip-40/)을 사용한 [리스팅 만료 기능을 추가](https://github.com/shopstr-eng/shopstr/pull/203)했으며, 판매자를 위한 [할인 코드](https://github.com/shopstr-eng/shopstr/pull/210)를 도입했습니다.

## NIP 업데이트 {#nip-updates}

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**새로운 NIP:**
- **[NIP-BE](/ko/topics/nip-be/)** - Bluetooth Low Energy 메시징 및 기기 동기화 ([#1979](https://github.com/nostr-protocol/nips/pull/1979))
- **[NIP-63](/ko/topics/nip-63/)** - 프로토콜 내 게이트된 콘텐츠를 처리하기 위한 페이월/프리미엄 콘텐츠 표준 ([#2156](https://github.com/nostr-protocol/nips/pull/2156))

**주요 변경 사항:**
- **[NIP-24](/ko/topics/nip-24/)** - Kind 0 사용자 메타데이터에 선택적 `languages` 배열 추가, 사용자가 향상된 콘텐츠 검색 및 릴레이 매칭을 위해 IETF BCP 47 태그를 사용하여 여러 선호 언어를 지정할 수 있음 ([#2159](https://github.com/nostr-protocol/nips/pull/2159))
- **[NIP-69](/ko/topics/nip-69/)** - `expires_at` 및 `expiration` 태그로 P2P 거래에 주문 만료 지원 추가 ([#2118](https://github.com/nostr-protocol/nips/pull/2118))
- **[NIP-59](/ko/topics/nip-59/)** - Gift wrap 이벤트를 이제 NIP-09/NIP-62 요청을 통해 삭제 가능 ([#2131](https://github.com/nostr-protocol/nips/pull/2131))
- **[NIP-51](/ko/topics/nip-51/)** - 일반 북마크에서 해시태그 및 URL 태그 제거; 해시태그는 이제 kind 30015 사용 ([#2133](https://github.com/nostr-protocol/nips/pull/2133))
- **[NIP-18](/ko/topics/nip-18/)** - `a` 태그 지원으로 교체 가능 이벤트에 대한 일반 리포스트 개선 ([#2132](https://github.com/nostr-protocol/nips/pull/2132))
- **[NIP-17](/ko/topics/nip-17/)** - 문구 개선 및 DM에 kind 7 리액션 지원 추가 ([#2098](https://github.com/nostr-protocol/nips/pull/2098))
- **[NIP-11](/ko/topics/nip-11/)** - 릴레이 공개 키 식별을 위한 `self` 필드 추가 ([#1764](https://github.com/nostr-protocol/nips/pull/1764))

## NIP 심층 분석: NIP-01과 NIP-19 {#nip-deep-dive-nip-01-and-nip-19}

이번 창간호에서는 모든 Nostr 개발자가 이해해야 할 두 가지 기초 NIP를 다룹니다. 자세한 내용은 [NIP-01](/ko/topics/nip-01/)과 [NIP-19](/ko/topics/nip-19/) 토픽 페이지를 참조하세요.

### NIP-01: 기본 프로토콜

[NIP-01](/ko/topics/nip-01/)은 핵심 프로토콜을 정의합니다. Nostr의 모든 것은 이 사양을 기반으로 합니다.

**이벤트**는 유일한 객체 유형입니다. 각 이벤트에는 다음이 포함됩니다:
- `id`: 직렬화된 이벤트의 SHA256 해시(이벤트의 고유 식별자)
- `pubkey`: 생성자의 공개 키(32바이트 hex, secp256k1)
- `created_at`: Unix 타임스탬프
- `kind`: 이벤트 유형을 분류하는 정수
- `tags`: 메타데이터용 배열의 배열
- `content`: 페이로드(해석은 kind에 따라 다름)
- `sig`: 해당 pubkey가 이 이벤트를 생성했음을 증명하는 Schnorr 서명

**Kind**는 릴레이가 이벤트를 저장하는 방식을 결정합니다:
- 일반 이벤트 (1, 2, 4-44, 1000-9999): 정상적으로 저장, 모든 버전 유지
- 교체 가능 이벤트 (0, 3, 10000-19999): pubkey당 최신 버전만 유지
- 임시 이벤트 (20000-29999): 저장되지 않고 구독자에게만 전달
- 주소 지정 가능 이벤트 (30000-39999): pubkey + kind + `d` 태그 조합당 최신 버전

Kind 0은 사용자 메타데이터(프로필), kind 1은 텍스트 노트(기본 게시물), kind 3은 팔로우 리스트입니다.

**Kind 1: 텍스트 노트**는 소셜 Nostr의 핵심입니다. Kind 1 이벤트는 트윗과 유사한 단문 게시물입니다. `content` 필드에는 메시지 텍스트가 포함됩니다(일반 텍스트, 클라이언트는 종종 마크다운을 렌더링). 태그를 통해 답글, 멘션, 참조가 가능합니다:

```json
{
  "id": "<32-byte-hex>",
  "pubkey": "<32-byte-hex>",
  "created_at": 1734480000,
  "kind": 1,
  "content": "Hello Nostr! Check out @jb55's work on Damus.",
  "tags": [
    ["e", "<replied-to-event-id>", "wss://relay.example.com", "reply"],
    ["p", "<jb55-pubkey>"]
  ],
  "sig": "<64-byte-hex>"
}
```

"reply" 마커가 있는 `e` 태그는 이것이 답글임을 나타냅니다(스레딩 규칙은 [NIP-10](/ko/topics/nip-10/) 참조). `p` 태그는 사용자를 멘션하여 클라이언트가 알림을 보내고 원시 pubkey 대신 이름을 렌더링할 수 있게 합니다. 클라이언트는 멘션된 사용자의 kind 0 이벤트를 가져와 표시 이름과 사진을 얻습니다.

타임라인을 구성하려면 클라이언트가 팔로우한 pubkey의 kind 1 이벤트를 구독합니다: `["REQ", "feed", {"kinds": [1], "authors": ["<pubkey1>", "<pubkey2>", ...], "limit": 50}]`. 릴레이는 일치하는 노트를 반환하고, 클라이언트는 이를 시간순으로 렌더링합니다.

**주소 지정 가능 이벤트** (30000-39999)는 교체 가능 이벤트처럼 작동하지만 `d` 태그를 추가 식별자로 사용합니다. 릴레이는 각 pubkey + kind + d-tag 조합의 최신 버전만 유지합니다. 이를 통해 편집 가능한 기사, 상품 목록 또는 사용자당 여러 교체 가능 항목이 필요한 모든 경우가 가능합니다.

**태그**는 첫 번째 요소가 태그 이름인 배열입니다. 표준 단일 문자 태그(`e`, `p`, `a`, `d`, `t`)는 효율적인 쿼리를 위해 릴레이에 의해 인덱싱됩니다. 예를 들어, `["e", "<event-id>"]`는 다른 이벤트를 참조하고, `["p", "<pubkey>"]`는 사용자를 참조합니다.

**클라이언트-릴레이 통신**은 JSON 배열을 메시지로 사용하는 WebSocket 연결을 사용합니다. 첫 번째 요소는 메시지 유형을 식별합니다.

클라이언트에서 릴레이로:
- `["EVENT", <event>]` - 릴레이에 이벤트 게시
- `["REQ", <sub-id>, <filter>, ...]` - 필터와 일치하는 이벤트 구독
- `["CLOSE", <sub-id>]` - 구독 종료

릴레이에서 클라이언트로:
- `["EVENT", <sub-id>, <event>]` - 구독과 일치하는 이벤트 전달
- `["EOSE", <sub-id>]` - "저장된 이벤트 종료" - 릴레이가 모든 히스토리 매치를 전송했고 이제 새 이벤트가 도착할 때만 전송
- `["OK", <event-id>, <true|false>, <message>]` - 이벤트가 수락 또는 거부되었는지(그리고 이유) 확인
- `["NOTICE", <message>]` - 릴레이의 사람이 읽을 수 있는 메시지

구독 흐름: 클라이언트가 구독 ID와 필터로 `REQ`를 전송, 릴레이가 일치하는 `EVENT` 메시지로 응답, 그런 다음 히스토리를 따라잡았음을 알리기 위해 `EOSE`를 전송. `EOSE` 이후 새로운 `EVENT` 메시지는 실시간입니다. 완료되면 클라이언트가 `CLOSE`를 전송합니다.

**필터**는 검색할 이벤트를 지정합니다. 필터 객체는 다음을 포함할 수 있습니다: `ids`(이벤트 ID), `authors`(pubkey), `kinds`(이벤트 유형), `#e`/`#p`/`#t`(태그 값), `since`/`until`(타임스탬프), `limit`(최대 결과). 하나의 필터 내 모든 조건은 AND 논리를 사용합니다. `REQ`에 여러 필터를 포함할 수 있으며, OR 논리로 결합됩니다 - 하나의 구독으로 다른 이벤트 유형을 가져오는 데 유용합니다.

### NIP-19: Bech32 인코딩 식별자

[NIP-19](/ko/topics/nip-19/)는 Nostr 어디서나 볼 수 있는 사용자 친화적 형식을 정의합니다: npub, nsec, note 등. 이들은 프로토콜 자체(hex 사용)에서 사용되지 않지만 공유와 표시에 필수적입니다.

**왜 bech32인가?** 원시 hex 키는 복사하기 쉽지 않고 시각적으로 구별하기 어렵습니다. Bech32 인코딩은 사람이 읽을 수 있는 접두사와 체크섬을 추가합니다. `npub`(공개 키)과 `nsec`(개인 키) 또는 `note`(이벤트 ID)를 즉시 구별할 수 있습니다.

**기본 형식**은 원시 32바이트 값을 인코딩합니다:
- `npub` - 공개 키(당신의 신원, 공유해도 안전)
- `nsec` - 개인 키(비밀 유지, 서명에 사용)
- `note` - 이벤트 ID(특정 이벤트 참조)

예시: hex pubkey `3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d`는 `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`가 됩니다.

**공유 가능 식별자**는 TLV(Type-Length-Value) 인코딩을 사용하여 메타데이터를 포함합니다:
- `nprofile` - 릴레이 힌트가 있는 프로필(클라이언트가 사용자를 찾는 데 도움)
- `nevent` - 릴레이 힌트, 작성자 pubkey, kind가 있는 이벤트
- `naddr` - 주소 지정 가능 이벤트 참조(pubkey + kind + d-tag + relays)

이들은 핵심 문제를 해결합니다: 누군가 노트 ID를 공유하면 어떤 릴레이에 있는지 어떻게 알 수 있을까요? `nevent`는 이벤트 ID와 제안된 릴레이를 함께 묶어 공유를 더 안정적으로 만듭니다.

**중요:** 프로토콜 자체에서는 bech32 형식을 사용하지 마세요. 이벤트, 릴레이 메시지, NIP-05 응답은 반드시 hex를 사용해야 합니다. Bech32는 순전히 사람 인터페이스용입니다: 표시, 복사/붙여넣기, QR 코드, URL.

## 릴리스 {#releases}

**Amber v4.0.4** - Android 서명자 앱이 NullPointerException을 수정하고, 활동 화면 성능을 개선했으며, 일부 이벤트 kind에 대한 번역을 추가했습니다. 이전 v4.0.3 릴리스에서는 개편된 암호화/복호화 UI, 계정 내보내기/가져오기, 계정별 릴레이 처리, bunker ping 지원, 충돌 보고 기능이 추가되었습니다. [릴리스](https://github.com/greenart7c3/Amber/releases/tag/v4.0.4)

**Coracle 0.6.28** - 웹 클라이언트 버그 수정 릴리스. 토픽 피드, imgproxy 비활성화 시 이미지 처리, 비링크 하이라이트 소스의 링크화 문제가 수정되었습니다. [릴리스](https://github.com/coracle-social/coracle/releases/tag/0.6.28)

**Flotilla v1.6.2** - Discord 유사 커뮤니티 클라이언트가 모달 스크롤 및 스타일 문제를 수정했습니다. 이 사이클의 이전 릴리스에서는 알림을 위한 선택적 배지와 사운드, 개선된 링크 렌더링, 초대 링크용 QR 코드 스캔, 간소화된 지갑 설정이 추가되었습니다. [릴리스](https://github.com/coracle-social/flotilla/releases/tag/1.6.2)

**nak v0.17.2** - 명령줄 Nostr 도구에 빠른 NIP 참조 조회를 위한 새로운 `nip` 명령이 추가되었고, git 저장소 처리 및 stdin 이벤트 처리 수정이 포함되었습니다. [릴리스](https://github.com/fiatjaf/nak/releases/tag/v0.17.2)

**White Noise v0.2.1** - MLS 기반 암호화 메시징 앱의 주요 릴리스로 Blossom을 통한 이미지 공유, 백그라운드 동기화, 푸시 알림, 8개 언어 현지화, 그룹 멤버 관리가 추가되었습니다. [릴리스](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Amethyst v1.04.2** - 팔로우 리스트/팩, 새로운 타임라인 필터, 이미지 갤러리, H.265 비디오 압축(50% 더 작은 파일)을 도입한 기능 릴리스. Kotlin Multiplatform 마이그레이션 완료. [릴리스](https://github.com/vitorpamplona/amethyst/releases/tag/v1.04.2)

**Mostro v0.15.5** - NIP-69 주문 만료 지원 및 개선된 거래 내역 응답이 포함된 P2P 거래 봇 업데이트. [릴리스](https://github.com/MostroP2P/mostro/releases/tag/v0.15.5)

**Nosflare v8.9.26** - Cloudflare 인프라에 구축된 서버리스 Nostr 릴레이. 이 릴리스는 websocket 실패를 일으킬 수 있는 버그를 해결하는 중요한 핫픽스를 제공하여 릴레이에 의존하는 사용자와 애플리케이션에 더 안정적인 연결을 보장합니다. [릴리스](https://github.com/Spl0itable/nosflare/releases/tag/v8.9.26)

**Noscall v0.4.1** - Nostr 기반 보안 오디오 및 비디오 통화 앱. 이 릴리스는 Me 페이지의 팝업 UI를 개선하고 여러 알려진 문제를 수정하여 더 나은 안정성과 통화 신뢰성을 제공합니다. [릴리스](https://github.com/sanah9/noscall/releases/tag/v0.4.1-release)

**Gitplaza v0.25.0** - Git 관련 활동에 중점을 둔 데스크톱 Nostr 클라이언트. 이 릴리스는 인박스 피드를 위한 고급 kind 필터를 도입하고, 필터에 일반 zaps를 포함하며, 탭 텍스트 형식을 단순화합니다. 성능 개선으로 코멘트 트리 로딩을 최적화하고, 불필요한 데이터베이스 쿼리를 줄이며, 더 빠른 표시를 위해 캐시된 코멘트 브랜치를 사용합니다. [릴리스](https://codeberg.org/dluvian/gitplaza/releases/tag/v0.25.0)

## 주목할 만한 코드 및 문서 변경 {#notable-code-and-documentation-changes}

### Damus (iOS) {#damus}

안정성에 초점을 맞춘 충돌 및 UI 수정: compose 뷰의 [커서 점프 수정](https://github.com/damus-io/damus/pull/3377), 트랜잭션 안전성을 위해 Swift의 `~Copyable` 타입을 사용한 [NostrDB 인터페이스 재설계](https://github.com/damus-io/damus/pull/3366), 액션 바 재인스턴스화를 수정한 [스레드 UI 안정성](https://github.com/damus-io/damus/pull/3341), AttributeGraph 사이클로 인한 [뮤트 리스트 프리즈](https://github.com/damus-io/damus/pull/3346), 크로스 스레드 트랜잭션 정리로 인한 [프로필 충돌](https://github.com/damus-io/damus/pull/3334). 또한 AI 코딩 에이전트를 위한 [AGENTS.md](https://github.com/damus-io/damus/pull/3293) 가이드라인 추가.

### Notedeck (데스크톱/모바일) {#notedeck}

[보안 키 저장소](https://github.com/damus-io/notedeck/pull/1191)가 nsec를 자동 마이그레이션과 함께 OS 보안 저장소로 이동. [미래 노트 필터링](https://github.com/damus-io/notedeck/pull/1201)이 24시간 이상 미래 날짜의 이벤트를 숨김(스팸 방지). [nevent 복사](https://github.com/damus-io/notedeck/pull/1183)가 이제 릴레이 힌트를 포함. 또한: [프로필 컬럼 빠른 추가](https://github.com/damus-io/notedeck/pull/1212), [키보드 탐색](https://github.com/damus-io/notedeck/pull/1208), [미디어 로딩 최적화](https://github.com/damus-io/notedeck/pull/1210).

### Amethyst (Android) {#amethyst}

Nostr Connect를 위한 [[NIP-46](/ko/topics/nip-46/) 원격 서명](https://github.com/vitorpamplona/amethyst/pull/1555) 지원. 공개/비공개 리스트 관리가 포함된 [북마크 구성](https://github.com/vitorpamplona/amethyst/pull/1586). 릴레이 정보 파싱 엣지 케이스에 대한 [strfry 호환성](https://github.com/vitorpamplona/amethyst/pull/1596) 수정.

### Primal (Android) {#primal}

`nostrconnect://` URL을 위한 [Nostr Connect 딥 링크](https://github.com/PrimalHQ/primal-android-app/pull/788). bunker 연결을 위한 QR 스캔을 통한 [원격 로그인](https://github.com/PrimalHQ/primal-android-app/pull/787). [연결 경쟁 조건 수정](https://github.com/PrimalHQ/primal-android-app/pull/783).

### White Noise (암호화 메시징) {#white-noise}

[앱 데이터 보존 수정](https://github.com/marmot-protocol/whitenoise/pull/890)이 프라이버시를 위해 Android 자동 백업을 비활성화. [채팅 스크롤 동작](https://github.com/marmot-protocol/whitenoise/pull/861)이 히스토리를 읽을 때 위치를 유지.

### Zeus (Lightning Wallet) {#zeus}

배치 zap 처리량 향상을 위한 [[NIP-47](/ko/topics/nip-47/) 병렬 결제](https://github.com/ZeusLN/zeus/pull/3407).

## 개발자 모범 사례

**Auth 이벤트를 방어적으로 검증** - go-nostr가 릴레이 태그가 누락된 경우 [NIP-42 검증에서의 패닉](https://github.com/nbd-wtf/go-nostr/pull/182)을 수정했습니다. 잘 형식화된 이벤트를 기대하는 인증 흐름에서도 항상 필수 태그를 액세스하기 전에 확인하세요.

**인증 상태에 따라 속도 제한** - khatru가 [NIP-42 기반 속도 제한](https://github.com/fiatjaf/khatru/pull/57)을 추가하여 릴레이가 인증된 연결과 익명 연결에 다른 제한을 적용할 수 있습니다. 일괄 제한 대신 인증 상태에 따른 계층화된 제한을 고려하세요.

**리스트에 커서 페이지네이션 사용** - Blossom이 `/list` 엔드포인트에서 [날짜 기반 페이지네이션을 커서 기반으로 교체](https://github.com/hzrd149/blossom/pull/65)했습니다. 날짜 기반 페이지네이션은 항목이 타임스탬프를 공유할 때 깨집니다; 커서가 안정적인 반복을 제공합니다.

**이벤트 유형에 대한 스키마 검증** - [nostrability/schemata](https://github.com/nostrability/schemata) 프로젝트가 NIP 준수 이벤트 검증을 위한 JSON 스키마를 제공합니다. 잘못 형식화된 이벤트가 릴레이에 도달하기 전에 잡기 위해 개발 중 스키마 검증 통합을 고려하세요.

---

이번 주는 여기까지입니다. 무언가를 만들고 계신가요? 공유할 뉴스가 있으신가요? 프로젝트를 다뤄주길 원하시나요? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DM으로 연락하세요</a> 또는 Nostr에서 찾아주세요.

