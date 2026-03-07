---
title: "MIP-05：隐私保护推送通知"
date: 2025-12-17
translationOf: /en/topics/mip-05.md
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05 为 Marmot 客户端定义了一个推送通知协议，试图在普通移动推送系统通常会暴露设备令牌和账户关系的环境中保护隐私。

## 工作原理

- 设备令牌使用 ECDH+HKDF 和 ChaCha20-Poly1305 加密
- 临时密钥防止通知之间的关联
- 三事件 gossip 协议（kinds 447-449）在群组成员之间同步加密令牌
- 通过 NIP-59 gift wrapping 的诱饵令牌隐藏群组大小

## 隐私模型

- 推送通知服务器无法识别用户
- 通知模式不会泄露群组成员资格
- 设备令牌无法跨消息关联

具体改进在于：推送提供商看到的是不透明的投递令牌，而非从群组成员到设备的直接映射。这并不能在绝对意义上使通知匿名，但它减少了推送层默认获取的信息量。

## 事件类型

- **Kind 447**：加密设备令牌发布
- **Kind 448**：令牌同步请求
- **Kind 449**：令牌同步响应

## 权衡

MIP-05 通过增加协调工作来增加隐私。客户端必须在群组成员之间同步加密令牌状态，而诱饵令牌有意增加了消息开销。

这意味着实现者需要在投递可靠性和元数据保护之间取得平衡。该协议之所以有用，正是因为它将推送视为隐私问题，而非仅仅是传输便利。

---

**主要来源：**
- [MIP-05 规范](https://github.com/marmot-protocol/marmot/blob/master/05.md)
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)
- [White Noise v0.2.1 版本](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)
- [第3期周刊：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**另请参阅：**
- [Marmot 协议](/zh/topics/marmot/)
- [NIP-59：Gift Wrap](/zh/topics/nip-59/)
