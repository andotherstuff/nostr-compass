---
title: "Trusted Relay Assertions"
date: 2026-01-21
draft: false
categories:
  - Protocol
  - Relays
---

Trusted Relay Assertions는 리레이 신뢰도 점수 매기기 및 평판 관리를 표준화하기 위한 드래프트 NIP 제안입니다. 명세서는 주장 제공자가 관찰된 메트릭, 운영자 평판 및 사용자 보고서에서 계산된 신뢰 점수를 게시하는 kind 30385 이벤트를 도입합니다.

## 작동 방식

제안은 리레이 생태계의 격차를 채웁니다. [NIP-11](/ko/topics/nip-11/)이 리레이가 자신에 대해 주장하는 것을 정의하고 [NIP-66](/ko/topics/nip-66/)이 우리가 관찰하는 것을 측정하는 반면, Trusted Relay Assertions는 리레이 신뢰성에 대해 우리가 내리는 결론을 표준화합니다.

주장 제공자는 세 가지 차원에서 점수를 계산합니다. 신뢰도는 가용성, 복구 속도, 일관성 및 대기 시간을 측정합니다. 품질은 정책 문서, TLS 보안 및 운영자 책임성을 평가합니다. 접근성은 액세스 장벽, 관할권 자유도 및 감시 위험을 평가합니다. 전체 신뢰 점수 (0-100)는 가중치를 포함한 이러한 구성 요소를 결합합니다: 신뢰도 40%, 품질 35%, 접근성 25%.

각 주장은 관찰 개수를 기반으로 신뢰도 수준 (낮음, 중간, 높음)을 포함합니다. 운영자 검증은 여러 방법을 사용합니다: 서명된 NIP-11 문서를 통한 암호화 증명, DNS TXT 레코드 또는 .well-known 파일. 명세서는 운영자 신뢰 점수를 통한 Web of Trust를 통합합니다. 정책 분류는 사용자가 적절한 리레이를 찾을 수 있게 합니다: 공개, 중재, 큐레이션 또는 특화.

사용자는 kind 10385 이벤트를 통해 신뢰할 수 있는 주장 제공자를 선언합니다. 클라이언트는 여러 제공자를 쿼리하고 점수를 비교합니다. 제안은 리레이 운영자가 [NIP-32](/ko/topics/nip-32/) 라벨 이벤트를 사용하여 점수에 이의를 제기할 수 있는 항소 절차를 포함합니다.

## 사용 사례

[NIP-46](/ko/topics/nip-46/) 원격 서명자의 경우, 신뢰 주장은 사용자가 연결 URI에 내장된 낯선 리레이를 수락하기 전에 평가할 수 있게 합니다. [NIP-65](/ko/topics/nip-65/) 리레이 목록과 결합하여, 클라이언트는 사용자 선호도와 제3자 신뢰 평가에 기반한 정보 있는 리레이 선택 결정을 내릴 수 있습니다.

명세서는 기존 리레이 발견 메커니즘을 보완합니다. [NIP-66](/ko/topics/nip-66/)은 발견을 제공하고 (무엇이 존재하는가), 이 제안은 평가를 추가합니다 (무엇이 좋은가). 함께 하드코딩된 기본값이나 입소문 권장사항에 의존하지 않고 정보 있는 리레이 선택을 활성화합니다.

---

**주요 출처:**
- [Draft NIP Document](https://nostr.com/nevent1qqsqjymvcp6ch3ps3fqsxljf6j8u3adz64ucw8npnzuj3cn6dekn0gspz9mhxue69uhkummnw3ezumrpdejz7qg3waehxw309ahx7um5wgh8w6twv5hsyga3qg) - Kind 30817 이벤트가 명세서를 제안합니다.

**언급된 곳:**
- [Newsletter #6: News](/ko/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6: NIP Updates](/ko/newsletters/2026-01-21-newsletter/#nip-updates)

**참고 항목:**
- [NIP-11: Relay Information Document](/ko/topics/nip-11/)
- [NIP-66: Relay Discovery and Liveness Monitoring](/ko/topics/nip-66/)
- [NIP-32: Labeling](/ko/topics/nip-32/)
