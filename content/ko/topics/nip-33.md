---
title: "NIP-33: 매개변수화된 대체 가능 이벤트 (주소 지정 가능 이벤트)"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - 프로토콜
---

NIP-33은 원래 매개변수화된 대체 가능 이벤트를 정의했습니다. 이는 relay가 `(pubkey, kind, d-tag)` 튜플당 하나의 이벤트만 보유하는 이벤트 클래스입니다. 이 개념은 이후 "주소 지정 가능 이벤트"로 이름이 변경되었으며 [NIP-01](/ko/topics/nip-01/)에 통합되었습니다. NIP-33 문서는 현재 NIP-01로 리디렉션되지만, 코드베이스와 문서에서 흔한 참조로 남아 있습니다.

## 작동 방식

주소 지정 가능 이벤트는 `30000-39999` 범위의 kind를 사용합니다. 각 이벤트는 `d` 태그를 포함하며, 이 값은 저자의 pubkey 및 kind 번호와 함께 고유한 주소를 형성합니다. relay가 기존 `(pubkey, kind, d-tag)` 튜플과 일치하는 새 이벤트를 수신하면, 이전 이벤트를 새 이벤트(`created_at` 기준)로 대체합니다. 이로 인해 주소 지정 가능 이벤트는 프로필, 설정, 앱 구성, 분류 광고 목록 등 최신 버전만 중요한 변경 가능 상태에 유용합니다.

클라이언트는 `<kind>:<pubkey>:<d-tag>` 형식의 `a` 태그로 주소 지정 가능 이벤트를 참조하며, 선택적으로 relay 힌트가 뒤따릅니다.

## 일반적인 용도

- Kind `30023` 장문 기사
- Kind `30078` 앱별 데이터 (NIP-78에서 사용)
- Kind `31923` 캘린더 이벤트 (NIP-52)
- Kind `31990` 핸들러 추천 (NIP-89)
- Kind `30009` 배지 정의 (NIP-58)
- Kind `31991` 에이전트 실행 구성 (Notedeck Agentium)

## NIP-01과의 관계

NIP-33은 통합 작업의 일환으로 NIP-01에 병합되었습니다. NIP-01 사양은 현재 세 가지 이벤트 보존 범주를 정의합니다: 일반 이벤트(그대로 보관), 대체 가능 이벤트(`(pubkey, kind)`당 하나), 주소 지정 가능 이벤트(`(pubkey, kind, d-tag)`당 하나). NIP-33은 주소 지정 가능 이벤트 개념의 유효한 약칭으로 남아 있습니다.

---

**주요 출처:**
- [NIP-33 (리디렉트)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [NIP-01 사양](https://github.com/nostr-protocol/nips/blob/master/01.md) - 주소 지정 가능 이벤트 섹션

**언급된 곳:**
- [뉴스레터 #13: Notedeck](/en/newsletters/2026-03-11-newsletter/#notedeck-adds-nip-11-relay-limits-and-agentium-features)

**같이 보기:**
- [NIP-01: 기본 프로토콜](/ko/topics/nip-01/)
