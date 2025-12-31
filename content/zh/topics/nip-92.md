---
title: "NIP-92: Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2025-12-31
draft: false
categories:
  - 媒体
  - 协议
---

NIP-92 允许用户通过在事件中包含 URL 以及描述这些资源的内联元数据标签，将媒体文件附加到 Nostr 事件中。

## 工作原理

1. 用户将媒体 URL 直接放置在事件内容中（例如，在 kind 1 文本笔记中）
2. 相应的 `imeta`（内联元数据）标签提供每个 URL 的详细信息
3. 客户端可以根据元数据将 imeta URL 替换为富媒体预览
4. 元数据通常在撰写过程中上传文件时自动生成

## imeta 标签

每个 `imeta` 标签必须有一个 `url` 和至少一个其他字段。支持的字段包括：

- `url` - 媒体 URL（必需）
- `m` - 文件的 MIME 类型
- `dim` - 图像尺寸（宽度 x 高度）
- `blurhash` - 用于预览生成的 blurhash
- `alt` - 用于无障碍访问的替代文本
- `x` - SHA-256 哈希（来自 NIP-94）
- `fallback` - 主 URL 失败时的备用 URL

## 示例

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**主要来源：**
- [NIP-92 规范](https://github.com/nostr-protocol/nips/blob/master/92.md)

**相关提及：**
- [新闻通讯 #3：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**另请参阅：**
- [NIP-94：文件元数据](/zh/topics/nip-94/)
