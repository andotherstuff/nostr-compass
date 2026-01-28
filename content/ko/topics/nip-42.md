---
title: "NIP-42: 클라이언트의 relay 인증"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42는 클라이언트가 relay에 인증하는 방법을 정의합니다. Relay는 접근 제어를 제공하거나 남용을 방지하거나 유료 relay 서비스를 구현하기 위해 인증을 요구할 수 있습니다.

## 작동 방식

인증 흐름은 relay가 클라이언트에 AUTH 메시지를 보낼 때 시작됩니다. 이 메시지에는 클라이언트가 서명해야 하는 챌린지 문자열이 포함됩니다. 클라이언트는 챌린지가 포함된 kind 22242 인증 event를 생성하고 자신의 개인 키로 서명합니다. Relay는 서명과 챌린지를 검증한 후 접근을 허용합니다.

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

챌린지는 재전송 공격을 방지합니다: 클라이언트는 각 인증 시도에 대해 새로운 챌린지에 서명해야 합니다. 태그의 relay URL은 인증 토큰이 다른 relay에서 재사용될 수 없도록 보장합니다.

## 사용 사례

유료 relay는 NIP-42를 사용하여 접근을 허용하기 전에 구독자를 확인합니다. 인증 후, relay는 결제 상태나 구독 만료를 확인할 수 있습니다. 비공개 relay는 승인된 pubkey로 접근을 제한하여 폐쇄적인 커뮤니티나 개인 relay 인프라를 만듭니다.

인증을 통해 속도 제한이 더 효과적이 됩니다. Relay는 IP 주소 대신 인증된 pubkey별로 요청 속도를 추적하여, 공유 IP 뒤의 정당한 사용자를 지원하면서 남용을 방지할 수 있습니다. Relay가 event 게시에 인증을 요구할 때 스팸 방지가 향상됩니다.

일부 relay는 분석을 위해 NIP-42를 사용하여, 중앙화된 계정 없이 어떤 사용자가 어떤 콘텐츠에 접근하는지 추적합니다. [NIP-11](/ko/topics/nip-11/) 메타데이터와 결합하여, 클라이언트는 연결을 시도하기 전에 relay가 인증을 요구하는지 확인합니다.

---

**주요 출처:**
- [NIP-42 명세](https://github.com/nostr-protocol/nips/blob/master/42.md) - 클라이언트의 relay 인증

**참고:**
- [NIP-11: Relay 정보 문서](/ko/topics/nip-11/)
- [NIP-50: 검색 기능](/ko/topics/nip-50/)
