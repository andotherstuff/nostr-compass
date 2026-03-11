---
title: "NIP-47：Nostr Wallet Connect"
date: 2025-12-17
draft: false
translationOf: /en/topics/nip-47.md
translationDate: 2026-03-11
categories:
  - 钱包
  - Lightning
---

NIP-47 定义了 Nostr Wallet Connect，一种允许 Nostr 应用与远程闪电网络钱包服务通信的协议，无需将钱包的主凭证暴露给每个客户端。

## 工作原理

钱包服务发布一个可替换的 kind `13194` 信息事件，描述其支持的方法和加密模式。客户端使用 `nostr+walletconnect://` URI 连接，其中包含钱包服务公钥、一个或多个中继以及该连接的专用密钥。请求以 kind `23194` 事件发送，响应以 kind `23195` 事件返回。

## 命令与通知

常用方法包括 `pay_invoice`、`pay_keysend`、`make_invoice`、`lookup_invoice`、`list_transactions`、`get_balance` 和 `get_info`。钱包服务还可以推送通知，如 `payment_received`、`payment_sent` 和 `hold_invoice_accepted`。

规范最初随时间增加了多个可选方法，但最近的清理移除了 `multi_` 支付方法。实际上，当客户端坚持使用钱包信息事件中声明的命令而非假设广泛的方法集时，互操作性会更好。

## 用例

- **打赏（Zap）** - 向帖子、个人资料或内容创作者发送聪
- **支付** - 从任何 Nostr 应用支付闪电网络发票
- **钱包用户体验分离** - 跨多个 Nostr 客户端使用同一个钱包服务

## 安全与互操作说明

连接 URI 包含一个专用密钥，客户端用它进行签名和加密。这为每个应用赋予独立的钱包身份，有助于撤销和隐私保护。钱包可以限制消费额度、禁用方法或撤销单个连接而不影响其他连接。

NIP-44 现在是首选的加密模式。规范仍然记录了 NIP-04 回退方案以兼容旧实现，因此客户端需要检查钱包声明的 `encryption` 标签，而非假设每个钱包都已迁移。

---

**主要来源：**
- [NIP-47 规范](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913：Hold Invoice 支持](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210：简化](https://github.com/nostr-protocol/nips/pull/2210)

**提及于：**
- [Newsletter #1：新闻](/zh/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2：发布](/zh/newsletters/2025-12-24-newsletter/#releases)
- [Newsletter #3：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #8：NIP 深度解析](/zh/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-47-nostr-wallet-connect)
- [Newsletter #10：NIP 更新](/zh/newsletters/2026-02-18-newsletter/#nip-updates)

**另请参阅：**
- [NIP-57：Zaps](/zh/topics/nip-57/)
