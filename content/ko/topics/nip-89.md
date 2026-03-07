---
title: "NIP-89: 추천 애플리케이션 핸들러"
date: 2026-01-07
translationOf: /en/topics/nip-89.md
translationDate: 2026-03-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---
NIP-89는 애플리케이션이 자신의 기능을 알리는 방법과 사용자가 특정 이벤트 kind를 처리하는 앱을 추천하는 방법을 정의한다.

## 이벤트 종류

- **kind 31990** - 애플리케이션 핸들러 (앱 개발자가 게시)
- **kind 31989** - 앱 추천 (사용자가 게시)

## 작동 방식

1. **애플리케이션**이 지원하는 이벤트 kind와 콘텐츠 열기 방법을 설명하는 핸들러 이벤트를 게시한다
2. **사용자**가 특정 이벤트 kind에 사용하는 앱을 추천한다
3. **클라이언트**가 추천을 조회하여 알 수 없는 이벤트 유형에 대한 "열기..." 기능을 제공한다

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

`k` 태그는 지원되는 이벤트 kind를 지정한다. URL 템플릿은 NIP-19 인코딩된 엔티티의 자리 표시자로 `<bech32>`를 사용한다.

같은 핸들러 이벤트가 라우팅 패턴이 동일한 여러 지원 kind를 알릴 수 있다. 이를 통해 앱 발견을 간결하게 유지하고 목적지 로직이 동일할 때 kind마다 하나의 핸들러 이벤트를 게시하는 것을 피한다.

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

`d` 태그는 추천되는 이벤트 kind이다. 여러 `a` 태그로 다른 플랫폼에 대해 다른 앱을 추천할 수 있다.

## Client 태그

NIP-89는 게시 앱이 일반 이벤트에 첨부할 수 있는 선택적 `client` 태그도 정의한다. 이 태그는 클라이언트 이름과 핸들러 이벤트에 대한 포인터를 기록하여, 다른 클라이언트가 노트의 출처를 표시하거나 더 풍부한 애플리케이션 메타데이터를 조회할 수 있게 한다.

이는 프라이버시 관련 영향이 있다. 명세는 클라이언트가 사용자에게 옵트아웃을 허용해야 한다고 명시한다. 모든 이벤트에 소프트웨어 신원을 게시하면 사람들이 노출하고 싶지 않은 사용 패턴이 드러날 수 있기 때문이다.

## 사용 사례

- 장문 글(kind 30023)을 표시할 수 있는 앱 발견
- 특정 이벤트 유형을 지원하는 클라이언트 찾기
- 클라이언트 간 "열기..." 기능
- 암호화 지원을 위한 클라이언트 기능 감지

## 신뢰 및 안전 참고사항

NIP-89는 상호운용성을 개선하지만, 리디렉트 공격 표면도 생성한다. 클라이언트가 신뢰할 수 없는 릴레이에서 임의의 핸들러 공지를 조회하면 사용자를 악성 또는 오해의 소지가 있는 애플리케이션으로 보낼 수 있다.

이것이 추천 흐름이 팔로우하는 사람들로부터 시작되는 이유다. 소셜 필터링된 추천은 완벽하지 않지만, 모든 게시된 핸들러를 동등하게 신뢰할 수 있는 것으로 취급하는 것보다 안전하다.

---

**주요 출처:**
- [NIP-89 명세](https://github.com/nostr-protocol/nips/blob/master/89.md)

**언급된 뉴스레터:**
- [Newsletter #4: NIP 심층 분석](/en/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Newsletter #12: Damus](/en/newsletters/2026-03-04-newsletter/#damus-nip-89-recommended-application-handlers)

**같이 보기:**
- [NIP-19: Bech32 인코딩 엔티티](/ko/topics/nip-19/)
