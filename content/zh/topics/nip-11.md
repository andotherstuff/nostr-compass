---
title: "NIP-11：中继器信息文档"
date: 2025-12-17
draft: false
translationOf: /en/topics/nip-11.md
translationDate: 2026-03-11
categories:
  - 中继
  - 协议
---

NIP-11 定义了中继器如何发布其机器可读的自我描述，包括声明的功能支持、限制和运营者元数据。

## 工作原理

客户端通过向中继器的 WebSocket URL 发送带有 `Accept: application/nostr+json` 头的 HTTP GET 请求来获取中继器信息。中继器返回一个描述其功能的 JSON 文档。

## 常用字段

- **name** - 人类可读的中继器名称
- **description** - 中继器的用途说明
- **supported_nips** - 声明支持的 NIP 列表
- **limitation** - 限制条件，如最大消息大小、是否要求认证等
- **pubkey** - 中继器运营者的公钥（如果提供）
- **contact** - 运营者联系方式

## 信任模型

NIP-11 是自我报告的元数据。它告诉你中继器对自身的描述，而非它在实际流量中已证明的能力。这对于发现和用户体验仍然有用，但客户端不应在未测试实际行为的情况下将 `supported_nips` 视为事实。

这一区分对中继器选择很重要。中继器可能宣称支持 NIP-50 搜索、认证要求或大消息限制，但真正的答案只有在客户端实际连接并执行这些代码路径后才会显现。

## 重要意义

- 客户端可以在连接之前检查中继器是否支持所需功能
- 发现服务可以索引中继器能力
- 用户可以在发布之前查看中继器策略

## 近期规范方向

规范随时间进行了精简。较旧的可选字段如 `software`、`version`、隐私策略详情和保留元数据在多年采用率低迷后被移除。这使得当前的 NIP-11 文档更小、更贴近实际，但也意味着客户端不应期望从中继器获取丰富的策略元数据。

---

**主要来源：**
- [NIP-11 规范](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - 中继器身份字段更新
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - 清理很少使用的字段
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - 移除已弃用的字段

**提及于：**
- [第1期周刊：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)

**另请参阅：**
- [NIP-66：中继器发现与存活监测](/zh/topics/nip-66/)
