---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2025-12-31
draft: false
categories:
  - 库
  - 开发
---

Quartz是由Vitor Pamplona开发的Nostr Kotlin Multiplatform库。它最初从Amethyst Android客户端提取，为JVM、Android、iOS和Linux平台提供可复用的Nostr协议实现。

## 工作原理

Quartz作为共享库提供Nostr核心功能：

- **事件处理**：Nostr事件的解析、验证和创建
- **加密**：Secp256k1签名、NIP-44加密、密钥管理
- **Relay通信**：连接管理、消息排序、订阅处理
- **NIP支持**：实现常见NIP，包括NIP-06、NIP-19、NIP-44等

## 主要特性

- **Kotlin Multiplatform**：单一代码库编译到多个目标平台
- **目标平台**：Android、JVM、iOS（ARM64、模拟器）、Linux
- **性能优化**：高效的事件处理和加密操作
- **Blossom集成**：通过Blossom协议支持媒体上传
- **OpenTimestamp**：用于时间戳验证的完整Kotlin移植

## 架构

该库使用模块化的源代码集结构：
- `commonMain`：所有平台的共享代码
- `jvmAndroid`：JVM和Android之间共享的代码
- `androidMain`：Android专用实现
- `jvmMain`：桌面JVM实现
- `iosMain`：iOS专用实现

## OpenSats资助

2025年12月，OpenSats宣布将Quartz纳入其第十四轮Nostr资助计划。该资助支持持续开发，以通过与Android和桌面版本相同的Kotlin Multiplatform方法在iOS上实现Amethyst。

---

**主要来源：**
- [Maven Central上的Quartz](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Amethyst仓库](https://github.com/vitorpamplona/amethyst)

**提及于：**
- [Newsletter #3: 十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3: 新闻](/zh/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3: Amethyst重要变更](/zh/newsletters/2025-12-31-newsletter/#amethyst-android)

**另请参阅：**
- [Blossom协议](/zh/topics/blossom/)
