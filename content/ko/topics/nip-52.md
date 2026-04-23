---
title: "NIP-52: 캘린더 이벤트"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52는 Nostr의 캘린더 이벤트, 캘린더, RSVP를 정의합니다. 각 앱이 저마다의 이벤트 모델을 새로 만들지 않고도, 시간 기반 또는 날짜 기반 이벤트를 게시할 수 있는 표준 방식을 제공합니다.

## 이벤트 종류

### Kind 31922: 날짜 기반 캘린더 이벤트

시계 시간이 중요하지 않은 종일 또는 여러 날 이벤트에는 kind `31922`를 사용합니다.

```json
{
  "kind": 31922,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Nostr Meetup"],
    ["start", "2026-02-15"],
    ["end", "2026-02-16"],
    ["location", "Austin, TX"]
  ]
}
```

### Kind 31923: 시간 기반 캘린더 이벤트

정확한 시작 시각과 종료 시각이 있는 이벤트에는 kind `31923`을 사용합니다.

```json
{
  "kind": 31923,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Weekly Call"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["D", "19755"],
    ["start_tzid", "America/New_York"]
  ]
}
```

시간 기반 이벤트에는 하나 이상의 `D` 태그도 필요하며, 각 태그는 이벤트가 걸치는 날짜들의 일 단위 Unix timestamp를 담습니다. 이 태그가 존재하는 이유는 릴레이와 클라이언트가 전체 timestamp를 전부 파싱하지 않고도 날짜 단위로 인덱싱할 수 있게 하기 위해서입니다.

## 캘린더와 RSVP 지원

Kind `31924`는 캘린더이며, 캘린더 이벤트의 addressable list입니다. Kind `31925`는 RSVP로, `a` 태그로 특정 캘린더 이벤트를 가리키고 선택적으로 `e` 태그로 특정 revision까지 가리킵니다.

Kind `31925` 이벤트에서 사용자는 다음 값으로 응답할 수 있습니다:

- `accepted` - 참석함
- `declined` - 참석하지 않음
- `tentative` - 참석할 수도 있음

RSVP는 `fb` 값으로 `free` 또는 `busy`를 포함할 수도 있어, 참석 여부를 넘어 일정 점유 맥락까지 표현할 수 있습니다.

## 구현 참고사항

- **주소 지정 가능**: 이벤트와 캘린더를 중복 생성 없이 갱신할 수 있음
- **시간대 지원**: 시간 기반 이벤트는 IANA timezone identifier를 사용할 수 있음
- **위치 데이터**: 태그에 사람이 읽을 수 있는 위치, 링크, geohash를 담을 수 있음
- **협업 요청**: 이벤트 작성자는 태깅을 통해 다른 사람의 캘린더에 포함 요청을 보낼 수 있음

반복 이벤트는 의도적으로 범위 밖입니다. 명세는 recurrence rule을 클라이언트에 맡기며, 덕분에 릴레이 쪽 인덱싱을 단순하게 유지하고 daylight saving time 변경이나 예외 처리 같은 일반적인 캘린더 edge case를 피합니다.

## 왜 중요한가

NIP-52는 단순히 회의 하나를 기술하는 수준을 넘습니다. 이벤트 정의, 캘린더 소속, 참석자 응답을 서로 다른 이벤트 kind로 분리합니다. 이 구조 덕분에 한 앱이 이벤트를 게시하고, 다른 앱이 캘린더를 집계하고, 세 번째 앱이 RSVP 상태를 관리하더라도 세 앱이 같은 backend를 공유할 필요가 없습니다.

---

**주요 출처:**
- [NIP-52 Specification](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: Day-Granularity Timestamp Tag](https://github.com/nostr-protocol/nips/pull/1752)

**언급된 뉴스레터:**
- [Newsletter #7: Notedeck Calendar App Draft](/ko/newsletters/2026-01-28-newsletter/)
- [Newsletter #10: NIP Updates](/ko/newsletters/2026-02-18-newsletter/)
- [Newsletter #10: NIP Deep Dive](/ko/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Calendar by Form* v0.2.0](/en/newsletters/2026-03-11-newsletter/)

**같이 보기:**
- [NIP-22: 댓글](/ko/topics/nip-22/)
- [NIP-51: 리스트](/ko/topics/nip-51/)
