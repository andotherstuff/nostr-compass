---
title: "NIP-05 (도메인 검증)"
date: 2026-02-04
description: "NIP-05는 도메인 검증을 통해 Nostr pubkey에 사람이 읽을 수 있는 식별자를 부여합니다."
---

NIP-05는 Nostr 공개 키를 `user@example.com`과 같이 사람이 읽을 수 있는 인터넷 식별자에 매핑합니다. 이를 통해 중앙 기관에 대한 신뢰 없이 도메인 소유권을 통해 신원을 확인할 수 있습니다.

## 작동 방식

사용자는 프로필 메타데이터에 `nip05` 필드를 추가하여 식별자를 주장합니다. 식별자는 `name@domain` 형식을 따릅니다. 클라이언트는 `https://domain/.well-known/nostr.json`을 가져와 해당 이름이 사용자의 pubkey에 매핑되는지 확인하여 주장을 검증합니다.

well-known 경로의 JSON 파일에는 로컬 이름을 16진수 pubkey에 매핑하는 `names` 객체가 포함됩니다:

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

검증에 성공하면 클라이언트는 npub 대신 또는 함께 식별자를 표시할 수 있습니다. 일부 클라이언트는 검증된 식별자에 체크 표시나 다른 표시를 보여줍니다.

## Relay 힌트

`nostr.json` 파일에는 선택적으로 pubkey를 relay URL 배열에 매핑하는 `relays` 객체를 포함할 수 있습니다. 이는 클라이언트가 특정 사용자의 event를 어디서 찾을 수 있는지 발견하는 데 도움이 됩니다.

## 구현

대부분의 주요 클라이언트가 NIP-05 검증을 지원합니다:
- Damus, Amethyst, Primal이 검증된 식별자를 표시
- 많은 relay 서비스가 NIP-05 식별자를 기능으로 제공
- 다양한 무료 및 유료 NIP-05 제공업체 존재

## 주요 출처

- [NIP-05 명세](https://github.com/nostr-protocol/nips/blob/master/05.md)

## 관련 뉴스레터

- [Newsletter #8 (2026-02-04)](/ko/newsletters/2026-02-04-newsletter/) - 16진수 키와 이름에 소문자 요구 PR
