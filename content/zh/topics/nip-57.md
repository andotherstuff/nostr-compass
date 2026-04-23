---
title: "NIP-57：Zaps"
date: 2025-12-17
translationOf: /en/topics/nip-57.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 定义了 zaps，也就是把 Lightning 支付附着到 Nostr 身份和内容上的方式。它同时标准化了获取 zap-enabled invoice 的请求，以及 wallet 在付款完成后发布的 receipt event。

## 工作原理

1. 客户端从 profile 元数据或目标 event 上的 `zap` tag 中发现接收者的 LNURL endpoint。
2. 客户端把签名后的 kind `9734` zap request 发送到接收者的 LNURL callback，而不是 relays。
3. 用户支付 invoice。
4. 接收者的 wallet 服务器将 kind `9735` zap receipt 发布到 zap request 中列出的 relays。
5. 客户端验证并展示 zap。

## Zap Request（kind 9734）

zap request 是一个已签名 event，用来标识付款人以及计划支付的目标。它通常包括：

- 带接收者 pubkey 的 `p` tag
- 指向被 zap event 的 `e` tag（可选）
- 以 millisatoshis 表示金额的 `amount` tag
- 用于指定 receipt 应发布到哪里的 `relays` tag

可寻址内容可以使用 `a` tag 来替代或补充 `e` tag。可选的 `k` tag 用于记录目标 kind。

## Zap Receipt（kind 9735）

它由接收者的 wallet 服务器在付款确认后发布，包含：

- `description` tag 中的原始 zap request
- 带已支付 invoice 的 `bolt11` tag
- 用于证明付款的 `preimage` tag

客户端应当使用接收者 LNURL 响应中的 `nostrPubkey`、invoice 金额以及原始 zap request 来验证 receipt。没有经过这一步验证的 receipt，只能算是一种付款声明。

## 信任与权衡

zaps 的价值在于，它们让支付可以在社交图谱中可见，但 receipt 仍然是由接收者的 wallet 基础设施创建的。规范本身也明确指出，zap receipt 不是一种通用的付款证明。更准确地说，它是一条由 wallet 签名的声明，表示某张与 zap request 绑定的 invoice 已被支付。

在把 receipt 显示为有效 zap 之前，验证型客户端应检查四件事：receipt 的签名是否匹配接收者 LNURL 响应中广告的 `nostrPubkey`，`bolt11` invoice 金额是否与嵌入 zap request 中的 `amount` tag 一致，invoice 的 description hash 是否绑定到字符串化的 zap request，以及 `preimage` 是否哈希到 invoice 的 `payment_hash`。如果客户端在不做这些校验的情况下就展示汇总后的 zap 数量，那么攻击者只需发布伪造的 kind `9735` events 就能轻易欺骗它。

## Private 与 Anonymous Zaps

private zaps 在此基础上额外增加了一层保密性。发送者可以把 zap request 的 `content` 加密给接收者，并在外层请求上加入 `anon` tag，这样 relay 网络能看到支付目标，但无法读取附带留言。anonymous zap 更进一步：客户端会为 zap request 本身生成新的临时 keypair，因此 receipt 仍能证明付款发生过，但接收者无法把这次 zap 与发送者长期使用的 pubkey 关联起来。

## Zap Goals 与 Splits

NIP-57 也是 [NIP-75](/zh/topics/nip-75/) 所定义 zap-goal 系统的基础。goal 是一种 kind `9041` event，用于声明目标金额和统计 receipts 的 relay 集，而客户端则通过把匹配 kind `9735` events 中已验证过的 `bolt11` 金额相加，来计算 goal 进度。

zap splits 定义在 NIP 的附录中，允许接收者在 kind `0` profile 中发布多个带权重的 `zap` tags，这样一笔 zap 支付就能原子性地分配给多个 pubkeys。[Amethyst](https://github.com/vitorpamplona/amethyst)、[Damus](https://github.com/damus-io/damus) 和 [noStrudel](https://github.com/hzrd149/nostrudel) 都已经端到端实现了 split-paying。

---

**主要来源：**
- [NIP-57 Specification](https://github.com/nostr-protocol/nips/blob/master/57.md)

**提及于：**
- [Newsletter #1：News](/zh/newsletters/2025-12-17-newsletter/)
- [Newsletter #2：News](/zh/newsletters/2025-12-24-newsletter/)
- [Newsletter #3：Notable Code Changes](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #9：NIP Updates](/zh/newsletters/2026-02-11-newsletter/)
- [Newsletter #19：NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-47：Nostr Wallet Connect](/zh/topics/nip-47/)
- [NIP-75：Zap Goals](/zh/topics/nip-75/)
- [NIP-53：Live Activities](/zh/topics/nip-53/)
