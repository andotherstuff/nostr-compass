---
title: "NIP-26：委托 event 签名"
date: 2026-09-30
translationOf: /en/topics/nip-26.md
translationDate: 2026-10-02
draft: false
categories:
  - NIPs
  - Identity
---

NIP-26 记录了一种方式，让一个 Nostr 密钥授权另一个密钥签署有限范围的 event。其当前规范被标记为 **draft**（草案）和 **unrecommended**（不推荐），因此它记录的是一种早期设计，而不是给新集成的建议。

## 工作原理 {#how-it-works}

账户密钥签署一个委托令牌，其中写明被委托的密钥和条件。这些条件可以限制 event kind 和 `created_at` 时间。被委托方用自己的密钥签署 event，并在 `delegation` tag 中附上该令牌。读取方必须同时验证 event 签名和委托令牌是否符合这些条件。支持该方案的 relay 还可以按委托方进行搜索。

这一模型让应用无需持有账户的主签名密钥即可发布内容。额外的验证和 relay 搜索要求也说明了为什么实现不能把普通的 event 签名当作委托身份的充分证明。[当前规范](https://github.com/nostr-protocol/nips/blob/master/26.md)明确将这种方法标记为不推荐。

---

**主要来源：**
- [NIP-26 规范及当前状态](https://github.com/nostr-protocol/nips/blob/master/26.md)
- [2022 年 9 月的委托签名文本](https://github.com/nostr-protocol/nips/commit/b62aa418d)

**提及于：**
- [第42期周刊：2022 年 9 月](/zh/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)
