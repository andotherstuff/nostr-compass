---
title: "NIP-33: 매개변수화된 대체 가능 이벤트 (주소 지정 가능 이벤트)"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - 프로토콜
---

NIP-33은 원래 relay가 `(pubkey, kind, d-tag)` 튜플마다 하나의 이벤트만 유지하는 이벤트 클래스인 매개변수화된 대체 가능 이벤트를 정의했다. 이 개념은 이후 "주소 지정 가능 이벤트"로 이름이 바뀌어 [NIP-01](/ko/topics/nip-01/)에 통합되었다. 현재 NIP-33 문서는 NIP-01로 리다이렉트되지만, 코드베이스와 문서에서는 여전히 널리 쓰이는 참조 이름이다.

## 작동 방식

주소 지정 가능 이벤트는 `30000-39999` 범위의 kind를 사용한다. 각 이벤트는 값이 `d` 태그를 가지며, 이 값은 작성자의 pubkey와 kind 번호와 함께 고유 주소를 형성한다. relay가 기존 `(pubkey, kind, d-tag)` 튜플과 일치하는 새 이벤트를 받으면, 이전 이벤트를 더 새로운 이벤트(`created_at` 기준)로 교체한다. 이 때문에 주소 지정 가능 이벤트는 프로필, 설정, 앱 구성, 분류형 목록 등 최신 버전만 중요하고 변경 가능한 상태를 표현하는 데 유용하다.

클라이언트는 `<kind>:<pubkey>:<d-tag>` 형식의 `a` 태그로 주소 지정 가능 이벤트를 참조하며, 선택적으로 relay 힌트를 덧붙일 수 있다.

## 일반적인 용도

- Kind `30023` 장문 아티클
- Kind `30078` 앱 전용 데이터 (NIP-78에서 사용)
- Kind `31923` 캘린더 이벤트 (NIP-52)
- Kind `31990` 핸들러 추천 (NIP-89)
- Kind `30009` 배지 정의 (NIP-58)
- Kind `31991` 에이전트 실행 구성 (Notedeck Agentium)

## NIP-01과의 관계

NIP-33은 통합 작업의 일부로 NIP-01에 병합되었다. 현재 NIP-01 사양은 이벤트 보존을 세 가지 범주로 정의한다. 일반 이벤트는 그대로 유지되고, 대체 가능 이벤트는 `(pubkey, kind)`마다 하나가 유지되며, 주소 지정 가능 이벤트는 `(pubkey, kind, d-tag)`마다 하나가 유지된다. NIP-33은 여전히 주소 지정 가능 이벤트 개념을 가리키는 유효한 약칭이다.

---

**주요 출처:**
- [NIP-33 (redirect)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md) - Addressable events section

**언급된 뉴스레터:**
- [Newsletter #13: Notedeck](/ko/newsletters/2026-03-11-newsletter/#notedeck-adds-nip-11-relay-limits-and-agentium-features)

**같이 보기:**
- [NIP-01: Basic Protocol](/ko/topics/nip-01/)
