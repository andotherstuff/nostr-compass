---
title: "NIP-49：私钥加密"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - 密钥管理
  - 安全
---

NIP-49 定义了客户端如何使用密码加密用户的私钥并将结果编码为 `ncryptsec` 字符串。其目标是提供比存储原始 `nsec` 更强默认安全性的可移植性，同时保持加密密钥在客户端之间易于迁移。

## 工作原理

客户端从原始的 32 字节 secp256k1 私钥开始，而非十六进制或 bech32 字符串。它使用 scrypt 从用户密码派生临时对称密钥，采用每个密钥随机的盐值和存储为 `LOG_N` 的可调工作因子。然后使用 XChaCha20-Poly1305 加密私钥，前置版本和密钥处理元数据，并以 `ncryptsec` 前缀进行 bech32 编码。

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

上面的 event 是一个示例容器，并非 NIP-49 要求。NIP-49 标准化的是加密密钥格式本身，而不是用于发布它的专用 event kind。客户端可以在本地存储 `ncryptsec`，通过应用特定存储同步，或将其作为备份导出呈现。

## 安全模型

NIP-49 同时做了两件事。它将用户密码转换为适当的加密密钥，并通过内存困难的 KDF 减缓暴力破解恢复尝试。工作因子很重要。更高的 `LOG_N` 值使合法用户的解密更慢，但也提高了攻击者离线猜测的成本。

该格式还携带一个单字节标志，描述密钥在加密前是否曾以不安全方式处理过。这不会改变密文本身，但它给客户端提供了一种方式来区分新生成的受保护备份和在被包装前已经以明文形式传播的密钥。

## 实现说明

- 密码在密钥派生前被规范化为 Unicode NFKC，以便在不同客户端之间一致地输入相同密码。
- XChaCha20-Poly1305 使用 24 字节随机数和认证加密，因此篡改密文在解密时会干净地失败。
- 对称密钥在使用后应被清零和丢弃。
- 规范不建议将加密密钥发布到公共 relay，因为收集大量加密密钥会改善攻击者的离线破解条件。

## 实现

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - 使用 NIP-49 加密私钥添加注册兼容性

---

**主要来源：**
- [NIP-49 规范](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - 使用 NIP-49 的客户端注册流程

**提及于：**
- [周刊 #13：Formstr](/en/newsletters/2026-03-11-newsletter/#formstr)
- [周刊 #13：NIP 深度解析](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49-private-key-encryption)

**另见：**
- [NIP-46：Nostr Connect](/zh/topics/nip-46/)
- [NIP-55：Android 签名器应用](/zh/topics/nip-55/)
