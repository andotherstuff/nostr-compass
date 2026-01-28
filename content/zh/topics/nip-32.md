---
title: "NIP-32：标签"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-32 定义了将标签附加到 Nostr 事件、用户和其他实体的标准。标签提供结构化元数据，客户端可用于分类、内容警告、信誉系统和审核。

## 工作原理

标签使用 kind 1985 事件，`L` 标签定义标签命名空间，`l` 标签在该命名空间内应用特定标签。被标记的实体通过标准标签引用，如 `e`（事件）、`p`（pubkey）或 `r`（中继 URL）。

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

命名空间系统防止标签冲突。"ugc-moderation"命名空间中的"spam"标签与"relay-report"命名空间中的"spam"具有不同的语义。这使得多个标签系统可以共存而不会相互干扰。

## 用例

内容审核系统使用标签来标记垃圾信息、非法内容或违反政策的内容。信誉系统将信任评分或验证状态附加到 pubkey。媒体平台应用内容警告（成人内容、暴力、剧透）。中继运营者使用标签进行申诉和争议解决。

可信中继声明提案使用 NIP-32 标签进行中继申诉。当运营者对信任评分提出异议时，他们发布带有 `L` = `relay-appeal` 和"spam"、"censorship"或"score"等标签类型的 kind 1985 事件。

客户端实现在如何使用标签方面各有不同。一些客户端将关注用户的标签视为推荐，而其他客户端查询专门的标签服务。去中心化设计让用户选择信任哪些标签者。

---

**主要来源：**
- [NIP-32 规范](https://github.com/nostr-protocol/nips/blob/master/32.md) - 标签标准

**提及于：**
- [通讯 #6：NIP 更新](/zh/newsletters/2026-01-21-newsletter/#nip-updates)

**另请参阅：**
- [可信中继声明](/zh/topics/trusted-relay-assertions/)
- [NIP-51：列表](/zh/topics/nip-51/)
