---
title: "NIP-72: 모더레이션 커뮤니티"
date: 2026-03-25
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Communities
---

NIP-72는 Nostr에서 모더레이션된 커뮤니티를 정의합니다. 커뮤니티는 공유 주제나 그룹 주변에 게시물을 조직하는 방법을 제공하며, 모더레이터가 콘텐츠를 승인한 뒤에만 커뮤니티 독자에게 보이게 합니다.

## 작동 방식

커뮤니티는 생성자가 게시하는 kind `34550` 이벤트로 정의됩니다. 이 이벤트에는 커뮤니티 이름, 설명, 규칙, 모더레이터 pubkey 목록이 포함됩니다. replaceable event 형식(kind `30000`-`39999` 범위)을 사용하므로 커뮤니티 정의는 시간이 지나며 업데이트할 수 있습니다.

```json
{
  "kind": 34550,
  "tags": [
    ["d", "example-community"],
    ["name", "Example Community"],
    ["description", "A community for discussing examples"],
    ["p", "<moderator_pubkey>", "", "moderator"],
    ["relay", "wss://relay.example.com", "moderator"]
  ],
  "content": "",
  "pubkey": "<creator_pubkey>",
  "created_at": 1742860800,
  "sig": "<signature>"
}
```

사용자는 커뮤니티 정의를 가리키는 `a` 태그를 자신의 이벤트에 추가해 게시물을 제출합니다. 이 게시물은 아직 커뮤니티 독자에게 보이지 않습니다. 모더레이터는 제출물을 검토하고, 승인하면 원본 게시물을 감싼 kind `4549` 승인 이벤트를 게시합니다. 커뮤니티를 표시하는 클라이언트는 인정된 모더레이터의 승인 이벤트가 있는 게시물만 보여 줍니다.

이 승인 모델은 커뮤니티가 쓰기 제한이 아니라 읽기 필터라는 뜻입니다. 누구나 게시할 수 있지만, 승인된 게시물만 커뮤니티 피드에 나타납니다. 모더레이터는 기본 데이터를 막는 게이트키퍼라기보다 큐레이터에 가깝습니다.

## 고려 사항

승인 이벤트는 별도의 Nostr 이벤트이므로 moderation 결정은 투명하고 감사 가능합니다. 한 커뮤니티에서 거부된 게시물도 다른 커뮤니티에서는 승인될 수 있습니다. 같은 콘텐츠가 서로 독립적인 moderation을 가진 여러 커뮤니티에 존재할 수 있습니다.

커뮤니티 기능에는 relay 지원이 중요합니다. 클라이언트는 커뮤니티 정의와 승인 이벤트를 모두 질의해야 하므로, 이러한 이벤트 kind를 효율적으로 인덱싱하는 릴레이가 필요합니다.

[NIP-29](/ko/topics/nip-29/) 릴레이 기반 그룹과 비교하면 차이는 분명합니다. NIP-29에서는 멤버십과 moderation 모두에 대해 릴레이가 권한 주체이지만, NIP-72는 일반 Nostr 이벤트 위에서 동작합니다. kind `34550`, `4549`, 그리고 제출 이벤트 kind를 운반하는 어떤 릴레이든 커뮤니티를 제공할 수 있고, moderation은 가시적이며 포크할 수 있습니다. 대신 승인되지 않은 제출물은 클라이언트 렌더링 계층에서만 숨겨지므로, 스팸이 아예 wire에 올라오지 않아야 하는 경우에는 NIP-29가 더 적합합니다.

## 구현체

- [noStrudel](https://github.com/hzrd149/nostrudel)은 오래전부터 NIP-72 커뮤니티를 지원했으며, 모더레이터용 대기 제출물 큐를 포함합니다.
- [Amethyst](https://github.com/vitorpamplona/amethyst)는 [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468)에서 kind `34550` 커뮤니티 정의 작성, 모더레이터 및 relay hint 추가, `a` 태그를 사용한 게시물 제출, kind `4549` 이벤트를 통한 승인 대기열 관리를 포함한 1급 커뮤니티 생성 및 관리 기능을 추가했습니다.

---

**주요 출처:**
- [NIP-72 명세](https://github.com/nostr-protocol/nips/blob/master/72.md) - Moderated Communities
- [Amethyst PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) - NIP-72 커뮤니티 생성과 moderation

**언급된 뉴스레터:**
- [Newsletter #15](/ko/newsletters/2026-03-25-newsletter/)
- [Newsletter #19: Amethyst community support](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-29: 릴레이 기반 그룹](/ko/topics/nip-29/)
