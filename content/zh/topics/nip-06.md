---
title: "NIP-06：助记词密钥派生"
date: 2026-10-28
translationOf: /en/topics/nip-06.md
translationDate: 2026-10-28
draft: false
categories: ["Identity", "Keys"]
---

NIP-06 描述了如何从助记词种子短语派生 Nostr 密钥对。[当前官方 NIP-06 文本](https://github.com/nostr-protocol/nips/blob/master/06.md)被标记为草案（draft）且为可选，并带有以下警告：

> __警告__ `unrecommended`：优先使用单个 nsec

本页出于历史兼容性的考虑介绍 NIP-06，并不推荐采用种子派生。

## 工作原理

根据[当前规范](https://github.com/nostr-protocol/nips/blob/master/06.md)，BIP39 用于生成助记词，并从这些词派生出二进制种子。随后，BIP32 沿路径 `m/44'/1237'/<account>'/0/0` 派生密钥，其中 1237 是 Nostr 在 SLIP44 中的条目。基础客户端可以使用账户 0。递增账户值，即可从同一种子得到其他密钥。只有当两个实现在派生步骤上保持一致，并对结果使用正确的编码时，它们才能重现相同的身份。

## 测试向量

一个 [2023 年 10 月 12 日的 commit](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b) 添加了两个测试向量：一个基于 12 个单词的助记词构建，另一个基于 24 个单词的助记词构建。每个向量都以十六进制列出预期的私钥和公钥，并附有对应的 nsec 和 npub 编码。开发者可以借助这些向量交叉检验各自的实现。这些向量并不涉及密钥保管，不能证明安全性，也不保证普遍的互操作性。

## 另请参阅

- [NIP-01](/zh/topics/nip-01/)

**原始资料：**

- [NIP-06（当前版本）](https://github.com/nostr-protocol/nips/blob/master/06.md)
- [添加 NIP-06 测试向量的 commit（2023 年 10 月 12 日）](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)

**提及于：**

- [第 46 期新闻简报](/zh/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)
