---
title: "NIP-33：参数化可替换事件（可寻址事件）"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - 协议
---

NIP-33 最初定义了参数化可替换事件，这是一类 relay 仅保留每个 `(pubkey, kind, d-tag)` 元组的一个 event 的事件。该概念后来被重命名为"可寻址事件"并纳入 [NIP-01](/zh/topics/nip-01/)。NIP-33 文档现在重定向到 NIP-01，但在代码库和文档中仍是常见的引用。

## 工作原理

可寻址事件使用 `30000-39999` 范围内的 kind。每个 event 携带一个 `d` tag，其值与作者的 pubkey 和 kind 编号一起构成唯一地址。当 relay 收到与现有 `(pubkey, kind, d-tag)` 元组匹配的新 event 时，它会用较新的（按 `created_at`）替换较旧的。这使得可寻址事件适用于可变状态：个人资料、设置、应用配置、分类列表以及只需最新版本的类似结构。

客户端使用格式为 `<kind>:<pubkey>:<d-tag>` 的 `a` tag 引用可寻址事件，可选地后跟 relay 提示。

## 常见用途

- Kind `30023` 长文内容
- Kind `30078` 应用特定数据（NIP-78 使用）
- Kind `31923` 日历事件（NIP-52）
- Kind `31990` 处理器推荐（NIP-89）
- Kind `30009` 徽章定义（NIP-58）
- Kind `31991` 代理运行配置（Notedeck Agentium）

## 与 NIP-01 的关系

NIP-33 作为整合工作的一部分被合并到 NIP-01 中。NIP-01 规范现在定义了三种 event 保留类别：常规事件（原样保留）、可替换事件（每个 `(pubkey, kind)` 保留一个）和可寻址事件（每个 `(pubkey, kind, d-tag)` 保留一个）。NIP-33 仍然是可寻址事件概念的有效简称。

---

**主要来源：**
- [NIP-33（重定向）](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [NIP-01 规范](https://github.com/nostr-protocol/nips/blob/master/01.md) - 可寻址事件部分

**提及于：**
- [周刊 #13：Notedeck](/en/newsletters/2026-03-11-newsletter/#notedeck-adds-nip-11-relay-limits-and-agentium-features)

**另见：**
- [NIP-01：基本协议](/zh/topics/nip-01/)
