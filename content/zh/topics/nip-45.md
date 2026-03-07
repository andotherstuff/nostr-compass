---
title: "NIP-45：事件计数"
date: 2026-02-11
draft: false
translationOf: /en/topics/nip-45.md
translationDate: 2026-03-07
categories:
  - NIPs
  - Protocol
---

NIP-45 定义了客户端如何请求中继统计符合过滤条件的事件数量，而无需传输匹配的事件本身。它复用 NIP-01 的过滤语法，因此客户端通常可以用相同的过滤条件将现有的 `REQ` 转换为 `COUNT` 请求。

## 工作原理

客户端发送带有订阅 ID 和过滤条件的 `COUNT` 请求：

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

中继返回计数结果：

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

这避免了仅为显示一个数字而下载数百或数千个事件。如果客户端在一个 `COUNT` 请求中发送多个过滤条件，中继会将它们聚合为单个结果，就像多个 `REQ` 过滤条件进行 OR 合并一样。

## HyperLogLog 近似计数

截至 2026 年 2 月，NIP-45 支持 HyperLogLog（HLL）近似计数（[PR #1561](https://github.com/nostr-protocol/nips/pull/1561)）。中继可以将结果标记为近似值，对于跨中继去重，它们可以在计数旁返回 256 个 HLL 寄存器：

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<512-char hex string>"}]
```

HLL 解决了一个根本问题：跨多个中继统计不同事件的数量。如果中继 A 报告 50 个反应，中继 B 报告 40 个，总数并不是 90，因为许多事件同时存在于两个中继上。客户端通过取每个寄存器位置的最大值来合并 HLL 值，从而获得全网范围的估算，而无需下载原始事件。

规范将寄存器数量固定为 256 以确保互操作性。这使载荷保持较小，并使中继端缓存变得可行，因为每个中继对相同的合格过滤条件计算出相同的寄存器布局。

## 互操作说明

HLL 仅适用于带有标签属性的过滤条件，因为用于构建寄存器的偏移量来源于过滤条件中第一个标记值。规范还列出了一小组典型查询，包括反应、转发、引用、回复、评论和关注者计数。这些是中继最容易预计算或缓存的计数类型。

## 重要意义

关注者计数、反应计数和回复计数是主要用例。没有 NIP-45，客户端要么必须信任单个中继的本地视图，要么下载所有匹配的事件并在本地去重。NIP-45 将计数保留在中继内部，HLL 使多中继计数变得可行，而无需将某个中继变成权威来源。

---

**主要来源：**
- [NIP-45：事件计数](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561：HyperLogLog 中继响应](https://github.com/nostr-protocol/nips/pull/1561)

**提及于：**
- [Newsletter #9：NIP 深度解析](/zh/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-45-event-counting-and-hyperloglog)
- [Newsletter #9：NIP 更新](/zh/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12：Nostr 五年二月回顾](/zh/newsletters/2026-03-04-newsletter/)

**另请参阅：**
- [NIP-11：中继信息文档](/zh/topics/nip-11/)
