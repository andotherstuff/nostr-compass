---
title: "NIP-57：Zaps"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 定义了 zaps，一种向 Nostr 用户和内容发送闪电支付并提供支付发生的加密证明的方式。

## 工作原理

1. 客户端从接收者的 kind 0 个人资料获取其闪电地址
2. 客户端从接收者的 LNURL 服务器请求发票，包含一个 zap 请求事件
3. 用户支付发票
4. LNURL 服务器向 Nostr 中继发布 kind 9735 zap 收据
5. 客户端在接收者的内容上显示 zap

## Zap 请求（kind 9734）

zap 请求是一个签名事件，证明谁发送了 zap 以及 zap 了什么内容。它包括：
- 带有接收者公钥的 `p` 标签
- 带有被 zap 事件的 `e` 标签（可选）
- 以毫聪为单位的 `amount` 标签
- 列出发布收据位置的 `relays` 标签

## Zap 收据（kind 9735）

由 LNURL 服务器在支付确认后发布。包含：
- `description` 标签中的原始 zap 请求
- 带有已支付发票的 `bolt11` 标签
- 证明支付的 `preimage` 标签

---

**主要来源：**
- [NIP-57 规范](https://github.com/nostr-protocol/nips/blob/master/57.md)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)
- [第2期周刊：新闻动态](/zh/newsletters/2025-12-24-newsletter/#news)

**另请参阅：**
- [NIP-47：Nostr Wallet Connect](/zh/topics/nip-47/)

