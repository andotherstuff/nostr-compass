---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
translationOf: /en/topics/nip-47.md
translationDate: 2026-03-07
draft: false
categories:
  - Wallet
  - Lightning
---
NIP-47은 Nostr Wallet Connect를 정의한다. Nostr 앱이 원격 Lightning 월렛 서비스와 통신할 때 월렛의 주요 자격 증명을 모든 클라이언트에 노출하지 않도록 하는 프로토콜이다.

## 작동 방식

월렛 서비스는 지원하는 메서드와 암호화 모드를 설명하는 교체 가능한 kind `13194` 정보 이벤트를 게시한다. 클라이언트는 월렛 서비스 공개 키, 하나 이상의 릴레이, 그리고 해당 연결 전용 비밀을 포함하는 `nostr+walletconnect://` URI를 사용하여 연결한다. 요청은 kind `23194` 이벤트로 전송되고, 응답은 kind `23195` 이벤트로 돌아온다.

## 명령과 알림

주요 메서드에는 `pay_invoice`, `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, `get_info`가 있다. 월렛 서비스는 `payment_received`, `payment_sent`, `hold_invoice_accepted` 같은 알림도 푸시할 수 있다.

사양은 시간이 지나면서 여러 선택적 메서드가 추가되었으나, 최근 정리에서 `multi_` 결제 메서드는 제거되었다. 실제로는 클라이언트가 광범위한 메서드 세트를 가정하지 않고, 월렛의 정보 이벤트에서 광고하는 명령에 맞추는 것이 상호운용성에 더 유리하다.

## 사용 사례

- **Zapping** - 게시물, 프로필, 콘텐츠 크리에이터에게 sats 전송
- **결제** - 모든 Nostr 앱에서 Lightning 인보이스 결제
- **월렛 UX 분리** - 하나의 월렛 서비스를 여러 Nostr 클라이언트에서 사용

## 보안 및 상호운용성 참고사항

연결 URI에는 클라이언트가 서명과 암호화에 사용하는 전용 비밀이 포함된다. 각 앱에 고유한 월렛 ID가 부여되어 취소와 프라이버시 양면에서 도움이 된다. 월렛은 지출 한도를 설정하거나, 메서드를 비활성화하거나, 다른 연결에 영향을 주지 않고 하나의 연결만 취소할 수 있다.

NIP-44가 현재 선호하는 암호화 모드이다. 사양은 이전 구현체를 위해 NIP-04 폴백도 문서화하고 있으므로, 클라이언트는 모든 월렛이 마이그레이션했다고 가정하지 말고 월렛이 광고하는 `encryption` 태그를 확인해야 한다.

---

**주요 출처:**
- [NIP-47 사양](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: Hold Invoice 지원](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: 단순화](https://github.com/nostr-protocol/nips/pull/2210)

**언급된 뉴스레터:**
- [Newsletter #1: 뉴스](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: 릴리스](/en/newsletters/2025-12-24-newsletter/#releases)
- [Newsletter #3: 12월 회고](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #8: NIP 심층 분석](/en/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-47-nostr-wallet-connect)
- [Newsletter #10: NIP 업데이트](/en/newsletters/2026-02-18-newsletter/#nip-updates)

**같이 보기:**
- [NIP-57: Zaps](/ko/topics/nip-57/)
