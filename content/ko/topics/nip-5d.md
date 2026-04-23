---
title: "NIP-5D: Nostr Web Applets"
date: 2026-04-08
translationOf: /en/topics/nip-5d.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-5D는 iframe 안에서 실행되는 sandboxed 웹 애플리케이션("napplets")이 호스팅 애플리케이션("shell")과 통신하기 위한 `postMessage` 프로토콜을 정의합니다. 이는 [NIP-5A](/ko/topics/nip-5a/) (정적 웹사이트)에 런타임 통신 계층을 더해, 웹 앱이 사용자의 개인 키를 노출하지 않고도 Nostr 기능을 사용할 수 있게 확장합니다.

## 작동 방식

shell 애플리케이션은 sandboxed iframe 안에 napplet을 로드합니다. napplet은 브라우저의 `postMessage` API를 통해 구조화된 메시지 프로토콜로 shell과 통신합니다. shell은 이 메시지 채널을 통해 napplet에 Nostr signing, relay access, 사용자 컨텍스트를 제공합니다. iframe sandbox는 napplet이 사용자의 개인 키에 직접 접근하지 못하게 하므로, shell이 모든 Nostr 작업의 게이트키퍼 역할을 합니다.

## 사용 사례

- **상호작용하는 Nostr 앱**: 사용자가 `nsec`를 붙여넣지 않고도 Nostr 이벤트를 읽고 쓰는 앱 구축
- **앱 마켓플레이스**: 상호작용 웹 앱을 Nostr 이벤트로 배포
- **sandboxed 확장**: 서드파티 napplet을 통해 Nostr 클라이언트에 기능 추가

---

**주요 출처:**
- [NIP-5D PR #2303](https://github.com/nostr-protocol/nips/pull/2303) - Nostr Web Applets 제안

**언급된 뉴스레터:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)
- [Newsletter #19: NIP Updates](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-5A (정적 웹사이트)](/ko/topics/nip-5a/)
- [NIP-5C (Scrolls)](/ko/topics/nip-5c/)
