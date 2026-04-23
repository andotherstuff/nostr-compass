---
title: "NIP-AC: P2P 음성 및 영상 통화"
date: 2026-04-08
translationOf: /en/topics/nip-ac.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Messaging
---

NIP-AC는 Nostr 위에서 peer-to-peer 음성 및 영상 통화를 위한 프로토콜을 제안합니다. 이 명세는 통화 signaling(offer, answer, ICE candidate)에는 Nostr 이벤트를 사용하고, 실제 미디어 전송에는 WebRTC를 사용해 통화 설정은 탈중앙으로 유지하면서 오디오와 비디오에는 표준 브라우저 API를 활용합니다.

## 작동 방식

발신자는 WebRTC Session Description Protocol (SDP) offer를 담은 통화 offer 이벤트를 게시하고, 여기에 수신자의 pubkey를 태그합니다. 수신자는 SDP answer 이벤트로 응답합니다. 양쪽은 네트워크 경로를 협상하기 위해 ICE candidate 이벤트를 교환합니다. WebRTC 연결이 성립되면 미디어는 릴레이를 거치지 않고 피어 사이를 직접 흐릅니다.

signaling 이벤트는 암호화되므로 릴레이는 누가 누구에게 전화를 거는지 관찰할 수 없습니다. call state machine은 offer, answer, reject, busy, hangup 전이를 처리합니다.

## 구현체

- [Amethyst](https://github.com/vitorpamplona/amethyst)는 call state machine 테스트 스위트와 오래된 call offer 처리 로직을 포함해 NIP-AC 지원을 구축 중입니다.

---

**주요 출처:**
- [NIP-AC PR #2301](https://github.com/nostr-protocol/nips/pull/2301) - P2P Voice and Video Calls over WebRTC

**언급된 뉴스레터:**
- [Nostr Compass #17 (2026-04-08)](/ko/newsletters/2026-04-08-newsletter/)
- [Nostr Compass #18 (2026-04-15)](/ko/newsletters/2026-04-15-newsletter/)

**같이 보기:**
- [NIP-44 (암호화 페이로드)](/ko/topics/nip-44/)
