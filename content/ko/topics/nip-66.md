---
title: "NIP-66: Relay 발견 및 활성 모니터링"
date: 2026-01-21
translationOf: /en/topics/nip-66.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Relays
---

NIP-66은 relay 모니터링 데이터를 Nostr에 게시하는 것을 표준화합니다. 모니터 서비스는 relay의 가용성, 지연 시간, 프로토콜 준수, 지원되는 NIP를 지속적으로 테스트하고 결과를 kind 30166 event로 게시합니다.

## 작동 방식

모니터는 연결하고 테스트 구독을 보내 relay 가용성을 확인합니다. 지연 시간 측정은 연결 시간, 구독 응답 시간, event 전파 지연을 추적합니다. 프로토콜 준수 테스트는 relay 동작이 명세와 일치하는지 확인하여 구현 버그나 의도적인 편차를 감지합니다.

NIP 지원 검증은 실제로 광고된 기능이 올바르게 작동하는지 테스트하여 [NIP-11](/ko/topics/nip-11/) 주장을 넘어섭니다. Relay가 [NIP-50](/ko/topics/nip-50/) 검색 지원을 주장하지만 검색 쿼리가 실패하면, 모니터는 검증된 목록에서 NIP-50을 제외합니다. 이는 relay 기능에 대한 실제 정보를 제공합니다.

Kind 30166 event는 relay URL을 `d` 태그로 사용하여 파라미터화 교체 가능 event로 만듭니다. 각 모니터는 relay당 하나의 event를 게시하고 측정값이 변경되면 업데이트합니다. 여러 모니터가 동일한 relay를 추적하여 중복성과 교차 검증을 제공할 수 있습니다.

왕복 시간(rtt) 태그는 다양한 작업에 대한 지연 시간을 측정합니다:
- `rtt open`: WebSocket 연결 설정
- `rtt read`: 구독 응답 시간
- `rtt write`: Event 게시 속도

모든 값은 밀리초 단위입니다. 클라이언트는 이 메트릭을 사용하여 시간에 민감한 작업에 저지연 relay를 선호합니다.

지리적 정보는 클라이언트가 더 나은 지연 시간과 검열 저항을 위해 근처 relay를 선택하는 데 도움이 됩니다. `geo` 태그에는 국가 코드, 국가 이름, 지역이 포함됩니다. `network` 태그는 clearnet relay를 Tor 히든 서비스나 I2P 엔드포인트와 구별합니다.

## 사용 사례

모니터 데이터는 클라이언트의 relay 선택기, 탐색기 웹사이트, 신뢰 평가 시스템을 지원합니다. Relay 자체 보고와 독립적인 실시간 relay 상태를 제공함으로써, NIP-66은 정보에 기반한 relay 선택을 가능하게 합니다.

[NIP-11](/ko/topics/nip-11/)(자체 보고 기능) 및 Trusted Relay Assertions(신뢰 평가)와 결합하여, 생태계는 하드코딩된 기본값에 의존하지 않고 데이터 기반 relay 선택으로 나아갑니다.

---

**주요 출처:**
- [NIP-66 명세](https://github.com/nostr-protocol/nips/blob/master/66.md) - Relay 발견 및 활성 모니터링 표준

**언급된 곳:**
- [뉴스레터 #6: NIP 심층 분석](/ko/newsletters/2026-01-21-newsletter/#nip-deep-dive-nip-11-and-nip-66)

**참고:**
- [NIP-11: Relay 정보 문서](/ko/topics/nip-11/)
- [Trusted Relay Assertions](/ko/topics/trusted-relay-assertions/)
