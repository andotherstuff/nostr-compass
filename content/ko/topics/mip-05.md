---
title: "MIP-05: 프라이버시 보존 푸시 알림"
date: 2025-12-17
translationOf: /en/topics/mip-05.md
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---
MIP-05는 일반적인 모바일 푸시 시스템이 디바이스 토큰과 계정 관계를 노출하는 환경에서, 프라이버시를 보존하려는 Marmot 클라이언트용 푸시 알림 프로토콜을 정의한다.

## 작동 방식

- 디바이스 토큰은 ECDH+HKDF와 ChaCha20-Poly1305로 암호화된다
- 임시 키(ephemeral key)가 알림 간 상관관계를 방지한다
- 세 가지 이벤트 가십 프로토콜(kind 447-449)이 그룹 구성원 간 암호화된 토큰을 동기화한다
- NIP-59 gift wrapping을 통한 디코이 토큰이 그룹 크기를 감춘다

## 프라이버시 모델

- 푸시 알림 서버가 사용자를 식별할 수 없다
- 알림 패턴으로 그룹 구성원이 드러나지 않는다
- 메시지 간 디바이스 토큰을 상관시킬 수 없다

구체적인 개선점은 푸시 제공자가 그룹 구성원에서 디바이스로의 직접 매핑이 아니라 불투명한 전달 토큰을 본다는 것이다. 이것이 알림을 절대적 의미에서 익명으로 만드는 것은 아니지만, 푸시 계층이 기본적으로 학습하는 정보량을 줄인다.

## 이벤트 종류

- **Kind 447**: 암호화된 디바이스 토큰 게시
- **Kind 448**: 토큰 동기화 요청
- **Kind 449**: 토큰 동기화 응답

## 트레이드오프

MIP-05는 조정 작업을 추가하여 프라이버시를 확보한다. 클라이언트는 그룹 구성원 간 암호화된 토큰 상태를 동기화해야 하며, 디코이 토큰은 의도적으로 메시지 오버헤드를 증가시킨다.

이는 구현자가 전달 신뢰성과 메타데이터 보호 사이에서 균형을 맞춰야 함을 의미한다. 이 프로토콜이 유용한 이유는 푸시를 단순한 전송 편의가 아니라 프라이버시 문제로 취급하기 때문이다.

---

**주요 출처:**
- [MIP-05 명세](https://github.com/marmot-protocol/marmot/blob/master/05.md)
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)
- [White Noise v0.2.1 릴리스](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**언급된 뉴스레터:**
- [Newsletter #1: 소식](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: 12월 회고](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**같이 보기:**
- [Marmot Protocol](/ko/topics/marmot/)
- [NIP-59: Gift Wrap](/ko/topics/nip-59/)
