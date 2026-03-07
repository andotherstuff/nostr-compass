---
title: "NIP-85: Trusted Assertions"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---
NIP-85는 Trusted Assertions를 정의한다. 비용이 많이 드는 계산을 신뢰할 수 있는 서비스 제공자에게 위임하고, 그 결과를 서명된 Nostr 이벤트로 게시하는 시스템이다.

## 작동 방식

Web of Trust 점수, 참여 지표 및 기타 계산 값은 많은 릴레이를 크롤링하고 대량의 이벤트를 처리해야 한다. 이 작업은 모바일 기기에서 비현실적이다. NIP-85는 전문 제공자가 이런 계산을 수행하고 클라이언트가 조회할 수 있는 결과를 게시할 수 있게 한다.

Trusted Assertions는 주소 지정 가능한 이벤트다. `d` 태그는 평가 대상 주체를 식별하고, 이벤트 kind는 주체의 종류를 식별한다: pubkey(30382), 일반 이벤트(30383), 주소 지정 가능한 이벤트(30384), NIP-73 식별자(30385).

사용자는 kind 10040을 통해 신뢰하는 제공자를 선언한다. 이 제공자 목록은 태그에 공개하거나 [NIP-44](/ko/topics/nip-44/)로 이벤트 콘텐츠에 암호화할 수 있으며, 이는 사용자가 자신의 신뢰 입력을 공개적으로 게시하고 싶지 않을 때 중요하다.

## 왜 중요한가

NIP-85의 핵심 통찰은 알고리즘이 아닌 출력을 표준화한다는 것이다. 두 제공자가 같은 pubkey에 대해 `rank` 태그를 게시하면서 서로 다른 Web of Trust 공식, 뮤트 처리, 릴레이 커버리지 또는 스팸 방지 휴리스틱을 사용할 수 있다. 계산이 다르더라도 결과 형식이 일치하므로 클라이언트 간 상호운용성이 유지된다.

이는 하나의 정식 랭킹 서비스가 있을 것이라고 가정하는 것보다 Nostr에 더 적합하다. 사용자가 누구의 어설션을 신뢰할지 선택한다.

## 신뢰 모델

서비스 제공자는 자체 어설션 이벤트에 서명해야 하며, 명세는 서로 다른 알고리즘이나 사용자별 관점에 대해 다른 서비스 키를 사용하도록 권장한다. 이를 통해 제공자가 관련 없는 랭킹 시스템을 하나의 불투명한 신원으로 합치는 것을 방지한다.

신뢰는 로컬에 유지된다. 서명된 출력은 어떤 제공자가 점수를 게시했는지 증명하지만, 점수가 정확한지는 증명하지 않는다. 클라이언트는 어떤 제공자 키를 사용할지, 어떤 릴레이에서 가져올지, 상충하는 어설션을 어떻게 처리할지에 대한 정책이 필요하다.

## 상호운용성 참고사항

NIP-85는 사람과 게시물을 넘어 확장된다. Kind 30385는 제공자가 책, 웹사이트, 해시태그, 위치 같은 NIP-73 외부 식별자를 평가할 수 있게 한다. 이를 통해 Nostr 자체 외부의 주제에 대한 상호운용 가능한 평판 및 참여 데이터의 경로가 생긴다.

---

**주요 출처:**
- [NIP-85 명세](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #2223](https://github.com/nostr-protocol/nips/pull/2223) - 서비스 제공자 발견 가능성 지침

**언급된 뉴스레터:**
- [Newsletter #10: NIP-85 심층 분석](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #11: NIP-85 서비스 제공자 발견 가능성](/en/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12: 프로토콜 요약](/en/newsletters/2026-03-04-newsletter/)

**같이 보기:**
- [NIP-44: 암호화된 페이로드](/ko/topics/nip-44/)
- [NIP-73: 외부 콘텐츠 ID](/ko/topics/nip-73/)
- [Web of Trust](/ko/topics/web-of-trust/)
