---
title: "NIP-55：Android 签名器应用"
date: 2025-12-17
translationOf: /en/topics/nip-55.md
translationDate: 2026-03-07
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55 定义了 Android 应用如何从单独的签名器应用请求签名和加密操作。它为 Android 客户端提供了浏览器扩展和远程 bunker 之外的原生替代方案。

## 工作原理

NIP-55 使用两种 Android 机制：

- **Intent** 用于前台流程，需要用户明确批准
- **Content resolver** 用于后台流程，在用户授予持久权限之后使用

常规连接流程从 `get_public_key` 开始。签名器返回用户公钥和签名器包名，客户端应缓存两者。在后台循环中重复调用 `get_public_key` 是规范明确警告的常见实现错误。

## 关键操作

- **get_public_key** - 检索用户的公钥和签名器包名
- **sign_event** - 签署 Nostr 事件
- **nip04_encrypt/decrypt** - 加密或解密 NIP-04 消息
- **nip44_encrypt/decrypt** - 加密或解密 NIP-44 消息
- **decrypt_zap_event** - 解密 zap 相关事件载荷

## 安全与用户体验说明

NIP-55 将密钥保留在设备上，但仍依赖于 Android 应用边界和签名器权限处理。Content resolver 支持比重复的 intent 提示提供更流畅的用户体验，但前提是用户已向该客户端授予持久批准。

对于 Android 上的 Web 应用，NIP-55 不如 NIP-46 方便。基于浏览器的流程无法像原生 Android 应用那样接收直接的后台响应，因此许多实现会退回到回调 URL、剪贴板传输或手动粘贴。

---

**主要来源：**
- [NIP-55 规范](https://github.com/nostr-protocol/nips/blob/master/55.md)

**提及于：**
- [第1期周刊：版本发布](/zh/newsletters/2025-12-17-newsletter/#releases)
- [第2期周刊：新闻动态](/zh/newsletters/2025-12-24-newsletter/#news)
- [第2期周刊：NIP 更新](/zh/newsletters/2025-12-24-newsletter/#nip-updates)
- [第3期周刊：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [第7期周刊：NIP 更新](/zh/newsletters/2026-01-07-newsletter/#nip-updates)
- [第11期周刊：NIP 深度解析](/zh/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-55-android-signer-application)

**另请参阅：**
- [NIP-46：Nostr Connect](/zh/topics/nip-46/)
