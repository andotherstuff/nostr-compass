---
title: "NIP-04: 加密直接消息（已弃用）"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2025-12-31
draft: false
categories:
  - 隐私
  - 消息传递
---

NIP-04定义了使用AES-256-CBC加密的加密直接消息。它是Nostr上私密消息的原始方法，但由于存在重大隐私限制，已被NIP-17取代并弃用。

## 工作原理

消息使用kind 4事件，采用以下加密方案：
1. 使用接收者的公钥和发送者的私钥通过ECDH生成共享密钥
2. 使用AES-256-CBC加密消息
3. 密文使用base64编码并附加初始化向量
4. `p`标签标识接收者的公钥

## 安全限制

NIP-04存在重大隐私缺陷：

- **元数据泄露** - 发送者的pubkey在每条消息中都公开可见
- **无发送者隐私** - 任何人都可以看到谁在给谁发消息
- **精确时间戳** - 消息时间未进行随机化处理
- **非标准实现** - 仅使用ECDH点的X坐标而非标准SHA256哈希

规范明确警告它"远未达到加密通信的最先进水平"。

## 弃用状态

NIP-04已被NIP-17取代并弃用，NIP-17使用NIP-59 gift wrapping来隐藏发送者身份。新的实现应使用NIP-17进行私密消息传递。

---

**主要来源:**
- [NIP-04规范](https://github.com/nostr-protocol/nips/blob/master/04.md)

**相关提及:**
- [Newsletter #3: 12月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**另请参阅:**
- [NIP-17: 私密直接消息](/zh/topics/nip-17/)
- [NIP-59: Gift Wrap](/zh/topics/nip-59/)
