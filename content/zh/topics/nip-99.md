---
title: "NIP-99：分类信息"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - 商务
  - 市场
---

NIP-99 定义了面向商品、服务、工作、租赁和其他报价的可寻址分类信息事件。它为市场类应用提供了比旧的 [NIP-15](/zh/topics/nip-15/) 市场规范更简单的事件模型，这也是为什么许多当前的商务客户端更倾向于基于 NIP-99 构建。

## 工作原理

活跃的列表使用 kind `30402`，草稿或非活跃列表使用 kind `30403`。作者 pubkey 就是卖家或报价创建者。`content` 字段承载人类可读的 Markdown 描述，而标签则保存诸如标题、摘要、价格、位置和状态等结构化字段。

```json
{
  "id": "b3e392b11f5d4f28321cedd09303a748acfd0487aea5a7450b3481c60b6e4f87",
  "pubkey": "a695f6b60119d9521934a691347d9f78e8770b56da16bb255ee286ddf9fda919",
  "created_at": 1741699200,
  "kind": 30402,
  "tags": [
    ["d", "shopstr-handmade-wallet-001"],
    ["title", "Handmade leather wallet"],
    ["summary", "Brown bifold wallet with Bitcoin and Nostr branding"],
    ["published_at", "1741699200"],
    ["location", "Austin, TX"],
    ["price", "75000", "SAT"],
    ["status", "active"],
    ["t", "merch"],
    ["t", "bitcoin"]
  ],
  "content": "Full listing description in Markdown, shipping details, and contact terms.",
  "sig": "4a5c7e8f9012ab34cd56ef7890ab12cd34ef56ab78cd90ef12ab34cd56ef78900112233445566778899aabbccddeeff00112233445566778899aabbccddeeff"
}
```

这个事件是可寻址的，因此卖家可以在保持相同身份元组，也就是 pubkey、kind 和 `d` 标签不变的情况下更新列表内容。与每次价格或状态变更都重新发布一条全新的不可变笔记相比，这让客户端处理列表修订更加干净。

## 为什么重要

NIP-99 的优势在于，它在标准化核心列表结构的同时，仍为不同市场设计留下了空间。一个客户端可以专注本地分类信息，另一个可以围绕订阅构建，第三个可以做全球商品目录。只要它们对事件结构达成一致，卖家发布一次，就仍然有机会在不同客户端之间获得可见性。

这种灵活性也解释了为什么当前的市场项目偏好它。规范的结构足够支撑搜索和展示，但它并不会强迫每个应用采用同一种托管、配送或支付工作流。

## 实现说明

- `price` 标签可以通过附加可选的频率字段来描述一次性或周期性支付。
- `t` 标签可以作为分类或搜索关键词使用。
- `image` 标签让客户端无需解析 Markdown 正文就能渲染图库视图。
- 当市场想提供更丰富的商品上下文时，列表可以通过 `e` 或 `a` 标签链接到相关事件或文档。

## 实现

- [Shopstr](https://github.com/shopstr-eng/shopstr) - 使用 NIP-99 列表并提供面向 agent 的 MCP 端点的 Nostr 市场
- [Milk Market](https://github.com/shopstr-eng/milk-market) - 构建在同一列表层之上的食品市场，支持混合支付选项

---

**主要来源：**
- [NIP-99 规范](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - 构建在 NIP-99 列表之上的 MCP 商务端点
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - 构建在市场列表之上的订阅和多商户结账

**提及于：**
- [Newsletter #13：Shopstr 和 Milk Market 开放 MCP 商务接口](/zh/newsletters/2026-03-11-newsletter/)

**另请参阅：**
- [NIP-15：市场报价](/zh/topics/nip-15/)
- [NIP-47：Nostr Wallet Connect](/zh/topics/nip-47/)
- [NIP-60：Cashu Wallet](/zh/topics/nip-60/)
