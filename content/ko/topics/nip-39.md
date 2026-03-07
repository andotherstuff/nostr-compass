---
title: "NIP-39: 프로필 내 외부 신원"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Identity
---
NIP-39는 사용자가 `i` 태그를 사용하여 Nostr 프로필에 외부 신원 주장을 첨부하는 방법을 정의한다. 이 태그는 Nostr 공개키를 GitHub, Twitter, Mastodon, Telegram 등 외부 플랫폼의 계정에 연결한다.

## 작동 방식

사용자는 kind 10011 이벤트에 `i` 태그로 신원 주장을 게시한다. 각 태그에는 `platform:identity` 값과 클라이언트가 주장을 검증할 수 있는 증명 포인터가 포함된다:

```json
{
  "kind": 10011,
  "tags": [
    ["i", "github:username", "gist-id"],
    ["i", "twitter:handle", "tweet-id"]
  ]
}
```

클라이언트는 플랫폼과 증명 값으로 증명 URL을 재구성한 뒤, 해당 외부 게시물에 사용자의 `npub`이 포함되어 있는지 확인한다. 이를 통해 중앙 검증자 없이도 클라이언트 간에 주장이 이식 가능하게 된다.

## 증명 모델

중요한 점은 NIP-39가 두 신원의 제어를 동시에 증명한다는 것이다: Nostr 키와 외부 계정. 증명의 어느 한 쪽이 사라지면 검증이 약해진다. 삭제된 gist나 트윗이 과거 이벤트를 무효화하지는 않지만, 대부분의 클라이언트가 의존하는 실시간 증명은 제거된다.

또 다른 유용한 구현 포인트는 가져오기 전략이다. 주장이 kind 0 밖에 존재하므로, 클라이언트는 프로필 상세 보기에서만, 팔로우한 사용자에 대해서만, 또는 아예 요청하지 않을지 선택할 수 있다. 이미 부하가 높은 kind 0 경로에 추가 부담을 주는 것을 방지한다.

## 현재 상태

현재 명세 기준으로 신원 주장은 kind 0 메타데이터가 아닌 전용 kind 10011 이벤트에 존재한다. 이 분리는 kind 0 프로필 가져오기를 경량화하려는 광범위한 작업에서 비롯되었다.

---

**주요 출처:**
- [NIP-39: 프로필 내 외부 신원](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - 신원 주장을 kind 0에서 분리

**언급된 뉴스레터:**
- [뉴스레터 #9: NIP 업데이트](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [뉴스레터 #12: Amethyst](/en/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)

**같이 보기:**
- [NIP-05: DNS 기반 검증](/ko/topics/nip-05/)
