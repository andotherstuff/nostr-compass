---
title: "Cashu：Ecash 协议"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-04-22
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu 是一个建立在 Bitcoin 和 Lightning 之上的 Chaumian ecash 协议。用户持有由 mint 发行的不记名 tokens，然后在不向 mint 暴露完整支付图谱的情况下转移这些 tokens。

## 工作原理

Cashu 使用盲签名来发行 ecash tokens：

1. **Minting**：用户向 mint 存入 Bitcoin/Lightning，并接收盲化 tokens
2. **Spending**：tokens 可以在点对点之间转移，无需 mint 参与
3. **Redemption**：接收方在 mint 处将 tokens 兑换回 Bitcoin/Lightning

mint 对盲化后的 secrets 进行签名，因此它之后可以验证 tokens，却无法在发行时看到原始 secrets。这就切断了 mint 内部存款与赎回之间的直接关联。

## 安全与信任模型

Cashu 提升了支付隐私，但它仍然是托管式的。mint 可以拒绝兑付、离线，或失去备付资金。

Cashu proofs 是不记名票据。谁控制 proof，谁就能花掉它。这让 proof 的处理更像现金，而不是账户余额：备份、设备被攻破，或明文 token 泄露，都会立刻产生后果。

## Nostr 集成

Cashu 以多种方式与 Nostr 集成：

- **Nutzaps**：以 ecash token 形式发送的 zaps，具有更强隐私性
- **Escrow**：适用于拼车等服务的基于 HTLC 的支付托管
- **Wallets**：Nostr 原生钱包会在 relays 上存储加密后的 Cashu tokens
- **[NIP-87](/zh/topics/nip-87/)**：通过 Nostr 做 mint 发现与评价
- **[TollGate](/zh/topics/tollgate/)**：一种按量付费的网络接入协议，会接受 Cashu ecash tokens 作为连接费用；截至其 [v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)，该行为已由 [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) 定义

## 权衡

Cashu 很快，因为转移发生在链下，并且在兑付之前通常也不需要 mint 参与。代价则是互操作性与信任。

在实践中，用户通常需要使用同一个 mint，或者依赖不同 mints 之间的 swap 或 bridge。这也是为什么 Nostr 应用经常把 Cashu 与 mint 发现、wallet 同步和评价系统一起使用。

---

**主要来源：**
- [Cashu NUTs Repository](https://github.com/cashubtc/nuts)
- [NUT-00: Cryptography and models](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)
- [NIP-87 Specification](https://github.com/nostr-protocol/nips/blob/master/87.md)

**提及于：**
- [Newsletter #7](/zh/newsletters/2026-01-28-newsletter/)
- [Newsletter #11](/zh/newsletters/2026-02-25-newsletter/)
- [Newsletter #19：TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-60：Cashu Wallet](/zh/topics/nip-60/)
- [NIP-87：Cashu Mint Recommendations](/zh/topics/nip-87/)
- [TollGate](/zh/topics/tollgate/)
