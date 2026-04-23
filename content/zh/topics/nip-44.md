---
title: "NIP-44：加密载荷"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - Cryptography
  - Privacy
---

NIP-44 定义了 Nostr 载荷的版本化加密标准，用现代密码学原语替换存在缺陷的 NIP-04 加密方案。

## 工作原理

NIP-44 version 2 采用多步加密流程：

1. **Key Agreement**：发送者与接收者的公钥通过 ECDH（secp256k1）生成共享密钥
2. **Key Derivation**：使用 SHA256 和盐值 `nip44-v2` 做 HKDF-extract，生成会话密钥
3. **Per-Message Keys**：基于随机 nonce，通过 HKDF-expand 派生 ChaCha key、nonce 和 HMAC key
4. **Padding**：对内容进行填充，隐藏消息长度
5. **Encryption**：使用 ChaCha20 加密填充后的内容
6. **Authentication**：使用 HMAC-SHA256 提供完整性校验

输出是一个带版本的 base64 payload，放在普通已签名 Nostr event 的内部。规范要求客户端在解密内部 NIP-44 payload 之前，先验证外层 NIP-01 event 的签名。

## 密码学选择

- **ChaCha20** 而不是 AES：更快，也更抗多密钥攻击
- **HMAC-SHA256** 而不是 Poly1305：多项式 MAC 更容易伪造
- **SHA256**：与现有 Nostr 原语保持一致
- **版本化格式**：便于未来升级算法

## 安全属性

- **已认证加密**：消息不能被静默篡改
- **长度隐藏**：padding 会掩盖消息尺寸
- **会话密钥**：同一会话共用密钥，降低持续通信中的计算开销
- **经过审计**：Cure53 安全审计未发现可利用漏洞

## 实现说明

NIP-44 不是对 NIP-04 payload 的直接替换。它定义的是一种加密格式，而不是私信 event kind。像 [NIP-17](/zh/topics/nip-17/) 和 [NIP-59](/zh/topics/nip-59/) 这样的协议，才定义了这种加密 payload 在实际消息流程中如何使用。

明文输入必须是 UTF-8 文本，长度在 1 到 65535 字节之间。这对实现者是个实打实的限制：如果你的应用需要加密任意二进制 blob，就必须额外做编码，或使用不同的容器格式。

## 限制

NIP-44 不提供：
- **前向保密**：密钥泄露后，历史消息会暴露
- **事后恢复安全**：密钥被攻破后缺乏自动恢复机制
- **可否认性**：消息仍然可以被证明由特定 keys 签署
- **元数据隐藏**：relay 架构本身仍限制隐私上限

对于高安全需求，NIP-104（double ratchet）或基于 MLS 的 Marmot 协议能提供更强保证。

## 历史

NIP-44 revision 3 于 2023 年 12 月在独立的 Cure53 安全审计之后合并。它构成了 NIP-17 私密私信和 NIP-59 gift wrapping 的密码学基础。

---

**主要来源：**
- [NIP-44 Specification](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44 Reference Implementations](https://github.com/paulmillr/nip44)
- [Cure53 Audit Report](https://cure53.de/audit-report_nip44-implementations.pdf)

**提及于：**
- [Newsletter #4：NIP 深度解析](/zh/newsletters/2026-01-07-newsletter/)
- [Newsletter #3：December 2023](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #3：December 2024](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #12：Marmot](/zh/newsletters/2026-03-04-newsletter/)
- [Newsletter #13：Vector](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19：nostter 的 NIP-44 迁移](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19：nowhere 对 Nostr 流量加密](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-04：加密私信（已弃用）](/zh/topics/nip-04/)
- [NIP-17：私密私信](/zh/topics/nip-17/)
- [NIP-59：Gift Wrap](/zh/topics/nip-59/)
- [NIP-104：Double Ratchet Encryption](/zh/topics/nip-104/)
- [MLS：Message Layer Security](/zh/topics/mls/)
