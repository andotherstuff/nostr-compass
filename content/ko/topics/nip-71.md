---
title: "NIP-71: Video Events"
date: 2026-01-13
draft: false
categories:
  - Media
  - Protocol
---

NIP-71은 Nostr에서 비디오 콘텐츠를 위한 event kind를 정의하여 적절한 메타데이터 지원과 함께 비디오 공유를 가능하게 합니다. 이 사양은 일반 비디오 event와 주소 지정 가능한 비디오 event를 모두 다루며, 후자는 크리에이터가 다시 게시하지 않고도 비디오 메타데이터를 업데이트할 수 있도록 2026년 1월에 추가되었습니다.

## Event Kind

NIP-71은 화면비와 주소 지정 가능성에 따라 두 가지 범주로 나뉜 네 가지 event kind를 정의합니다.

일반 비디오 event는 가로(가로형) 비디오에 kind 21을, 세로(세로형/쇼츠) 비디오에 kind 22를 사용합니다. 이들은 게시된 후 콘텐츠가 변경 불가능한 표준 Nostr event입니다.

주소 지정 가능한 비디오 event는 가로 비디오에 kind 34235를, 세로 비디오에 kind 34236을 사용합니다. 이들은 pubkey, kind, `d` 태그의 조합으로 식별되는 매개변수화된 교체 가능 event입니다. 동일한 식별자로 새 event를 게시하면 이전 버전이 대체되어 메타데이터 업데이트가 가능합니다.

## 구조

완전한 주소 지정 가능한 비디오 event에는 식별 필드, 메타데이터 태그 및 비디오 콘텐츠 참조가 포함됩니다.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 34235,
  "tags": [
    ["d", "my-video-2026-01"],
    ["title", "Introduction to Nostr Video"],
    ["summary", "A walkthrough of NIP-71 video events"],
    ["url", "https://example.com/video.mp4"],
    ["thumb", "https://example.com/thumbnail.jpg"],
    ["duration", "300"],
    ["dim", "1920x1080"],
    ["origin", "youtube:dQw4w9WgXcQ"]
  ],
  "content": "Extended description, transcript, or additional notes about the video.",
  "sig": "sig1234..."
}
```

`d` 태그는 해당 kind의 비디오 내에서 고유 식별자를 제공하므로 다른 `d` 값을 사용하여 여러 주소 지정 가능한 비디오를 가질 수 있습니다. `title`과 `summary` 태그는 클라이언트에서 표시할 비디오 제목과 짧은 설명을 제공합니다. `url` 태그는 실제 비디오 파일을 가리키고 `thumb`은 미리보기 이미지를 제공합니다. `duration` 태그는 길이를 초 단위로 지정하고 `dim`은 선택적으로 비디오 크기를 지정합니다.

`origin` 태그는 다른 서비스에서 콘텐츠를 가져올 때 소스 플랫폼을 추적합니다. 이는 YouTube, Vimeo 또는 기타 플랫폼에서 Nostr 호스팅으로 비디오를 마이그레이션할 때 출처를 보존합니다.

`content` 필드는 확장된 설명, 전체 스크립트 또는 비디오와 관련된 추가 텍스트를 담을 수 있습니다.

## 주소 지정 가능한 Event가 중요한 이유

일반 비디오 event(kind 21 및 22)는 게시된 후 변경할 수 없습니다. 비디오를 게시한 후 제목에 오타가 있거나, 썸네일을 업데이트하거나, 다른 비디오 서비스로 마이그레이션하여 호스팅 URL을 변경해야 하는 경우 원본 event를 수정할 수 없습니다. 유일한 옵션은 새 ID로 새 event를 게시하는 것이며, 이는 기존 참조를 끊고 참여 지표를 잃게 됩니다.

주소 지정 가능한 비디오 event는 event를 교체 가능하게 만들어 이 문제를 해결합니다. pubkey, event kind, `d` 태그의 조합이 비디오를 고유하게 식별합니다. 동일한 식별자로 새 event를 게시하면 relay가 이전 버전을 새 버전으로 대체합니다. 비디오를 가져오는 클라이언트는 항상 최신 메타데이터를 받습니다.

이는 게시 후 메타데이터 오류 수정, 브랜딩 개선에 따른 썸네일 업데이트, 공급자 변경 시 비디오 호스팅 URL 마이그레이션, 그리고 `origin` 태그를 통해 출처를 보존하면서 Vine과 같은 중단된 플랫폼에서 콘텐츠 가져오기에 특히 유용합니다.

## 구현

주소 지정 가능한 비디오 event(kind 34235 및 34236)는 현재 Amethyst와 nostrvine에 구현되어 있습니다. 두 클라이언트 모두 주소 지정 가능한 비디오 event를 생성, 표시 및 업데이트할 수 있습니다.

---

**주요 출처:**
- [NIP-71 사양](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - 주소 지정 가능한 비디오 event 업데이트

**언급된 곳:**
- [Newsletter #5: NIP 업데이트](/ko/newsletters/2026-01-13-newsletter/#nip-updates)

**참고:**
- [NIP-94: 파일 메타데이터](/ko/topics/nip-94/)
