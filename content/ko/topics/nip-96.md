---
title: "NIP-96: HTTP 파일 저장소"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Media
---

NIP-96은 Nostr 클라이언트가 HTTP 미디어 서버에서 파일을 업로드, 다운로드, 관리하는 방법을 정의했습니다. 현재 Blossom을 권장하며 "비권장"으로 표시되어 있지만, 프로젝트들이 두 미디어 표준 사이의 전환을 진행하고 있어 NIP-96은 여전히 관련성이 있습니다.

## 작동 방식

클라이언트는 `/.well-known/nostr/nip96.json`을 가져와 파일 서버의 기능을 파악합니다. 여기에는 API URL, 지원되는 콘텐츠 유형, 크기 제한, 사용 가능한 미디어 변환이 포함됩니다.

업로드 시 클라이언트는 NIP-98 인가 헤더(업로더의 신원을 증명하는 서명된 Nostr event)와 함께 API URL로 `multipart/form-data` POST를 보냅니다. 서버는 파일 URL, SHA-256 해시, MIME 유형, 크기를 포함하는 NIP-94 파일 메타데이터 구조를 반환합니다.

다운로드는 `<api_url>/<sha256-hash>`로의 GET 요청을 사용하며, 이미지 리사이징 같은 서버 측 변환을 위한 선택적 쿼리 파라미터가 있습니다. 삭제는 NIP-98 인증과 함께 DELETE를 사용합니다. 사용자는 선호하는 업로드 서버를 선언하기 위해 kind 10096 event를 게시합니다.

## 비권장 이유

NIP-96은 파일 URL을 특정 서버에 묶었습니다. 서버가 다운되면 해당 서버의 URL을 참조하는 모든 Nostr 노트가 미디어를 잃었습니다. Blossom은 파일 콘텐츠의 SHA-256 해시를 표준 식별자로 만들어 이를 뒤집었습니다. 동일한 파일을 호스팅하는 모든 Blossom 서버가 같은 해시 경로에서 제공하므로, 콘텐츠가 기본적으로 서버 간에 이동 가능합니다.

Blossom은 API도 단순화합니다: 업로드에 PUT, 다운로드에 GET, 인가에 서명된 Nostr event(HTTP 헤더가 아님)를 사용합니다. 비권장 처리는 2025년 9월 [PR #2047](https://github.com/nostr-protocol/nips/pull/2047)을 통해 이루어졌습니다.

## 전환 과정

nostr.build와 void.cat 같은 서버가 NIP-96을 지원했고 Blossom 엔드포인트를 추가하거나 마이그레이션했습니다. 클라이언트는 다양한 단계에 있습니다: Angor v0.2.5는 프로젝트 이미지를 위해 NIP-96 서버 설정을 추가했고, ZSP v0.3.1은 Blossom 서버로만 업로드합니다. 나머지 NIP-96 구현이 마이그레이션을 완료할 때까지 공존이 계속될 것입니다.

Kind 10096 서버 선호 event는 Blossom 서버 선택에도 유용합니다. NIP-94 파일 메타데이터(kind 1063 event)는 어떤 업로드 프로토콜로 생성되었든 파일 속성을 설명합니다.

---

**주요 출처:**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**언급된 곳:**
- [뉴스레터 #9: NIP 심층 분석](/ko/newsletters/2026-02-11-newsletter/#nip-심층-분석-nip-96-http-파일-저장소와-blossom으로의-전환)

**참고:**
- [Blossom 프로토콜](/ko/topics/blossom/)
- [NIP-94: 파일 메타데이터](/ko/topics/nip-94/)
