---
title: "NIP-40：过期时间戳"
date: 2025-12-17
draft: false
translationOf: /en/topics/nip-40.md
translationDate: 2026-03-07
categories:
  - Protocol
---

NIP-40 定义了一个过期标签，用于告知中继何时应该删除事件。

## 工作原理

事件中包含一个带有 Unix 时间戳的 `expiration` 标签：

```json
["expiration", "1734567890"]
```

过了这个时间后，中继应该删除该事件并拒绝提供服务。

## 重要意义

- 应在设定时间后消失的临时内容
- 有时效限制的优惠或公告
- 市场中的商品过期（如 Shopstr）
- 减少中继存储需求

过期是一种保留提示，而非撤销系统。它有助于统一中继对过时内容的处理行为，但一旦其他中继、客户端或归档已经复制了该事件，它并不保证内容被彻底删除。

## 信任与安全说明

- 中继不强制要求遵守过期设置（但大多数会遵守）
- 客户端不应依赖过期机制来删除安全敏感内容
- 内容一旦被其他客户端获取，可能会被缓存或重新发布
- 过期不会隐藏事件曾经存在的事实。事件 ID、引用或中继外的副本可能在时间戳过后仍然存在

---

**主要来源：**
- [NIP-40 规范](https://github.com/nostr-protocol/nips/blob/master/40.md)

**提及于：**
- [Newsletter #1：新闻](/zh/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3：重要代码变更](/zh/newsletters/2025-12-31-newsletter/#rust-nostr-library)

**另请参阅：**
- [NIP-01：基础协议](/zh/topics/nip-01/)
