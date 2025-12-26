---
title: "NIP-69：点对点交易"
date: 2025-12-17
draft: false
categories:
  - Trading
  - Protocol
---

NIP-69 定义了一个在 Nostr 上进行点对点交易的协议，创建跨多个平台的统一订单簿，而不是分散的流动性池。

## 事件 Kind

- **Kind 38383** - P2P 订单事件

## 订单结构

订单使用标签来指定交易参数：

- `d` - 订单 ID
- `k` - 订单类型（买入/卖出）
- `f` - 法币货币（ISO 4217 代码）
- `amt` - 比特币金额（聪）
- `fa` - 法币金额
- `pm` - 接受的支付方式
- `premium` - 价格溢价/折扣百分比
- `network` - 结算层（主链、闪电网络、Liquid）
- `expiration` - 订单过期时间

## 订单生命周期

订单经历以下状态：
- `pending` - 开放且可供匹配
- `in-progress` - 与对手方发起交易
- `success` - 交易完成
- `canceled` - 被挂单方撤回
- `expired` - 超过过期时间

## 安全性

`bond` 标签指定双方都必须支付的保证金，提供防止放弃或欺诈的保护。

---

**主要来源：**
- [NIP-69 规范](https://github.com/nostr-protocol/nips/blob/master/69.md)

**提及于：**
- [第1期周刊：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)
- [第1期周刊：版本发布](/zh/newsletters/2025-12-17-newsletter/#releases)
- [第2期周刊：新闻动态](/zh/newsletters/2025-12-24-newsletter/#news)

