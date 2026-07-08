---
title: "CLINK：面向 Nostr 密钥的通用 Lightning 接口"
date: 2026-06-17
draft: false
translationOf: /en/topics/clink.md
translationDate: 2026-07-01
categories:
  - Payments
  - Lightning
---

CLINK（Common Lightning Interface for Nostr Keys，面向 Nostr 密钥的通用 Lightning 接口）是一种提议的支付请求格式，让发送方可以通过单一的 noffer 接口向任意具备 Nostr 密钥的身份付款。CLINK noffer 编码了收款方的 Nostr 公钥，以及足够的路由元数据，使发送方的钱包能够构造一笔 Lightning 支付、一笔链上支付或者未来的其他结算原语，并最终结算到收款方。收款方为每个身份发布一个 noffer，发送方支付时无需知道收款钱包是通过 Lightning、链上还是其他通道来结算。

## 工作原理

CLINK noffer 是一种结构化的支付请求，发送方钱包将其解码为具体的支付指令。noffer 承载了：

- 收款方的 Nostr 公钥，作为规范的身份根
- 一个或多个支付端点（Lightning 节点 URI、链上地址派生提示、未来的其他通道）
- 支付的可选元数据（备注、金额、有效期）
- 收款方签名，将 noffer 绑定到其 Nostr 身份

支持 CLINK 的发送钱包读取 noffer，选择自己能够服务的通道（仅支持 Lightning 的钱包支付 Lightning 端点，多通道钱包挑选成本最低的路径），然后提交支付。收款方钱包通过发布或获取相应的完成事件来确认收款，Nostr 公钥作为跨通道的持久身份存在。

## 为什么要有一个以 Nostr 密钥为根的接口

LNURL 和 BOLT-12 已经作为 Lightning 支付请求格式存在，Bitcoin 也有众所周知的链上结算地址格式。CLINK 并不取代其中任何一个。它增加了一层以 Nostr 密钥为根的抽象，让发送方可以通过收款方的 Nostr 身份来寻址，并由钱包决定使用哪一种底层通道。当用户切换 Lightning 提供商、开设新的 mint 或者迁移链上钱包时，只需用同一个 Nostr 密钥重新发布 noffer，发送方无需更新自己的地址簿。

对于 Zeus Pay（它会为每个账户生成一个 CLINK noffer）来说，这意味着发送方仅凭 Nostr 密钥就可以向任意 Zeus 用户付款。对于 Amethyst 的链上 zap 驱动，CLINK 验证状态机会确认链上已签名的 noffer 与 zap 请求中声称的 Nostr pubkey 一致，从而堵住针对未签名链上 zap 的伪造路径。

## 实现

- [Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) 上线了 CLINK noffer 支付支持，Zeus Pay 为每个账户生成一个 CLINK noffer，使发送方仅凭 Nostr 密钥就可以向任意 Zeus 用户付款
- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) 上线了用于链上 zap 校验的 CLINK 驱动，包含一个验证状态机和重新验证驱动（[PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039)、[PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177)、[PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182)）

---

**Primary sources:**
- [Zeus v13.1.0-rc1 release notes](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) - CLINK noffer 上线
- [Amethyst PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039) - NIP-BC 链上 zap 验证状态机与重新验证驱动
- [Amethyst PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177) - 实现 CLINK（面向 Nostr 密钥的通用 Lightning 接口）
- [Amethyst PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182) - 为 CLINK 协议 DTO 添加 kotlinx-serialization 支持

**Mentioned in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/zh/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #27: Zeus v13.1.0-rc1 ships CLINK noffers and queue-less NWC](/zh/newsletters/2026-06-17-newsletter/#zeus-v1310-rc1-ships-clink-noffers-and-queue-less-nwc)

**See also:**
- [NIP-57: Zaps](/zh/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/zh/topics/nip-47/)
