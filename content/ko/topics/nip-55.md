---
title: "NIP-55: Android Signer Application"
date: 2025-12-17
translationOf: /en/topics/nip-55.md
translationDate: 2026-04-22
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55는 Android 앱이 별도 signer 애플리케이션에 서명과 암호화 작업을 요청하는 방법을 정의합니다. Android 클라이언트에 browser extension과 원격 bunker의 네이티브 대안을 제공합니다.

## 작동 방식

NIP-55는 두 가지 Android 메커니즘을 사용합니다:

- **Intents** - 명시적인 사용자 승인이 필요한 foreground 흐름
- **Content resolvers** - 사용자가 영구 권한을 부여한 뒤의 background 흐름

일반적인 연결 흐름은 `get_public_key`로 시작합니다. signer는 사용자 pubkey와 signer 패키지 이름을 함께 반환하며, 클라이언트는 둘 다 캐시해야 합니다. background loop 안에서 `get_public_key`를 반복 호출하는 것은 명세가 명시적으로 경고하는 흔한 구현 실수입니다.

## 핵심 작업

- **get_public_key** - 사용자의 pubkey와 signer 패키지 이름 가져오기
- **sign_event** - Nostr 이벤트 서명
- **nip04_encrypt/decrypt** - NIP-04 메시지 암호화 또는 복호화
- **nip44_encrypt/decrypt** - NIP-44 메시지 암호화 또는 복호화
- **decrypt_zap_event** - zap 관련 이벤트 payload 복호화

## 보안과 UX 참고사항

NIP-55는 키를 기기 안에 유지하지만, 여전히 Android 앱 경계와 signer의 권한 처리에 의존합니다. Content resolver 지원은 반복되는 intent 승인 프롬프트보다 훨씬 매끄러운 UX를 제공하지만, 이는 사용자가 해당 클라이언트에 지속적인 승인을 준 이후에만 가능합니다.

Android 웹 앱에서는 NIP-55가 NIP-46보다 덜 편리합니다. browser 기반 흐름은 네이티브 Android 앱처럼 직접적인 background 응답을 받을 수 없기 때문에, 많은 구현이 callback URL, clipboard 전달, 수동 붙여넣기로 fallback합니다.

---

**주요 출처:**
- [NIP-55 Specification](https://github.com/nostr-protocol/nips/blob/master/55.md)

**언급된 뉴스레터:**
- [Newsletter #1: Releases](/ko/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: News](/ko/newsletters/2025-12-24-newsletter/)
- [Newsletter #2: NIP Updates](/ko/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #4: NIP Updates](/ko/newsletters/2026-01-07-newsletter/)
- [Newsletter #11: NIP Deep Dive](/ko/newsletters/2026-02-25-newsletter/)
- [Newsletter #13: Samizdat v1.0.0-alpha](/en/newsletters/2026-03-11-newsletter/)

**같이 보기:**
- [NIP-46: Nostr Connect](/ko/topics/nip-46/)
