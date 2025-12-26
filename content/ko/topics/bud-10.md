---
title: "BUD-10: Blossom URI 스킴"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-10은 사용 가능한 모든 서버에서 파일을 검색하는 데 필요한 모든 정보를 포함하는 Blossom용 커스텀 URI 스킴을 정의합니다.

## URI 형식

```
blossom:<sha256>.<ext>?size=<bytes>&server=<url>&server=<url>&pubkey=<hex>
```

구성 요소:
- **sha256**: 파일 해시(필수)
- **ext**: 파일 확장자
- **size**: 바이트 단위 파일 크기
- **server**: 하나 이상의 서버 힌트
- **pubkey**: BUD-03 서버 검색을 위한 작성자 pubkey

## 이점

- 정적 HTTP URL보다 더 탄력적
- 여러 서버에 걸친 자동 폴백
- pubkey 힌트를 통한 작성자 기반 검색
- 자체 검증(해시가 무결성 보장)

---

**주요 출처:**
- [BUD-10 PR](https://github.com/hzrd149/blossom/pull/84)

**언급된 곳:**
- [뉴스레터 #1: 뉴스](/ko/newsletters/2025-12-17-newsletter/#news)

**참고:**
- [Blossom 프로토콜](/ko/topics/blossom/)
- [BUD-03: 사용자 서버 리스트](/ko/topics/bud-03/)

