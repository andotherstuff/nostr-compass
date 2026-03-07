---
title: "NIP-A4: 공개 메시지"
date: 2025-12-24
translationOf: /en/topics/nip-a4.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---
NIP-A4는 알림 화면용으로 설계된 공개 메시지(kind 24)를 정의하며, 폭넓은 클라이언트 지원을 목표로 한다.

## 작동 방식

Kind `24`는 한 명 이상의 수신자에게 보내는 서명된 평문 메시지다. 메시지 본문은 `content`에 들어가고, `p` 태그가 수신 대상을 식별한다. 스펙에 따르면 클라이언트는 이 이벤트를 수신자의 [NIP-65](/ko/topics/nip-65/) inbox 릴레이와 발신자의 outbox 릴레이에 전송해야 한다.

스레드 대화와 달리, 이 메시지에는 채팅 이력, 방 상태, 스레드 루트 개념이 없다. 알림 화면에 표시되어 단독으로 이해될 수 있도록 설계되었다.

## 프로토콜 규칙

- `p` 태그로 수신자를 식별
- 스레딩을 위한 `e` 태그 사용 금지
- 다른 이벤트를 인용하기 위해 `q` 태그 사용 가능
- [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md) 만료 태그와 함께 사용하면 오래된 알림성 메시지가 시간이 지나면 사라짐

## 왜 존재하는가

NIP-A4는 클라이언트에게 완전한 스레드 노트보다 단순한 공개 메시지 프리미티브를 제공한다. 멘션 스타일 메시지, 간단한 shoutout, 영구 대화 트리를 구축하는 것이 과도한 일회성 알림에 유용하다.

트레이드오프는 이 메시지가 공개라는 점이다. 비공개 세션 상태를 생성하지 않기 때문에 알림 UI에 표시하기 쉽다. 누구나 메시지를 보면 읽고 답장할 수 있다.

## 상호운용성 참고사항

NIP-A4는 지정된 수신자를 대상으로 하기 때문에 DM 프로토콜과 혼동하기 쉽지만, 여전히 공개 이벤트 kind이다. 클라이언트는 kind `24`를 비공개 메시지로 표시하거나 릴레이 배치 이상의 기밀성을 가정해서는 안 된다.

---

**주요 출처:**
- [NIP-A4 명세](https://github.com/nostr-protocol/nips/blob/master/A4.md)
- [NIP-A4 PR](https://github.com/nostr-protocol/nips/pull/1988)

**언급된 뉴스레터:**
- [Newsletter #2: NIP 업데이트](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3: 12월 회고](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**같이 보기:**
- [NIP-01: 기본 프로토콜](/ko/topics/nip-01/)
- [NIP-10: 텍스트 노트 스레딩](/ko/topics/nip-10/)
