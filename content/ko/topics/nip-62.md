---
title: "NIP-62: Vanish Requests"
date: 2026-01-13
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62는 사용자가 relay에 콘텐츠 삭제를 요청할 수 있는 메커니즘인 vanish request를 정의합니다. relay가 이러한 요청을 반드시 이행할 의무는 없지만, NIP-62를 지원하면 사용자에게 게시된 데이터에 대한 더 많은 제어권을 제공하고 네트워크 전반에 삭제 의도를 신호하는 표준화된 방법을 제공합니다.

## 작동 방식

vanish request는 콘텐츠 제거를 원하는 사용자가 서명한 kind 62 event입니다. 요청은 `e` 태그에 ID를 포함하여 특정 event를 대상으로 하거나, `e` 태그를 완전히 생략하여 해당 pubkey의 모든 콘텐츠 삭제를 요청할 수 있습니다.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 62,
  "tags": [
    ["e", "event1234...", "wss://relay.example.com"],
    ["e", "event5678...", "wss://relay.example.com"]
  ],
  "content": "Removing old posts",
  "sig": "sig1234..."
}
```

`content` 필드는 선택적으로 삭제 요청에 대한 사람이 읽을 수 있는 이유를 포함합니다. `e` 태그의 relay 힌트는 원본 event가 게시된 위치를 relay에 알려주지만, relay는 지정된 event가 있는지 여부와 관계없이 요청을 이행할 수 있습니다.

## Relay 동작

NIP-62를 지원하는 relay는 지정된 event를 저장소에서 삭제하고 구독자에게 제공하는 것을 중지해야 합니다. vanish request 자체는 삭제가 요청되었다는 기록으로 유지될 수 있으며, 이는 삭제된 event가 다른 relay에서 다시 가져오는 것을 방지하는 데 도움이 됩니다.

vanish request가 모든 `e` 태그를 생략하면, relay는 이를 해당 pubkey의 모든 event를 제거하라는 요청으로 해석합니다. 이것은 더 과감한 조치이며 relay가 다르게 처리할 수 있습니다. 예를 들어 pubkey를 "vanished"로 표시하고 앞으로 해당 event를 수락하거나 제공하는 것을 거부할 수 있습니다.

relay는 NIP-62를 지원할 필요가 없습니다. Nostr 네트워크는 탈중앙화되어 있으며, 각 relay 운영자는 자체 데이터 보존 정책을 결정합니다. 사용자는 vanish request를 게시했다고 해서 콘텐츠가 모든 곳에서 삭제될 것이라고 가정해서는 안 됩니다.

## 개인정보 보호 고려 사항

vanish request는 최선의 노력을 기울이는 삭제 메커니즘이지 개인정보 보호를 보장하는 것이 아닙니다. vanish request를 게시한 후에도 콘텐츠의 복사본이 NIP-62를 지원하지 않는 다른 relay, 클라이언트 기기의 로컬 캐시, 서드파티 아카이브나 검색 엔진, 그리고 백업에 존재할 수 있습니다.

요청 자체도 서명된 Nostr event이므로 공개 기록의 일부가 됩니다. vanish request를 보는 사람은 당신이 무언가를 삭제했다는 것을 알 수 있으며, 삭제된 것이 무엇인지 볼 수 없더라도 마찬가지입니다.

비공개로 유지해야 하는 콘텐츠의 경우, 사후 삭제에 의존하기보다 [NIP-17](/ko/topics/nip-17/)과 같은 암호화된 메시징 사용을 고려하세요.

---

**주요 출처:**
- [NIP-62 사양](https://github.com/nostr-protocol/nips/blob/master/62.md)

**언급된 곳:**
- [Newsletter #5: 주목할 만한 코드 변경 사항](/ko/newsletters/2026-01-13-newsletter/#rust-nostr-library)
