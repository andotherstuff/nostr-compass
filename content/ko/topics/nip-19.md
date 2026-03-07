---
title: "NIP-19: Bech32 인코딩 엔티티"
date: 2025-12-17
translationOf: /en/topics/nip-19.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identity
---
NIP-19는 Nostr 식별자를 공유하기 위한 사람이 읽기 쉬운 형식을 정의한다. 이 bech32 인코딩 문자열은 표시와 공유에 사용되며, 프로토콜 자체에서는 사용되지 않는다 (프로토콜은 hex를 사용).

## 작동 방식

원시 hex 키는 복사 시 오류가 발생하기 쉽고 시각적으로 구별하기 어렵다. Bech32 인코딩은 사람이 읽을 수 있는 접두사와 체크섬을 추가하여, 어떤 유형의 데이터인지 명확히 하고 많은 복사 오류를 감지한다.

기본 형식은 단일 32바이트 값을 인코딩한다:

- **npub** - 공개키 (신원, 공유 가능)
- **nsec** - 비밀키 (비밀 유지, 서명에 사용)
- **note** - 이벤트 ID (특정 이벤트 참조)

예시: hex 공개키 `3bf0c63f...`는 `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`가 된다.

확장 형식은 TLV 인코딩을 사용하여 식별자와 함께 조회 힌트를 전달한다:

- **nprofile** - 릴레이 힌트가 포함된 프로필
- **nevent** - 릴레이 힌트, 작성자 공개키, kind가 포함된 이벤트
- **naddr** - 공개키, kind, `d` 태그, 릴레이 힌트가 포함된 주소 지정 가능 이벤트 참조

## 왜 중요한가

릴레이 힌트는 권위적이지 않지만, 클라이언트가 공유된 이벤트를 첫 시도에 가져올 수 있는지를 좌우하는 경우가 많다. 콘텐츠가 수신자의 현재 릴레이 세트 밖에 있을 때, `nevent`, `nprofile`, `naddr`가 단순 `note`나 `npub` 값보다 더 나은 공유 형식인 이유다.

안정성도 실질적 차이점이다. `note`는 하나의 불변 이벤트 ID를 가리키고, `naddr`는 시간이 지남에 따라 교체될 수 있는 주소 지정 가능 이벤트를 가리킨다. 장문 콘텐츠, 캘린더, 저장소 공지에는 `naddr`가 보통 적합한 링크 유형이다.

## 구현 참고사항

- Bech32는 사람 인터페이스에서만 사용: 표시, 복사/붙여넣기, QR 코드, URL
- 프로토콜 메시지, 이벤트, NIP-05 응답에 bech32 형식을 사용하지 말 것
- 모든 프로토콜 통신은 hex 인코딩을 사용해야 함
- nevent/nprofile/naddr 생성 시 검색 가능성을 위해 릴레이 힌트 포함
- `nsec`는 모든 곳에서 비밀 자료로 취급할 것. 클라이언트는 기본적으로 표시하거나, 로그에 기록하거나, 지원 내보내기에 포함해서는 안 됨

---

**주요 출처:**
- [NIP-19 명세](https://github.com/nostr-protocol/nips/blob/master/19.md)

**언급된 뉴스레터:**
- [뉴스레터 #1: NIP 심층 분석](/en/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)
- [뉴스레터 #3: 12월 회고](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [뉴스레터 #3: 주목할 코드 변경](/en/newsletters/2025-12-31-newsletter/#damus-ios)
- [뉴스레터 #4: 릴레이 힌트 지원](/en/newsletters/2026-01-07-newsletter/)
- [뉴스레터 #8: Damus iOS](/en/newsletters/2026-02-04-newsletter/#damus-ios)
- [뉴스레터 #11: notecrumbs](/en/newsletters/2026-02-25-newsletter/)

**같이 보기:**
- [NIP-01: 기본 프로토콜](/ko/topics/nip-01/)
- [NIP-10: 답글 스레드](/ko/topics/nip-10/)
