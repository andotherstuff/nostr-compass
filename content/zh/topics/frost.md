---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2025-12-31
draft: false
categories:
  - 密码学
  - 协议
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) 是一种门限签名方案，允许一组参与者协作生成有效的Schnorr签名，而无需任何单一方持有完整的私钥。

## 工作原理

FROST支持T-of-N门限签名，即N个密钥持有者中的T个参与者必须合作才能生成有效签名。该协议分两轮运行：

1. **承诺轮**: 每个参与者生成并共享加密承诺
2. **签名轮**: 参与者将各自的部分签名合并为最终的聚合签名

生成的签名与标准Schnorr签名无法区分，保持与现有验证系统的向后兼容性。

## 关键特性

- **门限安全**: 单个参与者无法独自签名；T方必须合作
- **轮次效率**: 签名仅需两轮通信
- **防伪保护**: 新技术可防御针对先前门限方案的攻击
- **签名聚合**: 多个签名合并为单个紧凑签名
- **隐私性**: 最终签名不会透露哪T个参与者进行了签名

## Nostr中的使用场景

在Nostr环境中，FROST可实现：

- **法定人数治理**: 群组可通过T-of-N方案共享nsec，成员可以代表自己或委托给理事会
- **多重签名管理**: 需要多个管理员签名的社区管理
- **去中心化密钥管理**: 在多方之间分配信任以执行关键操作

## 标准化

FROST于2024年6月被标准化为RFC 9591，标题为"The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures"。

---

**主要来源:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [University of Waterloo CrySP](https://crysp.uwaterloo.ca/software/frost/)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**相关提及:**
- [Newsletter #3: NIPs仓库](/zh/newsletters/2025-12-31-newsletter/#nips-repository)

**另请参阅:**
- [NIP-XX Quorum提案](https://github.com/nostr-protocol/nips/pull/2179)
