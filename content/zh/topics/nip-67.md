---
title: "NIP-67：EOSE 完整性提示"
date: 2026-04-22
translationOf: /en/topics/nip-67.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-67 是一个开放提案，它为 [NIP-01](/zh/topics/nip-01/) 里现有的 `EOSE` 消息增加了一个可选的第三元素，用来指示 relay 是否已经交付了所有与过滤器匹配的已存储 events。它的目标是替代客户端今天用来判断订阅到底是“确实取完了”还是“被 relay 上限截断了”的不可靠启发式方法。

## 问题

`EOSE` 只表示已存储事件与实时事件的边界，却不携带任何关于完整性的信息。在实践中，relay 通常会对单个订阅设置上限，常见范围是 300 到 1000 条，这与客户端设置的 `limit` 无关。客户端向一个上限为 300 的 relay 请求最近 500 条笔记时，只会收到 300 条 events 和一个 `EOSE`，但无法区分“这就是全部结果”还是“relay 中途截断了结果”。当前常见的绕法，是把返回的 event 数量与客户端的 `limit` 做比较并保守分页，但这既会在 relay 上限低于请求值时漏掉 events，也会在上限恰好等于真实匹配数的倍数时白白浪费一次往返。

边界时间戳相同的情况会让问题更糟。使用 `until = oldest_created_at` 分页时，如果一批结果中最旧的几条 event 共享同一个时间戳，那么取决于 relay 如何比较时间戳，客户端可能会漏取，或者重复抓取这些 events。

## 变更内容

NIP-67 为 `EOSE` 增加一个可选的第三元素：

```
["EOSE", "<subscription_id>", "finish"]   // 已交付所有匹配的已存储事件
["EOSE", "<subscription_id>"]             // 不对完整性做任何声明（旧格式）
```

规范只定义了正向信号。一个宣称支持 NIP-67 但省略该提示的 relay，等于在说还有更多数据。一个没有宣称支持的 relay，则继续回落到现有启发式，因此这项改动与当前所有客户端和 relay 都向后兼容。

当客户端知道某个 relay 支持 NIP-67 时，只要看到 `"finish"` 就可以停止分页，避免在上限恰好等于结果集大小时进行那次必然多余的额外往返，也能向用户更准确地展示结果是否完整。

## 状态

该提案目前仍以 [PR #2317](https://github.com/nostr-protocol/nips/pull/2317) 的形式开放在 NIPs 仓库中。

---

**主要来源：**
- [PR #2317: NIP-67 EOSE Completeness Hint](https://github.com/nostr-protocol/nips/pull/2317)
- [NIP-01 规范](https://github.com/nostr-protocol/nips/blob/master/01.md)

**提及于：**
- [Newsletter #19：NIP 更新](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-01：基础协议流程](/zh/topics/nip-01/)
- [NIP-11：Relay 信息文档](/zh/topics/nip-11/)
