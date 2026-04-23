---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
translationOf: /en/topics/nip-46.md
translationDate: 2026-04-22
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46은 Nostr 릴레이를 통한 원격 서명을 정의합니다. 클라이언트는 흔히 bunker라고 불리는 별도 signer와 통신하므로, 서명 키를 사용자가 현재 쓰고 있는 앱 밖에 둘 수 있습니다.

## 작동 방식

1. 클라이언트는 bunker 세션에만 쓰이는 로컬 키페어를 생성합니다.
2. 연결은 `bunker://` 또는 `nostrconnect://` URI로 수립됩니다.
3. 클라이언트와 signer는 릴레이를 통해 암호화된 kind `24133` 요청 및 응답 이벤트를 교환합니다.
4. 연결 후 클라이언트는 `get_public_key`를 호출해 실제로 서명 대상인 사용자 pubkey를 알아냅니다.

## 연결 방식

- **bunker://** - signer가 시작하는 연결
- **nostrconnect://** - QR 코드나 deep link를 통한 클라이언트 시작 연결

`nostrconnect://` 흐름에는 필수 공유 비밀이 포함되어 있으므로, 클라이언트는 첫 응답이 정말 의도한 signer에게서 왔는지 검증할 수 있습니다. 이것은 단순한 연결 spoofing을 막아 줍니다.

## 지원 작업

- `sign_event` - 임의 이벤트 서명
- `get_public_key` - signer에서 사용자 pubkey 조회
- `nip04_encrypt/decrypt` - NIP-04 암호화 작업
- `nip44_encrypt/decrypt` - NIP-44 암호화 작업
- `switch_relays` - signer에게 갱신된 relay 집합 요청

많은 구현체는 설정 과정에서 `sign_event:1`이나 `nip44_encrypt` 같은 permission string도 사용해 signer가 전체 접근 대신 좁은 범위만 승인할 수 있게 합니다.

## 릴레이와 신뢰 모델

NIP-46은 개인 키를 클라이언트 밖으로 옮기지만 signer에 대한 신뢰 자체를 제거하지는 않습니다. signer는 요청을 승인하거나 거부하거나 지연시킬 수 있고, 클라이언트가 수행해 달라고 요청하는 모든 작업을 볼 수 있습니다. 양쪽이 모두 접근 가능한 릴레이를 통해 요청과 응답이 전달되므로 relay 선택도 중요합니다.

`switch_relays` 메서드는 signer가 시간이 지나며 세션을 다른 relay 집합으로 옮길 수 있게 하기 위해 존재합니다. 이를 무시하는 클라이언트는 signer의 relay 선호가 바뀔 때 안정성이 떨어집니다.

---

**주요 출처:**
- [NIP-46 Specification](https://github.com/nostr-protocol/nips/blob/master/46.md)

**언급된 뉴스레터:**
- [Newsletter #1: Notable Code Changes](/ko/newsletters/2025-12-17-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #4: Primal Android Becomes a Full Signing Hub](/ko/newsletters/2026-01-07-newsletter/)
- [Newsletter #12: NDK Collaborative Events and NIP-46 Timeout](/ko/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: NipLock signer support](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Forgesworn Heartwood signer](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Flotilla Aegis NIP-46 login](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-55: Android Signer](/ko/topics/nip-55/)
