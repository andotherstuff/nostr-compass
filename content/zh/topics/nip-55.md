---
title: "NIP-55：Android 签名器应用"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55 定义了 Android 应用程序如何从专用签名器应用请求签名操作，允许用户将私钥保存在一个安全位置，同时使用多个 Nostr 客户端。

## 工作原理

NIP-55 使用 Android 的 content provider 接口来暴露签名操作。签名器应用注册为 content provider，其他 Nostr 应用可以在不直接访问私钥的情况下请求签名。

流程：
1. 客户端应用调用签名器的 content provider
2. 签名器向用户显示批准 UI
3. 用户批准或拒绝请求
4. 签名器将签名（或拒绝）返回给客户端

## 关键操作

- **get_public_key** - 检索用户的公钥（初始连接时调用一次）
- **sign_event** - 签署 Nostr 事件
- **nip04_encrypt/decrypt** - 加密或解密 NIP-04 消息
- **nip44_encrypt/decrypt** - 加密或解密 NIP-44 消息

## 连接初始化

一个常见的实现错误是从后台进程重复调用 `get_public_key`。规范建议仅在初始连接设置时调用一次，然后缓存结果。

---

**主要来源：**
- [NIP-55 规范](https://github.com/nostr-protocol/nips/blob/master/55.md)

**提及于：**
- [第1期周刊：版本发布](/zh/newsletters/2025-12-17-newsletter/#releases)
- [第2期周刊：新闻动态](/zh/newsletters/2025-12-24-newsletter/#news)
- [第2期周刊：NIP 更新](/zh/newsletters/2025-12-24-newsletter/#nip-updates)

**另请参阅：**
- [NIP-46：Nostr Connect](/zh/topics/nip-46/)

