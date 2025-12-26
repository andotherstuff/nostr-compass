---
title: "MIP-05：隐私保护推送通知"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05 定义了一个保护用户隐私的推送通知协议，解决了传统推送系统需要服务器知道设备令牌和用户身份的问题。

## 工作原理

- 设备令牌使用 ECDH+HKDF 和 ChaCha20-Poly1305 加密
- 临时密钥防止通知之间的关联
- 三事件 gossip 协议（kinds 447-449）在群组成员之间同步加密令牌
- 通过 NIP-59 gift wrapping 的诱饵令牌隐藏群组大小

## 隐私保证

- 推送通知服务器无法识别用户
- 通知模式不会泄露群组成员资格
- 设备令牌无法跨消息关联

## 事件 Kinds

- **Kind 447**：加密设备令牌发布
- **Kind 448**：令牌同步请求
- **Kind 449**：令牌同步响应

---

**主要来源：**
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)

**提及于：**
- [第1期周刊：新闻动态](/zh/newsletters/2025-12-17-newsletter/#news)

**另请参阅：**
- [Marmot 协议](/zh/topics/marmot/)
- [NIP-59：Gift Wrap](/zh/topics/nip-59/)

