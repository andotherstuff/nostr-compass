---
title: "NIP-22: 댓글"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---
NIP-22는 주소 지정 가능한 모든 Nostr 콘텐츠에 댓글을 달 수 있는 표준을 정의하여, 글, 동영상, 캘린더 이벤트 및 기타 주소 지정 가능한 이벤트에 대한 스레드 토론을 가능하게 한다.

## 작동 방식

댓글은 평문 `content`를 가진 kind 1111 이벤트를 사용한다. 루트 범위 태그는 대문자이고, 부모-답글 태그는 소문자이다:

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["K", "30023"],
    ["P", "<root-pubkey>", "wss://relay.example"],
    ["a", "30023:pubkey:article-id", "wss://relay.example"],
    ["e", "<parent-event-id>", "wss://relay.example", "<parent-pubkey>"],
    ["k", "30023"],
    ["p", "<parent-pubkey>", "wss://relay.example"]
  ],
  "content": "Great article!"
}
```

## 태그 구조

- **`A` / `E` / `I`** - 토론의 루트 범위: 주소 지정 가능한 이벤트, 이벤트 ID, 또는 외부 식별자
- **`K`** - 해당 루트 항목의 kind 또는 루트 범위 유형
- **`P`** - 루트 이벤트가 존재할 때 그 작성자
- **`a` / `e` / `i`** - 답글 대상인 직접 부모
- **`k`** - 부모 항목의 kind 또는 범위 유형
- **`p`** - 부모 항목의 작성자

최상위 댓글의 경우 루트와 부모가 보통 같은 대상을 가리킨다. 댓글에 대한 답글의 경우 루트는 고정된 채로 소문자 부모 태그가 답글 대상인 특정 댓글을 가리키도록 이동한다.

## 상호운용성 참고사항

NIP-22 댓글은 kind 1 답글의 범용 대체가 아니다. 사양에서 댓글을 kind 1 노트에 답글로 사용해서는 안 된다고 명시하고 있다. 노트 간 스레드에는 클라이언트가 계속 [NIP-10](/ko/topics/nip-10/)을 사용해야 한다.

또 다른 유용한 구분은 범위이다. NIP-22는 `I` 및 `i` 태그를 통해 URL과 [NIP-73](/ko/topics/nip-73/)의 기타 외부 식별자를 포함한 비노트 리소스에 토론을 고정할 수 있다. 이를 통해 클라이언트가 웹 페이지, 팟캐스트 또는 기타 Nostr 외부 객체에 댓글 스레드를 붙이는 표준 방법을 갖게 된다.

## 활용 사례

- 글 토론
- 동영상 댓글
- [NIP-52](/ko/topics/nip-52/) 캘린더 이벤트 토론
- 위키 페이지 토론 페이지
- `I` 태그로 식별되는 외부 리소스에 대한 댓글

---

**주요 출처:**
- [NIP-22 사양](https://github.com/nostr-protocol/nips/blob/master/22.md)

**언급된 뉴스레터:**
- [Newsletter #7: Notedeck](/en/newsletters/2026-01-28-newsletter/#notedeck)
- [Newsletter #10: AI Agent NIPs Arrive](/en/newsletters/2026-02-18-newsletter/#ai-agent-nips-arrive)
- [Newsletter #12: diVine](/en/newsletters/2026-03-04-newsletter/#divine)

**같이 보기:**
- [NIP-10: 답글 스레드](/ko/topics/nip-10/)
- [NIP-52: 캘린더 이벤트](/ko/topics/nip-52/)
- [NIP-73: 외부 콘텐츠 ID](/ko/topics/nip-73/)
