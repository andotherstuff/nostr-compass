---
title: "Cashu：Ecash 协议"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-01-28
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu 是一个基于 Bitcoin 和 Lightning Network 构建的 Chaumian ecash 协议，通过加密代币实现私密、即时和低费用的支付。

## 工作原理

Cashu 使用盲签名创建不可追踪的 ecash 代币：

1. **铸造**：用户向铸造厂存入 Bitcoin/Lightning 并接收盲化代币
2. **消费**：代币可以在用户之间点对点转移，无需铸造厂参与
3. **赎回**：接收者在铸造厂赎回代币以换取 Bitcoin/Lightning

由于盲化过程，铸造厂无法将存款与赎回关联，提供了强大的隐私保证。

## 关键特性

- **隐私**：铸造厂无法追踪用户之间的代币转移
- **即时**：转账离线进行，无需区块链确认
- **低费用**：代币转移没有链上费用
- **托管**：用户信任铸造厂会履行赎回

## Nostr 集成

Cashu 以多种方式与 Nostr 集成：

- **Nutzaps**：作为 zaps 发送的 ecash 代币，具有增强的隐私性
- **托管**：用于拼车等服务的基于 HTLC 的支付托管
- **钱包**：Nostr 原生钱包在中继上存储加密的 Cashu 代币
- **[NIP-87](/zh/topics/nip-87/)**：通过 Nostr 进行铸造厂发现和评价

## 信任模型

与自我托管的 Bitcoin 不同，Cashu 需要信任铸造厂运营者。用户应该：
- 使用信誉良好、评价良好的铸造厂
- 保持与信任级别相适应的小额余额
- 了解铸造厂可能跑路或下线，从而带走资金

## 相关

- [NIP-87](/zh/topics/nip-87/) - Cashu 铸造厂推荐
- [NIP-60](/zh/topics/nip-60/) - Nostr 钱包
