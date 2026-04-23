---
title: "NIP-44: 암호화된 페이로드"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - Cryptography
  - Privacy
---

NIP-44는 Nostr payload를 위한 버전 관리형 암호화 표준을 정의하며, 결함이 있던 NIP-04 암호화 방식을 현대적인 암호학 primitive로 대체합니다.

## 작동 방식

NIP-44 version 2는 다단계 암호화 과정을 사용합니다:

1. **키 합의**: 발신자와 수신자 공개키 사이의 ECDH (secp256k1)가 공유 비밀을 생성
2. **키 도출**: SHA256과 salt `nip44-v2`를 사용하는 HKDF-extract가 대화 키를 생성
3. **메시지별 키**: HKDF-expand가 무작위 nonce에서 ChaCha 키, nonce, HMAC 키를 도출
4. **패딩**: 메시지 길이를 숨기기 위해 내용을 패딩함
5. **암호화**: ChaCha20이 패딩된 내용을 암호화
6. **인증**: HMAC-SHA256이 메시지 무결성을 제공

출력은 일반 서명된 Nostr 이벤트 안에 들어가는 버전 관리형 base64 payload입니다. 명세는 클라이언트가 안쪽 NIP-44 payload를 복호화하기 전에 바깥 NIP-01 이벤트 서명을 검증해야 한다고 요구합니다.

## 암호학적 선택

- **AES 대신 ChaCha20**: 더 빠르고 다중 키 공격 저항성이 더 좋음
- **Poly1305 대신 HMAC-SHA256**: 다항식 MAC은 위조가 더 쉬움
- **SHA256**: 기존 Nostr primitive와 일관됨
- **버전 관리 형식**: 향후 알고리즘 업그레이드 가능

## 보안 속성

- **인증된 암호화**: 메시지를 변조할 수 없음
- **길이 은닉**: 패딩이 메시지 크기를 가림
- **대화 키**: 이어지는 대화에서 같은 키를 써 계산량을 줄임
- **감사 완료**: Cure53 보안 감사에서 악용 가능한 취약점을 찾지 못함

## 구현 참고사항

NIP-44는 NIP-04 payload의 drop-in replacement가 아닙니다. 이것은 암호화 형식을 정의할 뿐, direct-message 이벤트 kind 자체를 정의하지는 않습니다. 실제 메시지 흐름에서 이 암호화 payload를 어떻게 사용하는지는 [NIP-17](/ko/topics/nip-17/)과 [NIP-59](/ko/topics/nip-59/) 같은 프로토콜이 정의합니다.

평문 입력은 길이가 1바이트에서 65535바이트인 UTF-8 텍스트입니다. 이것은 구현자에게 실제 제약입니다. 애플리케이션이 임의의 binary blob을 암호화해야 한다면, 추가 인코딩이나 다른 container 형식이 필요합니다.

## 한계

NIP-44는 다음을 제공하지 않습니다:
- **전방 비밀성**: 키가 유출되면 과거 메시지도 노출됨
- **사후 침해 보안**: 키 유출 뒤 회복 불가
- **부인 가능성**: 메시지가 특정 키로 서명되었다는 사실을 증명 가능함
- **메타데이터 은닉**: 릴레이 아키텍처가 프라이버시를 제한함

더 강한 보장이 필요한 경우 NIP-104 (double ratchet)이나 Marmot 같은 MLS 기반 프로토콜이 더 적합합니다.

## 역사

NIP-44 revision 3은 독립적인 Cure53 보안 감사를 거친 뒤 2023년 12월에 병합되었습니다. 이는 NIP-17 비공개 DM과 NIP-59 gift wrapping의 암호학적 기반을 이룹니다.

---

**주요 출처:**
- [NIP-44 Specification](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44 Reference Implementations](https://github.com/paulmillr/nip44)
- [Cure53 Audit Report](https://cure53.de/audit-report_nip44-implementations.pdf)

**언급된 뉴스레터:**
- [Newsletter #4: NIP Deep Dive](/ko/newsletters/2026-01-07-newsletter/)
- [Newsletter #3: December 2023](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #3: December 2024](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #12: Marmot](/ko/newsletters/2026-03-04-newsletter/)
- [Newsletter #13: Vector](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: nostter NIP-44 migration](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: nowhere encrypts Nostr traffic](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-04: 암호화된 다이렉트 메시지 (지원 중단)](/ko/topics/nip-04/)
- [NIP-17: 비공개 다이렉트 메시지](/ko/topics/nip-17/)
- [NIP-59: Gift Wrap](/ko/topics/nip-59/)
- [NIP-104: Double Ratchet Encryption](/ko/topics/nip-104/)
- [MLS: Message Layer Security](/ko/topics/mls/)
