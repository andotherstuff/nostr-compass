---
title: "NIP-55: Android 서명자 애플리케이션"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55는 Android 애플리케이션이 전용 서명자 앱에 서명 작업을 요청하는 방법을 정의하여, 사용자가 여러 Nostr 클라이언트를 사용하면서 개인 키를 안전한 한 곳에 보관할 수 있게 합니다.

## 작동 방식

NIP-55는 Android의 콘텐츠 프로바이더 인터페이스를 사용하여 서명 작업을 노출합니다. 서명자 앱이 콘텐츠 프로바이더로 등록하면 다른 Nostr 앱이 개인 키에 직접 접근하지 않고 서명을 요청할 수 있습니다.

흐름:
1. 클라이언트 앱이 서명자의 콘텐츠 프로바이더를 호출
2. 서명자가 사용자에게 승인 UI를 표시
3. 사용자가 요청을 승인하거나 거부
4. 서명자가 서명(또는 거부)을 클라이언트에 반환

## 주요 작업

- **get_public_key** - 사용자의 공개 키 검색(초기 연결 시 한 번만 호출)
- **sign_event** - Nostr 이벤트에 서명
- **nip04_encrypt/decrypt** - NIP-04 메시지 암호화 또는 복호화
- **nip44_encrypt/decrypt** - NIP-44 메시지 암호화 또는 복호화

## 연결 시작

일반적인 구현 실수는 백그라운드 프로세스에서 `get_public_key`를 반복적으로 호출하는 것입니다. 사양은 초기 연결 설정 시에만 한 번 호출한 다음 결과를 캐시할 것을 권장합니다.

---

**주요 출처:**
- [NIP-55 사양](https://github.com/nostr-protocol/nips/blob/master/55.md)

**언급된 곳:**
- [뉴스레터 #1: 릴리스](/ko/newsletters/2025-12-17-newsletter/#releases)
- [뉴스레터 #2: 뉴스](/ko/newsletters/2025-12-24-newsletter/#news)
- [뉴스레터 #2: NIP 업데이트](/ko/newsletters/2025-12-24-newsletter/#nip-updates)

**참고:**
- [NIP-46: Nostr Connect](/ko/topics/nip-46/)

