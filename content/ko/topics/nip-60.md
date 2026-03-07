---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2026-03-07
draft: false
categories:
  - Wallet
  - Ecash
---
NIP-60은 Cashu 기반 ecash 지갑이 Nostr 내에서 작동하는 방식을 정의한다. 지갑 정보가 릴레이에 저장되어, 별도 계정 없이 다양한 애플리케이션에서 작동하는 이식 가능한 지갑을 가능하게 한다.

## 작동 방식

NIP-60은 릴레이에 저장되는 세 가지 핵심 이벤트 타입과 보류 중인 견적을 위한 하나의 선택적 헬퍼 이벤트를 사용한다:

**Wallet 이벤트 (kind 17375):** 민트 URL과 결제 수신용 개인 키를 포함하는 암호화된 지갑 설정이 담긴 대체 가능 이벤트. 이 키는 사용자의 Nostr 신원 키와 분리되어 있다.

**Token 이벤트 (kind 7375):** 암호화된 미사용 Cashu proof를 저장한다. Proof가 사용되면 클라이언트가 기존 이벤트를 삭제하고 남은 proof로 새 이벤트를 생성한다.

**지출 이력 (kind 7376):** 자금 이동을 보여주는 선택적 거래 기록으로, 암호화된 콘텐츠와 생성/삭제된 token 이벤트 참조를 포함한다.

**Quote 이벤트 (kind 7374):** 보류 중인 민트 견적을 위한 선택적 암호화 상태. 명세는 로컬 상태만으로 충분하지 않은 경우를 위해 만료 태그가 있는 단기 이벤트를 권장한다.

## 상태 모델

NIP-60은 자금 수신 행위가 아닌 지갑 상태 동기화에 관한 것이다. Wallet 이벤트는 클라이언트에게 어떤 민트와 지갑 키를 사용할지 알려주고, token 이벤트가 미사용 proof를 담고 있으므로 실제 잔액 상태다.

이 구분은 상호운용성에 중요하다. 두 클라이언트가 같은 지갑을 표시하려면 token 롤오버를 동일하게 해석해야 한다: proof를 사용하고, 대체 proof를 발행하고, [NIP-09](/ko/topics/nip-09/)를 통해 사용된 token 이벤트를 삭제하여 다른 클라이언트가 사용된 proof를 잔액으로 계속 계산하지 않도록 해야 한다.

## 왜 중요한가

- **사용 편의성** - 신규 사용자가 외부 계정 설정 없이 즉시 ecash를 수신할 수 있다
- **상호운용성** - 지갑 데이터가 다양한 Nostr 애플리케이션을 따라다닌다
- **프라이버시** - 모든 지갑 데이터가 사용자의 키로 암호화된다
- **Proof 관리** - 지갑 상태 전환을 추적하여 클라이언트가 동일한 잔액으로 수렴할 수 있다

## 상호운용성 참고사항

클라이언트는 먼저 kind 10019를 통해 지갑 릴레이 정보를 찾고, 전용 지갑 릴레이 목록이 없으면 사용자의 [NIP-65](/ko/topics/nip-65/) 릴레이 목록으로 폴백한다. 이 폴백은 유용하지만, 릴레이가 실제로 암호화된 지갑 이벤트를 저장하고 제공해야 지갑 이식성이 작동한다는 의미이기도 하다.

명세는 지갑 개인 키를 사용자의 Nostr 신원 키와 분리하도록 요구한다. 이는 지갑 수신 처리를 메인 서명 키로부터 격리하고, 하나의 키가 두 가지 다른 용도로 재사용될 가능성을 줄인다.

## 워크플로우

1. 클라이언트가 지갑 릴레이 또는 사용자의 릴레이 목록에서 지갑 설정을 가져온다
2. Token 이벤트를 로드하고 복호화하여 사용 가능한 자금을 확인한다
3. 지출 시 새 token 이벤트를 생성하고 기존 이벤트를 삭제한다
4. 선택적 이력 이벤트가 사용자 참조용으로 거래를 기록한다

---

**주요 출처:**
- [NIP-60 명세](https://github.com/nostr-protocol/nips/blob/master/60.md)

**언급된 뉴스레터:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #9: NIP Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)

**같이 보기:**
- [NIP-57: Zaps](/ko/topics/nip-57/)
- [NIP-09: 이벤트 삭제 요청](/ko/topics/nip-09/)
- [NIP-47: Nostr Wallet Connect](/ko/topics/nip-47/)
