---
title: "NIP-85：可信断言"
date: 2026-02-18
draft: false
translationOf: /en/topics/nip-85.md
translationDate: 2026-03-07
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85 定义了可信断言（Trusted Assertions），一种将复杂计算委托给可信服务提供商的系统，提供商将签名结果作为 Nostr 事件发布。

## 工作原理

信任网络评分、互动指标和其他计算值需要爬取大量中继并处理海量事件。这项工作在移动设备上不切实际。NIP-85 允许专业提供商执行这些计算并发布客户端可查询的结果。

可信断言是可寻址事件。`d` 标签标识被评分的主体，事件类型标识主体的类型：公钥（30382）、常规事件（30383）、可寻址事件（30384）和 NIP-73 标识符（30385）。

用户通过 kind 10040 声明信任哪些提供商。这些提供商列表可以是标签中的公开信息，也可以用 [NIP-44](/zh/topics/nip-44/) 加密在事件内容中，当用户不想公开披露其信任输入时这一点很重要。

## 重要意义

NIP-85 的核心洞察在于它标准化了输出格式，而非算法。两个提供商可以都为同一公钥发布 `rank` 标签，同时使用不同的信任网络公式、静音处理、中继覆盖范围或反垃圾启发式算法。客户端保持互操作性，因为结果格式一致，即使计算方式不同。

这比假装会有一个规范的排名服务更适合 Nostr。用户自己选择信任谁的断言。

## 信任模型

服务提供商必须签名自己的断言事件，规范建议为不同的算法或用户特定的视角使用不同的服务密钥。这防止提供商将不相关的排名系统合并到一个不透明的身份中。

信任仍然是本地的。签名的输出证明了哪个提供商发布了评分，而不是评分是否正确。客户端需要制定策略来决定使用哪些提供商密钥、从哪些中继获取数据，以及如何处理相互矛盾的断言。

## 互操作说明

NIP-85 不仅限于人和帖子。kind 30385 允许提供商为 NIP-73 外部标识符（如书籍、网站、话题标签和地点）评分。这为 Nostr 之外的主题建立了可互操作的声誉和互动数据通道。

---

**主要来源：**
- [NIP-85 规范](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #2223](https://github.com/nostr-protocol/nips/pull/2223) - 服务提供商可发现性指南

**提及于：**
- [Newsletter #10：NIP-85 深度解析](/zh/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #11：NIP-85 服务提供商可发现性](/zh/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12：协议回顾](/zh/newsletters/2026-03-04-newsletter/)

**另请参阅：**
- [NIP-44：加密载荷](/zh/topics/nip-44/)
- [NIP-73：外部内容标识符](/zh/topics/nip-73/)
- [信任网络](/zh/topics/web-of-trust/)
