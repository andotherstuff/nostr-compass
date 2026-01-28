---
title: "Cashu: Ecash 프로토콜"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-01-28
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu는 Bitcoin과 Lightning Network 위에 구축된 Chaumian ecash 프로토콜로, 암호화 토큰을 통해 프라이빗하고 즉각적이며 낮은 수수료의 결제를 가능하게 합니다.

## 작동 방식

Cashu는 블라인드 서명을 사용하여 추적 불가능한 ecash 토큰을 생성합니다:

1. **발행**: 사용자가 Bitcoin/Lightning을 mint에 입금하고 블라인드 토큰을 받습니다
2. **지출**: 토큰은 mint의 개입 없이 P2P로 전송될 수 있습니다
3. **상환**: 수신자가 mint에서 토큰을 Bitcoin/Lightning으로 상환합니다

블라인딩 과정으로 인해 mint는 입금과 상환을 연결할 수 없어 강력한 프라이버시 보장을 제공합니다.

## 주요 특성

- **프라이버시**: Mint가 사용자 간 토큰 전송을 추적할 수 없음
- **즉시성**: 전송이 오프라인에서 발생하며 블록체인 확인이 필요 없음
- **저수수료**: 토큰 전송에 온체인 수수료 없음
- **수탁형**: 사용자가 mint의 상환 이행을 신뢰해야 함

## Nostr 통합

Cashu는 여러 방식으로 Nostr와 통합됩니다:

- **Nutzaps**: 향상된 프라이버시로 zap으로 전송되는 ecash 토큰
- **에스크로**: 라이드셰어링 같은 서비스를 위한 HTLC 기반 결제 에스크로
- **지갑**: Nostr 네이티브 지갑이 relay에 암호화된 Cashu 토큰을 저장
- **[NIP-87](/ko/topics/nip-87/)**: Nostr를 통한 mint 발견 및 리뷰

## 신뢰 모델

자기 수탁 Bitcoin과 달리 Cashu는 mint 운영자를 신뢰해야 합니다. 사용자는:
- 평판이 좋고 잘 리뷰된 mint를 사용해야 합니다
- 신뢰 수준에 적합한 소액 잔고를 유지해야 합니다
- Mint가 자금과 함께 엑싯 스캠하거나 오프라인이 될 수 있음을 이해해야 합니다

## 관련 항목

- [NIP-87](/ko/topics/nip-87/) - Cashu Mint 추천
- [NIP-60](/ko/topics/nip-60/) - Nostr Wallet
