---
title: "NIP-99: 분류 광고 목록"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - 상거래
  - 마켓플레이스
---

NIP-99는 상품, 서비스, 채용, 임대 및 기타 제안을 위한 주소 지정 가능한 분류 광고 목록 이벤트를 정의합니다. 이전의 [NIP-15](/ko/topics/nip-15/) 마켓플레이스 사양보다 더 간단한 이벤트 모델을 마켓플레이스 앱에 제공하기 때문에, 현재 많은 상거래 클라이언트가 NIP-99를 기반으로 구축합니다.

## 작동 방식

활성 목록은 kind `30402`를 사용하고, 초안 또는 비활성 목록은 kind `30403`을 사용합니다. 저자 pubkey는 판매자 또는 제안 생성자입니다. `content` 필드는 Markdown으로 된 사람이 읽을 수 있는 설명을 담고, 태그는 제목, 요약, 가격, 위치, 상태 같은 구조화된 필드를 보유합니다.

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

이벤트는 주소 지정 가능하므로, 판매자는 pubkey, kind, `d` 태그로 구성된 동일한 신원 튜플을 유지하면서 목록을 업데이트할 수 있습니다. 이로 인해 가격이나 상태가 변경될 때마다 완전히 새로운 불변 노트를 게시하는 것보다 클라이언트의 목록 수정이 더 깔끔해집니다.

## 중요성

NIP-99의 강점은 다양한 마켓플레이스 설계를 위한 여지를 남기면서도 핵심 목록 형태를 표준화한다는 점입니다. 한 클라이언트는 지역 분류 광고에, 다른 하나는 구독에, 또 다른 하나는 글로벌 제품 카탈로그에 집중할 수 있습니다. 모두 이벤트 구조에 동의한다면 판매자는 한 번 게시하고도 일정 수준의 크로스 클라이언트 가시성을 얻을 수 있습니다.

이 유연성은 또한 현재 마켓플레이스 프로젝트들이 NIP-99를 선호하는 이유를 설명합니다. 사양은 검색과 표시를 지원할 만큼 구조화되어 있지만, 모든 앱을 단일 에스크로, 배송 또는 결제 워크플로로 강제하지 않습니다.

## 구현 참고 사항

- `price` 태그는 선택적 빈도 필드를 추가하여 일회성 또는 반복 결제를 설명할 수 있습니다.
- `t` 태그는 카테고리 또는 검색 키워드로 작동합니다.
- `image` 태그는 클라이언트가 Markdown 본문을 파싱하지 않고 갤러리 뷰를 렌더링할 수 있게 합니다.
- 마켓플레이스가 더 풍부한 제품 컨텍스트를 원할 때 목록은 `e` 또는 `a` 태그로 관련 이벤트나 문서에 링크할 수 있습니다.

## 구현체

- [Shopstr](https://github.com/shopstr-eng/shopstr) - 에이전트 대면 MCP 엔드포인트가 있는 NIP-99 목록을 사용하는 Nostr 마켓플레이스
- [Milk Market](https://github.com/shopstr-eng/milk-market) - 혼합 결제 옵션이 있는 동일한 목록 레이어 위에 구축된 식품 마켓플레이스

---

**주요 출처:**
- [NIP-99 사양](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - NIP-99 목록 위에 구축된 MCP 상거래 엔드포인트
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - 마켓플레이스 목록 위에 구축된 구독 및 다중 판매자 결제

**언급된 곳:**
- [뉴스레터 #13: Shopstr와 Milk Market MCP 상거래 인터페이스 오픈](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**같이 보기:**
- [NIP-15: 마켓플레이스 제안](/ko/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/ko/topics/nip-47/)
- [NIP-60: Cashu Wallet](/ko/topics/nip-60/)
