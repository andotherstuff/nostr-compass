---
title: "NIP-44: Encrypted Payloads"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2025-12-31
draft: false
categories:
  - NIP
  - 密码学
  - 隐私
---

NIP-44定义了Nostr有效载荷的版本化加密标准，用现代加密原语替代有缺陷的NIP-04加密方案。

## 工作原理

NIP-44版本2使用多步骤加密过程：

1. **密钥协商**：发送者和接收者公钥之间的ECDH（secp256k1）产生共享密钥
2. **密钥派生**：使用SHA256和盐值`nip44-v2`的HKDF-extract创建对话密钥
3. **消息密钥**：HKDF-expand从随机nonce派生ChaCha密钥、nonce和HMAC密钥
4. **填充**：对内容进行填充以隐藏消息长度
5. **加密**：ChaCha20加密填充后的内容
6. **认证**：HMAC-SHA256提供消息完整性

## 加密选择

- **ChaCha20**优于AES：更快，多密钥攻击抵抗力更强
- **HMAC-SHA256**优于Poly1305：多项式MAC更容易伪造
- **SHA256**：与现有Nostr原语一致
- **版本化格式**：允许未来算法升级

## 安全属性

- **认证加密**：消息无法被篡改
- **长度隐藏**：填充模糊消息大小
- **对话密钥**：持续对话使用相同密钥减少计算
- **已审计**：Cure53安全审计未发现可利用的漏洞

## 限制

NIP-44不提供：
- **Forward Secrecy**：泄露的密钥暴露过去的消息
- **Post-Compromise Security**：密钥泄露后的恢复
- **可否认性**：消息可证明由特定密钥签名
- **元数据隐藏**：中继架构限制隐私

对于高安全需求，NIP-104（Double Ratchet）或基于MLS的协议（如Marmot）提供更强的保证。

## 历史

NIP-44修订版3在Cure53独立安全审计后于2023年12月合并。它构成了NIP-17私信和NIP-59 gift wrapping的加密基础。

---

**主要来源：**
- [NIP-44规范](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44参考实现](https://github.com/paulmillr/nip44)
- [Cure53审计报告](https://cure53.de/audit-report_nip44-implementations.pdf)

**提及：**
- [通讯 #3：2023年12月](/zh/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [通讯 #3：2024年12月](/zh/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)

**另请参阅：**
- [NIP-04: 加密直接消息（已弃用）](/zh/topics/nip-04/)
- [NIP-17: 私密直接消息](/zh/topics/nip-17/)
- [NIP-59: 礼物包装](/zh/topics/nip-59/)
- [NIP-104: 双棘轮加密](/zh/topics/nip-104/)
- [MLS: 消息层安全](/zh/topics/mls/)
