---
title: "NIP-11：Relay 信息文档"
date: 2025-12-17
translationOf: /en/topics/nip-11.md
translationDate: 2026-04-22
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11 定义了 relay 如何发布一份机器可读的自我描述，其中包括它声称支持的功能、限制条件以及运营者元数据。

## 工作原理

客户端通过向 relay 的 WebSocket URL 发起 HTTP GET 请求，并带上 `Accept: application/nostr+json` 头来获取 relay 信息。relay 会返回一份描述自身能力的 JSON 文档。

## 常用字段

- **name** - 人类可读的 relay 名称
- **description** - relay 的用途说明
- **supported_nips** - 声称支持的 NIP 列表
- **limitation** - 例如最大消息大小、是否需要 auth 等限制
- **pubkey** - relay 运营者公钥（若提供）
- **contact** - 运营者联系方式

## 信任模型

NIP-11 是自报的元数据。它告诉你 relay 自己如何描述自己，而不是它在真实流量里已经证明过什么。这对发现和 UX 仍然很有用，但客户端不应在未经测试的情况下，把 `supported_nips` 当成事实真相。

这点对 relay 选择很重要。一个 relay 可能会宣称支持 NIP-50 搜索、认证要求或大消息限制，但只有客户端真正连上去并走过这些代码路径，才能知道真实情况。

## 为什么重要

- 客户端可以在连接前检查 relay 是否支持必需功能
- 发现服务可以索引 relay 的能力
- 用户可以在发布前查看 relay 策略

## 近期规范方向

这个规范随着时间推移已经被持续瘦身。像 `software`、`version`、隐私政策细节和保留期元数据等旧的可选字段，因为多年采用度不高，已经被移除。这样做让当前的 NIP-11 文档更小、更符合现实，但也意味着客户端不应再期待 relay 会提供丰富的策略元数据。

[PR #2318](https://github.com/nostr-protocol/nips/pull/2318) 提议向 relay 信息文档增加一个可选的 `access_control` 对象，列出 relay 的 gating 模式（open、invite、payment、allowlist），以及客户端可用于申请访问的 endpoint。这个字段只具有提示性质，目的是让客户端和目录服务在公开发现列表中筛除受限 relay，并提前告诉用户为什么某个 relay 拒绝写入。

## 实现

- [nostream PR #557](https://github.com/Cameri/nostream/pull/557) 让 nostream 达到完整的 NIP-11 relay 信息对齐。

---

**主要来源：**
- [NIP-11 规范](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - relay identity 字段更新
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - 清理低使用率字段
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - 删除已弃用字段
- [PR #2318](https://github.com/nostr-protocol/nips/pull/2318) - 用于受限 relay 发现的 `access_control` 字段
- [nostream PR #557](https://github.com/Cameri/nostream/pull/557) - 完整 NIP-11 relay info 对齐

**提及于：**
- [Newsletter #1：NIP 更新](/zh/newsletters/2025-12-17-newsletter/)
- [Newsletter #13：NIP 更新](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19：NIP 更新（`access_control` 提案）](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-66：Relay Discovery and Liveness Monitoring](/zh/topics/nip-66/)
