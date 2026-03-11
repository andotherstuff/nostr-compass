---
title: "NIP-44：加密载荷"
date: 2025-12-31
draft: false
translationOf: /en/topics/nip-44.md
translationDate: 2026-03-11
categories:
  - NIP
  - 密码学
  - 隐私
---

NIP-44 定义了 Nostr 载荷的版本化加密标准，用现代密码学原语替代了存在缺陷的 NIP-04 加密方案。

## 工作原理

NIP-44 第 2 版使用多步加密流程：

1. **密钥协商**：发送方和接收方公钥之间的 ECDH（secp256k1）生成共享密钥
2. **密钥派生**：使用 SHA256 和盐值 `nip44-v2` 进行 HKDF-extract，创建会话密钥
3. **消息密钥**：HKDF-expand 从随机 nonce 派生 ChaCha 密钥、nonce 和 HMAC 密钥
4. **填充**：对内容进行填充以隐藏消息长度
5. **加密**：ChaCha20 加密填充后的内容
6. **认证**：HMAC-SHA256 提供消息完整性

输出是一个版本化的 base64 载荷，放入普通的已签名 Nostr 事件中。规范要求客户端在解密内部 NIP-44 载荷之前，先验证外层的 NIP-01 事件签名。

## 密码学选择

- **ChaCha20** 优于 AES：更快，多密钥攻击抵抗力更强
- **HMAC-SHA256** 优于 Poly1305：多项式 MAC 更容易伪造
- **SHA256**：与现有的 Nostr 原语一致
- **版本化格式**：允许未来升级算法

## 安全属性

- **认证加密**：消息无法被篡改
- **长度隐藏**：填充掩盖消息大小
- **会话密钥**：持续对话使用相同密钥可减少计算开销
- **已审计**：Cure53 安全审计未发现可利用的漏洞

## 实现说明

NIP-44 并非 NIP-04 载荷的直接替代品。它定义的是加密格式，而非私信事件类型。[NIP-17](/zh/topics/nip-17/) 和 [NIP-59](/zh/topics/nip-59/) 等协议定义了加密载荷如何在实际消息流中使用。

明文输入是 UTF-8 文本，长度从 1 到 65535 字节。这对实现者是一个实际的约束：如果你的应用需要加密任意二进制数据，则需要额外的编码或不同的容器格式。

## 局限性

NIP-44 不提供：
- **前向保密**：密钥泄露会暴露过去的消息
- **泄露后安全**：密钥泄露后的恢复
- **可否认性**：消息可被证明由特定密钥签名
- **元数据隐藏**：中继架构限制了隐私性

对于高安全性需求，NIP-104（双棘轮）或基于 MLS 的协议（如 Marmot）提供更强的保证。

## 历史

NIP-44 修订版 3 在 2023 年 12 月经过独立的 Cure53 安全审计后合并。它构成了 NIP-17 私密消息和 NIP-59 gift wrapping 的密码学基础。

---

**主要来源：**
- [NIP-44 规范](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44 参考实现](https://github.com/paulmillr/nip44)
- [Cure53 审计报告](https://cure53.de/audit-report_nip44-implementations.pdf)

**提及于：**
- [Newsletter #4：NIP 深度解析](/zh/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Newsletter #3：2023 年 12 月](/zh/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [Newsletter #3：2024 年 12 月](/zh/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)
- [Newsletter #12：Marmot](/zh/newsletters/2026-03-04-newsletter/#marmot-development-kit-ships-first-public-release)

**另请参阅：**
- [NIP-04：加密私信（已弃用）](/zh/topics/nip-04/)
- [NIP-17：私密消息](/zh/topics/nip-17/)
- [NIP-59：Gift Wrap](/zh/topics/nip-59/)
- [NIP-104：双棘轮加密](/zh/topics/nip-104/)
- [MLS：消息层安全](/zh/topics/mls/)
