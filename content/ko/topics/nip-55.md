---
title: "NIP-55: Android 서명 애플리케이션"
date: 2025-12-17
translationOf: /en/topics/nip-55.md
translationDate: 2026-03-11
draft: false
categories:
  - 서명
  - Mobile
---
NIP-55는 Android 앱이 별도의 서명 애플리케이션에 서명 및 암호화 작업을 요청하는 방법을 정의한다. Android 클라이언트에게 브라우저 확장과 원격 벙커의 네이티브 대안을 제공한다.

## 작동 방식

NIP-55는 두 가지 Android 메커니즘을 사용한다:

- **인텐트(Intents)**: 명시적 사용자 승인이 필요한 포그라운드 흐름
- **콘텐츠 리졸버(Content resolvers)**: 사용자가 영구 권한을 부여한 후의 백그라운드 흐름

일반적인 연결 흐름은 `get_public_key`로 시작한다. 서명 앱이 사용자 공개키와 서명 앱 패키지 이름을 반환하고, 클라이언트는 둘 다 캐시해야 한다. 백그라운드 루프에서 `get_public_key`를 반복 호출하는 것은 명세가 명시적으로 경고하는 흔한 구현 실수이다.

## 주요 작업

- **get_public_key** - 사용자의 공개키와 서명 앱 패키지 이름 조회
- **sign_event** - Nostr 이벤트 서명
- **nip04_encrypt/decrypt** - NIP-04 메시지 암호화 또는 복호화
- **nip44_encrypt/decrypt** - NIP-44 메시지 암호화 또는 복호화
- **decrypt_zap_event** - zap 관련 이벤트 페이로드 복호화

## 보안 및 UX 참고사항

NIP-55는 키를 기기 내에 유지하지만, Android 앱 경계와 서명 앱의 권한 처리에 의존한다. 콘텐츠 리졸버 지원은 반복적인 인텐트 프롬프트보다 훨씬 매끄러운 UX를 제공하지만, 사용자가 해당 클라이언트에 영구 승인을 부여한 후에만 가능하다.

Android 웹 앱의 경우, NIP-55는 NIP-46보다 편의성이 떨어진다. 브라우저 기반 흐름은 네이티브 Android 앱처럼 직접적인 백그라운드 응답을 받을 수 없어, 많은 구현이 콜백 URL, 클립보드 전송, 수동 붙여넣기로 대체한다.

---

**주요 출처:**
- [NIP-55 명세](https://github.com/nostr-protocol/nips/blob/master/55.md)

**언급된 뉴스레터:**
- [뉴스레터 #1: 릴리스](/en/newsletters/2025-12-17-newsletter/#releases)
- [뉴스레터 #2: 뉴스](/en/newsletters/2025-12-24-newsletter/#news)
- [뉴스레터 #2: NIP 업데이트](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [뉴스레터 #3: 12월 회고](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [뉴스레터 #7: NIP 업데이트](/en/newsletters/2026-01-07-newsletter/#nip-updates)
- [뉴스레터 #11: NIP 심층 분석](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-55-android-signer-application)

**같이 보기:**
- [NIP-46: Nostr Connect](/ko/topics/nip-46/)
