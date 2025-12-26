---
title: "NIP-A4：公开消息"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-A4 定义了为通知屏幕设计的公开消息（kind 24），目标是获得广泛的客户端支持。

## 工作原理

与线程对话不同，这些消息没有聊天历史或消息链的概念。它们是简单的一次性消息，旨在出现在接收者的通知信息流中。

## 结构

- 使用 `q` 标签（引用）而不是 `e` 标签以避免线程复杂性
- 没有对话状态或历史
- 为简单公开通知设计

## 使用场景

- 公开致谢或喊话
- 向用户广播消息
- 不需要回复线程的通知

---

**主要来源：**
- [NIP-A4 PR](https://github.com/nostr-protocol/nips/pull/1988)

**提及于：**
- [第2期周刊：NIP 更新](/zh/newsletters/2025-12-24-newsletter/#nip-updates)

**另请参阅：**
- [NIP-01：基础协议](/zh/topics/nip-01/)
- [NIP-10：文本笔记线程](/zh/topics/nip-10/)

