---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2025-12-31
draft: false
categories:
  - 신뢰
  - 소셜 그래프
---

Web of Trust(WoT)는 평판과 신뢰성이 중앙 기관이 아닌 소셜 그래프 관계에서 파생되는 분산형 신뢰 모델입니다.

## 작동 방식

Nostr에서 Web of Trust는 팔로우 그래프(NIP-02 연락처 목록)와 신고 이벤트를 활용하여 신뢰 점수를 계산합니다:

1. **그래프 구축**: pubkey, 이벤트 및 그 관계(팔로우, 뮤트, 신고)로부터 방향성 그래프가 구축됨
2. **가중치 할당**: 신뢰할 수 있는 것으로 알려진 pubkey(예: 검증된 NIP-05 식별자를 가진 것)에 초기 가중치가 할당됨
3. **반복 전파**: PageRank와 유사한 알고리즘을 사용하여 신뢰 점수가 네트워크를 통해 흐름
4. **Sybil 저항**: 공격자가 많은 가짜 계정을 생성하면, 그들에게 전달되는 신뢰는 가짜 수로 나뉨

## 주요 특성

- **탈중앙화**: 중앙 기관이 평판을 결정하지 않음
- **개인화**: 팔로우하는 사람을 기반으로 각 사용자의 관점에서 신뢰를 계산할 수 있음
- **Sybil 저항**: 신뢰 희석으로 인해 봇 팜이 시스템을 쉽게 조작할 수 없음
- **조합 가능**: 스팸 필터링, 콘텐츠 검열, relay 입장, 결제 디렉토리에 적용 가능

## Nostr에서의 응용

- **스팸 필터링**: relay가 WoT를 사용하여 낮은 신뢰 콘텐츠를 필터링할 수 있음
- **콘텐츠 발견**: 네트워크가 신뢰하는 계정의 콘텐츠 표시
- **결제 디렉토리**: 사칭 방지가 포함된 Lightning 주소 검색
- **Relay 정책**: WoT relay는 신뢰할 수 있는 pubkey의 노트만 수락
- **탈중앙화 검열**: 커뮤니티가 신뢰 점수를 기반으로 큐레이션할 수 있음

## 구현

여러 프로젝트가 Nostr용 Web of Trust를 구현하고 있습니다:
- **Nostr.Band Trust Rank**: 네트워크를 위한 PageRank 스타일 점수
- **WoT Relays**: 소셜 거리로 필터링하는 relay
- **DCoSL**: 탈중앙화 평판 시스템용 프로토콜
- **Noswot**: 팔로우와 신고를 기반으로 한 신뢰 점수

---

**주요 출처:**
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [DCoSL 프로토콜](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**언급된 곳:**
- [Newsletter #3: 12월 요약](/ko/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**함께 보기:**
- [NIP-02: 팔로우 목록](/ko/topics/nip-02/)
