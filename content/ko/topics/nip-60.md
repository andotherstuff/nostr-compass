---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2025-12-31
draft: false
categories:
  - 지갑
  - Ecash
---

NIP-60은 Cashu 기반 ecash 지갑이 Nostr 내에서 어떻게 작동하는지 정의합니다. 지갑 정보는 relay에 저장되어, 별도의 계정 없이도 다양한 애플리케이션에서 작동하는 휴대용 지갑을 가능하게 합니다.

## 작동 방식

NIP-60은 relay에 저장되는 세 가지 유형의 이벤트를 사용합니다:

**지갑 이벤트 (kind 17375):** mint URL과 결제 수신을 위한 개인 키를 포함한 암호화된 지갑 구성을 담고 있는 교체 가능한 이벤트입니다. 이 키는 사용자의 Nostr 신원 키와 별개입니다.

**토큰 이벤트 (kind 7375):** 암호화된 미사용 Cashu 증명을 저장합니다. 증명이 사용되면 클라이언트는 이전 이벤트를 삭제하고 남은 증명으로 새 이벤트를 생성합니다.

**지출 내역 (kind 7376):** 자금 이동을 보여주는 선택적 거래 기록으로, 암호화된 콘텐츠와 생성/파기된 토큰 이벤트에 대한 참조를 포함합니다.

## 주요 특징

- **사용 편의성** - 신규 사용자가 외부 계정 설정 없이 즉시 ecash를 받을 수 있습니다
- **상호 운용성** - 지갑 데이터가 다양한 Nostr 애플리케이션에서 사용자를 따라갑니다
- **프라이버시** - 모든 지갑 데이터가 사용자의 키로 암호화됩니다
- **증명 관리** - 이중 지불을 방지하기 위해 어떤 토큰 이벤트가 사용되었는지 추적합니다

## 워크플로우

1. 클라이언트가 relay에서 지갑 구성을 가져옴
2. 토큰 이벤트가 로드되고 복호화되어 사용 가능한 자금을 확인
3. 지출 시 새 토큰 이벤트가 생성되고 이전 것이 삭제됨
4. 선택적 내역 이벤트가 사용자 참조를 위해 거래를 기록

---

**주요 출처:**
- [NIP-60 사양](https://github.com/nostr-protocol/nips/blob/master/60.md)

**관련 언급:**
- [뉴스레터 #3: 12월 요약](/ko/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**참고:**
- [NIP-57: Zaps](/ko/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/ko/topics/nip-47/)
