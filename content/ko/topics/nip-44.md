---
title: "NIP-44: 암호화된 페이로드"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - 암호화
  - 프라이버시
---
NIP-44는 Nostr 페이로드를 위한 버전 관리형 암호화 표준을 정의하며, 결함이 있는 NIP-04 암호화 방식을 현대적인 암호화 기본 요소로 대체한다.

## 작동 방식

NIP-44 버전 2는 다단계 암호화 프로세스를 사용한다:

1. **키 합의**: 송신자와 수신자의 공개 키 간 ECDH(secp256k1)를 통해 공유 비밀을 생성한다
2. **키 도출**: SHA256과 솔트 `nip44-v2`를 사용한 HKDF-extract로 대화 키를 생성한다
3. **메시지별 키**: HKDF-expand가 랜덤 논스로부터 ChaCha 키, 논스, HMAC 키를 도출한다
4. **패딩**: 메시지 길이를 숨기기 위해 콘텐츠를 패딩한다
5. **암호화**: ChaCha20으로 패딩된 콘텐츠를 암호화한다
6. **인증**: HMAC-SHA256이 메시지 무결성을 보장한다

출력은 일반 서명된 Nostr 이벤트 내부에 들어가는 버전 관리형 base64 페이로드이다. 사양에 따르면 클라이언트는 내부 NIP-44 페이로드를 복호화하기 전에 외부 NIP-01 이벤트 서명을 검증해야 한다.

## 암호화 선택

- **ChaCha20**(AES 대신): 더 빠르고, 다중 키 공격에 대한 저항성이 우수
- **HMAC-SHA256**(Poly1305 대신): 다항식 MAC은 위조가 더 쉬움
- **SHA256**: 기존 Nostr 기본 요소와 일관성 유지
- **버전 관리 형식**: 향후 알고리즘 업그레이드 가능

## 보안 속성

- **인증된 암호화**: 메시지 변조가 불가능
- **길이 은닉**: 패딩으로 메시지 크기를 은폐
- **대화 키**: 진행 중인 대화에 동일한 키를 사용하여 연산량 감소
- **감사 완료**: Cure53 보안 감사에서 악용 가능한 취약점 없음 확인

## 구현 참고사항

NIP-44는 NIP-04 페이로드의 직접 대체가 아니다. 암호화 형식을 정의할 뿐, 다이렉트 메시지 이벤트 kind를 정의하지 않는다. [NIP-17](/ko/topics/nip-17/)과 [NIP-59](/ko/topics/nip-59/) 같은 프로토콜이 실제 메시지 흐름에서 암호화된 페이로드의 사용 방식을 정의한다.

평문 입력은 1~65535 바이트 길이의 UTF-8 텍스트이다. 이것은 구현자에게 실질적인 제약이다: 임의의 바이너리 블롭을 암호화해야 하는 경우 추가 인코딩이나 다른 컨테이너 형식이 필요하다.

## 한계

NIP-44는 다음을 제공하지 않는다:
- **전방 비밀성**: 키가 유출되면 과거 메시지가 노출됨
- **사후 침해 보안**: 키 침해 후 복구 불가
- **부인 가능성**: 메시지가 특정 키에 의해 서명되었음을 증명할 수 있음
- **메타데이터 은닉**: 릴레이 아키텍처가 프라이버시를 제한

높은 보안이 필요한 경우, NIP-104(더블 래칫)나 Marmot 같은 MLS 기반 프로토콜이 더 강력한 보장을 제공한다.

## 역사

NIP-44 리비전 3은 독립적인 Cure53 보안 감사를 거쳐 2023년 12월에 병합되었다. NIP-17 비공개 DM과 NIP-59 gift wrapping의 암호화 기반을 형성한다.

---

**주요 출처:**
- [NIP-44 사양](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44 참조 구현](https://github.com/paulmillr/nip44)
- [Cure53 감사 보고서](https://cure53.de/audit-report_nip44-implementations.pdf)

**언급된 뉴스레터:**
- [Newsletter #4: NIP 심층 분석](/en/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Newsletter #3: 2023년 12월](/en/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [Newsletter #3: 2024년 12월](/en/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)
- [Newsletter #12: Marmot](/en/newsletters/2026-03-04-newsletter/#marmot-development-kit-ships-first-public-release)

**같이 보기:**
- [NIP-04: 암호화된 다이렉트 메시지 (폐기됨)](/ko/topics/nip-04/)
- [NIP-17: 비공개 다이렉트 메시지](/ko/topics/nip-17/)
- [NIP-59: Gift Wrap](/ko/topics/nip-59/)
- [NIP-104: 더블 래칫 암호화](/ko/topics/nip-104/)
- [MLS: Message Layer Security](/ko/topics/mls/)
