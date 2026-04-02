---
title: "NIP-86：Relay 管理 API"
date: 2026-04-01
translationOf: /en/topics/nip-86.md
translationDate: 2026-04-01
draft: false
categories:
  - Relay
  - 协议
---

NIP-86 定义了一种用于 relay 管理的 JSON-RPC 接口，让授权客户端通过标准化 API 向 relay 发送管理命令。Relay 运营者可以封禁或允许 pubkey、管理访问列表以及查询 relay 状态，而无需 relay 特定的工具。

## 工作原理

管理 API 在与 relay WebSocket 端点相同的 URI 上使用类 JSON-RPC 请求通过 HTTP 进行通信。请求使用 `application/nostr+json+rpc` 内容类型，并在 `Authorization` 头中使用 [NIP-98](/zh/topics/nip-98/)（HTTP Auth）签名 event 进行认证。Relay 在执行命令前验证请求的 pubkey 是否在其管理员列表中。

可用方法包括封禁和允许 pubkey、列出被封禁用户以及查询 relay 配置。标准化接口意味着单个客户端实现可以管理任何兼容 NIP-86 的 relay。

## 实现

- [Amethyst](https://github.com/vitorpamplona/amethyst) - 带有 NIP-86 relay 管理 UI 的 Android 客户端（v1.07.0+）

---

**主要来源：**
- [NIP-86 规范](https://github.com/nostr-protocol/nips/blob/master/86.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - 客户端 NIP-86 支持
- [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) - Relay 管理用户搜索对话框

**提及于：**
- [周刊 #16：Amethyst 发布 relay 管理](/zh/newsletters/2026-04-01-newsletter/#amethyst-发布固定笔记relay-管理和-request-to-vanish)

**另见：**
- [NIP-11：Relay 信息文档](/zh/topics/nip-11/)
- [NIP-98：HTTP Auth](/zh/topics/nip-98/)
- [NIP-42：客户端对 Relay 的认证](/zh/topics/nip-42/)
