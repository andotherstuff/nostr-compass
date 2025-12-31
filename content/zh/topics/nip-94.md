---
title: "NIP-94: File Metadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2025-12-31
draft: false
categories:
  - 媒体
  - 协议
---

NIP-94定义了一个文件元数据事件（kind 1063），用于组织和分类Nostr上共享的文件，使relay能够有效地过滤和组织内容。

## 工作原理

1. 用户将文件上传到托管服务
2. 发布包含文件元数据的kind 1063事件
3. 事件内容包含人类可读的描述
4. 结构化的tag提供机器可读的元数据
5. 专业客户端可以系统地组织和显示文件

## 必需和可选标签

**核心tag：**
- `url` - 文件下载链接
- `m` - MIME type（需要小写格式）
- `x` - 文件的SHA-256哈希

**可选tag：**
- `ox` - 服务器转换前原始文件的SHA-256哈希
- `size` - 文件大小（字节）
- `dim` - 图片/视频尺寸（宽 x 高）
- `magnet` - 用于torrent分发的magnet URI
- `i` - torrent infohash
- `blurhash` - 预览用占位图像
- `thumb` - 缩略图URL
- `image` - 预览图URL
- `summary` - 文本摘录
- `alt` - 无障碍描述
- `fallback` - 备用下载源

## 使用场景

NIP-94专为文件共享应用程序设计，而非社交或长文内容客户端。建议的应用包括：

- Torrent索引relay
- 作品集分享平台（类似Pinterest）
- 软件配置和更新分发
- 媒体库和档案

---

**主要来源：**
- [NIP-94规范](https://github.com/nostr-protocol/nips/blob/master/94.md)

**提及于：**
- [Newsletter #3: 十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**另请参阅：**
- [NIP-92: 媒体附件](/zh/topics/nip-92/)
- [Blossom](/zh/topics/blossom/)
