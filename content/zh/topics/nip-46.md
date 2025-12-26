---
title: "NIP-46：Nostr Connect"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46 定义了远程签名，允许签名器应用程序持有密钥，而客户端通过 Nostr 中继请求签名。

## 工作原理

1. 签名器生成连接 URI（`bunker://` 或 `nostrconnect://`）
2. 用户将 URI 粘贴到客户端中
3. 客户端将签名请求作为加密事件发送到签名器的中继
4. 签名器提示用户批准，返回签名后的事件

## 连接方法

- **bunker://** - 签名器发起的连接
- **nostrconnect://** - 客户端通过二维码或深度链接发起的连接

## 支持的操作

- `sign_event` - 签署任意事件
- `get_public_key` - 检索签名器的公钥
- `nip04_encrypt/decrypt` - NIP-04 加密操作
- `nip44_encrypt/decrypt` - NIP-44 加密操作

---

**主要来源：**
- [NIP-46 规范](https://github.com/nostr-protocol/nips/blob/master/46.md)

**提及于：**
- [第1期周刊：重要代码变更](/zh/newsletters/2025-12-17-newsletter/#amethystandroid)

**另请参阅：**
- [NIP-55：Android 签名器](/zh/topics/nip-55/)

