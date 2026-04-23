---
title: "NIP-42: 릴레이에 대한 클라이언트 인증"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42는 클라이언트가 릴레이에 인증하는 방법을 정의합니다. 릴레이는 접근 제어, 남용 방지, 유료 릴레이 서비스 구현을 위해 인증을 요구할 수 있습니다.

## 작동 방식

인증 흐름은 릴레이가 클라이언트에게 `AUTH` 메시지를 보내는 순간 시작됩니다. 이 메시지에는 클라이언트가 서명해야 하는 challenge 문자열이 들어 있습니다. 클라이언트는 challenge를 포함한 kind 22242 인증 이벤트를 만들고 자신의 개인 키로 서명합니다. 릴레이는 서명과 challenge를 검증한 뒤 접근을 허용합니다.

```json
{
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com"],
    ["challenge", "random-challenge-string"]
  ],
  "content": "",
  "pubkey": "<client_pubkey>",
  "created_at": 1736784000,
  "sig": "<signature>"
}
```

challenge는 재전송 공격을 막습니다. 태그 안 릴레이 URL은 같은 서명 이벤트가 서로 다른 릴레이에서 재사용되는 것을 방지합니다.

## 프로토콜 참고사항

인증은 연결 범위에 묶입니다. challenge는 연결이 유지되는 동안, 혹은 릴레이가 새 challenge를 보낼 때까지 유효합니다. 이 서명 이벤트는 ephemeral이며 일반 이벤트처럼 브로드캐스트해서는 안 됩니다.

명세는 기계 판독 가능한 오류 접두사도 정의합니다. `auth-required:`는 클라이언트가 아직 인증하지 않았음을 뜻합니다. `restricted:`는 인증은 했지만 그 pubkey에 요청한 동작을 수행할 권한이 여전히 없다는 뜻입니다.

## 사용 사례

유료 릴레이는 접근을 허용하기 전에 구독자를 검증하기 위해 NIP-42를 사용합니다. 비공개 릴레이는 읽기나 쓰기를 승인된 pubkey로 제한할 때 이를 사용합니다. 또한 릴레이가 IP 주소 대신 인증된 키별로 행동을 추적할 수 있으므로 rate limiting도 더 나아집니다.

[NIP-11](/ko/topics/nip-11/) 메타데이터와 결합하면 클라이언트는 보호된 질의를 시도하기 전에 릴레이가 NIP-42를 지원하는지 발견할 수 있습니다. 실제로는 지원이 아직 고르지 않기 때문에, 클라이언트는 릴레이가 NIP-42를 광고하지만 보호된 이벤트를 잘못 처리하는 경우를 위한 fallback 경로도 필요합니다.

---

**주요 출처:**
- [NIP-42 Specification](https://github.com/nostr-protocol/nips/blob/master/42.md) - Authentication of clients to relays

**언급된 뉴스레터:**
- [Newsletter #6: Relay Information Documents](/ko/newsletters/2026-01-21-newsletter/)
- [Newsletter #9: Marmot Relay Status Testing](/ko/newsletters/2026-02-11-newsletter/)
- [Newsletter #10: Nostr MCP Server](/ko/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Relay AUTH Starts Reaching Real Apps](/en/newsletters/2026-03-11-newsletter/)

**같이 보기:**
- [NIP-11: 릴레이 정보 문서](/ko/topics/nip-11/)
- [NIP-50: 검색 기능](/ko/topics/nip-50/)
