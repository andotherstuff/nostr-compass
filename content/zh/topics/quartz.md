---
title: "Quartz"
date: 2025-12-31
draft: false
translationOf: /en/topics/quartz.md
translationDate: 2026-03-07
categories:
  - Library
  - Development
---

Quartz 是由 Vitor Pamplona 开发的 Kotlin 多平台 Nostr 库。它是 Amethyst 从单一代码库推进 Android、桌面端乃至最终 iOS 支持的共享协议和数据层。

## 工作原理

Quartz 作为共享库提供核心 Nostr 功能：

- **事件处理**：Nostr 事件的解析、验证和创建
- **密码学**：Secp256k1 签名、NIP-44 加密、密钥管理
- **中继通信**：连接管理、消息排序、订阅处理
- **NIP 支持**：常见 NIP 的实现，包括 NIP-06、NIP-19、NIP-44 等

## 重要意义

Quartz 将协议密集型逻辑从单个应用中提取到可复用的库中。这很重要，因为中继处理、事件解析、加密和存储规则变得更容易在客户端之间共享，而不是在每个平台上重新实现。

具体成果已经体现在 Amethyst 的桌面端工作中。资助支持的重构将共享代码移入 Kotlin 多平台模块，如 `commonMain`、`jvmAndroid` 和 `jvmMain`，使桌面端支持变成了库和模块问题，而非完整重写。

## 架构

该库使用模块化的源集结构：
- `commonMain`：所有平台的共享代码
- `jvmAndroid`：JVM 和 Android 之间共享的代码
- `androidMain`：Android 特定实现
- `jvmMain`：桌面端 JVM 实现
- `iosMain`：iOS 特定实现

## 当前状态

2025 年 12 月，OpenSats 在第十四波 Nostr 资助中宣布资助 Quartz。该仓库作为独立库存在，但迄今为止大部分可见进展是通过 Amethyst 的 PR 落地的，这些 PR 将应用模块转换为多平台代码并跟踪各目标平台的功能对等性。

---

**主要来源：**
- [Quartz 仓库](https://github.com/vitorpamplona/quartz)
- [Quartz on Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Amethyst 仓库](https://github.com/vitorpamplona/amethyst)
- [OpenSats 第十四波 Nostr 资助](https://opensats.org/blog/fourteenth-wave-of-nostr-grants)

**提及于：**
- [Newsletter #3：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3：新闻](/zh/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3：Amethyst 重要变更](/zh/newsletters/2025-12-31-newsletter/#amethyst-android)

**另请参阅：**
- [Blossom 协议](/zh/topics/blossom/)
