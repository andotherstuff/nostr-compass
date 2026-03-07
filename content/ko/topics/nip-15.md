---
title: "NIP-15: Nostr 마켓플레이스"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---
NIP-15는 Nostr 기반 탈중앙 마켓플레이스 프로토콜을 정의하며, 판매자가 상품을 등록하고 구매자가 Bitcoin 및 Lightning으로 결제할 수 있게 한다.

## 작동 방식

### 판매자 상점 (Kind 30017)

판매자는 주소 지정 가능 이벤트로 상점을 생성한다:

```json
{
  "kind": 30017,
  "tags": [
    ["d", "my-stall"],
    ["name", "Bob's Electronics"],
    ["description", "Quality used electronics"],
    ["currency", "sat"],
    ["shipping", "{...shipping options...}"]
  ]
}
```

### 상품 (Kind 30018)

상품은 상점 내에 등록된다:

```json
{
  "kind": 30018,
  "tags": [
    ["d", "product-123"],
    ["stall_id", "my-stall"],
    ["name", "Raspberry Pi 4"],
    ["price", "50000"],
    ["quantity", "5"],
    ["images", "https://..."]
  ]
}
```

## 구매 절차

1. 구매자가 여러 상점의 상품을 탐색
2. 구매자가 판매자에게 암호화된 주문 메시지 전송
3. 판매자가 Lightning 인보이스로 응답
4. 구매자가 인보이스 결제
5. 판매자가 상품 배송

## 왜 중요한가

- **탈중앙화**: 중앙 마켓플레이스 운영자 없음
- **상호운용**: 모든 NIP-15 클라이언트가 모든 판매자 조회 가능
- **프라이버시**: 주문이 구매자와 판매자 사이에서 암호화
- **Bitcoin 네이티브**: Lightning 결제 내장

실질적 장점은 이식성이다. 판매자가 카탈로그 데이터를 한 번 게시하면 여러 클라이언트가 이를 렌더링할 수 있어, 하나의 마켓플레이스 프론트엔드에 종속되지 않는다.

## 절충점

NIP-15는 상품 목록을 표준화하지, 신뢰를 표준화하지는 않는다. 구매자는 여전히 판매자의 정당성, 재고의 실제 여부, 분쟁 처리 방법을 스스로 판단해야 한다. 프로토콜은 공통 데이터 구조와 메시지 흐름을 제공하지만, 평판과 이행은 애플리케이션 수준의 문제로 남는다.

결제와 배송도 부분적으로만 표준화되어 있다. 클라이언트가 상점과 상품을 이해할 수 있어도, 인보이스, 주문 상태, 배송 추적에는 커스텀 로직이 필요할 수 있다.

## 구현 현황

- **Plebeian Market** - 전체 기능 NIP-15 마켓플레이스
- **Shopstr** - 허가 불필요 Bitcoin 커머스
- **Amethyst** - 소셜 피드 내 상품 목록 통합

---

**주요 출처:**
- [NIP-15 명세](https://github.com/nostr-protocol/nips/blob/master/15.md)

**언급된 뉴스레터:**
- [뉴스레터 #7: 2024년 1월 프로토콜 강화](/en/newsletters/2026-01-28-newsletter/#january-2024-protocol-hardening)

**같이 보기:**
- [NIP-44: 암호화 페이로드](/ko/topics/nip-44/)
- [NIP-57: Lightning Zaps](/ko/topics/nip-57/)
