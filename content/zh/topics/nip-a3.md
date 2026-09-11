---
title: "NIP-A3: 支付目标"
date: 2026-09-09
translationOf: /en/topics/nip-a3.md
translationDate: 2026-09-11
draft: false
categories:
  - Protocol
  - Payments
---

NIP-A3 定义了一种可移植的方式，让 Nostr 账户能够发布适用于多个网络和服务的支付地址。一个可替换的 kind `10133` 事件包含一个或多个 `payto` 标签。

## 工作原理

每个标签的格式为 `["payto", "<type>", "<address>"]`。类型使用小写形式，例如 `bitcoin`、`lightning` 或 `monero`。客户端可以验证已知格式，并在存在原生支付 URI 时进行呈现；对于不熟悉的类型，则回退到 RFC 8905 中定义的 `payto:` URI 方案。

该事件声明的是支付目的地，而不是一笔已完成的付款或 Nostr zap。客户端仍需决定支持哪些支付类型、如何验证地址，以及在将目的地交给钱包之前以多清晰的方式向用户展示。

## 实现

- [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041) 在识别到兼容的目标时，提供可选择启用的支付转交功能。
- [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) 将允许的目标类型映射到支付 URI。
- [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) 验证 Monero 目标并查询作者的中继。

---

**主要来源：**
- [NIP-A3 规范](https://github.com/nostr-protocol/nips/blob/master/A3.md)
- [RFC 8905：payto URI 方案](https://www.rfc-editor.org/rfc/rfc8905.html)

**提及于：**
- [第 39 期新闻简报：NIP-A3 支付目标已获三个客户端支持](/zh/newsletters/2026-09-09-newsletter/#nip-a3-payment-targets-reach-three-clients)

**另请参阅：**
- [NIP-47：Nostr Wallet Connect](/zh/topics/nip-47/)
