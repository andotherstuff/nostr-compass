---
title: "NIP-27：文本笔记引用"
date: 2026-02-04
description: "NIP-27 定义了如何使用 nostr: URI 方案在笔记内容中引用个人资料、笔记和其他实体。"
translationOf: /en/topics/nip-27.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-27 规定了如何在文本笔记的内容中嵌入对 Nostr 实体的引用。引用使用 `nostr:` URI 方案，后跟 bech32 编码的标识符（npub、note、nevent、nprofile、naddr）。

## 工作原理

在撰写提及另一个用户或引用另一个事件的笔记时，引用直接嵌入到内容中：

```
Check out this post by nostr:npub1... about nostr:note1...
```

客户端解析这些引用并适当渲染它们，通常作为可点击的链接或内联个人资料卡片。被引用的实体也可能被镜像到事件标签中用于索引或通知，但规范将此列为可选。

NIP 还涵盖了标签话题的解析。以 `#` 为前缀的标签被提取并添加到事件的 `t` 标签中以便搜索。

## 引用类型

- `nostr:npub1...` - 引用用户个人资料
- `nostr:note1...` - 引用特定笔记事件
- `nostr:nevent1...` - 引用带 relay 提示的事件
- `nostr:nprofile1...` - 引用带 relay 提示的个人资料
- `nostr:naddr1...` - 引用可寻址事件

## 重要意义

NIP-27 将人们阅读的内容与客户端存储的内容分开。用户可以在富文本编辑器中输入 `@name`，但发布的事件在 `content` 中仍然可以包含稳定的 `nostr:nprofile...` 引用。这使引用可以跨客户端移植，而不依赖于某个应用的提及语法。

另一个实际好处是健壮性。嵌入在文本中的原始 `nostr:nevent...` 或 `nostr:naddr...` 仍然携带足够的信息，让其他客户端能够重建目标，即使它从未见过原始的本地渲染。

## 互操作说明

- 在内容本身中使用 [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) 格式：`nostr:<bech32-id>`
- 仅当你的客户端需要提及通知或更强的事件索引时，才添加 `p` 或 `q` 标签
- 不要假设每个内联引用都应该成为回复关系。规范将该选择留给客户端

---

**主要来源：**

- [NIP-27 规范](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19（Bech32 编码实体）](/zh/topics/nip-19/) - 定义了引用中使用的编码格式

**提及于：**

- [第8期周刊（2026-02-04）](/zh/newsletters/2026-02-04-newsletter/) - nostr-tools 修复了换行符后标签话题解析的问题

**另请参阅：**
- [NIP-18：转发](/zh/topics/nip-18/)
- [NIP-19：Bech32 编码实体](/zh/topics/nip-19/)
