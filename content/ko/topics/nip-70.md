---
title: "NIP-70: 보호된 이벤트"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - Relay
  - 접근 제어
---

NIP-70은 저자가 `[["-"]]` 태그로 이벤트를 보호됨으로 표시하는 방법을 정의합니다. 보호된 이벤트는 relay가 해당 동작을 지원하고 인증된 게시자가 이벤트 저자와 동일한 pubkey인지 확인하는 경우에만 수락될 수 있습니다.

## 작동 방식

핵심 규칙은 간단합니다. 이벤트에 `[["-"]]` 태그가 포함되어 있으면, relay는 기본적으로 이를 거부해야 합니다. 보호된 이벤트를 지원하려는 relay는 먼저 [NIP-42](/ko/topics/nip-42/) `AUTH` 흐름을 실행하고 인증된 클라이언트가 자신의 이벤트를 게시하고 있는지 확인해야 합니다.

이로 인해 NIP-70은 암호화 규칙이 아닌 게시 권한 규칙입니다. 콘텐츠는 여전히 읽을 수 있습니다. 변경되는 것은 태그를 존중하는 relay에 해당 이벤트를 배치할 수 있는 사람입니다. 이를 통해 relay는 저자가 제3자 재게시를 거부하길 원하는 반폐쇄 피드 및 기타 컨텍스트를 지원할 수 있습니다.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

## AUTH 흐름 함의

보호된 이벤트는 relay가 게시 시 저자 신원을 실제로 강제할 때만 유용합니다. 그래서 NIP-70이 [NIP-42](/ko/topics/nip-42/)에 직접적으로 의존합니다. 일치하는 인증 확인 없이 `[["-"]]` 이벤트를 수락하는 relay는 태그를 정책이 아닌 장식으로 취급하는 것입니다.

## Relay 동작 및 제한

NIP-70은 콘텐츠가 영원히 격리될 것을 보장하지 않습니다. 수신자는 여전히 보이는 것을 복사하여 다른 곳에 새 이벤트로 게시할 수 있습니다. 사양은 relay에 저자의 의도를 존중하고 보호된 이벤트의 직접 재게시를 거부하는 표준 방법만 제공합니다.

그래서 후속 작업이 중요합니다. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251)은 보호된 이벤트를 포함하는 리포스트에까지 규칙을 확장하여, 원본 이벤트는 보호되었지만 래퍼 이벤트는 보호되지 않은 쉬운 우회를 차단합니다.

## 구현체

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - 보호된 이벤트를 위한 NIP-42 인증 지원 추가
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - 보호된 이벤트를 포함하는 리포스트 거부
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - 보호된 이벤트 처리 관련 헬퍼 지원 추가

---

**주요 출처:**
- [NIP-70 사양](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - NIP-70을 NIPs 저장소에 추가
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - 보호된 이벤트를 포함하는 리포스트 거부
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - NIP-42 인증 및 보호된 이벤트를 위한 relay 구현

**언급된 곳:**
- [뉴스레터 #13: NIP 업데이트](/en/newsletters/2026-03-11-newsletter/#nip-updates)
- [뉴스레터 #13: NIP 심층 분석](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-70-protected-events)

**같이 보기:**
- [NIP-42: 클라이언트 인증](/ko/topics/nip-42/)
- [NIP-11: Relay 정보 문서](/ko/topics/nip-11/)
