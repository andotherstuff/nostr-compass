---
title: "NIP-32: 라벨링"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Protocol
---
NIP-32는 Nostr 이벤트, 사용자, 기타 엔티티에 라벨을 부착하는 표준을 정의한다. 라벨은 클라이언트가 분류, 콘텐츠 경고, 평판 시스템, 모더레이션에 활용할 수 있는 구조화된 메타데이터를 제공한다.

## 작동 방식

라벨은 kind 1985 이벤트를 사용하며, `L` 태그로 라벨 네임스페이스를 정의하고 `l` 태그로 해당 네임스페이스 내 특정 라벨을 적용한다. 라벨 대상 엔티티는 `e`(이벤트), `p`(공개키), `r`(릴레이 URL) 등 표준 태그로 참조한다.

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Contains explicit imagery"
}
```

네임스페이스 시스템은 라벨 충돌을 방지한다. "ugc-moderation" 네임스페이스의 "spam" 라벨은 "relay-report" 네임스페이스의 "spam"과 다른 의미를 가진다. 덕분에 여러 라벨 시스템이 서로 간섭 없이 공존할 수 있다.

## 왜 중요한가

핵심 설계 결정은 라벨이 프로토콜에 내장된 사실이 아니라 주장(assertion)이라는 점이다. kind 1985 이벤트는 어떤 행위자가 특정 네임스페이스에서 무언가에 라벨을 붙였다는 것을 나타낸다. 클라이언트는 누구의 라벨을 표시하고, 숨기고, 무시할지 결정하는 신뢰 정책이 여전히 필요하다.

이 특성 덕분에 NIP-32는 모더레이션을 넘어 폭넓게 활용된다. 동일한 구조로 콘텐츠 경고, 인증 마커, 분류 체계, 릴레이 평판 데이터를 전달할 수 있으며, 모든 클라이언트를 하나의 전역 용어 체계에 강제하지 않는다.

## 활용 사례

콘텐츠 모더레이션 시스템은 라벨을 사용해 스팸, 불법 콘텐츠, 정책 위반을 표시한다. 평판 시스템은 공개키에 신뢰 점수나 인증 상태를 부여한다. 미디어 플랫폼은 NSFW, 폭력, 스포일러 등의 콘텐츠 경고를 적용한다. 릴레이 운영자는 이의 제기 및 분쟁 해결에 라벨을 활용한다.

Trusted Relay Assertions 제안은 릴레이 이의 제기에 NIP-32 라벨을 사용한다. 운영자가 신뢰 점수에 이의를 제기할 때 `L = relay-appeal`과 `spam`, `censorship`, `score` 같은 라벨이 포함된 kind 1985 이벤트를 게시한다.

## 상호운용성 참고사항

클라이언트마다 라벨 소비 방식이 다르다. 일부는 팔로우한 사용자의 라벨을 추천으로 취급하고, 다른 일부는 전문 라벨링 서비스에 질의한다. 탈중앙화 설계 덕분에 사용자가 어떤 라벨러를 신뢰할지 선택할 수 있지만, 신뢰 맥락이 보이지 않는 라벨은 오해를 유발할 수 있다.

---

**주요 출처:**
- [NIP-32 명세](https://github.com/nostr-protocol/nips/blob/master/32.md) - 라벨링 표준

**언급된 뉴스레터:**
- [뉴스레터 #6: NIP 업데이트](/en/newsletters/2026-01-21-newsletter/#nip-updates)

**같이 보기:**
- [Trusted Relay Assertions](/ko/topics/trusted-relay-assertions/)
- [NIP-51: 리스트](/ko/topics/nip-51/)
