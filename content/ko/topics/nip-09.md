---
title: "NIP-09"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-02-25
draft: false
categories: ["NIP 명세", "프로토콜"]
---

NIP-09는 Event 삭제를 정의합니다. 사용자가 이전에 게시한 event를 relay에서 제거하도록 요청하는 메커니즘입니다.

## 동작 방식

사용자는 삭제하려는 event ID를 참조하는 `e` 태그가 포함된 kind 5 event를 게시합니다. NIP-09를 지원하는 relay는 참조된 event 제공을 중단하고 저장소에서 삭제할 수 있습니다.

삭제는 요청이지 보장이 아닙니다. Relay가 삭제 요청을 무시할 수 있으며, event가 이미 삭제를 지원하지 않는 relay로 전파되었을 수도 있습니다. 개인정보 보호가 필요한 콘텐츠 제거에 NIP-09를 신뢰해서는 안 됩니다.

## 주요 특징

NIP-09는 kind 5 삭제 요청 event를 사용하며, `e` 태그로 삭제할 event ID를 참조합니다. 선택적 사유 필드로 삭제 맥락을 제공할 수 있습니다. Relay의 준수는 자발적입니다.

---

**주요 출처:** [NIP-09 명세](https://github.com/nostr-protocol/nips/blob/master/09.md)

**언급된 곳:** [뉴스레터 #11: NIP-60 심층 분석](/ko/newsletters/2026-02-25-newsletter/#nip-심층-분석-nip-60-cashu-지갑)

**참조:** [NIP-60: Cashu 지갑](/ko/topics/nip-60/)
