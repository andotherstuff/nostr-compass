---
title: "NIP-04: 암호화된 다이렉트 메시지 (지원 중단)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-04는 kind 4 이벤트와 ECDH로 파생한 공유 비밀을 사용하는 암호화된 다이렉트 메시지를 정의합니다. 이것은 Nostr의 첫 DM 방식이었지만, 이제는 레거시 기술이며 새로운 비공개 메시징 작업은 NIP-17로 옮겨갔습니다.

## 작동 방식

메시지는 다음과 같은 기본 흐름의 kind 4 이벤트를 사용합니다:

1. 발신자가 secp256k1 ECDH로 공유 비밀을 도출합니다.
2. 평문을 AES-256-CBC로 암호화합니다.
3. 이벤트는 수신자를 가리키는 `p` 태그를 포함합니다.
4. 암호문은 IV와 함께 base64로 인코딩되어 `content`에 저장됩니다.

이벤트 자체는 여전히 일반적인 서명된 Nostr 이벤트이므로, 릴레이는 평문을 읽지 못해도 바깥 메타데이터는 볼 수 있습니다.

## 보안과 프라이버시 한계

NIP-04는 상당한 프라이버시 결함이 있습니다:

- **메타데이터 유출** - 모든 메시지에서 발신자 pubkey가 공개적으로 보임
- **발신자 프라이버시 부재** - 누가 누구에게 메시지를 보내는지 누구나 볼 수 있음
- **정확한 타임스탬프** - 메시지 시각이 무작위화되지 않음
- **비표준 키 처리** - 이 방식은 ECDH 포인트의 X 좌표만 사용해 라이브러리 간 정확성 확보를 어렵게 만들고 프로토콜 진화 여지도 거의 남기지 않았음

명세는 이것이 "암호화 통신의 최신 기술 수준에 전혀 가깝지 않다"고 명시적으로 경고합니다.

## 왜 대체되었는가

NIP-04는 메시지 내용을 암호화하지만 소셜 그래프를 숨기지 않습니다. 릴레이 운영자는 여전히 누가 이벤트를 보냈는지, 누가 그것을 받는지, 언제 발행되었는지를 볼 수 있습니다. payload를 복호화하지 못해도 이 메타데이터만으로 대화 관계를 파악하기에 충분합니다.

NIP-17은 NIP-44 payload 암호화와 NIP-59 gift wrapping을 결합해 이 문제를 해결합니다. 이를 통해 릴레이와 일반 관찰자로부터 발신자를 숨깁니다. 새 구현은 NIP-04를 호환성 전용으로 취급해야 합니다.

## 구현 현황

레거시 클라이언트와 signer는 예전 대화와 오래된 앱이 여전히 돌아다니기 때문에 여전히 NIP-04 encrypt/decrypt 메서드를 노출합니다. 이 호환성 계층은 마이그레이션에 중요하지만, kind 4 이벤트 위에 새 기능을 쌓는다는 것은 대개 오래된 프라이버시 한계를 그대로 끌고 가는 뜻이기도 합니다.

---

**주요 출처:**
- [NIP-04 Specification](https://github.com/nostr-protocol/nips/blob/master/04.md)

**언급된 뉴스레터:**
- [Newsletter #4: NIP Deep Dive](/ko/newsletters/2026-01-07-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #19: nostter NIP-44 migration](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-44: 암호화된 페이로드](/ko/topics/nip-44/)
- [NIP-17: 비공개 다이렉트 메시지](/ko/topics/nip-17/)
- [NIP-59: Gift Wrap](/ko/topics/nip-59/)
