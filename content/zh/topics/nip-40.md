---
title: "NIP-40：过期时间戳"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-40 定义了一个过期标签，告诉中继何时应该删除事件。

## 结构

事件包含带有 Unix 时间戳的 `expiration` 标签：

```json
["expiration", "1734567890"]
```

在此时间之后，中继应该删除事件并拒绝提供它。

## 使用场景

- 应在设定时间后消失的临时内容
- 限时优惠或公告
- 市场中的商品过期（例如 Shopstr）
- 减少中继存储需求

## 注意事项

- 中继不强制要求遵守过期时间（但大多数会遵守）
- 客户端不应依赖过期来删除安全关键内容
- 一旦内容被其他客户端获取，它可能被缓存或重新发布

---

**主要来源：**
- [NIP-40 规范](https://github.com/nostr-protocol/nips/blob/master/40.md)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)

