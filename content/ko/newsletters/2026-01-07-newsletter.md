---
title: 'Nostr Compass #4'
date: 2026-01-07
publishDate: 2026-01-07
draft: false
type: newsletters
---

Nostr 프로토콜 생태계에 대한 주간 가이드, Nostr Compass에 다시 오신 것을 환영합니다.

**이번 주:** Primal Android가 [NIP-46](/ko/topics/nip-46/) 원격 서명과 [NIP-55](/ko/topics/nip-55/) 로컬 서명자 지원을 탑재하여 다른 Android 앱을 위한 완전한 서명 허브가 되었습니다. [Marmot Protocol](/ko/topics/marmot/) 팀은 보안 감사 결과에 대응하여 [MLS](/ko/topics/mls/) 기반 암호화 메시징을 강화하는 18개의 PR을 병합했습니다. Citrine이 v1.0에 도달했고 Applesauce는 전체 라이브러리 스위트에 걸쳐 v5.0을 출시했습니다. TENEX는 Nostr에서 AI 에이전트 감독 기능을 구축하고 있으며, Jumble은 스마트 릴레이 풀링을 추가했습니다. NIP-55 스펙 수정으로 `nip44_encrypt` 반환 필드가 명확해졌고, [NIP-50](/ko/topics/nip-50/) PR은 고급 검색을 위한 쿼리 표현식 확장을 제안합니다. 심층 분석에서는 [NIP-04](/ko/topics/nip-04/)와 [NIP-44](/ko/topics/nip-44/)를 설명합니다: 레거시 암호화의 보안 결함과 현대적 대체 방식이 이를 어떻게 해결하는지 알아봅니다.

## 뉴스

