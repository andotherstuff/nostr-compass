---
title: "Gamma Markets"
date: 2026-07-15
draft: false
translationOf: /en/topics/gamma-markets.md
translationDate: 2026-07-15
categories:
  - Commerce
  - Marketplace
  - Protocol
---

Gamma Markets 是一套直接构建在 [NIP-99](/zh/topics/nip-99/) 分类广告之上的电商约定，由一个 Nostr 市场开发者工作组协作制定，即 Shopstr、Cypher、Plebeian Market 和 Conduit Market 背后的团队。它补齐了 NIP-99 自身未定义的配送、订单流程、合集和评价约定。

## 工作方式

Gamma Markets 围绕 NIP-99 既有的 kind `30402` 广告事件加入五个事件 kind，且不改变该事件的形态：

- **kind 30405** - 商品合集，通过 `a` tag 把多条广告归为一组
- **kind 30406** - 配送选项，带有按国家的定价和可选的按重量或距离计费规则
- **kind 16** - 订单消息：创建（type 1）、付款请求（type 2）、状态更新（type 3）和配送更新（type 4）
- **kind 14** - 买家与商家之间的一般沟通
- **kind 17** - 付款收据
- **kind 31555** - 商品评价，寻址到特定的卖家 pubkey 和广告 `d` tag

商家的付款偏好通过其 kind `0` 个人资料元数据上的 `payment_preference` tag 声明，客户端则通过 [NIP-89](/zh/topics/nip-89/) 应用推荐发现兼容的应用。订单沟通构建在 [NIP-17](/zh/topics/nip-17/) 私密消息之上，没有自己新的加密方案。

该规范的决定性设计选择是：任何东西都不会向下继承。属于某个合集、或使用某个配送选项的广告，都用 `a` tag 显式引用它，而不是自动继承父级的设置。这是对更早的 [NIP-15](/zh/topics/nip-15/) 摊位模型的刻意背离，在那个模型里，商品会默默继承其摊位的货币和运费表。

### 示例：订单创建（kind 16，type 1）

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

## 为何重要

单靠 NIP-99 只标准化了广告本身，即一条签名的、可寻址的分类广告。在 Gamma Markets 之前，每个在 NIP-99 上构建真实电商的客户端都会为配送、结账和评价发明自己的私有约定，这意味着两个符合 NIP-99 的客户端可以各自正确渲染广告，却没有共同的方式在彼此之间完成一笔订单。Gamma Markets 在不触动 NIP-99 广告格式本身的前提下填补了这一空白，因此既有的 NIP-99 广告无需修改即保持有效。

## 实现

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Nostr 市场，编写该规范的四个项目之一
- [Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) - 市场协议，在同一设计空间中构建自己的订单状态与结账流程

---

**主要来源：**
- [Gamma Markets 规范仓库](https://github.com/GammaMarkets/market-spec)
- [NIP-99 电商用例扩展，PR #1784](https://github.com/nostr-protocol/nips/pull/1784) - 从 NIP-99 规范文档链接到 Gamma Markets 规范的已合并链接

**提及于：**
- [Newsletter #31：NIP Deep Dive：NIP-99 与 Gamma Markets 商务扩展](/zh/newsletters/2026-07-15-newsletter/#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)

**另见：**
- [NIP-99: Classified Listings](/zh/topics/nip-99/)
- [NIP-15: Nostr Marketplace](/zh/topics/nip-15/)
- [NIP-17: Private Direct Messages](/zh/topics/nip-17/)
