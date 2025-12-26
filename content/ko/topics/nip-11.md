---
title: "NIP-11: 릴레이 정보"
date: 2025-12-17
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11은 릴레이가 지원하는 NIP, 제한 사항, 연락처 정보를 포함하여 자신에 대한 메타데이터를 노출하는 방법을 정의합니다.

## 작동 방식

클라이언트는 `Accept: application/nostr+json` 헤더와 함께 릴레이의 WebSocket URL에 HTTP GET 요청을 보내 릴레이 정보를 가져옵니다. 릴레이는 기능을 설명하는 JSON 문서를 반환합니다.

## 주요 필드

- **name** - 사람이 읽을 수 있는 릴레이 이름
- **description** - 릴레이의 용도
- **supported_nips** - 구현된 NIP 목록
- **limitation** - 최대 메시지 크기, 필수 인증 등의 제한 사항
- **self** - 릴레이 자체의 공개 키(릴레이 신원을 위한 새 필드)

## 사용 사례

- 클라이언트는 연결 전에 릴레이가 필요한 기능을 지원하는지 확인할 수 있음
- 검색 서비스가 릴레이 기능을 인덱싱할 수 있음
- 사용자가 게시 전에 릴레이 정책을 볼 수 있음

---

**주요 출처:**
- [NIP-11 사양](https://github.com/nostr-protocol/nips/blob/master/11.md)

**언급된 곳:**
- [뉴스레터 #1: NIP 업데이트](/ko/newsletters/2025-12-17-newsletter/#nip-updates)

