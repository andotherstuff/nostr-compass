---
title: "NIP-27 (텍스트 노트 참조)"
date: 2026-02-04
description: "NIP-27은 nostr: URI 체계를 사용하여 노트 콘텐츠 내에서 프로필, 노트 및 기타 엔티티를 참조하는 방법을 정의합니다."
---

NIP-27은 텍스트 노트의 콘텐츠 내에 Nostr 엔티티에 대한 참조를 포함하는 방법을 명시합니다. 참조는 `nostr:` URI 체계 다음에 bech32로 인코딩된 식별자(npub, note, nevent, nprofile, naddr)를 사용합니다.

## 작동 방식

다른 사용자를 멘션하거나 다른 event를 참조하는 노트를 작성할 때, 참조는 콘텐츠에 직접 포함됩니다:

```
nostr:npub1...님의 이 게시물을 확인하세요. nostr:note1...에 대한 글입니다.
```

클라이언트는 이러한 참조를 파싱하고 적절하게 렌더링합니다. 일반적으로 클릭 가능한 링크나 인라인 프로필 카드로 표시됩니다. 참조된 엔티티는 인덱싱 및 알림 목적으로 event의 태그에도 추가됩니다.

이 NIP는 해시태그 파싱도 다룹니다. `#`로 시작하는 태그는 추출되어 검색 가능성을 위해 event의 `t` 태그에 추가됩니다.

## 참조 유형

- `nostr:npub1...` - 사용자 프로필 참조
- `nostr:note1...` - 특정 노트 event 참조
- `nostr:nevent1...` - relay 힌트가 포함된 event 참조
- `nostr:nprofile1...` - relay 힌트가 포함된 프로필 참조
- `nostr:naddr1...` - 주소 지정 가능한 event 참조

## 구현

모든 주요 Nostr 클라이언트가 NIP-27을 구현합니다:
- 텍스트 파서가 작성 중 참조를 추출
- 렌더러가 참조를 대화형 요소로 표시
- 알림 시스템이 관련 태그를 사용

## 주요 출처

- [NIP-27 명세](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Bech32 인코딩 엔티티)](/ko/topics/nip-19/) - 참조에 사용되는 인코딩 형식 정의

## 관련 뉴스레터

- [Newsletter #8 (2026-02-04)](/ko/newsletters/2026-02-04-newsletter/) - 줄바꿈 후 해시태그 파싱에 대한 nostr-tools 수정
