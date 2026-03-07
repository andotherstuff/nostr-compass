---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2026-03-07
draft: false
categories:
  - Trust
  - Social Graph
---
Web of Trust(WoT)는 중앙 기관이 아닌 소셜 그래프 관계에서 평판과 신뢰성을 도출하는 탈중앙화 신뢰 모델이다.

## 작동 방식

Nostr에서 Web of Trust는 보통 [NIP-02: 팔로우 목록](/ko/topics/nip-02/)의 팔로우 그래프에서 시작하고, 때로는 뮤트, 신고, 검증된 신원 신호를 추가한다. 클라이언트나 서비스는 이미 신뢰하는 하나 이상의 시드 공개키를 선택한 다음, 그래프를 통해 신뢰를 외부로 전파한다.

1. **그래프 구축**: 팔로우와 선택적 부정 신호로 방향 그래프 생성
2. **시드 선택**: 관찰자가 이미 신뢰하는 공개키에서 시작
3. **점수 전파**: PageRank 또는 변형 알고리즘으로 그래프를 통해 순위 전파
4. **컷오프 및 정규화**: 그래프 깊이 제한, 저신호 계정 감쇠, 표시 또는 필터링용 최종 점수 정규화

정확한 알고리즘은 표준화되어 있지 않다. 두 WoT 시스템이 서로 다른 시드, 그래프 깊이, 감쇠 규칙, 뮤트 및 신고 처리 방식을 사용하기 때문에 다른 랭킹을 산출하면서도 둘 다 유효할 수 있다.

## 왜 중요한가

WoT는 Nostr에 중앙 중재 서비스 없이 랭킹과 필터링을 수행하는 방법을 제공한다. 개인화된 신뢰 그래프는 단순 팔로워 수보다 조작하기 어렵다. 가짜 계정이 효과를 내려면 관찰자의 기존 네트워크에서 신뢰가 흘러들어와야 하기 때문이다.

반대로 콜드 스타트 문제가 있다. 아무도 팔로우하지 않으면, 개인화된 WoT는 랭킹의 근거가 거의 없다. 많은 제품이 초기 팔로우 추천, 신뢰 제공자 기본값, 외부 서비스의 사전 계산된 점수로 이 문제를 해결한다.

## Nostr에서의 활용

- **스팸 필터링**: 릴레이가 WoT를 사용하여 저신뢰 콘텐츠 필터링
- **콘텐츠 발견**: 네트워크가 신뢰하는 계정의 콘텐츠 노출
- **결제 디렉토리**: 사칭 방지를 포함한 Lightning 주소 조회
- **릴레이 정책**: WoT 릴레이가 신뢰받는 공개키의 노트만 수락
- **탈중앙화 중재**: 커뮤니티가 신뢰 점수를 기반으로 큐레이션

## 구현 참고사항

WoT 계산은 네트워크의 큰 부분을 크롤링해야 하므로, 많은 클라이언트가 로컬에서 직접 계산하지 않는다. [NIP-85: Trusted Assertions](/ko/topics/nip-85/)가 존재하는 이유 중 하나가 바로 이것이다: 로컬 계산이 너무 비쌀 때 서명된 제3자 WoT 계산 결과를 소비하는 방법을 클라이언트에 제공한다.

기존 구현들은 서로 다른 질문에 답한다. 글로벌 신뢰 순위는 전체 네트워크에서의 발견과 스팸 저항에 유용하다. 개인화된 로컬 점수는 "내 그래프가 신뢰할 계정을 보여줘"에 더 적합하다. 어떤 모델이 산출한 것인지 모르고 WoT 숫자를 읽는 것은 흔한 혼란의 원인이다.

---

**주요 출처:**
- [NIP-02: Follow List](https://github.com/nostr-protocol/nips/blob/master/02.md)
- [NIP-85: Trusted Assertions](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [DCoSL Protocol](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**언급된 뉴스레터:**
- [Newsletter #3: 12월 회고](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**같이 보기:**
- [NIP-02: 팔로우 목록](/ko/topics/nip-02/)
