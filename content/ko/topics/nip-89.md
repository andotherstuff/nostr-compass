---
title: "NIP-89: 권장 애플리케이션 핸들러"
date: 2026-01-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89는 애플리케이션이 자신의 기능을 알리는 방법과 사용자가 특정 이벤트 종류를 처리하는 앱을 추천하는 방법을 정의합니다.

## 이벤트 종류

- **kind 31990** - 애플리케이션 핸들러(앱 개발자가 게시)
- **kind 31989** - 앱 추천(사용자가 게시)

## 작동 방식

1. **애플리케이션**이 지원하는 이벤트 종류와 콘텐츠를 여는 방법을 설명하는 핸들러 이벤트를 게시합니다
2. **사용자**가 특정 이벤트 종류에 사용하는 앱을 추천합니다
3. **클라이언트**가 추천을 쿼리하여 알 수 없는 이벤트 유형에 대해 "다음에서 열기..." 기능을 제공합니다

## 애플리케이션 핸들러

```json
{
  "id": "<event-id>",
  "pubkey": "<app-developer-pubkey>",
  "created_at": 1736200000,
  "kind": 31990,
  "tags": [
    ["d", "<app-identifier>"],
    ["k", "30023"],
    ["web", "https://app.example.com/a/<bech32>", "naddr"],
    ["ios", "appname://open/<bech32>"]
  ],
  "content": "{\"name\": \"My App\", \"picture\": \"...\"}",
  "sig": "<signature>"
}
```

`k` 태그는 지원되는 이벤트 종류를 지정합니다. URL 템플릿은 NIP-19로 인코딩된 엔티티의 플레이스홀더로 `<bech32>`를 사용합니다.

## 사용자 추천

```json
{
  "id": "<event-id>",
  "pubkey": "<user-pubkey>",
  "created_at": 1736200000,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:app-pubkey:identifier", "wss://relay", "web"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

`d` 태그는 추천되는 이벤트 종류입니다. 여러 `a` 태그로 다른 플랫폼에 대해 다른 앱을 추천할 수 있습니다.

## 사용 사례

- 장문 기사(kind 30023)를 표시할 수 있는 앱 발견
- 특정 이벤트 유형을 지원하는 클라이언트 찾기
- 크로스 클라이언트 "다음에서 열기..." 기능
- 암호화 지원을 위한 클라이언트 기능 감지

---

**주요 자료:**
- [NIP-89 명세](https://github.com/nostr-protocol/nips/blob/master/89.md)

**언급된 곳:**
- [뉴스레터 #4: NIP 심층 분석](/ko/newsletters/2026-01-07-newsletter/#nip-44-버전-관리-암호화)

**관련 항목:**
- [NIP-19: Bech32 인코딩 엔티티](/ko/topics/nip-19/)
