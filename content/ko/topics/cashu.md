---
title: "Cashu: Ecash 프로토콜"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-04-22
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu는 Bitcoin과 Lightning 위에 구축된 Chaumian ecash 프로토콜입니다. 사용자는 mint가 발행한 bearer token을 보유하고, 전체 결제 그래프를 mint에 노출하지 않은 채 그 token을 전송합니다.

## 작동 방식

Cashu는 blind signature를 사용해 ecash token을 발행합니다:

1. **Minting**: 사용자가 Bitcoin/Lightning을 mint에 예치하고 blinded token을 받음
2. **Spending**: token을 mint 개입 없이 peer-to-peer로 전송 가능
3. **Redemption**: 수신자가 mint에서 token을 Bitcoin/Lightning으로 상환

mint는 blinded secret에 서명하므로, 발행 시점에는 원래 secret을 보지 않으면서도 나중에 token을 검증할 수 있습니다. 이로써 mint 내부에서 예치와 상환 사이의 직접 연결이 끊어집니다.

## 보안과 신뢰 모델

Cashu는 결제 프라이버시를 향상시키지만, 여전히 custodial입니다. mint는 상환을 거부할 수 있고, 오프라인이 될 수 있고, 준비금을 잃을 수 있습니다.

Cashu proof는 bearer instrument입니다. proof를 통제하는 사람이 곧 쓸 수 있는 사람입니다. 그래서 proof 관리는 계좌 잔액보다 현금에 더 가깝습니다. 백업, 기기 탈취, 평문 token 유출은 모두 즉각적인 영향을 가집니다.

## Nostr 통합

Cashu는 여러 방식으로 Nostr와 통합됩니다:

- **Nutzaps**: 프라이버시가 강화된 ecash token 기반 zap
- **Escrow**: ridesharing 같은 서비스용 HTLC 기반 결제 escrow
- **Wallets**: Nostr 네이티브 wallet이 암호화된 Cashu token을 릴레이에 저장
- **[NIP-87](/ko/topics/nip-87/)**: Nostr를 통한 mint 발견과 리뷰
- **[TollGate](/ko/topics/tollgate/)**: [v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) 기준 [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)에서 정의된, 연결을 위해 Cashu ecash token을 받는 종량제 네트워크 접속 프로토콜

## 트레이드오프

Cashu는 전송이 오프체인에서 일어나고, 상환 전까지는 흔히 off-mint 상태로 유지되기 때문에 빠릅니다. 대가로 상호운용성과 신뢰 문제가 뒤따릅니다.

실제로 사용자는 종종 같은 mint를 써야 하거나, mint 간 swap이나 bridge가 필요합니다. 그래서 Nostr 애플리케이션은 Cashu를 mint discovery, wallet sync, review 시스템과 함께 쓰는 경우가 많습니다.

---

**주요 출처:**
- [Cashu NUTs Repository](https://github.com/cashubtc/nuts)
- [NUT-00: Cryptography and models](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)
- [NIP-87 Specification](https://github.com/nostr-protocol/nips/blob/master/87.md)

**언급된 뉴스레터:**
- [Newsletter #7](/ko/newsletters/2026-01-28-newsletter/)
- [Newsletter #11](/ko/newsletters/2026-02-25-newsletter/)
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-60: Cashu Wallet](/ko/topics/nip-60/)
- [NIP-87: Cashu Mint Recommendations](/ko/topics/nip-87/)
- [TollGate](/ko/topics/tollgate/)
