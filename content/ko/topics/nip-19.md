---
title: "NIP-19: Bech32 인코딩 엔티티"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-19는 Nostr 식별자를 공유하기 위한 사용자 친화적 형식을 정의합니다. 이러한 bech32 인코딩 문자열은 표시와 공유에 사용되지만 프로토콜 자체(hex 사용)에서는 사용되지 않습니다.

## 왜 Bech32인가?

원시 hex 키는 복사하기 쉽지 않고 시각적으로 구별할 수 없습니다. Bech32 인코딩은 사람이 읽을 수 있는 접두사와 체크섬을 추가하여 어떤 유형의 데이터를 보고 있는지 즉시 명확하게 합니다.

## 기본 형식

원시 32바이트 값을 인코딩합니다:

- **npub** - 공개 키(당신의 신원, 공유해도 안전)
- **nsec** - 개인 키(비밀 유지, 서명에 사용)
- **note** - 이벤트 ID(특정 이벤트 참조)

예시: hex pubkey `3bf0c63f...`는 `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`가 됩니다.

## 공유 가능 식별자

TLV(Type-Length-Value) 인코딩을 사용하여 메타데이터를 포함합니다:

- **nprofile** - 릴레이 힌트가 있는 프로필(클라이언트가 사용자를 찾는 데 도움)
- **nevent** - 릴레이 힌트, 작성자 pubkey, kind가 있는 이벤트
- **naddr** - 주소 지정 가능 이벤트 참조(pubkey + kind + d-tag + relays)

이들은 검색 문제를 해결합니다: 누군가 노트 ID를 공유하면 클라이언트가 어떤 릴레이에 있는지 어떻게 알 수 있을까요? 릴레이 힌트를 식별자에 묶어 공유된 링크가 더 신뢰할 수 있게 됩니다.

## 구현 참고 사항

- bech32는 사람 인터페이스에만 사용: 표시, 복사/붙여넣기, QR 코드, URL
- 프로토콜 메시지, 이벤트, NIP-05 응답에서는 절대 bech32 형식을 사용하지 않음
- 모든 프로토콜 통신은 hex 인코딩을 사용해야 함
- nevent/nprofile/naddr 생성 시 더 나은 검색을 위해 릴레이 힌트 포함

---

**주요 출처:**
- [NIP-19 사양](https://github.com/nostr-protocol/nips/blob/master/19.md)

**언급된 곳:**
- [뉴스레터 #1: NIP 심층 분석](/ko/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)

**참고:**
- [NIP-01: 기본 프로토콜](/ko/topics/nip-01/)
- [NIP-21: nostr: URI 스킴](https://github.com/nostr-protocol/nips/blob/master/21.md)

