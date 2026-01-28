---
title: "NIP-22：评论"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Social
---

NIP-22 定义了对任何可寻址 Nostr 内容进行评论的标准，支持在文章、视频、日历事件和其他可寻址事件上进行线程讨论。

## 工作原理

评论使用 kind 1111 事件，带有引用被评论内容的标签：

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["E", "root-event-id", "wss://relay.example"],
    ["K", "30023"]
  ],
  "content": "Great article!"
}
```

## 标签结构

- **`A` 标签**：引用被评论的可寻址事件（kind:pubkey:d-tag 格式）
- **`E` 标签**：引用用于线程的根事件 ID
- **`K` 标签**：指示根事件的类型
- **`e` 标签**：引用嵌套回复的父评论

## 与 Kind 1 的区别

虽然 kind 1 笔记可以回复其他笔记，但 NIP-22 评论专门设计用于：

- 可寻址内容（文章、视频、日历事件）
- 维护清晰的父子关系
- 支持长文内容的审核和线程

## 用例

- 文章讨论
- 视频评论
- [NIP-52](/zh/topics/nip-52/) 日历事件讨论
- Wiki 页面讨论页
- 任何可寻址事件类型

## 相关

- [NIP-01](/zh/topics/nip-01/) - 基础协议（kind 1 笔记）
- [NIP-52](/zh/topics/nip-52/) - 日历事件
