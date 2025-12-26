---
title: "NIP-69: P2P 거래"
date: 2025-12-17
draft: false
categories:
  - Trading
  - Protocol
---

NIP-69는 Nostr를 통한 P2P 거래 프로토콜을 정의하여 분산된 유동성 풀 대신 여러 플랫폼에 걸친 통합 오더북을 생성합니다.

## 이벤트 Kind

- **Kind 38383** - P2P 주문 이벤트

## 주문 구조

주문은 태그를 사용하여 거래 매개변수를 지정합니다:

- `d` - 주문 ID
- `k` - 주문 유형(매수/매도)
- `f` - 법정화폐(ISO 4217 코드)
- `amt` - 사토시 단위 Bitcoin 금액
- `fa` - 법정화폐 금액
- `pm` - 허용되는 결제 방법
- `premium` - 가격 프리미엄/할인 백분율
- `network` - 정산 레이어(onchain, lightning, liquid)
- `expiration` - 주문 만료 시간

## 주문 수명주기

주문은 상태를 통해 진행됩니다:
- `pending` - 열려 있고 매칭 가능
- `in-progress` - 상대방과 거래 시작됨
- `success` - 거래 완료
- `canceled` - 메이커가 철회함
- `expired` - 만료 시간 지남

## 보안

`bond` 태그는 양 당사자가 지불해야 하는 보증금을 지정하여 이탈이나 사기에 대한 보호를 제공합니다.

---

**주요 출처:**
- [NIP-69 사양](https://github.com/nostr-protocol/nips/blob/master/69.md)

**언급된 곳:**
- [뉴스레터 #1: NIP 업데이트](/ko/newsletters/2025-12-17-newsletter/#nip-updates)
- [뉴스레터 #1: 릴리스](/ko/newsletters/2025-12-17-newsletter/#releases)
- [뉴스레터 #2: 뉴스](/ko/newsletters/2025-12-24-newsletter/#news)

