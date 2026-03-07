---
title: "ContextVM"
date: 2026-02-25
translationOf: /en/topics/contextvm.md
translationDate: 2026-03-07
draft: false
categories:
  - Infrastructure
  - AI
  - Protocol
---

ContextVM 是一个用于通过 Nostr 传输 MCP（Model Context Protocol）流量的协议和工具链。它让 MCP 客户端和服务器能够相互发现并交换签名消息，而无需依赖中央注册表、域名或 OAuth。

## 工作原理

ContextVM SDK 提供了用于 MCP over Nostr 的 TypeScript 客户端和服务器传输层。现有的 MCP 服务器可以继续使用其常规传输方式，同时通过网关将其暴露给 Nostr；没有原生 Nostr 支持的客户端可以通过代理层连接。

中继充当消息总线。它们路由事件，而签名和加密为端点提供身份验证和传输隐私。

## 组件

**SDK**：TypeScript 库，提供客户端/服务器传输、代理支持以及将本地 MCP 服务器桥接到 Nostr 的网关功能。

**CVMI**：用于服务器发现和方法调用的命令行界面。

**Relatr**：信任评分服务，根据社交图谱距离和个人资料验证计算个性化评分。

## 重要意义

ContextVM 是一个传输桥接层，而非 MCP 本身的替代品。这一点很重要，因为它降低了采用成本：现有的 MCP 服务器无需重写其工具模式或业务逻辑即可获得 Nostr 可达性。

近期的 ContextVM 工作还推进了 gift-wrapped 流量的临时投递。这对于工具调用和中间响应很有用，因为这些场景下持久的中继存储是不必要的，还可能产生额外的隐私暴露。

## 互操作说明

2026 年 2 月和 3 月，该项目从实现阶段转向标准化。团队提交了关于 MCP JSON-RPC over Nostr 以及 gift wrap 临时变体的 NIP 提案。即使这些提案发生变化，它们也更清晰地展示了协议边界：MCP 保持为应用层，Nostr 处理发现和传输。

---

**主要来源：**
- [ContextVM 网站](https://contextvm.org)
- [ContextVM SDK](https://github.com/ContextVM/sdk)
- [CVMI CLI](https://github.com/ContextVM/cvmi)
- [Relatr](https://github.com/ContextVM/relatr)
- [NIP PR #2245：临时 Gift Wrap](https://github.com/nostr-protocol/nips/pull/2245)
- [NIP PR #2246：MCP JSON-RPC over Nostr](https://github.com/nostr-protocol/nips/pull/2246)

**提及于：**
- [第11期周刊：ContextVM 新闻](/zh/newsletters/2026-02-25-newsletter/#contextvm-mcp-over-nostr)
- [第12期周刊](/zh/newsletters/2026-03-04-newsletter/)

**另请参阅：**
- [NIP-90：数据自动售货机](/zh/topics/nip-90/)
