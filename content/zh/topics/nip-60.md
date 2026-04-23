---
title: "NIP-60：Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Ecash
---

NIP-60 定义了基于 Cashu 的 ecash wallets 如何在 Nostr 内运行。wallet 信息被存储在 relays 上，因此可以形成可移植的钱包，在不同应用之间工作，而无需单独注册账户。

## 工作原理

NIP-60 使用三种存储在 relays 上的核心 event 类型，以及一种可选的、用于待处理 quotes 的辅助 event：

**Wallet Event（kind 17375）：** 一种可替换 event，包含加密后的 wallet 配置，其中包括 mint URLs 和一个用于接收付款的私钥。这个 key 与用户的 Nostr 身份 key 分离。

**Token Events（kind 7375）：** 存储加密后的、未花费的 Cashu proofs。当 proofs 被花掉后，客户端会删除旧 event，并创建一个带有剩余 proofs 的新 event。

**Spending History（kind 7376）：** 可选的交易记录，用来展示资金流动，内容经过加密，并引用被创建或销毁的 token events。

**Quote Events（kind 7374）：** 可选的、面向待处理 mint quotes 的加密状态。规范建议这些 event 应当是短生命周期的，并带有 expiration tags，主要用于本地状态不足以处理的情况。

## 状态模型

NIP-60 关注的是 wallet 状态同步，而不是“接收金钱”这个动作本身。wallet event 告诉客户端该使用哪些 mints 和哪个 wallet key，而 token events 才是真正的余额状态，因为它们包含未花费 proofs。

这一区分对互操作很重要。两个客户端只有在以同样方式解释 token rollover 时，才能展示同一个 wallet：花掉 proofs、发布替代 proofs，并通过 [NIP-09](/zh/topics/nip-09/) 删除已花费的 token event，这样其他客户端才不会继续把已经花掉的 proofs 计入余额。

## 为什么重要

- **易用性** - 新用户无需额外注册账户，就能立刻接收 ecash
- **互操作性** - wallet 数据会跟随用户出现在不同的 Nostr 应用中
- **隐私** - 所有 wallet 数据都加密到用户自己的 keys 上
- **Proof 管理** - 追踪 wallet 状态变迁，让多个客户端能收敛到同一个余额

## 互操作说明

客户端会先通过 kind 10019 查找 wallet relay 信息；如果没有单独的 wallet relay list，则回退到用户的 [NIP-65](/zh/topics/nip-65/) relay list。这种回退很有用，但也意味着 wallet 的可移植性仍然依赖这些 relays 真的会存储并提供加密后的 wallet events。

规范还要求 wallet 私钥与用户的 Nostr 身份 key 保持分离。这样一来，wallet 收款相关处理就不会与主签名 key 混在一起，也能降低同一个 key 被复用到两个不同目的上的风险。

## 工作流

1. 客户端从 wallet relays 或用户的 relay list 中抓取 wallet 配置
2. 加载并解密 token events，以获得可用资金
3. 花费时创建新的 token events，并删除旧 ones
4. 可选的 history events 记录交易，供用户查看

---

**主要来源：**
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)

**提及于：**
- [Newsletter #3：December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #11：NIP Deep Dive](/zh/newsletters/2026-02-25-newsletter/)
- [Newsletter #13：Shopstr and Milk Market Open MCP Commerce Surfaces](/en/newsletters/2026-03-11-newsletter/)

**另请参阅：**
- [NIP-57：Zaps](/zh/topics/nip-57/)
- [NIP-09：Event Deletion Request](/zh/topics/nip-09/)
- [NIP-47：Nostr Wallet Connect](/zh/topics/nip-47/)
