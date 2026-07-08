---
title: "NIP-B0: 웹 북마크"
date: 2026-05-28
draft: false
translationOf: /en/topics/nip-b0.md
translationDate: 2026-07-01
categories:
  - Protocol
  - Social
---

NIP-B0은 웹 북마크를 일급 Nostr 이벤트로 게시하는 매개변수화된 대체 가능 이벤트 (kind 39701)를 정의한다. 이 제안은 사용자가 중앙 북마크 서비스에 의존하지 않고도 클라이언트 전반에서 발견되고, zap되고, 재게시될 수 있는 큐레이팅된 북마크 컬렉션을 구축할 수 있도록 한다.

## 작동 방식

북마크는 `d` tag가 북마크된 페이지의 정규 URL인 kind 39701 이벤트이다. 대체 가능 시맨틱은 저자가 중복 이벤트를 생성하지 않고 해당 URL에 대한 자신의 북마크를 업데이트 (재태그, 제목 업데이트, 오래된 것으로 표시)할 수 있도록 한다. content 필드는 북마크에 대한 저자의 노트를 담는다; tag는 발견을 위한 제목, 설명, 이미지 및 `t` 토픽 tag를 담는다.

```json
{
  "kind": 39701,
  "tags": [
    ["d", "https://example.com/an-article-worth-saving"],
    ["title", "Article Title"],
    ["t", "nostr"],
    ["t", "protocol"],
    ["published_at", "1717000000"]
  ],
  "content": "Useful primer on the topic.",
  "pubkey": "...",
  "sig": "..."
}
```

`d` tag는 저자별로 북마크를 고유하게 식별하므로, 두 사용자가 자신의 주석과 tag 세트로 동일한 URL을 북마크할 수 있다.

## 발견 및 큐레이션

모든 북마크가 일급 이벤트이므로, 모든 Nostr 클라이언트는 tag 또는 저자별로 필터링된 kind 39701 이벤트를 구독하여 북마크 피드를 렌더링할 수 있다. 큐레이터 중심 워크플로가 자연스러워진다: 큐레이터가 북마크 목록을 게시하고, 독자가 큐레이터의 pubkey를 팔로우하고, 북마크는 이를 전달하는 모든 relay를 통해 흐른다. 중앙 디렉터리가 없다.

## 구현

- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) — 3-박스 아키텍처 (curator, indexer, viewer)와 직접 큐레이터에게 전달되는 NIP-57 zap으로 자금이 조달되는 tier 시스템을 갖춘 참조 웹 클라이언트. 파일 저장을 위해 NIP-07, NIP-46, NIP-57, NIP-44, NIP-98, NIP-65 및 Blossom BUD-01/BUD-04와 함께 NIP-B0을 구현한다.

## 신뢰 및 보안 참고 사항

- 북마크는 기본적으로 공개된다; 이러한 방식으로 비공개 독서 목록을 게시하지 말 것
- 재게시는 relay가 계속해서 이벤트를 전달하는 것에 의존한다; 임시 relay는 북마크를 삭제한다
- `published_at` tag는 게시자가 주장한 것이며 검증할 수 없다

---

**주요 출처:**
- [NIP-B0 제안 명세](https://github.com/nostr-protocol/nips/pull/2089) — 제안된 kind 39701 웹 북마크 이벤트를 추적
- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) — 큐레이터 tier 시스템이 있는 참조 구현

**언급된 곳:**
- [Newsletter #24: deepmarks NIP-B0 bookmarks with curator-monetized publishing](/ko/newsletters/2026-05-28-newsletter/#deepmarks-nip-b0-bookmarks-with-curator-monetized-publishing)
- [Newsletter #27: Also shipped](/ko/newsletters/2026-06-17-newsletter/#also-shipped)

**참고:**
- [NIP-57: Lightning Zaps](/ko/topics/nip-57/)
- [NIP-65: Relay List Metadata](/ko/topics/nip-65/)
