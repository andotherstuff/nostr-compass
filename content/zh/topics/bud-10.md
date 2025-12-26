---
title: "BUD-10：Blossom URI 方案"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-10 为 Blossom 定义了一个自定义 URI 方案，嵌入了从任何可用服务器检索文件所需的所有信息。

## URI 格式

```
blossom:<sha256>.<ext>?size=<bytes>&server=<url>&server=<url>&pubkey=<hex>
```

组成部分：
- **sha256**：文件哈希（必需）
- **ext**：文件扩展名
- **size**：文件大小（字节）
- **server**：一个或多个服务器提示
- **pubkey**：用于 BUD-03 服务器发现的作者公钥

## 优势

- 比静态 HTTP URL 更具弹性
- 跨多个服务器自动回退
- 通过公钥提示进行基于作者的发现
- 自验证（哈希确保完整性）

---

**主要来源：**
- [BUD-10 PR](https://github.com/hzrd149/blossom/pull/84)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)

**另请参阅：**
- [Blossom 协议](/zh/topics/blossom/)
- [BUD-03：用户服务器列表](/zh/topics/bud-03/)

