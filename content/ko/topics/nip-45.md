---
title: "NIP-45: 이벤트 카운팅"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45는 클라이언트가 릴레이에 필터와 일치하는 이벤트 개수를 묻되, 일치한 이벤트 자체는 전송받지 않는 방법을 정의합니다. NIP-01 필터 구문을 재사용하므로, 클라이언트는 기존 `REQ`를 같은 필터를 가진 `COUNT` 요청으로 바꾸는 경우가 많습니다.

## 작동 방식

클라이언트는 구독 ID와 필터를 담은 `COUNT` 요청을 보냅니다:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

릴레이는 개수로 응답합니다:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

이 방식은 단지 숫자를 보여 주기 위해 수백, 수천 개의 이벤트를 내려받는 일을 피하게 해 줍니다. 클라이언트가 하나의 `COUNT` 요청에 여러 필터를 보내면, 릴레이는 여러 `REQ` 필터가 OR로 결합되는 것처럼 이를 하나의 결과로 집계합니다.

## HyperLogLog 근사 카운팅

2026년 2월 기준으로 NIP-45는 HyperLogLog(HLL) 근사 카운팅을 지원합니다([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). 릴레이는 결과를 근사값으로 표시할 수 있고, 여러 릴레이 사이 중복 제거를 위해 count와 함께 256개의 HLL 레지스터를 반환할 수 있습니다:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<512-char hex string>"}]
```

HLL은 근본 문제를 해결합니다. 여러 릴레이에 퍼진 고유 이벤트를 어떻게 셀 것인가입니다. 릴레이 A가 리액션 50개를, 릴레이 B가 40개를 보고해도 총합은 90이 아닙니다. 많은 이벤트가 양쪽에 모두 존재하기 때문입니다. 클라이언트는 각 레지스터 위치에서 최댓값을 취해 HLL 값을 병합하고, raw event를 내려받지 않고도 네트워크 전체 추정치를 얻습니다.

명세는 상호운용성을 위해 레지스터 개수를 256으로 고정합니다. 이 덕분에 payload가 작게 유지되고, 같은 적격 필터에 대해 모든 릴레이가 같은 레지스터 레이아웃을 계산하므로 릴레이 측 캐싱도 실용적입니다.

## 상호운용성 참고사항

HLL은 태그 속성이 있는 필터에서만 정의됩니다. 레지스터를 구성하는 offset이 필터 안 첫 태그 값에서 유도되기 때문입니다. 명세는 reaction, repost, quote, reply, comment, follower count 같은 소수의 canonical query도 따로 언급합니다. 이런 카운트가 릴레이가 사전 계산하거나 캐시하기 가장 쉽기 때문입니다.

## 왜 중요한가

follower count, reaction count, reply count가 주된 사용 사례입니다. NIP-45가 없으면 클라이언트는 단일 릴레이의 로컬 뷰를 신뢰하거나, 일치하는 이벤트를 전부 내려받아 로컬에서 중복 제거해야 합니다. NIP-45는 카운팅을 릴레이 안에서 처리하고, HLL은 한 릴레이를 권위자로 만들지 않고도 다중 릴레이 카운트를 실용화합니다.

---

## 구현체

- [nostream](https://github.com/Cameri/nostream)는 [PR #522](https://github.com/Cameri/nostream/pull/522)에서 `COUNT` 지원을 추가해, 클라이언트가 이벤트를 가져오지 않고도 필터 일치 개수를 물을 수 있게 했습니다.

---

**주요 출처:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)
- [nostream PR #522](https://github.com/Cameri/nostream/pull/522) - NIP-45 COUNT 지원

**언급된 뉴스레터:**
- [Newsletter #9: NIP Deep Dive](/ko/newsletters/2026-02-11-newsletter/)
- [Newsletter #9: NIP Updates](/ko/newsletters/2026-02-11-newsletter/)
- [Newsletter #12: Five Years of Nostr Februaries](/ko/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: nostream NIP-45 support](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-11: 릴레이 정보 문서](/ko/topics/nip-11/)
