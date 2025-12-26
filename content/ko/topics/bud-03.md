---
title: "BUD-03: 사용자 서버 리스트"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-03은 사용자가 선호하는 Blossom 서버를 게시하는 방법을 정의하여, 클라이언트가 사용자의 미디어 파일을 업로드하고 검색할 위치를 검색할 수 있게 합니다.

## 작동 방식

사용자는 Blossom 서버를 나열하는 kind 10063 이벤트를 게시합니다. 그러면 클라이언트가:
- 사용자가 선호하는 서버에 미디어 업로드
- pubkey가 주어지면 사용자의 blob을 어디서 찾을 수 있는지 검색

이를 통해 콘텐츠에 서버 URL을 직접 포함하는 것의 대안으로 작성자 기반 검색이 가능합니다.

---

**주요 출처:**
- [BUD-03 사양](https://github.com/hzrd149/blossom/blob/master/buds/03.md)

**참고:**
- [Blossom 프로토콜](/ko/topics/blossom/)
- [NIP-51: 리스트](/ko/topics/nip-51/)

