---
title: "NIP-44: Encrypted Payloads"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2025-12-31
draft: false
categories:
  - NIP
  - 암호학
  - 프라이버시
---

NIP-44는 Nostr 페이로드를 위한 버전 관리된 암호화 표준을 정의하며, 결함이 있는 NIP-04 암호화 체계를 현대적인 암호화 프리미티브로 대체합니다.

## 작동 방식

NIP-44 버전 2는 다단계 암호화 프로세스를 사용합니다:

1. **키 합의**: 송신자와 수신자 공개 키 간의 ECDH(secp256k1)가 공유 비밀을 생성
2. **키 도출**: SHA256과 솔트 `nip44-v2`를 사용한 HKDF-extract가 대화 키 생성
3. **메시지별 키**: HKDF-expand가 무작위 nonce에서 ChaCha 키, nonce, HMAC 키를 도출
4. **패딩**: 메시지 길이를 숨기기 위해 콘텐츠에 패딩 적용
5. **암호화**: ChaCha20이 패딩된 콘텐츠를 암호화
6. **인증**: HMAC-SHA256이 메시지 무결성 제공

## 암호화 선택

- **ChaCha20**(AES 대신): 더 빠르고 다중 키 공격에 대한 저항성이 우수
- **HMAC-SHA256**(Poly1305 대신): 다항식 MAC은 위조하기 더 쉬움
- **SHA256**: 기존 Nostr 프리미티브와 일관성
- **버전 관리 형식**: 향후 알고리즘 업그레이드 가능

## 보안 속성

- **인증된 암호화**: 메시지 변조 불가
- **길이 숨김**: 패딩이 메시지 크기를 불명확하게 함
- **대화 키**: 지속적인 대화에 동일한 키를 사용하여 계산 감소
- **감사 완료**: Cure53 보안 감사에서 악용 가능한 취약점 발견되지 않음

## 제한 사항

NIP-44는 다음을 제공하지 않습니다:
- **Forward Secrecy**: 손상된 키가 과거 메시지 노출
- **Post-Compromise Security**: 키 손상 후 복구
- **부인 가능성**: 메시지가 특정 키로 서명된 것으로 증명 가능
- **메타데이터 숨김**: 릴레이 아키텍처가 프라이버시 제한

고보안 요구사항에는 NIP-104(Double Ratchet) 또는 Marmot과 같은 MLS 기반 프로토콜이 더 강력한 보장을 제공합니다.

## 역사

NIP-44 리비전 3은 Cure53의 독립적인 보안 감사 후 2023년 12월에 병합되었습니다. NIP-17 프라이빗 DM과 NIP-59 gift wrapping의 암호화 기반을 형성합니다.

---

**주요 출처:**
- [NIP-44 사양](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44 참조 구현](https://github.com/paulmillr/nip44)
- [Cure53 감사 보고서](https://cure53.de/audit-report_nip44-implementations.pdf)

**언급:**
- [뉴스레터 #3: 2023년 12월](/ko/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [뉴스레터 #3: 2024년 12월](/ko/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)

**참고:**
- [NIP-04: 암호화 다이렉트 메시지 (지원 중단)](/ko/topics/nip-04/)
- [NIP-17: 프라이빗 다이렉트 메시지](/ko/topics/nip-17/)
- [NIP-59: 기프트 랩](/ko/topics/nip-59/)
- [NIP-104: 더블 래칫 암호화](/ko/topics/nip-104/)
- [MLS: 메시지 레이어 보안](/ko/topics/mls/)
