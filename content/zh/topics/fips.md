---
title: "FIPS"
date: 2026-02-25
translationOf: /en/topics/fips.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Networking
  - Infrastructure
---

FIPS（Free Internetworking Peering System）是一个自组织网状网络协议，使用 Nostr 风格的 secp256k1 密钥对作为节点身份。

## 工作原理

FIPS 旨在让对等网络在没有中央服务器或证书颁发机构的情况下运行。节点发现邻居、构建路由状态，并仅使用本地知识转发数据包。

该设计结合了生成树和布隆过滤器可达性数据。每个节点获得相对于树的坐标，然后贪心地向目标路由。如果贪心路由失败，树仍然提供一条回退路径。

两个加密层保护流量。链路层加密（Noise IK 模式）保护邻居之间的逐跳通信。会话层加密（Noise XK 模式）提供端到端保护，防止中间路由器窥探。

## 重要意义

FIPS 复用了 Nostr 开发者已经熟悉的密钥模型，但将其应用于数据包路由而非社交事件。这赋予了它一个简洁的身份体系：网络身份就是加密密钥，而非 IP 分配或证书链。

传输无关的设计同样重要。相同的路由和身份模型原则上可以运行在 UDP、以太网、蓝牙或 LoRa 之上，这使得 FIPS 在对抗性或不可靠的网络环境中很有价值。

## 实现状态

正如 Compass 所报道的，当前的 Rust 实现已经包含可工作的 UDP 传输和基于布隆过滤器的发现。基于中继的引导仍是未来工作，因此目前该协议更多是一个网络底层基础设施，而非完善的 Nostr 中继替代方案。

---

**主要来源：**
- [FIPS 仓库](https://github.com/jmcorgan/fips)
- [设计文档](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)

**提及于：**
- [第11期周刊：FIPS 新闻](/zh/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)
- [第12期周刊](/zh/newsletters/2026-03-04-newsletter/)

**另请参阅：**
- [Marmot 协议](/zh/topics/marmot/)
