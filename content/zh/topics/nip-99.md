---
title: "NIP-99：分类列表"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - 商业
  - 市场
---

NIP-99 为商品、服务、工作、租赁和其他报价定义了可寻址的分类列表 event。它为市场应用提供了比旧版 [NIP-15](/zh/topics/nip-15/) 市场规范更简单的 event 模型，这就是为什么许多当前的商业客户端选择基于 NIP-99 构建。

## 工作原理

活跃列表使用 kind `30402`，而草稿或非活跃列表使用 kind `30403`。作者 pubkey 是卖方或报价创建者。`content` 字段以 Markdown 格式承载人类可读的描述，tag 保存标题、摘要、价格、位置和状态等结构化字段。

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

该 event 是可寻址的，因此卖方可以在保持相同的 pubkey、kind 和 `d` tag 身份元组的情况下更新列表。这使得列表修订对客户端来说比每次价格或状态变更都发布全新的不可变笔记更加简洁。

## 重要性

NIP-99 的优势在于它为不同的市场设计留有空间，同时仍然标准化了核心列表结构。一个客户端可以专注于本地分类广告，另一个专注于订阅，再一个专注于全球产品目录。如果它们都同意 event 结构，卖方只需发布一次，仍然可以获得一些跨客户端的可见性。

这种灵活性也解释了为什么当前的市场项目青睐它。该规范的结构足以支持搜索和展示，但它不会强迫每个应用采用单一的托管、运输或支付工作流。

## 实现说明

- `price` tag 可以通过添加可选的频率字段来描述一次性或周期性支付。
- `t` tag 充当分类或搜索关键词。
- `image` tag 让客户端无需解析 Markdown 正文即可渲染画廊视图。
- 当市场需要更丰富的产品上下文时，列表可以使用 `e` 或 `a` tag 链接到相关 event 或文档。

## 实现

- [Shopstr](https://github.com/shopstr-eng/shopstr) - 使用 NIP-99 列表并带有面向代理的 MCP 端点的 Nostr 市场
- [Milk Market](https://github.com/shopstr-eng/milk-market) - 基于相同列表层构建的食品市场，支持混合支付选项

---

**主要来源：**
- [NIP-99 规范](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - 基于 NIP-99 列表的 MCP 商业端点
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - 基于市场列表的订阅和多商户结账

**提及于：**
- [周刊 #13：Shopstr 和 Milk Market 开放 MCP 商业接口](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**另见：**
- [NIP-15：市场报价](/zh/topics/nip-15/)
- [NIP-47：Nostr Wallet Connect](/zh/topics/nip-47/)
- [NIP-60：Cashu 钱包](/zh/topics/nip-60/)
