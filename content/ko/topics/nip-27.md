---
title: "NIP-27 (텍스트 노트 참조)"
date: 2026-02-04
translationOf: /en/topics/nip-27.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---
NIP-27은 텍스트 노트의 콘텐츠 내에 Nostr 엔티티 참조를 삽입하는 방법을 지정한다. 참조는 `nostr:` URI 스킴 뒤에 bech32로 인코딩된 식별자(npub, note, nevent, nprofile, naddr)를 사용한다.

## 작동 방식

다른 사용자를 멘션하거나 다른 이벤트를 참조하는 노트를 작성할 때, 참조가 콘텐츠에 직접 삽입된다:

```
Check out this post by nostr:npub1... about nostr:note1...
```

클라이언트는 이 참조를 파싱하여 적절하게 렌더링한다. 일반적으로 클릭 가능한 링크나 인라인 프로필 카드로 표시된다. 참조된 엔티티는 인덱싱이나 알림을 위해 이벤트 태그에도 반영될 수 있지만, 사양에서는 이를 선택 사항으로 남겨두고 있다.

NIP에서는 해시태그 파싱도 다룬다. `#`로 시작하는 태그는 추출되어 검색 가능하도록 이벤트의 `t` 태그에 추가된다.

## 참조 유형

- `nostr:npub1...` - 사용자 프로필 참조
- `nostr:note1...` - 특정 노트 이벤트 참조
- `nostr:nevent1...` - 릴레이 힌트가 포함된 이벤트 참조
- `nostr:nprofile1...` - 릴레이 힌트가 포함된 프로필 참조
- `nostr:naddr1...` - 주소 지정 가능한 이벤트 참조

## 왜 중요한가

NIP-27은 사람이 읽는 것과 클라이언트가 저장하는 것을 분리한다. 사용자가 리치 편집기에서 `@name`을 입력하더라도, 게시된 이벤트의 `content`에는 안정적인 `nostr:nprofile...` 참조가 포함될 수 있다. 이를 통해 하나의 앱의 멘션 문법에 의존하지 않고도 클라이언트 간에 참조가 이식 가능해진다.

또 다른 실용적인 장점은 복원력이다. 텍스트에 삽입된 `nostr:nevent...` 또는 `nostr:naddr...`는 다른 클라이언트가 원래의 로컬 렌더링을 본 적이 없더라도 대상을 재구성하기에 충분한 정보를 담고 있다.

## 상호운용성 참고사항

- 콘텐츠 자체에는 [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) 형식을 사용: `nostr:<bech32-id>`
- 멘션 알림이나 더 강력한 이벤트 인덱싱이 필요한 경우에만 `p` 또는 `q` 태그를 추가
- 모든 인라인 참조가 답글 관계가 되어야 한다고 가정하지 말 것. 사양에서는 그 선택을 클라이언트에 맡기고 있다

---

**주요 출처:**

- [NIP-27 사양](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Bech32 인코딩 엔티티)](/ko/topics/nip-19/) - 참조에 사용되는 인코딩 형식을 정의

**언급된 뉴스레터:**

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - 줄바꿈 이후 해시태그 파싱에 대한 nostr-tools 수정

**같이 보기:**
- [NIP-18: 리포스트](/ko/topics/nip-18/)
- [NIP-19: Bech32 인코딩 엔티티](/ko/topics/nip-19/)
