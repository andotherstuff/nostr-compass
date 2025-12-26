---
title: "NIP-59：Gift Wrap"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 定义了 gift wrapping，一种通过用一次性身份的多层加密包裹事件来隐藏发送者的技术。

## 结构

gift-wrapped 事件有三层：

1. **Rumor** - 原始未签名事件内容
2. **Seal**（kind 13）- 加密给接收者的 rumor，由真正的发送者签名
3. **Gift Wrap**（kind 1059）- 加密给接收者的 seal，由随机的一次性密钥签名

外层使用仅为此消息生成的随机密钥对，因此观察者无法将其链接到发送者。

## 为什么是三层？

- **rumor** 包含实际内容
- **seal** 证明真正的发送者（仅接收者可见）
- **gift wrap** 对中继和观察者隐藏发送者

## 删除支持

Gift wrap 事件现在可以通过 NIP-09/NIP-62 删除请求删除。这是为了允许用户从中继移除包裹的消息而添加的。

## 使用场景

- 私密直接消息（NIP-17）
- 匿名提示或举报
- 任何发送者隐私重要的场景

---

**主要来源：**
- [NIP-59 规范](https://github.com/nostr-protocol/nips/blob/master/59.md)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)
- [第1期周刊：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)

**另请参阅：**
- [NIP-17：私密直接消息](/zh/topics/nip-17/)

