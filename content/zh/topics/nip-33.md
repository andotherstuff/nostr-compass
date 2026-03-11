---
title: "NIP-33：参数化可替换事件（可寻址事件）"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - 协议
---

NIP-33 最初定义的是参数化可替换事件，这类事件在 relay 中对每个 `(pubkey, kind, d-tag)` 元组只保留一个事件。这个概念后来被重新命名为“可寻址事件”，并并入了 [NIP-01](/zh/topics/nip-01/)。NIP-33 文档现在会重定向到 NIP-01，但在代码库和文档中仍然是一个常见引用。

## 工作原理

可寻址事件使用 `30000-39999` 范围内的 kind。每个事件都携带一个 `d` 标签，其值与作者的 pubkey 和 kind 编号一起构成唯一地址。当 relay 收到一个与现有 `(pubkey, kind, d-tag)` 元组匹配的新事件时，它会用较新的事件替换较旧的事件，判断依据是 `created_at`。这让可寻址事件非常适合表达可变状态，例如 profile、设置、应用配置、分类信息以及其他只关心最新版本的数据结构。

客户端使用 `a` 标签引用可寻址事件，其格式为 `<kind>:<pubkey>:<d-tag>`，后面可以选择附加 relay 提示。

## 常见用途

- Kind `30023` 长文文章
- Kind `30078` 应用专用数据（由 NIP-78 使用）
- Kind `31923` 日历事件（NIP-52）
- Kind `31990` 处理器推荐（NIP-89）
- Kind `30009` 徽章定义（NIP-58）
- Kind `31991` agent 运行配置（Notedeck Agentium）

## 与 NIP-01 的关系

NIP-33 作为一次整合工作的一部分并入了 NIP-01。NIP-01 规范现在定义了三种事件保留类别：普通事件（按原样保留）、可替换事件（每个 `(pubkey, kind)` 保留一个）以及可寻址事件（每个 `(pubkey, kind, d-tag)` 保留一个）。因此，NIP-33 仍然是描述可寻址事件这一概念的有效简称。

---

**主要来源：**
- [NIP-33（重定向）](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [NIP-01 规范](https://github.com/nostr-protocol/nips/blob/master/01.md) - 可寻址事件部分

**提及于：**
- [Newsletter #13：Notedeck](/zh/newsletters/2026-03-11-newsletter/)

**另请参阅：**
- [NIP-01：基础协议](/zh/topics/nip-01/)
