---
title: "NIP-94: 파일 메타데이터"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2026-04-22
draft: false
categories:
  - Media
  - Protocol
---

NIP-94는 공유 파일을 정리하고 분류하기 위한 파일 메타데이터 이벤트(kind 1063)를 정의합니다. 이를 통해 릴레이가 콘텐츠를 더 효과적으로 필터링하고 정리할 수 있습니다.

## 작동 방식

NIP-94는 kind `1063`을 파일의 독립적인 메타데이터 이벤트로 사용합니다. 이벤트 `content`에는 사람이 읽을 수 있는 설명이 들어가고, 태그에는 다운로드 URL, MIME type, 해시, 크기, 미리보기 힌트 같은 기계 판독 필드가 담깁니다.

이 분리가 중요한 이유는 메타데이터 이벤트를 그 파일을 링크하는 특정 노트와 별개로 인덱싱하고 필터링하고 재사용할 수 있기 때문입니다. 클라이언트는 자유 형식 게시물 텍스트에서 메타데이터를 긁어내는 대신, kind `1063` 이벤트를 자산의 정식 설명으로 취급할 수 있습니다.

## 필수 및 선택 태그

**핵심 태그:**
- `url` - 파일 다운로드 링크
- `m` - MIME type (소문자 형식 필수)
- `x` - 파일의 SHA-256 해시

**선택 태그:**
- `ox` - 서버 변환 이전 원본 파일의 SHA-256 해시
- `size` - 바이트 단위 파일 크기
- `dim` - 이미지/비디오 크기 (가로 x 세로)
- `magnet` - 토렌트 배포용 Magnet URI
- `i` - 토렌트 infohash
- `blurhash` - preview용 placeholder 이미지
- `thumb` - thumbnail URL
- `image` - preview 이미지 URL
- `summary` - 텍스트 발췌
- `alt` - 접근성 설명
- `fallback` - 대체 다운로드 소스
- `service` - NIP-96 같은 저장 프로토콜 또는 서비스 유형

`ox`와 `x` 태그는 놓치기 쉽지만 실제로 꽤 유용합니다. `ox`는 원래 업로드된 파일을 식별하고, `x`는 서버가 실제로 제공하는 변환된 버전을 식별할 수 있습니다. 미디어 호스트가 업로드를 압축하거나 리사이즈할 때도, 클라이언트는 변환된 blob이 원본과 바이트 단위로 같다고 가장하지 않으면서 원본 파일의 정체성을 유지할 수 있습니다.

## 언제 써야 하는가

NIP-94는 소셜 또는 장문 콘텐츠 클라이언트보다 파일 공유 애플리케이션을 위해 설계되었습니다. 예로는 다음이 있습니다:

- 토렌트 인덱싱 릴레이
- 포트폴리오 공유 플랫폼 (Pinterest와 비슷한 형태)
- 소프트웨어 설정과 업데이트 배포
- 미디어 라이브러리와 아카이브

파일 메타데이터가 다른 이벤트 안에 들어 있는 URL을 꾸며 주는 역할만 하면 된다면 [NIP-92: 미디어 첨부](/ko/topics/nip-92/)가 더 가볍습니다. 파일 자체를 일급 객체처럼 질의 가능하게 해야 할 때는 NIP-94가 더 적합합니다.

## 상호운용성 참고사항

NIP-94는 여러 저장 backend에서 동작합니다. 파일은 [NIP-96: HTTP File Storage](/ko/topics/nip-96/), Blossom, 또는 다른 서비스를 통해 업로드된 뒤에도 같은 kind `1063` 이벤트 형태로 설명될 수 있습니다. 메타데이터 형식이 특정 단일 업로드 프로토콜보다 더 오래 살아남는 이유가 여기에 있습니다.

---

**주요 출처:**
- [NIP-94 Specification](https://github.com/nostr-protocol/nips/blob/master/94.md)

**언급된 뉴스레터:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #14: NIP Deep Dive](/ko/newsletters/2026-03-18-newsletter/)

**같이 보기:**
- [NIP-92: 미디어 첨부](/ko/topics/nip-92/)
- [Blossom](/ko/topics/blossom/)
