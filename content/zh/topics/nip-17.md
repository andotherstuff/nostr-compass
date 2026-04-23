---
title: "NIP-17：私密私信"
date: 2025-12-17
translationOf: /en/topics/nip-17.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17 使用 NIP-59 gift wrapping 来定义私密私信，并为发送者提供隐私。与在外层 event 中暴露发送者的 NIP-04 DM 不同，NIP-17 会把发送者从 relays 和普通观察者面前隐藏起来。

## 工作原理

消息会被包裹在多层加密之中：
1. 实际消息内容位于 kind 14 的 rumor event 中。
2. 一个 seal 会把该内容加密给接收方。
3. 一个 gift wrap 再次加密 seal，并由一次性 keypair 发布。

最外层的 gift wrap 使用随机的一次性 keypair，因此 relays 和观察者无法判断消息是谁发出的。

## 消息结构

- **Kind 14** - 包裹层内部真正的 DM 内容
- **Kind 1059** - 发布到 relays 的最外层 gift wrap event
- 包裹流程内部的 payload 使用 NIP-44 加密
- 规范后来也做过调整，以更好支持 reactions 等交互式 DM 功能

## 安全与信任模型

- relay 看不到发送者（gift wrap 的一次性 keypair 把它隐藏起来）
- 接收者仍然可见（体现在 gift wrap 的 `p` tag 中）
- 消息时间戳会在一个时间窗口内随机化
- relay 上不会暴露线程结构或会话分组

接收者在解包之后仍然会知道是谁发来的。NIP-17 隐藏的是发送者相对于网络的位置，而不是相对于对话另一方的身份。这一点在把它描述为“私密 DM”时很重要。

## 为什么重要

NIP-04 能加密内容，但会让元数据保持可见：
- 发送者 pubkey 公开可见
- 接收者 pubkey 在 `p` tag 中
- 时间戳完全精确

NIP-17 通过更复杂的实现换来了发送者隐私。

这种复杂性带来了真实的隐私提升。relay 仍然能看出一条包裹后的消息是发给某个接收者的，但它无法像面对 kind 4 消息那样，仅通过外层 event 元数据直接画出发送者与接收者之间的关系图。

## 互操作说明

NIP-17 还定义了用于私密消息的 inbox relay lists。客户端可以发布 kind 10050 event，让发送者知道应把 DM 发往哪些 relays。把 DM 路由与公开内容路由分开，有助于避免把私密流量发错地方。

---

**主要来源：**
- [NIP-17 规范](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - wording cleanup 与 reaction support 更新

**提及于：**
- [Newsletter #1：NIP 更新](/zh/newsletters/2025-12-17-newsletter/)
- [Newsletter #2：News](/zh/newsletters/2025-12-24-newsletter/)
- [Newsletter #3：December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #3：Notable Code Changes](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #5：News](/zh/newsletters/2026-01-13-newsletter/)
- [Newsletter #13：Vector](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19：NipLock 密码管理器](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-04：加密私信（已弃用）](/zh/topics/nip-04/)
- [NIP-44：加密载荷](/zh/topics/nip-44/)
- [NIP-59：Gift Wrap](/zh/topics/nip-59/)
