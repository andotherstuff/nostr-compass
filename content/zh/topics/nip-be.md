---
title: "NIP-BE：低功耗蓝牙"
date: 2025-12-17
draft: false
translationOf: /en/topics/nip-be.md
translationDate: 2026-03-07
categories:
  - Protocol
  - Connectivity
---

NIP-BE 规定了 Nostr 应用如何通过低功耗蓝牙（BLE）进行通信和同步，使具备离线功能的应用能够在附近设备之间同步数据而无需互联网连接。

## 工作原理

NIP-BE 在 BLE 上复用标准 Nostr 消息帧，而非发明单独的事件模型。设备广播 BLE 服务加设备 UUID，相遇时比较 UUID，并确定性地决定哪一方成为 GATT 服务器、哪一方成为 GATT 客户端。

GATT 服务使用类似 Nordic UART 的结构，包含一个写特征和一个读/通知特征。这使传输保持足够简单，适用于受限的移动端协议栈，同时仍能承载普通的 Nostr 消息。

## 消息分帧

BLE 的载荷限制较小，因此 NIP-BE 使用 DEFLATE 压缩消息，将其拆分为带索引的块，并一次只发送一条消息。规范将消息上限设为 64 KB，这提醒人们该传输方式适用于同步和本地传播，而非批量传输。

## 同步模型

建立连接后，对等节点使用基于 [NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md) negentropy 消息的半双工同步流程，包括 `NEG-OPEN`、`NEG-MSG`、`EVENT` 和 `EOSE`。这一设计选择很重要，因为它让实现可以复用现有的中继同步逻辑，而非构建仅限 BLE 的复制算法。

半双工规则也反映了不稳定 BLE 链路的现实。间歇性的短距离连接在每一方都清楚轮到谁发言时运行得更好。

## 重要意义

NIP-BE 为 Nostr 应用提供了本地优先网络的路径。两部手机可以在彼此靠近时直接同步笔记或中继状态，即使两者都没有可用的互联网。这使得 BLE 对于抗审查、灾难场景和低连接社交应用非常有用。

约束同样重要：BLE 带宽低，连接短暂，大量历史记录不适合传输。在实践中，NIP-BE 最适合增量同步和近距离消息传播，而非完整的存档复制。

---

**主要来源：**
- [NIP-BE 规范](https://github.com/nostr-protocol/nips/blob/master/BE.md)
- [PR #1979](https://github.com/nostr-protocol/nips/pull/1979)

**提及于：**
- [Newsletter #1：新闻](/zh/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**另请参阅：**
- [NIP-01：基础协议](/zh/topics/nip-01/)
