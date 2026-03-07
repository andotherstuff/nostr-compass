---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2026-03-07
draft: false
categories:
  - Cryptography
  - Protocol
  - Messaging
  - Privacy
---
MLS(Message Layer Security)는 종단 간 암호화 그룹 메시징을 위한 IETF 프로토콜이다. 시간이 지남에 따라 구성원이 변경될 수 있는 그룹에 전방 비밀성(forward secrecy)과 침해 후 보안(post-compromise security)을 제공한다.

## 작동 방식

MLS는 TreeKEM이라는 트리 기반 키 합의 구조를 사용한다:

1. **Key Package**: 각 참가자가 자신의 신원과 암호화 키를 포함한 key package를 게시한다
2. **그룹 상태**: ratchet tree가 그룹의 암호학적 상태를 유지한다
3. **커밋**: 구성원이 참여, 탈퇴, 키 교체 시 트리를 업데이트한다
4. **메시지 암호화**: 공유된 그룹 비밀에서 파생된 키로 콘텐츠를 암호화한다

## 왜 중요한가

MLS는 쌍대(pairwise) 암호화가 잘 해결하지 못하는 문제를 해결한다: 구성원이 비동기적으로 참여, 탈퇴, 키 교체를 할 때 그룹 구성원과 암호화 상태를 일관되게 유지하는 것이다.

트리 구조가 실용적 핵심이다. 업데이트가 모든 참가자에게 다른 모든 참가자와 쌍대로 재협상하도록 요구하지 않으므로, 임시방편적 그룹 키 방식보다 훨씬 더 잘 확장된다.

## 표준화

- **RFC 9420** (2023년 7월): 핵심 MLS 프로토콜 명세
- **RFC 9750** (2025년 4월): 시스템 통합을 위한 MLS 아키텍처

## Nostr에서의 채택

여러 Nostr 애플리케이션이 보안 그룹 메시징에 MLS를 사용한다:

- **KeyChat**: 모바일 및 데스크톱용 MLS 기반 암호화 메시징 앱
- **White Noise**: Marmot 프로토콜 통합을 통한 MLS 비공개 메시징
- **Marmot Protocol**: MLS 기반 그룹 암호화를 제공하는 Nostr 확장

MLS는 [NIP-04](/ko/topics/nip-04/)나 [NIP-44](/ko/topics/nip-44/) 단독보다 강력한 그룹 보안 보장을 제공하며, 구성원이 자주 변경될 때 특히 그렇다.

## 트레이드오프

MLS는 완전한 메시징 제품이 아니다. 애플리케이션은 프로토콜 주변에 신원, 전송, 스팸 방지, 저장, 충돌 처리를 여전히 필요로 한다.

이것이 Marmot 같은 Nostr 프로젝트가 MLS 위에 추가 규칙을 얹는 이유이다. 암호학은 표준화되어 있지만, 주변 애플리케이션 프로토콜이 상호운용성에 여전히 중요하다.

---

**주요 출처:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol 웹사이트](https://messaginglayersecurity.rocks/)

**언급된 뉴스레터:**
- [Newsletter #3: 릴리스](/en/newsletters/2025-12-31-newsletter/#releases)
- [Newsletter #10](/en/newsletters/2026-02-18-newsletter/)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**같이 보기:**
- [Marmot Protocol](/ko/topics/marmot/)
- [MIP-05: 프라이버시 보존 푸시 알림](/ko/topics/mip-05/)
- [NIP-17: 비공개 다이렉트 메시지](/ko/topics/nip-17/)
- [NIP-44: 암호화된 페이로드](/ko/topics/nip-44/)
