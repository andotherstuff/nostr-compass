---
title: "NIP-04：加密私信（已弃用）"
date: 2025-12-31
draft: false
translationOf: /en/topics/nip-04.md
translationDate: 2026-03-07
categories:
  - Privacy
  - Messaging
---

NIP-04 使用 kind 4 事件和 ECDH 派生的共享密钥定义加密私信。它是 Nostr 最初的私信方案，但现在已是遗留技术，新的隐私消息工作已转移到 NIP-17。

## 工作原理

消息使用 kind 4 事件，基本流程如下：

1. 发送方通过 secp256k1 ECDH 派生共享密钥。
2. 明文使用 AES-256-CBC 加密。
3. 事件包含一个指定接收方的 `p` 标签。
4. 密文经 base64 编码后与 IV 一起存储在 `content` 中。

事件本身仍然是普通的签名 Nostr 事件，因此中继器可以看到外部元数据，但无法读取明文。

## 安全与隐私限制

NIP-04 存在显著的隐私缺陷：

- **元数据泄露** - 发送方的 pubkey 在每条消息中公开可见
- **无发送方隐私** - 任何人都可以看到谁在给谁发消息
- **精确时间戳** - 消息时间未做随机化处理
- **非标准密钥处理** - 该方案仅使用 ECDH 点的 X 坐标，这使得跨库的正确性更难保证，并且几乎没有协议演进的空间

规范明确警告它"距离加密通信的最新技术水平还很远"。

## 为何被替代

NIP-04 加密了消息内容，但没有隐藏社交图谱。中继器运营者仍然可以看到谁发送了事件、谁接收它以及何时发布。即使不解密载荷，这些元数据也足以映射出对话关系。

NIP-17 通过将 NIP-44 载荷加密与 NIP-59 Gift Wrap 相结合来解决这个问题，从而对中继器和随机观察者隐藏发送方。新的实现应将 NIP-04 视为仅用于兼容性。

## 实现状态

遗留客户端和签名器仍然暴露 NIP-04 加解密方法，因为旧对话和较老的应用仍在流通中。这个兼容层对迁移很重要，但在 kind 4 事件之上构建新功能通常意味着继续承受旧的隐私限制。

---

**主要来源：**
- [NIP-04 规范](https://github.com/nostr-protocol/nips/blob/master/04.md)

**提及于：**
- [第4期周刊：NIP 深度解析](/zh/newsletters/2026-01-07-newsletter/#nip-04-encrypted-direct-messages-legacy)
- [第3期周刊：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**另请参阅：**
- [NIP-44：加密载荷](/zh/topics/nip-44/)
- [NIP-17：私密私信](/zh/topics/nip-17/)
- [NIP-59：Gift Wrap](/zh/topics/nip-59/)
