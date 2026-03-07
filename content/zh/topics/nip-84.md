---
title: "NIP-84：高亮"
date: 2026-02-18
draft: false
translationOf: /en/topics/nip-84.md
translationDate: 2026-03-07
categories:
  - Content
  - Protocol
---

NIP-84 定义了 kind 9802 "高亮"事件，允许用户标记和分享他们认为有价值的 Nostr 长文内容段落。

## 工作原理

`.content` 字段包含高亮的文本。事件使用 `a` 或 `e` 标签引用 Nostr 原生内容的源材料，或使用 `r` 标签引用外部 URL（客户端应去除跟踪参数）。可选的 `p` 标签标注原作者，可选的 `context` 标签在高亮内容是较大段落的一部分时提供上下文文本。

对于非文本媒体，高亮内容可以为空。这为客户端提供了一种指向音频或视频高亮的方式，同时将源引用保留在标签中。

## 引用高亮

用户可以添加 `comment` 标签来创建引用高亮，渲染效果类似于引用转发。这避免了在微博客户端中产生重复条目。在评论中，`p` 标签提及需要一个 "mention" 属性以区别于作者/编辑标注，`r` 标签 URL 使用 "source" 属性表示来源引用。

## 重要意义

NIP-84 将高亮段落与周围的讨论分离。客户端可以将选中的文本作为主要对象渲染，然后将评论作为可选元数据处理，而不是将两者混合在普通笔记中。

这对阅读和研究工具很有用，因为它保留了精确的摘录。两个读者可以对同一篇文章发表评论，同时产生其他客户端能够理解的可移植高亮事件。

## 互操作说明

归属标签比看起来更重要。带有 `author` 或 `editor` 角色的 `p` 标签告诉客户端谁创建了源材料，而引用评论中的 `mention` 角色含义则不同。如果客户端将这些情况合并处理，它们可能会错误标注高亮来源或错误地通知相关人员。

---

**主要来源：**
- [NIP-84 规范](https://github.com/nostr-protocol/nips/blob/master/84.md)

**提及于：**
- [Newsletter #10：版本发布](/zh/newsletters/2026-02-18-newsletter/#prism-share-anything-to-nostr-from-android)

**另请参阅：**
- [NIP-94：文件元数据](/zh/topics/nip-94/)
