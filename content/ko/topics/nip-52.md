---
title: "NIP-52: 캘린더 이벤트"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Calendar
  - Events
---
NIP-52는 Nostr에서 캘린더 이벤트, 캘린더, RSVP를 정의한다. 앱마다 별도의 이벤트 모델을 만들지 않고도, 시간 기반 또는 날짜 기반 이벤트를 게시할 수 있는 표준 방법을 제공한다.

## 이벤트 종류

### Kind 31922: 날짜 기반 캘린더 이벤트

시계 시간이 중요하지 않은 종일 또는 여러 날 이벤트에는 kind `31922`를 사용한다.

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

정확한 시작 및 종료 시간이 있는 이벤트에는 kind `31923`을 사용한다.

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

시간 기반 이벤트에는 하나 이상의 `D` 태그가 필요하며, 각 태그에는 이벤트가 걸쳐 있는 날의 일 단위 Unix 타임스탬프가 포함된다. 이 태그 덕분에 릴레이와 클라이언트가 전체 타임스탬프를 파싱하지 않고도 일 단위로 인덱싱할 수 있다.

## 캘린더 및 RSVP 지원

Kind `31924`는 캘린더로, 캘린더 이벤트의 주소 지정 가능한 리스트이다. Kind `31925`는 RSVP로, `a` 태그로 특정 캘린더 이벤트를 가리키며 선택적으로 `e` 태그로 특정 리비전을 가리킨다.

Kind `31925` 이벤트에서 사용자는 다음과 같이 응답할 수 있다:

- `accepted` - 참석 예정
- `declined` - 불참
- `tentative` - 참석 가능

RSVP에는 `fb` 값으로 `free` 또는 `busy`를 포함할 수 있어, 참석 상태 외에 일정 맥락 정보도 추가할 수 있다.

## 구현 참고사항

- **주소 지정 가능**: 이벤트와 캘린더를 중복 생성 없이 업데이트 가능
- **시간대 지원**: 시간 기반 이벤트에 IANA 시간대 식별자 사용 가능
- **위치 데이터**: 사람이 읽을 수 있는 위치, 링크, geohash를 태그에 포함 가능
- **협업 요청**: 이벤트 작성자가 태그를 통해 다른 사람의 캘린더에 포함을 요청 가능

반복 이벤트는 의도적으로 범위에서 제외되었다. 명세는 반복 규칙을 클라이언트에 위임하여 릴레이 측 인덱싱을 단순하게 유지하고, 일광 절약 시간 변경과 예외 처리 같은 일반적인 캘린더 엣지 케이스를 피한다.

## 왜 중요한가

NIP-52는 단순히 회의를 설명하는 것 이상이다. 이벤트 정의, 캘린더 소속, 참석자 응답을 서로 다른 이벤트 종류로 분리한다. 이를 통해 한 앱이 이벤트를 게시하고, 다른 앱이 캘린더를 집계하고, 세 번째 앱이 RSVP 상태를 관리하는 것이 가능하며, 세 앱 모두 같은 백엔드를 공유할 필요가 없다.

---

**주요 출처:**
- [NIP-52 명세](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: 일 단위 타임스탬프 태그](https://github.com/nostr-protocol/nips/pull/1752)

**언급된 뉴스레터:**
- [뉴스레터 #7: Notedeck 캘린더 앱 초안](/en/newsletters/2026-01-28-newsletter/#notedeck-progress-calendar-app-and-ux-polish)
- [뉴스레터 #10: NIP 업데이트](/en/newsletters/2026-02-18-newsletter/#nip-updates)
- [뉴스레터 #10: NIP 심층 분석](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-52-calendar-events)

**같이 보기:**
- [NIP-22: 댓글](/ko/topics/nip-22/)
- [NIP-51: 리스트](/ko/topics/nip-51/)
