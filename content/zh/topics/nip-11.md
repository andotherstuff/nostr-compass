---
title: "NIP-11：中继信息"
date: 2025-12-17
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 定义了中继如何暴露关于自身的元数据，包括支持的 NIPs、限制和联系信息。

## 工作原理

客户端通过向中继的 WebSocket URL 发送带有 `Accept: application/nostr+json` 头的 HTTP GET 请求来获取中继信息。中继返回描述其功能的 JSON 文档。

## 关键字段

- **name** - 人类可读的中继名称
- **description** - 中继的用途
- **supported_nips** - 已实现的 NIP 列表
- **limitation** - 限制，如最大消息大小、是否需要认证等
- **self** - 中继自己的公钥（用于中继身份的新字段）

## 使用场景

- 客户端可以在连接前检查中继是否支持所需功能
- 发现服务可以索引中继功能
- 用户可以在发布前查看中继策略

---

**主要来源：**
- [NIP-11 规范](https://github.com/nostr-protocol/nips/blob/master/11.md)

**提及于：**
- [第1期周刊：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)

