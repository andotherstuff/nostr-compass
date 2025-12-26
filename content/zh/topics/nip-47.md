---
title: "NIP-47：Nostr Wallet Connect"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 定义了一个协议，用于将 Nostr 应用程序连接到闪电钱包，无需向每个应用暴露钱包凭证即可实现支付。

## 工作原理

钱包（如 Zeus）运行一个 NWC 服务，在特定 Nostr 中继上监听支付请求。应用使用包含钱包公钥和中继信息的连接字符串进行连接。支付请求和响应在应用和钱包之间加密。

## 使用场景

- **Zapping** - 向帖子、个人资料或内容创作者发送聪
- **支付** - 从任何 Nostr 应用支付闪电发票
- **订阅** - 为付费内容进行定期支付

## 关键特性

- **预算控制** - 为每个连接设置消费限额
- **自定义中继** - 使用您自己的中继进行钱包通信
- **并行支付** - 同时处理多个 zap 用于批量操作

---

**主要来源：**
- [NIP-47 规范](https://github.com/nostr-protocol/nips/blob/master/47.md)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)
- [第2期周刊：版本发布](/zh/newsletters/2025-12-24-newsletter/#releases)

**另请参阅：**
- [NIP-57：Zaps](/zh/topics/nip-57/)

