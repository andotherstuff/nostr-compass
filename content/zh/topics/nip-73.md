---
title: "NIP-73：外部内容标识符"
date: 2026-02-04
draft: false
translationOf: /en/topics/nip-73.md
translationDate: 2026-03-07
categories:
  - Protocol
  - Discovery
  - Metadata
---

NIP-73 定义了在 Nostr 事件中引用外部内容的标准方式。它使用 `i` 标签表示标识符本身，使用 `k` 标签表示标识符类型，以便客户端围绕相同的书籍、网站、播客单集、地点、话题标签或区块链对象组织讨论。

## 工作原理

使用 NIP-73 的事件包含一个 `i` 标签（包含规范化的外部标识符）和一个 `k` 标签（描述标识符的类型）。客户端可以查询引用同一主题的所有事件。

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

规范涵盖多种标识符类别，包括：

- 不含片段的规范化网页 URL
- 书籍的 ISBN
- 电影的 ISAN
- geohash 以及 ISO 3166 国家或分区代码
- 播客 feed、单集和发布者的 GUID
- 话题标签
- 区块链交易和地址标识符

## 规范化规则

NIP-73 中面向使用者的关键细节是规范化。相同的主题应映射到一个规范字符串，否则客户端会将讨论分散到多个含义相同的标识符上。

规范中的示例：

- geohash 使用 `geo:<value>` 且必须小写
- 国家和分区代码使用 `iso3166:<code>` 且必须大写
- ISBN 省略连字符
- 网页 URL 去掉片段
- 区块链交易哈希使用小写十六进制

这看似微小，但它决定了是一场共享的对话还是多个互不兼容的索引。

## 实用模式

NIP-73 是通用的引用层，不是内容格式。长文笔记可以指向一个书籍 ISBN，评论可以指向一个电影 ISAN，本地帖子可以指向一个 geohash 或国家代码，而无需每次都发明一个自定义标签。

规范还允许将可选的 URL 提示作为 `i` 标签的第二个值。当客户端没有针对该标识符类型的自定义渲染器时，这为其提供了一个回退链接。

## 重要意义

Nostr 已经拥有强大的内部引用机制用于事件和用户档案。NIP-73 将这一理念扩展到 Nostr 之外的事物。一旦标识符规范化，评论、评分、高亮和可信断言都可以跨不同客户端关联到同一个外部主题。

这也是 NIP-85 建立在 NIP-73 基础上的原因。可信断言不仅可以为用户和事件评分，还可以为 NIP-73 标识符（如书籍、网站、话题标签和地点）评分。

---

**主要来源：**
- [NIP-73 规范](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - 添加 ISO 3166 国家和分区代码

**提及于：**
- [Newsletter #8：NIP 更新](/zh/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #10：NIP-85 深度解析](/zh/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)

**另请参阅：**
- [NIP-85：可信断言](/zh/topics/nip-85/)
