---
title: "NIP-55：Android Signer Application"
date: 2025-12-17
translationOf: /en/topics/nip-55.md
translationDate: 2026-04-22
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55 定义了 Android apps 如何向独立的 signer application 请求签名和加密操作。它为 Android 客户端提供了浏览器扩展和远程 bunker 之外的原生替代方案。

## 工作原理

NIP-55 使用两种 Android 机制：

- **Intents**：用于需要明确用户批准的前台流程
- **Content resolvers**：用于用户授予持久权限之后的后台流程

常见的连接流程从 `get_public_key` 开始。signer 会返回用户 pubkey 和 signer 的 package name，而客户端应缓存这两项信息。在后台循环中反复调用 `get_public_key` 是一种常见实现错误，规范明确对此提出了警告。

## 关键操作

- **get_public_key** - 获取用户 pubkey 和 signer package name
- **sign_event** - 为一个 Nostr event 签名
- **nip04_encrypt/decrypt** - 加密或解密 NIP-04 消息
- **nip44_encrypt/decrypt** - 加密或解密 NIP-44 消息
- **decrypt_zap_event** - 解密与 zap 相关的 event payload

## 安全与 UX 说明

NIP-55 把 keys 保留在设备端，但它仍然依赖 Android 的 app 边界和 signer 的权限处理。与反复弹出 intent 提示相比，content resolver 支持能带来顺畅得多的 UX，但前提是用户已经向该客户端授予了持久授权。

对于 Android 上的 web apps，NIP-55 不如 NIP-46 顺手。浏览器环境无法像原生 Android apps 那样接收直接的后台响应，因此许多实现会回退到 callback URL、剪贴板传递或手动粘贴等方式。

---

**主要来源：**
- [NIP-55 Specification](https://github.com/nostr-protocol/nips/blob/master/55.md)

**提及于：**
- [Newsletter #1：Releases](/zh/newsletters/2025-12-17-newsletter/)
- [Newsletter #2：News](/zh/newsletters/2025-12-24-newsletter/)
- [Newsletter #2：NIP Updates](/zh/newsletters/2025-12-24-newsletter/)
- [Newsletter #3：December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #4：NIP Updates](/zh/newsletters/2026-01-07-newsletter/)
- [Newsletter #11：NIP Deep Dive](/zh/newsletters/2026-02-25-newsletter/)
- [Newsletter #13：Samizdat v1.0.0-alpha](/en/newsletters/2026-03-11-newsletter/)

**另请参阅：**
- [NIP-46：Nostr Connect](/zh/topics/nip-46/)
