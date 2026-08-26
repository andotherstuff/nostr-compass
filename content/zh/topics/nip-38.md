---
title: "NIP-38：用户状态"
date: 2026-08-26
translationOf: /en/topics/nip-38.md
translationDate: 2026-08-26
draft: false
description: "定义短时效的用户状态事件，包括通用状态与音乐状态两个类别。"
---

NIP-38 为简短的用户状态定义了 kind 30315 可寻址事件。`d` tag 标明状态类别，例如 `general` 或 `music`，可选的 `r` 与 `p` tag 可以链接到某个 URL 或指明一位艺人。客户端可以使用事件的 `expiration` tag 来停止显示过期状态。

## 工作方式

用户发布一个 kind 30315 事件，状态文本放在 `content` 中。该事件按 pubkey、kind 与 `d` tag 可寻址，因此同一类别下更新的事件会取代较早的那个。content 字段为空则清除该状态。

---

**主要来源：**

- [NIP-38 规范](https://github.com/nostr-protocol/nips/blob/master/38.md) - 用户状态

**提及于：**

- [新闻通讯 #37：NoorNote v1.3.6：个人资料状态与分类信息](/zh/newsletters/2026-08-26-newsletter/#noornote-v136个人资料状态与分类信息)
