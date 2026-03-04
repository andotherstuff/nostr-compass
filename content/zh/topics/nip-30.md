---
title: "NIP-30：自定义表情"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-04
draft: false
categories:
  - NIP
  - 社交
---

NIP-30 定义了客户端如何在 Nostr event 中显示自定义表情。自定义表情通过短代码（`:shortcode:`）在 event 内容中引用，并通过 `emoji` tag 将每个短代码映射到图片 URL 来解析。

## 工作原理

使用自定义表情的 event 在内容中包含短代码引用，同时附带 `emoji` tag：

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

客户端在渲染内容时将 `:gleam:` 和 `:nostrich:` 替换为指定 URL 的内联图片。短代码必须为字母数字（允许下划线分隔），图片 URL 应指向适合内联显示的小型方形图片。

## 表情集

自定义表情可以组织成命名集合，作为 kind 30030 参数化可替换 event 发布。每个集合通过 `d` tag 标识符将相关表情分组：

```json
{
  "kind": 30030,
  "tags": [
    ["d", "nostr-animals"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"],
    ["emoji", "nostrcat", "https://example.com/nostrcat.png"]
  ]
}
```

2026 年 3 月的更新（[PR #2247](https://github.com/nostr-protocol/nips/pull/2247)）在 emoji tag 中添加了可选的表情集地址引用，让客户端在用户点击表情时可以打开其所属的表情集进行浏览或收藏。

## 表情回应

NIP-30 自定义表情也可用于 kind 7 回应 event。当回应的 `content` 设置为短代码，并附带匹配的 `emoji` tag 时，将在被引用的 event 上渲染为自定义表情回应：

```json
{
  "kind": 7,
  "content": ":fire:",
  "tags": [
    ["emoji", "fire", "https://example.com/fire.gif"],
    ["e", "<event-id>"]
  ]
}
```

---

**主要来源：**
- [NIP-30 规范](https://github.com/nostr-protocol/nips/blob/master/30.md)
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - emoji tag 中的表情集地址

**提及于：**
- [第12期周刊：NoorNote v0.5.x](/zh/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [第12期周刊：NIP 更新](/zh/newsletters/2026-03-04-newsletter/#nip-更新)
