---
title: "NIP-75：Zap Goals"
date: 2026-04-22
translationOf: /en/topics/nip-75.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-75 定义了一种可被用户 zap 的筹款目标 event。目标会声明一个以 millisatoshis 为单位的金额目标，以及一组用于统计该目标 zap receipt 的 relays。任何引用了该目标 event 的 [NIP-57](/zh/topics/nip-57/) zap，都会计入它的进度。

## 工作原理

一个 zap goal 是 `kind:9041` event。`.content` 是人类可读的描述。必填标签包括 `amount`（目标金额，单位为 millisats）和 `relays`（用于统计 zap receipt 的 relay 列表）。可选标签包括 `closed_at`，用于在某个时间戳后停止统计，以及 `image` 和 `summary`。该目标还可以包含 `r` 或 `a` tag，用来链接到外部 URL 或某个可寻址 event，也可以通过借用自 NIP-57 附录 G 的 zap-split tags 携带多个受益人 pubkey。

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1776500000,
  "kind": 9041,
  "tags": [
    ["relays", "wss://alicerelay.example.com", "wss://bobrelay.example.com"],
    ["amount", "210000"],
    ["image", "<image url>"],
    ["summary", "Nostrasia travel expenses"]
  ],
  "content": "Nostrasia travel expenses",
  "sig": "<128-char hex>"
}
```

客户端通过在 zap request 中加入一个指向该目标 event 的 `e` tag，把某次 zap 附加到目标上。目标进度等于该目标所声明 relays 上、所有匹配 zap receipt 金额的总和。设置了 `closed_at` 之后，在该时间戳之后发布的 zap receipts 就不再计入统计。

## 实现

- [Amethyst](https://github.com/vitorpamplona/amethyst) 现在会通过 [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) 在直播头部渲染目标进度条和一键 zap 按钮，把 NIP-75 接入了 NIP-53 的 Live Activities 页面。

---

**主要来源：**
- [NIP-75 规范](https://github.com/nostr-protocol/nips/blob/master/75.md)
- [Amethyst PR #2469: live stream top zappers and goal header](https://github.com/vitorpamplona/amethyst/pull/2469)

**提及于：**
- [Newsletter #19：Amethyst 直播 zap goals](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19：NIP-57 深度解析](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-57：Lightning Zaps](/zh/topics/nip-57/)
- [NIP-53：Live Activities](/zh/topics/nip-53/)
