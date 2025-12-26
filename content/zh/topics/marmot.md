---
title: "Marmot 协议"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot 是一个建立在 Nostr 之上的端到端加密群组消息协议，使用消息层安全（MLS）标准实现前向保密和泄露后安全。

## 工作原理

Marmot 用基于 MLS 的群聊加密扩展了 Nostr。与一对一的 NIP-17 私信不同，Marmot 处理安全的群组通信，其中成员可以加入和离开，同时保持加密保证。

## 关键特性

- 通过 MLS 实现前向保密和泄露后安全
- 动态成员资格的群组密钥管理
- 通过 MIP-05 实现隐私保护推送通知

---

**主要来源：**
- [Marmot 协议仓库](https://github.com/marmot-protocol/marmot)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)
- [第1期周刊：版本发布](/zh/newsletters/2025-12-17-newsletter/#releases)

**另请参阅：**
- [MIP-05：隐私保护推送通知](/zh/topics/mip-05/)
- [NIP-17：私密直接消息](/zh/topics/nip-17/)
- [NIP-59：Gift Wrap](/zh/topics/nip-59/)

