---
title: "NIP-29：基于中继的群组"
date: 2025-12-24
draft: false
categories:
  - Social
  - Groups
---

NIP-29 定义了基于中继的群组，其中中继管理群组成员资格、权限和消息可见性。

## 群组访问标签

- **private**：只有成员可以阅读群组消息
- **closed**：加入请求被忽略（仅限邀请）
- **hidden**：中继对非成员隐藏群组元数据，使群组无法被发现
- **restricted**：只有成员可以向群组写入消息

这些标签可以组合。群组可以是 `restricted`（写入受限）但不是 `hidden`（仍可发现）。省略标签启用相反的行为：没有 `private` 意味着任何人都可以阅读，没有 `closed` 意味着加入请求会被处理。

## 工作原理

中继是群组操作的权威：
- 维护成员列表和角色
- 强制执行写入权限
- 控制非成员可以看到什么

客户端向中继发送群组消息，中继在接受前验证成员资格。

## 隐私考虑

- `hidden` 群组提供最强的可发现性保护：它们不会出现在搜索或中继列表中
- `private` 群组对非成员隐藏消息内容
- `closed` 群组简单地忽略加入请求；与 `private` 或 `hidden` 结合以获得更强的访问控制
- `restricted` 控制谁可以写入，独立于读取访问

---

**主要来源：**
- [NIP-29 规范](https://github.com/nostr-protocol/nips/blob/master/29.md)

**提及于：**
- [第2期周刊：NIP 更新](/zh/newsletters/2025-12-24-newsletter/#nip-updates)

