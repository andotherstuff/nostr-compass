---
title: "Gamma Markets"
date: 2026-07-15
draft: false
translationOf: /en/topics/gamma-markets.md
translationDate: 2026-07-15
categories:
  - Commerce
  - Marketplace
  - Protocol
---

Gamma Markets는 [NIP-99](/ko/topics/nip-99/) 클래시파이드 리스팅 위에 직접 구축된 전자상거래 규약 집합으로, Nostr 마켓플레이스 개발자 작업 그룹, 즉 Shopstr, Cypher, Plebeian Market, Conduit Market을 만든 팀들이 협력하여 개발했습니다. 이는 NIP-99 자체가 정의하지 않은 채 두는 배송, 주문 흐름, 컬렉션, 리뷰 규약을 채워 넣습니다.

## 작동 방식

Gamma Markets는 NIP-99의 기존 kind `30402` 리스팅 이벤트를 중심으로 다섯 개의 이벤트 kind를 추가하며, 그 이벤트의 형태는 바꾸지 않습니다:

- **Kind 30405** - 상품 컬렉션, `a` tag를 통해 여러 리스팅을 함께 묶음
- **Kind 30406** - 배송 옵션, 국가별 가격 책정과 선택적 무게 또는 거리 기반 비용 규칙 포함
- **Kind 16** - 주문 메시지: 생성(type 1), 결제 요청(type 2), 상태 업데이트(type 3), 배송 업데이트(type 4)
- **Kind 14** - 일반 구매자/판매자 통신
- **Kind 17** - 결제 영수증
- **Kind 31555** - 상품 리뷰, 특정 판매자 pubkey와 리스팅 `d` tag로 주소 지정됨

판매자의 결제 선호는 kind `0` 프로필 메타데이터의 `payment_preference` tag를 통해 선언되며, 클라이언트는 [NIP-89](/ko/topics/nip-89/) 애플리케이션 추천을 통해 호환 앱을 발견합니다. 주문 통신은 자체 새 암호화 방식 없이 [NIP-17](/ko/topics/nip-17/) 비공개 메시지 위에 구축됩니다.

이 명세의 결정적 설계 선택은 아무것도 계단식으로 상속되지 않는다는 것입니다: 컬렉션에 속하거나 배송 옵션을 사용하는 리스팅은 상위의 설정을 자동으로 상속하는 대신 `a` tag로 명시적으로 참조합니다. 이는 상품이 부스의 통화와 배송 표를 조용히 상속하던 더 오래된 [NIP-15](/ko/topics/nip-15/) 부스 모델에서 의도적으로 벗어난 것입니다.

### 예시: 주문 생성 (kind 16, type 1)

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

## 왜 중요한가

NIP-99 단독으로는 리스팅 자체, 즉 서명되고 주소 지정 가능한 클래시파이드 광고만 표준화합니다. Gamma Markets 이전에는 NIP-99 위에 실제 전자상거래를 구축하는 모든 클라이언트가 배송, 체크아웃, 리뷰에 대한 자체 비공개 규약을 발명했으며, 이는 NIP-99 호환 클라이언트 두 개가 각각 리스팅을 올바르게 렌더링하면서도 서로 간에 주문을 완료할 공유된 방법이 없다는 것을 의미했습니다. Gamma Markets는 NIP-99 리스팅 형식 자체를 건드리지 않고 그 공백을 메우므로, 기존 NIP-99 리스팅은 수정 없이 유효하게 유지됩니다.

## 구현

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Nostr 마켓플레이스, 명세를 저술한 네 프로젝트 중 하나
- [Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) - 같은 설계 공간에서 자체 주문 상태 및 체크아웃 흐름을 구축하는 마켓플레이스 프로토콜

---

**주요 출처:**
- [Gamma Markets 명세 저장소](https://github.com/GammaMarkets/market-spec)
- [NIP-99 전자상거래 사용 사례 확장, PR #1784](https://github.com/nostr-protocol/nips/pull/1784) - 표준 NIP-99 문서에서 Gamma Markets 명세로의 병합된 링크

**언급된 곳:**
- [Newsletter #31: NIP Deep Dive: NIP-99와 Gamma Markets 커머스 확장](/ko/newsletters/2026-07-15-newsletter/#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)

**함께 보기:**
- [NIP-99: Classified Listings](/ko/topics/nip-99/)
- [NIP-15: Nostr Marketplace](/ko/topics/nip-15/)
- [NIP-17: Private Direct Messages](/ko/topics/nip-17/)
