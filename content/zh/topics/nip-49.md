---
title: "NIP-49：私钥加密"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - 密钥管理
  - 安全
---

NIP-49 定义了客户端如何用密码加密用户的私钥，并将结果编码为 `ncryptsec` 字符串。它的目标是在比原始 `nsec` 存储更安全的默认设置下保持可移植性，同时仍让加密后的密钥易于在不同客户端之间迁移。

## 工作原理

客户端从原始的 32 字节 secp256k1 私钥开始，而不是 hex 或 bech32 字符串。它使用 scrypt 从用户密码派生一个临时对称密钥，配合每个密钥独立的随机 salt 和记录在 `LOG_N` 中的可调工作因子。随后，它使用 XChaCha20-Poly1305 加密私钥，在前面附加版本和密钥处理元数据，并最终以 `ncryptsec` 前缀进行 bech32 编码。

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

上面的 event 只是一个容器示例，并不是 NIP-49 的硬性要求。NIP-49 规范化的是加密密钥格式本身，而不是专门用于发布它的某个 event kind。客户端可以在本地保存 `ncryptsec`，通过应用专用存储同步，或将其作为备份导出字符串展示给用户。

## 安全模型

NIP-49 同时做了两件事：它把用户密码变成合格的加密密钥，并用内存硬型 KDF 提高暴力恢复的成本。工作因子在这里非常关键。更高的 `LOG_N` 值会让合法用户解密更慢，但也会显著提高攻击者进行离线猜测的成本。

该格式还携带一个一字节标志，用于描述该密钥在加密前是否曾以不安全方式处理过。这不会改变密文本身，但它为客户端提供了一种方法，用来区分一个全新生成、受保护的备份，与一个在包装之前就已经以明文形式被复制粘贴过的密钥。

## 实现说明

- 密码在派生密钥之前会先归一化为 Unicode NFKC，以保证同一密码在不同客户端中的输入结果一致。
- XChaCha20-Poly1305 使用 24 字节 nonce 和认证加密，因此任何对密文的篡改都会在解密时被明确检测出来。
- 对称密钥在使用后应被清零并丢弃。
- 规范不建议把加密密钥发布到公共 relay，因为收集越多加密密钥，攻击者进行离线破解时的条件就越有利。

## 实现

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - 为注册流程增加基于 NIP-49 加密私钥的兼容支持

---

**主要来源：**
- [NIP-49 规范](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - 使用 NIP-49 的客户端侧注册流程

**提及于：**
- [Newsletter #13：Formstr](/zh/newsletters/2026-03-11-newsletter/#formstr)
- [Newsletter #13：NIP 深度解析](/zh/newsletters/2026-03-11-newsletter/#nip-深度解析nip-49私钥加密)

**另请参阅：**
- [NIP-46：Nostr Connect](/zh/topics/nip-46/)
- [NIP-55：Android 签名器应用](/zh/topics/nip-55/)
