---
title: "NIP-30: 커스텀 이모지"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-04
draft: false
categories:
  - NIP
  - 소셜
---

NIP-30은 클라이언트가 Nostr event에서 커스텀 이모지를 표시하는 방법을 정의합니다. 커스텀 이모지는 event 내용에서 숏코드(`:shortcode:`)를 사용하여 참조되며, 각 숏코드를 이미지 URL에 매핑하는 `emoji` 태그를 통해 해석됩니다.

## 작동 방식

커스텀 이모지를 사용하는 event는 내용의 숏코드 참조와 함께 `emoji` 태그를 포함합니다:

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

클라이언트는 렌더링된 내용에서 `:gleam:`과 `:nostrich:`를 지정된 URL의 인라인 이미지로 대체합니다. 숏코드는 영숫자여야 하며(밑줄 구분자 허용), 이미지 URL은 인라인 표시에 적합한 작은 정사각형 이미지를 가리켜야 합니다.

## 이모지 세트

커스텀 이모지는 kind 30030 매개변수화된 교체 가능 event로 게시되는 명명된 세트로 구성할 수 있습니다. 각 세트는 `d` 태그 식별자 아래 관련 이모지를 그룹화합니다:

```json
{
  "kind": 30030,
  "tags": [
    ["d", "nostr-animals"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"],
    ["emoji", "nostrcat", "https://example.com/nostrcat.png"]
  ]
}
```

2026년 3월 업데이트([PR #2247](https://github.com/nostr-protocol/nips/pull/2247))에서 이모지 태그에 선택적 이모지 세트 주소 참조가 추가되어, 사용자가 이모지를 클릭할 때 클라이언트가 원본 세트를 열어 탐색하거나 북마크할 수 있게 되었습니다.

## 리액션

NIP-30 커스텀 이모지는 kind 7 리액션 event에서도 작동합니다. `content`가 숏코드로 설정되고 일치하는 `emoji` 태그가 있는 리액션은 참조된 event에 커스텀 이모지 리액션으로 렌더링됩니다:

```json
{
  "kind": 7,
  "content": ":fire:",
  "tags": [
    ["emoji", "fire", "https://example.com/fire.gif"],
    ["e", "<event-id>"]
  ]
}
```

---

**주요 출처:**
- [NIP-30 사양](https://github.com/nostr-protocol/nips/blob/master/30.md)
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - 태그에 이모지 세트 주소 추가

**언급된 곳:**
- [뉴스레터 #12: NoorNote v0.5.x](/ko/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [뉴스레터 #12: NIP 업데이트](/ko/newsletters/2026-03-04-newsletter/#nip-업데이트)
