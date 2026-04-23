---
title: "Marmot 协议"
date: 2025-12-17
translationOf: /en/topics/marmot.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot 是一套建立在 Nostr 上的端到端加密群组消息协议。它把 Nostr 的身份与 relay 网络，与 MLS 的群组密钥管理、前向保密和事后恢复安全组合在一起。

## 工作原理

Marmot 使用 Nostr 负责身份、relay 传输和 event 分发，再在其上叠加 MLS 来处理群组成员变化和消息加密。与专注一对一消息的 [NIP-17](/zh/topics/nip-17/) 不同，Marmot 面向的是成员会加入、离开和轮换密钥的群组场景。

## 为什么重要

MLS 为 Marmot 带来了 Nostr 的私信方案本身无法提供的性质：群组状态演化、移除成员的语义，以及在密钥被攻破后通过后续密钥更新完成恢复。

这就是它最有价值的分工。Nostr 在开放网络中解决身份与传输，MLS 解决经过认证的群组密钥协商，而 Marmot 是二者之间的粘合层。

## 实现状态

该协议仍处于实验阶段，但现在已经拥有多个实现和真实应用。[MDK](https://github.com/marmot-protocol/mdk) 是主要的 Rust 参考栈，[marmot-ts](https://github.com/marmot-protocol/marmot-ts) 将这一模型带到 TypeScript，而 [White Noise](https://github.com/marmot-protocol/whitenoise)、[Amethyst](https://github.com/vitorpamplona/amethyst)、Pika 和 Vector 等应用都已经在使用兼容 Marmot 的组件。

最近的工作重点是加固与互操作。以审计为导向的修复在 2026 年初陆续落地，而 MIP-03 则引入了确定性的 commit 决议机制，使客户端在多个 relay 上遇到并发群组状态变更竞态时也能最终收敛。

2026 年 4 月，Amethyst 将其内嵌 MDK 与 MIP-01 和 MIP-05 的 wire format 对齐：[PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) 增加了 TLS 风格长度前缀的 VarInt 编码和基于 MDK test vectors 的往返验证，[PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) 增加了 MIP-00 KeyPackage Relay List 支持，[PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) 补上了跨客户端与 White Noise 测试中暴露的 admin gate 和媒体处理缺口。[PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466) 修正了 MLS commit framing，使加密 welcome 的字节与 mdk-core 输出一致，[PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471) 修复了一个导致多个 co-admin 状态分叉的外层解密 bug。后续的 [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) 又增加了完整的 MLS commit 密码学验证，而 [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) 则发布了 `amy`，一个由 Amethyst 实现驱动的 Marmot/MLS 群组操作 CLI。

MDK 方面，[PR #261](https://github.com/marmot-protocol/mdk/pull/261) 通过把群组的 `RequiredCapabilities` 计算为被邀请者能力的 LCD，打通了 Amethyst 与 White Noise 之间的跨版本邀请；[PR #262](https://github.com/marmot-protocol/mdk/pull/262) 在持久化创建者 signer 之前先解析被邀请者 key packages；[PR #264](https://github.com/marmot-protocol/mdk/pull/264) 统一了不同实现之间的 SelfUpdate wire format；[PR #265](https://github.com/marmot-protocol/mdk/pull/265) 暴露了 `group_required_proposals` 访问器。

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) 也正处于从全局单例迁移到按账户划分的 `AccountSession` 视图的多阶段重构中：[PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) 建起了 `AccountSession` 与 `AccountManager` 骨架，之后的各阶段已陆续把 relay handles、草稿与设置、消息操作、群组读写、成员关系、push notifications、key-package 读取、群组创建，以及截至 [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770) 的 session 级 event dispatch 都迁移过去。[marmot-ts PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68) 则把 TypeScript 客户端迁移到了可寻址的 kind `30443` key packages。

---

**主要来源：**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)
- [MLS Protocol](https://messaginglayersecurity.rocks/)
- [Marmot Development Kit (MDK)](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)
- [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)
- [White Noise client](https://github.com/marmot-protocol/whitenoise)
- [Amethyst PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) - MIP-01/MIP-05 wire format alignment
- [Amethyst PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) - MIP-00 KeyPackage Relay List
- [Amethyst PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) - Amy CLI

**提及于：**
- [Newsletter #1：News](/zh/newsletters/2025-12-17-newsletter/)
- [Newsletter #1：Releases](/zh/newsletters/2025-12-17-newsletter/)
- [Newsletter #4](/zh/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/zh/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/zh/newsletters/2026-03-04-newsletter/)
- [Newsletter #19：Amethyst MIP 兼容](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19：MDK 互操作工作](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19：whitenoise-rs session 重构](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [MLS（Message Layer Security）](/zh/topics/mls/)
- [MIP-05：隐私保护型 Push Notifications](/zh/topics/mip-05/)
- [NIP-17：私密私信](/zh/topics/nip-17/)
- [NIP-59：Gift Wrap](/zh/topics/nip-59/)
