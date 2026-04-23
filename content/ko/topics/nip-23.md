---
title: "NIP-23: 장문 콘텐츠"
date: 2026-04-08
translationOf: /en/topics/nip-23.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
---

NIP-23은 Nostr에서 장문 텍스트 콘텐츠를 위한 kind `30023`을 정의합니다. kind `1`의 짧은 노트와 달리, 장문 이벤트는 `d` 태그로 식별되는 parameterized replaceable event이며 Markdown 서식을 지원하고 제목, 요약, 이미지, 게시일 같은 메타데이터 태그를 포함합니다.

## 작동 방식

장문 이벤트는 고유 식별자로 `d` 태그를 사용하는 kind `30023`을 사용하므로, 작성자는 같은 `d` 태그를 가진 새 이벤트를 게시해 콘텐츠를 업데이트할 수 있습니다. `content` 필드에는 Markdown 텍스트가 들어갑니다. 표준 태그로는 `title`, `summary`, `image`(헤더 이미지 URL), `published_at`(원래 게시 시각), `t`(hashtag)가 있습니다. 이 이벤트는 parameterized replaceable event이므로 릴레이는 작성자별 `d` 태그당 최신 버전만 저장합니다.

## 주요 태그

- `d` - 고유한 글 식별자(slug)
- `title` - 글 제목
- `summary` - 짧은 설명
- `image` - 헤더 이미지 URL
- `published_at` - 원래 게시 Unix timestamp (`created_at`과 다르며, `created_at`은 수정 때마다 바뀜)
- `t` - hashtag 또는 주제 태그

## 구현체

- [Habla](https://habla.news) - 장문 콘텐츠 리더 및 게시 도구
- [YakiHonne](https://yakihonne.com) - 장문 콘텐츠 플랫폼
- [Highlighter](https://highlighter.com) - 읽기 및 주석 도구

---

**주요 출처:**
- [NIP-23 명세](https://github.com/nostr-protocol/nips/blob/master/23.md)

**같이 보기:**
- [NIP-01 (기본 프로토콜)](/ko/topics/nip-01/)
