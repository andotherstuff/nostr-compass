---
title: "NIP-57: Zaps"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57은 결제가 발생했다는 암호화 증명과 함께 Nostr 사용자와 콘텐츠에 Lightning 결제를 보내는 방법인 zaps를 정의합니다.

## 작동 방식

1. 클라이언트가 수신자의 kind 0 프로필에서 Lightning 주소를 가져옴
2. 클라이언트가 zap 요청 이벤트를 포함하여 수신자의 LNURL 서버에 인보이스 요청
3. 사용자가 인보이스 결제
4. LNURL 서버가 Nostr 릴레이에 kind 9735 zap 영수증 게시
5. 클라이언트가 수신자의 콘텐츠에 zap 표시

## Zap 요청 (kind 9734)

zap 요청은 누가 zap을 보냈고 어떤 콘텐츠에 보냈는지 증명하는 서명된 이벤트입니다. 포함 내용:
- 수신자 pubkey가 있는 `p` 태그
- zap된 이벤트가 있는 `e` 태그(선택적)
- 밀리사토시 단위의 `amount` 태그
- 영수증을 게시할 위치를 나열하는 `relays` 태그

## Zap 영수증 (kind 9735)

결제 확인 후 LNURL 서버에서 게시합니다. 포함 내용:
- `description` 태그의 원본 zap 요청
- 결제된 인보이스가 있는 `bolt11` 태그
- 결제를 증명하는 `preimage` 태그

---

**주요 출처:**
- [NIP-57 사양](https://github.com/nostr-protocol/nips/blob/master/57.md)

**언급된 곳:**
- [뉴스레터 #1: 뉴스](/ko/newsletters/2025-12-17-newsletter/#news)
- [뉴스레터 #2: 뉴스](/ko/newsletters/2025-12-24-newsletter/#news)

**참고:**
- [NIP-47: Nostr Wallet Connect](/ko/topics/nip-47/)

