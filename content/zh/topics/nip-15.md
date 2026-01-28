---
title: "NIP-15：Nostr 市场"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15 定义了 Nostr 上去中心化市场的协议，使商家能够列出商品，买家能够使用 Bitcoin 和 Lightning 进行购买。

## 工作原理

### 商家店铺 (Kind 30017)

商家创建店铺作为可寻址事件：

```json
{
  "kind": 30017,
  "tags": [
    ["d", "my-stall"],
    ["name", "Bob's Electronics"],
    ["description", "Quality used electronics"],
    ["currency", "sat"],
    ["shipping", "{...shipping options...}"]
  ]
}
```

### 商品 (Kind 30018)

商品在店铺内列出：

```json
{
  "kind": 30018,
  "tags": [
    ["d", "product-123"],
    ["stall_id", "my-stall"],
    ["name", "Raspberry Pi 4"],
    ["price", "50000"],
    ["quantity", "5"],
    ["images", "https://..."]
  ]
}
```

## 购买流程

1. 买家浏览多个店铺的商品
2. 买家向商家发送加密的订单消息
3. 商家回复 Lightning 发票
4. 买家支付发票
5. 商家发货

## 主要特性

- **去中心化**：没有中心化的市场运营商
- **可互操作**：任何 NIP-15 客户端都可以浏览任何商家
- **私密**：订单在买卖双方之间加密
- **Bitcoin 原生**：内置 Lightning 支付

## 实现

- **Plebeian Market** - 功能完整的 NIP-15 市场
- **Shopstr** - 无需许可的 Bitcoin 商务
- **Amethyst** - 在社交信息流中集成商品列表

## 相关

- [NIP-44](/zh/topics/nip-44/) - 订单的加密消息
- [NIP-57](/zh/topics/nip-57/) - Lightning Zaps
