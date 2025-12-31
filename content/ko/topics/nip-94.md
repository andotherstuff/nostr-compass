---
title: "NIP-94: File Metadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2025-12-31
draft: false
categories:
  - 미디어
  - 프로토콜
---

NIP-94는 Nostr에서 공유되는 파일을 정리하고 분류하기 위한 파일 메타데이터 이벤트(kind 1063)를 정의하여, relay가 콘텐츠를 효과적으로 필터링하고 정리할 수 있게 합니다.

## 작동 방식

1. 사용자가 호스팅 서비스에 파일을 업로드
2. 파일에 대한 메타데이터가 포함된 kind 1063 이벤트가 게시됨
3. 이벤트 내용에는 사람이 읽을 수 있는 설명이 포함됨
4. 구조화된 tag가 기계가 읽을 수 있는 메타데이터를 제공
5. 전문 클라이언트가 파일을 체계적으로 정리하고 표시할 수 있음

## 필수 및 선택 태그

**핵심 tag:**
- `url` - 파일 다운로드 링크
- `m` - MIME type (소문자 형식 필수)
- `x` - 파일의 SHA-256 해시

**선택 tag:**
- `ox` - 서버 변환 전 원본 파일의 SHA-256 해시
- `size` - 바이트 단위의 파일 크기
- `dim` - 이미지/비디오 치수 (너비 x 높이)
- `magnet` - torrent 배포용 magnet URI
- `i` - torrent infohash
- `blurhash` - 미리보기용 플레이스홀더 이미지
- `thumb` - 썸네일 URL
- `image` - 미리보기 이미지 URL
- `summary` - 텍스트 발췌
- `alt` - 접근성 설명
- `fallback` - 대체 다운로드 소스

## 사용 사례

NIP-94는 소셜 또는 장문 콘텐츠 클라이언트가 아닌 파일 공유 애플리케이션을 위해 설계되었습니다. 권장 애플리케이션은 다음과 같습니다:

- Torrent 인덱싱 relay
- 포트폴리오 공유 플랫폼 (Pinterest와 유사)
- 소프트웨어 설정 및 업데이트 배포
- 미디어 라이브러리 및 아카이브

---

**주요 출처:**
- [NIP-94 사양](https://github.com/nostr-protocol/nips/blob/master/94.md)

**언급된 곳:**
- [Newsletter #3: 12월 요약](/ko/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**함께 보기:**
- [NIP-92: 미디어 첨부](/ko/topics/nip-92/)
- [Blossom](/ko/topics/blossom/)
