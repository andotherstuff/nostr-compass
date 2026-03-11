---
title: "NIP-39: 프로필 내 외부 신원"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - 신원
---

NIP-39는 사용자가 `i` 태그를 사용해 Nostr 프로필에 외부 신원 주장을 첨부하는 방법을 정의한다. 이 태그는 Nostr pubkey를 GitHub, Twitter, Mastodon, Telegram 같은 외부 플랫폼 계정과 연결한다.

## 작동 방식

사용자는 kind 10011 이벤트에 `i` 태그로 신원 주장을 게시한다. 각 태그에는 `platform:identity` 값과 함께, 클라이언트가 그 주장을 검증할 수 있게 해주는 증명 포인터가 들어간다.

```json
{
  "id": "5f1c7b7e2c6f3d4a9b0e6a2d8c1f7e3b4a6d9c0e1f2a3b4c5d6e7f8091a2b3c4",
  "pubkey": "3bf0c63fcb8d0d8b6a8fcb3c7f5cb2a972f8a0b5a3d6d8790bb2d4e4f0d6b1c2",
  "created_at": 1741699200,
  "kind": 10011,
  "tags": [
    ["i", "github:alice", "9f5df4e2a8b14c1f9e6d2b7c4a1e8f90"],
    ["i", "twitter:alice_dev", "1898123456789012345"]
  ],
  "content": "",
  "sig": "8f4c62d8a7e9b1c3d5f7091a2b4c6d8e0f1234567890abcdeffedcba09876543211223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

클라이언트는 플랫폼과 증명 값에서 증명 URL을 재구성한 뒤, 해당 외부 게시물에 사용자의 `npub`이 포함되어 있는지 확인한다. 이를 통해 중앙 검증자 없이도 주장을 클라이언트 간에 이식 가능하게 유지할 수 있다.

## 증명 모델

중요한 점은 NIP-39가 두 신원의 통제권을 동시에 증명한다는 것이다. 하나는 Nostr 키이고, 다른 하나는 외부 계정이다. 이 증명의 어느 한쪽이라도 사라지면 검증은 약해진다. 삭제된 gist나 tweet이 과거 이벤트를 무효로 만들지는 않지만, 대부분의 클라이언트가 의존하는 실시간 증명을 없애 버리기는 한다.

또 하나의 유용한 구현 포인트는 가져오기 전략이다. 이제 신원 주장이 kind 0 바깥에 존재하므로, 클라이언트는 프로필 상세 보기에서만 요청할지, 팔로우한 사용자에 대해서만 요청할지, 아니면 아예 요청하지 않을지를 결정할 수 있다. 이렇게 하면 이미 부하가 높은 kind 0 경로에 더 많은 무게를 얹지 않게 된다.

## 구현체

- [Amethyst PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747) - 외부 신원을 전용 kind 10011 이벤트로 게시
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - NIP 세트에 kind 10011 레지스트리 참조를 명시적으로 추가

## 현재 상태

현재 사양 기준으로 신원 주장은 kind 0 메타데이터가 아니라 전용 kind 10011 이벤트에 들어간다. 이런 분리는 kind 0 프로필 가져오기를 더 가볍게 만들려는 더 넓은 작업에서 나왔다.

---

**주요 출처:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - 신원 주장을 kind 0 밖으로 이동
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - kind 10011 참조 명시적 추가

**언급된 뉴스레터:**
- [Newsletter #9: NIP Updates](/ko/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12: Amethyst](/ko/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)
- [Newsletter #13: NIP Updates](/ko/newsletters/2026-03-11-newsletter/#nip-updates)

**같이 보기:**
- [NIP-05: DNS-Based Verification](/ko/topics/nip-05/)
