---
title: "NIP-21: nostr: URI 스킴"
date: 2026-04-22
translationOf: /en/topics/nip-21.md
translationDate: 2026-04-23
draft: false
categories:
  - Protocol
  - Interoperability
---

NIP-21은 `nostr:` URI 스킴을 정의합니다. 이를 통해 애플리케이션, 웹사이트, 운영체제가 `npub`, `nprofile`, `nevent`, `naddr` 같은 Nostr 식별자를 열 때, 사용자가 핸들러로 등록한 Nostr 클라이언트로 연결할 수 있습니다.

## 작동 방식

`nostr:` URI는 스킴 접두사 뒤에 [NIP-19](/ko/topics/nip-19/)의 bech32 식별자 중 `nsec`를 제외한 값을 붙이는 형식입니다. 클라이언트와 운영체제는 이 스킴을 `mailto:`나 `tel:`과 같은 방식으로 처리합니다. 사용자가 어떤 앱을 핸들러로 등록하면 시스템 어디에서든 `nostr:` 링크를 클릭했을 때 원하는 Nostr 클라이언트에서 열 수 있습니다.

명세의 예시는 다음과 같습니다:

- `nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9` 는 사용자 프로필을 가리킵니다
- `nostr:nprofile1...` 는 relay 힌트가 포함된 사용자 프로필을 가리킵니다
- `nostr:nevent1...` 는 relay 힌트가 포함된 특정 event를 가리킵니다
- `nostr:naddr1...` 는 매개변수화된 교체 가능 event(예: 장문 글)를 가리킵니다

## HTML 페이지를 Nostr 엔티티에 연결하기

NIP-21은 Nostr 엔티티와 대응되는 웹 페이지를 위한 두 가지 유용한 `<link>` 규약도 정의합니다. Nostr event와 같은 콘텐츠를 제공하는 페이지(예: [NIP-23](/ko/topics/nip-23/) `kind:30023` 글을 렌더링한 블로그 포스트)는 Nostr URI를 가리키는 `<link rel="alternate">`를 포함할 수 있습니다. 프로필 페이지는 Nostr 기반 작성자임을 나타내기 위해 `nprofile`을 가리키는 `<link rel="me">` 또는 `<link rel="author">`를 포함할 수 있습니다.

## 왜 중요한가

이 스킴은 어떤 Nostr 식별자든 단일 클라이언트 UI 밖에서 실제로 동작하는 링크로 만들 수 있는 상호운용성 계층입니다. 브라우저 확장, 모바일 OS 핸들러, 데스크톱 셸이 모두 `nostr:` URI를 사용자가 설치한 클라이언트로 라우팅할 수 있으므로, 어디에 URI를 붙여 넣더라도 Nostr 네이티브 방식으로 프로필이나 event를 열 수 있습니다.

## 구현체

`nostr:` URI 지원은 주요 웹, 모바일, 데스크톱 Nostr 클라이언트 전반에 널리 퍼져 있습니다. [nos2x](https://github.com/fiatjaf/nos2x)와 [Alby](https://github.com/getAlby/lightning-browser-extension) 같은 브라우저 확장은 데스크톱 브라우저에서 URI 등록을 처리합니다.

---

**주요 출처:**

- [NIP-21 명세](https://github.com/nostr-protocol/nips/blob/master/21.md)

**언급된 뉴스레터:**

- [뉴스레터 #19: Nostrability migrates to NIP-34](/en/newsletters/2026-04-22-newsletter/#nostrability-migrates-to-nip-34-and-opens-19-per-nip-interop-trackers)

**같이 보기:**

- [NIP-19: bech32 인코딩 엔티티](/ko/topics/nip-19/)
- [NIP-23: 장문 콘텐츠](/ko/topics/nip-23/)
