---
title: 'Nostr Compass #6'
date: 2026-01-21
publishDate: 2026-01-21
draft: false
type: newsletters
---

노스트 컴퍼스에 다시 방문해주셨습니다. 노스트의 주간 가이드입니다.

**이번 주:** Bitchat는 C Tor를 Rust Arti 구현으로 교체하여 더 나은 안정성과 성능을 제공합니다. nostrdb-rs는 제로 할당 데이터베이스 작업을 활성화하는 스트리밍 폴드 쿼리를 획득합니다. Listr는 1년 이상의 휴면 후 NDK 3 베타 마이그레이션과 AI 지원 유지보수로 대규모 리팩토링을 받습니다. Zeus는 [NIP-47](/ko/topics/nip-47/) (원격 라이트닝 제어를 위한 Nostr Wallet Connect) 수정사항 및 Cashu 개선에 중점을 둔 17개의 병합된 PR을 출시하며, Primal Android는 지갑 백업 흐름 및 [NIP-92](/ko/topics/nip-92/) (올바른 종횡비를 위한 미디어 치수) 지원을 추가합니다. 새로운 드래프트 NIP는 표준화된 리레이 신뢰도 점수 매기기를 위해 [Trusted Relay Assertions](/ko/topics/trusted-relay-assertions/)를 제안합니다.

## 뉴스

### Bitchat가 Tor 지원을 위해 Rust Arti로 이동

