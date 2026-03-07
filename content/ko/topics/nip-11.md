---
title: "NIP-11: 릴레이 정보 문서"
date: 2025-12-17
translationOf: /en/topics/nip-11.md
translationDate: 2026-03-07
draft: false
categories:
  - Relay
  - Protocol
---
NIP-11은 릴레이가 지원하는 기능, 제한 사항, 운영자 메타데이터를 포함하여 기계가 읽을 수 있는 자기 설명을 게시하는 방법을 정의한다.

## 작동 방식

클라이언트는 릴레이의 WebSocket URL에 `Accept: application/nostr+json` 헤더를 포함한 HTTP GET 요청을 보내 릴레이 정보를 가져온다. 릴레이는 자신의 기능을 설명하는 JSON 문서를 반환한다.

## 주요 필드

- **name** - 사람이 읽을 수 있는 릴레이 이름
- **description** - 릴레이의 용도
- **supported_nips** - 지원을 표명한 NIP 목록
- **limitation** - 최대 메시지 크기, 인증 필요 여부 등의 제한 사항
- **pubkey** - 릴레이 운영자 공개 키 (제공된 경우)
- **contact** - 운영자 연락처

## 신뢰 모델

NIP-11은 자기 보고 메타데이터다. 릴레이가 자신에 대해 말하는 것이지, 실제 트래픽에서 입증된 것이 아니다. 검색과 UX에는 여전히 유용하지만, 클라이언트는 동작을 테스트하지 않고 `supported_nips`를 사실로 받아들여서는 안 된다.

이 구분은 릴레이 선택에 중요하다. 릴레이가 NIP-50 검색, 인증 요구 사항, 대용량 메시지 제한을 광고할 수 있지만, 실제 답은 클라이언트가 연결하여 해당 코드 경로를 실행해야만 나타난다.

## 왜 중요한가

- 클라이언트가 연결 전에 릴레이가 필요한 기능을 지원하는지 확인할 수 있다
- 검색 서비스가 릴레이 기능을 인덱싱할 수 있다
- 사용자가 게시 전에 릴레이 정책을 확인할 수 있다

## 최근 명세 방향

명세는 시간이 지나면서 축소되었다. `software`, `version`, 개인정보 보호 정책 세부사항, 보존 메타데이터 같은 이전의 선택적 필드들은 수년간 채택이 저조하여 제거되었다. 현재 NIP-11 문서는 더 작고 현실적이지만, 클라이언트가 릴레이로부터 풍부한 정책 메타데이터를 기대해서는 안 된다는 것도 의미한다.

---

**주요 출처:**
- [NIP-11 명세](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - 릴레이 identity 필드 업데이트
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - 잘 사용되지 않는 필드 정리
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - 더 이상 사용되지 않는 필드 제거

**언급된 뉴스레터:**
- [Newsletter #1: NIP 업데이트](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**같이 보기:**
- [NIP-66: 릴레이 검색 및 활성 모니터링](/ko/topics/nip-66/)
