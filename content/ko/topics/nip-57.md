---
title: "NIP-57: Zaps"
date: 2025-12-17
translationOf: /en/topics/nip-57.md
translationDate: 2026-03-07
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---
NIP-57은 zap을 정의한다. Zap은 Lightning 결제를 Nostr 신원 및 콘텐츠에 연결하는 방식이다. Zap 가능 인보이스 요청과 결제 후 지갑이 발행하는 영수증 이벤트 모두를 표준화한다.

## 작동 방식

1. 클라이언트가 프로필 메타데이터 또는 대상 이벤트의 `zap` 태그에서 수신자의 LNURL 엔드포인트를 탐색한다.
2. 클라이언트가 서명된 kind `9734` zap 요청을 릴레이가 아닌 수신자의 LNURL 콜백으로 전송한다.
3. 사용자가 인보이스를 결제한다.
4. 수신자의 지갑 서버가 zap 요청에 나열된 릴레이에 kind `9735` zap 영수증을 발행한다.
5. 클라이언트가 zap을 검증하고 표시한다.

## Zap 요청 (kind 9734)

Zap 요청은 결제자와 의도된 대상을 식별하는 서명된 이벤트다. 일반적으로 다음을 포함한다:

- 수신자 공개키가 포함된 `p` 태그
- zap 대상 이벤트가 포함된 `e` 태그 (선택사항)
- 밀리사토시 단위의 `amount` 태그
- 영수증을 발행할 릴레이를 나열하는 `relays` 태그

주소 지정 가능 콘텐츠는 `e` 태그 대신 또는 함께 `a` 태그를 사용할 수 있다. 선택적 `k` 태그는 대상 kind를 기록한다.

## Zap 영수증 (kind 9735)

결제 확인 후 수신자의 지갑 서버가 발행한다. 다음을 포함한다:

- `description` 태그 내 원본 zap 요청
- 결제된 인보이스가 포함된 `bolt11` 태그
- 결제 증명인 `preimage` 태그

클라이언트는 수신자의 LNURL `nostrPubkey`, 인보이스 금액, 원본 zap 요청에 대해 영수증을 검증해야 한다. 해당 검증 없는 영수증은 단순한 주장에 불과하다.

## 신뢰와 트레이드오프

Zap은 소셜 그래프 내에서 결제를 가시적으로 만들기 때문에 유용하지만, 영수증은 여전히 수신자의 지갑 인프라가 생성한다. 명세 자체도 zap 영수증이 보편적 결제 증명이 아님을 명시한다. Zap 영수증은 zap 요청에 연결된 인보이스가 결제되었다는 지갑 서명 진술로 이해하는 것이 가장 정확하다.

---

**주요 출처:**
- [NIP-57 명세](https://github.com/nostr-protocol/nips/blob/master/57.md)

**언급된 뉴스레터:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#amethyst-android)
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)

**같이 보기:**
- [NIP-47: Nostr Wallet Connect](/ko/topics/nip-47/)
