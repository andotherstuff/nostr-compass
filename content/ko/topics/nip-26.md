---
title: "NIP-26: 위임된 event 서명"
date: 2026-09-30
translationOf: /en/topics/nip-26.md
translationDate: 2026-10-02
draft: false
categories:
  - NIPs
  - Identity
---

NIP-26은 하나의 Nostr 키가 다른 키에게 제한된 범위의 event에 서명하도록 권한을 부여하는 방법을 문서화한다. 현재 명세는 **draft**이자 **unrecommended**로 표시되어 있으므로, 새로운 통합을 위한 권고가 아니라 이전 설계의 기록이다.

## 작동 방식 {#how-it-works}

계정 키는 위임받는 키와 조건을 명시한 위임 토큰에 서명한다. 조건은 event kind와 `created_at` 시각을 제한할 수 있다. 위임받은 키는 자신의 키로 event에 서명하고 `delegation` tag에 토큰을 첨부한다. 읽는 쪽은 event 서명과 위임 토큰을 모두 해당 조건에 대조해 검증해야 한다. 이 방식을 지원하는 relay는 위임자 기준으로 검색할 수도 있다.

이 모델은 애플리케이션이 계정의 주 서명 키를 보유하지 않고도 게시할 수 있게 한다. 추가 검증과 relay 검색 요구 사항은 구현체가 일반 event 서명을 위임된 신원의 충분한 증명으로 취급할 수 없는 이유를 설명한다. [현재 명세](https://github.com/nostr-protocol/nips/blob/master/26.md)는 이 접근 방식을 명시적으로 unrecommended로 표시한다.

---

**주요 출처:**
- [NIP-26 명세와 현재 상태](https://github.com/nostr-protocol/nips/blob/master/26.md)
- [2022년 9월 위임 서명 문서](https://github.com/nostr-protocol/nips/commit/b62aa418d)

**언급된 뉴스레터:**
- [Newsletter #42: 2022년 9월](/ko/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)
