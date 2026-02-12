---
title: "NIP-45: Event 카운팅"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45는 클라이언트가 event 자체를 전송하지 않고 필터와 일치하는 event의 수를 relay에 요청하는 방법을 정의합니다. 클라이언트는 REQ와 동일한 필터 구문으로 COUNT 메시지를 보내고, relay는 카운트로 응답합니다.

## 작동 방식

클라이언트는 구독 ID와 필터가 포함된 COUNT 요청을 보냅니다:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

relay는 카운트로 응답합니다:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

이를 통해 숫자를 표시하기 위해 수백, 수천 개의 event를 다운로드하는 것을 피할 수 있습니다.

## HyperLogLog 근사 카운팅

2026년 2월 기준, NIP-45는 HyperLogLog (HLL) 근사 카운팅을 지원합니다([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). relay는 COUNT 응답과 함께 256바이트 HLL 레지스터 값을 반환할 수 있습니다:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

HLL은 근본적인 문제를 해결합니다: 여러 relay에 걸쳐 고유한 event를 카운팅하는 것입니다. relay A가 50개의 리액션을 보고하고 relay B가 40개를 보고하면, 많은 event가 양쪽 relay에 존재하기 때문에 합계는 90이 아닙니다. 여러 relay의 HLL 레지스터는 각 레지스터 위치에서 최대값을 취하여 병합할 수 있으며, 네트워크 전체에서 자동으로 중복을 제거합니다.

256개의 레지스터로 표준 오차는 약 5.2%입니다. HyperLogLog++ 보정은 200개 미만의 작은 카디널리티에서 정확도를 향상시킵니다. 리액션 event 두 개만으로도 256바이트 HLL 페이로드보다 더 많은 대역폭을 소비하므로, 사소한 숫자 이상의 모든 카운트에 효율적입니다.

명세는 모든 relay 구현 간의 상호 운용성을 위해 레지스터 수를 256으로 고정합니다.

## 사용 사례

소셜 메트릭(팔로워 수, 리액션 수, 리포스트 수)이 주요 활용 분야입니다. HLL 없이 클라이언트는 카운트를 위해 단일 "신뢰할 수 있는" relay에 쿼리하거나(데이터를 중앙화), 로컬에서 중복 제거를 위해 모든 relay에서 전체 event를 다운로드해야 합니다(대역폭 낭비). HLL은 relay당 256바이트의 오버헤드로 근사적인 크로스 relay 카운트를 제공합니다.

---

**주요 출처:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**언급된 곳:**
- [뉴스레터 #9: NIP 심층 분석](/ko/newsletters/2026-02-11-newsletter/#nip-심층-분석-nip-45-event-카운팅과-hyperloglog)
- [뉴스레터 #9: NIP 업데이트](/ko/newsletters/2026-02-11-newsletter/#nip-업데이트)

**참고:**
- [NIP-11: Relay 정보 문서](/ko/topics/nip-11/)
