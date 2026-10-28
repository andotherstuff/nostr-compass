---
title: "Buzz NIP-AP: 에이전트 페르소나"
date: 2026-10-21
translationOf: /en/topics/nip-ap.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

Buzz NIP-AP는 nostr-protocol/nips에서 승인된 NIP에 속하지 않는 Buzz 프로젝트의 초안 사양입니다.

이 사양은 kind 30175 페르소나 event를 정의합니다. 이는 AI 에이전트를 인스턴스화하기 위한 addressable 정의로, 평문 `d` 슬러그를 키로 사용합니다. Kind 30178에는 팀 카탈로그 프로젝션이 담깁니다. 이를 구현하는 relay는 두 kind 모두에 접근 제한을 적용합니다. 작성자는 자신의 event를 읽을 수 있고, 다른 열람자는 event에 `["shared", "true"]`가 포함된 경우에만 쿼리, 실시간 전달, 검색, 카운트, id 조회에서 해당 event를 볼 수 있습니다. 팀을 공유하면 페르소나가 공유되지 않은 멤버까지 포함해 모든 멤버의 내장 프로젝션과 지침이 노출됩니다. 이 제한은 콘텐츠를 암호화하지 않고 접근만 통제하므로, relay 운영자는 여전히 콘텐츠를 읽을 수 있습니다.

1차 자료: Buzz 저장소의 [NIP-AP 사양](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md).

## 1차 자료

- [Buzz NIP-AP: 에이전트 페르소나](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md)

## 언급된 곳

- [뉴스레터 #46 (2026-10-28): buzz](/ko/newsletters/2026-10-28-newsletter/#buzz)

- [뉴스레터 45](/en/newsletters/2026-10-21-newsletter/#buzz)
