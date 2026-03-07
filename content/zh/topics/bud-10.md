---
title: "BUD-10：Blossom URI 方案"
date: 2025-12-17
translationOf: /en/topics/bud-10.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

BUD-10 定义了 `blossom:` URI 方案，这是一种可移植的 blob 引用，可以在文件哈希之外携带服务器提示、作者提示和预期大小。

## URI 格式

```
blossom:<sha256>.<ext>?xs=<server>&as=<pubkey>&sz=<bytes>
```

规范要求使用小写的 64 字符 SHA-256 哈希和文件扩展名。如果扩展名未知，客户端应回退到 `.bin`。

## 解析流程

客户端应分阶段解析 `blossom:` URI：

1. 按出现顺序尝试所有 `xs` 服务器提示
2. 如果存在 `as` 作者公钥，获取每个作者的 [BUD-03](/zh/topics/bud-03/) 服务器列表并尝试这些服务器
3. 必要时回退到知名服务器或本地缓存

这种顺序很有用，因为它让发送者可以附加即时提示以便快速检索，同时仍为接收者提供在这些提示过期时的恢复路径。

## 重要意义

`blossom:` URI 的工作方式更像磁力链接而非普通媒体 URL。它们描述要获取什么 blob 并包含在哪里找到它的线索，而不是假设某个主机将永远可用。

可选的 `sz` 字段在哈希之外增加了一个具体的完整性检查。客户端可以在下载前后验证预期大小，这有助于捕获不完整的传输并改善大型媒体的用户体验。

---

**主要来源：**
- [BUD-10 规范](https://github.com/hzrd149/blossom/blob/master/buds/10.md)
- [Blossom 仓库](https://github.com/hzrd149/blossom)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)

**另请参阅：**
- [Blossom 协议](/zh/topics/blossom/)
- [BUD-03：用户服务器列表](/zh/topics/bud-03/)
