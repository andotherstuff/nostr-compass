---
title: "NIP-45：事件计数"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 定义了客户端如何请求 relay 计算匹配过滤器的 event 数量，而无需传输 event 本身。客户端发送与 REQ 相同过滤器语法的 COUNT 消息，relay 返回计数结果。

## 工作原理

客户端发送带有订阅 ID 和过滤器的 COUNT 请求：

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

relay 返回计数：

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

这避免了仅为显示一个数字而下载数百或数千个 event。

## HyperLogLog 近似计数

截至 2026 年 2 月，NIP-45 支持 HyperLogLog (HLL) 近似计数（[PR #1561](https://github.com/nostr-protocol/nips/pull/1561)）。relay 可以在 COUNT 响应中返回 256 字节的 HLL 寄存器值：

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

HLL 解决了一个根本问题：跨多个 relay 计算不同 event 的数量。如果 relay A 报告 50 个反应，relay B 报告 40 个，总数并非 90，因为许多 event 同时存在于两个 relay 上。来自多个 relay 的 HLL 寄存器可以通过取每个寄存器位置的最大值来合并，自动实现跨网络去重。

使用 256 个寄存器时，标准误差约为 5.2%。HyperLogLog++ 修正提高了 ~200 个 event 以下小基数的准确度。即使两个反应 event 消耗的带宽也超过 256 字节的 HLL 负载，因此对于任何超过微量数字的计数都很高效。

规范将寄存器数量固定为 256，以确保所有 relay 实现之间的互操作性。

## 用例

社交指标（关注者数量、反应数量、转发数量）是主要应用。没有 HLL 时，客户端要么查询单个"可信"relay 获取计数（将数据中心化），要么从所有 relay 下载所有 event 在本地去重（浪费带宽）。HLL 以每个 relay 256 字节的开销提供近似的跨 relay 计数。

---

**主要来源：**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**提及于：**
- [新闻通讯 #9：NIP 深入解析](/zh/newsletters/2026-02-11-newsletter/#nip-深入解析nip-45事件计数与-hyperloglog)
- [新闻通讯 #9：NIP 更新](/zh/newsletters/2026-02-11-newsletter/#nip-更新)

**另见：**
- [NIP-11：Relay 信息文档](/zh/topics/nip-11/)
