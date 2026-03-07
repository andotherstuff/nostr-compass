---
title: "NIP-59：Gift Wrap"
date: 2025-12-17
translationOf: /en/topics/nip-59.md
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 定义了 gift wrap，一种封装事件的方式，使中继和外部观察者无法从接收到的外层事件中获知真正的发送者。

## 结构

Gift-wrapped 事件有三层：

1. **Rumor** - 没有签名的目标事件。
2. **Seal**（kind `13`）- 加密给接收者的 rumor，由真正的发送者签名。
3. **Gift Wrap**（kind `1059`）- 再次加密的 seal，由随机的一次性密钥签名。

Seal 必须有空标签。外层 gift wrap 通常携带接收者的 `p` 标签，以便中继进行路由。

## 隐藏了什么

Gift wrap 对中继和网络观察者隐藏了发送者，因为外层事件由一次性密钥签名。然而，接收者仍然可以解密内层 seal 并了解是哪个长期密钥签署的。因此隐私收益是传输层的元数据保护，而非对接收者的匿名性。

规范还建议随机化包装器时间戳，并在可能的情况下使用需要身份验证的中继，且仅向目标接收者提供 wrapped 事件。如果没有这些中继行为，接收者元数据仍可能泄露。

## 操作说明

Gift wrap 本身不是消息协议。其他协议（如私密消息系统）将其作为构建模块使用。

中继可能选择不长期存储 wrapped 事件，因为它们没有公共用途。规范还允许在外层包装器上使用工作量证明，用于需要额外垃圾信息防护的实现。

## 用例

- 私密直接消息（NIP-17）
- 仅好友可见的笔记（NIP-FR 提案）
- 推送通知载荷（NIP-9a 提案）
- 任何需要对网络隐藏发送者的场景

---

**主要来源：**
- [NIP-59 规范](https://github.com/nostr-protocol/nips/blob/master/59.md)

**提及于：**
- [第8期周刊：NIP 深度解析](/zh/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-59-gift-wrap)
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)
- [第1期周刊：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)
- [第3期周刊：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [第15期周刊：开放 PR 和项目更新](/zh/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**另请参阅：**
- [NIP-17：私密直接消息](/zh/topics/nip-17/)
