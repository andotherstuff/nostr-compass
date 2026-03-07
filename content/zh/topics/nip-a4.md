---
title: "NIP-A4：公开消息"
date: 2025-12-24
draft: false
translationOf: /en/topics/nip-a4.md
translationDate: 2026-03-07
categories:
  - Protocol
  - Social
---

NIP-A4 定义了公开消息（kind 24），专为通知界面设计，目标是获得广泛的客户端支持。

## 工作原理

Kind `24` 是发送给一个或多个接收者的签名明文消息。消息正文存放在 `content` 中，`p` 标签标识目标接收者。规范要求客户端将这些事件发送到接收者的 [NIP-65](/zh/topics/nip-65/) 收件箱中继和发送者的发件箱中继。

与线程对话不同，这些消息没有聊天历史、房间状态或线程根的概念。它们旨在出现在通知界面中，并且可以独立理解。

## 协议规则

- 使用 `p` 标签标识接收者
- 不得使用 `e` 标签进行线程化
- 可以使用 `q` 标签引用其他事件
- 与 [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md) 过期标签配合使用效果最佳，使过时的通知式消息随时间消失

## 存在意义

NIP-A4 为客户端提供了一种比完整线程笔记更简单的公开消息原语。这对于提及式消息、轻量级致意或一次性通知很有用，在这些场景中构建永久对话树会增加超出价值的复杂性。

权衡在于这些消息是公开的。它们之所以容易在通知界面中显示，正是因为它们不创建私密会话状态。任何人只要看到它们就可以阅读和回复。

## 互操作说明

NIP-A4 容易与直接消息协议混淆，因为它指定了接收者，但它仍然是公开事件类型。客户端不应将 kind `24` 呈现为私密消息，也不应假设中继放置之外存在任何保密性。

---

**主要来源：**
- [NIP-A4 规范](https://github.com/nostr-protocol/nips/blob/master/A4.md)
- [NIP-A4 PR](https://github.com/nostr-protocol/nips/pull/1988)

**提及于：**
- [Newsletter #2：NIP 更新](/zh/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**另请参阅：**
- [NIP-01：基础协议](/zh/topics/nip-01/)
- [NIP-10：文本笔记线程化](/zh/topics/nip-10/)
