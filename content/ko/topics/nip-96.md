---
title: "NIP-96: HTTP File Storage"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - 미디어
---
NIP-96은 Nostr 클라이언트가 HTTP 미디어 서버에서 파일을 업로드, 다운로드, 관리하는 방법을 정의한다. 현재 Blossom을 권장하면서 "비권장(unrecommended)"으로 표시되었지만, 기존 서버와 클라이언트가 전환 기간 동안 계속 지원하고 있어 여전히 중요하다.

## 작동 방식

클라이언트는 `/.well-known/nostr/nip96.json`을 가져와 파일 서버의 기능을 탐색한다. 이 문서는 업로드 API URL, 선택적 다운로드 URL, 지원되는 콘텐츠 유형, 크기 제한, 서버가 미디어 변환이나 위임 호스팅을 지원하는지 여부를 광고한다.

업로드 시 클라이언트는 [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) 인증 헤더와 함께 `multipart/form-data` POST를 API URL로 전송한다. 서버는 원본 해시를 위한 `ox`와 해당되는 경우 실제로 제공될 변환된 파일을 위한 `x`를 포함하는 NIP-94 형태의 메타데이터 객체로 응답한다.

다운로드는 이미지 너비 같은 선택적 쿼리 파라미터와 함께 `GET <api_url>/<sha256-hash>`를 사용한다. 삭제는 NIP-98 인증과 함께 `DELETE`를 사용한다. 사용자는 kind `10096` 이벤트를 발행하여 선호하는 업로드 서버를 선언한다.

## 데이터 모델 상세

유용한 세부사항 하나는 NIP-96이 서버가 업로드를 변환하더라도 원본 파일 해시로 파일을 식별한다는 점이다. 이를 통해 클라이언트는 동일한 안정적 식별자로 자산을 삭제하거나 재다운로드할 수 있으면서도, 가능한 경우 서버 생성 썸네일이나 재압축 변형을 받을 수 있다.

well-known 문서는 `delegated_to_url`도 지원하여, 릴레이가 클라이언트를 별도의 HTTP 스토리지 서버로 안내할 수 있다. 이를 통해 릴레이 소프트웨어가 전체 미디어 API를 직접 구현하지 않아도 되었다.

## 비권장 처리된 이유

NIP-96은 파일 URL을 특정 서버에 묶었다. 서버가 다운되면 해당 서버 URL을 참조하는 모든 Nostr 노트가 미디어를 잃었다. Blossom은 파일 콘텐츠의 SHA-256 해시를 정식 식별자로 만들어 이를 뒤집었다. 같은 파일을 호스팅하는 어떤 Blossom 서버든 같은 해시 경로로 제공하므로, 콘텐츠가 기본적으로 서버 간에 이식 가능하다.

Blossom은 API도 단순화한다: 업로드에 일반 PUT, 다운로드에 GET, 인증에 HTTP 헤더가 아닌 서명된 Nostr 이벤트를 사용한다. 비권장 처리는 2025년 9월에 [PR #2047](https://github.com/nostr-protocol/nips/pull/2047)을 통해 이루어졌다.

## 상호운용성 참고사항

nostr.build와 void.cat 같은 서버는 NIP-96을 지원했고 Blossom 엔드포인트를 추가하거나 마이그레이션했다. 클라이언트는 다양한 단계에 있다: Angor v0.2.5는 NIP-96 서버 설정을 추가했고 ZSP v0.3.1은 Blossom 서버에만 업로드한다. 나머지 NIP-96 구현이 마이그레이션을 완료할 때까지 공존이 계속될 것이다.

Kind 10096 서버 선호 이벤트는 Blossom 서버 선택에도 여전히 유용하다. NIP-94 파일 메타데이터(kind 1063 이벤트)는 어떤 업로드 프로토콜이 생성했는지와 관계없이 파일 속성을 설명한다.

---

**주요 출처:**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: NIP-96 비권장 표시](https://github.com/nostr-protocol/nips/pull/2047)

**언급된 뉴스레터:**
- [Newsletter #9: NIP Deep Dive](/en/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-96-http-file-storage-and-the-transition-to-blossom)

**같이 보기:**
- [Blossom Protocol](/ko/topics/blossom/)
- [NIP-94: File Metadata](/ko/topics/nip-94/)
