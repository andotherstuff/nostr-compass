---
title: "NIP-77: Negentropy 집합 조정"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-77.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Sync
---

NIP-77은 Nostr 릴레이와 클라이언트가 [Negentropy](/ko/topics/negentropy/) 집합 조정 프로토콜을 사용하여 전체 데이터셋을 재전송하지 않고도 각 측에서 누락된 이벤트를 찾아 이벤트 집합을 효율적으로 동기화하는 방법을 정의합니다.

## 작동 방식

Negentropy 조정은 전용 메시지 타입을 사용하여 WebSocket 연결을 통해 실행됩니다. 클라이언트와 릴레이는 정렬된 이벤트 집합에 대한 컴팩트한 범위 지문을 교환하여 차이가 있는 범위만 좁혀 나갑니다. 차이가 식별되면 누락된 이벤트 ID(그런 다음 누락된 이벤트 자체)만 전송됩니다.

NIP-77은 사양을 구현하는 모든 클라이언트와 릴레이가 효율적인 동기화 세션을 협상할 수 있도록 메시지 프레이밍을 표준화합니다. 프로토콜은 기존 Nostr WebSocket 연결을 통해 `NEG-OPEN`, `NEG-MSG`, `NEG-CLOSE` 메시지 타입을 사용합니다.

## 중요한 이유

기존 Nostr 동기화는 타임스탬프 기반 `since` 필터를 사용하는데, 클록 드리프트, 동일한 타임스탬프를 가진 이벤트, 순서에 맞지 않게 도착하는 이벤트로 인해 이벤트를 놓칠 수 있습니다. Negentropy는 타임스탬프에 의존하는 대신 실제 이벤트 집합을 비교하여 단순 폴링보다 훨씬 적은 왕복으로 증명 가능한 완전한 동기화를 제공합니다.

이는 특히 다음에 유용합니다:
- 오프라인 이후 따라잡는 모바일 클라이언트
- 릴레이 간 복제
- 로컬 릴레이 동기화 (Citrine의 릴레이 집계기처럼)

## 구현

- [Citrine](https://github.com/greenart7c3/Citrine) — [PR #139](https://github.com/greenart7c3/Citrine/pull/139)에서 Android 릴레이 노드에 효율적인 집합 조정 동기화를 위한 NIP-77 지원 추가
- [strfry](https://github.com/hoytech/strfry) — 릴레이 측 Negentropy 지원
- [nostr-tools](https://github.com/nbd-wtf/nostr-tools) — 클라이언트 측 Negentropy 구현

---

**주요 출처:**
- [NIP-77 사양](https://github.com/nostr-protocol/nips/blob/master/77.md)
- [Negentropy 프로토콜](https://github.com/hoytech/negentropy)

**언급된 곳:**
- [뉴스레터 #22: Citrine v3.0.0-pre1](/ko/newsletters/2026-05-14-newsletter/#citrine-v300-pre1-lands-built-in-tor-and-relay-aggregation)

**참고:**
- [Negentropy](/ko/topics/negentropy/)
