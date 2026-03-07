---
title: "NIP-45: 이벤트 카운팅"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Protocol
---
NIP-45는 클라이언트가 릴레이에 필터와 일치하는 이벤트의 수를 요청하되, 일치하는 이벤트 자체는 전송하지 않는 방법을 정의한다. NIP-01 필터 구문을 재사용하므로, 클라이언트는 기존 `REQ`를 동일한 필터로 `COUNT` 요청으로 변환할 수 있다.

## 작동 방식

클라이언트가 구독 ID와 필터를 포함한 `COUNT` 요청을 전송한다:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

릴레이가 카운트로 응답한다:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

이로써 단순히 숫자를 표시하기 위해 수백 또는 수천 개의 이벤트를 다운로드하는 것을 피할 수 있다. 클라이언트가 하나의 `COUNT` 요청에 여러 필터를 전송하면, 릴레이는 여러 `REQ` 필터가 OR로 결합되는 것과 마찬가지로 하나의 결과로 집계한다.

## HyperLogLog 근사 카운팅

2026년 2월 기준, NIP-45는 HyperLogLog(HLL) 근사 카운팅을 지원한다([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). 릴레이는 결과를 근사값으로 표시할 수 있으며, 릴레이 간 중복 제거를 위해 카운트와 함께 256개의 HLL 레지스터를 반환할 수 있다:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<512자 hex 문자열>"}]
```

HLL은 근본적인 문제를 해결한다: 여러 릴레이에 걸친 고유 이벤트 카운팅이다. 릴레이 A가 50개의 리액션을, 릴레이 B가 40개를 보고하면, 많은 이벤트가 양쪽 릴레이에 모두 존재하므로 합계는 90이 아니다. 클라이언트는 각 레지스터 위치에서 최댓값을 취하여 HLL 값을 병합하며, 원시 이벤트를 다운로드하지 않고도 네트워크 전체 추정치를 얻을 수 있다.

사양은 상호운용성을 위해 레지스터 수를 256으로 고정한다. 이를 통해 페이로드를 작게 유지하고, 모든 릴레이가 동일한 적격 필터에 대해 동일한 레지스터 레이아웃을 계산하므로 릴레이 측 캐싱이 실용적이 된다.

## 상호운용성 참고사항

HLL은 태그 속성이 있는 필터에 대해서만 정의되는데, 레지스터를 구성하는 데 사용되는 오프셋이 필터의 첫 번째 태그 값에서 파생되기 때문이다. 사양은 리액션, 리포스트, 인용, 답글, 댓글, 팔로워 수를 포함한 소수의 표준 쿼리도 명시한다. 이들은 릴레이가 사전 계산하거나 캐싱하기 가장 쉬운 카운트이다.

## 왜 중요한가

팔로워 수, 리액션 수, 답글 수가 주요 사용 사례이다. NIP-45 없이는 클라이언트가 단일 릴레이의 로컬 뷰를 신뢰하거나, 모든 일치하는 이벤트를 다운로드하여 로컬에서 중복을 제거해야 한다. NIP-45는 카운팅을 릴레이 내부에서 처리하며, HLL은 하나의 릴레이를 권위자로 만들지 않고도 다중 릴레이 카운트를 실용적으로 만든다.

---

**주요 출처:**
- [NIP-45: 이벤트 카운팅](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog 릴레이 응답](https://github.com/nostr-protocol/nips/pull/1561)

**언급된 뉴스레터:**
- [Newsletter #9: NIP 심층 분석](/en/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-45-event-counting-and-hyperloglog)
- [Newsletter #9: NIP 업데이트](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12: Nostr 2월의 5년](/en/newsletters/2026-03-04-newsletter/)

**같이 보기:**
- [NIP-11: 릴레이 정보 문서](/ko/topics/nip-11/)
