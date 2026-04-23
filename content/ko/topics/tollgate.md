---
title: "TollGate: Nostr와 Cashu 위의 종량제 인터넷"
date: 2026-04-22
translationOf: /en/topics/tollgate.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocols
---

TollGate는 소액의 잦은 bearer asset 결제를 대가로 네트워크 접속을 판매하는 프로토콜입니다. WiFi router, Ethernet switch, Bluetooth tether처럼 연결을 제어할 수 있는 장치는 TollGate로 동작하며, 가격을 광고하고 [Cashu](/ko/topics/cashu/) ecash token을 받고 세션을 관리합니다. 고객은 실제로 사용한 시간이나 megabyte만큼만 비용을 냅니다. 계정도 없고, 구독도 없고, KYC도 없습니다.

## 작동 방식

TollGate는 관심사를 세 계층으로 나눕니다. 프로토콜 계층은 이벤트 형식과 결제 의미를 정의합니다. 인터페이스 계층은 고객과 gate가 그 이벤트를 어떻게 교환하는지 정의합니다. 미디어 계층은 유료 트래픽이 실제로 지나가는 물리 링크를 설명합니다. 동작하는 TollGate는 각 계층에서 하나 이상의 명세를 조합하며, 일부 인터페이스는 Nostr relay 위에서, 일부는 일반 HTTP 위에서 동작합니다.

프로토콜 계층에서 [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)은 세 가지 기본 이벤트를 정의합니다. 가격과 허용 mint를 나열하는 Advertisement kind, 고객이 얼마나 결제했고 얼마나 사용했는지 추적하는 Session kind, 대역 외 메시지를 위한 Notice kind입니다. [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)는 그 위에 Cashu 결제를 얹어, 고객이 TollGate가 광고한 임의의 mint에서 ecash token을 상환하고 세션 크레딧을 받을 수 있게 합니다.

인터페이스 계층에서는 [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md)부터 HTTP-03까지가 임의의 relay에 WebSocket 연결을 열기 어려운 제한적 운영체제용 HTTP 표면을 정의하고, [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)은 가능한 클라이언트를 위한 Nostr-relay transport를 정의합니다. 미디어 계층에서는 [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)이 captive-portal WiFi 구성이 결제한 고객을 어떻게 식별하고 라우팅하는지 설명합니다.

결제 자산이 credential이 아니라 bearer token이기 때문에, 고객은 이를 만들기 위해 사전 인터넷 접속이 필요하지 않습니다. 로컬 wallet에 들어 있는 Cashu token만 있으면 첫 1분의 연결을 살 수 있고, 그 뒤 필요하면 더 많은 token으로 충전하면 됩니다. TollGate끼리 서로 uplink를 살 수도 있으므로, 도달 범위는 단일 운영자를 넘어 확장될 수 있습니다.

## 왜 중요한가

기존 유료 WiFi는 계정, captive portal, 결제 카드에 의존하며, 각각이 마찰과 데이터 흔적을 남깁니다. TollGate의 모델은 연결성을 어떤 paying customer에게나, 그가 누구인지 알지 못한 채 판매할 수 있는 상품으로 바꿉니다. 이 추상화는 독립 운영자가 각자 가격을 정하고, 선호하는 mint를 받고, lock-in이 아니라 커버리지와 품질로 경쟁하게 합니다.

[v0.1.0 릴리스](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)는 이 명세군의 첫 태그 스냅샷입니다. 모든 세부 사항을 표준화한 것은 아니지만, router firmware, client wallet, multi-hop reseller가 안정적인 기준 구현을 바탕으로 개발을 시작할 만큼 표면을 고정합니다.

---

**주요 출처:**
- [TollGate v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)
- [TIP-01: Base Events](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)
- [TIP-02: Cashu payments](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)
- [HTTP-01 through HTTP-03](https://github.com/OpenTollGate/tollgate/tree/v0.1.0)
- [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)
- [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)
- [TollGate repository](https://github.com/OpenTollGate/tollgate)

**언급된 뉴스레터:**
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [Cashu](/ko/topics/cashu/)
- [NIP-60: Cashu Wallet](/ko/topics/nip-60/)
