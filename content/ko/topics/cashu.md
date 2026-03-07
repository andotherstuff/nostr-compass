---
title: "Cashu: Ecash 프로토콜"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-03-07
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---
Cashu는 Bitcoin과 Lightning 위에 구축된 Chaumian ecash 프로토콜이다. 사용자는 mint가 발행한 bearer 토큰을 보유하고, 전체 결제 그래프를 mint에 노출하지 않고 토큰을 전송한다.

## 작동 방식

Cashu는 blind signature를 사용해 ecash 토큰을 발행한다:

1. **발행(Minting)**: 사용자가 Bitcoin/Lightning을 mint에 예치하고 blinded 토큰을 받는다
2. **지출(Spending)**: 토큰은 mint 개입 없이 P2P로 전송할 수 있다
3. **상환(Redemption)**: 수신자가 mint에서 토큰을 Bitcoin/Lightning으로 상환한다

mint는 blinded secret에 서명하므로, 발행 시점의 원본 secret을 보지 않고도 나중에 토큰을 검증할 수 있다. 이로써 mint 내부에서 예치와 상환 사이의 직접적인 연결이 끊어진다.

## 보안 및 신뢰 모델

Cashu는 결제 프라이버시를 개선하지만 여전히 수탁형(custodial)이다. mint는 상환을 거부하거나, 오프라인이 되거나, 담보 자금을 잃을 수 있다.

Cashu proof는 bearer instrument이다. proof를 통제하는 사람이 사용할 수 있다. 이 때문에 proof 관리는 계좌 잔액보다 현금에 가깝다. 백업, 기기 침해, 평문 토큰 유출 모두 즉각적으로 영향을 미친다.

## Nostr 통합

Cashu는 여러 방식으로 Nostr와 통합된다:

- **Nutzaps**: 프라이버시가 강화된 ecash 토큰 기반 zap
- **에스크로**: 라이드셰어링 같은 서비스를 위한 HTLC 기반 결제 에스크로
- **지갑**: Nostr 네이티브 지갑이 암호화된 Cashu 토큰을 릴레이에 저장
- **[NIP-87](/ko/topics/nip-87/)**: Nostr를 통한 mint 발견 및 리뷰

## 트레이드오프

Cashu는 전송이 오프체인에서, 상환까지는 오프민트에서 이루어지기 때문에 빠르다. 트레이드오프는 상호운용성과 신뢰이다.

실제로 사용자는 같은 mint를 사용하거나, mint 간 스왑이나 브릿지가 필요한 경우가 많다. 그래서 Nostr 애플리케이션은 Cashu를 mint 발견, 지갑 동기화, 리뷰 시스템과 결합하는 경우가 많다.

---

**주요 출처:**
- [Cashu NUTs 저장소](https://github.com/cashubtc/nuts)
- [NUT-00: 암호화 및 모델](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60: Cashu 지갑](/ko/topics/nip-60/)
- [NIP-87: Cashu Mint 추천](/ko/topics/nip-87/)

**언급된 뉴스레터:**
- [뉴스레터 #7](/en/newsletters/2026-01-28-newsletter/)
- [뉴스레터 #11](/en/newsletters/2026-02-25-newsletter/)

**같이 보기:**
- [NIP-60: Cashu 지갑](/ko/topics/nip-60/)
- [NIP-87: Cashu Mint 추천](/ko/topics/nip-87/)
