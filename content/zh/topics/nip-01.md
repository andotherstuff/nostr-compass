---
title: "NIP-01：基础协议"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-01 定义了 Nostr 的基础协议，建立了所有其他 NIP 所依赖的数据结构和通信模式。

## 事件

事件是 Nostr 中唯一的对象类型。每一条数据，从个人资料更新到文本帖子再到反应，都表示为具有以下结构的事件：

- **id**：序列化事件的 SHA256 哈希（唯一标识符）
- **pubkey**：创建者的公钥（32 字节十六进制，secp256k1）
- **created_at**：Unix 时间戳
- **kind**：整数，表示事件类型
- **tags**：数组的数组，用于元数据
- **content**：载荷（解释取决于 kind）
- **sig**：Schnorr 签名，证明真实性

## Kinds

Kinds 决定中继如何存储和处理事件：

- **常规事件**（1, 2, 4-44, 1000-9999）：正常存储，保留所有版本
- **可替换事件**（0, 3, 10000-19999）：每个公钥仅保留最新版本
- **临时事件**（20000-29999）：不存储，仅转发给订阅者
- **可寻址事件**（30000-39999）：每个公钥 + kind + `d` 标签组合的最新版本

核心 kinds 包括：0（用户元数据）、1（文本笔记）、3（关注列表）。

## 客户端-中继通信

客户端通过 WebSocket 连接使用 JSON 数组与中继通信：

**客户端到中继：**
- `["EVENT", <event>]` - 发布事件
- `["REQ", <sub-id>, <filter>, ...]` - 订阅事件
- `["CLOSE", <sub-id>]` - 结束订阅

**中继到客户端：**
- `["EVENT", <sub-id>, <event>]` - 传递匹配的事件
- `["EOSE", <sub-id>]` - 存储事件结束（现在开始实时流式传输）
- `["OK", <event-id>, <true|false>, <message>]` - 接受/拒绝确认
- `["NOTICE", <message>]` - 人类可读消息

## 过滤器

过滤器指定要检索哪些事件，字段包括：`ids`、`authors`、`kinds`、`#e`/`#p`/`#t`（标签值）、`since`/`until` 和 `limit`。一个过滤器内的条件使用 AND 逻辑；`REQ` 中的多个过滤器使用 OR 逻辑组合。

---

**主要来源：**
- [NIP-01 规范](https://github.com/nostr-protocol/nips/blob/master/01.md)

**提及于：**
- [第1期周刊：NIP 深度解析](/zh/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-and-nip-19)

**另请参阅：**
- [NIP-19：Bech32 编码实体](/zh/topics/nip-19/)
- [Kind 注册表](/zh/kind-registry/)

