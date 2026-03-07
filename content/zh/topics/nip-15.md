---
title: "NIP-15：Nostr 市场"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15 为 Nostr 上的去中心化市场定义了协议，使商家能够列出商品，买家能够使用 Bitcoin 和 Lightning 进行购买。

## 工作原理

### 商家摊位（Kind 30017）

商家将摊位创建为可寻址事件：

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

### 商品（Kind 30018）

商品在摊位内列出：

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

1. 买家浏览多个摊位的商品
2. 买家向商家发送加密的订单消息
3. 商家回复 Lightning 发票
4. 买家支付发票
5. 商家发货

## 重要意义

- **去中心化**：没有中心化的市场运营商
- **互操作性**：任何 NIP-15 客户端都可以浏览任何商家
- **隐私保护**：订单在买家和卖家之间加密
- **Bitcoin 原生**：内置 Lightning 支付

实际的收益在于可移植性。商家只需发布一次目录数据，就可以让多个客户端渲染它，而不是被锁定在某个市场前端中。

## 权衡

NIP-15 标准化的是商品列表，而非信任。买家仍然需要判断商家是否合法、库存是否真实以及如何处理纠纷。协议提供了通用的数据结构和消息流，但声誉和履约仍然是应用层面的问题。

支付和物流也只是部分标准化。客户端可以理解摊位和商品，但仍然可能需要自定义逻辑来处理发票、订单状态或物流跟踪。

## 实现状态

- **Plebeian Market** - 功能完整的 NIP-15 市场
- **Shopstr** - 无需许可的 Bitcoin 商业平台
- **Amethyst** - 在社交信息流中集成商品列表

---

**主要来源：**
- [NIP-15 规范](https://github.com/nostr-protocol/nips/blob/master/15.md)

**提及于：**
- [第7期周刊：2024年1月协议加固](/zh/newsletters/2026-01-28-newsletter/#january-2024-protocol-hardening)

**另请参阅：**
- [NIP-44：加密载荷](/zh/topics/nip-44/)
- [NIP-57：Lightning Zaps](/zh/topics/nip-57/)
