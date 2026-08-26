---
title: "NIP-38: 사용자 상태"
date: 2026-08-26
translationOf: /en/topics/nip-38.md
translationDate: 2026-08-26
draft: false
description: "일반 상태와 음악 상태 범주를 포함한, 짧게 유지되는 사용자 상태 이벤트를 정의합니다."
---

NIP-38은 짧은 사용자 상태를 위해 kind 30315 addressable 이벤트를 정의합니다. `d` tag는 `general`이나 `music` 같은 상태 범주를 나타내고, 선택적인 `r`과 `p` tag는 URL로 연결하거나 아티스트를 지정할 수 있습니다. 클라이언트는 이벤트의 `expiration` tag를 사용해 오래된 상태의 표시를 멈출 수 있습니다.

## 작동 방식

사용자는 상태 문구를 `content`에 담은 kind 30315 이벤트를 게시합니다. 이벤트는 pubkey, kind, `d` tag로 addressable하므로 같은 범주의 더 새로운 이벤트가 이전 것을 대체합니다. content 필드가 비어 있으면 그 상태는 지워집니다.

---

**주요 출처:**

- [NIP-38 사양](https://github.com/nostr-protocol/nips/blob/master/38.md) - 사용자 상태

**언급된 곳:**

- [뉴스레터 #37: NoorNote v1.3.6: 프로필 상태와 분류 광고](/ko/newsletters/2026-08-26-newsletter/#noornote-v136-프로필-상태와-분류-광고)
