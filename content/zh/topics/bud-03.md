---
title: "BUD-03：用户服务器列表"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-03 定义了用户如何发布其首选的 Blossom 服务器，使客户端能够发现在哪里上传和检索用户的媒体文件。

## 工作原理

用户发布一个列出其 Blossom 服务器的 kind 10063 事件。然后客户端可以：
- 将媒体上传到用户的首选服务器
- 在给定公钥时发现在哪里找到用户的 blob

这作为直接在内容中嵌入服务器 URL 的替代方案，实现了基于作者的发现。

---

**主要来源：**
- [BUD-03 规范](https://github.com/hzrd149/blossom/blob/master/buds/03.md)

**另请参阅：**
- [Blossom 协议](/zh/topics/blossom/)
- [NIP-51：列表](/zh/topics/nip-51/)

