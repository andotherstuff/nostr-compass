---
title: "NIP-50: Search"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2025-12-31
draft: false
categories:
  - 协议
  - 中继
---

NIP-50定义了Nostr中继的通用搜索功能，允许客户端执行超越按标签或ID结构化查询的全文搜索。

## 工作原理

协议在REQ消息的过滤器对象中添加了`search`字段：

1. 客户端提交人类可读的搜索查询（例如"最佳nostr应用"）
2. 中继解释查询并与事件数据匹配，主要是`content`字段
3. 结果按相关性而非时间顺序排列
4. `limit`过滤器在相关性排序后应用

搜索过滤器可以与`kinds`和`ids`等其他约束组合，以进行更具体的查询。

## 搜索扩展

中继可以选择性地支持以下扩展参数：

- `include:spam` - 禁用默认垃圾邮件过滤
- `domain:<domain>` - 按已验证的NIP-05域名过滤
- `language:<code>` - 按ISO语言代码过滤
- `sentiment:<value>` - 按负面/中性/正面情绪过滤
- `nsfw:<true/false>` - 包含或排除NSFW内容

## 客户端注意事项

- 客户端应通过`supported_nips`字段检查中继功能
- 建议进行客户端结果验证
- 并非所有中继都实现搜索；它仍然是可选功能

---

**主要来源：**
- [NIP-50规范](https://github.com/nostr-protocol/nips/blob/master/50.md)

**提及：**
- [通讯 #3：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**另请参阅：**
- [NIP-11: 中继信息](/zh/topics/nip-11/)
