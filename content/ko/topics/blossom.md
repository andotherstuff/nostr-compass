---
title: "Blossom 프로토콜"
date: 2025-12-17
translationOf: /en/topics/blossom.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---
Blossom은 Nostr용 미디어 호스팅 프로토콜로, 일반 HTTP 서버에 blob을 저장하고 서버가 할당하는 ID 대신 SHA-256 해시로 주소를 지정한다.

## 작동 방식

Blossom 서버는 blob 조회, 업로드, 관리를 위한 간결한 HTTP 인터페이스를 제공한다. 정식 식별자는 파일 해시이므로, 동일한 blob은 모든 호환 서버에서 같은 주소를 유지한다.

- `GET /<sha256>` 해시로 blob 조회
- `PUT /upload` blob 업로드
- kind `24242` Nostr 이벤트로 업로드 및 관리 작업을 인가
- kind `10063` 이벤트는 [BUD-03](/ko/topics/bud-03/)에 정의되며, 사용자가 선호하는 서버를 공개할 수 있게 한다

해시가 식별자이기 때문에, 클라이언트는 다운로드 후 로컬에서 무결성을 검증할 수 있고 기존 참조를 변경하지 않고 다른 서버에서 재시도할 수 있다.

## 왜 중요한가

Blossom은 blob 저장소를 소셜 이벤트와 분리한다. 노트나 프로필이 미디어를 가리킬 때 특정 호스트의 URL 설계에 종속되지 않는다.

장애 처리 방식도 달라진다. 서버가 사라지면 클라이언트는 미러, 캐시, 또는 작성자의 [BUD-03](/ko/topics/bud-03/) 목록을 통해 발견한 서버에서 같은 해시를 가져올 수 있다. 원본 호스트 URL이 유일한 위치 지정자인 미디어 시스템에 비해 실질적인 개선이다.

## 상호운용성 참고사항

Blossom은 모듈식이다. 핵심 조회 및 업로드 동작은 BUD-01과 BUD-02에 있고, 미러링, 미디어 최적화, 인가, URI 공유는 별도 BUD로 분리되어 있다.

이 분리 덕분에 클라이언트는 기본 상호운용에 필요한 최소한만 구현한 뒤, [BUD-10](/ko/topics/bud-10/) URI 힌트나 로컬 캐싱 같은 선택적 기능을 지원이 성숙해지면 추가할 수 있다.

---

**주요 출처:**
- [Blossom 저장소](https://github.com/hzrd149/blossom)
- [BUD-01: 서버 요구사항 및 blob 조회](https://github.com/hzrd149/blossom/blob/master/buds/01.md)
- [BUD-02: Blob 업로드 및 관리](https://github.com/hzrd149/blossom/blob/master/buds/02.md)
- [로컬 Blossom 캐시 가이드](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md)

**언급된 뉴스레터:**
- [뉴스레터 #1: 뉴스](/en/newsletters/2025-12-17-newsletter/)
- [뉴스레터 #2: 주요 코드 변경사항](/en/newsletters/2025-12-24-newsletter/)
- [뉴스레터 #10: Blossom 로컬 캐시 레이어 등장](/en/newsletters/2026-02-18-newsletter/)

**같이 보기:**
- [BUD-03: 사용자 서버 목록](/ko/topics/bud-03/)
- [BUD-10: Blossom URI 스킴](/ko/topics/bud-10/)
