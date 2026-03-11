---
title: "NIP-42: 릴레이에 대한 클라이언트 인증"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Authentication
---
NIP-42는 클라이언트가 릴레이에 인증하는 방법을 정의한다. 릴레이는 접근 제어, 남용 방지, 유료 릴레이 서비스 구현을 위해 인증을 요구할 수 있다.

## 작동 방식

인증 흐름은 릴레이가 클라이언트에 `AUTH` 메시지를 보내는 것으로 시작된다. 이 메시지에는 클라이언트가 서명해야 하는 챌린지 문자열이 포함된다. 클라이언트는 챌린지를 포함한 kind 22242 인증 이벤트를 생성하고 개인키로 서명한다. 릴레이는 서명과 챌린지를 검증한 뒤 접근을 허용한다.

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

챌린지는 재전송 공격을 방지한다. 태그의 릴레이 URL은 동일한 서명 이벤트가 다른 릴레이에서 재사용되는 것을 막는다.

## 프로토콜 참고사항

인증은 연결 범위에 한정된다. 챌린지는 연결이 유지되는 동안 유효하며, 릴레이가 새 챌린지를 보내면 갱신된다. 서명된 이벤트는 일시적이며 일반 이벤트로 브로드캐스트해서는 안 된다.

명세는 기계 판독 가능한 오류 접두사도 정의한다. `auth-required:`는 클라이언트가 아직 인증하지 않았다는 의미이고, `restricted:`는 인증은 했지만 해당 공개키가 요청한 작업에 대한 권한이 없다는 의미이다.

## 활용 사례

유료 릴레이는 NIP-42를 사용해 접근 허용 전에 구독자를 확인한다. 비공개 릴레이는 승인된 공개키로 읽기 또는 쓰기를 제한한다. 릴레이가 IP 주소 대신 인증된 키별로 행동을 추적할 수 있어 속도 제한도 개선된다.

[NIP-11](/ko/topics/nip-11/) 메타데이터와 결합하면 클라이언트가 보호된 쿼리를 시도하기 전에 릴레이가 NIP-42를 지원하는지 확인할 수 있다. 실제로는 지원이 아직 균일하지 않아, 릴레이가 NIP-42를 표방하면서도 보호된 이벤트를 올바르게 처리하지 못할 때를 위한 대체 경로가 필요하다.

---

**주요 출처:**
- [NIP-42 명세](https://github.com/nostr-protocol/nips/blob/master/42.md) - 릴레이에 대한 클라이언트 인증

**언급된 뉴스레터:**
- [뉴스레터 #6: 릴레이 정보 문서](/en/newsletters/2026-01-21-newsletter/#relay-information-documents-get-formalized)
- [뉴스레터 #9: Marmot 릴레이 상태 테스트](/en/newsletters/2026-02-11-newsletter/#nip-70-relay-support-critical-for-encrypted-messaging-security)
- [뉴스레터 #10: Nostr MCP Server](/en/newsletters/2026-02-18-newsletter/#nostr-mcp-server)

**같이 보기:**
- [NIP-11: 릴레이 정보 문서](/ko/topics/nip-11/)
- [NIP-50: 검색 기능](/ko/topics/nip-50/)
