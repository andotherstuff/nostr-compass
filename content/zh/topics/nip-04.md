---
title: "NIP-04：加密私信（已弃用）"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-04 定义了使用 kind 4 events 和基于 ECDH 派生共享密钥的加密私信。它是 Nostr 最早的 DM 方案，但现在已经属于遗留技术，新的私密消息工作已转向 NIP-17。

## 工作原理

消息使用 kind 4 events，基本流程如下：

1. 发送方通过 secp256k1 ECDH 派生共享密钥。
2. 使用 AES-256-CBC 加密明文。
3. event 通过 `p` tag 标明接收者。
4. 密文会与 IV 一起编码为 base64，并存放在 `content` 中。

event 本身仍然是普通的、已签名的 Nostr event，因此 relays 虽然无法读取明文，但仍能看到外层元数据。

## 安全与隐私限制

NIP-04 存在明显的隐私缺陷：

- **元数据泄露**：每条消息都公开发送者 pubkey
- **没有发送者隐私**：任何人都能看出谁在给谁发消息
- **精确时间戳**：消息时间不会被随机化
- **非标准密钥处理**：该方案只使用 ECDH 点的 X 坐标，这让跨库正确性更难保证，也几乎不给协议演进留下空间

规范本身就明确警告，它“离加密通信的最先进水平还很远”。

## 为什么被替换

NIP-04 能加密消息内容，但无法隐藏社交图谱。relay 运营者依然可以看出是谁发了 event、谁接收，以及它在何时发布。即便无法解密 payload，这些元数据也足以勾勒出对话关系。

NIP-17 通过把 NIP-44 payload 加密与 NIP-59 gift wrapping 结合起来解决了这一点，它能把发送者从 relays 和随意观察者面前隐藏起来。新的实现应当只把 NIP-04 当作兼容层。

## 实现状态

遗留客户端和 signer 仍然会暴露 NIP-04 的 encrypt/decrypt 方法，因为旧对话和老应用依然在网络中流通。这个兼容层对迁移仍然重要，但如果继续在 kind 4 events 上构建新功能，就等于把旧有的隐私限制继续带进未来。

---

**主要来源：**
- [NIP-04 规范](https://github.com/nostr-protocol/nips/blob/master/04.md)

**提及于：**
- [Newsletter #4：NIP 深度解析](/zh/newsletters/2026-01-07-newsletter/)
- [Newsletter #3：December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #19：nostter 的 NIP-44 迁移](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-44：加密载荷](/zh/topics/nip-44/)
- [NIP-17：私密私信](/zh/topics/nip-17/)
- [NIP-59：Gift Wrap](/zh/topics/nip-59/)
