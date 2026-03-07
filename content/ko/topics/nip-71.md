---
title: "NIP-71: 비디오 이벤트"
date: 2026-01-13
translationOf: /en/topics/nip-71.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---
NIP-71은 Nostr에서 비디오 콘텐츠를 위한 이벤트 kind를 정의하여, 적절한 메타데이터 지원과 함께 비디오 공유를 가능하게 한다. 이 사양은 일반 비디오 이벤트와 addressable 비디오 이벤트를 모두 다루며, 후자는 2026년 1월에 추가되어 크리에이터가 재게시 없이 비디오 메타데이터를 업데이트할 수 있게 한다.

## 이벤트 Kind

NIP-71은 화면 비율과 addressability에 따라 두 가지 범주로 나뉜 네 가지 이벤트 kind를 정의한다.

일반 비디오 이벤트는 가로(landscape) 비디오에 kind 21, 세로(portrait/shorts) 비디오에 kind 22를 사용한다. 이들은 게시 후 콘텐츠를 변경할 수 없는 표준 Nostr 이벤트이다.

Addressable 비디오 이벤트는 가로 비디오에 kind 34235, 세로 비디오에 kind 34236을 사용한다. pubkey, kind, `d` 태그의 조합으로 식별되는 매개변수화된 교체 가능 이벤트이다. 같은 식별자로 새 이벤트를 게시하면 이전 버전을 대체하여 메타데이터 업데이트가 가능하다.

## 구조

완전한 addressable 비디오 이벤트는 식별 필드, 메타데이터 태그, 비디오 콘텐츠 참조를 포함한다.

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

`d` 태그는 해당 kind의 비디오 내에서 고유 식별자를 제공하므로, 다른 `d` 값을 사용하여 여러 addressable 비디오를 가질 수 있다. `title`과 `summary` 태그는 클라이언트에서 표시할 비디오 제목과 짧은 설명을 제공한다. `url` 태그는 실제 비디오 파일을 가리키고, `thumb`은 미리보기 이미지를 제공한다. `duration` 태그는 초 단위의 길이를 지정하고, `dim`은 선택적으로 비디오 해상도를 지정한다.

`origin` 태그는 다른 서비스에서 콘텐츠를 가져올 때 원본 플랫폼을 추적한다. YouTube, Vimeo 또는 기타 플랫폼에서 Nostr 호스팅으로 비디오를 마이그레이션할 때 출처를 보존한다.

`content` 필드에는 확장 설명, 전체 자막, 비디오와 관련된 추가 텍스트를 담을 수 있다.

## Addressable 이벤트가 중요한 이유

일반 비디오 이벤트(kind 21, 22)는 게시 후 변경할 수 없다. 비디오를 게시한 후 제목의 오타를 발견하거나, 썸네일을 업데이트하고 싶거나, 다른 비디오 서비스로 마이그레이션하여 호스팅 URL을 변경해야 하는 경우 원본 이벤트를 수정할 수 없다. 유일한 방법은 새 ID로 새 이벤트를 게시하는 것인데, 이는 기존 참조를 깨뜨리고 참여 지표를 잃게 된다.

Addressable 비디오 이벤트는 이벤트를 교체 가능하게 만들어 이 문제를 해결한다. pubkey, 이벤트 kind, `d` 태그의 조합이 비디오를 고유하게 식별한다. 같은 식별자로 새 이벤트를 게시하면 릴레이가 이전 버전을 새 버전으로 대체한다. 비디오를 가져오는 클라이언트는 항상 최신 메타데이터를 받게 된다.

이는 게시 후 메타데이터 오류 수정, 브랜딩 개선에 따른 썸네일 업데이트, 호스팅 제공자 변경 시 비디오 호스팅 URL 마이그레이션, Vine과 같은 중단된 플랫폼에서 `origin` 태그를 통해 출처를 보존하면서 콘텐츠를 가져올 때 특히 유용하다.

추가적인 이점은 안정적인 링크이다. 다른 이벤트는 크리에이터가 주변 표시 세부사항을 업데이트하는 동안 같은 addressable 비디오를 계속 참조할 수 있으며, 이는 여러 불변 재게시에 걸쳐 댓글과 참조가 분산되는 것보다 깔끔하다.

## 트레이드오프

교체 가능성은 메타데이터 유지 관리에 도움이 되지만, 클라이언트가 얼마나 많은 이력 상태를 보존할지 결정해야 한다는 의미이기도 하다. 크리에이터가 게시 후 제목이나 요약을 변경하면, 이전 클라이언트가 이전 버전을 인덱싱했을 수 있지만 최신 이벤트가 정규 버전이 된다.

Kind 21과 22는 불변 게시 기록이 필요한 애플리케이션에서 여전히 중요하다. NIP-71은 모든 비디오 워크플로를 교체 가능 모델로 강제하지 않는다.

## 구현

Addressable 비디오 이벤트(kind 34235, 34236)는 현재 Amethyst와 nostrvine에 구현되어 있다. 두 클라이언트 모두 addressable 비디오 이벤트를 생성, 표시, 업데이트할 수 있다.

---

**주요 출처:**
- [NIP-71 사양](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Addressable 비디오 이벤트 업데이트

**언급된 뉴스레터:**
- [뉴스레터 #5: NIP 업데이트](/en/newsletters/2026-01-13-newsletter/#nip-updates)
- [뉴스레터 #12: NoorNote](/en/newsletters/2026-03-04-newsletter/)

**같이 보기:**
- [NIP-94: 파일 메타데이터](/ko/topics/nip-94/)
