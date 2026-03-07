---
title: "NIP-69：点对点交易"
date: 2025-12-17
draft: false
translationOf: /en/topics/nip-69.md
translationDate: 2026-03-07
categories:
  - Trading
  - Protocol
---

NIP-69 定义了一种通过 Nostr 进行点对点交易的协议，创建一个跨多个平台的统一订单簿，而非碎片化的流动性池。

## 工作原理

NIP-69 使用可寻址的 kind 38383 事件来表示买卖订单。可寻址格式很重要，因为一个订单可能会随时间经历多个状态变化，同时通过其 `d` 标签保持相同的逻辑身份。

## 订单结构

订单使用标签来指定交易参数：

- `d` - 订单 ID
- `k` - 订单类型（买入/卖出）
- `f` - 法币货币（ISO 4217 代码）
- `amt` - 比特币金额（以聪为单位）
- `fa` - 法币金额
- `pm` - 接受的支付方式
- `premium` - 价格溢价/折扣百分比
- `network` - 比特币网络（mainnet、testnet、signet、regtest）
- `layer` - 结算层（onchain、lightning、liquid）
- `expiration` - 订单过期时间

## 订单生命周期

订单按以下状态推进：
- `pending` - 开放且可供匹配
- `in-progress` - 已与对手方发起交易
- `success` - 交易完成
- `canceled` - 由挂单者撤回
- `expired` - 超过过期时间

规范区分了两种时间限制。`expires_at` 标记待处理订单何时不再被视为开放，而 `expiration` 为中继提供一个时间戳，中继可以使用 [NIP-40](/zh/topics/nip-40/) 来完全移除过期的订单事件。

## 重要意义

NIP-69 是一项互操作性举措。Mostro、lnp2pBot、RoboSats、Peach 以及其他 P2P 交易系统可以将订单以统一的事件格式公开，而不是将流动性封锁在各自独立的应用中。

可选的 `g` 标签还使本地面对面交易成为可能，而无需更改订单模式的其他部分。这很有用，因为本地现金交易需要地理过滤，而在线闪电网络交易则不需要。

## 安全与信任

`bond` 标签指定了双方都必须支付的保证金，提供对放弃交易或欺诈行为的保护。

但这并不消除交易对手风险。支付争议、法币欺诈、声誉和托管规则仍然存在于应用层。NIP-69 标准化了订单发布，而非争议解决。

---

**主要来源：**
- [NIP-69 规范](https://github.com/nostr-protocol/nips/blob/master/69.md)
- [Mostro 协议规范](https://mostro.network/protocol/)

**提及于：**
- [Newsletter #1：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #1：版本发布](/zh/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2：新闻](/zh/newsletters/2025-12-24-newsletter/#news)

**另请参阅：**
- [NIP-40：过期时间戳](/zh/topics/nip-40/)
