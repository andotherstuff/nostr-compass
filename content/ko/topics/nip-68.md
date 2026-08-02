---
title: "NIP-68: 사진 우선 피드"
date: 2026-07-29
translationOf: /en/topics/nip-68.md
translationDate: 2026-08-02
draft: false
categories:
  - Media
  - Protocol
---

NIP-68은 주소 지정 가능한 사진 이벤트를 정의합니다. 클라이언트가 이미지 메타데이터, 캡션, label, 이미지 파일 참조를 클라이언트 간 이식 가능한 방식으로 발행하면서 이벤트 자체는 blob 저장소와 분리할 수 있게 합니다.

## 작동 방식

사진은 kind `20`을 사용하며 `title` tag와 함께 `content`에 설명을 담습니다. `imeta` tag는 각 이미지를 `url`, MIME type을 나타내는 `m`, 크기를 나타내는 `dim`, `alt` 텍스트, 선택적 SHA-256 해시 같은 필드로 설명합니다. 여러 `imeta` tag를 사용하면 하나의 이벤트가 이미지 모음을 나타낼 수 있습니다.

이벤트에는 사진에 등장했거나 크레디트에 명시된 사람을 표시하는 `p` tag, 주제를 표시하는 `t` tag, 일반 Nostr 참조를 넣을 수 있습니다. 또한 media type, hash, location, content-warning tag를 포함할 수 있어 클라이언트가 이미지 게시물을 일관되게 필터링하고 렌더링할 수 있습니다.

NIP-68은 저장 backend를 규정하지 않습니다. 다른 클라이언트가 이미지를 표시하고 검증할 수 있을 만큼 충분한 `imeta` 메타데이터를 발행한다면, 클라이언트는 일반 HTTPS URL이나 Blossom 같은 콘텐츠 주소 지정 시스템을 참조할 수 있습니다.

## 구현

[NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0)은 이미지 중심 클라이언트 기능과 함께 NIP-68 이미지 tag를 추가했습니다.

---

**주요 출처:**
- [NIP-68 명세](https://github.com/nostr-protocol/nips/blob/master/68.md)
- [NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0)

**언급된 뉴스레터:**
- [뉴스레터 #33: 태그 릴리스](/ko/newsletters/2026-07-29-newsletter/#tagged-releases)

**같이 보기:**
- [Blossom 프로토콜](/ko/topics/blossom/)
- [NIP-94: 파일 메타데이터](/ko/topics/nip-94/)
