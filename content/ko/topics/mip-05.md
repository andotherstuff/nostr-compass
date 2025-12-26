---
title: "MIP-05: 프라이버시 보존 푸시 알림"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05는 사용자 프라이버시를 유지하는 푸시 알림 프로토콜을 정의하여, 기존 푸시 시스템이 서버가 기기 토큰과 사용자 신원을 알아야 하는 문제를 해결합니다.

## 작동 방식

- 기기 토큰은 ECDH+HKDF와 ChaCha20-Poly1305로 암호화됨
- 임시 키가 알림 간 상관관계 방지
- 세 가지 이벤트 가십 프로토콜(kind 447-449)이 그룹 멤버 간에 암호화된 토큰 동기화
- NIP-59 gift wrapping을 통한 디코이 토큰이 그룹 크기 숨김

## 프라이버시 보장

- 푸시 알림 서버가 사용자를 식별할 수 없음
- 알림 패턴으로 그룹 멤버십이 드러나지 않음
- 기기 토큰이 메시지 간에 상관될 수 없음

## 이벤트 Kind

- **Kind 447**: 암호화된 기기 토큰 게시
- **Kind 448**: 토큰 동기화 요청
- **Kind 449**: 토큰 동기화 응답

---

**주요 출처:**
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)

**언급된 곳:**
- [뉴스레터 #1: 뉴스](/ko/newsletters/2025-12-17-newsletter/#news)

**참고:**
- [Marmot 프로토콜](/ko/topics/marmot/)
- [NIP-59: Gift Wrap](/ko/topics/nip-59/)

