---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2025-12-31
draft: false
categories:
  - 密码学
  - 协议
  - 消息传递
  - 隐私
---

Message Layer Security (MLS) 是一个IETF标准化的端到端加密群组消息协议。它为从两人到数千人的群组提供具有前向保密性和入侵后安全性的高效密钥建立。

## 工作原理

MLS使用一种称为TreeKEM的基于树的密钥协商结构：

1. **密钥包**: 每个参与者发布包含其身份和加密密钥的密钥包
2. **群组状态**: 棘轮树维护群组的加密状态
3. **提交**: 成员在加入、离开或轮换密钥时更新树
4. **消息加密**: 内容使用从群组共享密钥派生的密钥进行加密

## 关键安全特性

- **前向保密性**: 即使当前密钥被泄露，过去的消息仍保持安全
- **入侵后安全性**: 密钥轮换后，未来的消息恢复安全
- **成员身份验证**: 所有群组成员都经过加密验证
- **异步操作**: 成员可以在不是所有参与者都在线的情况下加入/离开
- **可扩展性**: 对多达50,000名参与者的群组高效

## 标准化

- **RFC 9420**（2023年7月）：核心MLS协议规范
- **RFC 9750**（2025年4月）：系统集成的MLS架构

## Nostr中的采用

多个Nostr应用程序使用MLS进行安全群组消息传递：

- **KeyChat**: 面向移动端和桌面端的基于MLS的加密消息应用
- **White Noise**: 使用MLS并集成Marmot协议的私密消息传递
- **Marmot Protocol**: 提供基于MLS的群组加密的Nostr扩展

MLS提供比单独使用NIP-04或NIP-44更强的安全保证，特别是对于成员动态加入和离开的群聊。

## 行业采用

除Nostr外，MLS正被以下采用：
- Google Messages（通过GSMA Universal Profile 3.0使用MLS的RCS）
- Apple Messages（宣布支持MLS的RCS）
- Cisco WebEx、Wickr、Matrix

---

**主要来源:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**相关提及:**
- [Newsletter #3: 发布](/zh/newsletters/2025-12-31-newsletter/#releases)

**另请参阅:**
- [Marmot Protocol](/zh/topics/marmot/)
- [MIP-05: 隐私保护推送通知](/zh/topics/mip-05/)
- [NIP-17: 私密直接消息](/zh/topics/nip-17/)
- [NIP-44: 加密负载](/zh/topics/nip-44/)
