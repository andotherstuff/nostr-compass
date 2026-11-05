---
title: "NIP-31：处理未知事件类型"
date: 2026-11-04
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-31.md
translationDate: 2026-11-05
---

> **状态警告：** 当前的 [NIP-31 规范](https://github.com/nostr-protocol/nips/blob/master/31.md)将自身标记为 `unrecommended`，理由是“不必要地臃肿”，其状态行写的是草案（draft）、不推荐（unrecommended）和可选（optional）。中继上已经存有使用这一约定的事件，因此本页说明客户端如何读取这些事件。本页并不推荐在新协议中使用 NIP-31。

NIP-31 定义了一个顶层 `alt` 标签。该标签为那些不打算作为普通文本笔记阅读的自定义事件类型提供一段简短的纯文本摘要。

## 工作原理 {#how-it-works}

自定义类型事件的作者会添加一个 `alt` 标签，写入一段人能读懂的标签文字。围绕 kind 1 构建的客户端不必订阅每一种它们无法识别的类型。当某条笔记引用了这样的事件时，用户仍可能看到它，而即使客户端没有实现该类型，这段标签文字也能提供一些上下文。

标签片段，并非完整事件：

```
["alt", "<short plaintext summary>"]
```

可读的标签文字只解决显示问题。它无法投票、处理钱包请求，也无法执行该类型的任何其他原生操作。若需要更丰富的交互，规范指向了 [NIP-89：推荐应用处理程序](/zh/topics/nip-89/)。

## 实现 {#implementations}

在 noStrudel [提交 7c68acf 中的未知事件卡片](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)里，第一个 `alt` 标签会被去除首尾空白后作为主标签显示，并可附带一行 `Using <client>`。若该值缺失或为空，则显示 `Unknown event (kind ...)`，最多三行内容会单独显示。同一组件会通过 NIP-89 处理程序模板解析 `client` 标签。当存在可分享的地址时，它会显示一个 Open 按钮；当能解析出有效的处理程序链接时，则显示 `Open in <client>`。说明文字和应用跳转是两个独立的控件。

Amethyst [提交 553f761 中的 UnknownEventDigest.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) 优先使用它判定为正文的内容，否则回退到 `alt`。其解析器会去除值的首尾空白，并取第一个非空的 `alt`。因此，对于第一个 `alt` 为空的事件，这里得到的标签可能与 noStrudel 中不同。以上两段描述反映的都是这些提交中的源代码，均不能证实已发布版本的实际行为。

## 局限 {#limits}

- `alt` 是一个标签，因此受 [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) 中定义的事件 ID 和签名覆盖。有效的签名表明作者发布了这段标签文字，但不能表明标签文字准确，所以摘要可能具有误导性。
- 标签是公开的。带有加密内容的事件上的 `alt` 会暴露其摘要，并可能泄露内容本应隐藏的信息。
- 上述两项特性都来自 NIP-01 的事件封装。NIP-31 自身的文本并未将它们列为要求。
- 顶层 `alt` 标签不同于 `imeta` 内用于图片描述的 `alt` 字段，渲染器会分别解析二者。

---

**主要来源：**
- [NIP-31 规范](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [noStrudel 提交 7c68acf 中的 embedded-unknown.tsx](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)
- [Amethyst 提交 553f761 中的 UnknownEventDigest.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt)

**提及于：**
- [Nostr Compass #47：NIP 深度解析](/zh/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)

**另请参阅：**
- [NIP-89：推荐应用处理程序](/zh/topics/nip-89/)
- [NIP-73：外部内容 ID](/zh/topics/nip-73/)
- [NIP-01：基本协议流程说明](/zh/topics/nip-01/)
