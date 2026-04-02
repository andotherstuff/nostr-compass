---
title: "NIP-98: HTTP Auth"
date: 2026-03-25
translationOf: /en/topics/nip-98.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - 인증
---

NIP-98은 Nostr 이벤트를 사용한 HTTP 인증을 정의합니다. 비밀번호, API 키 또는 OAuth 흐름 없이 서버가 표준 HTTP 요청에서 클라이언트의 Nostr 신원을 확인할 수 있게 합니다.

## 작동 방식

클라이언트가 HTTP 요청을 인증해야 할 때, kind 27235 이벤트를 생성합니다. 이 이벤트는 태그에 대상 URL과 HTTP 메서드를 포함하여 인증을 특정 요청에 바인딩합니다.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1742860800,
  "kind": 27235,
  "tags": [
    ["u", "https://files.example.com/upload"],
    ["method", "POST"],
    ["payload", "<sha256-hash-of-request-body>"]
  ],
  "content": "",
  "sig": "<128-char hex>"
}
```

클라이언트는 이 이벤트에 서명하고, base64로 인코딩한 뒤, `Nostr` 스킴과 함께 HTTP `Authorization` 헤더에 넣어 전송합니다:

```
Authorization: Nostr <base64-encoded-signed-event>
```

서버는 이벤트를 디코딩하고, 서명을 확인하며, URL과 메서드가 실제 요청과 일치하는지 확인하고, 타임스탬프가 최근인지 확인합니다. 모든 확인이 통과하면 서버는 어떤 Nostr pubkey가 요청을 보냈는지 알 수 있습니다.

선택적 `payload` 태그는 요청 본문의 SHA-256 해시를 포함하여, 인증 이벤트가 다른 콘텐츠와 함께 재사용되는 것을 방지합니다. 타임스탬프 확인(서버는 보통 몇 분 이상 된 이벤트를 거부)은 재생 공격을 방지합니다.

## 사용 사례

Blossom 서버는 NIP-98을 사용하여 파일 업로드와 삭제를 인증하며, 저장된 미디어를 특정 Nostr 신원에 연결합니다. 파일 호스팅 서비스는 pubkey별 업로드 할당량을 강제하는 데 사용합니다. 자체 계정 시스템을 유지하지 않고 Nostr 사용자를 식별해야 하는 모든 HTTP API는 NIP-98 헤더를 신원 증명으로 수락할 수 있습니다.

---

**주요 출처:**
- [NIP-98 사양](https://github.com/nostr-protocol/nips/blob/master/98.md) - HTTP Auth

**언급된 곳:**
- [뉴스레터 #15](/ko/newsletters/2026-03-25-newsletter/)
