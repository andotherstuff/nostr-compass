---
title: "NIP-01：基础协议"
date: 2025-12-17
translationOf: /en/topics/nip-01.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
---

NIP-01 定义了 Nostr 其余部分赖以建立的基础 event 模型和 relay 协议。任何客户端、relay 或库只要在说 Nostr，起点都在这里。

## 工作原理

events 是 Nostr 中唯一的对象类型。profiles、notes、reactions、relay lists，以及许多应用特定的 payload，都使用同一个七字段信封：

- **id**：序列化 event 的 SHA256 哈希（唯一标识符）
- **pubkey**：创建者公钥（32-byte hex，secp256k1）
- **created_at**：Unix 时间戳
- **kind**：对 event 类型进行分类的整数
- **tags**：承载元数据的数组的数组
- **content**：payload（如何解释取决于 kind）
- **sig**：证明真实性的 Schnorr 签名

event `id` 是序列化 event 数据的 SHA256 哈希，而不是任意标识符。这在实践中很重要：改动任何字段，包括 tag 顺序或时间戳，都会生成不同的 event，并要求新的签名。

## Kinds

Kinds 决定 relay 如何存储和处理 events：

- **常规事件**（1、2、4-44、1000-9999）：正常存储，保留所有版本
- **可替换事件**（0、3、10000-19999）：每个 pubkey 只保留最新版本
- **临时事件**（20000-29999）：不存储，只转发给订阅者
- **可寻址事件**（30000-39999）：每个 pubkey + kind + `d` tag 组合保留最新版本

核心 kinds 包括 0（用户元数据）、1（文本笔记）和 3（关注列表）。

## 客户端与 relay 通信

客户端通过 WebSocket 连接，使用 JSON 数组与 relays 通信：

**客户端到 relay：**
- `["EVENT", <event>]` - 发布 event
- `["REQ", <sub-id>, <filter>, ...]` - 订阅 events
- `["CLOSE", <sub-id>]` - 结束订阅

**relay 到客户端：**
- `["EVENT", <sub-id>, <event>]` - 传递匹配的 event
- `["EOSE", <sub-id>]` - 已存储 events 结束，接下来进入实时流
- `["OK", <event-id>, <true|false>, <message>]` - 接受/拒绝确认
- `["NOTICE", <message>]` - 人类可读的消息

在实践中，大多数更高层的 NIP 并不会改变传输层。它们会定义新的 event kinds、tags 或解释规则，但仍继续使用 NIP-01 的 `EVENT`、`REQ` 和 `CLOSE` 消息。

## Filters

filters 指定要检索哪些 events，字段包括 `ids`、`authors`、`kinds`、`#e`/`#p`/`#t`、`since`、`until` 和 `limit`。单个 filter 内部使用 AND 逻辑，而同一个 `REQ` 中的多个 filters 之间使用 OR 逻辑。

## 互操作说明

有两个细节会造成很多实现 bug。第一，客户端应把 relay 响应视为最终一致，而不是全局有序，因为不同 relays 可能返回不同的历史子集。第二，可替换和可寻址 events 意味着“最新”本身就是协议模型的一部分，因此当多个 relays 给出不同答案时，客户端需要用确定性规则挑出最新的有效 event。

---

**主要来源：**
- [NIP-01 规范](https://github.com/nostr-protocol/nips/blob/master/01.md)

**提及于：**
- [第1期周刊：NIP 深度解析](/zh/newsletters/2025-12-17-newsletter/)
- [Newsletter #19：NIP-67 EOSE 完整性提示提案](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-19：Bech32 编码实体](/zh/topics/nip-19/)
- [Kind 注册表](/en/kind-registry/)
