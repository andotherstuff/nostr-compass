---
title: "NIP-69: P2P 거래"
date: 2025-12-17
translationOf: /en/topics/nip-69.md
translationDate: 2026-03-07
draft: false
categories:
  - Trading
  - Protocol
---
NIP-69는 Nostr를 통한 P2P 거래 프로토콜을 정의하며, 분산된 유동성 풀 대신 여러 플랫폼에 걸친 통합 오더북을 생성한다.

## 작동 방식

NIP-69는 매수 및 매도 주문에 addressable kind 38383 이벤트를 사용한다. addressable 형식이 중요한 이유는 주문이 `d` 태그를 통해 같은 논리적 ID를 유지하면서 시간에 따라 여러 상태를 거칠 수 있기 때문이다.

## 주문 구조

주문은 태그를 사용하여 거래 매개변수를 지정한다:

- `d` - 주문 ID
- `k` - 주문 유형 (buy/sell)
- `f` - 법정화폐 통화 (ISO 4217 코드)
- `amt` - 비트코인 금액 (사토시 단위)
- `fa` - 법정화폐 금액
- `pm` - 수락하는 결제 방법
- `premium` - 가격 프리미엄/할인 백분율
- `network` - 비트코인 네트워크 (mainnet, testnet, signet, regtest)
- `layer` - 정산 레이어 (onchain, lightning, liquid)
- `expiration` - 주문 만료 시점

## 주문 생명주기

주문은 다음 상태를 거친다:
- `pending` - 매칭 가능한 상태로 열려 있음
- `in-progress` - 상대방과 거래가 시작됨
- `success` - 거래 완료
- `canceled` - 메이커가 철회
- `expired` - 만료 시간 경과

이 사양은 두 가지 시간 제한을 구분한다. `expires_at`는 대기 중인 주문이 열린 것으로 간주되지 않아야 하는 시점을 표시하고, `expiration`은 릴레이가 [NIP-40](/ko/topics/nip-40/)과 함께 사용하여 오래된 주문 이벤트를 완전히 제거할 수 있는 타임스탬프를 제공한다.

## 왜 중요한가

NIP-69는 상호운용성을 위한 것이다. Mostro, lnp2pBot, RoboSats, Peach 및 기타 P2P 거래 시스템이 유동성을 별도의 앱 내에 가두는 대신 하나의 공유 이벤트 형식으로 주문을 노출할 수 있다.

선택적 `g` 태그는 나머지 주문 스키마를 변경하지 않고 로컬 대면 거래도 가능하게 한다. 이는 로컬 현금 거래에는 지리적 필터링이 필요하지만 온라인 Lightning 거래에는 필요하지 않기 때문에 유용하다.

## 보안 및 신뢰

`bond` 태그는 양측이 지불해야 하는 보증금을 지정하여 포기나 사기에 대한 보호를 제공한다.

이것이 거래 상대방 위험을 제거하지는 않는다. 결제 분쟁, 법정화폐 사기, 평판, 수탁 규칙은 여전히 애플리케이션 레이어에 있다. NIP-69는 주문 게시를 표준화하지, 분쟁 해결을 표준화하지는 않는다.

---

**주요 출처:**
- [NIP-69 사양](https://github.com/nostr-protocol/nips/blob/master/69.md)
- [Mostro 프로토콜 사양](https://mostro.network/protocol/)

**언급된 뉴스레터:**
- [뉴스레터 #1: NIP 업데이트](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [뉴스레터 #1: 릴리스](/en/newsletters/2025-12-17-newsletter/#releases)
- [뉴스레터 #2: 뉴스](/en/newsletters/2025-12-24-newsletter/#news)

**같이 보기:**
- [NIP-40: 만료 타임스탬프](/ko/topics/nip-40/)
