---
title: "NIP-94: File Metadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---
NIP-94는 Nostr에서 공유 파일을 정리하고 분류하기 위한 파일 메타데이터 이벤트(kind 1063)를 정의하여, 릴레이가 콘텐츠를 효과적으로 필터링하고 정리할 수 있게 한다.

## 작동 방식

NIP-94는 kind `1063`을 파일의 독립 메타데이터 이벤트로 사용한다. 이벤트 `content`에는 사람이 읽을 수 있는 설명이 들어가고, 태그에는 다운로드 URL, MIME 유형, 해시, 크기, 미리보기 힌트 같은 기계 판독 가능한 필드가 포함된다.

이러한 분리가 중요한 이유는 메타데이터 이벤트가 파일을 링크하는 노트와 독립적으로 인덱싱, 필터링, 재사용될 수 있기 때문이다. 클라이언트는 자유형식 게시물 텍스트에서 메타데이터를 스크래핑하는 대신 kind `1063` 이벤트를 자산의 정식 설명으로 취급할 수 있다.

## 필수 및 선택 태그

**핵심 태그:**
- `url` - 파일 다운로드 링크
- `m` - MIME 유형 (소문자 형식 필수)
- `x` - 파일의 SHA-256 해시

**선택 태그:**
- `ox` - 서버 변환 전 원본 파일의 SHA-256 해시
- `size` - 파일 크기(바이트)
- `dim` - 이미지/비디오 크기 (가로 x 세로)
- `magnet` - 토렌트 배포용 Magnet URI
- `i` - 토렌트 infohash
- `blurhash` - 미리보기용 플레이스홀더 이미지
- `thumb` - 썸네일 URL
- `image` - 미리보기 이미지 URL
- `summary` - 텍스트 발췌
- `alt` - 접근성 설명
- `fallback` - 대체 다운로드 소스
- `service` - NIP-96 같은 스토리지 프로토콜 또는 서비스 유형

`ox`와 `x` 태그는 놓치기 쉽지만 실무에서 유용하다. `ox`는 원본 업로드 파일을 식별하고, `x`는 서버가 실제로 제공하는 변환된 버전을 식별할 수 있다. 미디어 호스트가 업로드를 압축하거나 크기를 변경할 때, 변환된 blob이 바이트 단위로 동일한 것처럼 위장하지 않으면서도 원본 파일 아이덴티티를 보존할 수 있다.

## 사용 시기

NIP-94는 소셜이나 장문 콘텐츠 클라이언트보다 파일 공유 애플리케이션을 위해 설계되었다. 권장 활용 분야는 다음과 같다:

- 토렌트 인덱싱 릴레이
- 포트폴리오 공유 플랫폼 (Pinterest와 유사)
- 소프트웨어 설정 및 업데이트 배포
- 미디어 라이브러리 및 아카이브

파일 메타데이터가 다른 이벤트 내에 임베드된 URL을 장식하기만 하면 된다면, [NIP-92: 미디어 첨부](/ko/topics/nip-92/)가 더 가볍다. NIP-94는 파일 자체가 일급 객체로 쿼리 가능해야 할 때 더 나은 선택이다.

## 상호운용성 참고사항

NIP-94는 스토리지 백엔드를 가리지 않는다. 파일은 [NIP-96: HTTP File Storage](/ko/topics/nip-96/), Blossom, 또는 다른 서비스를 통해 업로드된 후에도 동일한 kind `1063` 이벤트 형태로 설명될 수 있다. 메타데이터 형식이 어떤 단일 업로드 프로토콜보다 오래 지속되는 이유가 바로 이것이다.

---

**주요 출처:**
- [NIP-94 명세](https://github.com/nostr-protocol/nips/blob/master/94.md)

**언급된 뉴스레터:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**같이 보기:**
- [NIP-92: 미디어 첨부](/ko/topics/nip-92/)
- [Blossom](/ko/topics/blossom/)
