---
title: "NIP-30：自定义表情"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-30 定义了客户端如何在 Nostr 事件中显示自定义表情。自定义表情在事件内容中通过短代码（`:shortcode:`）引用，并通过 `emoji` 标签将每个短代码映射到图片 URL 来解析。

## 工作原理

使用自定义表情的事件在内容中包含短代码引用和对应的 `emoji` 标签：

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

客户端在渲染内容时将 `:gleam:` 和 `:nostrich:` 替换为来自指定 URL 的内联图片。短代码必须是字母数字格式（允许下划线分隔符），图片 URL 应指向适合内联显示的小型正方形图片。

## 表情集

自定义表情可以组织成命名集合，作为 kind 30030 参数化可替换事件发布。每个集合将相关的表情分组在一个 `d` 标签标识符下：

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

2026年3月的更新（[PR #2247](https://github.com/nostr-protocol/nips/pull/2247)）在 emoji 标签中添加了可选的表情集地址引用，允许客户端在用户点击表情时打开其来源集合以进行浏览或收藏。

## 互操作说明

自定义表情是一个展示层功能，不是传输保证。如果客户端不理解 NIP-30 或无法获取图片 URL，它应该仍然显示原始的 `:shortcode:` 文本。这种回退机制正是可读短代码重要的原因。

除非引用了表情集，否则标签是事件局部的。在两个不同的事件中重复使用 `:fire:` 并不意味着它们有共享的全局含义，除非两者都指向相同的图片或集合。客户端应首先从当前事件中解析表情定义。

## 反应

NIP-30 自定义表情同样适用于 kind 7 反应事件。当反应的 `content` 设置为短代码并包含匹配的 `emoji` 标签时，它会在被引用的事件上渲染为自定义表情反应：

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
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - 标签中的表情集地址

**提及于：**
- [第12期周刊：NoorNote v0.5.x](/zh/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [第12期周刊：NIP 更新](/zh/newsletters/2026-03-04-newsletter/#nip-updates)
