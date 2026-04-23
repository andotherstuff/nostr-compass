---
title: "NIP-23：长文内容"
date: 2026-04-08
translationOf: /en/topics/nip-23.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - 长文
---

NIP-23 为 Nostr 上的长文内容定义了 kind `30023`。与 kind `1` 的短笔记不同，长文 event 是参数化可替换 event（以 `d` tag 为键），支持 Markdown 格式，并包含标题、摘要、图片和发布日期等元数据标签。

## 工作原理

长文 event 使用 kind `30023`，并用 `d` tag 作为唯一标识符，因此作者可以通过发布新的、带有相同 `d` tag 的 event 来更新内容。`content` 字段承载 Markdown 文本。标准标签包括 `title`、`summary`、`image`（头图 URL）、`published_at`（原始发布时间戳）和 `t`（hashtag）。由于这是参数化可替换 event，relay 对于每位作者的每个 `d` tag 只存储最新版本。

## 关键标签

- `d` - 唯一文章标识符（slug）
- `title` - 文章标题
- `summary` - 简短描述
- `image` - 头图 URL
- `published_at` - 原始发布的 Unix 时间戳（不同于每次编辑都会更新的 `created_at`）
- `t` - hashtag 或主题标签

## 实现

- [Habla](https://habla.news) - 长文内容阅读与发布平台
- [YakiHonne](https://yakihonne.com) - 长文内容平台
- [Highlighter](https://highlighter.com) - 阅读与批注工具

---

**主要来源：**
- [NIP-23 规范](https://github.com/nostr-protocol/nips/blob/master/23.md)

**另请参阅：**
- [NIP-01（基础协议）](/zh/topics/nip-01/)
