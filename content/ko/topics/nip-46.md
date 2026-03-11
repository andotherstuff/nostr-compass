---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
translationOf: /en/topics/nip-46.md
translationDate: 2026-03-11
draft: false
categories:
  - 서명
  - 프로토콜
---
NIP-46은 Nostr 릴레이를 통한 원격 서명을 정의한다. 클라이언트가 흔히 벙커(bunker)라 불리는 별도의 서명자와 통신하여, 서명 키가 사용자가 활발히 사용 중인 앱 외부에 보관될 수 있도록 한다.

## 작동 방식

1. 클라이언트가 벙커 세션 전용으로 사용되는 로컬 키 쌍을 생성한다.
2. `bunker://` 또는 `nostrconnect://` URI를 통해 연결이 수립된다.
3. 클라이언트와 서명자가 릴레이를 통해 암호화된 kind `24133` 요청 및 응답 이벤트를 교환한다.
4. 연결 후, 클라이언트는 `get_public_key`를 호출하여 서명 대상인 실제 사용자 공개 키를 확인한다.

## 연결 방법

- **bunker://** - 서명자가 시작하는 연결
- **nostrconnect://** - QR 코드 또는 딥링크를 통해 클라이언트가 시작하는 연결

`nostrconnect://` 흐름에는 필수 공유 비밀이 포함되어 클라이언트가 첫 번째 응답이 의도된 서명자로부터 온 것인지 검증할 수 있다. 이를 통해 단순한 연결 스푸핑을 방지한다.

## 지원되는 작업

- `sign_event` - 임의의 이벤트에 서명
- `get_public_key` - 서명자로부터 사용자의 공개 키 조회
- `nip04_encrypt/decrypt` - NIP-04 암호화 작업
- `nip44_encrypt/decrypt` - NIP-44 암호화 작업
- `switch_relays` - 서명자에게 업데이트된 릴레이 세트 요청

많은 구현체가 설정 시 `sign_event:1`이나 `nip44_encrypt` 같은 권한 문자열도 사용하여, 서명자가 전체 접근 대신 제한된 범위를 승인할 수 있게 한다.

## 릴레이 및 신뢰 모델

NIP-46은 개인 키를 클라이언트 밖으로 옮기지만, 서명자에 대한 신뢰를 제거하지는 않는다. 서명자는 요청을 승인, 거부, 또는 지연시킬 수 있으며, 클라이언트가 요청하는 모든 작업을 볼 수 있다. 릴레이 선택도 중요한데, 프로토콜이 양측 모두 접근할 수 있는 릴레이를 통한 요청 및 응답 전달에 의존하기 때문이다.

`switch_relays` 메서드는 서명자가 세션을 시간이 지남에 따라 다른 릴레이 세트로 이동할 수 있도록 존재한다. 이를 무시하는 클라이언트는 서명자의 릴레이 환경설정이 변경될 때 안정성이 떨어진다.

---

**주요 출처:**
- [NIP-46 사양](https://github.com/nostr-protocol/nips/blob/master/46.md)

**언급된 뉴스레터:**
- [Newsletter #1: 주요 코드 변경](/en/newsletters/2025-12-17-newsletter/#amethyst-android)
- [Newsletter #3: 12월 회고](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #7: Primal Android가 완전한 서명 허브로](/en/newsletters/2026-01-07-newsletter/#primal-android-becomes-a-full-signing-hub)
- [Newsletter #15: NDK 협업 이벤트와 NIP-46 타임아웃](/en/newsletters/2026-03-04-newsletter/#ndk-collaborative-events-and-nip-46-timeout)

**같이 보기:**
- [NIP-55: Android Signer](/ko/topics/nip-55/)
