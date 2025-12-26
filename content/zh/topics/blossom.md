---
title: "Blossom 协议"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

Blossom 是一个为 Nostr 提供去中心化文件存储的媒体托管协议，使用内容寻址 URL。

## 工作原理

文件存储在 Blossom 服务器上，通过其 SHA256 哈希进行寻址。这意味着：
- 相同的文件在所有服务器上始终具有相同的 URL
- 可以从任何拥有文件的服务器检索文件
- 客户端可以通过检查哈希来验证文件完整性

## 特性

- 内容寻址存储
- 多服务器冗余
- 通过 BUD-03 进行作者发现
- 通过 BUD-10 的自定义 URI 方案
- `/list` 端点的基于游标的分页

---

**主要来源：**
- [Blossom 仓库](https://github.com/hzrd149/blossom)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)
- [第2期周刊：重要代码变更](/zh/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)

**另请参阅：**
- [BUD-03：用户服务器列表](/zh/topics/bud-03/)
- [BUD-10：Blossom URI 方案](/zh/topics/bud-10/)

