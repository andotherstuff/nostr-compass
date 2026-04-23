---
title: "NIP-45：事件计数"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 定义了客户端如何让 relay 对匹配某个 filter 的 events 进行计数，而无需传输这些匹配 events 本身。它复用了 NIP-01 的 filter 语法，因此客户端通常可以把现有 `REQ` 直接改写为使用相同 filters 的 `COUNT` 请求。

## 工作原理

客户端发送一个带订阅 ID 和 filter 的 `COUNT` 请求：

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

relay 返回计数结果：

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

这样客户端就不必为了显示一个数字而下载成百上千条 events。如果客户端在一个 `COUNT` 请求里带了多个 filters，relay 会像处理多个 `REQ` filters 一样，把它们按 OR 逻辑汇总成一个结果。

## HyperLogLog 近似计数

截至 2026 年 2 月，NIP-45 已支持 HyperLogLog（HLL）近似计数（[PR #1561](https://github.com/nostr-protocol/nips/pull/1561)）。relays 可以把结果标记为近似值；为了做跨 relay 去重，它们还可以在返回计数时附带 256 个 HLL registers：

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<512-char hex string>"}]
```

HLL 解决了一个根本问题：如何跨多个 relays 统计不同的 events。如果 relay A 报告 50 个 reactions，relay B 报告 40 个，总数并不一定是 90，因为许多 events 可能在两个 relays 上都存在。客户端通过对每个 register 位置取最大值来合并 HLL，从而在不下载原始 events 的情况下得到全网近似值。

规范把 register 数量固定为 256，以保证互操作性。这让 payload 保持足够小，也使 relay 端缓存更可行，因为所有 relays 面对相同的合格 filter 都会计算出同样的 register 布局。

## 互操作说明

HLL 只为带 tag 属性的 filters 定义，因为构造 registers 所使用的 offset，来自 filter 中第一个带标签的值。规范还点名了一小组规范化查询，包括 reactions、reposts、quotes、replies、comments 和 follower counts。这些也是 relays 最容易预计算或缓存的计数类型。

## 为什么重要

follower counts、reaction counts 和 reply counts 是最典型的使用场景。没有 NIP-45，客户端要么只能相信某个 relay 的本地视图，要么必须把所有匹配 events 下载下来再自己去重。NIP-45 把计数留在 relay 内部完成，而 HLL 又让多 relay 计数成为可能，而不需要把某个 relay 变成唯一权威。

---

## 实现

- [nostream](https://github.com/Cameri/nostream) 在 [PR #522](https://github.com/Cameri/nostream/pull/522) 中加入了 `COUNT` 支持，让客户端可以询问有多少 events 匹配某个 filter，而不必把它们抓下来。

---

**主要来源：**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)
- [nostream PR #522](https://github.com/Cameri/nostream/pull/522) - NIP-45 COUNT support

**提及于：**
- [Newsletter #9：NIP 深度解析](/zh/newsletters/2026-02-11-newsletter/)
- [Newsletter #9：NIP 更新](/zh/newsletters/2026-02-11-newsletter/)
- [Newsletter #12：Five Years of Nostr Februaries](/zh/newsletters/2026-03-04-newsletter/)
- [Newsletter #19：nostream 的 NIP-45 支持](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-11：Relay 信息文档](/zh/topics/nip-11/)
