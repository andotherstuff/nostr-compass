---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47은 Nostr 애플리케이션을 Lightning 지갑에 연결하는 프로토콜을 정의하여 모든 앱에 지갑 자격 증명을 노출하지 않고 결제를 가능하게 합니다.

## 작동 방식

지갑(예: Zeus)이 특정 Nostr 릴레이에서 결제 요청을 수신하는 NWC 서비스를 실행합니다. 앱은 지갑의 pubkey와 릴레이 정보가 포함된 연결 문자열을 사용하여 연결합니다. 결제 요청과 응답은 앱과 지갑 간에 암호화됩니다.

## 사용 사례

- **Zapping** - 게시물, 프로필, 콘텐츠 크리에이터에게 sats 전송
- **결제** - 모든 Nostr 앱에서 Lightning 인보이스 결제
- **구독** - 프리미엄 콘텐츠에 대한 반복 결제

## 주요 기능

- **예산 제어** - 연결당 지출 한도 설정
- **커스텀 릴레이** - 지갑 통신에 자체 릴레이 사용
- **병렬 결제** - 배치 작업을 위해 동시에 여러 zaps 처리

---

**주요 출처:**
- [NIP-47 사양](https://github.com/nostr-protocol/nips/blob/master/47.md)

**언급된 곳:**
- [뉴스레터 #1: 뉴스](/ko/newsletters/2025-12-17-newsletter/#news)
- [뉴스레터 #2: 릴리스](/ko/newsletters/2025-12-24-newsletter/#releases)

**참고:**
- [NIP-57: Zaps](/ko/topics/nip-57/)

