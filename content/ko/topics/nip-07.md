---
title: "NIP-07: 브라우저 확장 서명자"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - 서명
  - 보안
---
NIP-07은 브라우저 확장 프로그램이 웹 기반 Nostr 클라이언트에 서명 기능을 제공하기 위한 표준 인터페이스를 정의한다. 개인 키를 웹사이트에 노출하지 않고 확장 프로그램 내에서 안전하게 보관한다.

## 작동 방식

브라우저 확장 프로그램이 `window.nostr` 객체를 주입하면 웹 앱이 이를 사용할 수 있다:

```javascript
// 공개 키 가져오기
const pubkey = await window.nostr.getPublicKey();

// 이벤트 서명
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// 암호화 (NIP-04, 레거시)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// 복호화 (NIP-04, 레거시)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// NIP-44 메서드 (최신, 지원되는 경우)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## 보안 모델

- **키 격리**: 개인 키가 확장 프로그램 밖으로 나가지 않는다
- **사용자 승인**: 확장 프로그램이 각 서명 요청마다 승인을 요구할 수 있다
- **도메인 제어**: 확장 프로그램이 서명을 요청할 수 있는 사이트를 제한할 수 있다

NIP-07은 키 관리를 개선하지만, 확장 프로그램 자체에 대한 신뢰를 제거하지는 않는다. 악의적이거나 손상된 확장 프로그램은 잘못된 것에 서명하거나, 메타데이터를 유출하거나, 권한을 과도하게 부여할 수 있다.

## 상호운용성 참고사항

NIP-07에서 가장 어려운 부분은 API 형태가 아니라 기능 차이다. 일부 확장 프로그램은 `getPublicKey()`와 `signEvent()`만 지원한다. 다른 확장 프로그램은 `nip04`, `nip44` 또는 더 새로운 선택적 메서드도 제공한다. 웹 앱은 모든 주입된 서명자가 동일하게 동작한다고 가정하지 말고 기능 감지와 적절한 폴백을 구현해야 한다.

사용자 승인 UX도 동작을 변화시킨다. 백그라운드 접근을 자동으로 기대하는 사이트는 한 확장 프로그램에서는 잘 작동하지만 모든 요청마다 승인을 요구하는 다른 확장 프로그램에서는 고장난 것처럼 느껴질 수 있다. 좋은 NIP-07 앱은 서명을 대화형 권한 경계로 취급한다.

## 구현 현황

주요 NIP-07 확장 프로그램:
- **Alby** - Nostr 서명 기능이 포함된 Lightning 지갑
- **nos2x** - 경량 Nostr 서명자
- **Flamingo** - 기능이 풍부한 Nostr 확장 프로그램

## 한계

- 브라우저 전용 (모바일 미지원)
- 확장 프로그램 설치 필요
- 확장 프로그램마다 승인 UX가 다름

기기 간 또는 모바일 서명에는 NIP-46과 NIP-55가 더 적합하다.

---

**주요 출처:**
- [NIP-07 명세](https://github.com/nostr-protocol/nips/blob/master/07.md)
- [PR #2233](https://github.com/nostr-protocol/nips/pull/2233) - `peekPublicKey()` 제안

**언급된 뉴스레터:**
- [Newsletter #7: NIP 업데이트](/en/newsletters/2026-01-28-newsletter/#nip-updates)
- [Newsletter #8: 뉴스](/en/newsletters/2026-02-04-newsletter/#news)
- [Newsletter #11: 뉴스](/en/newsletters/2026-02-25-newsletter/#news)

**같이 보기:**
- [NIP-04: 암호화 다이렉트 메시지 (지원 중단)](/ko/topics/nip-04/)
- [NIP-44: 암호화 페이로드](/ko/topics/nip-44/)
- [NIP-46: Nostr Connect](/ko/topics/nip-46/)
- [NIP-55: Android 서명자 애플리케이션](/ko/topics/nip-55/)
