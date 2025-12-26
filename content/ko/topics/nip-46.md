---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46은 서명자 애플리케이션이 키를 보유하고 클라이언트가 Nostr 릴레이를 통해 서명을 요청할 수 있는 원격 서명을 정의합니다.

## 작동 방식

1. 서명자가 연결 URI(`bunker://` 또는 `nostrconnect://`)를 생성
2. 사용자가 클라이언트에 URI를 붙여넣기
3. 클라이언트가 서명자의 릴레이에 암호화된 이벤트로 서명 요청 전송
4. 서명자가 사용자에게 승인을 요청하고 서명된 이벤트 반환

## 연결 방법

- **bunker://** - 서명자 주도 연결
- **nostrconnect://** - QR 코드 또는 딥 링크를 통한 클라이언트 주도 연결

## 지원되는 작업

- `sign_event` - 임의의 이벤트에 서명
- `get_public_key` - 서명자의 공개 키 검색
- `nip04_encrypt/decrypt` - NIP-04 암호화 작업
- `nip44_encrypt/decrypt` - NIP-44 암호화 작업

---

**주요 출처:**
- [NIP-46 사양](https://github.com/nostr-protocol/nips/blob/master/46.md)

**언급된 곳:**
- [뉴스레터 #1: 주목할 만한 코드 변경](/ko/newsletters/2025-12-17-newsletter/#amethyst-android)

**참고:**
- [NIP-55: Android 서명자](/ko/topics/nip-55/)

