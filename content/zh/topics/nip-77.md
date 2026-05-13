---
title: "NIP-77：Negentropy集合协调"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-77.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Sync
---

NIP-77定义了Nostr中继和客户端如何使用[Negentropy](/zh/topics/negentropy/)集合协调协议来高效同步事件集合，在不重新发送完整数据集的情况下找出双方各自缺少哪些事件。

## 工作原理

Negentropy协调通过WebSocket连接使用专用消息类型运行。客户端和中继在各自已排序的事件集合上交换紧凑的范围指纹，逐步缩小到仅有差异的范围。一旦确定差异，只传输缺失的事件ID（然后是缺失的事件本身）。

NIP-77对消息框架进行标准化，使任何实现该规范的客户端和中继都能协商高效的同步会话。协议在现有Nostr WebSocket连接上使用`NEG-OPEN`、`NEG-MSG`和`NEG-CLOSE`消息类型。

## 为何重要

传统的Nostr同步使用基于时间戳的`since`过滤器，可能因时钟漂移、具有相同时间戳的事件或乱序到达的事件而遗漏事件。Negentropy比较实际事件集合而非依赖时间戳，与简单轮询相比，以明显更少的往返次数实现可证明完整的同步。

这对以下场景特别有用：
- 离线后需要追赶同步的移动端客户端
- 中继间复制
- 本地中继同步（如Citrine的中继聚合器）

## 实现

- [Citrine](https://github.com/greenart7c3/Citrine) — [PR #139](https://github.com/greenart7c3/Citrine/pull/139) 为Android中继节点添加了高效集合协调同步的NIP-77支持
- [strfry](https://github.com/hoytech/strfry) — 中继端Negentropy支持
- [nostr-tools](https://github.com/nbd-wtf/nostr-tools) — 客户端Negentropy实现

---

**主要来源：**
- [NIP-77规范](https://github.com/nostr-protocol/nips/blob/master/77.md)
- [Negentropy协议](https://github.com/hoytech/negentropy)

**提及于：**
- [新闻通讯#22：Citrine v3.0.0-pre1](/zh/newsletters/2026-05-14-newsletter/#citrine-v300-pre1-lands-built-in-tor-and-relay-aggregation)

**另见：**
- [Negentropy](/zh/topics/negentropy/)
