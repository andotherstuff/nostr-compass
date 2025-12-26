---
title: "Blossom 프로토콜"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

Blossom은 콘텐츠 주소 지정 가능 URL을 사용하는 탈중앙화 파일 저장소를 제공하는 Nostr용 미디어 호스팅 프로토콜입니다.

## 작동 방식

파일은 Blossom 서버에 저장되고 SHA256 해시로 주소가 지정됩니다. 이것은 다음을 의미합니다:
- 동일한 파일은 모든 서버에서 항상 동일한 URL을 가짐
- 파일은 해당 파일을 가진 모든 서버에서 검색 가능
- 클라이언트는 해시를 확인하여 파일 무결성 검증 가능

## 기능

- 콘텐츠 주소 지정 가능 저장소
- 다중 서버 중복성
- BUD-03을 통한 작성자 검색
- BUD-10을 통한 커스텀 URI 스킴
- `/list` 엔드포인트에서 커서 기반 페이지네이션

---

**주요 출처:**
- [Blossom 저장소](https://github.com/hzrd149/blossom)

**언급된 곳:**
- [뉴스레터 #1: 뉴스](/ko/newsletters/2025-12-17-newsletter/#news)
- [뉴스레터 #2: 주목할 만한 코드 변경](/ko/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)

**참고:**
- [BUD-03: 사용자 서버 리스트](/ko/topics/bud-03/)
- [BUD-10: Blossom URI 스킴](/ko/topics/bud-10/)

