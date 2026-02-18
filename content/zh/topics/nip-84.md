---
title: "NIP-84：高亮"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-02-18
draft: false
categories:
  - Content
  - Protocol
---

NIP-84 定义了 kind 9802 "高亮" event，让用户标记并分享他们认为有价值的 Nostr 长文内容段落。

## 工作方式

`.content` 字段包含高亮文本。Event 通过 `a` 或 `e` tag 引用 Nostr 原生内容作为来源，或通过 `r` tag 引用外部 URL（客户端应去除追踪参数）。可选的 `p` tag 归因原始作者，可选的 `context` tag 在高亮内容为较长段落的一部分时提供上下文文本。

## 引用高亮

用户可以添加 `comment` tag 创建引用高亮，渲染为引用转发。这防止了在微博客户端中出现重复条目。在评论中，`p` tag 提及需要"mention"属性以区分于作者/编辑归因，`r` tag URL 使用"source"属性标注来源引用。

---

**主要来源：**
- [NIP-84 规范](https://github.com/nostr-protocol/nips/blob/master/84.md)

**提及于：**
- [Newsletter #10：版本发布](/zh/newsletters/2026-02-18-newsletter/#prism从-android-分享任意内容到-nostr)

**另请参见：**
- [NIP-94：文件元数据](/zh/topics/nip-94/)
