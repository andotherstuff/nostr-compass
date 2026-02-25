---
title: "NIP-85"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85 定义了可信断言（Trusted Assertions）系统，允许将高成本计算委托给可信服务提供商，由其将签名结果作为 Nostr event 发布。

## 工作原理

Web of Trust 评分、参与度指标以及其他计算值需要爬取多个 relay 并处理大量 event。这类工作在移动设备上不切实际。NIP-85 允许专门的服务提供商执行这些计算并发布供客户端查询的结果。

服务提供商通过 kind 30085 event 公布其能力。客户端通过查询用户已关注或信任的 pubkey 的这些公告来发现提供商。结果以由提供商签名的 kind 30382 event 形式返回。

## 主要特性

- 资源密集型指标的委托计算
- 通过社交图谱发现提供商
- 用于可验证结果的签名断言
- 客户端侧信任决策

---

**主要来源：**
- [NIP-85 规范](https://github.com/nostr-protocol/nips/blob/master/85.md)

**提及于：**
- [Newsletter #10：NIP-85 深入解析](/zh/newsletters/2026-02-18-newsletter/#nip-深入解析nip-85-可信断言)
- [Newsletter #11：NIP-85 服务提供商可发现性](/zh/newsletters/2026-02-25-newsletter/#nip-更新)

**参见：**
- [Web of Trust](/zh/topics/web-of-trust/)
