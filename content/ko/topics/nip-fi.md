---
title: "Buzz NIP-FI: 연합 신원 어서션"
date: 2026-09-30
translationOf: /en/topics/nip-fi.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Identity
  - Relays
---

NIP-FI는 Buzz의 **프로젝트 고유** 연합 신원 어서션 명세다. 이 이름은 `nostr-protocol/nips` 저장소에서 채택되었거나 Buzz 외부의 relay와 상호 운용된다는 뜻이 아니다.

## HTTP 수신 경로 {#http-ingress}

강제 모드에서 보호된 HTTP 요청에 대해 Buzz는 연합 신원 어서션을 NIP-98 서명 인증 event와 짝지어 처리한다. HTTP 서명으로 증명된 Nostr 공개 키는 어서션에 명시된 키와 일치해야 한다. 누락되었거나, 일치하지 않거나, 검증할 수 없는 증거는 거부된다. Buzz는 이 짝짓기를 사용해 외부 신원 발급자의 인가 결정을 요청을 보내는 Nostr 키와 연결한다.

[프로젝트 명세 개정](https://github.com/block/buzz/pull/7254)은 강제 모델을 정의한다. [병합된 HTTP 수신 경로 구현](https://github.com/block/buzz/pull/7264)은 relay 브리지, 미디어, 워크플로, Git 경로를 포함한 Buzz의 보호된 HTTP 표면을 다룬다. 이 병합은 소스 테스트를 보고할 뿐이며, 다른 Nostr relay가 같은 정책을 구현한다는 뜻은 아니다.

---

**주요 출처:**
- [Buzz NIP-FI 명세 개정](https://github.com/block/buzz/pull/7254)
- [Buzz HTTP 수신 경로 구현](https://github.com/block/buzz/pull/7264)

**언급된 뉴스레터:**
- [Newsletter #42: Buzz 신원 제어](/ko/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
