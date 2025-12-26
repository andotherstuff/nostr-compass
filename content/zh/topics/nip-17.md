---
title: "NIP-17：私密直接消息"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17 使用 NIP-59 gift wrapping 定义私密直接消息以保护发送者隐私。与暴露发送者的 NIP-04 私信不同，NIP-17 消息隐藏了发送消息的人。接收者在外层 gift wrap 中仍然可见。

## 工作原理

消息被包裹在多层加密中：
1. 实际消息内容（kind 14）
2. 将内容加密给接收者的 seal
3. 隐藏发送者身份的 gift wrap

外层 gift wrap 使用随机的一次性密钥对，因此中继和观察者无法确定谁发送了消息。

## 消息结构

- **Kind 14** - 实际的私信内容（在 seal 内部）
- 内容使用 NIP-44 加密
- 支持私信对话中的反应（kind 7）

## 隐私保证

- 中继无法看到发送者（被 gift wrap 的一次性密钥对隐藏）
- 接收者可见（在 gift wrap 的 `p` 标签中）
- 消息时间戳在一个窗口内随机化
- 中继上没有可见的线程或对话分组

## 与 NIP-04 的比较

NIP-04 私信加密内容但保留可见的元数据：
- 发送者公钥是公开的
- 接收者公钥在 `p` 标签中
- 时间戳是精确的

NIP-17 以更复杂的实现为代价隐藏了发送者。

---

**主要来源：**
- [NIP-17 规范](https://github.com/nostr-protocol/nips/blob/master/17.md)

**提及于：**
- [第1期周刊：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)
- [第2期周刊：新闻动态](/zh/newsletters/2025-12-24-newsletter/#news)

**另请参阅：**
- [NIP-59：Gift Wrap](/zh/topics/nip-59/)

