---
title: "NIP-52: 캘린더 이벤트"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52는 Nostr의 캘린더 기능을 위한 event kind를 정의하여, 일정 관리, RSVP, 이벤트 조정을 가능하게 합니다.

## Event Kind

### Kind 31922: 날짜 기반 캘린더 이벤트
특정 시간 없이 하루 이상에 걸친 이벤트:

```json
{
  "kind": 31922,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Nostr Meetup"],
    ["start", "2026-02-15"],
    ["end", "2026-02-15"],
    ["location", "Austin, TX"]
  ]
}
```

### Kind 31923: 시간 기반 캘린더 이벤트
특정 시작 및 종료 시간이 있는 이벤트:

```json
{
  "kind": 31923,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Weekly Call"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["start_tzid", "America/New_York"]
  ]
}
```

## RSVP 지원

Kind 31925 event는 사용자가 캘린더 이벤트에 응답할 수 있게 합니다:

- `accepted` - 참석 예정
- `declined` - 참석 안 함
- `tentative` - 참석 가능

## 기능

- **주소 지정 가능**: 중복 생성 없이 이벤트 업데이트 가능
- **시간대 지원**: IANA 식별자를 통한 적절한 시간대 처리
- **위치**: 물리적 또는 가상 회의 장소
- **반복**: 반복 이벤트 지원 (제안된 확장)

## 관련 항목

- [NIP-22](/ko/topics/nip-22/) - 댓글 (캘린더 이벤트 토론용)
- [NIP-51](/ko/topics/nip-51/) - 목록 (캘린더 컬렉션용)
