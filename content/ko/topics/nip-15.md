---
title: "NIP-15: Nostr 마켓플레이스"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15는 Nostr의 탈중앙화 마켓플레이스를 위한 프로토콜을 정의하여, 판매자가 제품을 등록하고 구매자가 Bitcoin과 Lightning을 사용하여 구매할 수 있게 합니다.

## 작동 방식

### 판매자 상점 (Kind 30017)

판매자는 주소 지정 가능 event로 상점을 생성합니다:

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

### 제품 (Kind 30018)

제품은 상점 내에 등록됩니다:

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

## 구매 흐름

1. 구매자가 여러 상점에서 제품을 탐색
2. 구매자가 판매자에게 암호화된 주문 메시지 전송
3. 판매자가 Lightning 인보이스로 응답
4. 구매자가 인보이스 결제
5. 판매자가 제품 배송

## 주요 기능

- **탈중앙화**: 중앙 마켓플레이스 운영자 없음
- **상호운용성**: 모든 NIP-15 클라이언트가 모든 판매자를 탐색 가능
- **프라이빗**: 주문이 구매자와 판매자 간에 암호화됨
- **Bitcoin 네이티브**: Lightning 결제 내장

## 구현체

- **Plebeian Market** - 전체 기능을 갖춘 NIP-15 마켓플레이스
- **Shopstr** - 무허가 Bitcoin 상거래
- **Amethyst** - 소셜 피드에 통합된 제품 목록

## 관련 항목

- [NIP-44](/ko/topics/nip-44/) - 주문을 위한 암호화 메시지
- [NIP-57](/ko/topics/nip-57/) - Lightning Zaps
