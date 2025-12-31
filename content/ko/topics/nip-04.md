---
title: "NIP-04: 암호화된 다이렉트 메시지 (지원 중단)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2025-12-31
draft: false
categories:
  - 프라이버시
  - 메시징
---

NIP-04는 AES-256-CBC 암호화를 사용한 암호화된 다이렉트 메시지를 정의합니다. Nostr에서 프라이빗 메시징의 원래 방법이었지만 심각한 프라이버시 제한으로 인해 NIP-17로 대체되어 지원 중단되었습니다.

## 작동 방식

메시지는 다음 암호화 체계로 kind 4 이벤트를 사용합니다:
1. 수신자의 공개 키와 발신자의 개인 키를 사용한 ECDH로 공유 비밀 생성
2. 메시지를 AES-256-CBC로 암호화
3. 암호문을 초기화 벡터와 함께 base64로 인코딩
4. `p` 태그로 수신자의 공개 키 식별

## 보안 제한 사항

NIP-04는 심각한 프라이버시 결함이 있습니다:

- **메타데이터 유출** - 발신자의 pubkey가 모든 메시지에서 공개적으로 표시됨
- **발신자 프라이버시 없음** - 누가 누구에게 메시지를 보내는지 누구나 볼 수 있음
- **정확한 타임스탬프** - 메시지 타이밍이 무작위화되지 않음
- **비표준 구현** - 표준 SHA256 해시 대신 ECDH 포인트의 X 좌표만 사용

사양서는 "암호화된 통신의 최첨단 기술에 근접하지도 않는다"고 명시적으로 경고합니다.

## 지원 중단 상태

NIP-04는 NIP-17로 대체되어 지원 중단되었습니다. NIP-17은 NIP-59 gift wrapping을 사용하여 발신자의 신원을 숨깁니다. 새로운 구현에서는 프라이빗 메시징에 NIP-17을 사용해야 합니다.

---

**주요 출처:**
- [NIP-04 사양](https://github.com/nostr-protocol/nips/blob/master/04.md)

**언급된 곳:**
- [Newsletter #3: 12월 회고](/ko/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**참고 항목:**
- [NIP-17: 프라이빗 다이렉트 메시지](/ko/topics/nip-17/)
- [NIP-59: Gift Wrap](/ko/topics/nip-59/)
