---
title: "NIP-07：浏览器扩展签名器"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07 定义了浏览器扩展为基于 Web 的 Nostr 客户端提供签名功能的标准接口，将私钥安全地保存在扩展中，而不是暴露给网站。

## 工作原理

浏览器扩展注入一个 `window.nostr` 对象，供 Web 应用使用：

```javascript
// 获取公钥
const pubkey = await window.nostr.getPublicKey();

// 签名事件
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// 加密 (NIP-04, 旧版)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// 解密 (NIP-04, 旧版)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// NIP-44 方法 (现代版, 如果支持)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## 安全模型

- **密钥隔离**：私钥永远不会离开扩展
- **用户批准**：扩展可以提示每个签名请求
- **域名控制**：扩展可以限制哪些网站可以请求签名

## 实现

流行的 NIP-07 扩展包括：
- **Alby** - 带有 Nostr 签名的 Lightning 钱包
- **nos2x** - 轻量级 Nostr 签名器
- **Flamingo** - 功能丰富的 Nostr 扩展

## 限制

- 仅限浏览器（不支持移动端）
- 需要安装扩展
- 每个扩展的批准体验不同

## 替代方案

- [NIP-46](/zh/topics/nip-46/) - 通过 Nostr 中继的远程签名
- [NIP-55](/zh/topics/nip-55/) - Android 本地签名器

## 相关

- [NIP-44](/zh/topics/nip-44/) - 现代加密（替代 NIP-04）
- [NIP-46](/zh/topics/nip-46/) - 远程签名
