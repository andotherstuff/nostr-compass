---
title: "NIP-37: Draft Wraps"
date: 2026-07-01
draft: false
translationOf: /en/topics/nip-37.md
translationDate: 2026-07-01
categories:
  - NIP
  - Drafts
  - Privacy
---

NIP-37은 모든 kind의 서명되지 않은 draft 이벤트에 대한 암호화된 저장 이벤트를 정의한다. 장문의 기사, 다가오는 캘린더 이벤트, 또는 나중에 보낼 수도 있는 메시지를 작성하는 사용자는 draft를 kind `31234` 이벤트 아래 [NIP-44](/ko/topics/nip-44/)로 자신의 키로 암호화하여 relay에 저장할 수 있다. draft는 사용자의 키를 보유한 모든 클라이언트에서 복구 가능하며, 동일한 NIP는 사용자가 개인 draft를 저장하고자 하는 relay를 명명하는 별도의 `kind:10013` 목록 이벤트를 정의한다.

## 작동 방식

draft wrap은 kind `31234`의 매개변수화된 대체 가능 이벤트이다. 서명되지 않은 draft 이벤트는 JSON으로 문자열화되고, 서명자 자신의 공개 키에 NIP-44로 암호화되어 `.content`에 배치된다. `k` tag는 draft의 kind를 선언하여 클라이언트가 이벤트 유형별로 draft를 그룹화할 수 있도록 한다. `d` tag는 draft가 발전함에 따라 wrap을 대체할 수 있도록 draft 식별자를 담고, 오래된 draft가 자동으로 만료되도록 NIP-40 `expiration` tag가 권장된다.

```json
{
  "kind": 31234,
  "tags": [
    ["d", "<identifier>"],
    ["k", "<kind of the draft event>"],
    ["expiration", "<unix-timestamp>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

비워진 `.content` 필드는 draft가 삭제되었음을 나타낸다.

## Checkpoints

kind `1234`는 부모 `kind:31234` 이벤트에 속하는 체크포인트를 정의한다. 체크포인트는 부모 draft를 가리키는 `a` tag를 담으며, 클라이언트가 최신 draft와 함께 개정 이력을 저장할 수 있도록 한다.

```json
{
  "kind": 1234,
  "tags": [
    ["a", "31234:<pubkey>:<identifier>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

## 개인 콘텐츠용 Relay 목록 (kind 10013)

kind `10013`은 tag에 사용자가 draft wrap을 포함하여 개인 콘텐츠를 저장하고자 하는 relay를 나열하는 대체 가능 이벤트이다. kind `31234`를 게시하는 클라이언트는 사용자의 kind `10013` 이벤트에 나열된 relay에 게시해야 한다(SHOULD). 이는 공개 게시에 사용되는 relay 세트(NIP-65)를 개인 콘텐츠 저장에 사용되는 relay 세트와 분리하므로, 사용자는 공개 outbox에 해당 세트를 노출하지 않고도 신뢰할 수 있는 소수의 relay에 개인 draft를 고정할 수 있다.

## 구현

- [Notedeck](https://github.com/damus-io/notedeck) - kind-10013 목록으로 private-sync relay를 저장 (2026-06 추가)

---

**주요 출처:**
- [NIP-37 명세](https://github.com/nostr-protocol/nips/blob/master/37.md)
- [Notedeck의 private-sync relay를 kind-10013으로 저장하는 커밋](https://github.com/damus-io/notedeck) - Damus 팀이 데스크톱 sync relay 관리를 위해 spec 채택

**언급된 곳:**
- [Newsletter #29: Notedeck](/ko/newsletters/2026-07-01-newsletter/#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments)

**참고:**
- [NIP-44: Versioned Encryption](/ko/topics/nip-44/)
- [NIP-65: Relay List Metadata](/ko/topics/nip-65/)
