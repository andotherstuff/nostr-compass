---
title: "Negentropy: 집합 조정 프로토콜"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-01-28
draft: false
categories:
  - Protocol
  - Sync
---

Negentropy는 전체 데이터셋을 전송하지 않고 누락된 event를 식별하여 Nostr 클라이언트와 relay 간의 효율적인 동기화를 가능하게 하는 집합 조정 프로토콜입니다.

## 작동 방식

필터와 일치하는 모든 event를 요청하는 대신, negentropy는 클라이언트가 자신의 로컬 event 집합을 relay의 집합과 비교하고 차이점만 식별할 수 있게 합니다. 이는 다중 라운드 프로토콜을 통해 수행됩니다:

1. **지문 생성**: 클라이언트와 relay가 각각 자신의 event 집합의 지문을 계산
2. **비교**: 지문이 교환되고 비교됨
3. **조정**: 누락된 event ID만 식별되어 전송됨

## 중요한 이유

전통적인 Nostr 동기화는 타임스탬프 기반 `since` 필터를 사용하는데, 다음과 같은 이유로 event를 놓칠 수 있습니다:
- 클라이언트와 relay 간의 시계 드리프트
- 동일한 타임스탬프를 가진 여러 event
- 순서가 맞지 않게 도착하는 event

Negentropy는 타임스탬프에 의존하지 않고 실제 event 집합을 비교하여 이러한 문제를 해결합니다.

## 사용 사례

- **DM 복구**: 클라이언트가 오래된 타임스탬프의 다이렉트 메시지도 감지하고 가져올 수 있음
- **피드 동기화**: relay 간 완전한 타임라인 동기화 보장
- **오프라인 동기화**: 연결 끊김 기간 후 효율적으로 따라잡기

## 구현

Negentropy는 relay 지원이 필요합니다. 클라이언트는 일반적으로 표준 REQ 구독을 대체하기보다 대체 복구 메커니즘으로 구현하며, relay가 프로토콜을 지원하지 않을 때 우아하게 대체합니다.

## 관련 항목

- [NIP-01](/ko/topics/nip-01/) - 기본 프로토콜
