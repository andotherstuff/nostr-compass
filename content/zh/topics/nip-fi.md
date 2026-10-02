---
title: "Buzz NIP-FI：联合身份断言"
date: 2026-09-30
translationOf: /en/topics/nip-fi.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Identity
  - Relays
---

NIP-FI 是 Buzz **项目专属**的联合身份断言规范。这个名称并不意味着它已被 `nostr-protocol/nips` 仓库采纳，也不意味着它能与 Buzz 之外的 relay 互操作。

## HTTP 入口 {#http-ingress}

在强制模式下，对于受保护的 HTTP 请求，Buzz 会把联合身份断言与一个 NIP-98 签名授权 event 配对。由 HTTP 签名证明的 Nostr 公钥必须与断言中指定的密钥一致。缺失、不匹配或无法验证的证据都会被拒绝。Buzz 借助这种配对，把外部身份签发方的授权决定与发出请求的 Nostr 密钥联系起来。

[项目规范修订](https://github.com/block/buzz/pull/7254)定义了强制执行模型。[已合并的 HTTP 入口实现](https://github.com/block/buzz/pull/7264)覆盖了 Buzz 受保护的 HTTP 接口，包括 relay 桥接、媒体、工作流和 Git 路径。该合并报告的是源代码测试；它并不意味着其他 Nostr relay 实现了相同的策略。

---

**主要来源：**
- [Buzz NIP-FI 规范修订](https://github.com/block/buzz/pull/7254)
- [Buzz HTTP 入口实现](https://github.com/block/buzz/pull/7264)

**提及于：**
- [第42期周刊：Buzz 身份控制](/zh/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
