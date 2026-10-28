---
title: 'Buzz 草案 NIP-RS：跨设备阅读状态同步'
date: 2026-10-28
translationOf: /en/topics/nip-rs.md
translationDate: 2026-10-28
draft: false
---

**状态：** 这是 Buzz 项目专属的草案提案。NIP-RS 并非已被接受的官方 NIP。这一标签出自 Buzz 项目文档，官方 NIPs 仓库既未分配也未批准它。

## 目的

借助 NIP-RS，同一用户的多台设备可以共享该用户已经读到的位置。每个安装实例都会发布一个 `kind:30078` 可寻址 event。其 `d` tag 为 `read-state:` 后接一个随机槽位 ID，内容则使用 NIP-44 加密给用户自己的密钥。明文将上下文 ID 映射到时间戳边界，每个边界都表示在该时间点及之前的所有内容均已读。该草案不会发布已读回执，也不会透露其他人读过什么。

## 限制

边界只是关于近期活动的尽力而为的提示，并不构成完整的已读消息历史。手动标记未读的覆盖设置（包括墓碑下限）遵循另一套独立的持久化约定。要加载完整的覆盖状态，就得依赖 relay 的排序和容量行为，而客户端无法完全验证这些行为，因此任意一个 relay 未必会返回完整的未读状态。上下文 ID 大多只在同一客户端系列内部才有意义。

一个仍处于开放状态的拉取请求 #8639 提议，将 Buzz 客户端迁移到 `buzz_v1` NIP-11 能力上，其后端是一个私有的、经过认证的 HTTP API，默认处于禁用状态。不具备该能力的 relay 将继续使用 NIP-RS。

## 主要来源

- [Buzz NIP-RS 草案：跨设备阅读状态同步（固定版本）](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-RS.md)
- [Buzz 拉取请求 #8639：通过 relay 能力实现阅读状态（开放中）](https://github.com/block/buzz/pull/8639)

## 另请参阅

- [NIP-44](/zh/topics/nip-44/)
- [NIP-78](/zh/topics/nip-78/)

**提及于：**

- [第 46 期简报：Buzz](/zh/newsletters/2026-10-28-newsletter/#buzz)
