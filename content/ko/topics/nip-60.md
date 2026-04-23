---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Ecash
---

NIP-60은 Cashu 기반 ecash wallet이 Nostr 안에서 어떻게 동작하는지 정의합니다. wallet 정보는 릴레이에 저장되므로, 별도 계정을 요구하지 않고도 여러 애플리케이션 사이를 이동할 수 있는 이식 가능한 wallet을 만들 수 있습니다.

## 작동 방식

NIP-60은 릴레이에 저장되는 세 가지 핵심 이벤트 타입과, 보류 중인 quote를 위한 하나의 선택적 헬퍼 이벤트를 사용합니다:

**Wallet 이벤트 (kind 17375):** mint URL과 결제 수신용 개인 키를 포함한 암호화 wallet 설정이 담긴 replaceable 이벤트입니다. 이 키는 사용자의 Nostr identity 키와는 별개입니다.

**Token 이벤트 (kind 7375):** 암호화된 미사용 Cashu proof를 저장합니다. proof가 사용되면 클라이언트는 예전 이벤트를 삭제하고 남은 proof로 새 이벤트를 만듭니다.

**지출 이력 (kind 7376):** 자금 이동을 보여 주는 선택적 거래 기록으로, 암호화된 내용과 생성되거나 소멸한 token 이벤트에 대한 참조를 담습니다.

**Quote 이벤트 (kind 7374):** 보류 중인 mint quote를 위한 선택적 암호화 상태입니다. 명세는 로컬 상태만으로 충분하지 않은 경우를 위해, 주로 만료 태그가 있는 짧은 생명의 이벤트를 권장합니다.

## 상태 모델

NIP-60은 돈을 받는 행위 자체보다 wallet 상태 동기화에 관한 명세입니다. wallet 이벤트는 어떤 mint와 wallet 키를 써야 하는지 알려 주고, token 이벤트는 미사용 proof를 담기 때문에 실제 잔액 상태를 이룹니다.

이 구분은 상호운용성에 중요합니다. 두 클라이언트가 같은 wallet을 보여 주려면 token rollover를 똑같이 해석해야 합니다. 즉, proof를 쓰고, 대체 proof를 게시하고, 다른 클라이언트가 사용된 proof를 잔액으로 계속 세지 않도록 [NIP-09](/ko/topics/nip-09/)를 통해 사용된 token 이벤트를 삭제해야 합니다.

## 왜 중요한가

- **사용 편의성** - 새 사용자가 외부 계정 설정 없이 곧바로 ecash를 받을 수 있음
- **상호운용성** - wallet 데이터가 여러 Nostr 애플리케이션 사이에서 따라다님
- **프라이버시** - 모든 wallet 데이터가 사용자의 키로 암호화됨
- **Proof 관리** - wallet 상태 전이를 추적해 클라이언트가 같은 잔액으로 수렴하게 함

## 상호운용성 참고사항

클라이언트는 먼저 kind 10019를 통해 wallet relay 정보를 찾고, 전용 wallet relay 목록이 없으면 사용자의 [NIP-65](/ko/topics/nip-65/) relay 목록으로 fallback합니다. 이 fallback은 유용하지만, 동시에 wallet 이식성이 실제로는 릴레이가 이 암호화 wallet 이벤트를 저장하고 제공해 줄 때만 작동한다는 뜻이기도 합니다.

또한 명세는 wallet 개인 키를 사용자의 Nostr identity 키와 분리해 둘 것을 요구합니다. 이렇게 해야 wallet 수신 처리가 메인 서명 키에서 분리되고, 하나의 키를 서로 다른 두 목적에 재사용할 가능성이 줄어듭니다.

## 워크플로우

1. 클라이언트가 wallet relay 또는 사용자 relay 목록에서 wallet 설정을 가져옵니다.
2. Token 이벤트를 불러와 복호화해 사용 가능한 자금을 확인합니다.
3. 지출은 새 token 이벤트를 만들고 오래된 이벤트를 삭제합니다.
4. 선택적 history 이벤트가 사용자 참고용으로 거래를 기록합니다.

---

**주요 출처:**
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)

**언급된 뉴스레터:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #11: NIP Deep Dive](/ko/newsletters/2026-02-25-newsletter/)
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/en/newsletters/2026-03-11-newsletter/)

**같이 보기:**
- [NIP-57: Zaps](/ko/topics/nip-57/)
- [NIP-09: 이벤트 삭제 요청](/ko/topics/nip-09/)
- [NIP-47: Nostr Wallet Connect](/ko/topics/nip-47/)
