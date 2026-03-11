---
title: "NIP-46：Nostr Connect"
date: 2025-12-17
draft: false
translationOf: /en/topics/nip-46.md
translationDate: 2026-03-11
categories:
  - 签名
  - 协议
---

NIP-46 定义了通过 Nostr 中继进行远程签名的协议。客户端与一个独立的签名器（通常称为 bunker）通信，这样签名密钥可以保存在用户正在使用的应用之外。

## 工作原理

1. 客户端生成一个仅用于 bunker 会话的本地密钥对。
2. 通过 `bunker://` 或 `nostrconnect://` URI 建立连接。
3. 客户端和签名器通过中继交换加密的 kind `24133` 请求和响应事件。
4. 连接后，客户端调用 `get_public_key` 来获取其代签的实际用户公钥。

## 连接方式

- **bunker://** - 签名器发起的连接
- **nostrconnect://** - 客户端通过二维码或深度链接发起的连接

`nostrconnect://` 流程包含一个必需的共享密钥，以便客户端验证第一个响应确实来自预期的签名器。这可以防止简单的连接欺骗。

## 支持的操作

- `sign_event` - 签名任意事件
- `get_public_key` - 从签名器获取用户的公钥
- `nip04_encrypt/decrypt` - NIP-04 加密操作
- `nip44_encrypt/decrypt` - NIP-44 加密操作
- `switch_relays` - 请求签名器提供更新的中继集

许多实现还在设置期间使用权限字符串，如 `sign_event:1` 或 `nip44_encrypt`，以便签名器可以批准有限的范围而非完全访问权限。

## 中继与信任模型

NIP-46 将私钥移出客户端，但并不消除对签名器的信任。签名器可以批准、拒绝或延迟请求，并且能看到客户端请求它执行的每一项操作。中继的选择也很重要，因为协议依赖于请求和响应通过双方都能访问的中继传递。

`switch_relays` 方法的存在是为了让签名器可以随时间将会话迁移到不同的中继集。忽略此方法的客户端在签名器中继偏好变更时可靠性会降低。

---

**主要来源：**
- [NIP-46 规范](https://github.com/nostr-protocol/nips/blob/master/46.md)

**提及于：**
- [Newsletter #1：重要代码变更](/zh/newsletters/2025-12-17-newsletter/#amethyst-android)
- [Newsletter #3：十二月回顾](/zh/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #7：Primal Android 成为完整签名中心](/zh/newsletters/2026-01-07-newsletter/#primal-android-becomes-a-full-signing-hub)
- [Newsletter #15：NDK 协作事件与 NIP-46 超时](/zh/newsletters/2026-03-04-newsletter/#ndk-collaborative-events-and-nip-46-timeout)

**另请参阅：**
- [NIP-55：Android 签名器](/zh/topics/nip-55/)
