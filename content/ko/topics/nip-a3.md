---
title: "NIP-A3: 결제 대상"
date: 2026-09-09
translationOf: /en/topics/nip-a3.md
translationDate: 2026-09-11
draft: false
categories:
  - Protocol
  - Payments
---

NIP-A3는 Nostr 계정이 여러 네트워크와 서비스의 결제 주소를 게시할 수 있는 이식성 있는 방식을 정의합니다. 교체 가능한 kind `10133` 이벤트에는 하나 이상의 `payto` 태그가 포함됩니다.

## 작동 방식

각 태그의 형식은 `["payto", "<type>", "<address>"]`입니다. type은 `bitcoin`, `lightning`, `monero`처럼 소문자로 표기합니다. 클라이언트는 알려진 형식을 검증하고 해당 형식의 네이티브 결제 URI가 있는 경우 이를 표시할 수 있습니다. 알 수 없는 type에는 RFC 8905의 `payto:` URI 스킴을 사용합니다.

이 이벤트는 결제 목적지를 선언하며, 완료된 결제나 Nostr zap을 나타내지는 않습니다. 어떤 결제 type을 지원할지, 주소를 어떻게 검증할지, 지갑으로 넘기기 전에 목적지를 얼마나 명확하게 표시할지는 여전히 클라이언트가 결정합니다.

## 구현

- [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041)는 호환되는 대상을 인식하면 사용자가 선택할 수 있는 결제 전달 기능을 제공합니다.
- [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851)는 허용된 대상 type을 결제 URI에 매핑합니다.
- [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98)는 Monero 대상을 검증하고 작성자의 relay를 조회합니다.

---

**주요 출처:**
- [NIP-A3 명세](https://github.com/nostr-protocol/nips/blob/master/A3.md)
- [RFC 8905: payto URI 스킴](https://www.rfc-editor.org/rfc/rfc8905.html)

**언급된 뉴스레터:**
- [뉴스레터 #39: NIP-A3 결제 대상을 지원하는 클라이언트가 3개로 증가](/ko/newsletters/2026-09-09-newsletter/#nip-a3-payment-targets-reach-three-clients)

**함께 보기:**
- [NIP-47: Nostr Wallet Connect](/ko/topics/nip-47/)
