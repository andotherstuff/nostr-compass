---
title: "NIP-92：媒体附件"
date: 2025-12-31
draft: false
translationOf: /en/topics/nip-92.md
translationDate: 2026-03-07
categories:
  - Media
  - Protocol
---

NIP-92 允许用户通过在事件中包含 URL 及描述这些资源的内联元数据标签，将媒体文件附加到 Nostr 事件。

## 工作原理

用户将媒体 URL 直接放在事件内容中，例如 kind `1` 文本笔记中。匹配的 `imeta` 标签随后为该 URL 添加机器可读的详细信息。客户端可以使用这些元数据来渲染预览、预留布局空间，并避免在笔记已显示后才去猜测文件属性。

每个 `imeta` 标签应匹配事件内容中的一个 URL。客户端可以忽略不匹配的标签，这为实现提供了一个拒绝过时或格式错误元数据的简单规则。

## imeta 标签

每个 `imeta` 标签必须有一个 `url` 和至少一个其他字段。支持的字段包括：

- `url` - 媒体 URL（必填）
- `m` - 文件的 MIME 类型
- `dim` - 图片尺寸（宽 x 高）
- `blurhash` - 用于预览生成的 Blurhash
- `alt` - 用于无障碍访问的替代文本描述
- `x` - SHA-256 哈希（来自 NIP-94）
- `fallback` - 主 URL 失败时的替代 URL

由于 `imeta` 可能携带来自 [NIP-94：文件元数据](/zh/topics/nip-94/) 的字段，客户端可以复用它们已经理解的独立文件元数据事件中的相同 MIME 类型、尺寸、哈希和无障碍文本。

## 重要意义

最直接的好处是在下载前获得更好的渲染效果。如果存在 `dim`，客户端可以为图片或视频预留正确的空间，而不是在文件加载后重排时间线。如果存在 `blurhash`，可以先显示低成本预览。如果存在 `alt`，附件对屏幕阅读器和低视力用户仍然可用。

NIP-92 还让客户端将帖子本身作为数据源。URL 保留在 `content` 中，因此旧客户端仍然显示普通链接，而新客户端可以将同一笔记升级为更丰富的媒体卡片。

## 互操作说明

NIP-92 是内联元数据，而非独立的媒体对象格式。如果客户端需要具有自己事件的可复用文件记录，[NIP-94：文件元数据](/zh/topics/nip-94/) 更为合适。

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
- [Primal Android PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) - 尺寸和宽高比处理的客户端实现

**提及于：**
- [Newsletter #3：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #6：新闻](/zh/newsletters/2026-01-21-newsletter/#news)

**另请参阅：**
- [NIP-94：文件元数据](/zh/topics/nip-94/)
