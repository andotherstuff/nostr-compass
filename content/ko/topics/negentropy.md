---
title: "Negentropy: 집합 조정 프로토콜"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Sync
---
Negentropy는 전체 데이터셋을 재전송하지 않고 한쪽에는 있지만 다른 쪽에는 없는 이벤트를 찾기 위한 집합 조정(set-reconciliation) 프로토콜이다.

## 작동 방식

모든 이벤트를 필터로 요청하는 대신, negentropy는 두 정렬된 집합을 비교하여 차이가 있는 범위만 좁혀 나간다. 프로토콜은 간결한 범위 요약을 교환하고, 필요한 곳에서만 명시적 ID 목록으로 전환한다.

1. **정렬**: 양쪽 모두 레코드를 타임스탬프 순으로 정렬하고, 같은 타임스탬프에서는 ID 순으로 정렬한다
2. **범위 비교**: 레코드 범위에 대한 fingerprint를 교환한다
3. **세분화**: 불일치하는 범위를 실제 누락된 ID가 명확해질 때까지 분할한다

## 왜 중요한가

전통적인 Nostr 동기화는 타임스탬프 기반 `since` 필터를 사용하는데, 다음과 같은 이유로 이벤트를 놓칠 수 있다:
- 클라이언트와 릴레이 간 시계 오차
- 동일한 타임스탬프를 가진 여러 이벤트
- 순서가 뒤바뀌어 도착하는 이벤트

Negentropy는 타임스탬프에 의존하지 않고 실제 이벤트 집합을 비교함으로써 이런 문제를 해결한다.

## 실제 활용

- **DM 복구**: 클라이언트가 오래된 타임스탬프의 누락된 다이렉트 메시지를 감지하고 가져올 수 있다
- **피드 동기화**: 릴레이 간 완전한 타임라인 동기화를 보장한다
- **오프라인 동기화**: 연결이 끊겼던 기간 이후 효율적으로 따라잡는다

실제 구현에서 주목할 점은, 많은 클라이언트가 일반 구독을 negentropy로 대체하지 않는다는 것이다. 보수 경로로 사용한다. 예를 들어 Damus는 일반적인 DM 로딩을 유지하면서, 수동 새로고침 시 negentropy를 추가하여 일반 흐름에서 놓친 메시지를 복구한다.

## 트레이드오프

Negentropy는 양쪽 모두 지원해야 하며, 표준 `REQ` 사용 이상의 프로토콜 복잡성을 추가한다. 최소한의 구현 노력보다 정확성이 더 중요할 때 가장 유용하다.

혼합 환경에서는 모든 릴레이가 이 프로토콜을 지원하지 않으므로, 클라이언트에 여전히 적절한 폴백 동작이 필요하다.

---

**주요 출처:**
- [Negentropy 프로토콜 저장소](https://github.com/hoytech/negentropy)
- [Damus PR #3536](https://github.com/damus-io/damus/pull/3536)
- [Damus PR #3547](https://github.com/damus-io/damus/pull/3547)

**언급된 뉴스레터:**
- [뉴스레터 #6: Damus, 안정적인 DM 동기화를 위해 negentropy 출시](/en/newsletters/2026-01-28-newsletter/#damus-ships-negentropy-for-reliable-dm-syncing)
- [뉴스레터 #12](/en/newsletters/2026-03-04-newsletter/)

**같이 보기:**
- [NIP-01: 기본 프로토콜](/ko/topics/nip-01/)
