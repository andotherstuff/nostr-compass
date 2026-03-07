---
title: "NIP-50：搜索"
date: 2025-12-31
draft: false
translationOf: /en/topics/nip-50.md
translationDate: 2026-03-07
categories:
  - Protocol
  - Relay
---

NIP-50 为 Nostr 中继定义了通用搜索功能。它在 NIP-01 的精确匹配过滤之上添加了全文检索式查询。

## 工作原理

该协议在 `REQ` 消息的过滤对象中添加了 `search` 字段：

1. 客户端提交人类可读的查询字符串，如 `best nostr apps`。
2. 中继将该查询与事件数据进行匹配，主要是 `content` 字段。
3. 结果按匹配质量排序，而非按 `created_at`。
4. `limit` 在相关性排序之后生效。

搜索过滤条件可以与 `kinds`、`ids`、作者和其他普通过滤字段组合使用，以实现更具体的查询。

## 搜索扩展

中继可以选择性地支持以下扩展参数：

- `include:spam` - 禁用默认的垃圾信息过滤
- `domain:<domain>` - 按已验证的 NIP-05 域名过滤
- `language:<code>` - 按 ISO 语言代码过滤
- `sentiment:<value>` - 按负面、中性或正面情绪过滤
- `nsfw:<true/false>` - 包含或排除 NSFW 内容

中继应忽略其不支持的扩展，因此客户端需要将它们视为提示而非保证。

## 互操作说明

- 客户端应通过 `supported_nips` 字段检查中继能力
- 建议在客户端侧验证结果
- 并非所有中继都实现了搜索功能；它仍然是一个可选特性

由于排名的实现因中继而异，相同的查询在不同中继上可能返回不同的结果集。关注召回率的客户端应查询多个搜索中继并合并结果。

## 重要意义

当你已经知道想要的作者、类型或标签时，结构化过滤条件效果很好。搜索则用于相反的情况：发现。这使得 NIP-50 对应用目录、长期归档和公开笔记搜索很有用，但也意味着搜索质量在很大程度上取决于每个中继的索引和垃圾信息过滤策略。

---

**主要来源：**
- [NIP-50 规范](https://github.com/nostr-protocol/nips/blob/master/50.md)

**提及于：**
- [Newsletter #3：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #7：NIP 更新](/zh/newsletters/2026-01-07-newsletter/#nip-updates)

**另请参阅：**
- [NIP-11：中继信息](/zh/topics/nip-11/)
