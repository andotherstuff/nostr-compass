---
title: "NIP-28: 공개 채팅"
date: 2026-09-30
translationOf: /en/topics/nip-28.md
translationDate: 2026-10-02
draft: false
categories:
  - NIPs
  - Social
---

NIP-28은 공개 채팅 채널, 채널 메시지, 클라이언트 측 모더레이션을 Nostr event로 설명한다. 현재 명세는 **draft**이자 **unrecommended**로 표시되어 있으며, 구현자에게 현재의 relay 기반 그룹에는 NIP-29를 사용하도록 안내한다.

## event 모델 {#event-model}

kind `40`은 채널을 생성하고, kind `41`은 채널 메타데이터를 갱신하며, kind `42`는 메시지를 담는다. kind `43`과 `44`는 사용자가 자신의 클라이언트에서 메시지를 숨기거나 다른 사용자를 음소거할 수 있게 한다. 메시지 tag는 채널 생성 event를 참조하며, 답장 대상 메시지를 식별할 수 있다. relay는 이러한 클라이언트 측 숨김 및 음소거 선택을 강제할 필요가 없다.

[2022년 9월 명세 변경](https://github.com/nostr-protocol/nips/commit/3423a6dfb)은 공개 채팅방을 공유된 프로토콜 주제로 만들었다. [현재 명세](https://github.com/nostr-protocol/nips/blob/master/28.md)가 새 구현체에 다른 경로를 권장하더라도, 이 역사적 역할은 여전히 이해해 둘 가치가 있다.

---

**주요 출처:**
- [NIP-28 명세와 현재 상태](https://github.com/nostr-protocol/nips/blob/master/28.md)
- [2022년 9월 공개 채팅 변경](https://github.com/nostr-protocol/nips/commit/3423a6dfb)

**언급된 뉴스레터:**
- [Newsletter #42: 2022년 9월](/ko/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)

**같이 보기:**
- [NIP-29: relay 기반 그룹](/ko/topics/nip-29/)
