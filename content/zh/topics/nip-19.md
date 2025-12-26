---
title: "NIP-19：Bech32 编码实体"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-19 定义了用于分享 Nostr 标识符的人类友好格式。这些 bech32 编码的字符串用于显示和分享，但在协议本身中从不使用（协议使用十六进制）。

## 为什么使用 Bech32？

原始十六进制密钥容易复制出错且视觉上无法区分。Bech32 编码添加了人类可读的前缀和校验和，使您可以立即清楚地知道正在查看的是什么类型的数据。

## 基本格式

这些编码原始 32 字节值：

- **npub** - 公钥（您的身份，可安全分享）
- **nsec** - 私钥（保密，用于签名）
- **note** - 事件 ID（引用特定事件）

示例：十六进制公钥 `3bf0c63f...` 变为 `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`。

## 可分享标识符

这些使用 TLV（类型-长度-值）编码包含元数据：

- **nprofile** - 带有中继提示的个人资料（帮助客户端找到用户）
- **nevent** - 带有中继提示、作者公钥和 kind 的事件
- **naddr** - 可寻址事件引用（公钥 + kind + d 标签 + 中继）

这些解决了发现问题：当有人分享一个笔记 ID 时，客户端如何知道哪个中继有它？通过在标识符中捆绑中继提示，分享的链接变得更可靠。

## 实现说明

- 仅在人类界面使用 bech32：显示、复制/粘贴、二维码、URL
- 永远不要在协议消息、事件或 NIP-05 响应中使用 bech32 格式
- 所有协议通信必须使用十六进制编码
- 生成 nevent/nprofile/naddr 时，包含中继提示以获得更好的可发现性

---

**主要来源：**
- [NIP-19 规范](https://github.com/nostr-protocol/nips/blob/master/19.md)

**提及于：**
- [第1期周刊：NIP 深度解析](/zh/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)

**另请参阅：**
- [NIP-01：基础协议](/zh/topics/nip-01/)
- [NIP-21：nostr: URI 方案](https://github.com/nostr-protocol/nips/blob/master/21.md)

