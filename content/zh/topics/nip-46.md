---
title: "NIP-46：Nostr Connect"
date: 2025-12-17
translationOf: /en/topics/nip-46.md
translationDate: 2026-04-22
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46 定义了通过 Nostr relays 进行远程签名的方式。客户端与独立的 signer 通信，这个 signer 通常被称为 bunker，因此签名密钥可以留在用户当前正在使用的 app 之外。

## 工作原理

1. 客户端生成一个只用于 bunker 会话的本地 keypair。
2. 连接通过 `bunker://` 或 `nostrconnect://` URI 建立。
3. 客户端与 signer 通过 relays 交换加密的 kind `24133` 请求与响应 events。
4. 连接建立后，客户端调用 `get_public_key`，获取它实际在为哪个用户 pubkey 做签名。

## 连接方式

- **bunker://** - 由 signer 发起的连接
- **nostrconnect://** - 由客户端通过 QR code 或 deep link 发起的连接

`nostrconnect://` 流程包含一个必需的共享密钥，因此客户端可以验证第一条响应确实来自目标 signer。这可以防止简单的连接伪造。

## 支持的操作

- `sign_event` - 为任意 event 签名
- `get_public_key` - 从 signer 获取用户 pubkey
- `nip04_encrypt/decrypt` - NIP-04 加密与解密操作
- `nip44_encrypt/decrypt` - NIP-44 加密与解密操作
- `switch_relays` - 请求 signer 提供更新后的 relay 集合

许多实现还会在初始化时使用 `sign_event:1` 或 `nip44_encrypt` 这样的 permission strings，以便 signer 批准一个较窄的权限范围，而不是给出完全访问权限。

## Relay 与信任模型

NIP-46 把私钥移出客户端，但并没有把信任从 signer 身上移除。signer 仍然可以批准、拒绝或延迟请求，而且它能看到客户端要求它执行的每一个操作。relay 的选择也同样重要，因为该协议依赖请求和响应在双方都能到达的 relays 上传递。

`switch_relays` 方法的存在，是为了让 signer 能随着时间推移把会话迁移到另一组 relays。忽略它的客户端，在 signer 的 relay 偏好发生变化后，可靠性就会变差。

---

**主要来源：**
- [NIP-46 Specification](https://github.com/nostr-protocol/nips/blob/master/46.md)

**提及于：**
- [Newsletter #1：Notable Code Changes](/zh/newsletters/2025-12-17-newsletter/)
- [Newsletter #3：December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #4：Primal Android Becomes a Full Signing Hub](/zh/newsletters/2026-01-07-newsletter/)
- [Newsletter #12：NDK Collaborative Events and NIP-46 Timeout](/zh/newsletters/2026-03-04-newsletter/)
- [Newsletter #19：NipLock signer support](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19：Forgesworn Heartwood signer](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19：Flotilla Aegis NIP-46 login](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-55：Android Signer](/zh/topics/nip-55/)
