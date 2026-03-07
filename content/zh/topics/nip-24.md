---
title: "NIP-24：额外元数据字段"
date: 2025-12-17
translationOf: /en/topics/nip-24.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identity
---

NIP-24 为 kind 0 用户元数据定义了基本 name、about 和 picture 之外的额外可选字段。

## 额外元数据字段

- **display_name**：比 `name` 更大、字符更丰富的替代名称
- **website**：与事件作者相关的网页 URL
- **banner**：用于可选背景显示的宽幅（约 1024x768）图片的 URL
- **bot**：布尔值，表示内容完全或部分由自动化产生
- **birthday**：包含可选 year、month 和 day 字段的对象

规范还将两个旧字段标记为已弃用：`displayName` 应改为 `display_name`，`username` 应改为 `name`。客户端在实际环境中仍然会遇到这些字段，因此即使写入方不应输出它们，宽容的解析器有助于向后兼容。

## 标准标签

NIP-24 还标准化了通用标签：
- `r`：网页 URL 引用
- `i`：外部标识符
- `title`：各种事件类型的名称
- `t`：标签话题（必须为小写）

## 重要意义

NIP-24 主要是关于统一。这些字段和标签已经在各客户端中出现，因此规范赋予它们一致的名称和含义。这减少了细小但恼人的不兼容问题，例如客户端对横幅图片应该放在 `banner` 还是某个应用特定键下的分歧。

对实现者来说的一个实际要点是，kind 0 在大多数客户端中仍然是一条热路径。额外元数据应保持轻量化。如果某个字段需要自己的获取模式或独立的更新周期，它可能应该放在单独的事件 kind 中，而不是膨胀个人资料元数据。

---

**主要来源：**
- [NIP-24 规范](https://github.com/nostr-protocol/nips/blob/master/24.md)

**提及于：**
- [第1期周刊：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)

**另请参阅：**
- [NIP-01：基础协议](/zh/topics/nip-01/)
