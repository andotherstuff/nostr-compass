---
title: "NIP-101e: 피트니스 운동"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-101e.md
translationDate: 2026-07-01
categories:
  - Fitness
  - Discovery
---

NIP-101e는 피트니스 추적 애플리케이션이 Nostr에서 훈련 세션을 게시하고, 공유하고, 발견할 수 있도록 운동 이벤트 형식을 정의한다. 이 spec은 세션 지표(거리, 시간, 고도, 심박수, 칼로리, 사이클링 케이던스, 소스 앱)를 구조화된 tag에 담는 kind 1301 이벤트를 사용하며, 클라이언트는 운동을 지표가 적절한 단위로 표시된 구조화된 카드로 렌더링할 수 있다.

## 작동 방식

NIP-101e 운동은 소스 애플리케이션이 캡처한 모든 지표에 대한 구조화된 tag를 가진 kind 1301 이벤트이다. 일반적인 tag에는 다음이 포함된다:

- 운동 종목에 대한 `type` (달리기, 자전거, 수영, 웨이트 등)
- 값과 단위가 있는 `distance`
- 초 단위의 `duration`
- 값과 단위가 있는 `elevation_gain`
- `start` 및 `end` 타임스탬프
- `heart_rate` (평균 및 최대)
- 에너지 소비에 대한 `calories`
- 게시 애플리케이션을 나타내는 `source`
- 해시태그 발견을 위한 `t` 토픽 tag

`content` 필드는 선택적인 사용자 작성 노트를 담는다 (사용자가 Strava 업로드에 첨부할 캡션에 해당). kind 1301을 인식하는 클라이언트는 구조화된 지표를 운동 카드로 렌더링하며, 그렇지 않은 클라이언트는 `content` 필드를 일반 노트로 표시하는 것으로 대체한다.

## 발견 및 피드 시맨틱

NIP-101e 이벤트는 일반적인 피드 이벤트이므로, 사용자가 게시한 운동은 다른 게시물과 마찬가지로 팔로워의 타임라인에 표시된다. 전용 운동 뷰가 있는 클라이언트는 저자 또는 해시태그 필터로 kind 1301을 구독하여 훈련 로그 표면, 리더보드 또는 커뮤니티 챌린지 피드를 구축할 수 있다. 저자 pubkey는 운동에 대한 정규 신원이므로, 다른 사용자의 운동을 읽는 타사 애플리케이션은 다른 Nostr 피드와 동일한 신뢰 가정을 상속받는다.

## 구현

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0)은 히어로 지표, 통계 그리드, 사이클링 전용 속도 표시 및 소스 배지를 갖춘 kind 1301 운동 렌더링을 출시했다 ([PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184), [PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226)에서 리팩터링됨)

---

**주요 출처:**
- [NIP-101e 명세](https://github.com/nostr-protocol/nips/blob/master/101e.md)
- [Amethyst PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184) - NIP-101e 피트니스 운동 지원 추가 (Kind 1301)
- [Amethyst PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226) - 히어로 지표와 통계 그리드로 운동 표시 재설계

**언급된 곳:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/ko/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
