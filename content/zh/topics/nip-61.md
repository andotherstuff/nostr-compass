---
title: "NIP-61：Nutzap"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-61.md
translationDate: 2026-07-01
categories:
  - Zaps
  - Ecash
---

NIP-61 定义了 "nutzap"，即以 Nostr 事件形式传递的点对点 Cashu ecash 支付。发送方发布一个 P2PK 锁定的 Cashu token，指向收款方的 Nostr 密钥，收款方可在方便时向 mint 兑付。proof 本身承载了价值，因此一笔 NIP-61 支付以自包含 token 的形式送达，收款方可按自己的节奏兑付，无需 Lightning 通道或交互式握手。

## 工作原理

NIP-61 建立在两个既有原语之上：[NIP-60](/zh/topics/nip-60/) Cashu 钱包和 Cashu 的 P2PK 锁。整个流程使用三种事件 kind。

**Mint 推荐（kind 10019）：** 收款方发布的可替换事件，声明自己接受 nutzap 的 mint，以及用于将 proof 锁定给自己的 Cashu 公钥。发送方在发送前先读取该事件，以确保锁定的 token 是收款方可以兑付的。

**Nutzap 事件（kind 9321）：** 支付本身。它承载 Cashu proof（P2PK 锁定到收款方在 kind 10019 中声明的 nutzap pubkey）、mint URL、可选的用于标识被 zap 的 note 的 `e` 和 `a` tag，以及一个指向收款方的 `p` tag。收款方通过正常的 Nostr 订阅收到该事件，用相应的私钥解锁 proof，然后将其存入自己的 NIP-60 钱包，或熔付为 Lightning。

**Nutzap 信息（kind 7375）：** 缓存状态，与 NIP-60 的 token 事件具有相同结构，用于记录已兑付的 nutzap proof，防止钱包在重新同步时重复计算。

## 权衡与信任模型

一枚 nutzap 是一个自包含的 ecash token。只要收款方之后能够联系到 mint，就可以兑付该笔支付。mint 本身是受信任的托管方，与 NIP-60 是同一种信任模型，而这种托管选择正是可离线、可即时最终确定的微支付明确要付出的代价。NIP-57 zap 要求收款方运行（或托管在）一个 Lightning 节点，并提供实时接受 HTLC 的 LNURL 端点。没有 Lightning 通道的手机、位于防火墙之后的用户，以及碰巧离线的收款方，都被排除在该模型之外。

Kind 10019 广告是社交层的信任门。发送方从收款方接受的 mint 中挑选一家，让收款方的兑付路径保持可预测。如果发送方挑选了收款方名单之外的 mint，就有生成无法兑付 token 的风险，因此钱包会先读取 kind 10019。

## 流程

1. 收款方发布一个 kind 10019，声明接受的 mint 和一个 nutzap pubkey
2. 发送方读取 kind 10019，在列出的一家 mint 铸造 proof，并用 P2PK 将其锁定到收款方的 nutzap pubkey
3. 发送方发布一个 kind 9321，携带锁定的 proof、mint URL 和目标 tag
4. 收款方通过正常的 Nostr 订阅收到该 kind 9321
5. 收款方使用其 nutzap 私钥解锁 proof，然后将其保留在自己的 NIP-60 钱包中，或熔付为 Lightning

## Nutzap 事件示例

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1750162800,
  "kind": 9321,
  "tags": [
    ["proof", "{\"amount\":21,\"secret\":\"...\",\"C\":\"...\",\"id\":\"...\"}"],
    ["u", "https://mint.example.com"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3"],
    ["p", "c5d8a4e3b2a1f0e9d8c7b6a5949382716050403020100ffeeddccbbaa99887766"]
  ],
  "content": "Great post!",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

## 实现

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) 在其 NIP-60/NIP-61 钱包界面上线了 nutzap 渲染，包含按 mint 分别显示的余额视图（[PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075)）

---

**Primary sources:**
- [NIP-61 Specification](https://github.com/nostr-protocol/nips/blob/master/61.md)
- [Amethyst PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075) - NIP-60 Cashu 钱包与 NIP-61 nutzap 支持

**Mentioned in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/zh/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**See also:**
- [NIP-57: Zaps](/zh/topics/nip-57/)
- [NIP-60: Cashu Wallet](/zh/topics/nip-60/)
- [Cashu](/zh/topics/cashu/)
