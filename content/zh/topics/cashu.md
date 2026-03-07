---
title: "Cashu：Ecash 协议"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-03-07
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu 是一个基于 Bitcoin 和 Lightning 构建的 Chaumian ecash 协议。用户持有由铸造厂发行的不记名代币，然后在不向铸造厂暴露完整支付图谱的情况下转移这些代币。

## 工作原理

Cashu 使用盲签名发行 ecash 代币：

1. **铸造**：用户向铸造厂存入 Bitcoin/Lightning 并接收盲化代币
2. **消费**：代币可以在用户之间点对点转移，无需铸造厂参与
3. **赎回**：接收者在铸造厂赎回代币以换取 Bitcoin/Lightning

铸造厂对盲化的密钥进行签名，因此它可以在之后验证代币，而无需在发行时看到原始密钥。这打破了铸造厂内部存款与赎回之间的直接关联。

## 安全与信任模型

Cashu 改善了支付隐私，但它仍然是托管式的。铸造厂可以拒绝赎回、离线或丢失备付资金。

Cashu 证明是不记名票据。谁控制了证明，谁就能花费它。这使得证明的处理更像现金而非账户余额：备份、设备泄露或明文代币泄漏都会立即产生影响。

## Nostr 集成

Cashu 以多种方式与 Nostr 集成：

- **Nutzaps**：作为 zaps 发送的 ecash 代币，具有增强的隐私性
- **托管**：用于拼车等服务的基于 HTLC 的支付托管
- **钱包**：Nostr 原生钱包在中继上存储加密的 Cashu 代币
- **[NIP-87](/zh/topics/nip-87/)**：通过 Nostr 进行铸造厂发现和评价

## 权衡

Cashu 速度快，因为转账发生在链下，通常在赎回之前也在铸造厂外进行。权衡在于互操作性和信任。

在实践中，用户通常需要使用相同的铸造厂，或者需要在铸造厂之间进行兑换或桥接。这就是 Nostr 应用程序经常将 Cashu 与铸造厂发现、钱包同步和评价系统结合使用的原因。

---

**主要来源：**
- [Cashu NUTs 仓库](https://github.com/cashubtc/nuts)
- [NUT-00：密码学和模型](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60：Cashu 钱包](/zh/topics/nip-60/)
- [NIP-87：Cashu 铸造厂推荐](/zh/topics/nip-87/)

**提及于：**
- [第7期周刊](/zh/newsletters/2026-01-28-newsletter/)
- [第11期周刊](/zh/newsletters/2026-02-25-newsletter/)

**另请参阅：**
- [NIP-60：Cashu 钱包](/zh/topics/nip-60/)
- [NIP-87：Cashu 铸造厂推荐](/zh/topics/nip-87/)
