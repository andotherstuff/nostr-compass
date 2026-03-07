---
title: "NIP-07：浏览器扩展签名器"
date: 2026-01-28
draft: false
translationOf: /en/topics/nip-07.md
translationDate: 2026-03-07
categories:
  - NIP
  - Signing
  - Security
---

NIP-07 定义了浏览器扩展为基于 Web 的 Nostr 客户端提供签名功能的标准接口，将私钥安全地保存在扩展中，而非暴露给网站。

## 工作原理

浏览器扩展注入一个 `window.nostr` 对象供 Web 应用使用：

```javascript
// 获取公钥
const pubkey = await window.nostr.getPublicKey();

// 签名事件
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// 加密（NIP-04，遗留方式）
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// 解密（NIP-04，遗留方式）
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// NIP-44 方法（现代方式，如果支持）
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## 安全模型

- **密钥隔离**：私钥永远不会离开扩展
- **用户审批**：扩展可以为每次签名请求弹出提示
- **域名控制**：扩展可以限制哪些站点可以请求签名

NIP-07 改善了密钥托管，但并未消除对扩展本身的信任。恶意或被入侵的扩展仍然可以签署错误的内容、泄露元数据或过于宽泛地授予权限。

## 互操作说明

NIP-07 最困难的部分不是 API 形状，而是能力差异。某些扩展仅支持 `getPublicKey()` 和 `signEvent()`。其他扩展还暴露了 `nip04`、`nip44` 或更新的可选方法。Web 应用需要功能检测和合理的回退方案，而不是假设每个注入的签名器行为都相同。

用户审批的用户体验也会影响行为。一个静默期望后台访问的站点可能在某个扩展上正常工作，而在每次请求都弹出提示的另一个扩展上感觉不可用。良好的 NIP-07 应用将签名视为交互式权限边界。

## 实现状态

流行的 NIP-07 扩展包括：
- **Alby** - 带有 Nostr 签名功能的闪电网络钱包
- **nos2x** - 轻量级 Nostr 签名器
- **Flamingo** - 功能丰富的 Nostr 扩展

## 局限性

- 仅限浏览器（不支持移动端）
- 需要安装扩展
- 每个扩展的审批用户体验不同

对于跨设备或移动端签名，NIP-46 和 NIP-55 通常更合适。

---

**主要来源：**
- [NIP-07 规范](https://github.com/nostr-protocol/nips/blob/master/07.md)
- [PR #2233](https://github.com/nostr-protocol/nips/pull/2233) - `peekPublicKey()` 提案

**提及于：**
- [第7期周刊：NIP 更新](/zh/newsletters/2026-01-28-newsletter/#nip-updates)
- [第8期周刊：动态](/zh/newsletters/2026-02-04-newsletter/#news)
- [第11期周刊：动态](/zh/newsletters/2026-02-25-newsletter/#news)

**另请参阅：**
- [NIP-04：加密私信（已弃用）](/zh/topics/nip-04/)
- [NIP-44：加密载荷](/zh/topics/nip-44/)
- [NIP-46：Nostr Connect](/zh/topics/nip-46/)
- [NIP-55：Android 签名器应用](/zh/topics/nip-55/)
