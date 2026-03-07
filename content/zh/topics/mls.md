---
title: "MLS（消息层安全）"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2026-03-07
draft: false
categories:
  - Cryptography
  - Protocol
  - Messaging
  - Privacy
---

Message Layer Security（MLS）是一个用于端到端加密群组消息的 IETF 协议。它为可能随时间变更成员的群组提供前向保密和泄露后安全。

## 工作原理

MLS 使用一种称为 TreeKEM 的基于树的密钥协商结构：

1. **密钥包**：每个参与者发布包含其身份和加密密钥的密钥包
2. **群组状态**：棘轮树维护群组的加密状态
3. **提交**：成员在加入、离开或轮换密钥时更新树
4. **消息加密**：内容使用从群组共享密钥派生的密钥进行加密

## 重要意义

MLS 解决了成对加密无法很好解决的问题：在成员异步加入、离开或轮换密钥时，保持群组成员资格和加密状态的一致性。

其树结构是关键的实用洞察。更新不需要每个参与者与所有其他人重新进行成对协商，因此该协议的扩展性远优于临时的群组密钥方案。

## 标准化

- **RFC 9420**（2023 年 7 月）：核心 MLS 协议规范
- **RFC 9750**（2025 年 4 月）：系统集成的 MLS 架构

## Nostr 中的采用

多个 Nostr 应用使用 MLS 进行安全群组消息传递：

- **KeyChat**：面向移动端和桌面端的基于 MLS 的加密消息应用
- **White Noise**：使用 MLS 并集成 Marmot 协议的私密消息传递
- **Marmot Protocol**：提供基于 MLS 的群组加密的 Nostr 扩展

MLS 提供了比单独使用 [NIP-04](/zh/topics/nip-04/) 或 [NIP-44](/zh/topics/nip-44/) 更强的群组安全保证，特别是在成员频繁变动时。

## 权衡

MLS 不是一个完整的消息产品。应用仍然需要围绕该协议处理身份、传输、垃圾信息防护、存储和冲突处理。

这就是 Marmot 等 Nostr 项目在 MLS 之上添加额外规则的原因。密码学已标准化，但周围的应用协议对互操作性仍然很重要。

---

**主要来源：**
- [RFC 9420：MLS 协议](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750：MLS 架构](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS 工作组](https://datatracker.ietf.org/wg/mls/about/)
- [MLS 协议网站](https://messaginglayersecurity.rocks/)

**提及于：**
- [第3期周刊：版本发布](/zh/newsletters/2025-12-31-newsletter/#releases)
- [第10期周刊](/zh/newsletters/2026-02-18-newsletter/)
- [第12期周刊](/zh/newsletters/2026-03-04-newsletter/)

**另请参阅：**
- [Marmot 协议](/zh/topics/marmot/)
- [MIP-05：隐私保护推送通知](/zh/topics/mip-05/)
- [NIP-17：私密直接消息](/zh/topics/nip-17/)
- [NIP-44：加密载荷](/zh/topics/nip-44/)
