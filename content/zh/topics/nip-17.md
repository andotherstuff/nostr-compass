---
title: "NIP-17：私密直接消息"
date: 2025-12-17
translationOf: /en/topics/nip-17.md
translationDate: 2026-03-11
draft: false
categories:
  - 隐私
  - 消息
---

NIP-17 使用 NIP-59 gift wrapping 定义了具有发送者隐私保护的私密直接消息。与在外层事件中暴露发送者的 NIP-04 私信不同，NIP-17 将发送者隐藏于 relay 和普通观察者之外。

## 工作原理

消息被包裹在多层加密中：
1. 实际消息内容存在于 kind 14 的 rumor 事件中。
2. seal 将该内容加密给接收者。
3. gift wrap 再次加密 seal，并使用一次性密钥对发布。

外层 gift wrap 使用随机的一次性密钥对，因此 relay 和观察者无法确定谁发送了消息。

## 消息结构

- **Kind 14** - 包裹层内部的实际私信内容
- **Kind 1059** - 发布到 relay 的外层 gift wrap 事件
- 在包裹流程中使用 NIP-44 加密载荷
- 规范已优化以更好地支持交互式私信功能，如反应

## 安全与信任模型

- relay 无法看到发送者（被 gift wrap 的一次性密钥对隐藏）
- 接收者可见（在 gift wrap 的 `p` 标签中）
- 消息时间戳在一个时间窗口内随机化
- relay 上没有可见的线程或对话分组

接收者在解包后仍然能知道谁发送了消息。NIP-17 隐藏的是发送者身份不被网络看到，而非不被对方看到。当人们将其描述为"私密私信"时，这是一个重要的区别。

## 重要意义

NIP-04 私信加密内容但保留可见的元数据：
- 发送者公钥是公开的
- 接收者公钥在 `p` 标签中
- 时间戳是精确的

NIP-17 以更复杂的实现为代价隐藏了发送者。

这种复杂性换来了真正的隐私改善。relay 仍然能看到一条包裹消息的收件人，但它无法像处理 kind 4 消息那样，直接从外层事件元数据构建发送者-接收者关系图。

## 互操作说明

NIP-17 还定义了用于私密消息的收件箱 relay 列表。客户端可以发布 kind 10050 事件，以便发送者知道应将私信投递到哪些 relay。将私信 relay 路由与公共内容路由分开，有助于避免将私密流量发布到错误的位置。

---

**主要来源：**
- [NIP-17 规范](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - 措辞清理和反应支持更新

**提及于：**
- [第1期周刊：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)
- [第2期周刊：新闻动态](/zh/newsletters/2025-12-24-newsletter/#news)
- [第3期周刊：12月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [第3期周刊：重要代码变更](/zh/newsletters/2025-12-31-newsletter/#shopstr-marketplace)
- [第5期周刊：新闻动态](/zh/newsletters/2026-01-13-newsletter/#news)

**另请参阅：**
- [NIP-04：加密直接消息（已弃用）](/zh/topics/nip-04/)
- [NIP-44：加密载荷](/zh/topics/nip-44/)
- [NIP-59：Gift Wrap](/zh/topics/nip-59/)
