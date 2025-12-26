---
title: "NIP-01: 기본 프로토콜"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-01은 Nostr의 기초 프로토콜을 정의하며, 다른 모든 NIP가 기반으로 하는 데이터 구조와 통신 패턴을 확립합니다.

## 이벤트

이벤트는 Nostr에서 유일한 객체 유형입니다. 프로필 업데이트부터 텍스트 게시물, 리액션에 이르기까지 모든 데이터 조각이 다음 구조의 이벤트로 표현됩니다:

- **id**: 직렬화된 이벤트의 SHA256 해시(고유 식별자)
- **pubkey**: 생성자의 공개 키(32바이트 hex, secp256k1)
- **created_at**: Unix 타임스탬프
- **kind**: 이벤트 유형을 분류하는 정수
- **tags**: 메타데이터용 배열의 배열
- **content**: 페이로드(해석은 kind에 따라 다름)
- **sig**: 진위를 증명하는 Schnorr 서명

## Kind

Kind는 릴레이가 이벤트를 저장하고 처리하는 방식을 결정합니다:

- **일반 이벤트** (1, 2, 4-44, 1000-9999): 정상적으로 저장, 모든 버전 유지
- **교체 가능 이벤트** (0, 3, 10000-19999): pubkey당 최신 버전만 유지
- **임시 이벤트** (20000-29999): 저장되지 않고 구독자에게만 전달
- **주소 지정 가능 이벤트** (30000-39999): pubkey + kind + `d` 태그 조합당 최신 버전

핵심 kind: 0(사용자 메타데이터), 1(텍스트 노트), 3(팔로우 리스트).

## 클라이언트-릴레이 통신

클라이언트는 JSON 배열을 사용하는 WebSocket 연결을 통해 릴레이와 통신합니다:

**클라이언트에서 릴레이로:**
- `["EVENT", <event>]` - 이벤트 게시
- `["REQ", <sub-id>, <filter>, ...]` - 이벤트 구독
- `["CLOSE", <sub-id>]` - 구독 종료

**릴레이에서 클라이언트로:**
- `["EVENT", <sub-id>, <event>]` - 일치하는 이벤트 전달
- `["EOSE", <sub-id>]` - 저장된 이벤트 종료(이제 실시간 스트리밍)
- `["OK", <event-id>, <true|false>, <message>]` - 수락/거부 확인
- `["NOTICE", <message>]` - 사람이 읽을 수 있는 메시지

## 필터

필터는 검색할 이벤트를 지정하며, `ids`, `authors`, `kinds`, `#e`/`#p`/`#t`(태그 값), `since`/`until`, `limit` 필드를 포함합니다. 필터 내 조건은 AND 논리를 사용하고, `REQ`의 여러 필터는 OR 논리로 결합됩니다.

---

**주요 출처:**
- [NIP-01 사양](https://github.com/nostr-protocol/nips/blob/master/01.md)

**언급된 곳:**
- [뉴스레터 #1: NIP 심층 분석](/ko/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-and-nip-19)

**참고:**
- [NIP-19: Bech32 인코딩 엔티티](/ko/topics/nip-19/)
- [Kind 레지스트리](/ko/kind-registry/)

