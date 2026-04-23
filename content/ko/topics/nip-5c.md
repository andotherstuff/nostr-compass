---
title: "NIP-5C: Scrolls (WASM 프로그램)"
date: 2026-04-08
translationOf: /en/topics/nip-5c.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-5C(이전 이름은 NIP-A5)는 Nostr에서 WebAssembly 프로그램("scrolls")을 게시하고 발견하고 실행하는 규약을 정의합니다. WASM 바이너리는 Nostr 이벤트로 저장되며, 어떤 클라이언트든 이를 가져와 sandboxed runtime에서 실행할 수 있습니다.

## 작동 방식

개발자는 컴파일된 바이너리를 담은 Nostr 이벤트로 WASM 프로그램을 게시합니다. 클라이언트는 표준 Nostr 질의를 통해 이 프로그램을 발견하고, 이벤트에서 WASM 바이너리를 내려받은 뒤 sandboxed WebAssembly runtime에서 실행합니다. 이 sandbox는 scroll이 호스트 시스템에 직접 접근하지 못하게 하며, runtime이 명시적으로 제공한 capability만 사용할 수 있게 제한합니다.

## 사용 사례

- **이식 가능한 compute**: WASM 실행을 지원하는 어느 클라이언트에서나 프로그램 실행
- **탈중앙 앱 배포**: app store 없이 애플리케이션을 게시하고 발견
- **조합 가능한 도구**: 여러 scroll을 연결해 복잡한 워크플로 구성

## 데모

[데모 앱](https://nprogram.netlify.app/)에서 브라우저 안에서 실행되는 scrolls를 볼 수 있으며, 예제 프로그램은 Nostr 이벤트로 게시되어 있습니다.

---

**주요 출처:**
- [NIP-5C PR #2281](https://github.com/nostr-protocol/nips/pull/2281) - Scrolls (WASM Programs) 제안

**언급된 뉴스레터:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)
- [Newsletter #19: NIP-5D applets proposal](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-5D (Web Applets)](/ko/topics/nip-5d/)
- [NIP-5A (정적 웹사이트)](/ko/topics/nip-5a/)
