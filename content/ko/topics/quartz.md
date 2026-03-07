---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2026-03-07
draft: false
categories:
  - Library
  - Development
---
Quartz는 Vitor Pamplona가 개발한 Kotlin Multiplatform Nostr 라이브러리다. Amethyst가 하나의 코드베이스에서 Android, 데스크톱, 그리고 궁극적으로 iOS까지 지원하기 위한 공유 프로토콜 및 데이터 계층이다.

## 작동 방식

Quartz는 공유 라이브러리로서 핵심 Nostr 기능을 제공한다:

- **이벤트 처리**: Nostr 이벤트의 파싱, 검증, 생성
- **암호화**: Secp256k1 서명, NIP-44 암호화, 키 관리
- **릴레이 통신**: 연결 관리, 메시지 순서, 구독 처리
- **NIP 지원**: NIP-06, NIP-19, NIP-44 등 주요 NIP 구현

## 왜 중요한가

Quartz는 프로토콜 집약적 로직을 단일 앱에서 재사용 가능한 라이브러리로 분리한다. 릴레이 처리, 이벤트 파싱, 암호화, 저장 규칙을 플랫폼별로 재구현하지 않고 클라이언트 간에 공유할 수 있게 되므로 의미가 크다.

구체적인 결과는 이미 Amethyst의 데스크톱 작업에서 나타났다. 그랜트 지원 리팩터링이 공유 코드를 `commonMain`, `jvmAndroid`, `jvmMain` 같은 Kotlin Multiplatform 모듈로 옮기면서, 데스크톱 지원이 전체 재작성이 아닌 라이브러리 및 모듈 문제가 되었다.

## 아키텍처

라이브러리는 모듈형 source set 구조를 사용한다:
- `commonMain`: 모든 플랫폼 공유 코드
- `jvmAndroid`: JVM과 Android 간 공유 코드
- `androidMain`: Android 전용 구현
- `jvmMain`: 데스크톱 JVM 구현
- `iosMain`: iOS 전용 구현

## 현재 상태

2025년 12월, OpenSats는 14차 Nostr 그랜트에서 Quartz에 대한 자금 지원을 발표했다. 레포지토리는 독립 라이브러리로 존재하지만, 지금까지 눈에 보이는 진전은 대부분 앱 모듈을 멀티플랫폼 코드로 전환하고 타겟 간 기능 동등성을 추적하는 Amethyst PR을 통해 이루어졌다.

---

**주요 출처:**
- [Quartz 저장소](https://github.com/vitorpamplona/quartz)
- [Quartz on Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Amethyst 저장소](https://github.com/vitorpamplona/amethyst)
- [OpenSats 14차 Nostr 그랜트](https://opensats.org/blog/fourteenth-wave-of-nostr-grants)

**언급된 뉴스레터:**
- [Newsletter #3: 12월 회고](/en/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: 뉴스](/en/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Amethyst 주요 변경사항](/en/newsletters/2025-12-31-newsletter/#amethyst-android)

**같이 보기:**
- [Blossom 프로토콜](/ko/topics/blossom/)
