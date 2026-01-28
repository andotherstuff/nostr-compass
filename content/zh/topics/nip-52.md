---
title: "NIP-52：日历事件"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 定义了 Nostr 上日历功能的事件类型，支持日程安排、RSVP 和活动协调。

## 事件类型

### Kind 31922：基于日期的日历事件
用于跨越一天或多天但没有具体时间的事件：

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

### Kind 31923：基于时间的日历事件
用于具有特定开始和结束时间的事件：

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

## RSVP 支持

Kind 31925 事件允许用户对日历事件做出回应：

- `accepted` - 将出席
- `declined` - 不会出席
- `tentative` - 可能出席

## 特性

- **可寻址**：事件可以更新而不会创建重复项
- **时区支持**：通过 IANA 标识符正确处理时区
- **位置**：实体或虚拟会议地点
- **重复**：支持重复事件（提议的扩展）

## 相关

- [NIP-22](/zh/topics/nip-22/) - 评论（用于日历事件讨论）
- [NIP-51](/zh/topics/nip-51/) - 列表（用于日历集合）
