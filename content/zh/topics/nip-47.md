---
title: "NIP-47：Nostr Wallet Connect"
date: 2025-12-17
translationOf: /en/topics/nip-47.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 定义了 Nostr Wallet Connect，这是一套让 Nostr app 与远程 Lightning wallet 服务通信的协议，同时不必把 wallet 的主凭证暴露给每个客户端。

## 工作原理

wallet 服务会发布一个可替换的 kind `13194` info event，用来描述它支持的方法和加密模式。客户端通过 `nostr+walletconnect://` URI 建立连接，这个 URI 包含 wallet 服务 pubkey、一个或多个 relays，以及该连接专用的 secret。请求以 kind `23194` events 发送，响应则以 kind `23195` events 返回。

## 命令与通知

常见方法包括 `pay_invoice`、`pay_keysend`、`make_invoice`、`lookup_invoice`、`list_transactions`、`get_balance` 和 `get_info`。wallet 服务还可以推送 `payment_received`、`payment_sent` 和 `hold_invoice_accepted` 等通知。

规范最初随着时间加入过多个可选方法，但最近的清理移除了 `multi_` 支付方法。在实践中，当客户端遵循 wallet 的 info event 中实际广告出来的命令，而不是假设它支持一整套广泛方法时，互操作性会更好。

## 使用场景

- **Zapping** - 向帖子、profile 或内容创作者发送 sats
- **Payments** - 从任意 Nostr app 支付 Lightning invoice
- **Wallet UX 分离** - 在多个 Nostr 客户端之间复用同一个 wallet 服务

## 安全与互操作说明

连接 URI 内含一个专用 secret，客户端会用它来做签名和加密。这让每个 app 都拥有属于自己的 wallet 身份，有利于撤销控制和隐私保护。wallet 可以限制消费额度、禁用特定方法，或只撤销某一个连接，而不影响其他连接。

NIP-44 现在是首选加密模式。规范仍然保留了面向旧实现的 NIP-04 fallback，因此客户端需要检查 wallet 广告的 `encryption` tag，而不能假设所有 wallet 都已迁移。

---

**主要来源：**
- [NIP-47 Specification](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: Hold Invoice Support](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: Simplification](https://github.com/nostr-protocol/nips/pull/2210)

**提及于：**
- [Newsletter #1：News](/zh/newsletters/2025-12-17-newsletter/)
- [Newsletter #2：Releases](/zh/newsletters/2025-12-24-newsletter/)
- [Newsletter #3：December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #8：NIP Deep Dive](/zh/newsletters/2026-02-04-newsletter/)
- [Newsletter #10：NIP Updates](/zh/newsletters/2026-02-18-newsletter/)
- [Newsletter #13：Shopstr and Milk Market Open MCP Commerce Surfaces](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19：ShockWallet Nostr-native wallet sync](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-57：Zaps](/zh/topics/nip-57/)
