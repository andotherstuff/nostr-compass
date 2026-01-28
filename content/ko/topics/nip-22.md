---
title: "NIP-22: 댓글"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Social
---

NIP-22는 모든 주소 지정 가능한 Nostr 콘텐츠에 댓글을 달기 위한 표준을 정의하여, 기사, 동영상, 캘린더 이벤트 및 기타 주소 지정 가능한 event에 대한 스레드 토론을 가능하게 합니다.

## 작동 방식

댓글은 댓글 대상 콘텐츠를 참조하는 태그가 포함된 kind 1111 event를 사용합니다:

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["E", "root-event-id", "wss://relay.example"],
    ["K", "30023"]
  ],
  "content": "Great article!"
}
```

## 태그 구조

- **`A` 태그**: 댓글 대상 주소 지정 가능 event를 참조 (kind:pubkey:d-tag 형식)
- **`E` 태그**: 스레딩을 위한 루트 event ID를 참조
- **`K` 태그**: 루트 event의 kind를 나타냄
- **`e` 태그**: 중첩 응답을 위한 부모 댓글을 참조

## Kind 1과의 차이점

Kind 1 노트가 다른 노트에 응답할 수 있지만, NIP-22 댓글은 특별히 다음을 위해 설계되었습니다:

- 주소 지정 가능 콘텐츠 (기사, 동영상, 캘린더 이벤트)
- 명확한 부모-자식 관계 유지
- 장문 콘텐츠에 대한 중재 및 스레딩 활성화

## 사용 사례

- 기사 토론
- 동영상 댓글
- [NIP-52](/ko/topics/nip-52/) 캘린더 이벤트 토론
- 위키 페이지 토론 페이지
- 모든 주소 지정 가능 event 유형

## 관련 항목

- [NIP-01](/ko/topics/nip-01/) - 기본 프로토콜 (kind 1 노트)
- [NIP-52](/ko/topics/nip-52/) - 캘린더 이벤트
