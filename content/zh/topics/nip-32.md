---
title: "NIP-32：标签系统"
date: 2026-01-21
draft: false
translationOf: /en/topics/nip-32.md
translationDate: 2026-03-07
categories:
  - NIPs
  - Protocol
---

NIP-32 定义了一套标准，用于将标签附加到 Nostr 事件、用户和其他实体上。标签提供结构化的元数据，客户端可以用于分类、内容警告、声誉系统和内容审核。

## 工作原理

标签使用 kind 1985 事件，其中 `L` 标签定义标签命名空间，`l` 标签在该命名空间内应用具体标签。被标记的实体通过标准标签引用，如 `e`（事件）、`p`（公钥）或 `r`（中继 URL）。

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Contains explicit imagery"
}
```

命名空间系统可以防止标签冲突。"ugc-moderation"命名空间中的"spam"标签与"relay-report"命名空间中的"spam"标签具有不同的语义。这使得多个标签系统可以共存而互不干扰。

## 重要意义

关键的设计选择在于，标签是断言而非协议内置的事实。一个 kind 1985 事件表示某个行为者在某个命名空间中为某事物打了标签。客户端仍然需要制定信任策略，决定展示、隐藏或忽略哪些标签。

这使得 NIP-32 的用途远不止内容审核。同样的结构可以承载内容警告、验证标记、分类系统或中继声誉数据，而无需强制所有客户端使用同一套全局词汇表。

## 用例

内容审核系统使用标签来标记垃圾信息、违法内容或违规行为。声誉系统将信任评分或验证状态附加到公钥上。媒体平台应用内容警告，如 NSFW、暴力或剧透。中继运营者使用标签进行申诉和争议解决。

Trusted Relay Assertions 提案使用 NIP-32 标签进行中继申诉。当运营者对信任评分有异议时，他们发布 kind 1985 事件，其中 `L = relay-appeal`，标签包括 `spam`、`censorship` 或 `score`。

## 互操作说明

不同客户端对标签的消费方式各有不同。有些将来自关注用户的标签视为推荐，有些则查询专门的标签服务。去中心化的设计让用户可以选择信任哪些标签提供者，但这也意味着没有可见信任上下文的标签可能会产生误导。

---

**主要来源：**
- [NIP-32 规范](https://github.com/nostr-protocol/nips/blob/master/32.md) - 标签系统标准

**提及于：**
- [Newsletter #6：NIP 更新](/zh/newsletters/2026-01-21-newsletter/#nip-updates)

**另请参阅：**
- [Trusted Relay Assertions](/zh/topics/trusted-relay-assertions/)
- [NIP-51：列表](/zh/topics/nip-51/)
