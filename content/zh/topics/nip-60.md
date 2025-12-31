---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2025-12-31
draft: false
categories:
  - 钱包
  - Ecash
---

NIP-60 定义了基于 Cashu 的 ecash 钱包如何在 Nostr 中运作。钱包信息存储在 relay 上，实现了无需单独账户即可在不同应用程序中使用的便携式钱包。

## 工作原理

NIP-60 使用三种存储在 relay 上的事件类型：

**钱包事件（kind 17375）：** 一个可替换事件，包含加密的钱包配置，包括 mint URL 和用于接收付款的私钥。此密钥与用户的 Nostr 身份密钥分开。

**代币事件（kind 7375）：** 存储加密的未花费 Cashu 证明。当证明被花费时，客户端删除旧事件并用剩余证明创建新事件。

**支出历史（kind 7376）：** 显示资金流动的可选交易记录，包含加密内容以及对已创建/销毁的代币事件的引用。

## 主要特点

- **易用性** - 新用户无需外部账户设置即可立即接收 ecash
- **互操作性** - 钱包数据在不同的 Nostr 应用程序中跟随用户
- **隐私性** - 所有钱包数据都使用用户的密钥加密
- **证明管理** - 追踪哪些代币事件已被花费以防止双重支付

## 工作流程

1. 客户端从 relay 获取钱包配置
2. 加载并解密代币事件以获取可用资金
3. 支出时创建新的代币事件并删除旧事件
4. 可选的历史事件记录交易供用户参考

---

**主要来源：**
- [NIP-60 规范](https://github.com/nostr-protocol/nips/blob/master/60.md)

**相关提及：**
- [新闻通讯 #3：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**另请参阅：**
- [NIP-57：Zaps](/zh/topics/nip-57/)
- [NIP-47：Nostr Wallet Connect](/zh/topics/nip-47/)
