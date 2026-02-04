---
title: "NIP-27 (文本笔记引用)"
date: 2026-02-04
description: "NIP-27 定义了如何使用 nostr: URI 方案在笔记内容中引用个人资料、笔记和其他实体。"
---

NIP-27 规定了如何在文本笔记内容中嵌入对 Nostr 实体的引用。引用使用 `nostr:` URI 方案，后跟 bech32 编码的标识符（npub、note、nevent、nprofile、naddr）。

## 工作原理

在撰写提及其他用户或引用其他事件的笔记时，引用直接嵌入内容中：

```
查看 nostr:npub1... 关于 nostr:note1... 的帖子
```

客户端解析这些引用并适当渲染，通常显示为可点击的链接或内联个人资料卡片。被引用的实体也会添加到事件的标签中，用于索引和通知目的。

该 NIP 还涵盖话题标签解析。以 `#` 为前缀的标签会被提取并添加到事件的 `t` 标签中以便搜索。

## 引用类型

- `nostr:npub1...` - 引用用户个人资料
- `nostr:note1...` - 引用特定笔记事件
- `nostr:nevent1...` - 引用带中继提示的事件
- `nostr:nprofile1...` - 引用带中继提示的个人资料
- `nostr:naddr1...` - 引用可寻址事件

## 实现

所有主流 Nostr 客户端都实现了 NIP-27：
- 文本解析器在撰写时提取引用
- 渲染器将引用显示为交互元素
- 通知系统使用关联的标签

## 主要来源

- [NIP-27 规范](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Bech32 编码实体)](/zh/topics/nip-19/) - 定义引用中使用的编码格式

## 相关提及

- [Newsletter #8 (2026-02-04)](/zh/newsletters/2026-02-04-newsletter/) - nostr-tools 修复换行符后的话题标签解析问题
