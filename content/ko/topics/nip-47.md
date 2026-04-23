---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
translationOf: /en/topics/nip-47.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47은 Nostr Wallet Connect를 정의합니다. 이 프로토콜은 Nostr 앱이 원격 Lightning wallet 서비스와 통신할 수 있게 해 주지만, wallet의 핵심 자격 증명을 모든 클라이언트에 노출하지는 않습니다.

## 작동 방식

wallet 서비스는 지원하는 메서드와 암호화 모드를 설명하는 replaceable kind `13194` 정보 이벤트를 게시합니다. 클라이언트는 wallet 서비스 pubkey, 하나 이상의 relay, 그리고 그 연결 전용 비밀을 담은 `nostr+walletconnect://` URI를 사용해 연결합니다. 요청은 kind `23194` 이벤트로 보내고 응답은 kind `23195` 이벤트로 받습니다.

## 명령과 알림

일반적인 메서드에는 `pay_invoice`, `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, `get_info`가 있습니다. wallet 서비스는 `payment_received`, `payment_sent`, `hold_invoice_accepted` 같은 notification도 푸시할 수 있습니다.

명세는 시간이 지나며 여러 선택 메서드를 키워 왔지만, 최근 정리 과정에서 `multi_` 결제 메서드는 제거되었습니다. 실제로는 클라이언트가 광범위한 메서드 집합을 가정하는 대신, wallet의 info 이벤트가 광고한 명령에 맞추는 편이 상호운용성에 더 유리합니다.

## 사용 사례

- **Zapping** - 게시물, 프로필, 콘텐츠 제작자에게 sats 보내기
- **결제** - 어떤 Nostr 앱에서든 Lightning invoice 지불
- **wallet UX 분리** - 하나의 wallet 서비스를 여러 Nostr 클라이언트에서 함께 사용

## 보안과 상호운용성 참고사항

연결 URI에는 클라이언트가 서명과 암호화에 쓰는 전용 비밀이 포함됩니다. 덕분에 각 앱은 고유한 wallet identity를 갖고, 이는 revoke와 privacy 양쪽에 도움이 됩니다. wallet은 지출 한도를 씌우거나, 특정 메서드를 비활성화하거나, 다른 연결에 영향을 주지 않고 하나의 연결만 revoke할 수 있습니다.

NIP-44가 이제 선호되는 암호화 모드입니다. 명세는 오래된 구현체를 위해 여전히 NIP-04 fallback도 문서화하므로, 클라이언트는 모든 wallet이 이미 마이그레이션했다고 가정하지 말고 wallet이 광고한 `encryption` 태그를 확인해야 합니다.

---

**주요 출처:**
- [NIP-47 Specification](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: Hold Invoice Support](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: Simplification](https://github.com/nostr-protocol/nips/pull/2210)

**언급된 뉴스레터:**
- [Newsletter #1: News](/ko/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: Releases](/ko/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #8: NIP Deep Dive](/ko/newsletters/2026-02-04-newsletter/)
- [Newsletter #10: NIP Updates](/ko/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: ShockWallet Nostr-native wallet sync](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-57: Zaps](/ko/topics/nip-57/)
