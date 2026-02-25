---
title: "NIP-09"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Protocol
---

NIP-09 定义了 Event 删除机制，允许用户请求 relay 移除其此前发布的 event。

## 工作原理

用户发布包含 `e` tag 的 kind 5 event，其中引用了待删除的 event ID。支持 NIP-09 的 relay 应停止提供被引用的 event，并可从存储中将其删除。

删除是一项请求，而非保证。Relay 可以忽略删除请求，且 event 可能已传播至不支持删除的 relay。用户不应依赖 NIP-09 来移除隐私敏感内容。

## 主要特性

- kind 5 删除请求 event
- 通过 e tag 按 ID 引用待删除的 event
- 可选的删除原因字段
- Relay 合规属自愿行为

---

**主要来源：**
- [NIP-09 规范](https://github.com/nostr-protocol/nips/blob/master/09.md)

**提及于：**
- [Newsletter #11：NIP-60 深入解析](/zh/newsletters/2026-02-25-newsletter/#nip-深入解析nip-60cashu-钱包)

**参见：**
- [NIP-60：Cashu 钱包](/zh/topics/nip-60/)
