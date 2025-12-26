---
title: "NIP-BE：蓝牙低功耗"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Connectivity
---

NIP-BE 规定了 Nostr 应用程序如何通过蓝牙低功耗进行通信和同步，使离线应用能够在没有互联网连接的情况下跨附近设备同步数据。

## GATT 结构

使用 Nordic UART 服务，包含两个特征：
- **写入特征** - 客户端向服务器发送数据
- **读取特征** - 服务器向客户端发送数据（通过通知）

## 消息分帧

BLE 有较小的载荷限制（根据版本为 20-256 字节），因此消息：
- 使用 DEFLATE 压缩
- 分割成带有 2 字节索引和最终批次标志的块
- 最大大小限制为 64KB

## 角色协商

设备在发现时比较广播的 UUID：
- UUID 较高的成为 GATT 服务器（中继角色）
- UUID 较低的成为 GATT 客户端
- 存在预定义的 UUID 用于单角色设备

## 同步

使用半双工通信和标准 Nostr 消息类型（`EVENT`、`EOSE`、`NEG-MSG`）来协调间歇性连接中的数据同步。

## 使用场景

- 附近设备之间的离线事件同步
- 无需互联网的网状式消息传播
- 网络不可用时的备用连接

---

**主要来源：**
- [NIP-BE 规范](https://github.com/nostr-protocol/nips/blob/master/BE.md)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)

