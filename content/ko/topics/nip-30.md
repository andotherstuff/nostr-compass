---
title: "NIP-30: 커스텀 이모지"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---
NIP-30은 Nostr 이벤트에서 커스텀 이모지를 표시하는 방법을 정의한다. 커스텀 이모지는 이벤트 콘텐츠에서 숏코드(`:shortcode:`)를 사용하여 참조되며, 각 숏코드를 이미지 URL에 매핑하는 `emoji` 태그를 통해 해석된다.

## 작동 방식

커스텀 이모지를 사용하는 이벤트는 콘텐츠의 숏코드 참조와 함께 `emoji` 태그를 포함한다:

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

클라이언트는 렌더링된 콘텐츠에서 `:gleam:`과 `:nostrich:`를 지정된 URL의 인라인 이미지로 대체한다. 숏코드는 영숫자여야 하며(밑줄 구분자 허용), 이미지 URL은 인라인 표시에 적합한 작고 정사각형인 이미지를 가리켜야 한다.

## 이모지 세트

커스텀 이모지는 kind 30030 매개변수화된 대체 가능 이벤트로 게시되는 이름 있는 세트로 구성할 수 있다. 각 세트는 `d` 태그 식별자 아래 관련 이모지를 그룹화한다:

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

2026년 3월 업데이트([PR #2247](https://github.com/nostr-protocol/nips/pull/2247))에서 emoji 태그에 선택적 이모지 세트 주소 참조를 추가하여, 사용자가 이모지를 클릭할 때 클라이언트가 원본 세트를 열어 탐색하거나 북마크할 수 있게 했다.

## 상호운용성 참고사항

커스텀 이모지는 표현 기능이지 전송 보장이 아니다. 클라이언트가 NIP-30을 이해하지 못하거나 이미지 URL을 가져올 수 없는 경우, 원시 `:shortcode:` 텍스트를 그대로 표시해야 한다. 이 폴백이 읽기 가능한 숏코드가 중요한 이유이다.

태그는 세트를 참조하지 않는 한 이벤트에 로컬이다. 두 개의 다른 이벤트에서 `:fire:`를 재사용하는 것이 둘 다 같은 이미지나 세트를 가리키지 않는 한 공유된 전역 의미를 암시하지 않는다. 클라이언트는 현재 이벤트의 이모지 정의를 먼저 해석해야 한다.

## 리액션

NIP-30 커스텀 이모지는 kind 7 리액션 이벤트에서도 작동한다. `content`가 숏코드로 설정되고 일치하는 `emoji` 태그가 있는 리액션은 참조된 이벤트에 커스텀 이모지 리액션으로 렌더링된다:

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
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - 태그 내 이모지 세트 주소

**언급된 뉴스레터:**
- [Newsletter #12: NoorNote v0.5.x](/en/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [Newsletter #12: NIP 업데이트](/en/newsletters/2026-03-04-newsletter/#nip-updates)
