---
title: "BUD-03：用户服务器列表"
date: 2025-12-17
translationOf: /en/topics/bud-03.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

BUD-03 定义了用户如何发布其首选的 Blossom 服务器，以便客户端知道在哪里上传 blob 以及当媒体 URL 失效时在哪里查找。

## 工作原理

用户发布一个包含一个或多个 `server` 标签的可替换 kind `10063` 事件。每个标签包含一个完整的 Blossom 服务器 URL。

客户端随后可以：
- 将 blob 上传到用户的首选服务器
- 通过作者的公钥发现可能的 blob 位置
- 当旧的 URL 失效时，从列出的服务器重试检索

## 实用细节

`server` 标签的顺序很重要。规范规定用户应将其最信任或最可靠的服务器排在前面，客户端上传时至少要尝试第一个服务器。这意味着 BUD-03 不仅仅是一个目录，它同时也是一个弱偏好信号。

检索指引同样具有实用性：当客户端从 URL 中提取 blob 哈希时，应使用路径中最后一个 64 字符的十六进制字符串。这有助于客户端从标准 Blossom URL 和仍嵌入哈希的非标准 CDN 风格 URL 中恢复 blob。

---

**主要来源：**
- [BUD-03 规范](https://github.com/hzrd149/blossom/blob/master/buds/03.md)
- [Blossom 仓库](https://github.com/hzrd149/blossom)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)

**另请参阅：**
- [Blossom 协议](/zh/topics/blossom/)
- [NIP-51：列表](/zh/topics/nip-51/)
