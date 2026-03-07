---
title: "NIP-94：文件元数据"
date: 2025-12-31
draft: false
translationOf: /en/topics/nip-94.md
translationDate: 2026-03-07
categories:
  - Media
  - Protocol
---

NIP-94 定义了文件元数据事件（kind 1063），用于在 Nostr 上组织和分类共享文件，使中继能够有效过滤和组织内容。

## 工作原理

NIP-94 使用 kind `1063` 作为文件的独立元数据事件。事件 `content` 包含人类可读的描述，而标签携带机器可读的字段，如下载 URL、MIME 类型、哈希值、尺寸和预览提示。

这种分离很重要，因为元数据事件可以独立于链接到该文件的任何笔记进行索引、过滤和复用。客户端可以将 kind `1063` 事件视为资产的规范描述，而不必从自由格式的帖子文本中抓取元数据。

## 必填和可选标签

**核心标签：**
- `url` - 文件下载链接
- `m` - MIME 类型（要求小写格式）
- `x` - 文件的 SHA-256 哈希

**可选标签：**
- `ox` - 服务器转换前原始文件的 SHA-256 哈希
- `size` - 文件大小（字节）
- `dim` - 图片/视频的尺寸（宽 x 高）
- `magnet` - 用于种子分发的 Magnet URI
- `i` - 种子 infohash
- `blurhash` - 预览占位图
- `thumb` - 缩略图 URL
- `image` - 预览图 URL
- `summary` - 文本摘要
- `alt` - 无障碍描述
- `fallback` - 替代下载源
- `service` - 存储协议或服务类型，如 NIP-96

`ox` 和 `x` 标签容易被忽略但在实践中很有用。`ox` 标识原始上传文件，而 `x` 可以标识服务器实际提供的转换后版本。当媒体主机压缩或调整上传文件大小时，客户端仍然可以保留原始文件身份，而不必假装转换后的数据与原始文件逐字节相同。

## 使用场景

NIP-94 专为文件共享应用设计，而非社交或长文客户端。建议的应用场景包括：

- 种子索引中继
- 作品集共享平台（类似 Pinterest）
- 软件配置和更新分发
- 媒体库和档案

如果文件元数据只需装饰嵌入在其他事件中的 URL，[NIP-92：媒体附件](/zh/topics/nip-92/) 更为轻量。当文件本身需要作为一等对象被查询时，NIP-94 是更好的选择。

## 互操作说明

NIP-94 可跨存储后端工作。文件可以通过 [NIP-96：HTTP 文件存储](/zh/topics/nip-96/)、Blossom 或其他服务上传，然后仍然使用相同的 kind `1063` 事件结构描述。这就是为什么该元数据格式比任何单一上传协议都更持久。

---

**主要来源：**
- [NIP-94 规范](https://github.com/nostr-protocol/nips/blob/master/94.md)

**提及于：**
- [Newsletter #3：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**另请参阅：**
- [NIP-92：媒体附件](/zh/topics/nip-92/)
- [Blossom](/zh/topics/blossom/)
