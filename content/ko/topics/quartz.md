---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2025-12-31
draft: false
categories:
  - 라이브러리
  - 개발
---

Quartz는 Vitor Pamplona가 개발한 Nostr용 Kotlin Multiplatform 라이브러리입니다. 원래 Amethyst Android 클라이언트에서 추출된 Quartz는 JVM, Android, iOS, Linux 플랫폼에서 재사용 가능한 Nostr 프로토콜 구현을 제공합니다.

## 작동 방식

Quartz는 공유 라이브러리로서 핵심 Nostr 기능을 제공합니다:

- **이벤트 처리**: Nostr 이벤트의 파싱, 검증 및 생성
- **암호화**: Secp256k1 서명, NIP-44 암호화, 키 관리
- **Relay 통신**: 연결 관리, 메시지 순서 지정, 구독 처리
- **NIP 지원**: NIP-06, NIP-19, NIP-44 등 일반적인 NIP 구현

## 주요 기능

- **Kotlin Multiplatform**: 단일 코드베이스로 여러 타겟에 컴파일
- **타겟 플랫폼**: Android, JVM, iOS (ARM64, 시뮬레이터), Linux
- **성능 최적화**: 효율적인 이벤트 처리 및 암호화 연산
- **Blossom 통합**: Blossom 프로토콜을 통한 미디어 업로드 지원
- **OpenTimestamp**: 타임스탬프 검증을 위한 완전한 Kotlin 포트

## 아키텍처

라이브러리는 모듈식 소스 세트 구조를 사용합니다:
- `commonMain`: 모든 플랫폼용 공유 코드
- `jvmAndroid`: JVM과 Android 간 공유 코드
- `androidMain`: Android 전용 구현
- `jvmMain`: 데스크톱 JVM 구현
- `iosMain`: iOS 전용 구현

## OpenSats 보조금

2025년 12월, OpenSats는 14차 Nostr 보조금의 일환으로 Quartz에 대한 자금 지원을 발표했습니다. 이 보조금은 이미 Android와 데스크톱 버전을 구동하는 것과 동일한 Kotlin Multiplatform 접근 방식을 통해 iOS에서 Amethyst를 구현하기 위한 지속적인 개발을 지원합니다.

---

**주요 출처:**
- [Maven Central의 Quartz](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Amethyst 저장소](https://github.com/vitorpamplona/amethyst)

**언급된 곳:**
- [Newsletter #3: 12월 요약](/ko/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: 뉴스](/ko/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Amethyst 주요 변경 사항](/ko/newsletters/2025-12-31-newsletter/#amethyst-android)

**함께 보기:**
- [Blossom 프로토콜](/ko/topics/blossom/)
