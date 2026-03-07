---
title: "NIP-29：基于 relay 的群组"
date: 2025-12-24
translationOf: /en/topics/nip-29.md
translationDate: 2026-03-07
draft: false
categories:
  - Social
  - Groups
---

NIP-29 定义了基于 relay 的群组，其中 relay 管理群组成员资格、权限和消息可见性。

## 工作原理

群组由 relay 主机加群组 ID 作为键，relay 是成员资格和管理的权威方。用户发送到群组的事件携带包含群组 ID 的 `h` 标签。relay 生成的元数据使用由 relay 自身密钥签名的可寻址事件。

核心元数据事件是 kind 39000，而 kinds 39001 到 39003 描述管理员、成员和支持的角色。管理操作通过 9000 系列事件完成，如 `put-user`、`remove-user`、`edit-metadata` 和 `create-invite`。

## 访问模型

- **private**：只有成员可以阅读群组消息
- **closed**：加入请求被忽略，除非 relay 使用邀请码处理
- **hidden**：relay 对非成员隐藏群组元数据，使群组不可发现
- **restricted**：只有成员可以向群组写入消息

这些标签是独立的。群组可以对所有人可读但只有成员可写，或者对非成员完全隐藏。这种分离很重要，因为客户端不应将"private"视为所有访问规则的笼统简写。

## 信任模型

NIP-29 不是一个免信任的群组协议。托管 relay 决定哪些管理事件有效、哪些角色存在、成员列表是否可见，以及是否接受旧的或脱离上下文的消息。客户端可以验证签名和时间线引用，但它仍然依赖 relay 策略来获取群组的实际状态。

这使迁移和分叉成为可能，但不是自动的。相同的群组 ID 可以存在于不同的 relay 上，具有不同的历史或规则，因此在实践中 relay URL 是群组身份的一部分。

## 实现说明

- 客户端应将 relay URL 视为群组主机键。2026年1月的一次澄清在规范中明确了这一点，消除了关于使用 pubkey 替代的歧义
- 群组状态从管理历史中重建，而 39000 系列 relay 事件是该状态的信息快照
- 时间线 `previous` 引用是为了防止跨 relay 分叉的脱离上下文的重新广播，而不仅仅是为了改善 UI 线程

---

**主要来源：**
- [NIP-29 规范](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - 澄清了 `private`、`closed` 和 `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - 澄清了 relay URL 作为 relay 键
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - 添加了 `unallowpubkey` 和 `unbanpubkey`

**提及于：**
- [第2期周刊：NIP 更新](/zh/newsletters/2025-12-24-newsletter/#nip-updates)
- [第3期周刊：12月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [第6期周刊：NIP 更新](/zh/newsletters/2026-01-21-newsletter/#nip-updates)
- [第11期周刊：NIP 更新](/zh/newsletters/2026-02-25-newsletter/#nip-updates)
- [第12期周刊：NIP 更新](/zh/newsletters/2026-03-04-newsletter/#nip-updates)

**另请参阅：**
- [NIP-11：relay 信息文档](/zh/topics/nip-11/)
