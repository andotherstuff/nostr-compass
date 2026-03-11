---
title: "NIP-99: 분류형 목록"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - 커머스
  - 마켓플레이스
---

NIP-99는 상품, 서비스, 구인, 임대 및 기타 제안을 위한 주소 지정 가능 분류형 목록 이벤트를 정의한다. 오래된 [NIP-15](/ko/topics/nip-15/) 마켓플레이스 사양보다 더 단순한 이벤트 모델을 마켓플레이스 앱에 제공하기 때문에, 현재의 많은 커머스 클라이언트가 대신 NIP-99를 기반으로 구축된다.

## 작동 방식

활성 목록은 kind `30402`를 사용하고, 초안이나 비활성 목록은 kind `30403`을 사용한다. 작성자 pubkey는 판매자 또는 제안 생성자다. `content` 필드에는 사람이 읽을 수 있는 Markdown 설명이 들어가고, 태그에는 제목, 요약, 가격, 위치, 상태 같은 구조화된 필드가 담긴다.

```json
{
  "id": "b3e392b11f5d4f28321cedd09303a748acfd0487aea5a7450b3481c60b6e4f87",
  "pubkey": "a695f6b60119d9521934a691347d9f78e8770b56da16bb255ee286ddf9fda919",
  "created_at": 1741699200,
  "kind": 30402,
  "tags": [
    ["d", "shopstr-handmade-wallet-001"],
    ["title", "Handmade leather wallet"],
    ["summary", "Brown bifold wallet with Bitcoin and Nostr branding"],
    ["published_at", "1741699200"],
    ["location", "Austin, TX"],
    ["price", "75000", "SAT"],
    ["status", "active"],
    ["t", "merch"],
    ["t", "bitcoin"]
  ],
  "content": "Full listing description in Markdown, shipping details, and contact terms.",
  "sig": "4a5c7e8f9012ab34cd56ef7890ab12cd34ef56ab78cd90ef12ab34cd56ef78900112233445566778899aabbccddeeff00112233445566778899aabbccddeeff"
}
```

이 이벤트는 주소 지정 가능하므로, 판매자는 pubkey, kind, `d` 태그의 동일한 식별 튜플을 유지한 채 목록을 업데이트할 수 있다. 따라서 가격이나 상태가 바뀔 때마다 완전히 새로운 불변 노트를 게시하는 것보다, 클라이언트 입장에서 목록 수정 이력이 더 깔끔해진다.

## 왜 중요한가

NIP-99의 강점은 핵심 목록 구조를 표준화하면서도 다양한 마켓플레이스 설계를 허용한다는 점이다. 어떤 클라이언트는 지역 분류 광고에 집중할 수 있고, 다른 클라이언트는 구독 모델에, 또 다른 클라이언트는 전 세계 상품 카탈로그에 집중할 수 있다. 모두가 이벤트 구조에 합의한다면, 판매자는 한 번 게시하고도 여러 클라이언트에서 어느 정도 가시성을 얻을 수 있다.

이 유연성은 현재의 마켓플레이스 프로젝트가 왜 이 사양을 선호하는지도 설명해준다. 이 사양은 검색과 표시를 지원할 만큼 충분히 구조화되어 있지만, 모든 앱을 하나의 escrow, 배송, 결제 워크플로에 강제로 맞추지는 않는다.

## 구현 메모

- `price` 태그는 선택적 빈도 필드를 추가해 일회성 결제와 반복 결제를 모두 표현할 수 있다.
- `t` 태그는 카테고리 또는 검색 키워드 역할을 한다.
- `image` 태그를 사용하면 클라이언트가 Markdown 본문을 파싱하지 않고도 갤러리 뷰를 렌더링할 수 있다.
- 마켓플레이스가 더 풍부한 상품 문맥을 원할 경우, 목록은 `e` 또는 `a` 태그로 관련 이벤트나 문서를 연결할 수 있다.

## 구현체

- [Shopstr](https://github.com/shopstr-eng/shopstr) - 에이전트용 MCP 엔드포인트와 함께 NIP-99 목록을 사용하는 Nostr 마켓플레이스
- [Milk Market](https://github.com/shopstr-eng/milk-market) - 동일한 목록 계층 위에 구축된 식품 마켓플레이스로, 법정화폐와 Bitcoin 결제를 혼합 지원

---

**주요 출처:**
- [NIP-99 Specification](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - NIP-99 목록 위에 구축된 MCP 커머스 엔드포인트
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - 마켓플레이스 목록 위의 구독 및 멀티 머천트 checkout

**언급된 뉴스레터:**
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/ko/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**같이 보기:**
- [NIP-15: Marketplace Offers](/ko/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/ko/topics/nip-47/)
- [NIP-60: Cashu Wallet](/ko/topics/nip-60/)
