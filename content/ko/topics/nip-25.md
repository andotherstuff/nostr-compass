---
title: "NIP-25: 리액션"
date: 2026-07-29
translationOf: /en/topics/nip-25.md
translationDate: 2026-08-26
draft: false
categories:
  - Protocol
  - Social
---

NIP-25는 리액션을 kind `7` 이벤트로 정의합니다. 노트, 기사, 분류 광고, 그 밖에 참조된 이벤트에 이모지나 짧은 리액션을 붙이기 위한 공통 이벤트 형태를 클라이언트에 제공합니다.

## 작동 방식

리액션 이벤트는 리액션 텍스트를 `content`에 담고 대상 이벤트의 `e` tag로 대상을 참조합니다. 대상이 addressable이면 리액션은 그 `a` tag도 포함합니다. 또한 참조된 이벤트 작성자에 대한 `p` tag도 포함하므로, relay와 클라이언트는 이벤트 내용에서 수신자를 추측하지 않고 알림을 전달할 수 있습니다.

기본 리액션은 `+`이므로 클라이언트는 비어 있는 리액션 content를 긍정적 반응으로 다룰 수 있습니다. 다른 이모지도 유효한 리액션 값입니다. 사양은 부정적 리액션을 위한 `-`도 허용하며, 이는 최초 도입 이후 2022년 7월의 후속 수정에서 추가되었습니다.

클라이언트는 리액션을 만들 때 대상 참조와 작성자 tag를 보존해야 합니다. 리액션은 일반적인 서명 이벤트이므로 평범한 relay subscription을 통해 전달되고, kind `7`을 인식하는 어떤 클라이언트에서도 렌더링될 수 있습니다.

## 구현

NIP-25는 노트에 대한 일반적인 상호작용의 일부로 Nostr 클라이언트와 라이브러리에 널리 구현되어 있습니다. kind와 tag로 이루어진 단순한 모델 덕분에 클라이언트는 별도의 전송 프로토콜 없이 개수, 개별 리액션, 알림을 표시할 수 있습니다.

---

**주요 출처:**

- [NIP-25 Specification](https://github.com/nostr-protocol/nips/blob/master/25.md)
- [도입 커밋](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88)
- [비추천 후속 수정](https://github.com/nostr-protocol/nips/commit/89bb08ba8683)

**언급된 곳:**

- [뉴스레터 #33: Nostr의 여섯 번의 7월](/ko/newsletters/2026-07-29-newsletter/#nostr의-여섯-번의-7월)
- [뉴스레터 #37: Marmot](/ko/newsletters/2026-08-26-newsletter/#marmot)

**함께 보기:**
- [NIP-01: Basic Protocol](/ko/topics/nip-01/)
- [NIP-10: Text Note Threading](/ko/topics/nip-10/)
