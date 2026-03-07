---
title: "Blossom 协议"
date: 2025-12-17
translationOf: /en/topics/blossom.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

Blossom 是一个为 Nostr 设计的媒体托管协议，将 blob 存储在普通 HTTP 服务器上，并通过 SHA-256 哈希而非服务器分配的 ID 来寻址。

## 工作原理

Blossom 服务器提供一组简洁的 HTTP 接口，用于 blob 的检索、上传和管理。标准标识符是文件哈希，因此同一个 blob 在任何兼容服务器上都保持相同的地址。

- `GET /<sha256>` 通过哈希检索 blob
- `PUT /upload` 上传 blob
- kind `24242` Nostr 事件用于授权上传和管理操作
- kind `10063` 事件（定义在 [BUD-03](/zh/topics/bud-03/) 中）允许用户发布其首选服务器

由于哈希即是标识符，客户端可以在下载后本地验证完整性，也可以在不更改底层引用的情况下尝试其他服务器。

## 重要意义

Blossom 将 blob 存储与社交事件分离。帖子或个人资料可以指向媒体，而无需将该媒体绑定到某个特定主机的 URL 设计。

这也改变了故障处理方式。如果某个服务器消失，客户端可以从镜像、缓存或通过作者的 [BUD-03](/zh/topics/bud-03/) 列表发现的服务器获取相同的哈希。相比原始主机 URL 是唯一定位器的媒体系统，这是一个实际的改进。

## 互操作说明

Blossom 是模块化的。核心的检索和上传行为位于 BUD-01 和 BUD-02 中，而镜像、媒体优化、授权和 URI 共享则被拆分到独立的 BUD 中。

这种拆分让客户端可以只实现基本互操作所需的最小功能，然后在支持成熟时添加可选功能，例如 [BUD-10](/zh/topics/bud-10/) URI 提示或本地缓存。

---

**主要来源：**
- [Blossom 仓库](https://github.com/hzrd149/blossom)
- [BUD-01：服务器要求和 blob 检索](https://github.com/hzrd149/blossom/blob/master/buds/01.md)
- [BUD-02：Blob 上传和管理](https://github.com/hzrd149/blossom/blob/master/buds/02.md)
- [本地 Blossom 缓存指南](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)
- [第2期周刊：重要代码变更](/zh/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)
- [第10期周刊：Blossom 本地缓存层出现](/zh/newsletters/2026-02-18-newsletter/#blossom-local-cache-layer-emerges)

**另请参阅：**
- [BUD-03：用户服务器列表](/zh/topics/bud-03/)
- [BUD-10：Blossom URI 方案](/zh/topics/bud-10/)
