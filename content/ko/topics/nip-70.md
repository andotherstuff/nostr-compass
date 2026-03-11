---
title: "NIP-70: 보호된 이벤트"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - 릴레이
  - 접근 제어
---

NIP-70은 작성자가 단순한 태그 `[["-"]]`로 이벤트를 보호된 것으로 표시하는 방법을 정의한다. 보호된 이벤트는 relay가 이 동작을 지원하기로 선택하고, 인증된 게시자가 이벤트 작성자와 동일한 pubkey임을 검증할 때만 수용될 수 있다.

## 작동 방식

핵심 규칙은 짧다. 이벤트에 `[["-"]]` 태그가 포함되어 있으면 relay는 기본적으로 이를 거부해야 한다. 보호된 이벤트를 지원하려는 relay는 먼저 [NIP-42](/ko/topics/nip-42/) `AUTH` 흐름을 수행하고, 인증한 클라이언트가 자기 자신의 이벤트를 게시하고 있음을 확인해야 한다.

이 때문에 NIP-70은 암호화 규칙이 아니라 게시 권한 규칙이다. 콘텐츠 자체는 여전히 읽을 수 있다. 바뀌는 것은 그 태그를 존중하는 relay에 누가 그 이벤트를 올릴 수 있는가이다. 이를 통해 relay는 반폐쇄형 피드나, 작성자가 제3자의 재게시를 relay가 거부하길 원하는 다른 문맥을 지원할 수 있다.

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

## AUTH 흐름의 의미

보호된 이벤트는 relay가 게시 시점에 작성자 신원을 실제로 강제할 때만 유용하다. 그래서 NIP-70은 [NIP-42](/ko/topics/nip-42/)에 직접 의존한다. 일치하는 auth 검사 없이 `[["-"]]` 이벤트를 받아들이는 relay는 이 태그를 정책이 아니라 장식으로 취급하는 셈이다.

## relay 동작과 한계

NIP-70은 콘텐츠가 영원히 제한된 상태로 남는다고 약속하지 않는다. 수신자는 여전히 본 내용을 복사해 다른 곳에 새 이벤트로 게시할 수 있다. 이 사양이 제공하는 것은 relay가 작성자의 의도를 존중하고 보호된 이벤트의 직접 재게시를 거부할 수 있도록 하는 표준적인 방법뿐이다.

그래서 후속 작업이 중요하다. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251)은 보호된 이벤트를 포함한 repost에도 이 규칙을 확장하여, 원본 이벤트는 보호된 채로 남아 있어도 래퍼 이벤트는 그렇지 않았던 쉬운 우회 경로를 막는다.

## 구현체

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - 보호된 이벤트를 위한 NIP-42 auth 지원 추가
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - 보호된 이벤트를 포함한 repost 거부
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - 보호된 이벤트 처리와 연결된 helper 지원 추가

---

**주요 출처:**
- [NIP-70 Specification](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - NIPs 저장소에 NIP-70 추가
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - 보호된 이벤트를 포함한 repost 거부
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - NIP-42 auth와 보호된 이벤트를 위한 relay 구현

**언급된 뉴스레터:**
- [Newsletter #13: NIP Updates](/ko/newsletters/2026-03-11-newsletter/#nip-updates)
- [Newsletter #13: NIP Deep Dive](/ko/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-70-protected-events)

**같이 보기:**
- [NIP-42: Client Authentication](/ko/topics/nip-42/)
- [NIP-11: Relay Information Document](/ko/topics/nip-11/)
