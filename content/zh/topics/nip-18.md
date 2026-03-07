---
title: "NIP-18：转发"
date: 2025-12-17
translationOf: /en/topics/nip-18.md
translationDate: 2026-03-07
draft: false
categories:
  - Social
  - Protocol
---

NIP-18 定义了如何转发事件，类似于其他平台上的转推功能。

## 工作原理

转发是 kind 6 事件（用于 kind 1 笔记）或 kind 16（通用转发），包含：
- 引用被转发事件的 `e` 标签
- 引用原作者的 `p` 标签
- 可选地在 `content` 字段中包含完整的原始事件

Kind 6 专用于文本笔记。Kind 16 的存在使客户端能够转发其他事件类型，而无需将所有内容都视为 kind 1 笔记。

## 互操作说明

改进了对使用 `a` 标签转发可替换事件的支持。这允许对可寻址事件（kinds 30000-39999）的转发通过其地址而非特定事件 ID 来引用。

这个区别很重要，因为可寻址事件可以随时间更新。通过 `a` 坐标转发让客户端指向可寻址事件的当前版本，而通过事件 ID 转发则冻结了某个特定的历史实例。

## 重要意义

转发不仅仅是一个 UI 分享按钮。它们是内容在社交图谱中传播的方式的一部分，是客户端计算互动的依据，也是 relay 提示数据在网络中传播的途径。如果客户端错误处理转发标签，线程重建和事件获取可能会以微妙的方式出错。

---

**主要来源：**
- [NIP-18 规范](https://github.com/nostr-protocol/nips/blob/master/18.md)
- [PR #2132](https://github.com/nostr-protocol/nips/pull/2132) - 通用转发的 `a` 标签支持

**提及于：**
- [第1期周刊：NIP 更新](/zh/newsletters/2025-12-17-newsletter/#nip-updates)
- [第8期周刊：新闻动态](/zh/newsletters/2026-02-04-newsletter/#news)

**另请参阅：**
- [NIP-01：基础协议](/zh/topics/nip-01/)
- [NIP-10：文本笔记线程](/zh/topics/nip-10/)