Bitchat는 C Tor에서 Tor 프로토콜의 Rust 구현인 [Arti](https://gitlab.torproject.org/tpo/core/arti)로 마이그레이션했습니다. [PR #958](https://github.com/permissionlesstech/bitchat/pull/958)은 C Tor 의존성을 제거하고 Arti를 통합하여 메모리 안전성 보장과 개선된 안정성을 제공합니다. 이 변경은 foreground 서비스 재시작을 야기한 휴면 웨이크 시도를 제거하여 C 구현의 오래된 문제를 해결합니다.

**사용자에게 미치는 영향:** 더 안정적인 암호화 메시징과 특히 모바일 기기에서 연결 해제가 적어집니다. Rust 구현은 충돌 위험을 감소시키고 지속적인 재연결 시도로 인한 배터리 소비를 줄입니다.

Arti는 Tor 프로토콜의 Rust로 완전히 다시 작성된 것으로 Tor 프로젝트에서 메모리 안전성을 통해 더 나은 보안을 제공하고 애플리케이션으로의 통합을 용이하게 하기 위해 개발되었습니다. Bitchat의 경우 메모리 안전성 특성은 암호화된 메시지와 리레이 연결을 처리할 때 공격 표면을 감소시킵니다. 이 마이그레이션은 팀의 최근 [Cure53 보안 감사](/ko/newsletters/2026-01-13-newsletter/#bitchat-completes-cure53-security-audit) (뉴스레터 #5에서 다룬)를 따르며 보안 개선을 계속합니다.

이 PR은 또한 ChatViewModel 및 BLEService에 대한 포괄적인 테스트 범위를 도입하고, 죽은 코드를 제거하며, 테스트 스위트를 안정화합니다. Bluetooth Low Energy 메시 안정성 개선이 Tor 변경과 함께 제공되어 대규모 전송 실패를 해결합니다. 이러한 변경들은 Tor가 인터넷 연결을 제공하는 오프라인 메시 네트워킹 시나리오에서 Bitchat의 복원력을 개선합니다.

### Listr가 AI 기반 유지보수로 되살아남

JeffG는 1년 이상 휴면 상태였던 노스트 리스트 관리 애플리케이션 [Listr](https://github.com/erskingardner/listr)의 대규모 리팩토링을 발표했습니다. AI 지원을 사용하여 [NDK](https://github.com/nostr-dev-kit/ndk) 3 베타로의 마이그레이션, Svelte 및 Vite의 최신 버전으로의 업데이트, 모든 의존성을 현재 상태로 업데이트하는 포괄적인 업그레이드를 완료했습니다. 리팩토링은 팔로우 팩에 대한 1급 지원을 추가하고, 50개 항목을 초과하는 리스트에 대한 페이지 매김을 구현하며, 휴면 기간 동안 누적된 많은 버그를 수정합니다.

**사용자에게 미치는 영향:** Listr는 팔로우 리스트, 콘텐츠 모음 및 주제 큐레이션을 관리하기 위한 개선된 성능과 새로운 기능으로 다시 온라인 상태입니다. 페이지 매김 수정은 대규모 리스트를 실제로 사용 가능하게 만듭니다.

JeffG는 AI 지원 없이는 이 유지보수 작업이 발생했을 가능성이 낮으며, 프로젝트가 버려지는 것을 방지한다고 언급했습니다. Listr는 노스트에서 콘텐츠 큐레이션을 활성화하여 사용자가 프로필, 주제 및 리소스의 리스트를 생성, 관리 및 공유할 수 있게 합니다. 업그레이드는 목록 관리가 프로토콜의 콘텐츠 발견의 중심이 됨에 따라 애플리케이션을 현재 노스트 표준 및 클라이언트 예상과 호환되게 유지합니다.

## NIP 업데이트

[NIPs 리포지토리](https://github.com/nostr-protocol/nips)의 최근 변경 사항:

**병합됨:**

- **[NIP-29](/ko/topics/nip-29/)** (Relay 기반 그룹) - Relay Key 명확화 ([#2190](https://github.com/nostr-protocol/nips/pull/2190) - 병합됨)는 relay 키가 relay URL 자체이지 pubkey가 아니라는 것을 명확히 합니다. 명세서는 이제 명시적으로 "relay 키는 relay의 WebSocket URL입니다 (예: wss://groups.example.com)"라고 명시하여 혼동을 피합니다. 이는 클라이언트가 주어진 그룹을 호스트하는 relay를 식별하는 방식에 영향을 미쳐 그룹이 호스팅 relay에 제대로 속하도록 합니다.

**공개 PR 및 토론:**

- **Trusted Relay Assertions** - 드래프트 NIP는 [NIP-66](/ko/topics/nip-66/) (relay 발견 및 모니터링) 메트릭, 운영자 평판 및 사용자 보고서에서 계산된 신뢰 점수 (0-100)를 포함하는 kind 30385 이벤트를 통해 relay 신뢰도 점수 매기기를 표준화할 것을 제안합니다. 명세서는 신뢰를 신뢰도 (가동 시간, 대기 시간), 품질 (TLS, 문서, 운영자 검증) 및 접근성 (관할권, 장벽, 감시 위험) 구성 요소로 나눕니다. 운영자 검증은 [NIP-11](/ko/topics/nip-11/) (relay 정보 문서)을 통한 암호화 서명, DNS TXT 레코드 및 .well-known 파일을 포함합니다. 사용자는 kind 10385 이벤트를 통해 신뢰할 수 있는 주장 제공자를 선언하여 클라이언트가 다양한 관점을 위해 여러 제공자를 쿼리할 수 있도록 합니다. 제안은 [NIP-66](/ko/topics/nip-66/) 발견과 평가를 보완하여 [NIP-46](/ko/topics/nip-46/) (원격 서명/Nostr Connect)이 연결 URI의 relay 신뢰성을 평가하는 데 도움을 줍니다.

- **Post-Quantum Cryptography** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) (공개)는 [뉴스레터 #5](/ko/newsletters/2026-01-13-newsletter/#nip-updates)에서 양자 저항 알고리즘 제안이 도입된 이후로 계속 진화합니다. 이번 주 토론은 암호화 민첩성을 위한 구현 세부 사항에 중점을 두었습니다: 마이그레이션 중에 클라이언트가 이중 서명을 처리하는 방식, 오래된 클라이언트의 역호환성, 더 큰 양자 저항 서명의 성능 함의. 기여자들은 ML-DSA-44만 의무화할지 또는 유연성을 위해 여러 알고리즘 (ML-DSA-44, Falcon-512, Dilithium)을 지원할지에 대해 논쟁했습니다. 합의는 단계적 접근 방식을 향하고 있습니다: 초기에는 선택적 양자 서명이며, 광범위한 클라이언트 지원과 실제 양자 위협의 출현 이후에만 의무화됩니다.

## NIP 깊이 분석: NIP-11 및 NIP-66

이번 주 relay 발견 및 평가를 활성화하는 두 개의 NIP를 살펴봅니다: NIP-11은 relay가 자신을 설명하는 방법을 정의하고, NIP-66은 relay 동작을 측정하는 방법을 표준화합니다. 함께 relay 신뢰도 평가 시스템의 기초를 형성합니다.

### [NIP-11](/ko/topics/nip-11/): Relay 정보 문서

[NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md)는 relay가 HTTP를 통해 제공하는 JSON 문서를 정의하여 기능, 정책 및 운영자 정보를 설명합니다. 클라이언트가 `wss://relay.example.com`에 연결할 때, 릴레이의 정보 문서를 검색하기 위해 `https://relay.example.com` (`wss://`를 `https://`로 대체)을 가져올 수 있습니다.

문서는 `Accept: application/nostr+json` 헤더와 함께 표준 HTTP 콘텐츠 협상을 사용합니다. 이는 relay가 브라우저에 일반 웹사이트를 제공하는 동시에 Nostr 클라이언트에 기계 읽기 가능한 메타데이터를 제공할 수 있게 합니다. 응답에는 relay 소프트웨어 이름 및 버전, 운영자 연락처 정보 (pubkey, 이메일, 대체 연락처), 지원되는 NIP 및 결제 요구사항 또는 콘텐츠 제한과 같은 운영 매개변수가 포함됩니다.

중요하게도 기본 NIP-11 문서는 HTTPS를 통해 제공되는 서명되지 않은 JSON으로 인증을 위해 전적으로 TLS 인증서에 의존합니다. 이는 relay의 웹 서버를 제어하는 모든 사람이 문서를 수정할 수 있음을 의미하므로 운영자 주장을 확인할 수 없습니다. Trusted Relay Assertions 제안은 relay의 `self` pubkey 필드를 통한 서명된 증명을 도입하여 relay가 인증 메커니즘에 서명된 이벤트를 사용하는 방식과 유사하게 운영자 정체성의 암호화 증명을 가능하게 함으로써 이 격차를 해결합니다.

```json
{
  "name": "relay.example.com",
  "description": "A general-purpose public relay",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "contact": "admin@example.com",
  "supported_nips": [1, 2, 4, 9, 11, 12, 16, 20, 22],
  "software": "git+https://github.com/relay/relay.git",
  "version": "1.2.3",
  "limitation": {
    "max_message_length": 16384,
    "max_subscriptions": 20,
    "max_filters": 100,
    "max_limit": 5000,
    "max_subid_length": 100,
    "min_prefix": 4,
    "max_event_tags": 2000,
    "max_content_length": 8196,
    "min_pow_difficulty": 0,
    "auth_required": false,
    "payment_required": false
  },
  "payments_url": "https://relay.example.com/payments",
  "fees": {
    "admission": [{"amount": 5000, "unit": "msats"}],
    "subscription": [{"amount": 1000, "unit": "msats", "period": 2592000}],
    "publication": []
  }
}
```

`limitation` 객체는 클라이언트에게 relay가 시행하는 제약 조건을 알립니다. `max_message_length`는 WebSocket 프레임 크기를 제한하고, `max_subscriptions`은 연결당 동시 REQ 구독을 한정하며, `max_filters`는 REQ당 필터를 제한하고, `max_limit`은 단일 필터가 요청할 수 있는 이벤트 수를 제약합니다. 이러한 매개변수는 클라이언트가 relay 기능에 맞게 동작을 적응하도록 도와 제한을 초과하여 연결을 끊는 것을 피합니다.

결제 정보는 `fees` 및 `payments_url`에 나타납니다. Relay는 허가 (일회성 액세스), 구독 (반복 액세스) 또는 게시 (이벤트당 수수료)에 대해 요금을 청구할 수 있습니다. `payments_url`은 일반적으로 라이트닝 인보이스 또는 ecash 민트에 대한 세부 사항을 가리킵니다. 유료 relay는 이 필드를 사용하여 클라이언트가 인증을 시도하기 전에 가격을 전달합니다.

`supported_nips` 배열은 클라이언트가 relay 기능을 발견할 수 있게 합니다. relay가 [NIP-50](/ko/topics/nip-50/)을 나열하면, 클라이언트는 전체 텍스트 검색 쿼리를 보낼 수 있음을 알고 있습니다. [NIP-42](/ko/topics/nip-42/)가 나타나면, 클라이언트는 인증 도전을 예상해야 합니다. 이 선언적 기능 광고는 점진적 개선을 활성화합니다: 클라이언트는 사용 가능한 고급 기능을 사용하는 동시에 제한된 지원이 있는 relay에서 정상적으로 저하됩니다.

운영자 정보는 책임성을 구축합니다. `pubkey` 필드는 relay 운영자를 노스트에서 식별하여 [NIP-17](/ko/topics/nip-17/) DM이나 공개 언급을 통한 직접 통신을 가능하게 합니다. `contact` 이메일은 오프 프로토콜 폴백을 제공합니다. 함께 이 필드들은 사용자가 남용 보고, 액세스 요청 또는 기술 문제에 대해 운영자에게 도달하도록 도웁니다.

[NIP-11](/ko/topics/nip-11/) 문서는 자체 보고됩니다: relay는 실제로 무엇을 하는지가 아니라 지원한다고 주장하는 것을 설명합니다. NIP-66이 중요해지는 곳입니다.

### [NIP-66](/ko/topics/nip-66/): Relay 발견 및 생성력 모니터링

[NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md)는 노스트에 relay 모니터링 데이터를 게시하는 것을 표준화합니다. 모니터 서비스는 가용성, 대기 시간, 프로토콜 준수 및 지원되는 NIP에 대해 relay를 지속적으로 테스트합니다. 그들은 결과를 kind 30166 이벤트로 게시하여 relay 자체 보고에 독립적인 실시간 relay 상태를 제공합니다.

모니터는 연결 및 테스트 구독 전송을 통해 relay 가용성을 확인합니다. 대기 시간 측정은 연결 시간, 구독 응답 시간 및 이벤트 전파 지연을 추적합니다. 프로토콜 준수 테스트는 relay 동작이 명세와 일치하는지 확인하여 구현 버그나 의도적인 편차를 포착합니다. NIP 지원 확인은 [NIP-11](/ko/topics/nip-11/) 주장을 넘어 실제로 광고된 기능이 올바르게 작동하는지 테스트합니다.

```json
{
  "id": "a34b5c7d89e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7",
  "pubkey": "4e2d0bc6f8e7c3a5b9f1d2e3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4",
  "created_at": 1736784000,
  "kind": 30166,
  "tags": [
    ["d", "wss://relay.example.com"],
    ["rtt", "open", "143", "1736784000"],
    ["rtt", "read", "89", "1736784000"],
    ["rtt", "write", "92", "1736784000"],
    ["nips", "1", "2", "4", "9", "11", "12"],
    ["geo", "US", "United States", "New York"],
    ["other", "network", "clearnet"],
    ["other", "payment_required", "false"],
    ["other", "auth_required", "false"]
  ],
  "content": "{\"last_check\": 1736784000, \"checks\": 8760}",
  "sig": "8b9c4d5e6a7f8b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b"
}
```

`d` 태그는 relay URL을 포함하여 이를 매개변수화된 교체 가능한 이벤트로 만듭니다. 각 모니터는 relay당 하나의 이벤트를 게시하며, 측정값이 변경될 때 업데이트합니다. 여러 모니터가 동일한 relay를 추적할 수 있어 중복성과 교차 검증을 제공합니다. 클라이언트는 relay 상태에 대한 다양한 관점을 얻기 위해 여러 모니터 pubkey를 쿼리합니다.

왕복 시간 (rtt) 태그는 다양한 작업에 대한 대기 시간을 측정합니다. `rtt open`은 WebSocket 연결 설정을 추적하고, `rtt read`는 구독 응답 시간을 측정하며, `rtt write`는 이벤트 게시 속도를 테스트합니다. 모든 값은 밀리초 단위입니다. 클라이언트는 이러한 메트릭을 사용하여 시간 민감한 작업을 위해 낮은 대기 시간 relay를 선호하거나 느린 relay를 폄하합니다.

`nips` 태그는 주장된 지원이 아닌 실제로 확인된 NIP 지원을 나열합니다. 모니터는 기능을 행사하여 각 NIP를 테스트합니다. relay가 [NIP-11](/ko/topics/nip-11/) 문서에서 [NIP-50](/ko/topics/nip-50/) 검색을 주장하지만 검색 쿼리가 실패하면, 모니터는 확인된 목록에서 NIP-50을 생략합니다. 이는 relay 기능에 대한 기초 사실을 제공합니다.

지리적 정보는 클라이언트가 더 나은 대기 시간과 검열 저항을 위해 근처 relay를 선택할 수 있게 합니다. `geo` 태그는 국가 코드, 국가 이름 및 지역을 포함합니다. `network` 태그는 clearnet relay를 Tor 숨겨진 서비스 또는 I2P 끝점과 구별합니다. 함께 이 태그들은 지리적 다양성을 활성화합니다: 클라이언트는 지역 검열에 저항하기 위해 여러 관할권의 relay에 연결할 수 있습니다.

모니터 데이터는 클라이언트의 relay 선택기, 탐색기 웹사이트 및 Trusted Relay Assertions 제안을 제공합니다. 자체 보고 [NIP-11](/ko/topics/nip-11/) 문서를 측정된 [NIP-66](/ko/topics/nip-66/) 데이터 및 계산된 신뢰 주장과 결합하여 생태계는 하드코딩된 기본값 또는 입소문 권장사항에 의존하는 것 대신 정보 있는 relay 선택으로 이동합니다.

## 릴리스

### 0xchat v1.5.3 - 향상된 메시징 기능

[0xchat v1.5.3](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.3-release)는 Telegram 스타일의 노스트 메시징 클라이언트에 상당한 개선을 제공합니다. 릴리스는 Amber 같은 외부 서명자를 통한 적절한 이벤트 서명을 방지하고 있던 [NIP-55](/ko/topics/nip-55/) (Android 서명자 애플리케이션) 준수 문제를 해결합니다. 완전한 준수는 0xchat이 이제 서명 작업을 올바르게 위임하여 보안을 개선하고 개인 키를 격리 상태로 유지함을 의미합니다.

업데이트는 FileDropServer 및 BlossomServer를 모두 기본 미디어 저장 옵션으로 통합하여 파일 업로드에 대한 중복성을 제공합니다. [Blossom](https://github.com/hzrd149/blossom)은 파일이 SHA-256 해시로 참조되는 콘텐츠 주소 지정 저장소를 제공하여 무결성을 보장하고 네트워크 전체에서 중복 제거를 활성화합니다. Moments에 대한 자동 초안 저장은 긴 형식 콘텐츠를 작성할 때 데이터 손실을 방지하여 앱 전환 또는 연결 중단 중 손실된 게시물에 대한 사용자 불만을 해결합니다.

Cashu 지갑 통합은 지갑 보기에서 소비된 토큰을 제거하는 자동 증명 필터링으로 연구됩니다. 이는 사용자가 유효한 증명과 함께 유효하지 않은 증명을 본 혼동스러운 사용자 경험을 해결하여 잔액 계산을 신뢰할 수 없게 만듭니다. 필터링은 클라이언트 측에서 발생하며 채팅 내 P2P 트랜잭션에 대한 결제 경험을 개선하는 동시에 개인정보 보호를 유지합니다.

### Amber v4.1.0 Pre-releases - UI 오버홀

[Amber v4.1.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre1)부터 [v4.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre3)까지는 인기 있는 Android 이벤트 서명자를 위한 재설계된 인터페이스를 도입합니다. 로그인 화면은 이제 어떤 애플리케이션이 서명 권한을 요청하는지 명확하게 표시하여 인증 흐름에 대한 사용자 혼동을 해결합니다. 새 이벤트 화면은 애플리케이션이 서명하기를 원하는 데이터를 자세히 검사할 수 있게 하여 사용자가 작업을 승인하기 전에 정보 있는 보안 결정을 내릴 수 있도록 합니다.

권한 관리는 각 연결된 애플리케이션에 부여된 기능을 정확히 보여주는 개선된 인터페이스로 상당한 주의를 받습니다. 사용자는 완전히 연결을 해제하지 않고도 특정 권한을 취소할 수 있어 서명 위임에 대한 세분화된 제어를 활성화합니다. 업데이트된 quartz 라이브러리를 사용하는 리팩토링된 relay 카운터는 이벤트 처리량 및 relay 성능에 대한 실시간 통계를 제공합니다. [NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) (Nostr Connect) bunker 연결은 이제 연결 실패 시 상세한 오류 메시지를 표시하여 암호화된 타임아웃 오류를 실행 가능한 진단으로 대체합니다.

## 주목할 만한 코드 및 문서 변경사항

*이들은 병합된 풀 요청 및 추적할 가치가 있는 초기 단계 개발입니다. 일부는 릴리스 전에 진화할 수 있는 실험적 기능입니다.*

### Zeus (라이트닝 지갑 Nostr Wallet Connect 포함)

Zeus는 이번 주 17개의 풀 요청을 병합하여 주요 [NIP-47](/ko/topics/nip-47/) Nostr Wallet Connect 구현으로서의 위치를 강화합니다. 가장 중요한 수정사항은 Nostr 클라이언트와의 상호 운용성 문제를 야기하고 있던 데이터 일관성 및 프로토콜 준수 문제를 해결합니다.

**트랜잭션 기록 수정** - [PR #3542](https://github.com/ZeusLN/zeus/pull/3542)는 NWC 트랜잭션 목록이 잘못되거나 중복된 항목을 표시한 중대한 버그를 해결합니다. 문제는 Zeus가 이벤트 업데이트를 적절히 처리하지 않으면서 트랜잭션 데이터를 캐시할 때 발생하여 사용자가 유령 트랜잭션을 보거나 누락된 결제를 봅니다. 수정사항은 적절한 이벤트 중복 제거 및 캐시 무효화를 구현하여 트랜잭션 기록이 라이트닝 노드 상태를 정확하게 반영하도록 합니다.

**프로토콜 준수** - [PR #3548](https://github.com/ZeusLN/zeus/pull/3548)은 완전한 NIP-47 준수를 예상하는 클라이언트와의 호환성을 깬 불완전한 `getInfo` 응답을 해결합니다. 일부 노스트 클라이언트는 `block_height` 또는 `network` 같은 필드가 누락된 부분 응답을 받을 때 충돌합니다. PR은 모든 필수 필드가 기본 기본값으로도 반환되도록 보장하여 기본 라이트닝 구현이 제공하지 않더라도 생태계 전반의 Zeus 호환성을 개선합니다.

**연결 복원력** - [PR #3543](https://github.com/ZeusLN/zeus/pull/3543)은 정지된 노스트 연결에 대한 타임아웃 알림을 구현합니다. 이전에는 사용자가 relay 연결이 조용히 떨어졌을 때 무한정 기다렸습니다. 이제 Zeus는 30초 동안 활동이 없은 후 명확한 타임아웃 메시지를 표시하여 사용자가 재시도하거나 relay를 전환할 수 있게 합니다. [PR #3541](https://github.com/ZeusLN/zeus/pull/3541)은 NWC가 호환되지 않는 라이트닝 구현에서 활성화되는 것을 방지하기 위해 백엔드 검증을 추가하여 런타임 충돌을 일으키기 전에 구성 오류를 포착합니다.

**Cashu 경합 조건** - [PR #3531](https://github.com/ZeusLN/zeus/pull/3531)은 동시 민트 작업이 토큰 데이터베이스를 손상시킬 수 있는 Cashu 토큰 관리의 동시성 버그를 수정합니다. 경합 조건은 여러 스레드가 적절한 잠금 없이 토큰 개수를 업데이트할 때 발생하여 때때로 잘못된 잔액을 초래합니다. 수정사항은 중요 섹션 주위에 mutex 보호를 추가하여 토큰 상태에 대한 원자적 업데이트를 보장합니다.

### Primal Android (클라이언트)

Primal Android는 지갑 보안 및 미디어 처리에 대한 중요한 개선과 함께 12개의 병합된 PR을 출시했습니다. 지갑 백업 구현은 가장 요청된 기능 중 하나를 해결하는 반면 NIP-92 지원은 애플리케이션 전체의 시각적 경험을 개선합니다.

**지갑 백업 시스템** - 4-PR 시리즈 ([#844](https://github.com/PrimalHQ/primal-android-app/pull/844), [#845](https://github.com/PrimalHQ/primal-android-app/pull/845), [#846](https://github.com/PrimalHQ/primal-android-app/pull/846), [#848](https://github.com/PrimalHQ/primal-android-app/pull/848))는 포괄적인 시드 구문 백업 기능을 구현합니다. 사용자는 이제 스크린샷을 방지하는 보안 흐름을 통해 12단어 니모닉을 내보낼 수 있으며, 지갑 대시보드에 백업 상태를 표시하고, 기존 사용자를 마이그레이션을 통해 안내합니다. 구현은 BIP-39 표준을 따르고 사용자가 부정확한 구문 기록으로 인해 자금을 잃는 것을 방지하기 위한 검증을 포함합니다.

**미디어 치수 (NIP-92)** - [PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718)은 올바른 이미지 및 비디오 종횡비에 대한 [NIP-92](/ko/topics/nip-92/) 지원을 구현합니다. 치수 메타데이터 없이 클라이언트는 콘텐츠가 로드될 때 이미지를 다운로드하여 레이아웃 점프를 야기합니다. NIP-92는 `dim` 태그 (예: `["dim", "1920x1080"]`)를 파일 메타데이터 이벤트에 추가하여 Primal이 미디어를 다운로드하기 전에 올바른 공간을 예약할 수 있게 합니다. 이는 이미지 갤러리에서 불안한 리플로우를 제거하고 인지된 성능을 개선합니다.

**원격 서명자 신뢰도** - [PR #841](https://github.com/PrimalHQ/primal-android-app/pull/841)은 누락된 `wss://` 접두어가 조용한 실패를 야기한 [NIP-46](/ko/topics/nip-46/) 연결 문제를 수정합니다. PR은 bunker 연결 설정 중에 relay URI를 검증하여 사용자가 베어 도메인을 붙여 넣을 때 프로토콜 접두어를 자동으로 추가합니다. [PR #843](https://github.com/PrimalHQ/primal-android-app/pull/843)은 나쁜 네트워크 조건이 회신이 루트 노트로 게시되도록 야기한 스레딩 버그를 해결하여 대화 흐름을 끊습니다. 수정사항은 네트워크 중단을 통해 부모 이벤트 ID가 지속되도록 보장합니다.

### Marmot Protocol: White Noise (암호화된 그룹 채팅 라이브러리)

[Marmot](/ko/topics/marmot/) Protocol의 암호화된 그룹 채팅을 구동하는 Rust 라이브러리인 White Noise는 사용자 경험 및 보안을 개선하는 6개의 PR을 병합했습니다. 변경사항은 Marmot을 주류 메시징 애플리케이션과의 기능 패리티에 더 가깝게 가져오는 동시에 개인정보 보호 우선 아키텍처를 유지합니다.

**읽음 확인** - [PR #433](https://github.com/marmot-protocol/whitenoise-rs/pull/433) 및 [#436](https://github.com/marmot-protocol/whitenoise-rs/pull/436)은 그룹 대화를 위한 메시지 읽음 추적을 구현합니다. 시스템은 단일 장치 내에서 그룹당 사용자당 읽음 위치를 저장하여 미읽음 개수 배지를 활성화합니다. 구현은 각 대화에 대한 마지막 읽음 메시지 위치를 추적하기 위해 단조적 타임스탬프를 사용합니다. 이 기초 기능은 미읽음 메시지 개수 per 대화를 보여주는 UI 지시자를 활성화합니다.

**대화 고정** - [PR #442](https://github.com/marmot-protocol/whitenoise-rs/pull/442)는 계정을 그룹에 연결하는 `accounts_groups` junction 테이블의 `pin_order` 필드를 통한 지속적인 대화 고정을 추가합니다. 고정된 대화는 메시지 활동과 관계없이 채팅 목록의 상단에 위치를 유지하여 Signal 및 WhatsApp의 사용자 예상과 일치합니다. 구현은 정수 정렬을 사용하여 무제한 핀을 결정론적 정렬로 허용합니다.

**결정론적 커밋 해석 (MIP-03)** - [PR #152](https://github.com/marmot-protocol/mdk/pull/152) (공개)는 분산 그룹 채팅에서 커밋 경합 조건의 중대한 문제를 해결하는 Marmot 개선 제안 03을 구현합니다. 여러 멤버가 그룹 상태 변경 (구성원 추가/제거, 권한 변경)을 동시에 제출할 때, 클라이언트는 커밋 정렬에 달라질 수 있어 그룹을 호환되지 않는 상태로 단편화합니다. MIP-03은 에포크 스냅샷과 결정론적 우승자 선택을 도입합니다: 가장 이른 `created_at` 타임스탬프가 있는 커밋이 이기며, 사전식 이벤트 ID가 타이브레이커입니다. 이는 모든 클라이언트가 롤백 및 재생을 통해 동일한 상태로 수렴할 수 있게 하여 네트워크 분할 중에도 그룹 일관성을 유지합니다.

**보안 강화** - [PR #443](https://github.com/marmot-protocol/whitenoise-rs/pull/443)은 `resolve_group_image_path`에서 참조를 사용하여 암호화 비밀의 불필요한 복사를 방지합니다. 이는 비밀이 해제된 힙 할당에서 복구될 수 있는 메모리 공격 윈도우를 줄입니다. [PR #438](https://github.com/marmot-protocol/whitenoise-rs/pull/438)은 keyring 매개변수를 통한 SQLCipher 데이터베이스 암호화를 활성화하여 메시지 기록을 보호합니다. keyring 통합은 구성 파일 대신 플랫폼 키체인에서 보안 키 저장을 허용합니다.

### nostrdb-rs (데이터베이스 라이브러리) - 공개 PR

**스트리밍 쿼리 구현** - [PR #58](https://github.com/damus-io/nostrdb-rs/pull/58) (공개)는 제로 할당 데이터베이스 작업을 활성화하는 스트리밍 폴드 쿼리를 제안합니다. 구현은 벡터로 전체 결과 세트를 구체화하지 않고 데이터베이스 결과를 한 번에 하나씩 처리하는 `fold`, `try_fold`, `count`, `any`, `all` 및 `find_map` 메서드를 추가합니다. 이 접근 방식은 메모리 소비를 감소시키고 일반적인 쿼리 패턴에 대한 조기 종료를 활성화합니다.

기술적 구현은 낮은 수준의 쿼리 결과 콜백 (`ndb_query_visit`)을 `ControlFlow` 변형을 C 방문자 작업으로 매핑하는 상태 저장 Rust 방문자로 노출합니다. 병합되면, 애플리케이션 코드는 반복자 로직처럼 읽히는 동시에 데이터베이스 계층 근처에서 실행됩니다. 예를 들어, 일치하는 노트를 세는 것은 그들을 수집하는 대신 결과를 통해 스트림하며, `find_map`은 나머지 행을 처리하지 않고 첫 번째 유용한 결과를 반환합니다.

nostrdb는 Damus 및 Notedeck (각각 iOS/macOS 및 데스크톱 클라이언트)을 구동합니다. 스트리밍 쿼리는 페이지 매김, 조건부 필터링 및 존재 확인과 같은 효율적인 패턴을 활성화합니다. PR은 쿼리 계층의 상당한 리팩토링인 3개 파일을 +756 추가 및 -32 삭제로 변경합니다. nostrdb-rs 기반 애플리케이션의 사용자는 대규모 타임라인을 탐색하거나 광범위한 이벤트 데이터베이스를 검색할 때 감소된 메모리 사용량을 볼 것입니다.

### nak (CLI 도구)

fiatjaf의 명령줄 노스트 도구인 nak는 빌드 시스템 개선 및 새 기능에 중점을 둔 6개의 PR을 병합했습니다. [PR #91](https://github.com/fiatjaf/nak/pull/91)은 nak이 Blossom 미디어 서버의 미러로 역할하도록 하는 Blossom 미러 기능을 구현합니다. [Blossom](/ko/topics/blossom/)은 노스트 이벤트와 함께 작동하는 콘텐츠 주소 지정 미디어 저장소 프로토콜입니다.

나머지 PR은 Windows, macOS 및 Linux 플랫폼 전반의 빌드 시스템 호환성을 해결하여 노스트 이벤트를 로컬 디렉토리로 마운트하기 위한 FUSE 파일 시스템 지원을 활성화합니다.

### Damus (iOS 클라이언트) - 공개 PR

Damus는 중요한 아키텍처 개선을 탐색하는 11개의 공개 PR을 가지고 있습니다. 이들은 아직 병합되지 않았지만 개인정보 보호, 동기화 효율성 및 모바일 데이터 최적화 주변의 iOS 노스트 클라이언트 개발에 대한 중요한 방향을 신호합니다.

**Tor 통합** - [PR #3535](https://github.com/damus-io/damus/pull/3535)는 Arti Tor 클라이언트를 Damus에 직접 내장하여 외부 의존성 없이 익명 relay 연결을 활성화합니다. Orbot 또는 Tor Browser 접근 방식과는 달리 Arti 내장은 iOS 샌드박싱 및 백그라운드 실행 제한과의 매끄러운 통합을 제공합니다. Rust 구현은 네트워크 익명화에 메모리 안전성을 제공하여 C Tor에 비해 공격 표면을 감소시킵니다. 사용자는 relay당 또는 전역적으로 Tor 모드를 전환할 수 있으며, 클라이언트는 회로 관리를 투명하게 처리합니다.

**Negentropy 동기화 프로토콜** - [PR #3536](https://github.com/damus-io/damus/pull/3536)은 동기화 효율성을 급격히 개선하는 set 조정 프로토콜인 Negentropy를 구현합니다. 마지막 연결 이후 모든 이벤트를 다운로드하는 대신, Negentropy는 클라이언트와 relay 사이의 정확히 어떤 이벤트가 다른지 식별하기 위해 콤팩트 핑거프린트 (Merkle 트리)를 교환합니다. 수백 명의 pubkey를 따르는 사용자의 경우, 이는 동기화 대역폭을 메가바이트에서 킬로바이트로 감소시킵니다. 구현은 RelayPool 및 SubscriptionManager와 통합하여 모든 연결된 relay 전체에서 자동 효율적 동기화를 활성화합니다.

**낮은 데이터 모드** - [PR #3549](https://github.com/damus-io/damus/pull/3549)는 사용자 피드백에 응하는 셀룰러 데이터 절약 기능을 추가합니다. 모드는 이미지 자동 로딩, 비디오 사전 로딩을 비활성화하고 구독 제한을 감소시킵니다. 계량된 연결의 사용자는 데이터 한도를 초과할 우려 없이 텍스트 콘텐츠를 탐색할 수 있습니다. 구현은 iOS 낮은 데이터 모드 설정을 존중하고 다양한 미디어 유형에 대한 세분화된 제어를 제공합니다.

**데이터베이스 최적화** - [PR #3548](https://github.com/damus-io/damus/pull/3548)은 더 빠른 쿼리 및 감소된 디스크 사용량을 위해 nostrdb 스냅샷 저장소를 다시 작업합니다. 최적화는 데이터베이스 스냅샷이 디스크에 지속되는 방식을 변경하여 읽기 성능과 쓰기 증폭을 모두 개선합니다. 이는 대규모 이벤트 데이터베이스를 가진 사용자로부터의 배터리 소비 불만을 해결합니다.

---

이번 주는 여기까지입니다. 뭔가 만들고 있나요? 공유할 뉴스가 있나요? 우리가 당신의 프로젝트를 다루기를 원하나요? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DM을 통해 연락하세요</a> 또는 노스트에서 우리를 찾으세요.
