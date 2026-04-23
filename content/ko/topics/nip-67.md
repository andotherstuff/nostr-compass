---
title: "NIP-67: EOSE 완전성 힌트"
date: 2026-04-22
translationOf: /en/topics/nip-67.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-67은 [NIP-01](/ko/topics/nip-01/)의 기존 `EOSE` 메시지에, 릴레이가 필터와 일치하는 저장 이벤트를 모두 전달했는지 나타내는 선택적 세 번째 요소를 추가하는 공개 제안입니다. 목적은 오늘날 클라이언트가 구독이 정말 끝났는지, 아니면 릴레이 쪽 상한에 걸려 중간에 끊겼는지 판단하기 위해 쓰는 불안정한 휴리스틱을 대체하는 것입니다.

## 문제

`EOSE`는 저장된 이벤트와 실시간 이벤트의 경계를 표시하지만, 완전성에 대한 정보는 담고 있지 않습니다. 실제로 릴레이는 보통 클라이언트의 `limit`과 별개로 구독당 상한을 두며, 일반적으로 300개에서 1000개 사이입니다. 예를 들어 300개 상한이 있는 릴레이에 마지막 노트 500개를 요청하면, 클라이언트는 300개 이벤트와 `EOSE`를 받지만 그것이 "원래 300개뿐"인지 "중간에 잘렸다"인지 구분할 방법이 없습니다. 현재의 우회책은 받은 이벤트 수를 `limit`과 비교해 방어적으로 pagination을 이어 가는 것인데, 상한이 요청한 `limit`보다 낮으면 이벤트를 놓치고, 실제 일치 수가 상한 배수일 때는 불필요한 왕복을 추가로 하게 됩니다.

타임스탬프 경계가 같은 이벤트가 여러 개 있을 때는 상황이 더 나빠집니다. `until = oldest_created_at`로 pagination하면 릴레이가 타임스탬프를 어떻게 비교하느냐에 따라 가장 오래된 시각을 공유하는 이벤트를 놓치거나 중복으로 가져오게 됩니다.

## 변경 사항

NIP-67은 `EOSE`에 선택적인 세 번째 요소를 추가합니다:

```
["EOSE", "<subscription_id>", "finish"]   // 일치하는 저장 이벤트를 모두 전달함
["EOSE", "<subscription_id>"]             // 완전성에 대한 주장 없음 (기존 형식)
```

명세는 긍정 신호만 정의합니다. NIP-67 지원을 광고한 릴레이가 이 힌트를 생략하면, 아직 더 남아 있다는 뜻입니다. NIP-67을 광고하지 않는 릴레이는 기존 휴리스틱으로 처리되므로, 이 변경은 현재의 모든 클라이언트와 릴레이와 하위 호환됩니다.

클라이언트는 릴레이가 NIP-67을 지원한다는 사실을 알고 있다면 `"finish"`를 보는 즉시 pagination을 멈출 수 있습니다. 이렇게 하면 상한이 결과 집합과 정확히 같을 때도 추가 왕복을 피할 수 있고, 사용자에게 더 정확한 완전성 정보를 보여 줄 수 있습니다.

## 상태

이 제안은 NIPs 저장소에 대한 [PR #2317](https://github.com/nostr-protocol/nips/pull/2317)로 열려 있습니다.

---

**주요 출처:**
- [PR #2317: NIP-67 EOSE Completeness Hint](https://github.com/nostr-protocol/nips/pull/2317)
- [NIP-01 명세](https://github.com/nostr-protocol/nips/blob/master/01.md)

**언급된 뉴스레터:**
- [Newsletter #19: NIP Updates](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-01: 기본 프로토콜 흐름](/ko/topics/nip-01/)
- [NIP-11: 릴레이 정보 문서](/ko/topics/nip-11/)
