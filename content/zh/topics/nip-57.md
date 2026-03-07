---
title: "NIP-57：Zaps"
date: 2025-12-17
translationOf: /en/topics/nip-57.md
translationDate: 2026-03-07
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 定义了 zap，一种将闪电网络支付附加到 Nostr 身份和内容的方式。它标准化了启用 zap 的发票请求和钱包在支付后发布的收据事件。

## 工作原理

1. 客户端从接收者的个人资料元数据或目标事件上的 `zap` 标签发现其 LNURL 端点。
2. 客户端将签名的 kind `9734` zap 请求发送到接收者的 LNURL 回调，而不是发送到中继。
3. 用户支付发票。
4. 接收者的钱包服务器将 kind `9735` zap 收据发布到 zap 请求中列出的中继。
5. 客户端验证并显示 zap。

## Zap 请求（kind 9734）

Zap 请求是一个签名事件，标识付款人和目标。通常包含：

- 带有接收者公钥的 `p` 标签
- 带有被 zap 事件的 `e` 标签（可选）
- 以毫聪为单位的 `amount` 标签
- 列出收据发布位置的 `relays` 标签

可寻址内容可以使用 `a` 标签替代或补充 `e` 标签。可选的 `k` 标签记录目标 kind。

## Zap 收据（kind 9735）

由接收者的钱包服务器在支付确认后发布。包含：

- `description` 标签中的原始 zap 请求
- 带有已支付发票的 `bolt11` 标签
- 证明支付的 `preimage` 标签

客户端应根据接收者的 LNURL `nostrPubkey`、发票金额和原始 zap 请求来验证收据。未经此验证的收据仅是一个声明。

## 信任与权衡

Zap 的价值在于它使支付在社交图谱中可见，但收据仍然由接收者的钱包基础设施创建。规范本身指出，zap 收据并非通用的支付证明。最好将其理解为钱包签署的声明，表示与 zap 请求关联的发票已被支付。

---

**主要来源：**
- [NIP-57 规范](https://github.com/nostr-protocol/nips/blob/master/57.md)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)
- [第2期周刊：新闻动态](/zh/newsletters/2025-12-24-newsletter/#news)
- [第3期周刊：值得关注的代码变更](/zh/newsletters/2025-12-31-newsletter/#amethyst-android)
- [第9期周刊：NIP 更新](/zh/newsletters/2026-02-11-newsletter/#nip-updates)

**另请参阅：**
- [NIP-47：Nostr Wallet Connect](/zh/topics/nip-47/)