**Primal Android가 완전한 서명 허브가 되다** - [버전 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18)은 [NIP-46](/ko/topics/nip-46/) 원격 서명과 [NIP-55](/ko/topics/nip-55/) 로컬 서명을 모두 추가하여 Primal을 다른 Nostr 앱을 위한 완전한 서명자로 만들었습니다. NIP-46을 통한 원격 서명은 사용자가 Nostr 릴레이를 통해 벙커 서비스에 연결할 수 있게 하여 키를 기기에서 완전히 분리합니다. NIP-55를 통한 로컬 서명은 Primal을 Android 콘텐츠 제공자로 노출하여 Amethyst나 Citrine 같은 앱이 개인 키에 직접 접근하지 않고도 서명을 요청할 수 있게 합니다. [여러 후속 PR](https://github.com/PrimalHQ/primal-android-app/pull/839)이 NIP-55 스펙의 16진수 pubkey 요구사항과의 호환성 문제를 수정했고, 잘못된 형식의 `nostrconnect://` URI 파싱을 개선했습니다. 이번 릴리스에는 부드러운 스크롤을 위한 미디어 사전 캐싱, 개선된 스레드 로드 시간, 아바타 사전 캐싱도 포함됩니다.

**Marmot Protocol 감사 후 보안 강화** - [NIP-104](/ko/topics/nip-104/) MLS 기반 엔드투엔드 암호화 메시징을 구현하는 [Marmot Development Kit](https://github.com/marmot-protocol/mdk) (mdk)가 이번 주에 광범위한 보안 수정을 받았습니다. 18개의 병합된 풀 리퀘스트가 감사 결과를 해결했는데, 여기에는 스토리지 수준 블롭 대체 공격을 방지하기 위한 [암호화된 그룹 이미지의 해시 검증](https://github.com/marmot-protocol/mdk/pull/97), 메모리 고갈을 방지하기 위한 [대기 중인 환영 메시지의 페이지네이션](https://github.com/marmot-protocol/mdk/pull/110), [오류 메시지에서의 MLS Group ID 유출](https://github.com/marmot-protocol/mdk/pull/112), 그리고 키 패키지를 위한 [base64 인코딩 강제](https://github.com/marmot-protocol/mdk/pull/98)가 포함됩니다. [Marmot 스펙 자체도](https://github.com/marmot-protocol/marmot/pull/20) MIP-04 v2 버전 관리 및 보안 개선으로 업데이트되었습니다. 활성 PR들은 논스 재사용, 시크릿 제로화, 캐시 오염 벡터를 계속 해결하고 있습니다.

**Nostrability가 릴레이 힌트 지원 추적** - 새로운 [릴레이 힌트 호환성 추적기](https://github.com/nostrability/nostrability/issues/270)가 클라이언트들이 생태계 전반에서 릴레이 힌트를 구성하고 소비하는 방식을 문서화합니다. 추적기는 대부분의 클라이언트가 이제 [NIP-10](/ko/topics/nip-10/) 및 [NIP-19](/ko/topics/nip-19/)에 따라 힌트를 구성하지만, 소비 방식은 매우 다양하다는 것을 보여줍니다: 일부 클라이언트는 발신 이벤트에 힌트를 포함하지만 수신 힌트를 가져오기에 사용하지 않습니다. 6개의 클라이언트가 완전한 구현으로 "Full" 등급을 받았습니다. 이 추적기는 상호 운용성을 확인하는 개발자와 일부 클라이언트가 다른 클라이언트가 찾지 못하는 콘텐츠를 찾을 수 있는 이유가 궁금한 사용자에게 유용합니다.

**Nostria 2.0 크로스 플랫폼 기능 대폭 개편 출시** - [Nostria](https://nostria.app) 클라이언트가 iOS(TestFlight), Android(Play Store), Web, Windows에 걸쳐 상당한 추가 기능과 함께 [버전 2.0을 출시](https://njump.me/nevent1qqs9z4l8z82zphszjlmrjkr8whpvupnlaxc7xk5gfg9syzj0thygtzgpz4mhxue69uhhyetvv9ujuerpd46hxtnfduhszxthwden5te0wfjkccte9enrw73wd9hsz9nhwden5te0wfjkccte9ec8y6tdv9kzumn9wsq3gamnwvaz7tmjv4kxz7fwv3sk6atn9e5k7qgkwaehxw309aex2mrp0yhxgctdw4eju6t09uq32amnwvaz7tmwdaejumr0dshsz9mhwden5te0wfjkccte9ec82c30989ksmfnv9kzumn9wshsqgzxsnsv7pfqqd7rw4fvr0jnkpqmwzfqq3znlc4pqunagxrkl84u66y7fq9)했습니다. 이번 릴리스는 재생목록 생성, 트랙 업로드, zap 기반 아티스트 결제, 기능하는 이퀄라이저가 있는 WinAmp 스타일 플레이어를 갖춘 네이티브 음악 지원을 추가합니다. 라이브 스트리밍은 게임플레이 스트림 중 풍부한 메타데이터를 표시하는 Game API 통합을 받았습니다. 새로운 요약 기능은 시간별, 일별 또는 주별 활동 다이제스트를 압축된 타임라인 뷰로 생성합니다. Discover 섹션은 콘텐츠와 프로필을 찾기 위한 큐레이션된 목록을 제공합니다. 미디어 게시는 크로스 클라이언트 검색 가능성을 위한 자동 짧은 형식 게시물 생성으로 단순화되었습니다. 원격 서명자 연결은 이제 수동 구성 없이 QR 코드 스캔을 통해 작동합니다. 프로필 발견은 일반적인 Nostr 문제점을 해결합니다: 사용자가 메타데이터를 가져오지 않고 릴레이 간에 이동할 때 Nostria가 프로필을 찾아 현재 릴레이에 다시 게시합니다. 프리미엄 구독자는 YouTube 채널 통합, 비공개 메모, 분석 대시보드, 병합/복원 옵션이 있는 자동 팔로잉 목록 백업을 이용할 수 있습니다.

## NIP 업데이트

[NIPs 저장소](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**병합됨:**
- **[NIP-55](/ko/topics/nip-55/)** - `nip44_encrypt` 메서드의 반환 필드 수정 ([#2184](https://github.com/nostr-protocol/nips/pull/2184)). Android 서명자는 이제 별도의 필드가 아닌 `signature` 필드에 암호화된 페이로드를 반환해야 합니다(`nip44_decrypt`와 일치). 이는 Amber 및 Primal의 기존 구현과 스펙을 일치시킵니다.

**열린 PR:**
- **[NIP-50](/ko/topics/nip-50/)** - 쿼리 표현식 확장 ([#2182](https://github.com/nostr-protocol/nips/pull/2182))은 구조화된 쿼리 표현식으로 NIP-50 검색을 확장할 것을 제안합니다. 이 PR은 `kind:1`, `author:npub1...` 같은 연산자와 불리언 조합(`AND`, `OR`, `NOT`)을 추가하여 단순 텍스트 매칭을 넘어서는 더 정밀한 검색 쿼리를 가능하게 합니다. 이를 통해 클라이언트는 기본 검색 문자열과의 하위 호환성을 유지하면서 고급 검색 인터페이스를 구축할 수 있습니다.

## NIP 심층 분석: NIP-04와 NIP-44

이번 주에는 Nostr의 암호화 표준을 다룹니다: 여전히 접하게 될 레거시 NIP-04와 심각한 보안 결함을 수정한 현대적 대체품 NIP-44입니다.

### [NIP-04](/ko/topics/nip-04/): 암호화된 다이렉트 메시지 (레거시)

[NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md)는 kind 4 이벤트를 사용하는 Nostr의 첫 암호화 메시징 시도였습니다. 구현이 간단하지만 알려진 보안 취약점이 있어 NIP-44를 위해 더 이상 사용되지 않습니다.

**작동 방식:** NIP-04는 ECDH(타원 곡선 Diffie-Hellman)를 사용하여 발신자와 수신자 간의 공유 비밀을 도출한 다음 AES-256-CBC로 암호화합니다.

```json
{
  "id": "<event-id>",
  "pubkey": "<sender-pubkey>",
  "created_at": 1736200000,
  "kind": 4,
  "tags": [["p", "<recipient-pubkey>"]],
  "content": "base64-ciphertext?iv=base64-iv",
  "sig": "<signature>"
}
```

암호화 흐름:
1. 공유 포인트 계산: `shared = ECDH(sender_privkey, recipient_pubkey)`
2. 키 도출: `key = SHA256(shared_x_coordinate)`
3. 무작위 16바이트 IV 생성
4. 암호화: `ciphertext = AES-256-CBC(key, iv, plaintext)`
5. 콘텐츠 형식화: `base64(ciphertext)?iv=base64(iv)`

**보안 문제:**

- **인증 없음:** AES-CBC는 기밀성은 제공하지만 무결성은 제공하지 않습니다. 릴레이를 제어하는 공격자가 암호문 비트를 수정하여 평문에 예측 가능한 변경을 일으킬 수 있습니다(비트 플리핑 공격).
- **평문 IV:** 초기화 벡터가 암호문과 함께 전송되며, 예측 가능한 IV를 가진 CBC 모드는 선택 평문 공격을 가능하게 합니다.
- **패딩 검증 없음:** 구현마다 PKCS#7 패딩을 처리하는 방식이 달라 패딩 오라클 공격이 가능할 수 있습니다.
- **메타데이터 노출:** 발신자 pubkey, 수신자 pubkey, 타임스탬프가 모두 릴레이에 노출됩니다.
- **키 재사용:** 두 당사자 간의 모든 메시지에 동일한 공유 비밀이 영원히 사용됩니다.

**여전히 존재하는 이유:** 많은 오래된 클라이언트와 릴레이가 NIP-04만 지원합니다. 레거시 시스템과 상호 작용할 때 이를 접하게 됩니다. Amber 같은 서명자와 Primal 같은 앱은 하위 호환성을 위해 여전히 `nip04_encrypt`/`nip04_decrypt`를 구현합니다.

### [NIP-44](/ko/topics/nip-44/): 버전 관리 암호화

[NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md)는 NIP-04의 알려진 결함을 수정하도록 설계된 현대적 암호화 표준입니다. NIP-44 구현에 대한 Cure53 보안 감사에서 타이밍 공격 및 순방향 비밀성 문제를 포함한 10개의 문제가 식별되었으며, 스펙이 확정되기 전에 해결되었습니다. 적절한 키 도출과 인증된 암호화와 함께 ChaCha20-Poly1305를 사용합니다.

**NIP-04 대비 주요 개선 사항:**

| 측면           | NIP-04                     | NIP-44                  |
|:---------------|:---------------------------|:------------------------|
| 암호           | AES-256-CBC                | XChaCha20-Poly1305      |
| 인증           | 없음                       | Poly1305 MAC            |
| 키 도출        | SHA256(shared_x)           | 솔트가 있는 HKDF        |
| 논스           | 16바이트 IV, 재사용 패턴   | 24바이트 무작위 논스    |
| 패딩           | PKCS#7 (길이 유출)         | 2의 거듭제곱으로 패딩   |
| 버전 관리      | 없음                       | 버전 바이트 접두사      |

**암호화 흐름:**

1. **대화 키:** 각 발신자-수신자 쌍에 대해 안정적인 키를 도출:
   ```
   shared_x = ECDH(sender_privkey, recipient_pubkey).x
   conversation_key = HKDF-SHA256(
     ikm = shared_x,
     salt = "nip44-v2",
     info = ""
   )
   ```

2. **메시지 키:** 각 메시지에 대해 무작위 32바이트 논스를 생성하고 암호화/인증 키를 도출:
   ```
   keys = HKDF-SHA256(
     ikm = conversation_key,
     salt = nonce,
     info = "nip44-v2"
   )
   chacha_key = keys[0:32]
   chacha_nonce = keys[32:44]
   hmac_key = keys[44:76]
   ```

3. **평문 패딩:** 메시지 길이를 숨기기 위해 다음 2의 거듭제곱으로 패딩(최소 32바이트):
   ```
   padded = [length_u16_be] + [plaintext] + [zeros to next power of 2]
   ```

4. **암호화 및 인증:**
   ```
   ciphertext = XChaCha20(chacha_key, chacha_nonce, padded)
   mac = HMAC-SHA256(hmac_key, nonce + ciphertext)
   ```

5. **페이로드 형식화:**
   ```
   payload = [version=0x02] + [nonce] + [ciphertext] + [mac]
   content = base64(payload)
   ```

**버전 바이트:** 첫 번째 바이트(`0x02`)는 암호화 버전을 나타냅니다. 이를 통해 기존 메시지를 손상시키지 않고 향후 업그레이드가 가능합니다. 버전 `0x01`은 널리 배포되지 않은 초기 초안이었습니다.

**복호화:**

1. base64 디코드, 버전 바이트가 `0x02`인지 확인
2. 논스(바이트 1-32), 암호문, MAC(마지막 32바이트) 추출
3. 수신자의 개인 키와 발신자의 공개 키를 사용하여 대화 키 도출
4. 대화 키와 논스에서 메시지 키 도출
5. 복호화 전에 MAC 검증(유효하지 않으면 거부)
6. 암호문 복호화, 길이 접두사 추출, 패딩되지 않은 평문 반환

**보안 속성:**

- **인증된 암호화:** Poly1305 MAC이 복호화 전에 모든 변조를 감지
- **순방향 비밀성(부분적):** 각 메시지가 고유한 논스를 사용하므로 한 메시지가 손상되어도 다른 메시지는 드러나지 않음. 그러나 개인 키가 손상되면 과거의 모든 메시지가 노출됨(래칫 없음).
- **길이 숨김:** 2의 거듭제곱 패딩이 정확한 메시지 길이를 숨김
- **타이밍 공격 저항:** MAC 검증을 위한 상수 시간 비교

**실제 사용:** NIP-44는 다음을 위한 암호화 레이어입니다:
- [NIP-17](/ko/topics/nip-17/) 비공개 다이렉트 메시지(gift wrap 내부)
- [NIP-46](/ko/topics/nip-46/) 원격 서명자 통신
- [NIP-59](/ko/topics/nip-59/) seal 암호화
- [Marmot Protocol](/ko/topics/nip-104/) 그룹 메시지, 여기서 NIP-44는 MLS exporter secret에서 도출된 키를 사용하여 MLS 암호화된 콘텐츠를 래핑
- 안전한 포인트 투 포인트 암호화가 필요한 모든 애플리케이션

**마이그레이션 가이드:** 새로운 애플리케이션은 NIP-44만 사용해야 합니다. 하위 호환성을 위해, NIP-04로 폴백하기 전에 연락처의 클라이언트가 NIP-44를 지원하는지([NIP-89](/ko/topics/nip-89/) 앱 메타데이터 또는 릴레이 지원을 통해) 확인하세요. 메시지를 받을 때는 먼저 NIP-44 복호화를 시도한 다음 레거시 콘텐츠에 대해 NIP-04로 폴백하세요.

## 릴리스

**Primal Android v2.6.18** - [전체 릴리스](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18)는 [NIP-46](/ko/topics/nip-46/) 원격 서명과 [NIP-55](/ko/topics/nip-55/) 로컬 서명을 추가하여 Primal을 다른 Android 앱을 위한 서명 허브로 만듭니다. 성능 개선에는 미디어 사전 캐싱, 아바타 사전 캐싱, 더 빠른 스레드 로딩이 포함됩니다. 버그 수정은 바이오의 자기 언급, 미디어 갤러리 크래시, 스트림 제목 폴백을 해결합니다. iOS에서 Primal은 NIP-46 서명 요청 수신을 위해 앱을 활성 상태로 유지하기 위해 백그라운드 오디오 재생을 사용합니다; 사용자는 설정에서 소리를 변경하거나 완전히 음소거할 수 있습니다.

**Mostro v0.15.6** - [NIP-69](/ko/topics/nip-69/) P2P 비트코인 거래 봇의 [최신 릴리스](https://github.com/MostroP2P/mostro/releases/tag/v0.15.6)는 Phase 4 감사 이벤트로 개발 펀드 구현을 완료합니다. 개발 수수료 지불은 이제 각 성공적인 지불 후 게시되는 kind 38383 Nostr 이벤트를 통해 추적되어 제3자 검증 및 분석이 가능합니다. 구매자/판매자 메시지에 대한 금액 계산이 수정되었고, 프리미엄 로직이 lnp2pbot 참조 구현과 일치하도록 조정되었습니다.

**Aegis v0.3.5** - 크로스 플랫폼 서명자가 [다크 모드를 추가](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.5)하고, 앱 아이콘 표시를 개선하고, 더 깔끔한 UI 레이아웃을 제공합니다. 버그 수정은 iOS iCloud Private Relay 충돌 및 이벤트 파싱 문제를 해결합니다. 이번 릴리스는 이벤트 JSON이 Rust 서명 함수에 전달되는 방식도 개선합니다.

**Citrine v1.0.0** - Android 릴레이 앱이 [1.0에 도달](https://github.com/greenart7c3/Citrine/releases/tag/v1.0.0)했습니다. Citrine은 Android 기기에서 직접 개인 Nostr 릴레이를 실행할 수 있게 해주며, 로컬 캐싱, 백업 또는 NIP-55 컴패니언으로 유용합니다. 이번 릴리스는 크래시 리포트 핸들러를 추가하고, 데이터베이스 쿼리 효율성을 개선하며, Crowdin을 통해 번역을 업데이트합니다.

**Applesauce v5.0.0** - hzrd149의 TypeScript 라이브러리 스위트가 정확성과 단순성에 초점을 맞춘 브레이킹 체인지와 함께 [메이저 버전을 출시](https://github.com/hzrd149/applesauce/releases)합니다. core 패키지는 이제 [기본적으로 이벤트 서명을 검증](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.0.0)하고 좌표 메서드를 더 명확한 "address" 용어를 사용하도록 이름을 변경합니다(`parseCoordinate` → `parseReplaceableAddress`). relay 패키지는 [기본 재시도를 10에서 3으로 낮추고](https://github.com/hzrd149/applesauce/releases/tag/applesauce-relay%405.0.0) 기본적으로 도달할 수 없는 릴레이를 무시하며, 더 간단한 이벤트 가져오기를 위한 `createUnifiedEventLoader`를 추가합니다. wallet 패키지는 [NIP-87](/ko/topics/nip-87/) [Cashu mint 검색](https://github.com/hzrd149/applesauce/releases/tag/applesauce-wallet%405.0.0)을 지원합니다. 패키지 전반에서 직접적인 `nostr-tools` 의존성이 제거되어 번들 크기와 버전 충돌이 감소했습니다.

## 주목할 만한 코드 및 문서 변경 사항

*이것들은 열린 풀 리퀘스트와 초기 단계 작업으로, 병합 전에 피드백을 받기에 완벽합니다. 관심이 가는 것이 있다면 리뷰나 코멘트를 고려해 보세요!*

### Damus (iOS)

일련의 PR이 장문 기사 경험을 개선합니다. [읽기 UX 개선](https://github.com/damus-io/damus/pull/3496)은 진행률 표시줄, 예상 읽기 시간, 세피아 모드, 조정 가능한 줄 높이, 스크롤 시 내비게이션을 숨기는 집중 모드를 추가합니다. [이미지 수정](https://github.com/damus-io/damus/pull/3489)은 마크다운 콘텐츠의 이미지가 독립 이미지를 블록 수준 요소로 전처리하여 적절한 종횡비로 표시되도록 합니다. [장문 미리보기 카드](https://github.com/damus-io/damus/pull/3497)는 인라인 `@naddr1...` 텍스트를 기사 제목과 메타데이터를 보여주는 풍부한 미리보기 카드로 대체합니다. 새로운 [릴레이 통합 테스트 스위트](https://github.com/damus-io/damus/pull/3508)는 [NIP-01](/ko/topics/nip-01/) 프로토콜 검증과 저하된 네트워크 조건(3G 시뮬레이션)에서의 동작을 포함한 137개의 네트워크 관련 테스트를 추가합니다.

### Bitchat (암호화 메시징)

iOS Nostr+Cashu 메신저의 보안 강화. [Noise 프로토콜 DH 비밀 클리어링](https://github.com/permissionlesstech/bitchat/pull/928)은 Diffie-Hellman 키 합의 후 공유 비밀이 제로화되지 않던 6곳을 수정하여 순방향 비밀성 보장을 복원합니다. [읽음 확인 큐에 대한 스레드 안전성](https://github.com/permissionlesstech/bitchat/pull/929)은 NostrTransport의 경쟁 조건을 방지하기 위한 배리어 동기화를 추가합니다. [메시지 중복 제거기 최적화](https://github.com/permissionlesstech/bitchat/pull/920)는 높은 메시지 볼륨에서 성능을 개선하고, [16진수 문자열 파싱 강화](https://github.com/permissionlesstech/bitchat/pull/919)는 잘못된 형식의 입력으로 인한 크래시를 방지합니다.

### Frostr (임계값 서명)

[FROST](/ko/topics/frost/) 기반 임계값 서명 프로토콜이 온보딩 중과 서명자 인터페이스에서 그룹 자격 증명 및 공유 자격 증명을 위한 [QR 코드 표시를 추가](https://github.com/FROSTR-ORG/igloo-desktop/pull/62)했습니다. 이를 통해 여러 기기에 키 공유를 배포할 때 사용자가 긴 문자열을 수동으로 복사하는 대신 자격 증명을 스캔할 수 있어 설정이 더 쉬워집니다.

### Marmot mdk (라이브러리)

위에서 언급한 보안 수정 외에도, 활성 PR들이 나머지 감사 결과를 해결합니다: [제로화를 위한 Secret<T> 타입](https://github.com/marmot-protocol/mdk/pull/109)은 드롭 시 민감한 데이터를 자동으로 제로화하는 래퍼 타입을 도입하고, [메시지 쿼리 페이지네이션](https://github.com/marmot-protocol/mdk/pull/111)은 채팅 기록을 로드할 때 메모리 고갈을 방지하며, [암호화된 스토리지](https://github.com/marmot-protocol/mdk/pull/102)는 그룹 상태와 메시지를 저장하는 SQLite 데이터베이스에 휴지 상태 암호화를 추가합니다.

### Amethyst (Android)

Android 클라이언트 전반의 바쁜 안정성 수정 주간. [관대한 JSON 파싱](https://github.com/vitorpamplona/amethyst/commit/2c42796)은 Kotlin Serialization을 더 관용적으로 만들어 잘못된 형식의 이벤트로 인한 크래시를 방지합니다. 이벤트 유효성 검사는 이제 과대한 값으로 인한 예외를 피하기 위해 처리 전에 [kind 필드 크기를 확인](https://github.com/vitorpamplona/amethyst/commit/40f9622)합니다. 신뢰 점수 UI는 시각적 간섭을 줄이기 위해 더 작은 아이콘을 받았고, [개선된 오류 로깅](https://github.com/vitorpamplona/amethyst/commit/69c53ac)은 릴레이 연결 문제 진단에 도움이 됩니다. Crowdin을 통한 번역 업데이트가 도착했고, 여러 SonarQube 경고가 해결되었습니다.

### TENEX (AI 에이전트)

Nostr 네이티브 AI 에이전트 프레임워크가 이번 주에 자율 기능을 구축하는 81개의 커밋을 보였습니다. 새로운 [에이전트 감독 시스템](https://github.com/tenex-chat/tenex/pull/48)은 에이전트 행동을 모니터링하고 필요할 때 개입하기 위한 행동 휴리스틱을 구현합니다. [위임 투명성](https://github.com/tenex-chat/tenex/commit/b244c10)은 위임 기록에 사용자 개입 로깅을 추가하여 사용자가 에이전트가 자신을 대신해 수행한 작업을 감사할 수 있게 합니다. [LLM 제공자 레지스트리](https://github.com/tenex-chat/tenex/pull/47)는 다른 AI 백엔드의 더 쉬운 통합을 위해 모듈화되었습니다. 크로스 프로젝트 대화 지원은 에이전트가 여러 Nostr 기반 프로젝트에서 컨텍스트를 유지할 수 있게 합니다.

### Jumble (웹 클라이언트)

릴레이 중심 웹 클라이언트가 여러 사용자 경험 개선을 추가했습니다. [스마트 릴레이 풀](https://github.com/CodyTseng/jumble/commit/695f2fe)은 사용 패턴에 따라 연결을 지능적으로 관리합니다. [라이브 피드 토글](https://github.com/CodyTseng/jumble/commit/917fcd9)은 사용자가 실시간 스트리밍과 수동 새로고침 사이를 전환할 수 있게 합니다. [새 노트 자동 표시](https://github.com/CodyTseng/jumble/commit/d1b3a8c)는 페이지 새로고침 없이 상단에 새 콘텐츠를 표시합니다. 팔로잉 피드와 알림을 위한 [영구 캐시](https://github.com/CodyTseng/jumble/commit/fd9f41c)는 재방문 시 로드 시간을 개선합니다. 사용자는 이제 설정을 통해 [기본 릴레이를 변경](https://github.com/CodyTseng/jumble/commit/53a67d8)할 수 있습니다.

---

이번 주는 여기까지입니다. 무언가를 만들고 계신가요? 공유할 뉴스가 있으신가요? 프로젝트를 다뤄주길 원하시나요? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DM으로 연락</a>하시거나 Nostr에서 찾아주세요.
