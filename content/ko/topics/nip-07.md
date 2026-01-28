---
title: "NIP-07: 브라우저 확장 서명자"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07은 브라우저 확장이 웹 기반 Nostr 클라이언트에 서명 기능을 제공하기 위한 표준 인터페이스를 정의하여, 개인 키를 웹사이트에 노출하지 않고 확장에서 안전하게 보관합니다.

## 작동 방식

브라우저 확장은 웹 앱이 사용할 수 있는 `window.nostr` 객체를 주입합니다:

```javascript
// 공개 키 가져오기
const pubkey = await window.nostr.getPublicKey();

// event 서명
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// 암호화 (NIP-04, 레거시)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// 복호화 (NIP-04, 레거시)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// NIP-44 메서드 (현대적, 지원되는 경우)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## 보안 모델

- **키 격리**: 개인 키가 확장을 절대 떠나지 않음
- **사용자 승인**: 확장이 각 서명 요청에 대해 프롬프트할 수 있음
- **도메인 제어**: 확장이 서명을 요청할 수 있는 사이트를 제한할 수 있음

## 구현체

인기 있는 NIP-07 확장:
- **Alby** - Nostr 서명이 포함된 Lightning 지갑
- **nos2x** - 경량 Nostr 서명자
- **Flamingo** - 기능이 풍부한 Nostr 확장

## 제한 사항

- 브라우저 전용 (모바일 지원 없음)
- 확장 설치 필요
- 각 확장마다 승인을 위한 다른 UX

## 대안

- [NIP-46](/ko/topics/nip-46/) - Nostr relay를 통한 원격 서명
- [NIP-55](/ko/topics/nip-55/) - Android 로컬 서명자

## 관련 항목

- [NIP-44](/ko/topics/nip-44/) - 현대적 암호화 (NIP-04 대체)
- [NIP-46](/ko/topics/nip-46/) - 원격 서명
