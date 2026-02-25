---
title: "NIP-90"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 定义了数据自动售货机（DVM），这是一种在 Nostr 上请求和支付计算工作的市场协议。

## 工作原理

客户端发布任务请求 event（kind 5000-5999），说明所需的计算内容。服务提供商监听与其能力匹配的请求，完成计算后发布结果。支付通过 Lightning 或任务流程中协商的其他机制完成。

任务类型由 kind 决定，涵盖文本生成、图像生成、翻译、内容发现等不同计算类型。每种 kind 规定了预期的输入/输出格式。

## 主要特性

- 去中心化计算市场
- 基于 kind 的任务类型系统
- 提供商在价格和质量上竞争
- 可扩展以支持新的计算类型

---

**主要来源：**
- [NIP-90 规范](https://github.com/nostr-protocol/nips/blob/master/90.md)

**提及于：**
- [Newsletter #11：NIP-AC DVM 代理协调](/zh/newsletters/2026-02-25-newsletter/#nip-更新)

**参见：**
- [NIP-85：Trusted Assertions](/zh/topics/nip-85/)
