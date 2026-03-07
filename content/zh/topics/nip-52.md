---
title: "NIP-52：日历事件"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 定义了 Nostr 上的日历事件、日历和 RSVP。它为客户端提供了一种标准方式来发布基于时间或基于日期的事件，无需每个应用都发明自定义事件模型。

## 事件类型

### Kind 31922：基于日期的日历事件

用于全天或多日事件，时钟时间无关紧要的场景。

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

用于具有精确开始和结束时间的事件。

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

基于时间的事件还需要一个或多个 `D` 标签，每个标签包含事件跨越日期的日粒度 Unix 时间戳。该标签的存在使得中继和客户端可以按日索引，而无需解析每个完整时间戳。

## 日历和 RSVP 支持

Kind `31924` 是一个日历，即日历事件的可寻址列表。Kind `31925` 是一个 RSVP，通过 `a` 标签指向特定日历事件，并可选通过 `e` 标签指向特定修订版本。

Kind `31925` 事件允许用户以以下方式回应：

- `accepted` - 将出席
- `declined` - 不会出席
- `tentative` - 可能出席

RSVP 还可以包含值为 `free` 或 `busy` 的 `fb` 字段，这在出席状态之外增加了日程安排上下文。

## 实现说明

- **可寻址**：事件和日历可以更新而不会创建重复项
- **时区支持**：基于时间的事件可以使用 IANA 时区标识符
- **位置数据**：标签可以包含人类可读的地点、链接和 geohash
- **协作请求**：事件作者可以通过标记他人的日历来请求将事件加入其中

重复事件被特意排除在规范范围之外。规范将重复规则推给客户端处理，这使得中继端索引保持简单，也避免了夏令时变更和例外情况的常见日历边界问题。

## 重要意义

NIP-52 的作用不仅仅是描述一次会议。它将事件定义、日历成员关系和参会者回应分离为不同的事件类型。这使得一个应用发布事件、另一个应用聚合日历、第三个应用管理 RSVP 状态成为可能，而这三者无需共享同一后端。

---

**主要来源：**
- [NIP-52 规范](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752：日粒度时间戳标签](https://github.com/nostr-protocol/nips/pull/1752)

**提及于：**
- [第7期周刊：Notedeck 日历应用草案](/zh/newsletters/2026-01-28-newsletter/#notedeck-progress-calendar-app-and-ux-polish)
- [第10期周刊：NIP 更新](/zh/newsletters/2026-02-18-newsletter/#nip-updates)
- [第10期周刊：NIP 深度解析](/zh/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-52-calendar-events)

**另请参阅：**
- [NIP-22：评论](/zh/topics/nip-22/)
- [NIP-51：列表](/zh/topics/nip-51/)
