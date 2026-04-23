---
title: "NIP-01: 기본 프로토콜"
date: 2025-12-17
translationOf: /en/topics/nip-01.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
---

NIP-01은 Nostr의 나머지 부분이 기반으로 삼는 기본 이벤트 모델과 릴레이 프로토콜을 정의합니다. 클라이언트, 릴레이, 라이브러리 가운데 무엇이든 Nostr를 사용한다면 여기서 시작합니다.

## 작동 방식

이벤트는 Nostr의 유일한 객체 유형입니다. 프로필, 노트, 반응, 릴레이 목록, 그리고 다양한 애플리케이션별 payload가 모두 같은 7개 필드 envelope를 사용합니다:

- **id**: 직렬화된 이벤트의 SHA256 해시 (고유 식별자)
- **pubkey**: 생성자의 공개키 (32-byte hex, secp256k1)
- **created_at**: Unix timestamp
- **kind**: 이벤트 유형을 분류하는 정수
- **tags**: 메타데이터를 위한 배열의 배열
- **content**: payload (해석은 kind에 따라 달라짐)
- **sig**: 진위를 증명하는 Schnorr 서명

이벤트 `id`는 임의의 식별자가 아니라 직렬화된 이벤트 데이터의 SHA256 해시입니다. 이것은 실무에서 중요합니다. 태그 순서나 timestamp를 포함해 어떤 필드든 바꾸면 다른 이벤트가 되고 새 서명이 필요합니다.

## Kinds

Kind는 릴레이가 이벤트를 저장하고 처리하는 방식을 결정합니다:

- **일반 이벤트** (1, 2, 4-44, 1000-9999): 일반적으로 저장되며 모든 버전을 보존함
- **대체 가능 이벤트** (0, 3, 10000-19999): pubkey당 최신 버전만 유지함
- **일회성 이벤트** (20000-29999): 저장하지 않고 구독자에게만 전달함
- **주소 지정 가능 이벤트** (30000-39999): pubkey + kind + `d` 태그 조합당 최신 버전 유지

핵심 kind로는 0 (사용자 메타데이터), 1 (텍스트 노트), 3 (팔로우 목록)이 있습니다.

## 클라이언트-릴레이 통신

클라이언트는 WebSocket 연결 위에서 JSON 배열을 사용해 릴레이와 통신합니다:

**클라이언트에서 릴레이로:**
- `[["EVENT", <event>]]` - 이벤트 발행
- `[["REQ", <sub-id>, <filter>, ...]]` - 이벤트 구독
- `[["CLOSE", <sub-id>]]` - 구독 종료

**릴레이에서 클라이언트로:**
- `[["EVENT", <sub-id>, <event>]]` - 일치하는 이벤트 전달
- `[["EOSE", <sub-id>]]` - 저장된 이벤트의 끝 (이후부터 실시간 스트리밍)
- `[["OK", <event-id>, <true|false>, <message>]]` - 수락 또는 거부 확인
- `[["NOTICE", <message>]]` - 사람이 읽을 수 있는 메시지

실제로 대부분의 상위 NIP은 전송 계층을 바꾸지 않습니다. NIP-01의 같은 `EVENT`, `REQ`, `CLOSE` 메시지를 그대로 사용하면서, 새로운 이벤트 kind와 태그, 해석 규칙을 정의합니다.

## 필터

필터는 어떤 이벤트를 가져올지 지정하며 `ids`, `authors`, `kinds`, `#e`/`#p`/`#t`, `since`, `until`, `limit` 같은 필드를 포함합니다. 하나의 필터 안 조건은 AND 논리를 사용합니다. 하나의 `REQ` 안 여러 필터는 OR 논리를 사용합니다.

## 상호운용성 참고사항

두 가지 세부사항이 구현 버그를 자주 일으킵니다. 첫째, 클라이언트는 릴레이 응답을 전역 순서가 아니라 eventual consistency로 처리해야 합니다. 서로 다른 릴레이가 서로 다른 히스토리 부분집합을 돌려줄 수 있기 때문입니다. 둘째, 대체 가능 이벤트와 주소 지정 가능 이벤트에서는 "최신"이 프로토콜 모델의 일부이므로, 여러 릴레이가 서로 다른 결과를 줄 때 클라이언트는 가장 최신의 유효 이벤트를 고르는 결정적 규칙이 필요합니다.

---

**주요 출처:**
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md)

**언급된 뉴스레터:**
- [Newsletter #1: NIP Deep Dive](/ko/newsletters/2025-12-17-newsletter/)
- [Newsletter #19: NIP-67 EOSE completeness hint proposal](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-19: Bech32 인코딩 엔티티](/ko/topics/nip-19/)
- [Kind Registry](/en/kind-registry/)
