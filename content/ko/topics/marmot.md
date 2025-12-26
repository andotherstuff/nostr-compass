---
title: "Marmot 프로토콜"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot은 전방 비밀성과 사후 침해 보안을 위해 Message Layer Security(MLS) 표준을 사용하여 Nostr에 구축된 종단 간 암호화 그룹 메시징 프로토콜입니다.

## 작동 방식

Marmot은 그룹 채팅을 위한 MLS 기반 암호화로 Nostr를 확장합니다. 일대일인 NIP-17 DM과 달리 Marmot은 멤버가 가입하고 탈퇴해도 암호화 보장을 유지하면서 보안 그룹 통신을 처리합니다.

## 주요 기능

- MLS를 통한 전방 비밀성과 사후 침해 보안
- 동적 멤버십을 위한 그룹 키 관리
- MIP-05를 통한 프라이버시 보존 푸시 알림

---

**주요 출처:**
- [Marmot 프로토콜 저장소](https://github.com/marmot-protocol/marmot)

**언급된 곳:**
- [뉴스레터 #1: 뉴스](/ko/newsletters/2025-12-17-newsletter/#news)
- [뉴스레터 #1: 릴리스](/ko/newsletters/2025-12-17-newsletter/#releases)

**참고:**
- [MIP-05: 프라이버시 보존 푸시 알림](/ko/topics/mip-05/)
- [NIP-17: 비공개 다이렉트 메시지](/ko/topics/nip-17/)
- [NIP-59: Gift Wrap](/ko/topics/nip-59/)

