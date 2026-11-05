---
title: "NIP-73: 외부 콘텐츠 ID"
date: 2026-02-04
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
translationOf: /en/topics/nip-73.md
translationDate: 2026-11-05
---

NIP-73은 Nostr 이벤트 안에서 외부 콘텐츠를 참조하는 표준 방식을 정의합니다. 식별자 자체에는 `i` 태그를, 식별자 유형에는 `k` 태그를 사용합니다. 그래서 클라이언트는 같은 책, 웹사이트, 팟캐스트 에피소드, 위치, 해시태그 또는 블록체인 객체를 중심으로 토론을 묶을 수 있습니다. [현재 명세](https://github.com/nostr-protocol/nips/blob/master/73.md)는 초안(draft)이자 선택 사항(optional)으로 표시되어 있습니다.

## 작동 방식 {#how-it-works}

NIP-73을 사용하는 이벤트에는 정규화된 외부 식별자를 담은 `i` 태그와 식별자 계열을 지정하는 `k` 태그가 들어갑니다. 클라이언트는 릴레이에 `i`로 정확히 하나의 대상을 질의하거나, `k`로 계열 전체를 질의할 수 있습니다. NIP-73은 자체 이벤트 kind를 추가하지 않습니다. 이 태그는 댓글, 리뷰 및 기타 이벤트에 담깁니다.

완전한 이벤트가 아닌 태그 일부:

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

웹페이지의 경우 정규화된 URL을 `i`에 넣고 `k`를 `web`으로 설정합니다. 명세는 다음을 포함한 여러 식별자 계열을 다룹니다.

- 프래그먼트가 없는 정규화된 웹 URL
- 책의 ISBN
- 영화의 ISAN
- DOI
- 지오해시 및 ISO 3166 국가 또는 하위 행정구역 코드
- 팟캐스트 피드, 에피소드, 퍼블리셔 GUID
- 해시태그
- 블록체인 트랜잭션 및 주소 식별자

## 정규화 규칙 {#normalization-rules}

일치 여부는 문자열이 동일한지에 따라 결정되므로, 명세는 계열마다 하나의 표기 형식을 정해 둡니다. 명세에 나온 예는 다음과 같습니다.

- 지오해시는 `geo:<value>`를 사용하며 소문자여야 합니다
- 국가 및 하위 행정구역 코드는 `iso3166:<code>`를 사용하며 대문자여야 합니다
- ISBN은 하이픈을 생략합니다
- DOI는 소문자로 씁니다
- 웹 URL에서는 프래그먼트를 제거합니다
- 블록체인 트랜잭션 해시는 소문자 16진수를 사용합니다

정규화는 하나의 식별자를 어떻게 표기할지를 고정할 뿐, 별칭을 병합하지는 않습니다. 판(edition)별 ISBN이나 서로 다른 문자열로 정규화되는 URL은 별개의 식별자로 남습니다. 따라서 책 한 권이나 글 한 편에 대한 토론이 여전히 여러 `i` 값에 흩어질 수 있습니다.

## URL 힌트 {#url-hints}

`i` 태그에는 세 번째 배열 요소로 선택적 URL 힌트를 넣을 수 있습니다. 이는 태그 이름 다음에 오는 두 번째 값입니다. 해당 식별자 유형을 위한 전용 렌더러가 없는 클라이언트는 이 힌트를 대체 링크로 사용할 수 있습니다.

태그 일부: `["i", "isbn:9780765382030", "<url-hint>"]`

힌트는 작성자가 고릅니다. 힌트는 식별자의 일부가 아니며, 소유권을 증명하지도 않고, 정식(canonical) 사이트를 지정하지도 않습니다.

## 신뢰와 맥락 {#trust-and-context}

식별자가 같은 두 이벤트는 같은 대화에 묶이며, 공유된 식별자가 확립하는 것은 그것뿐입니다. 서명된 이벤트는 그 작성자를 식별합니다. 하지만 이벤트가 참조하는 책, 사이트 또는 팟캐스트 퍼블리셔를 인증하지 않으며, 누가 그것을 관리하는지도 보여 주지 않습니다.

`i` 태그의 의미는 이벤트에 따라 달라집니다. [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) 댓글에서는 대문자 `I`/`K`가 루트 범위를, 소문자 `i`/`k`가 부모를 나타냅니다. 이 스레드 구조는 NIP-22에서 정의한 것이며, NIP-73은 댓글 kind를 정의하지 않습니다. [NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md)는 프로필의 외부 신원에 `i`를 사용하므로, 모든 `i` 태그가 NIP-73 대상인 것은 아닙니다.

[NIP-85](/ko/topics/nip-85/) 신뢰 주장(Trusted Assertions)도 책, 웹사이트, 해시태그, 위치 같은 NIP-73 식별자를 대상으로 삼을 수 있습니다.

## 구현 {#implementations}

rust-nostr의 [커밋 4c8099a 시점 nip73.rs](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)는 알려진 접두사를 파싱해 타입이 지정된 `ExternalContentId`로 만들고, 선택적 힌트를 타입이 지정된 URL로 변환합니다. 세 번째 태그 요소는 힌트가 있을 때만 기록합니다. 테스트에서는 하이픈이 들어간 ISBN이 그대로 유지됩니다. 파서가 접두사를 떼어 낸 뒤 나머지를 명세의 정규화 없이 저장하기 때문에, 타입 기반 파싱이 정식 문자열을 보장하지는 않습니다. 체인 ID는 계열에서 제외하여 `ethereum:100:tx:<hash>`를 `ethereum:tx`로 매핑합니다. 이 리비전에는 `iso3166` 국가 변형이 없습니다.

Amethyst의 [커밋 553f761 시점 DisplayExternalId.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)는 지오해시, 해시태그, URL 식별자를 각각의 전용 표시 화면으로 넘기고, 그 밖에 지원하는 유형은 일반 범위 칩으로 표시합니다. URL을 누르면 해당 페이지에 대한 앱 자체의 스레드 경로가 열립니다. 미리보기가 꺼져 있으면 일반 렌더링은 단순 링크 칩을 표시하며 미리보기를 요청하지 않습니다. 미리보기가 켜져 있으면 없는 미리보기를 가져오는 과정에서 대상 사이트에 접속할 수 있습니다. 두 파일 모두 출시된 버전이 어떻게 동작하는지는 보여 주지 않습니다.

---

**주요 출처:**
- [NIP-73 명세](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - ISO 3166 국가 및 하위 행정구역 코드 추가
- [커밋 4c8099a 시점 rust-nostr nip73.rs](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)
- [커밋 553f761 시점 Amethyst DisplayExternalId.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)

**언급된 곳:**
- [뉴스레터 #47: NIP 심층 분석](/ko/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)
- [뉴스레터 #45](/en/newsletters/2026-10-21-newsletter/#feather)
- [뉴스레터 #43](/en/newsletters/2026-10-07-newsletter/#protocol-and-spec-work)
- [뉴스레터 #37: 2025년 8월](/en/newsletters/2026-08-26-newsletter/#august-2025)
- [뉴스레터 #8: NIP 업데이트](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [뉴스레터 #10: NIP-85 심층 분석](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [뉴스레터 #36: 댓글 (NIP-22)](/en/newsletters/2026-08-19-newsletter/#comments-nip-22)
- [뉴스레터 #38: NIP 심층 분석](/en/newsletters/2026-09-02-newsletter/#reactions-nip-25)
- [뉴스레터 #40: NIP-73 팟캐스트 미디엄 필터](/en/newsletters/2026-09-16-newsletter/#nip-73-proposes-podcast-medium-filters)
- [뉴스레터 #42: 2024년 9월 외부 콘텐츠](/en/newsletters/2026-09-30-newsletter/#september-2024-posts-acquire-richer-context)

**함께 보기:**
- [NIP-31: 알 수 없는 이벤트 kind 처리](/ko/topics/nip-31/)
- [NIP-22: 댓글](/ko/topics/nip-22/)
- [NIP-39: 프로필의 외부 신원](/ko/topics/nip-39/)
- [NIP-85: 신뢰 주장](/ko/topics/nip-85/)
