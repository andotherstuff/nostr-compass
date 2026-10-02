---
title: "NIP-FE 제안: HTTP relay 명령"
date: 2026-09-30
translationOf: /en/topics/nip-fe.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Relays
---

Amethyst는 Geode relay와 Quartz 클라이언트 작업에서 HTTP를 통한 relay 명령에 NIP-FE라는 임시 명칭을 사용한다. 이 명칭은 할당된 NIP가 아니며, Nostr relay 전반에서 채택되었다는 증거도 아니다.

## 전송 방식 {#transport}

클라이언트는 WebSocket 연결을 여는 대신 `REQ`, `COUNT`, 또는 `EVENT` 프레임 하나를 relay HTTP 엔드포인트에 전송한다. 응답은 relay 프레임을 줄바꿈으로 구분된 JSON으로 스트리밍한다. 클라이언트는 완료된 응답과 중간에 끊긴 스트림을 구별해야 하며, 인증된 요청은 여전히 서명된 Nostr HTTP 인증을 사용한다. 이 전송 방식은 명령이 relay에 도달하는 방법을 바꿀 뿐, 기반이 되는 event 서명이나 event 내용은 바꾸지 않는다.

Amethyst의 [병합된 구현](https://github.com/vitorpamplona/amethyst/pull/4231)은 Geode 경로, Quartz 클라이언트 지원, 본문 및 동시성 제한, 프레이밍과 인증 테스트를 추가한다. 이는 소스 수준의 구현 증거이며, 독립적인 relay들이 같은 제안을 구현했다는 증거는 아니다.

## 명칭 충돌 {#naming-collision}

관련 없는 [NIPs 저장소의 초안 풀 리퀘스트](https://github.com/nostr-protocol/nips/pull/2488)도 **NIP-FE**라는 명칭을 사용하는데, 이 경우에는 제안된 다중 수신자 봉투 위에 구축되는 비공개 피드를 가리킨다. 그 작업은 열려 있으며 Amethyst의 HTTP 전송과는 다른 문제를 다룬다. 어느 쪽의 임시 사용도 이 명칭이 채택된 명세에 할당되었다는 것을 입증하지 않으므로, 독자는 출처와 주제로 제안을 식별해야 한다.

---

**주요 출처:**
- [Amethyst Geode 및 Quartz 구현 PR](https://github.com/vitorpamplona/amethyst/pull/4231)
- [Amethyst 저장소](https://github.com/vitorpamplona/amethyst)
- [NIP-FE를 함께 사용하는 열린 비공개 피드 초안](https://github.com/nostr-protocol/nips/pull/2488)

**언급된 뉴스레터:**
- [Newsletter #42: Amethyst relay 명령](/ko/newsletters/2026-09-30-newsletter/#amethyst-repairs-encrypted-group-interoperability)
