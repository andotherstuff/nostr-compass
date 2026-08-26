---
title: "NIP-25：回应"
date: 2026-07-29
translationOf: /en/topics/nip-25.md
translationDate: 2026-08-26
draft: false
categories:
  - Protocol
  - Social
---

NIP-25 把回应定义为 kind `7` 事件。它为客户端提供一种共用的事件形态，用来把表情或其他简短回应挂到笔记、文章、分类信息或其他被引用的事件上。

## 工作方式

回应事件把回应文本放在 `content` 中，并通过目标事件的 `e` tag 引用目标。当目标是可寻址事件时，回应还会包含它的 `a` tag。它同时包含指向被引用事件作者的 `p` tag，这让中继与客户端可以投递通知，而不必从事件内容里推断接收方。

默认回应是 `+`，因此客户端可以把空的回应 content 当作肯定的反馈。其他表情也是有效的回应值。规范还允许用 `-` 表示否定回应，这是在最初引入之后由 2022 年 7 月的补充加上的。

客户端在创建回应时应当保留目标引用与作者 tag。回应是普通的已签名事件，因此可以通过常规的中继 subscription 传播，并被任何识别 kind `7` 的客户端渲染。

## 实现

作为笔记日常互动的一部分，NIP-25 已被 Nostr 客户端与库广泛实现。它由 kind 与 tag 构成的简单模型，让客户端可以在没有单独传输协议的情况下显示数量、单条回应与通知。

---

**主要来源：**

- [NIP-25 Specification](https://github.com/nostr-protocol/nips/blob/master/25.md)
- [引入提交](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88)
- [反对票的后续补充](https://github.com/nostr-protocol/nips/commit/89bb08ba8683)

**提及于：**

- [新闻通讯 #33：Nostr 六年七月史](/zh/newsletters/2026-07-29-newsletter/#nostr-六年七月史)
- [新闻通讯 #37：Marmot](/zh/newsletters/2026-08-26-newsletter/#marmot)

**参见：**
- [NIP-01: Basic Protocol](/zh/topics/nip-01/)
- [NIP-10: Text Note Threading](/zh/topics/nip-10/)
