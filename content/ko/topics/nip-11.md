---
title: "NIP-11: 릴레이 정보 문서"
date: 2025-12-17
translationOf: /en/topics/nip-11.md
translationDate: 2026-04-22
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11은 릴레이가 자신에 대한 기계 판독 가능한 설명을 게시하는 방법을 정의합니다. 여기에는 릴레이가 주장하는 기능 지원, 제한, 운영자 메타데이터가 포함됩니다.

## 작동 방식

클라이언트는 릴레이의 WebSocket URL에 `Accept: application/nostr+json` 헤더를 포함한 HTTP GET 요청을 보내 릴레이 정보를 가져옵니다. 릴레이는 자신의 기능을 설명하는 JSON 문서를 반환합니다.

## 유용한 필드

- **name** - 사람이 읽을 수 있는 릴레이 이름
- **description** - 릴레이의 용도
- **supported_nips** - 지원한다고 주장하는 NIP 목록
- **limitation** - 최대 메시지 크기, 인증 요구 여부 같은 제한
- **pubkey** - 제공된 경우 릴레이 운영자 공개키
- **contact** - 운영자 연락처

## 신뢰 모델

NIP-11은 자기 보고형 메타데이터입니다. 이것은 릴레이가 자기 자신에 대해 무엇을 말하는지 보여 줄 뿐, 실제 트래픽에서 무엇이 증명되었는지를 보여 주지는 않습니다. 그래도 탐색과 UX에는 유용하지만, 클라이언트는 동작 테스트 없이 `supported_nips`를 사실로 받아들여서는 안 됩니다.

이 구분은 릴레이 선택에서 중요합니다. 릴레이는 NIP-50 검색, 인증 요구 사항, 큰 메시지 한도를 광고할 수 있지만, 실제 답은 클라이언트가 연결해서 해당 코드 경로를 실행해 볼 때에만 드러납니다.

## 왜 중요한가

- 클라이언트가 연결 전에 필요한 기능 지원 여부를 확인할 수 있음
- 탐색 서비스가 릴레이 capability를 인덱싱할 수 있음
- 사용자가 게시 전에 릴레이 정책을 볼 수 있음

## 최근 명세 방향

이 명세는 시간이 지나며 더 간결해졌습니다. `software`, `version`, privacy policy 세부 정보, retention 메타데이터 같은 오래된 선택 필드는 채택률이 낮아 제거되었습니다. 그 결과 현재의 NIP-11 문서는 더 작고 현실적이지만, 클라이언트는 릴레이가 풍부한 정책 메타데이터를 제공할 것이라고 기대해서는 안 됩니다.

[PR #2318](https://github.com/nostr-protocol/nips/pull/2318)은 릴레이 정보 문서에 선택적인 `access_control` 객체를 추가하는 제안입니다. 이 객체는 릴레이의 게이팅 방식(open, invite, payment, allowlist)과 접근 요청에 사용할 수 있는 endpoint를 나열합니다. 이 필드는 참고용이며, 클라이언트와 디렉터리가 gated relay를 공개 탐색 목록에서 걸러 내고 사용자가 왜 해당 릴레이가 쓰기를 거부하는지 미리 볼 수 있게 하기 위한 것입니다.

## 구현체

- [nostream PR #557](https://github.com/Cameri/nostream/pull/557) - nostream을 현재 명세와 완전히 맞는 NIP-11 relay info parity 상태로 끌어올림

---

**주요 출처:**
- [NIP-11 명세](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - relay identity 필드 업데이트
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - 잘 쓰이지 않는 필드 정리
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - deprecated 필드 제거
- [PR #2318](https://github.com/nostr-protocol/nips/pull/2318) - gated-relay discovery를 위한 `access_control` 필드
- [nostream PR #557](https://github.com/Cameri/nostream/pull/557) - Complete NIP-11 relay info parity

**언급된 뉴스레터:**
- [Newsletter #1: NIP Updates](/ko/newsletters/2025-12-17-newsletter/)
- [Newsletter #13: NIP Updates](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: NIP Updates (`access_control` proposal)](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-66: 릴레이 탐색과 활성 모니터링](/ko/topics/nip-66/)
