---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2025-12-31
draft: false
categories:
  - 암호학
  - 프로토콜
  - 메시징
  - 프라이버시
---

Message Layer Security (MLS)는 종단간 암호화 그룹 메시징을 위한 IETF 표준 프로토콜입니다. 2명부터 수천 명의 참가자로 구성된 그룹에 대해 순방향 비밀성과 침해 후 보안을 갖춘 효율적인 키 설정을 제공합니다.

## 작동 방식

MLS는 TreeKEM이라는 트리 기반 키 합의 구조를 사용합니다:

1. **키 패키지**: 각 참가자가 자신의 신원과 암호화 키가 포함된 키 패키지를 게시
2. **그룹 상태**: 래칫 트리가 그룹의 암호화 상태를 유지
3. **커밋**: 멤버가 참여, 탈퇴 또는 키 교체 시 트리를 업데이트
4. **메시지 암호화**: 콘텐츠는 그룹 공유 비밀에서 파생된 키로 암호화

## 주요 보안 특성

- **순방향 비밀성**: 현재 키가 손상되어도 과거 메시지는 안전하게 유지
- **침해 후 보안**: 키 교체 후 미래 메시지가 다시 안전해짐
- **멤버십 인증**: 모든 그룹 멤버가 암호학적으로 검증됨
- **비동기 운영**: 모든 참가자가 온라인이 아니어도 멤버가 참여/탈퇴 가능
- **확장성**: 최대 50,000명의 참가자 그룹에 효율적

## 표준화

- **RFC 9420** (2023년 7월): 핵심 MLS 프로토콜 사양
- **RFC 9750** (2025년 4월): 시스템 통합을 위한 MLS 아키텍처

## Nostr에서의 채택

여러 Nostr 애플리케이션이 보안 그룹 메시징에 MLS를 사용합니다:

- **KeyChat**: 모바일 및 데스크톱용 MLS 기반 암호화 메시징 앱
- **White Noise**: Marmot 프로토콜 통합과 함께 MLS를 사용한 프라이빗 메시징
- **Marmot Protocol**: MLS 기반 그룹 암호화를 제공하는 Nostr 확장

MLS는 멤버가 동적으로 참여하고 탈퇴하는 그룹 채팅에서 NIP-04나 NIP-44 단독보다 더 강력한 보안 보장을 제공합니다.

## 산업 채택

Nostr 외에도 MLS는 다음에서 채택되고 있습니다:
- Google Messages (GSMA Universal Profile 3.0을 통한 MLS가 포함된 RCS)
- Apple Messages (MLS용 RCS 지원 발표)
- Cisco WebEx, Wickr, Matrix

---

**주요 출처:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**언급된 곳:**
- [Newsletter #3: 릴리스](/ko/newsletters/2025-12-31-newsletter/#releases)

**참고 항목:**
- [Marmot Protocol](/ko/topics/marmot/)
- [MIP-05: 프라이버시 보호 푸시 알림](/ko/topics/mip-05/)
- [NIP-17: 프라이빗 다이렉트 메시지](/ko/topics/nip-17/)
- [NIP-44: 암호화된 페이로드](/ko/topics/nip-44/)
