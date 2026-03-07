---
title: "BUD-10: Blossom URI 스킴"
date: 2025-12-17
translationOf: /en/topics/bud-10.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---
BUD-10은 `blossom:` URI 스킴을 정의한다. 파일 해시와 함께 서버 힌트, 작성자 힌트, 예상 크기를 포함할 수 있는 이식 가능한 blob 참조이다.

## URI 형식

```
blossom:<sha256>.<ext>?xs=<server>&as=<pubkey>&sz=<bytes>
```

사양은 소문자 64자리 SHA-256 해시와 파일 확장자를 요구한다. 확장자를 알 수 없는 경우 클라이언트는 `.bin`으로 대체해야 한다.

## 해석 방식

클라이언트는 `blossom:` URI를 다음 단계로 해석해야 한다:

1. `xs` 서버 힌트를 나타난 순서대로 시도
2. `as` 작성자 공개키가 있으면 각 작성자의 [BUD-03](/ko/topics/bud-03/) 서버 목록을 가져와서 해당 서버를 시도
3. 필요하면 잘 알려진 서버나 로컬 캐시로 대체

이 순서는 보낸 사람이 빠른 조회를 위한 즉각적인 힌트를 첨부하면서도, 그 힌트가 오래된 경우를 대비한 복구 경로를 수신자에게 제공하기 때문에 유용하다.

## 왜 중요한가

`blossom:` URI는 일반 미디어 URL보다 magnet 링크에 가깝게 작동한다. 하나의 호스트가 영원히 사용 가능하다고 가정하는 대신, 어떤 blob을 가져올지 설명하고 어디서 찾을 수 있는지에 대한 단서를 포함한다.

선택적 `sz` 필드는 해시 외에 구체적인 무결성 검사를 추가한다. 클라이언트는 다운로드 전후에 예상 크기를 확인할 수 있어, 불완전한 전송을 감지하고 대용량 미디어의 사용자 경험을 개선한다.

---

**주요 출처:**
- [BUD-10 사양](https://github.com/hzrd149/blossom/blob/master/buds/10.md)
- [Blossom 저장소](https://github.com/hzrd149/blossom)

**언급된 뉴스레터:**
- [뉴스레터 #1: 뉴스](/en/newsletters/2025-12-17-newsletter/#news)

**같이 보기:**
- [Blossom 프로토콜](/ko/topics/blossom/)
- [BUD-03: 사용자 서버 목록](/ko/topics/bud-03/)
