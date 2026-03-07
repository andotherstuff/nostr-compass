---
title: "BUD-03: 사용자 서버 목록"
date: 2025-12-17
translationOf: /en/topics/bud-03.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---
BUD-03는 사용자가 선호하는 Blossom 서버를 공개하는 방법을 정의한다. 이를 통해 클라이언트는 blob을 어디에 업로드할지, 미디어 URL이 작동하지 않을 때 어디서 찾아야 할지 알 수 있다.

## 작동 방식

사용자는 하나 이상의 `server` 태그가 포함된 교체 가능한(replaceable) kind `10063` 이벤트를 발행한다. 각 태그에는 완전한 Blossom 서버 URL이 들어간다.

이후 클라이언트는 다음을 수행할 수 있다:
- 사용자가 선호하는 서버에 blob 업로드
- 작성자의 공개키로부터 blob 위치 추정
- 기존 URL이 깨졌을 때 목록에 있는 서버에서 재시도

## 참고 세부사항

`server` 태그의 순서가 중요하다. 사양에 따르면 사용자는 가장 신뢰하거나 안정적인 서버를 먼저 나열해야 하며, 클라이언트는 최소한 첫 번째 서버에 업로드를 시도해야 한다. 따라서 BUD-03는 단순한 디렉터리가 아니라 약한 선호도 신호이기도 하다.

조회 지침도 실용적이다. 클라이언트가 URL에서 blob 해시를 추출할 때, 경로에서 마지막 64자리 16진수 문자열을 사용해야 한다. 이를 통해 표준 Blossom URL과 해시가 포함된 비표준 CDN 스타일 URL 모두에서 blob을 복구할 수 있다.

---

**주요 출처:**
- [BUD-03 사양](https://github.com/hzrd149/blossom/blob/master/buds/03.md)
- [Blossom 저장소](https://github.com/hzrd149/blossom)

**언급된 뉴스레터:**
- [뉴스레터 #1: 뉴스](/en/newsletters/2025-12-17-newsletter/#news)

**같이 보기:**
- [Blossom 프로토콜](/ko/topics/blossom/)
- [NIP-51: 목록](/ko/topics/nip-51/)
