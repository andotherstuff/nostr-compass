---
title: "NIP-A4: 공개 메시지"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-A4는 광범위한 클라이언트 지원을 목표로 알림 화면용으로 설계된 공개 메시지(kind 24)를 정의합니다.

## 작동 방식

스레드 대화와 달리 이 메시지에는 채팅 기록이나 메시지 체인 개념이 없습니다. 수신자의 알림 피드에 나타나도록 의도된 간단한 일회성 메시지입니다.

## 구조

- 스레딩 복잡성을 피하기 위해 `e` 태그 대신 `q` 태그(인용) 사용
- 대화 상태나 기록 없음
- 간단한 공개 알림용으로 설계

## 사용 사례

- 공개 감사 또는 외침
- 사용자에게 브로드캐스트 메시지
- 답글 스레딩이 필요 없는 알림

---

**주요 출처:**
- [NIP-A4 PR](https://github.com/nostr-protocol/nips/pull/1988)

**언급된 곳:**
- [뉴스레터 #2: NIP 업데이트](/ko/newsletters/2025-12-24-newsletter/#nip-updates)

**참고:**
- [NIP-01: 기본 프로토콜](/ko/topics/nip-01/)
- [NIP-10: 텍스트 노트 스레딩](/ko/topics/nip-10/)

