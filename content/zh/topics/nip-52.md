---
title: "NIP-52：日历事件"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 定义了 Nostr 上的日历事件、日历和 RSVP。它给客户端提供了一种发布基于时间或日期的事件的标准方式，而不必为每个 app 都重新发明一套自定义 event 模型。

## Event Kinds

### Kind 31922：基于日期的日历事件

kind `31922` 用于那些不关心具体时钟时间的全天或多日事件。

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

### Kind 31923：基于时间的日历事件

kind `31923` 用于具有精确开始和结束时间的事件。

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

基于时间的事件还要求带有一个或多个 `D` tags，每个 tag 都包含事件跨越日期对应的日粒度 Unix 时间戳。这个 tag 的存在，是为了让 relays 和客户端能够按天索引，而不需要解析每一个完整时间戳。

## 日历与 RSVP 支持

kind `31924` 是一个日历，也就是一个可寻址的日历事件列表。kind `31925` 是 RSVP，它通过 `a` tag 指向某个特定的日历事件，也可以选择通过 `e` tag 指向某个具体修订版本。

kind `31925` events 允许用户回复：

- `accepted` - 会参加
- `declined` - 不会参加
- `tentative` - 可能参加

RSVP 还可以带有 `fb` 值 `free` 或 `busy`，从而在出席状态之外，再加入额外的日程上下文。

## 实现说明

- **可寻址**：事件与日历都可以更新，而不会制造重复项
- **时区支持**：基于时间的事件可以使用 IANA 时区标识符
- **位置数据**：tags 可以包含人类可读的位置、链接和 geohash
- **协作式请求**：事件作者可以通过打 tag 的方式请求将事件加入他人的日历

重复事件被有意排除在规范范围之外。规范把 recurrence rules 交给客户端处理，这样 relay 侧索引会更简单，也能避开夏令时变化和例外日期等经典日历边界问题。

## 为什么重要

NIP-52 的作用不只是描述一次会议。它把事件定义、日历归属和参与者响应拆分到不同 event kinds 里。这使得一个 app 可以发布事件，另一个 app 聚合日历，而第三个 app 管理 RSVP 状态，而三者却不需要共享同一个后端。

---

**主要来源：**
- [NIP-52 Specification](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: Day-Granularity Timestamp Tag](https://github.com/nostr-protocol/nips/pull/1752)

**提及于：**
- [Newsletter #7：Notedeck Calendar App Draft](/zh/newsletters/2026-01-28-newsletter/)
- [Newsletter #10：NIP Updates](/zh/newsletters/2026-02-18-newsletter/)
- [Newsletter #10：NIP Deep Dive](/zh/newsletters/2026-02-18-newsletter/)
- [Newsletter #13：Calendar by Form* v0.2.0](/en/newsletters/2026-03-11-newsletter/)

**另请参阅：**
- [NIP-22：Comment](/zh/topics/nip-22/)
- [NIP-51：Lists](/zh/topics/nip-51/)
