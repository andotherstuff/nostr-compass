---
title: "NIP-86: Relay 관리 API"
date: 2026-04-01
translationOf: /en/topics/nip-86.md
translationDate: 2026-04-01
draft: false
categories:
  - Relay
  - 프로토콜
---

NIP-86은 relay 관리를 위한 JSON-RPC 인터페이스를 정의하여, 인가된 클라이언트가 표준화된 API를 통해 relay에 관리 명령을 보낼 수 있게 합니다. Relay 운영자는 relay별 도구 없이 pubkey를 차단하거나 허용하고, 접근 목록을 관리하며, relay 상태를 조회할 수 있습니다.

## 작동 방식

관리 API는 relay WebSocket 엔드포인트와 동일한 URI에서 HTTP를 통한 JSON-RPC 형태의 요청을 사용합니다. 요청은 `application/nostr+json+rpc` 콘텐츠 타입을 사용하고 `Authorization` 헤더에 [NIP-98](/ko/topics/nip-98/) (HTTP Auth) 서명된 이벤트로 인증합니다. Relay는 명령을 실행하기 전에 요청하는 pubkey를 관리자 목록과 대조하여 확인합니다.

사용 가능한 메서드에는 pubkey 차단 및 허용, 차단된 사용자 목록 조회, relay 구성 쿼리가 포함됩니다. 표준화된 인터페이스는 단일 클라이언트 구현으로 모든 NIP-86 호환 relay를 관리할 수 있음을 의미합니다.

## 구현체

- [Amethyst](https://github.com/vitorpamplona/amethyst) - NIP-86 relay 관리 UI가 포함된 Android 클라이언트 (v1.07.0+)

---

**주요 출처:**
- [NIP-86 사양](https://github.com/nostr-protocol/nips/blob/master/86.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - 클라이언트 측 NIP-86 지원
- [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) - Relay 관리 사용자 검색 대화상자

**언급된 곳:**
- [뉴스레터 #16: Amethyst relay 관리 출시](/ko/newsletters/2026-04-01-newsletter/#amethyst-ships-pinned-notes-relay-management-and-request-to-vanish)

**같이 보기:**
- [NIP-11: Relay 정보 문서](/ko/topics/nip-11/)
- [NIP-98: HTTP Auth](/ko/topics/nip-98/)
- [NIP-42: 클라이언트의 Relay 인증](/ko/topics/nip-42/)
