---
title: "NIP-22：评论"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-22 定义了对任何可寻址 Nostr 内容进行评论的标准，支持在文章、视频、日历事件和其他可寻址事件上进行线程化讨论。

## 工作原理

评论使用 kind 1111 事件，`content` 为纯文本。根范围标签使用大写字母，父级回复标签使用小写字母：

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["K", "30023"],
    ["P", "<root-pubkey>", "wss://relay.example"],
    ["a", "30023:pubkey:article-id", "wss://relay.example"],
    ["e", "<parent-event-id>", "wss://relay.example", "<parent-pubkey>"],
    ["k", "30023"],
    ["p", "<parent-pubkey>", "wss://relay.example"]
  ],
  "content": "Great article!"
}
```

## 标签结构

- **`A` / `E` / `I`** - 讨论的根范围：可寻址事件、事件 ID 或外部标识符
- **`K`** - 根项目的 kind 或根范围类型
- **`P`** - 根事件的作者（如果存在）
- **`a` / `e` / `i`** - 正在回复的直接父级
- **`k`** - 父项目的 kind 或范围类型
- **`p`** - 父项目的作者

对于顶级评论，根和父级通常指向同一个目标。对于评论的回复，根保持不变，而小写的父级标签移动到正在回答的特定评论。

## 互操作说明

NIP-22 评论不是 kind 1 回复的通用替代品。规范明确指出评论不得用于回复 kind 1 笔记。对于笔记到笔记的线程，客户端应继续使用 [NIP-10](/zh/topics/nip-10/)。

另一个有用的区别是范围。NIP-22 可以通过 `I` 和 `i` 标签将讨论锚定到非笔记资源，包括来自 [NIP-73](/zh/topics/nip-73/) 的 URL 和其他外部标识符。这为客户端提供了一种标准方式，将评论线程附加到网页、播客或其他 Nostr 外部对象。

## 使用场景

- 文章讨论
- 视频评论
- [NIP-52](/zh/topics/nip-52/) 日历事件讨论
- Wiki 页面讨论页
- 通过 `I` 标签标识的外部资源的评论

---

**主要来源：**
- [NIP-22 规范](https://github.com/nostr-protocol/nips/blob/master/22.md)

**提及于：**
- [第7期周刊：Notedeck](/zh/newsletters/2026-01-28-newsletter/#notedeck)
- [第10期周刊：AI Agent NIP 到来](/zh/newsletters/2026-02-18-newsletter/#ai-agent-nips-arrive)
- [第12期周刊：diVine](/zh/newsletters/2026-03-04-newsletter/#divine)

**另请参阅：**
- [NIP-10：回复线程](/zh/topics/nip-10/)
- [NIP-52：日历事件](/zh/topics/nip-52/)
- [NIP-73：外部内容 ID](/zh/topics/nip-73/)
