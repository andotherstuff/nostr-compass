---
title: "FROST（灵活的轮次优化 Schnorr 门限签名）"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2026-03-07
draft: false
categories:
  - Cryptography
  - Protocol
---

FROST（Flexible Round-Optimized Schnorr Threshold Signatures）是一种门限签名方案，允许一组参与者在没有任何人持有完整私钥的情况下生成一个有效的 Schnorr 签名。

## 工作原理

FROST 支持 T-of-N 签名。任意门限数量的参与者可以合作为群组公钥生成签名。

签名协议使用两轮：

1. **承诺轮**：每个参与者生成并共享加密承诺
2. **签名轮**：参与者将各自的部分签名合并为最终的聚合签名

最终输出的验证方式与普通 Schnorr 签名相同。验证者看到的是一个公钥下的一个签名，而非一组共同签名者的列表。

## 安全说明

随机数处理至关重要。RFC 明确规定签名随机数是一次性使用的。重复使用可能泄漏密钥材料。

RFC 也没有标准化分布式密钥生成。它仅规定了签名协议本身，并在附录中包含了可信分发者密钥生成。在实践中，FROST 部署的安全性取决于签名流程和密钥份额的创建及存储方式。

## Nostr 中的使用场景

在 Nostr 环境中，FROST 可以支持：

- **法定人数治理**：群组可通过 T-of-N 方案共享 nsec，成员可以代表自己或委托给理事会
- **多重签名管理**：需要多个管理员签名的社区管理
- **去中心化密钥管理**：在多方之间分配信任以执行关键操作

## 状态

FROST 在 [RFC 9591](https://datatracker.ietf.org/doc/rfc9591/) 中有规定，于 2024 年 6 月在 IRTF 流上发布。这为该协议提供了一个稳定的公开规范，但它不是 IETF 标准轨道 RFC。

---

**主要来源：**
- [RFC 9591：FROST 协议](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST 论文（IACR）](https://eprint.iacr.org/2020/852.pdf)
- [Zcash Foundation Rust 实现](https://github.com/ZcashFoundation/frost)

**提及于：**
- [第3期周刊：NIPs 仓库](/zh/newsletters/2025-12-31-newsletter/#nips-repository)
- [第8期周刊](/zh/newsletters/2026-02-04-newsletter/)
- [第10期周刊](/zh/newsletters/2026-02-18-newsletter/)

**另请参阅：**
- [NIP-46：Nostr Connect](/zh/topics/nip-46/)
- [NIP-55：Android 签名器应用](/zh/topics/nip-55/)
