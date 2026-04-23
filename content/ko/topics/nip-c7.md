---
title: "NIP-C7: 채팅 메시지"
date: 2026-04-15
translationOf: /en/topics/nip-c7.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Messaging
---

NIP-C7은 kind `9`를 채팅 메시지를 위한 이벤트 kind로 정의합니다. 목적은 채팅 중심 트래픽을 일반 소셜 피드 트래픽과 분리해, 클라이언트가 각 맥락에 서로 다른 UX와 moderation 규칙을 적용할 수 있게 하는 데 있습니다.

## 작동 방식

kind `9` 이벤트는 메시지 콘텐츠와 함께 채팅 맥락을 식별하는 태그를 담습니다. [NIP-29](/ko/topics/nip-29/) 릴레이 기반 그룹에서는 그룹 ID를 담은 `h` 태그가 포함됩니다. 답글 스레딩은 이전 이벤트를 참조하는 `q` 태그를 사용합니다.

NIP-C7의 초점은 이 이벤트를 어디에 렌더링해야 하는가에 있습니다. kind `1` 텍스트 노트처럼 전역 노트 피드에 나타나는 대신, kind `9` 이벤트는 대화 상태와 스레딩이 명시적인 채팅 전용 뷰를 위한 것입니다.

## 구현체

- [Flotilla](https://gitea.coracle.social/coracle/flotilla)와 [Coracle](https://github.com/coracle-social/coracle)은 그룹 채팅 워크플로에서 kind `9`를 사용합니다.
- [Amethyst](https://github.com/vitorpamplona/amethyst)는 메시징 스택에 kind `9` 지원을 포함합니다.
- [White Noise](https://github.com/marmot-protocol/whitenoise)는 `q` 태그를 사용하는 NIP-C7 답글 스레딩을 사용합니다.

---

**주요 출처:**
- [NIP-C7 명세](https://github.com/nostr-protocol/nips/blob/master/C7.md)
- [PR #2310: Restrict kind 9 to chat views](https://github.com/nostr-protocol/nips/pull/2310)

**언급된 뉴스레터:**
- [Newsletter #18: NIP Updates](/en/newsletters/2026-04-15-newsletter/)

**같이 보기:**
- [NIP-29: 릴레이 기반 그룹](/ko/topics/nip-29/)
- [NIP-17: 비공개 DM](/ko/topics/nip-17/)
