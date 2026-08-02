---
title: "NIP-68：图片优先信息流"
date: 2026-07-29
translationOf: /en/topics/nip-68.md
translationDate: 2026-08-02
draft: false
categories:
  - Media
  - Protocol
---

NIP-68 定义可寻址的图片 event。它为客户端提供一种可移植方式，用于发布图片元数据、说明文字、标签和图片文件引用，同时让 event 本身与 blob 存储保持分离。

## 工作原理

图片使用 kind `20`，并带有 `title` tag，描述则放在 `content` 中。`imeta` tag 通过 `url`、表示 MIME type 的 `m`、表示尺寸的 `dim`、`alt` 文本和可选 SHA-256 哈希等字段描述每张图片。多个 `imeta` tag 让一个 event 可以表示一组图片。

event 可以包含指向图片中人物或署名者的 `p` tag、表示主题的 `t` tag，以及普通 Nostr 引用。它还可以包含媒体类型、哈希、位置和内容警告 tag，让客户端可以一致地过滤并渲染图片帖子。

NIP-68 不指定存储后端。客户端可以引用普通 HTTPS URL，也可以引用 Blossom 等内容寻址系统，只要发布的 `imeta` 元数据足以让另一个客户端显示并验证图片。

## 实现

[NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0) 在面向图片的客户端功能之外加入了 NIP-68 图片 tag。

---

**主要来源：**
- [NIP-68 规范](https://github.com/nostr-protocol/nips/blob/master/68.md)
- [NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0)

**提及于：**
- [Newsletter #33：打标签的发布](/zh/newsletters/2026-07-29-newsletter/#tagged-releases)

**另请参阅：**
- [Blossom 协议](/zh/topics/blossom/)
- [NIP-94：文件元数据](/zh/topics/nip-94/)
