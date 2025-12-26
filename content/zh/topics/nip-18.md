---
title: "NIP-18：转发"
date: 2025-12-17
draft: false
categories:
  - Social
  - Protocol
---

NIP-18 定义了如何转发事件，类似于其他平台上的转推。

## 结构

转发是一个 kind 6 事件（用于 kind 1 笔记）或 kind 16（通用转发），包含：
- 引用被转发事件的 `e` 标签
- 引用原作者的 `p` 标签
- 可选地，在 `content` 字段中包含完整的原始事件

## 近期变更

改进了对可替换事件的转发支持，添加了 `a` 标签支持。这允许转发可寻址事件（kinds 30000-39999）时通过地址引用它们，而不是特定的事件 ID。

---

**主要来源：**
- [NIP-18 规范](https://github.com/nostr-protocol/nips/blob/master/18.md)

**提及于：**
- [第1期周刊：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)

**另请参阅：**
- [NIP-01：基础协议](/zh/topics/nip-01/)

