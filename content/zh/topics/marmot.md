---
title: "Marmot 协议"
date: 2025-12-17
translationOf: /en/topics/marmot.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot 是一个在 Nostr 上实现端到端加密群组消息的协议。它将 Nostr 的身份和中继网络与 MLS 结合，用于群组密钥管理、前向保密和泄露后安全。

## 工作原理

Marmot 使用 Nostr 处理身份、中继传输和事件分发，然后在其上层叠加 MLS 以处理群组成员变更和消息加密。与专注于一对一消息的 [NIP-17](/zh/topics/nip-17/) 不同，Marmot 是为成员随时间加入、离开或轮换密钥的群组而构建的。

## 重要意义

MLS 赋予 Marmot 一些 Nostr 的直接消息方案本身不具备的属性：群组状态演进、成员移除语义，以及在密钥泄露后通过后续密钥更新进行恢复。

这种职责分离是关键洞察。Nostr 在开放网络中解决身份和传输问题，MLS 解决经过身份验证的群组密钥协商问题，Marmot 则是两者之间的粘合层。

## 实现状态

该协议仍处于实验阶段，但现在已有多个实现和活跃的应用使用。MDK 是主要的 Rust 参考技术栈，`marmot-ts` 将该模型带到 TypeScript，White Noise、Pika 和 Vector 等应用一直在使用 Marmot 兼容的组件。

近期工作聚焦于加固和互操作性。审计驱动的修复在 2026 年初落地，MIP-03 引入了确定性提交解析，使客户端在并发群组状态变更通过中继竞争时能够收敛。

---

**主要来源：**
- [Marmot 协议仓库](https://github.com/marmot-protocol/marmot)
- [NIP-104：基于 MLS 的加密群聊](/zh/topics/nip-104/)
- [Marmot 开发套件](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)
- [第1期周刊：版本发布](/zh/newsletters/2025-12-17-newsletter/#releases)
- [第4期周刊](/zh/newsletters/2026-01-07-newsletter/)
- [第7期周刊](/zh/newsletters/2026-01-28-newsletter/)
- [第12期周刊](/zh/newsletters/2026-03-04-newsletter/)

**另请参阅：**
- [MLS（消息层安全）](/zh/topics/mls/)
- [MIP-05：隐私保护推送通知](/zh/topics/mip-05/)
- [NIP-17：私密直接消息](/zh/topics/nip-17/)
- [NIP-59：Gift Wrap](/zh/topics/nip-59/)
